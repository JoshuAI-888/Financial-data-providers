# Rimes

## 1. Snapshot
- **Category:** Managed data services / enterprise data management (EDM) — benchmark & index data, security master, RegTech; not a portfolio-accounting/IBOR platform.
- **Owner / parent:** Independent operating company; acquired by Rothschild & Co (via its Five Arrows merchant-banking arm) in April 2024, taking over from EQT Partners (owner since Feb 2020). Two PE/ownership changes in six years.
- **HQ / footprint:** Dual HQ London/New York; states offices across Europe, the Americas and Asia Pacific, but no specific ANZ (Australia/NZ) office or client reference was found in public sources.
- **Initial fit:** Moderate — best fit is as a benchmark/index/security-master **data supplier into** the buyer's Databricks estate, not as the IDP's investment-modelling or IBOR layer.
- **Positioning:** A 30-year benchmark and index data specialist that has broadened into managed security-master, entity and portfolio data services, now pitching itself as the "AI-ready data" on-ramp for Databricks.

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

## 9. Commercials, TCO, exit & vendor viability
Pricing is undisclosed, as is standard for the vendor category — contact-for-quote only. No public information on data export/portability terms, derived-data rights, or egress charges from Rimes itself. Vendor viability is underpinned by scale (serves 60 of the top 100 global asset managers and 9 of the top 10 asset servicers, supporting >US$75tn AUM) but the two ownership changes since 2020 (EQT → Rothschild/Five Arrows) are a moderate roadmap-continuity risk to flag.

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

**Provisional domain scores (0–5, capped per evidence class; no PoV run, cap 4, reach 4 only with a named comparable production reference):**
- Domain 1 Investment data mastering: 3.0 (evidence: official docs)
- Domain 2 Databricks & open architecture: 3.0 (evidence: official docs/press release)
- Domain 3 Time to value & implementation: 1.5 (evidence: sales/marketing)
- Domain 4 Data quality & investment operations: 2.5 (evidence: official docs)
- Domain 5 Public/private total portfolio: 1.0 (evidence: marketing mention only)
- Domain 6 IBOR & investment modelling: 0.5 (evidence: capability not evidenced)
- Domain 7 AI & agent readiness: 1.0 (evidence: roadmap)
- Domain 8 Data coverage/currency/history: 3.0 (evidence: official docs)
- Domain 9 Integration & user self-service: 3.0 (evidence: official docs/press release)
- Domain 10 Governance/security/data rights: 2.5 (evidence: official docs)
- Domain 11 Commercials/TCO/exit: 1.0 (evidence: unknown/undisclosed)
- Domain 12 Vendor viability/roadmap/support: 2.5 (evidence: official docs/press release)

**Overall read:** Rimes leads narrowly on the one thing this buyer explicitly wants — a data vendor that plugs into Databricks natively via Delta Sharing without replication — announced concretely in Nov 2025. It is a credible benchmark/index/security-master content and managed-service supplier, not an IDP in the buyer's sense: it has no evidenced IBOR/investment-modelling engine, no private-markets/PE capability, and no Rimes-specific AI/agent interface. Biggest risk for this buyer: treating Rimes as a full IDP would leave IBOR, private-markets mastering and agentic AI entirely unaddressed, and ANZ support is unproven.

## 11. Sources
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
