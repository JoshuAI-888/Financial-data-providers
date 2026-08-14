# FINBOURNE

## 1. Snapshot
- **Category:** Investment data management platform with native bi-temporal IBOR/portfolio-accounting engine (LUSID), plus data virtualisation (Luminesce) and an emerging AI layer (Candela AI, MCP).
- **Owner / parent:** Independent, VC-backed. Founded 2016, London. £55m Series B (June 2024, led by Highland Europe and AXA Venture Partners); a further secondary round (led by CommerzVentures and HSBC Ventures) brought total raised to over £100m. Not publicly traded.
- **HQ / footprint:** London HQ; named enterprise clients include Baillie Gifford, LSEG and Northern Trust. APAC/ANZ presence is recent and early-stage — a dedicated Head of Sales for Australia & New Zealand (Marianne Antonicelli) was appointed in October 2025, signalling investment but limited maturity in-region.
- **Initial fit:** High — closest of the three to an IDP purpose-built around a native, bi-temporal IBOR and open APIs, but with an unconfirmed Databricks-specific integration and an unproven ANZ track record.
- **Positioning:** "You bought an IBOR, but did you get one?" — FINBOURNE's core pitch is that most incumbent IBORs are shallow, and LUSID delivers a genuine, near-real-time, bi-temporal book of record with agentic-AI access on top.

## 2. Investment-domain mastering
LUSID is described as a bi-temporal investment management data platform with native portfolio-accounting capability — security, transaction, holding and position entities are all first-class, accessible through a unified API layer. It supports complex fund structures, share classes, series, partnerships and fund-of-funds, and calculates multi-condition accruals across structures (native to fund accounting). Identifier concordance and explicit ISIN/SEDOL/CUSIP/FIGI mapping are not itemised in public sources but are plausible given the unified security-entity model. EDM+ is offered as an adjacent enterprise-data-management product. Coverage breadth is client-configured (LUSID is a data-management platform the client populates), so "native" data content (e.g. govvies, FX, credit) is less about vendor-supplied datasets and more about the model's ability to represent them — this differs materially from Rimes' vendor-sourced content model.

## 3. Databricks & open architecture
This is FINBOURNE's clearest gap versus its own AI/open-platform narrative: no Databricks-specific partnership, Delta Sharing, or Unity Catalog integration was found in public sources, despite targeted searches. What is evidenced is a general open-API philosophy, SDKs in Python/Java/C#, and Luminesce — a SQL-based data-virtualisation layer that can read and write across LUSID and external sources — plus a cited data-mesh-style integration with Northern Trust's Matrix Data Platform. For a buyer whose architecture principle is explicitly Databricks-first, this needs direct vendor confirmation; treat as not established rather than assumed.

## 4. IBOR & investment modelling
This is FINBOURNE's headline strength. LUSID's bi-temporal architecture is designed for point-in-time reconstruction and is positioned explicitly against "IBORs" that are really batch snapshots — FINBOURNE's own thought leadership catalogues the symptoms of a shallow IBOR (stale positions, manual corporate-action posting, reconciliation-by-Excel) that LUSID claims to solve. Intraday/event-driven mechanics are implied by the bi-temporal, near-real-time framing but not itemised with SLA-level detail in public sources.

## 5. Data quality & investment operations
FINBOURNE integrates Taskize for cross-party reconciliation-issue resolution — consolidating emails, messages, attachments and exception data into a single workflow with a "Smart Directory" for routing and stated auditability/traceability. EDM+ addresses enterprise data quality. Explicit four-eyes/override mechanics and tolerance-based price validation are not detailed in public sources.

## 6. Public/private total portfolio
FINBOURNE has a dedicated private-equity offering and "supporting growing private capital funds" content: automated NAV generation, customisable exception dashboards, performance attribution, and managed partner integrations connecting CRM/deal-pipeline tools, portfolio-monitoring tools and fund-admin data. Public and private markets are pitched on one unified platform. However, no specific evidence was found of GP/LP capital-call/distribution waterfall modelling or private-document ingestion/extraction with source traceability — treat those specific capabilities as not established from public sources.

## 7. AI & agent readiness
FINBOURNE announced an MCP integration explicitly built around Anthropic's Claude — "secure, permission-aware AI agents" accessing live investment data, automating workflows and taking real-time action, with every core entity (legal entities, transactions, holdings, positions) and key functions (P&L, chart of accounts, trial balance) exposed via the same unified API layer now extended to MCP. Candela AI is described as a natural-language layer over the whole LUSID ecosystem. This is a genuine, named product announcement (stronger evidence than roadmap talk), but a precise GA date and model-independence beyond the Claude/Anthropic integration were not established from public sources — **treat as early-availability/named-integration rather than confirmed mature GA across all LLM providers.**

## 8. Time-to-value, implementation, managed services & APAC support
No PoV timelines, implementation-FTE ratios, or connector-onboarding-speed benchmarks were found in public sources. APAC support is real but young: the ANZ sales-lead hire (Oct 2025) indicates FINBOURNE is only now building out regional go-to-market, with no ANZ client reference found publicly.

## 9. Commercials, TCO, exit & vendor viability
Pricing model, platform-vs-content separation, and export/exit terms are not published. Vendor viability is reasonably strong for a Series-B-stage company: >£100m total raised, backing from Highland Europe, AXA Venture Partners, CommerzVentures and HSBC Ventures, and named enterprise references (Baillie Gifford, LSEG, Northern Trust) — but FINBOURNE remains smaller in scale and less commercially battle-tested than Arcesium.

## 10. Evidence, maturity & provisional scores

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL — equities/fixed income/PE evidenced, others unconfirmed
- G02 security+entity+price mastering: PASS — core LUSID capability
- G03 intraday position/price + near-real-time txns: PARTIAL — bi-temporal/near-real-time claimed, not itemised
- G04 5yr history + point-in-time: PASS — bi-temporal architecture designed for this
- G05 IDP-as-master while Databricks consumes: UNKNOWN — no Databricks evidence found
- G06 open/native Databricks integration: FAIL — not established from public sources
- G07 bidirectional API: PASS — LUSID/Luminesce read+write evidenced
- G08 business users extend model w/o vendor coding: PARTIAL — configurable model claimed, not itemised
- G09 buyer can use own LLMs: PARTIAL — Claude/Anthropic confirmed, broader model independence unconfirmed
- G10 permission-aware MCP/agent interface: PASS — explicit MCP + permission-aware agent announcement
- G11 field-level provenance/lineage/override/audit: PARTIAL — bi-temporal audit trail inherent, field-level AI citations unconfirmed
- G12 full export on exit: UNKNOWN
- G13 AI/LLM data-use rights governable: UNKNOWN
- G14 credible APAC+ANZ support: PARTIAL — recent hire only, no ANZ reference
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: UNKNOWN
- G17 07:00 validated-portfolio SLA: UNKNOWN
- G18 internal ops retains exception/override control: PARTIAL — Taskize workflow implies client-side control
- G19 institutional security architecture: PARTIAL — institutional clients named, architecture not detailed
- G20 5-yr TCO transparency: FAIL — pricing undisclosed
- G21 critical function not roadmap-dependent: PARTIAL — core IBOR mature; MCP/AI layer newer
- G22 controlled write-back to downstream systems: PARTIAL — Luminesce write-back implied, controls undetailed

**Provisional domain scores (0–5, capped per evidence class; no PoV run, cap 4, reach 4 only with a named comparable production reference):**
- Domain 1 Investment data mastering: 3.0 (evidence: official docs)
- Domain 2 Databricks & open architecture: 1.5 (evidence: marketing/general open-API claims only)
- Domain 3 Time to value & implementation: 1.5 (evidence: sales/marketing)
- Domain 4 Data quality & investment operations: 2.5 (evidence: official docs/partner integration)
- Domain 5 Public/private total portfolio: 2.0 (evidence: official docs, gaps in specifics)
- Domain 6 IBOR & investment modelling: 3.0 (evidence: official docs/thought leadership)
- Domain 7 AI & agent readiness: 3.0 (evidence: official product announcement)
- Domain 8 Data coverage/currency/history: 2.0 (evidence: client-populated model, not vendor content)
- Domain 9 Integration & user self-service: 2.5 (evidence: official docs/named partner integration)
- Domain 10 Governance/security/data rights: 2.5 (evidence: official docs)
- Domain 11 Commercials/TCO/exit: 1.0 (evidence: undisclosed)
- Domain 12 Vendor viability/roadmap/support: 2.5 (evidence: official docs/press, funding record)

**Overall read:** FINBOURNE leads on genuine bi-temporal IBOR depth and on a named, permission-aware MCP/Claude integration that most directly matches the buyer's AI-agent ambitions — but it has no evidenced Databricks-native integration, which cuts against the buyer's core architecture principle, and its ANZ presence is a matter of months old. Biggest risk for this buyer: assuming Databricks openness because of the AI/open-API narrative, when that specific integration is unconfirmed and would need to be proven in diligence.

## 11. Sources
- https://www.finbourne.com/asset-managers/ — asset-manager positioning (accessed 2026-08-14)
- https://www.finbourne.com/platform/ — platform overview (accessed 2026-08-14)
- https://www.finbourne.com/insight/you-bought-an-ibor-but-did-you-get-one/ — IBOR thought-leadership article, Aug 2026 (accessed 2026-08-14)
- https://www.finbourne.com/finbourne-unlocks-compliant-agentic-ai-for-the-investment-industry-powered-by-mcp/ — MCP/Claude agentic AI announcement (accessed 2026-08-14)
- https://support.lusid.com/docs/candela-ai — Candela AI natural-language layer documentation (accessed 2026-08-14)
- https://www.finbourne.com/who-we-serve/alternative-asset-managers/private-equity/ — private equity offering (accessed 2026-08-14)
- https://www.finbourne.com/resources/private-capital-funds/ — private capital funds support content (accessed 2026-08-14)
- https://www.finbourne.com/fund-accounting/ — fund accounting/NAV/accruals capability (accessed 2026-08-14)
- https://www.taskize.com/finbourne-deploys-taskize-to-resolve-reconciliation-issues/ — Taskize reconciliation/exception workflow integration (accessed 2026-08-14)
- https://www.finbourne.com/finbourne-technology-appoints-marianne-antonicelli-as-head-of-sales-for-australia-and-new-zealand-operations-as-part-of-its-continued-expansion-in-the-region/ — ANZ sales lead appointment, Oct 2025 (accessed 2026-08-14)
- https://avpcap.com/finbourne-raises-55-million-in-series-b-round/ — Series B funding, June 2024 (accessed 2026-08-14)
- https://coverager.com/finbourne-raises-total-funding-to-100-million-following-secondary-round/ — secondary round, total funding >£100m (accessed 2026-08-14)
- https://www.finbourne.com/lseg-london-stock-exchange-group-partners-with-finbourne-to-power-digital-data-program-across-the-business/ — LSEG client reference (accessed 2026-08-14)
- https://www.globaltrading.net/northern-trust-integrates-finbourne-with-its-matrix-data-platform/ — Northern Trust data-mesh integration reference (accessed 2026-08-14)
