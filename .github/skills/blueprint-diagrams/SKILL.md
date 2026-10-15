---
name: blueprint-diagrams
description: How to edit or add the hand-drawn inline SVG architecture diagrams in src/blueprint.src.html (sheets PPA-01 to PPA-08). Use whenever a change touches a diagram, such as box text, a new box or arrow, an icon, a legend or a whole new diagram, so it keeps the grid, the theme-aware classes and stays readable.
---

# Blueprint diagrams

Each diagram is a hand-placed inline `<svg>` inside a diagram card. It scales to the card width, so it must read
well at about 1,000 to 1,200 px wide. Draw the mechanism: what flows where, which boundary is crossed, which
control applies. Don't draw a list of names in boxes.

## Card markup

```html
<figure class="diagram">
  <div class="dhead"><span class="dcode">PPA-NN</span><span class="dtitle">What this shows</span>
    <span class="legend"><span><i class="lg"></i>Zone G</span>…</span>
    <button class="expand" type="button">⤢ Expand</button></div>
  <div class="dbody"> <svg …>…</svg> </div>
  <figcaption><b>One-sentence claim.</b> Short explanation. <span class="tap-hint">Tap the diagram to enlarge it.</span></figcaption>
</figure>
```

## SVG rules

- `viewBox="0 0 1200 H"`. Pick H to fit the content. Always set `role="img"` and an `aria-label` that states the diagram's claim in one sentence.
- **No literal colours, no `<style>`, no `<script>`, no `<foreignObject>`.** Style only with these classes:

| Class | Draws |
|---|---|
| `s-band` | lane or band background (`rx="12"`) |
| `s-box` | normal box (`rx="8"`–`10"`) |
| `s-acc` | platform / CoE / highlighted box |
| `s-g` `s-a` `s-r` | Zone G / A / R box |
| `s-frame` + `s-dash` | dashed boundary (e.g. tenant) |
| `s-h` | box title, 12.5px semibold |
| `s-t` | primary label, 12px |
| `s-m` | secondary line, 11px muted |
| `s-c` | mono caption or lane label, 10.5px uppercase; write the text in capitals yourself |
| `s-ca` `s-cg` `s-cA` `s-cr` | add to a text class to colour it accent / G / A / R |
| `s-ln` | connector line · `s-lna` accent flow · `s-lnr` blocked/red · `s-lnm` muted · `s-dash` dashed |

- **Arrowheads:** each SVG defines its own markers with ids unique on the page, e.g. `m9` and `m9a` for diagram 9:
  `<marker id="m9" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="mk" d="M0,0L10,5L0,10z"/></marker>`
  (`mka` = accent, `mkr` = red). Reference them with `marker-end="url(#m9)"`.
- **Icons:** `<image href="{{IC:cs}}" x="…" y="…" width="18" height="18"/>`. Use 16–22 px, and keep the same width and height.
  Put an icon in the top-right corner of a box (x = box right − 26, y = box top + 7) or just left of a title,
  shifting the title right by 24 px. Never let an icon overlap text.

## Layout grid

- Outer margin 10–20 px. Columns and rows use even gaps (8, 10 or 12 px). Text inside a box starts 10–14 px from its left edge.
- Line spacing inside a box: title, then lines every 16–18 px. Box height = padding + lines. Don't leave large empty space.
- **Text budget.** At 11px a box holds roughly `(box width − 24) ÷ 5.6` characters per line; at 12.5px semibold, roughly `÷ 6.7`.
  Shorten the wording rather than shrinking the font. Don't go below 10.5px.
- Arrows run straight or with right-angle bends (`path d="M… H… V…"`), and their ends stop 2–3 px short of the target box so the arrowhead shows.
  Label an arrow with an `s-m` text placed beside it, not on top of it.
- When you move a box, move every arrow and label attached to it.
- Zone colours must match the tables on the same sheet.

## Workflow

1. Find the diagram by its `PPA-NN` code. Read the whole SVG before changing it.
2. Make the smallest change that tells the truth. Prefer editing text over moving geometry.
3. Run `python build/build.py --check --strict`. It fails if any SVG is malformed, any text runs past its box,
   or any text overlaps an icon. Fix every warning.
4. Update the `<figcaption>` and the `aria-label` if the diagram's claim changed.
5. In the pull request, describe which boxes or arrows changed and why, with the source URL.
