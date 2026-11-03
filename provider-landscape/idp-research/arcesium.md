# Arcesium

## 1. Snapshot
- **Category:** End-to-end investment operations & data platform — data mastering (Aquata), unified books-of-record/investment lifecycle (Opterra/UBOR), and, from Feb 2026, portfolio/order management (via the Limina acquisition). Broadest, most "second proprietary estate"-shaped of the three.
- **Owner / parent:** Spun out of the D. E. Shaw group in 2015 (originally a joint venture with Blackstone Multi-Asset Investing); J.P. Morgan later made a strategic investment. Independently operated today, still serving D. E. Shaw's own funds among its client base. Not publicly traded.
- **HQ / footprint:** New York HQ, with US and European operations; opened its **first on-the-ground Asia office in Hong Kong in January 2026** to serve "growing APAC client demand." No Australia/NZ office or named ANZ client reference found in public sources.
- **Initial fit:** Moderate-to-High — deepest, most concretely evidenced end-to-end capability (data + IBOR/ABOR + ops + now OMS), but the architecture pulls toward Arcesium becoming the analytical/operational estate itself rather than a thin mastering layer feeding Databricks, which cuts against the buyer's stated principle.
- **Positioning:** "Deploy any strategy at scale with unified investment data" — a single connected platform (Aquata + Opterra + Limina) spanning data governance through to order execution and books of record, serving hedge funds, institutional asset managers, private-markets firms and banks with over $6tn in gross AUM serviced.
- **Recent developments:** 20 May 2026: launched Arcesium Intelligence (100+ pre-built agents, Agent Studio, multi-model on Amazon Bedrock) for existing clients, GA status unstated; Aquata MCP server since Dec 2025; no shipped FactSet joint product, Databricks data-sharing or ANZ presence as of 3 Nov 2026.

## 2. Investment-domain mastering
Aquata is explicitly pitched as a self-service data platform with "hundreds of connectors" that ingests, validates, harmonises and distributes data into a single source of truth. Data-quality rules include security-master consistency and entity-data uniqueness, and instrument identifiers, pricing and reference data are normalised on ingestion (identifier concordance implied, though not itemised by standard ISIN/SEDOL/CUSIP/FIGI). Opterra is separately described as including "a world-leading security master" combined with UBOR, reconciliations, performance, reg reporting and treasury modules. Point-in-time/bitemporal history is claimed in the RFI evidence baseline but was not independently corroborated in public search results — treat as vendor-asserted, not yet triangulated.

## 3. Databricks & open architecture
This is Arcesium's clearest gap relative to Rimes: no Databricks-specific partnership, Delta Sharing, or Unity Catalog integration was found in public sources despite targeted search. The primary "open" interface evidenced is the Aquata MCP server (see Section 7), which is an AI/agent access layer, not a data-sharing/open-lakehouse integration. For a Databricks-first buyer this needs explicit vendor confirmation; absent that, Arcesium reads as more likely to want to be the analytical estate than to plug into one.

**Nov 2026 correction:** Databricks' MCP blog (4 Dec 2025) lists Arcesium among partners offering MCP services; the August 'launch partner' wording came from a LinkedIn post, not Databricks. No Delta Sharing or Unity Catalog integration is documented (checked 3 Nov 2026).

## 4. IBOR & investment modelling
Opterra's **UBOR® engine** unifies traditional IBOR and ABOR functions into one dataset, generating returns and a double-sided general ledger from a single unified thread of data across multi-asset, multi-currency portfolios — a genuinely differentiated, named capability (most competitors keep IBOR/ABOR separate). Public commentary notes rising client demand for real-time position/cash views, which Arcesium's own materials associate with UBOR, but explicit intraday-engine SLAs, trade-date-vs-settlement-date handling specifics, and projected-position mechanics were not independently detailed in public sources.

## 5. Data quality & investment operations
Aquata has a dedicated "financial data quality management" capability with configurable rules (security-master consistency, entity uniqueness). Opterra's reconciliation suite includes multiple asset-class-specific reconciliation types plus an "any-versus-any" catch-all. Arcesium's heritage (spun out to deliver D. E. Shaw's own middle/back-office capability to other managers) means a significant managed-service/outsourcing component is embedded in its model — evidenced further by its role supporting Neuberger Berman's asset-based-financing operations — which raises the same operational-control question as Rimes: exception handling may sit partly with Arcesium's own ops teams rather than purely the buyer's.

## 6. Public/private total portfolio
Concrete and comparatively strong evidence here. Opterra explicitly extends coverage to private credit and cryptocurrency alongside equities, fixed income, derivatives and FX. Aquata's AI-powered unstructured-data processing has a **named, working example**: extracting loan-lifecycle events (drawdowns, paydowns, interest repricing, fees) from loan notices across 15+ counterparties, reducing hours of manual validation to minutes of exception-based review — a genuine private-credit document-ingestion capability with a specific, quantified outcome. A dedicated private-markets solutions page exists, though GP/LP fund-structure, capital-call/distribution-waterfall and NAV modelling specifics were not independently confirmed in accessible public sources (the page itself could not be fetched due to sandbox egress blocking).

## 7. AI & agent readiness
Arcesium launched an **Aquata MCP server** enabling investment firms to connect "any enterprise AI tool" to their governed data foundation using natural language, via domain-aware schemas, to query data and run transformation workloads. This is a meaningfully model-independent framing (stronger than a single-LLM integration) and a named, recent product feature — evidence class is official product announcement, but as a newly unveiled AI suite it should be treated as **early-stage/recently-GA rather than long-proven**; per-agent identity/entitlement granularity, field-level citations, and write-approval controls were not itemised in public sources.

**Nov 2026 update:** on 20 May 2026 Arcesium announced **Arcesium Intelligence**, an agentic AI platform embedded in Opterra and Aquata with 100+ pre-configured agents (NAV review, P&L explanation, portfolio and data-quality monitoring), an Agent Studio for client-built agents and an orchestration layer over Arcesium's investment ontology. It is described as available to existing clients; GA vs preview is not stated. Firms are said to choose their own model, deployed on Amazon Bedrock. MCP is not part of it (the Aquata MCP server shipped 15 Dec 2025), and neither release describes per-agent entitlements, so 'permission-aware' is a vendor-governance claim rather than documented mechanics.

## 8. Time-to-value, implementation, managed services & APAC support
"Hundreds of connectors" and a self-service framing suggest faster dataset onboarding than a bespoke build, but no PoV timelines or FTE ratios were found. Managed-service delivery is a core, longstanding part of Arcesium's model (consistent with its D. E. Shaw services heritage). APAC support is real but very new: the Hong Kong office (opened Jan 2026) is explicitly Arcesium's **first on-the-ground Asia presence**; no Australia/NZ office or client reference was found.

## 9. Commercials, TCO, exit & vendor viability
Revenue model is subscription-based SaaS plus professional/consulting fees; no pricing tiers or export/exit terms are published. Vendor viability is the strongest of the three on scale and backing: $6tn+ gross AUM serviced (figures range $5.2tn–$6.4tn across recent disclosures), $860bn–$1.2tn sell-side capital balances, backed by D. E. Shaw and a J.P. Morgan strategic investment, and — most tellingly — made its **first-ever acquisition** (Limina, a Stockholm P/OMS vendor, Feb 2026) to build a unified front-to-back platform, signalling active capital deployment and roadmap execution, but also fresh integration risk from a very recent, unproven acquisition.

**Nov 2026 update:** the FactSet–Arcesium partnership (3 Dec 2025) still has no shipped joint product or availability date; no ownership, funding or pricing change found.

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
- G10 permission-aware MCP/agent interface: PARTIAL — Aquata MCP exists but no per-agent entitlement mechanics are documented (re-read Nov 2026) (Nov 2026)
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


**Overall read:** Arcesium is the most complete end-to-end platform of the three — genuine UBOR (unified IBOR/ABOR), strong private-credit document extraction with a quantified named result, model-independent MCP, and the deepest balance-sheet backing — but it has no evidenced Databricks-native integration and its architecture (now widened further by the Limina P/OMS acquisition) points toward becoming a second proprietary operational estate, the exact outcome the buyer's principle seeks to avoid. Biggest risk for this buyer: strong domain capability could become an architectural liability if Arcesium is adopted as an operating platform rather than a governed mastering layer feeding Databricks; APAC/ANZ support is unproven (first Asia office only opened Jan 2026, no Australia/NZ presence found).

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- https://www.databricks.com/blog/mcp-powered-financial-ai-workflows-databricks — Databricks MCP Marketplace — Arcesium launch partner [vendor · Platform-standards docs · 2026-08-14 · search-only]
- https://www.globenewswire.com/news-release/2025/12/03/3198703/7768/en/FactSet-and-Arcesium-Debut-Tech-To-Unite-Front-Middle-and-Back-Office-Workflows-for-Asset-Owners-and-Managers.html — FactSet–Arcesium partnership [vendor · Official release note · 2026-08-14 · search-only]
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
- https://www.businesswire.com/news/home/20260520686508/en/ — Arcesium Launches Comprehensive AI Platform to Operationalize Agentic AI for Institutional Investment (BusinessWire (Arcesium PR); accessed 2026-11-03) [vendor · Vendor marketing · 2026-05-20 · opened]
- https://ibsintelligence.com/ibsi-news/arcesium-launches-ai-platform-for-enterprise-data-management/ — Arcesium launches AI platform for enterprise data management (IBS Intelligence; accessed 2026-11-03) [independent · News · 2026-05-22 · opened]
- https://a-teaminsight.com/briefs/arcesium-adds-ai-led-arcesium-intelligence-to-platform/ — Arcesium adds AI-led Arcesium Intelligence to platform (A-Team Insight; accessed 2026-11-03) [independent · News · 2026-05-20 · opened]
- https://www.businesswire.com/news/home/20251215394851/en — Arcesium Unveils New Suite of AI Features in Aquata to Help Institutional Investors Scale Their AI Strategies (BusinessWire (Arcesium PR); accessed 2026-11-03) [vendor · Official release note · 2025-12-15 · opened]
- https://www.businesswire.com/news/home/20260202733930/en/ — Arcesium Acquires Limina to Deliver a Unified Front-to-Back Investment Platform (BusinessWire (Arcesium PR); accessed 2026-11-03) [vendor · Official release note · 2026-02-02 · search-only]
- https://www.arcesium.com/press-release/factset-and-arcesium-debut-tech-to-unite-front-middle-and-back-office-workflows — FactSet and Arcesium Debut Tech to Unite Front, Middle, and Back Office Workflows (Arcesium; accessed 2026-11-03) [vendor · Official release note · 2025-12-03 · opened]
- https://www.globenewswire.com/news-release/2025/12/03/3198703/0/en/FactSet-and-Arcesium-Debut-Tech-To-Unite-Front-Middle-and-Back-Office-Workflows-for-Asset-Owners-and-Managers.html — same release (GlobeNewswire (FactSet PR); accessed 2026-11-03) [vendor · Official release note · 2025-12-03 · search-only]
- https://kyodonewsprwire.jp/release/202601132314 — Arcesium Opens Hong Kong Office to Support Growing APAC Client Demand (Kyodo News PR Wire (Arcesium PR); accessed 2026-11-03) [vendor · Vendor marketing · 2026-01-13 · search-only]
- https://www.businesswire.com/news/home/20260407557995/en — Feynman Point Asset Management Selects Arcesium to Deliver Reconciliation Across Digital and Traditional Assets (BusinessWire (Arcesium PR); accessed 2026-11-03) [vendor · Vendor marketing · 2026-04-07 · opened]
- https://www.cutterassociates.com/insights/newsmaker-a-first-look-at-the-factset-arcesium-collaboration-for-the-buy-side — Newsmaker: A First Look at the FactSet-Arcesium Collaboration (Cutter Associates; accessed 2026-11-03) [independent · Independent research · 2025-12-12 · opened]
