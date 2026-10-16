---
name: microsoft-guidance-refresh
description: Research procedure for architecture-refresh issues. Use when asked to check Microsoft Power Platform, Copilot Studio or Dataverse guidance for changes and update the blueprint. Covers how to search Microsoft Learn through the microsoft-learn MCP server, what counts as a material change, how to map findings to sheets, and how to write the pull request.
---

# Microsoft guidance refresh

## 1. Find the review window

The review window starts at the **later** of:
- the date of the newest `CHANGELOG.md` entry, and
- the date of the most recently **closed** issue labelled `architecture-refresh`. That issue's closing comment lists what was already checked.

Only report changes published or updated after that date. Microsoft Learn pages show an update date at the top.

## 2. Search, then read

Use the `microsoft-learn` MCP server for every checklist item. Search first, then fetch the pages that matter.
Good searches, by sheet:

| Sheet | Searches |
|---|---|
| 02 Environments | "environment groups rules", "Managed Environments new features", "environment routing", "environment strategy" |
| 03 Data policies | "advanced connector policies", "data policies connector classification", "MCP server connector governance", "cross-tenant isolation" |
| 04 ALM | "Pipelines in Power Platform", "Dataverse Git integration", "solution checker enforcement", "Power Apps Test Engine" |
| 05 Credits | "Copilot Credits", "AI Builder credits", "capacity allocation environment", "pay-as-you-go billing policy", "auto-claim licensing" |
| 06 Reporting | "Power Platform inventory", "admin center data export", "Power Platform advisor", "CoE Starter Kit" |
| 07 Security | "Copilot Studio security governance", "Entra Agent ID", "IP firewall Power Platform", "customer-managed key Dataverse", "virtual network support" |
| 10 Scenarios | "GitHub Copilot harness admin controls", "Copilot Credits allocation environment group rule", "agent monthly consumption limit", "advanced connector policies custom connectors", "billing policy cost allocation" |
| Roadmap | "Power Platform release plan", "Copilot Studio release plan" |

Message-center posts aren't on Learn. Read them through `https://mc.merill.net` and search for Power Platform,
Copilot Studio, Dataverse or AI Builder. Note the MC number and dates.

If a host is blocked, write that in the PR description or the issue comment. Never fill the gap from memory.

## 3. Decide what is material

**Update the page for:**
- a feature reaching GA, entering preview, or being retired or renamed
- a changed date, limit, quota or price unit (e.g. credits per pack)
- new or changed Microsoft guidance that contradicts the blueprint
- a deadline on the page that has now passed. Remove or reword it.

**Don't update for:** wording edits on Learn, new tutorials, UI moves with no change in capability, third-party opinion.

## 4. Record evidence before editing

Build this table first. It goes into the PR description unchanged:

| # | Change | Sheet / element | Source (URL, page date or MC id) |
|---|---|---|---|

Every row needs a source. If two sources disagree, use the newer Microsoft one, and on the page say
"confirm in your tenant" in a `.panel.note`.

## 5. Edit

- Follow the `blueprint-design-system` and `blueprint-diagrams` skills.
- Update the Sources sheet (`id="src"`) with any new URLs, and its "as of" date.
- Bump the revision: x.y → x.(y+1) for content updates. Change it in the app bar, footer and `CHANGELOG.md`.
- Run `python build/build.py --check --strict`.

## 6. Report

Copilot always works in a pull request, so every refresh ends in one.

- **Changes found:** title the PR `Architecture refresh YYYY-MM-DD: <short summary>`. Its description holds the evidence table and a short "not changed" list of the sources you checked.
- **Nothing material:** make no file changes. Title the PR `Architecture refresh YYYY-MM-DD: no material changes` and list the review window and sources checked. The refresh workflow closes no-change PRs and their issues automatically.
