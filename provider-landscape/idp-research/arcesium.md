# Arcesium

## 1. Snapshot
- **Category:** End-to-end investment operations & data platform — data mastering (Aquata), unified books-of-record/investment lifecycle (Opterra/UBOR), and, from Feb 2026, portfolio/order management (via the Limina acquisition). Broadest, most "second proprietary estate"-shaped of the three.
- **Owner / parent:** Spun out of the D. E. Shaw group in 2015 (originally a joint venture with Blackstone Multi-Asset Investing); J.P. Morgan later made a strategic investment. Independently operated today, still serving D. E. Shaw's own funds among its client base. Not publicly traded.
- **HQ / footprint:** New York HQ, with US and European operations; opened its **first on-the-ground Asia office in Hong Kong in January 2026** to serve "growing APAC client demand." No Australia/NZ office or named ANZ client reference found in public sources.
- **Initial fit:** Moderate-to-High — deepest, most concretely evidenced end-to-end capability (data + IBOR/ABOR + ops + now OMS), but the architecture pulls toward Arcesium becoming the analytical/operational estate itself rather than a thin mastering layer feeding Databricks, which cuts against the buyer's stated principle.
- **Positioning:** "Deploy any strategy at scale with unified investment data" — a single connected platform (Aquata + Opterra + Limina) spanning data governance through to order execution and books of record, serving hedge funds, institutional asset managers, private-markets firms and banks with over $6tn in gross AUM serviced.

## 2. Investment-domain mastering
Aquata is explicitly pitched as a self-service data platform with "hundreds of connectors" that ingests, validates, harmonises and distributes data into a single source of truth. Data-quality rules include security-master consistency and entity-data uniqueness, and instrument identifiers, pricing and reference data are normalised on ingestion (identifier concordance implied, though not itemised by standard ISIN/SEDOL/CUSIP/FIGI). Opterra is separately described as including "a world-leading security master" combined with UBOR, reconciliations, performance, reg reporting and treasury modules. Point-in-time/bitemporal history is claimed in the RFI evidence baseline but was not independently corroborated in public search results — treat as vendor-asserted, not yet triangulated.

## 3. Databricks & open architecture
This is Arcesium's clearest gap relative to Rimes: no Databricks-specific partnership, Delta Sharing, or Unity Catalog integration was found in public sources despite targeted search. The primary "open" interface evidenced is the Aquata MCP server (see Section 7), which is an AI/agent access layer, not a data-sharing/open-lakehouse integration. For a Databricks-first buyer this needs explicit vendor confirmation; absent that, Arcesium reads as more likely to want to be the analytical estate than to plug into one.

## 4. IBOR & investment modelling
Opterra's **UBOR® engine** unifies traditional IBOR and ABOR functions into one dataset, generating returns and a double-sided general ledger from a single unified thread of data across multi-asset, multi-currency portfolios — a genuinely differentiated, named capability (most competitors keep IBOR/ABOR separate). Public commentary notes rising client demand for real-time position/cash views, which Arcesium's own materials associate with UBOR, but explicit intraday-engine SLAs, trade-date-vs-settlement-date handling specifics, and projected-position mechanics were not independently detailed in public sources.

## 5. Data quality & investment operations
Aquata has a dedicated "financial data quality management" capability with configurable rules (security-master consistency, entity uniqueness). Opterra's reconciliation suite includes multiple asset-class-specific reconciliation types plus an "any-versus-any" catch-all. Arcesium's heritage (spun out to deliver D. E. Shaw's own middle/back-office capability to other managers) means a significant managed-service/outsourcing component is embedded in its model — evidenced further by its role supporting Neuberger Berman's asset-based-financing operations — which raises the same operational-control question as Rimes: exception handling may sit partly with Arcesium's own ops teams rather than purely the buyer's.

## 6. Public/private total portfolio
Concrete and comparatively strong evidence here. Opterra explicitly extends coverage to private credit and cryptocurrency alongside equities, fixed income, derivatives and FX. Aquata's AI-powered unstructured-data processing has a **named, working example**: extracting loan-lifecycle events (drawdowns, paydowns, interest repricing, fees) from loan notices across 15+ counterparties, reducing hours of manual validation to minutes of exception-based review — a genuine private-credit document-ingestion capability with a specific, quantified outcome. A dedicated private-markets solutions page exists, though GP/LP fund-structure, capital-call/distribution-waterfall and NAV modelling specifics were not independently confirmed in accessible public sources (the page itself could not be fetched due to sandbox egress blocking).

## 7. AI & agent readiness
Arcesium launched an **Aquata MCP server** enabling investment firms to connect "any enterprise AI tool" to their governed data foundation using natural language, via domain-aware schemas, to query data and run transformation workloads. This is a meaningfully model-independent framing (stronger than a single-LLM integration) and a named, recent product feature — evidence class is official product announcement, but as a newly unveiled AI suite it should be treated as **early-stage/recently-GA rather than long-proven**; per-agent identity/entitlement granularity, field-level citations, and write-approval controls were not itemised in public sources.

## 8. Time-to-value, implementation, managed services & APAC support
"Hundreds of connectors" and a self-service framing suggest faster dataset onboarding than a bespoke build, but no PoV timelines or FTE ratios were found. Managed-service delivery is a core, longstanding part of Arcesium's model (consistent with its D. E. Shaw services heritage). APAC support is real but very new: the Hong Kong office (opened Jan 2026) is explicitly Arcesium's **first on-the-ground Asia presence**; no Australia/NZ office or client reference was found.

## 9. Commercials, TCO, exit & vendor viability
Revenue model is subscription-based SaaS plus professional/consulting fees; no pricing tiers or export/exit terms are published. Vendor viability is the strongest of the three on scale and backing: $6tn+ gross AUM serviced (figures range $5.2tn–$6.4tn across recent disclosures), $860bn–$1.2tn sell-side capital balances, backed by D. E. Shaw and a J.P. Morgan strategic investment, and — most tellingly — made its **first-ever acquisition** (Limina, a Stockholm P/OMS vendor, Feb 2026) to build a unified front-to-back platform, signalling active capital deployment and roadmap execution, but also fresh integration risk from a very recent, unproven acquisition.

## 10. Evidence, maturity & provisional scores

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL — equities/fixed income/derivatives/FX/private credit/crypto evidenced; explicit PE/GP-LP modelling unconfirmed
- G02 security+entity+price mastering: PASS — explicit in both Aquata and Opterra
- G03 intraday position/price + near-real-time txns: PARTIAL — demand/positioning language, not itemised SLA
- G04 5yr history + point-in-time: PARTIAL — bitemporal claimed in RFI baseline, not independently corroborated
- G05 IDP-as-master while Databricks consumes: UNKNOWN — no Databricks evidence found
- G06 open/native Databricks integration: FAIL — not established from public sources
- G07 bidirectional API: PARTIAL — MCP supports query + transformation workloads; general API write-back undetailed
- G08 business users extend model w/o vendor coding: UNKNOWN
- G09 buyer can use own LLMs: PASS — MCP explicitly framed as connecting "any enterprise AI tool"
- G10 permission-aware MCP/agent interface: PASS — Aquata MCP server explicit
- G11 field-level provenance/lineage/override/audit: PARTIAL — "governed, trusted" data foundation language, no field-level detail
- G12 full export on exit: UNKNOWN
- G13 AI/LLM data-use rights governable: UNKNOWN
- G14 credible APAC+ANZ support: PARTIAL — first Asia office just opened (HK, Jan 2026), no ANZ presence
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: UNKNOWN
- G17 07:00 validated-portfolio SLA: UNKNOWN
- G18 internal ops retains exception/override control: PARTIAL — managed-service heritage raises control-balance question
- G19 institutional security architecture: PARTIAL — serves major hedge funds/banks, architecture not detailed
- G20 5-yr TCO transparency: FAIL — pricing undisclosed
- G21 critical function not roadmap-dependent: PARTIAL — Aquata/UBOR mature; MCP AI suite and Limina P/OMS integration both very recent
- G22 controlled write-back to downstream systems: PARTIAL — MCP "transformation workloads" imply write, controls undetailed

**Provisional domain scores (0–5, capped per evidence class; no PoV run, cap 4, reach 4 only with a named comparable production reference):**
- Domain 1 Investment data mastering: 3.0 (evidence: official docs)
- Domain 2 Databricks & open architecture: 1.0 (evidence: capability not evidenced)
- Domain 3 Time to value & implementation: 1.5 (evidence: sales/marketing)
- Domain 4 Data quality & investment operations: 3.0 (evidence: official docs)
- Domain 5 Public/private total portfolio: 3.0 (evidence: official docs, named quantified use case)
- Domain 6 IBOR & investment modelling: 3.0 (evidence: official docs)
- Domain 7 AI & agent readiness: 3.0 (evidence: official product announcement, recent)
- Domain 8 Data coverage/currency/history: 2.5 (evidence: official docs, breadth implied not itemised)
- Domain 9 Integration & user self-service: 3.0 (evidence: official docs — "self-service" framing)
- Domain 10 Governance/security/data rights: 2.5 (evidence: official docs)
- Domain 11 Commercials/TCO/exit: 1.0 (evidence: undisclosed)
- Domain 12 Vendor viability/roadmap/support: 3.0 (evidence: official docs/press — scale, backing, acquisition)

**Overall read:** Arcesium is the most complete end-to-end platform of the three — genuine UBOR (unified IBOR/ABOR), strong private-credit document extraction with a quantified named result, model-independent MCP, and the deepest balance-sheet backing — but it has no evidenced Databricks-native integration and its architecture (now widened further by the Limina P/OMS acquisition) points toward becoming a second proprietary operational estate, the exact outcome the buyer's principle seeks to avoid. Biggest risk for this buyer: strong domain capability could become an architectural liability if Arcesium is adopted as an operating platform rather than a governed mastering layer feeding Databricks; APAC/ANZ support is unproven (first Asia office only opened Jan 2026, no Australia/NZ presence found).

## 11. Sources
- https://www.arcesium.com/institutional-asset-managers — institutional asset manager positioning (accessed 2026-08-14)
- https://www.arcesium.com/private-markets-managers-investors — private markets solutions page (accessed 2026-08-14; page could not be fetched due to sandbox egress block, referenced via search index only)
- https://www.arcesium.com/aquata-data-platform — Aquata data platform overview (accessed 2026-08-14)
- https://www.arcesium.com/aquata-data-platform/data-quality-for-investment-firms — Aquata data-quality rules (accessed 2026-08-14)
- https://www.arcesium.com/press-release/arcesium-unveils-new-suite-of-ai-features-in-aquata — Aquata MCP server and unstructured-data AI announcement (accessed 2026-08-14)
- https://a-teaminsight.com/blog/arcesium-aquata-update-deploys-ai-to-give-purpose-to-extracted-data/ — loan-lifecycle extraction use case detail (accessed 2026-08-14)
- https://www.arcesium.com/opterra — Opterra platform overview (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20240716886450/en/Arcesium-Unveils-Opterra-Investment-Lifecycle-Management-Platform-Empowering-Investment-Firms-to-Drive-Operational-Alpha — Opterra/UBOR launch, July 2024 (accessed 2026-08-14)
- https://www.arcesium.com/what-we-do/ubor/ — UBOR (unified IBOR/ABOR) engine description (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20260202733930/en/Arcesium-Acquires-Limina-to-Deliver-a-Unified-Front-to-Back-Investment-Platform — Limina P/OMS acquisition, Feb 2026 (accessed 2026-08-14)
- https://www.arcesium.com/press-release/arcesium-opens-hong-kong-office-to-support-growing-apac-client-demand — first Asia office, Jan 2026 (accessed 2026-08-14)
- https://www.institutionalinvestor.com/article/2bsvb8jnbwq7gyv2s2cjk/portfolio/d-e-shaw-spin-off-arcesium-brings-precision-to-posttrade-analysis — D. E. Shaw origin/spin-off history (accessed 2026-08-14)
- https://www.swfinstitute.org/news/77082/j-p-morgan-invests-in-d-e-shaw-backed-arcesium — J.P. Morgan strategic investment (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20250115179753/en/Arcesium-Provides-Technology-to-Support-Neuberger-Bermans-Specialty-Finance-Asset-Based-Financing-Operations — managed-service client example (accessed 2026-08-14)
