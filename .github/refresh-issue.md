Weekly review of Microsoft guidance for the Power Platform Enterprise Blueprint. Follow `.github/copilot-instructions.md`.

## 1. Check these sources for changes since the last `CHANGELOG.md` entry

**Environments & governance (sheets 01, 02)**
- [ ] https://learn.microsoft.com/power-platform/guidance/adoption/environment-strategy
- [ ] https://learn.microsoft.com/power-platform/admin/environment-groups
- [ ] https://learn.microsoft.com/power-platform/admin/managed-environment-overview
- [ ] https://learn.microsoft.com/power-platform/admin/default-environment-routing
- [ ] https://learn.microsoft.com/power-platform/admin/managed-governance

**Data policies (sheet 03)**
- [ ] https://learn.microsoft.com/power-platform/guidance/adoption/dlp-strategy
- [ ] Advanced connector policies (ACP) on Microsoft Learn: status, scope, custom-connector support
- [ ] https://learn.microsoft.com/power-platform/admin/cross-tenant-restrictions

**ALM (sheet 04)**
- [ ] Pipelines in Power Platform and Dataverse Git integration on Microsoft Learn

**Credits, licensing & FinOps (sheet 05)**
- [ ] https://learn.microsoft.com/power-platform/admin/pay-as-you-go-overview
- [ ] https://learn.microsoft.com/power-platform/admin/pay-as-you-go-usage-costs
- [ ] Copilot Credits, AI Builder retirement and capacity allocation (Microsoft Learn + message center)
- [ ] https://learn.microsoft.com/power-platform/admin/auto-claim-licensing

**Reporting (sheet 06)**
- [ ] Power Platform inventory and data export on Microsoft Learn
- [ ] CoE Starter Kit status: https://learn.microsoft.com/power-platform/guidance/coe/starter-kit

**Security & agents (sheets 07, 08)**
- [ ] https://learn.microsoft.com/microsoft-copilot-studio/admin-use-entra-agent-identities
- [ ] https://learn.microsoft.com/power-platform/architecture/reference-architectures/secure-access-azure-resources
- [ ] Copilot Studio governance and security on Microsoft Learn

**Roadmap signals**
- [ ] Power Platform and Copilot Studio release plans: https://learn.microsoft.com/power-platform/release-plan/
- [ ] Microsoft 365 message center posts tagged Power Platform or Copilot Studio (mirror: https://mc.merill.net)
- [ ] Icon updates: https://learn.microsoft.com/power-platform/guidance/icons

## 2. Update

- [ ] Edit `src/blueprint.src.html` only where a source shows a material change: a new or retired feature, a date, a limit, a renamed capability, or changed Microsoft guidance.
- [ ] Re-check any dated warnings on the page (for example "Act now" banners) and remove ones that have passed.
- [ ] Run `python build/build.py --check`.
- [ ] Bump the revision and add a `CHANGELOG.md` entry.

## 3. Report

- [ ] Open **one** pull request. In its description, list each change with its source URL.
- [ ] If nothing material changed, don't open a PR. Comment on this issue with the sources you checked, then close it.
