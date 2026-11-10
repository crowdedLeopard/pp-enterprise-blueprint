# Changelog

## rev 3.5 · 2026-11-10

**Connector inventory is announced for general availability by 10 November.** Power Platform Inventory captures the connectors and operations used by each resource, supporting deprecated-connector reviews, Premium connector adoption and data-policy scoping. Added to Reporting (sheet 06). Sources: [Power Platform inventory](https://learn.microsoft.com/power-platform/admin/power-platform-inventory) (updated 6 November 2026) and [MC1546312](https://mc.merill.net/message/MC1546312).

## rev 3.4 · 2026-11-09

**New sheet 12, Strategy.** Four tabs: *Line of sight* (each outcome on sheet 00 traced to decisions, controls, measures and sheets, plus how every decision D1–D10 is reversed and at what cost), *If Microsoft changes* (Microsoft's scheduled dates with pre-decided responses, and fourteen platform eventualities with their early signal and owner), *If the organisation changes* (acquisition, divestiture, region changes, funding model, regulation, demand, with the tenant-to-tenant move drawn step by step) and *If something breaks* (credits, storage, regional outage, deletions, restores, admin loss and the refresh workflow itself, with Microsoft's recovery numbers). Sheet 00 gains the strategic intent and principles the sheet aligns to.

**Dated deprecations added, from Microsoft Learn.** Unmanaged developer environments: creation ends 15 Nov 2026, suspended 15 Dec 2026, deleted from 15 Jan 2027; one managed developer environment per user from then on. Dataverse for Teams: creation ends 15 Nov 2026, suspended 15 Sep 2027, decommissioned 30 Oct 2027 unless upgraded. New *Act now* banner, D4 and the coverage KPI reworded, roadmap "Now" and open decisions updated.

**Copilot Managed Runtime (preview).** Routing for it is on in every tenant and can't be turned off; Microsoft keeps a managed default environment group; makers outside the routed security groups can't build its apps. The Copilot Studio *Create apps* path has an on/off switch and security-group scoping in the Microsoft 365 admin center, unlike the GitHub Copilot harness for agents. Added to sheet 02 and Scenario C.

**Verified for this revision:** storage overage lifecycle (85%, T0, T0+30, T0+90; production never disabled), backup retention (7 days; 7–28 for production managed environments, group rule), deleted-environment recovery (7 days, 28 with Dynamics 365 apps), self-service disaster recovery (managed production, region pair, replication lag typically under 15 minutes, not in Brazil or South Africa), tenant-to-tenant moves (self-service, 7-day approval window, up to 24 hours, security groups not migrated).

## rev 3.3 · 2026-11-09

**Logic and date review.** Eleven coherence fixes: Scenario B is now framed as the Phase 3 shape of Zone A (its connector-pack groups add to the 26 on sheet 02) and stays in mixed mode; the Tier 1 promotion trigger matches the dev-environment sharing rule (5) and default-environment limit (20); back-charges apply to approved tenant-pool exceptions and unbudgeted pay-as-you-go, since pool draw is otherwise off; Scenario C production uses Pipelines (Zone A) or CI/CD (Zone R) and the review its zone requires; owner names standardised on Cyber Defense Center; trials excluded from the coverage KPI. All "from 1 November 2026" wording moved to past tense now the date has passed.

**GitHub Copilot harness, re-verified against Microsoft Learn.** Microsoft's FAQ now states outright that no setting turns the harness on or off, confirming Scenario C's premise. Correction: the *Copilot Studio authors* tenant setting is not an access block for the harness (users can enter the experience without a licence), so Gate 1 now relies on environment security groups and Dataverse security roles, and the zero-credit posture is described as the closest thing to a block.

**Self-update repaired.** The refresh workflow had been skipping since 19 Oct because a branch-delete 403 aborted the step that closes finished issues. Tidy steps are now non-fatal, issues open for more than 3 days are closed as stale, completed reviews are logged to `.github/refresh-log.md`, and a missing assignment token fails the run loudly.

## rev 3.2 · 2026-10-16

**Fact-check against Microsoft Learn** (about 69 corrections; disputed claims checked in a browser). Highlights:

- AI Builder: no new or renewed credits from 1 Nov 2026; existing credits are honoured to the end of the contract, then usage falls back to Copilot Credits.
- New warning: managed environments require premium licences for every user, enforced from Feb 2027. This affects D4.
- 28 environment-group rules (not 6). IP firewall, cookie binding and sharing can be applied to whole groups from the Security page.
- Managed personal developer environments are cleaned up after 60 days of inactivity. Routing gives one environment per maker.
- The India geo needs an India-based tenant, so Asia Pacific now uses the Asia geo and Brazil is labelled South America.
- Test Engine deprecated (April 2026), replaced by Playwright. The solution checker blocks critical issues only. Pipelines targets must be managed.
- Endpoint filtering is preview and static-only. Copilot Studio channels, authentication and knowledge are governed by classic data policies (virtual connectors).
- Pay-as-you-go: agent limits are the hard stop, and Process licences and app passes don't apply in pay-as-you-go environments.
- Entra Agent ID covers new agents only; Conditional Access on agent identities is enforced only in Teams.
- CoE Starter Kit status now cited from Microsoft (no longer maintained; repo archived July 2026).

**New sheet 11, Operate:** control layers and catalogue, monitoring freshness ladder and alert catalogue, report pack (native vs lakehouse), monthly cross-charge calendar with back-charge rules and a worked example.

## rev 3.1 · 2026-10-16

New sheet 10, **Governance scenarios**, sourced from Microsoft Learn on 16 October 2026:

- **A · Cross-charge costs.** Billing policies per cost owner, per-environment Copilot Credit allocation with the *Cost controls – Draw from tenant credit pool* group rule, ownership mapping for licences and Dataverse, and a monthly statement. Credits are charged to the environment where an agent runs.
- **B · Different connector sets.** Connector packs as environment groups with advanced connector policy allowlists (including action-level *SomeAllowed*), Entra access packages, and the limits on custom, HTTP and MCP connectors.
- **C · Restrict the GitHub Copilot harness.** Four gates (who, where, what, how much), a posture for each environment class, and daily detection through inventory. No admin on/off switch is documented. All harness usage, including building and testing, is billed in Copilot Credits, and developer and trial environments have been billed since 1 Sep 2026.

## rev 3.0 · 2026-10-15

Initial published template. Sources reviewed as of 15 October 2026, including:

- Tenant environment strategy guidance (Microsoft Learn, updated 12 Oct 2026)
- Advanced connector policies GA (4 June 2026) and the later re-enablement of design-time enforcement
- AI Builder capacity add-ons and seeded credits retiring on 1 Nov 2026, with the move to Copilot Credits
- Entra Agent ID for new Copilot Studio agents (May 2026) and automatic migration (Sept 2026)
- CoE Starter Kit: final major monthly release Feb 2026
