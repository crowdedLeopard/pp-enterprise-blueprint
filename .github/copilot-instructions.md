# Copilot instructions: Power Platform Enterprise Blueprint

This repo is a single-page reference architecture template for governing Microsoft Power Platform
(Power Apps, Power Automate, Copilot Studio, Dataverse) in a large global organisation. It is
published to GitHub Pages from `main`.

## Files

| Path | What it is |
|---|---|
| `src/blueprint.src.html` | **The only file you normally edit.** All sheets, diagrams (inline SVG), tables and text. |
| `build/build.py` | Embeds Microsoft's official icons and validates the page. Writes `dist/index.html`. |
| `.github/refresh-issue.md` | Body of the daily "Architecture refresh" issue (the review checklist). |
| `CHANGELOG.md` | One entry per revision. |

`dist/` and `.cache/` are build output. Never commit them.

## How to validate

```bash
python build/build.py --check --strict
```

It runs offline. `--strict` also fails on diagram layout warnings, such as text running past its box or overlapping an icon. It checks that every inline SVG is well-formed XML, every `{{IC:key}}` icon placeholder
is known, and every tab has a matching sheet. A full build (`python build/build.py`) downloads Microsoft's
icon pack; you don't need it to validate.

## Skills

Use the repository skills in `.github/skills/`:
- `blueprint-design-system`: components, tokens and writing style for any HTML change.
- `blueprint-diagrams`: rules for editing the inline SVG diagrams.
- `microsoft-guidance-refresh`: the research and PR procedure for refresh issues.

## Editing rules

- **Keep it generic.** The reference organisation is fictional. Never add real customer names, tenant IDs,
  people or internal URLs.
- **Facts must be sourced.** Every product fact you add or change (feature names, GA dates, limits, prices,
  retirements) needs a Microsoft Learn page, Microsoft message-center post or official Microsoft blog as
  its source. Add new sources to the Sources sheet (`id="src"`). If a source is unclear or contradictory,
  say so in the page text ("confirm in your tenant") instead of stating it as settled.
- **Diagrams are hand-placed SVG on a grid.** When you change a box's text, keep it inside the box: at
  11px a line fits roughly `box width ÷ 6` characters. Don't move boxes unless you also move the arrows
  that connect to them. Keep the existing CSS classes (`s-box`, `s-g`, `s-a`, `s-r`, `s-acc`, `s-t`, `s-h`,
  `s-m`, `s-c`, `s-ln`, `s-lna`) so both light and dark themes keep working. Never hard-code colours.
- **Icons:** use only `{{IC:pp}}`, `{{IC:apps}}`, `{{IC:auto}}`, `{{IC:pages}}`, `{{IC:dv}}`, `{{IC:aib}}`, `{{IC:cs}}`.
  Don't crop, recolour or distort them (Microsoft's icon terms), and always put the product name near an icon.
- **Keep diagrams and tables consistent.** If a diagram says a zone uses a control, the tables on the
  same sheet must agree, and vice versa.
- **Writing style:** plain, direct sentences. No marketing language. British spelling (organisation,
  licence, optimise), matching the existing text.
- **Revision:** bump the template revision (e.g. `rev 3.0` → `rev 3.1`) in the app bar, footer and
  CHANGELOG for content changes. Update the "as of" date on the Sources sheet.

## Researching Microsoft guidance

- **Search Microsoft Learn first.** Use the `microsoft-learn` MCP server's search and fetch tools for every
  checklist item, including items that have no link. Treat the links in the checklist as starting points,
  not the full scope. Search for what changed: renamed features, new GA or retirement dates, new limits.
- **Message-center posts** aren't on Microsoft Learn. Read them through the mirror at `https://mc.merill.net`.
- **Only these hosts are reachable:** `learn.microsoft.com` (also through the MCP server) and `mc.merill.net`,
  plus GitHub's default allowlist. If a source you need is blocked, say so in the PR or issue comment
  instead of guessing its content.
- Prefer Microsoft Learn over third-party blogs. Use a third-party source only when Microsoft has nothing,
  and label it as third party on the Sources sheet.

## Refresh tasks (issues labelled `architecture-refresh`)

Follow the checklist in the issue. In short: review the listed Microsoft sources for anything that
changed since the last CHANGELOG entry, update the page, run `python build/build.py --check --strict`, add a
CHANGELOG entry, and open one pull request. The PR description must list **each change with the
source URL that justifies it**. If nothing material changed, make no file changes. Title the PR
`Architecture refresh YYYY-MM-DD: no material changes` and list the sources you checked in its
description. The workflow closes no-change PRs and their issues automatically.
