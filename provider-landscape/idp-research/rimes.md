# Rimes

## 1. Snapshot
- **Category:** Managed data services / enterprise data management (EDM) — benchmark & index data, security master, RegTech; not a portfolio-accounting/IBOR platform.
- **Owner / parent:** Independent operating company; acquired by Rothschild & Co (via its Five Arrows merchant-banking arm) in April 2024, taking over from EQT Partners (owner since Feb 2020). Two PE/ownership changes in six years.
- **HQ / footprint:** Dual HQ London/New York; states offices across Europe, the Americas and Asia Pacific, with named ANZ clients Rest (Matrix, selected Apr 2026) and NGS Super (Matrix, c. 2021–22); no ANZ office address confirmed.
- **Initial fit:** Moderate — best fit is as a benchmark/index/security-master **data supplier into** the buyer's Databricks estate, not as the IDP's investment-modelling or IBOR layer.
- **Positioning:** A 30-year benchmark and index data specialist that has broadened into managed security-master, entity and portfolio data services, now pitching itself as the "AI-ready data" on-ramp for Databricks.
- **Recent developments:** Rest (>A$100bn super) selected Rimes Matrix after a competitive procurement (vendor release 15 Apr 2026; go-live not stated); Databricks Delta Sharing partnership (Nov 2025) unchanged; new CEO (Sep 2025) and CRO (Jan 2026); no Rimes MCP found as of 3 Nov 2026.

## 2. Investment-domain mastering
Rimes' core, well-evidenced capability is security, price, entity and benchmark/index mastering — validated, enriched and standardised across ~2,500 datasets from 1,000+ data partners, spanning equities, fixed income, ESG, ETFs, commodities, crypto, real assets and corporate actions (native). A published white paper and its Enterprise Benchmark Solution (EBS) describe security-master consistency, governance and automation as core, native functions. Identifier concordance is implied by "concordance" language in its marketing but not itemised (ISIN/SEDOL/CUSIP/FIGI mapping specifically). No public evidence of native private-equity/private-markets security or entity mastering (GP/LP, fund, portfolio-company structures) — this looks custom/absent rather than native or configurable. Point-in-time/bitemporal history is not explicitly evidenced.

## 3. Databricks & open architecture
This is Rimes' strongest, most concretely evidenced domain for this buyer. On 18 Nov 2025 Rimes announced Managed Data Services natively on the Databricks Data Intelligence Platform via **Delta Sharing**, letting customers "connect to their structured datasets without replication," positioned to complement Databricks Agent Bricks. Rimes frames this as the first phase of a broader interoperability strategy since the 2024 Five Arrows investment. Unity Catalog compatibility, bidirectional/write-back APIs, and CDC/event mechanics are not detailed in public sources.

## 4. IBOR & investment modelling
No public evidence that Rimes provides event-driven or intraday position construction, trade-vs-settlement-date modelling, projected positions or cash/accruals engines. Rimes' own content treats IBOR as a client-side concept it advises on (e.g. sovereign-wealth-fund data-strategy commentary), not a capability it delivers. Treat this domain as largely out of scope for Rimes; it is a data layer, not a books-of-record engine.

## 5. Data quality & investment operations
Rimes combines automation with a vendor-operated managed service: a global team "continuously validates and cross-checks data," monitors pipelines, resolves exceptions, manages provider changes and holds itself to SLAs/KPIs. This is a strength for outsourcing data operations, but it means exception handling and remediation sit with Rimes' own ops team by default, not the buyer's — a governance question for G18 (who retains override control). No public detail on tolerance-based price validation, four-eyes overrides, or reconciliation workflow mechanics.

## 6. Public/private total portfolio
Weak evidence. Marketing copy references coverage of "public and private investment data," but no fund/GP/LP hierarchy, capital-call/distribution/NAV modelling, look-through, or private-document extraction capability was found in public sources. Treat as not established.

## 7. AI & agent readiness
Rimes' AI story is currently anchored entirely to the Databricks Agent Bricks complementarity announced in the Nov 2025 partnership — there is no Rimes-specific MCP, permission-aware agent tool, or per-agent entitlement model evidenced in public sources. A separate 2026 white paper ("Breaking Barriers to the Next Generation of Investment Data Management") discusses industry AI-readiness gaps generally but is not itself a product capability. **Maturity: roadmap-level for agent/MCP interfaces; the Databricks data-access layer itself is GA (Nov 2025).**

## 8. Time-to-value, implementation, managed services & APAC support
Rimes' managed-service delivery model (onboarding, provider-change management, SLA-bound operations) is well evidenced but no PoV timelines, connector counts specific to onboarding speed, or implementation-FTE ratios were found. APAC presence is claimed generically (offices "across... Asia Pacific") but no Australia/NZ office, client reference, or support-desk detail was found — this is a material unknown for the buyer's ANZ base.

**Nov 2026 update:** named ANZ clients now exist — Rest (>A$100bn super fund) selected Rimes Matrix after a competitive procurement for a total portfolio and rebalancing view (vendor release 15 Apr 2026, London/Sydney dateline; go-live not stated) and NGS Super (Matrix, c. 2021–22). Ross Allen has been Head of APAC since Nov 2025. An ANZ office and support-desk detail remain unconfirmed.

## 9. Commercials, TCO, exit & vendor viability
Pricing is undisclosed, as is standard for the vendor category — contact-for-quote only. No public information on data export/portability terms, derived-data rights, or egress charges from Rimes itself. Vendor viability is underpinned by scale (serves 60 of the top 100 global asset managers and 9 of the top 10 asset servicers, supporting >US$75tn AUM) but the two ownership changes since 2020 (EQT → Rothschild/Five Arrows) are a moderate roadmap-continuity risk to flag.

**Nov 2026 update:** Vijay Mayadas (ex-Broadridge) became President & CEO on 17 Sep 2025 and Kieran Kennedy (ex-Snowflake/FactSet) CRO on 6 Jan 2026; Five Arrows ownership unchanged. No Databricks, MCP or pricing news between 14 Aug and 3 Nov 2026.

## 10. Evidence, maturity & provisional scores

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL — broad reference/benchmark data, PE modelling unclear
- G02 security+entity+price mastering: PASS — explicit core product
- G03 intraday position/price + near-real-time txns: FAIL — no evidence, EOD/benchmark-oriented
- G04 5yr history + point-in-time: PARTIAL — deep benchmark history, bitemporal not confirmed
- G05 IDP-as-master while Databricks consumes: PASS — explicit via Delta Sharing, no replication
- G06 open/native Databricks integration: PASS — announced Nov 2025
- G07 bidirectional API: UNKNOWN — not detailed
- G08 business users extend model w/o vendor coding: UNKNOWN
- G09 buyer can use own LLMs: UNKNOWN — Databricks-side flexibility implied, not Rimes-specific
- G10 permission-aware MCP/agent interface: FAIL — no Rimes-specific tool found
- G11 field-level provenance/lineage/override/audit: PARTIAL — SLA/KPI managed service, no field-level detail
- G12 full export on exit: UNKNOWN
- G13 AI/LLM data-use rights governable: UNKNOWN
- G14 credible APAC+ANZ support: PARTIAL — general APAC claim, no ANZ specifics
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: UNKNOWN
- G17 07:00 validated-portfolio SLA: UNKNOWN
- G18 internal ops retains exception/override control: PARTIAL — vendor-managed exception resolution by default
- G19 institutional security architecture: PARTIAL — serves top-tier institutions, not detailed
- G20 5-yr TCO transparency: FAIL — pricing undisclosed
- G21 critical function not roadmap-dependent: PARTIAL — data mastering mature; AI/agent layer roadmap
- G22 controlled write-back to downstream systems: UNKNOWN


**Overall read:** Rimes leads narrowly on the one thing this buyer explicitly wants — a data vendor that plugs into Databricks natively via Delta Sharing without replication — announced concretely in Nov 2025. It is a credible benchmark/index/security-master content and managed-service supplier, not an IDP in the buyer's sense: it has no evidenced IBOR/investment-modelling engine, no private-markets/PE capability, and no Rimes-specific AI/agent interface. Biggest risk for this buyer: treating Rimes as a full IDP would leave IBOR, private-markets mastering and agentic AI entirely unaddressed, and ANZ support is unproven.

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- https://www.rimes.com/rimes-partners-with-databricks-to-deliver-managed-data-services/ — Rimes–Databricks managed data services (Delta Sharing) [vendor · Official release note · 2026-08-14 · search-only]
- https://www.prnewswire.com/news-releases/rimes-partners-with-databricks-to-deliver-managed-data-services-302617480.html — PR Newswire corroboration [independent · News · 2026-08-14 · search-only]
- https://www.rimes.com/rimes-partners-with-databricks-to-deliver-managed-data-services/ — Databricks Delta Sharing partnership announcement (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/rimes-partners-with-databricks-to-deliver-managed-data-services-302617480.html — corroborating press release, same announcement (accessed 2026-08-14)
- https://www.rimes.com/insights/rimes-outlines-approach-to-help-buy-side-conquer-challenge-of-managing-security-master-data/ — security master data white paper (accessed 2026-08-14)
- https://www.rimes.com/solutions/benchmark-and-index-solutions/ — benchmark/index solution and Enterprise Benchmark Solution (accessed 2026-08-14)
- https://www.rimes.com/solutions/data-management/ — data management / managed services description (accessed 2026-08-14)
- https://www.rimes.com/why-rimes/about-us/ — company scale, AUM served, office footprint claims (accessed 2026-08-14)
- https://a-teaminsight.com/blog/rimes-changes-hands-plans-accelerated-expansion-as-five-arrows-completes-acquisition/ — Five Arrows/Rothschild ownership change, April 2024 (accessed 2026-08-14)
- https://eqtgroup.com/news/eqt-invests-in-rimes-the-global-leader-in-managed-data-services-for-financial-institutions-2020-02-03 — prior EQT ownership, Feb 2020 (accessed 2026-08-14)
- https://www.rimes.com/breaking-barriers-to-the-next-generation-of-investment-data-management/ — industry AI-readiness white paper, April 2026 (accessed 2026-08-14)
- https://www.rimes.com/the-data-imperative-how-sovereign-wealth-funds-compete-in-an-information-first-era/ — IBOR discussed as client-side concept, not Rimes product (accessed 2026-08-14)
- https://www.rimes.com/rimes-rest-investment-intelligence-platform-matrix/ — Rest selects Rimes (fetch showed no Databricks mention) (Rimes; accessed 2026-11-03) [vendor · Vendor marketing · 2026-04-15 · opened]
- https://rimes.com/press-releases/rimes-to-acquire-matrix-idm-creating-an-advanced-investment-data-management-solution — Rimes to acquire Matrix IDM (Rimes; accessed 2026-11-03) [vendor · Official release note · 2021 · search-only]
- https://ffnews.com/newsarticle/hiring/rimes-strengthens-global-leadership-team-with-appointment-of-ross-allen-and-bill-blythe/ — Rimes strengthens global leadership team (Ross Allen, Bill Blythe) (FF News (PR syndication); accessed 2026-11-03) [vendor · News · 2025-11-05 · opened]
- https://ffnews.com/newsarticle/hiring/rimes-appoints-vijay-mayadas-as-president-and-chief-executive-officer/ — Rimes appoints Vijay Mayadas as President and CEO (FF News (PR syndication); accessed 2026-11-03) [vendor · News · 2025-09-17 · opened]
- https://www.pulse.bot/fintech/news/rimes-names-ex-snowflake-factset-exec-as-cro-f74166f2-afd6-48bc-881d-21a9a0387d7a — Rimes names ex-Snowflake, FactSet exec as CRO (Pulse; accessed 2026-11-03) [independent · News · 2026-01-06 · opened]
- https://www.finextra.com/pressarticle/91885/ngs-super-australia-inks-contract-with-rimes — NGS Super Australia inks contract with Rimes (Finextra (press article); accessed 2026-11-03) [vendor · News · 2021-22 · opened]
- https://a-teaminsight.com/blog/rimes-opens-ai-lab-to-drive-development-of-ai-enabled-data-driven-workflows/?brand=ati — Rimes opens AI Lab (A-Team Insight; accessed 2026-11-03) [independent · News · 2023-11-28 · opened]
- https://www.databricks.com/blog/mcp-marketplace-brings-real-time-intelligence-agentic-applications — MCP Marketplace (no Rimes mention seen) (Databricks; accessed 2026-11-03) [vendor · Vendor marketing · undated · search-only]
- https://financialit.net/news/infrastructure/rest-selects-rimes-support-portfolio-oversight-and-modernize-investment — Rest Selects Rimes to Support Portfolio Oversight and Modernize Investment Operations (Financial IT; accessed 2026-11-03) [independent · News · 2026-04-15 · opened]
- https://ffnews.com/newsarticle/fintech/rest-selects-rimes-to-support-portfolio-oversight-and-modernize-investment-operations/ — Rest Selects Rimes... (FF News; accessed 2026-11-03) [independent · News · 2026-04-14 · opened]
