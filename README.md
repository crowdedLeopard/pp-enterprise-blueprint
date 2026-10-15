# Power Platform Enterprise Blueprint

A reference architecture template for governing Microsoft Power Platform (Power Apps, Power Automate,
Copilot Studio, Dataverse) in a large global organisation. It has ten sheets, each with a diagram and the
detail behind it: environment strategy, data policies, ALM, credits and FinOps, reporting, security and
the operating model.

**Live page:** https://crowdedleopard.github.io/pp-enterprise-blueprint/

The reference organisation is fictional. Swap in your own values using the parameter table on the Overview sheet.

## How it stays current

```
Monday 06:00 UTC ─► "Architecture refresh" issue ─► Copilot coding agent reviews Microsoft guidance
                                                     │
                     you review & merge ◄── pull request with sourced changes
                            │
                            └─► GitHub Pages redeploys
```

- `.github/workflows/architecture-refresh.yml` opens the weekly issue and assigns it to Copilot.
- `.github/refresh-issue.md` is the checklist of Microsoft sources Copilot reviews. Edit it to change the scope.
- `.github/copilot-instructions.md` holds the editing rules Copilot follows: sourced facts only, keep diagrams aligned, keep it generic.
- `.github/workflows/check.yml` validates every pull request. `pages.yml` deploys on every push to `main`.

## One-time setup

1. **Turn on the Copilot coding agent** for this repository. It needs a Copilot plan that includes the coding agent.
2. **Let Copilot read Microsoft's docs.** *(Done for this repo.)* The agent runs behind a firewall. Under
   *Settings → Copilot → Internet access → Custom allowlist*, `learn.microsoft.com` and `mc.merill.net` are allowed.
   Under *Settings → Copilot → MCP servers*, the Microsoft Learn MCP server gives the agent search:
   ```json
   {"mcpServers": {"microsoft-learn": {"type": "http", "url": "https://learn.microsoft.com/api/mcp", "tools": ["*"]}}}
   ```
3. **Add the assignment token.** Create a fine-grained personal access token for this repo with read access to
   metadata and read/write access to actions, contents, issues and pull requests. Then run:
   ```bash
   gh secret set COPILOT_ASSIGN_TOKEN --repo crowdedLeopard/pp-enterprise-blueprint
   ```
   Paste the token when prompted. Without it, the weekly issue still opens, but you assign it to Copilot by hand.
4. **Approve workflow runs on Copilot's PRs.** GitHub asks for approval before running workflows on PRs opened by Copilot.

## Build locally

```bash
python build/build.py --check   # offline validation
python build/build.py           # writes dist/index.html
```

## Icons and trademarks

Microsoft, Power Platform, Power Apps, Power Automate, Power Pages, Copilot Studio, Dataverse and AI Builder are
trademarks of the Microsoft group of companies. The page embeds Microsoft's official Power Platform icons, which are
downloaded at build time and used under [Microsoft's icon terms](https://learn.microsoft.com/power-platform/guidance/icons)
for architecture documentation. The icon files are not redistributed in this repository. This is not a Microsoft document.
