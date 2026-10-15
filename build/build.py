"""Build dist/index.html from src/blueprint.src.html.

Icons: Microsoft's official Power Platform icons are downloaded at build time from
download.microsoft.com and embedded as data URIs. They are not committed to this repo.
Terms of use: https://learn.microsoft.com/power-platform/guidance/icons

  python build/build.py           full build; caches the icon pack in .cache/icons
  python build/build.py --check   validate only; no network, placeholder icons, no output
"""
import base64
import io
import os
import pathlib
import re
import sys
import urllib.request
import xml.dom.minidom
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
if os.name == "nt" and not str(ROOT).startswith("\\\\?\\"):
    ROOT = pathlib.Path("\\\\?\\" + str(ROOT))  # allow paths longer than 260 chars on Windows
SRC = ROOT / "src" / "blueprint.src.html"
OUT = ROOT / "dist" / "index.html"
CACHE = ROOT / ".cache" / "icons"
ICON_ZIP = ("https://download.microsoft.com/download/498606aa-6d27-4f13-aa5c-1401078c153b/"
            "Power-Platform-icons-scalable.zip")

# placeholder key -> file name inside Microsoft's icon pack
ICONS = {
    "pp": "PowerPlatform_scalable.svg",
    "apps": "PowerApps_scalable.svg",
    "auto": "PowerAutomate_scalable.svg",
    "pages": "PowerPages_scalable.svg",
    "dv": "Dataverse_scalable.svg",
    "aib": "AIBuilder_scalable.svg",
    "cs": "CopilotStudio_scalable.svg",
}
PLACEHOLDER = "data:image/svg+xml;base64," + base64.b64encode(
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" rx="20" fill="#888"/></svg>'
).decode()

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
"""
BASE_STYLE = "\n<style>html{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"


def fetch_icons():
    CACHE.mkdir(parents=True, exist_ok=True)
    if any(not (CACHE / f).exists() for f in ICONS.values()):
        print("Downloading Microsoft Power Platform icon pack...")
        data = urllib.request.urlopen(ICON_ZIP, timeout=60).read()
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for name in z.namelist():
                base = name.rsplit("/", 1)[-1]
                if base in ICONS.values():
                    (CACHE / base).write_bytes(z.read(name))
    uris = {}
    for key, fname in ICONS.items():
        path = CACHE / fname
        if not path.exists():
            sys.exit(f"Icon {fname} is missing from Microsoft's pack. Update ICONS in build/build.py.")
        raw = path.read_bytes()
        if re.search(rb"<script|javascript:|\bon\w+\s*=", raw, re.I):
            sys.exit(f"Icon {fname} contains script content; refusing to embed it.")
        uris[key] = "data:image/svg+xml;base64," + base64.b64encode(raw).decode()
    return uris


# Approximate glyph widths (in em) for the page fonts: Segoe UI / system sans, Cascadia Mono.
SVG_TEXT = {"s-t": (12, "sans", 1.0), "s-h": (12.5, "sans", 1.05), "s-m": (11, "sans", 1.0), "s-c": (10.5, "mono", 1.0)}


def _text_width(s, size, family, weight):
    if family == "mono":
        return len(s) * size * 0.65  # 0.6em glyphs + 0.05em letter-spacing
    em = 0.0
    for ch in s:
        if ch.isupper() or ch in "@%&MW":
            em += 0.63
        elif ch.isdigit():
            em += 0.55
        elif ch == " ":
            em += 0.27
        elif ch in ".,:;'|!il·()[]":
            em += 0.28
        else:
            em += 0.51
    return em * size * weight


def lint_diagrams(body):
    """Warn when SVG text likely overflows its box or collides with an icon."""
    warnings = []
    for idx, svg in enumerate(re.findall(r"<svg.*?</svg>", body, re.S), 1):
        doc = xml.dom.minidom.parseString(
            svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1).encode())
        root = doc.documentElement
        if not root.getAttribute("viewBox"):
            continue  # inline logos and icons, not diagrams
        vx, _, vw, _ = (float(v) for v in root.getAttribute("viewBox").split())
        num = lambda el, a: float(el.getAttribute(a) or 0)  # noqa: E731
        rects = [(num(r, "x"), num(r, "y"), num(r, "width"), num(r, "height"))
                 for r in doc.getElementsByTagName("rect") if r.getAttribute("width")]
        images = [(num(i, "x"), num(i, "y"), num(i, "width"), num(i, "height"))
                  for i in doc.getElementsByTagName("image")]
        if vw < 200:
            continue
        for t in doc.getElementsByTagName("text"):
            if t.getAttribute("transform"):
                continue
            s = "".join(n.data for n in t.childNodes if n.nodeType == n.TEXT_NODE)
            size, family, weight = 12, "sans", 1.0
            for c in t.getAttribute("class").split():
                if c in SVG_TEXT:
                    size, family, weight = SVG_TEXT[c]
            x, y = num(t, "x"), num(t, "y")
            w = _text_width(s, size, family, weight)
            anchor = t.getAttribute("text-anchor") or "start"
            left = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
            right, top, bottom = left + w, y - size * 0.75, y + size * 0.2
            mid_y = y - size * 0.35
            boxes = [r for r in rects if r[0] <= x <= r[0] + r[2] and r[1] <= mid_y <= r[1] + r[3]]
            if boxes:
                bx, by, bw, bh = min(boxes, key=lambda r: r[2] * r[3])
                lo, hi = bx + 2, bx + bw - 2
            else:
                lo, hi = vx, vx + vw
            label = f'Diagram {idx}: "{s[:50]}" at ({x:.0f},{y:.0f})'
            if left < lo or right > hi:
                warnings.append(f"{label} is ~{w:.0f}px wide and runs past its box ({lo:.0f}–{hi:.0f}). Shorten it.")
            for ix, iy, iw, ih in images:
                if left < ix + iw and right > ix and top < iy + ih and bottom > iy:
                    warnings.append(f"{label} overlaps the icon at ({ix:.0f},{iy:.0f}). Move the icon or shorten the text.")
    return warnings


def main():
    check = "--check" in sys.argv
    src = SRC.read_text(encoding="utf-8")

    unknown = set(re.findall(r"\{\{IC:(\w+)\}\}", src)) - ICONS.keys()
    if unknown:
        sys.exit(f"Unknown icon keys {sorted(unknown)}. Valid keys: {sorted(ICONS)}")

    icons = {k: PLACEHOLDER for k in ICONS} if check else fetch_icons()
    body = re.sub(r"\{\{IC:(\w+)\}\}", lambda m: icons[m.group(1)], src)

    for i, svg in enumerate(re.findall(r"<svg.*?</svg>", body, re.S), 1):
        try:
            xml.dom.minidom.parseString(
                svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1).encode())
        except Exception as e:  # noqa: BLE001
            sys.exit(f"Inline SVG #{i} is not well-formed: {e}")

    layout = lint_diagrams(body)
    for w in layout:
        print("warning:", w)
    if layout and "--strict" in sys.argv:
        sys.exit(f"{len(layout)} diagram layout warning(s). Fix them or run without --strict.")

    tabs = set(re.findall(r'class="tab"[^>]*data-sheet="(\w+)"', body))
    sheets = set(re.findall(r'<section class="sheet" id="(\w+)"', body))
    if tabs != sheets:
        sys.exit(f"Tabs and sheets don't match. Tabs only: {sorted(tabs - sheets)}; sheets only: {sorted(sheets - tabs)}")

    if check:
        print(f"check ok: {len(sheets)} sheets, {body.count('<svg')} inline SVGs")
        return

    cut = body.index("</style>") + len("</style>")
    page = HEAD + body[:cut] + BASE_STYLE + "</head>\n<body>\n" + body[cut:] + "\n</body>\n</html>\n"
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"built dist/index.html ({len(page) // 1024} KB)")


if __name__ == "__main__":
    main()
