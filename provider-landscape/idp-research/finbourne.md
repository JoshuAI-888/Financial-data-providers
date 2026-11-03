# FINBOURNE

## 1. Snapshot
- **Category:** Investment data management platform with native bi-temporal IBOR/portfolio-accounting engine (LUSID), plus data virtualisation (Luminesce) and an emerging AI layer (Candela AI, MCP).
- **Owner / parent:** Independent, VC-backed. Founded 2016, London. £55m Series B (June 2024, led by Highland Europe and AXA Venture Partners); a further secondary round (led by CommerzVentures and HSBC Ventures) brought total raised to over £100m. Not publicly traded.
- **HQ / footprint:** London HQ; named enterprise clients include Baillie Gifford, LSEG and Northern Trust. APAC/ANZ presence is recent and early-stage — a dedicated Head of Sales for Australia & New Zealand (Marianne Antonicelli) was appointed in October 2025, signalling investment but limited maturity in-region.
- **Initial fit:** High — closest of the three to an IDP purpose-built around a native, bi-temporal IBOR and open APIs, but with an unconfirmed Databricks-specific integration and an unproven ANZ track record.
- **Positioning:** "You bought an IBOR, but did you get one?" — FINBOURNE's core pitch is that most incumbent IBORs are shallow, and LUSID delivers a genuine, near-real-time, bi-temporal book of record with agentic-AI access on top.
- **Recent developments:** 26 Oct 2026: AustralianSuper went live on LUSID as its whole-of-fund investment book of record (first named ANZ production reference); Sep 2026: agents reported in production at OMBA and a ~30-engineer forward-deployed programme launched; LSEG Yield Book embedding (due Q2 2026) not yet confirmed live; no Databricks integration found.

## 2. Investment-domain mastering
LUSID is described as a bi-temporal investment management data platform with native portfolio-accounting capability — security, transaction, holding and position entities are all first-class, accessible through a unified API layer. It supports complex fund structures, share classes, series, partnerships and fund-of-funds, and calculates multi-condition accruals across structures (native to fund accounting). Identifier concordance and explicit ISIN/SEDOL/CUSIP/FIGI mapping are not itemised in public sources but are plausible given the unified security-entity model. EDM+ is offered as an adjacent enterprise-data-management product. Coverage breadth is client-configured (LUSID is a data-management platform the client populates), so "native" data content (e.g. govvies, FX, credit) is less about vendor-supplied datasets and more about the model's ability to represent them — this differs materially from Rimes' vendor-sourced content model.

## 3. Databricks & open architecture
This is FINBOURNE's clearest gap versus its own AI/open-platform narrative: no Databricks-specific partnership, Delta Sharing, or Unity Catalog integration was found in public sources, despite targeted searches. What is evidenced is a general open-API philosophy, SDKs in Python/Java/C#, and Luminesce — a SQL-based data-virtualisation layer that can read and write across LUSID and external sources — plus a cited data-mesh-style integration with Northern Trust's Matrix Data Platform. For a buyer whose architecture principle is explicitly Databricks-first, this needs direct vendor confirmation; treat as not established rather than assumed.

**Nov 2026 re-check:** still no FINBOURNE–Databricks Delta Sharing, Unity Catalog or Marketplace evidence (checked 3 Nov 2026).

## 4. IBOR & investment modelling
This is FINBOURNE's headline strength. LUSID's bi-temporal architecture is designed for point-in-time reconstruction and is positioned explicitly against "IBORs" that are really batch snapshots — FINBOURNE's own thought leadership catalogues the symptoms of a shallow IBOR (stale positions, manual corporate-action posting, reconciliation-by-Excel) that LUSID claims to solve. Intraday/event-driven mechanics are implied by the bi-temporal, near-real-time framing but not itemised with SLA-level detail in public sources.

## 5. Data quality & investment operations
FINBOURNE integrates Taskize for cross-party reconciliation-issue resolution — consolidating emails, messages, attachments and exception data into a single workflow with a "Smart Directory" for routing and stated auditability/traceability. EDM+ addresses enterprise data quality. Explicit four-eyes/override mechanics and tolerance-based price validation are not detailed in public sources.

## 6. Public/private total portfolio
FINBOURNE has a dedicated private-equity offering and "supporting growing private capital funds" content: automated NAV generation, customisable exception dashboards, performance attribution, and managed partner integrations connecting CRM/deal-pipeline tools, portfolio-monitoring tools and fund-admin data. Public and private markets are pitched on one unified platform. However, no specific evidence was found of GP/LP capital-call/distribution waterfall modelling or private-document ingestion/extraction with source traceability — treat those specific capabilities as not established from public sources.

## 7. AI & agent readiness
FINBOURNE announced an MCP integration explicitly built around Anthropic's Claude — "secure, permission-aware AI agents" accessing live investment data, automating workflows and taking real-time action, with every core entity (legal entities, transactions, holdings, positions) and key functions (P&L, chart of accounts, trial balance) exposed via the same unified API layer now extended to MCP. Candela AI is described as a natural-language layer over the whole LUSID ecosystem. This is a genuine, named product announcement (stronger evidence than roadmap talk), but a precise GA date and model-independence beyond the Claude/Anthropic integration were not established from public sources — **treat as early-availability/named-integration rather than confirmed mature GA across all LLM providers.**

**Nov 2026 update:** trade coverage (Sep 2026) relays that OMBA has run FINBOURNE agents in production for six months (data-load checks, reconciliations, valuations, commentary; vendor says 7 clients in production and 30+ out-of-the-box agents) and that FINBOURNE launched a ~30-engineer Forward Deployed Engineering programme on its Candela agentic layer. Both are vendor-originated claims; no named LLM or new model-independence statement. The LSEG Yield Book embedding announced for Q2 2026 has not been confirmed live.

## 8. Time-to-value, implementation, managed services & APAC support
No PoV timelines, implementation-FTE ratios, or connector-onboarding-speed benchmarks were found in public sources. APAC support is real but young: the ANZ sales-lead hire (Oct 2025) indicates FINBOURNE is only now building out regional go-to-market, with no ANZ client reference found publicly.

**Nov 2026 update:** AustralianSuper went live on LUSID as a whole-of-fund investment book of record with a total-portfolio view (FINBOURNE news 26 Oct 2026; Asset Servicing Times 27 Oct 2026; Inserv Insights 26 Oct 2026). This is the first named ANZ production reference; selection date, modules and implementation duration were not disclosed. No NZ client or local office found.

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
- G14 credible APAC+ANZ support: PASS — AustralianSuper live on LUSID (Oct 2026) plus ANZ head of sales (Nov 2026)
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: UNKNOWN
- G17 07:00 validated-portfolio SLA: UNKNOWN
- G18 internal ops retains exception/override control: PARTIAL — Taskize workflow implies client-side control
- G19 institutional security architecture: PARTIAL — institutional clients named, architecture not detailed
- G20 5-yr TCO transparency: FAIL — pricing undisclosed
- G21 critical function not roadmap-dependent: PARTIAL — core IBOR mature; MCP/AI layer newer
- G22 controlled write-back to downstream systems: PARTIAL — Luminesce write-back implied, controls undetailed


**Overall read:** FINBOURNE leads on genuine bi-temporal IBOR depth and on a named, permission-aware MCP/Claude integration that most directly matches the buyer's AI-agent ambitions — but it has no evidenced Databricks-native integration, which cuts against the buyer's core architecture principle, and its ANZ presence is a matter of months old. Biggest risk for this buyer: assuming Databricks openness because of the AI/open-API narrative, when that specific integration is unconfirmed and would need to be proven in diligence.

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- https://www.finbourne.com/finbourne-unlocks-compliant-agentic-ai-for-the-investment-industry-powered-by-mcp/ — FINBOURNE compliant agentic AI via MCP [vendor · Official release note · 2026-08-14 · search-only]
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
- https://www.assetservicingtimes.com/assetservicesnews/industryarticle.php?article_id=18498 — AustralianSuper goes live with total portfolio view on FINBOURNE's platform (Asset Servicing Times; accessed 2026-11-03) [independent · News · 2026-10-27 · opened]
- https://www.inservinsights.net/2026/10/australiansuper-goes-live-on-lusid/ — AustralianSuper goes live on LUSID (Inserv Insights; accessed 2026-11-03) [independent · News · 2026-10-26 · opened]
- https://www.finbourne.com/finbourne-and-lseg-extend-partnership-to-deliver-integrated-fixed-income-analytics/ — FINBOURNE and LSEG extend partnership to deliver integrated fixed income analytics (FINBOURNE; accessed 2026-11-03) [vendor · Official release note · 2025-11-05 · opened]
- https://www.fi-desk.com/yield-book-data-made-available-through-finbournes-lusid/ — Yield Book data made available through Finbourne's LUSID (The DESK; accessed 2026-11-03) [independent · News · 2025-11-06 · opened]
- https://techintelpro.com/news/ai/enterprise-ai/omba-runs-finbourne-agentic-ai-to-cut-ops-burden-by-20 — OMBA runs FINBOURNE agentic AI to cut ops burden by 20% (TechIntelPro; accessed 2026-11-03) [independent · News · 2026-09-11 · opened]
- https://a-teaminsight.com/blog/finbourne-puts-even-more-humans-in-the-loop-to-build-client-confidence-and-business/ — FINBOURNE puts even more humans in the loop... (A-Team Insight; accessed 2026-11-03) [independent · News · 2026-09-14 · opened]
- https://www.summit-group.com/news-and-insights/summit-group-strengthens-channel-islands-fund-services-with-finbourne-technology-investment/ — Summit Group selects Finbourne as strategic fund administration platform partner (Summit Group; accessed 2026-11-03) [independent · Named customer case study · 2026-06 · search-only]
- https://www.finextra.com/pressarticle/102050/finbourne-appoints-marianne-antonicelli-as-head-of-sales-for-australia-and-new-zealand — Finbourne appoints Marianne Antonicelli as head of sales for ANZ (Finextra; accessed 2026-11-03) [vendor · News · 2025-10 · search-only]
- https://www.finbourne.com/news/ — FINBOURNE news listing (items 10 Sep - 26 Oct 2026) (FINBOURNE; accessed 2026-11-03) [vendor · Vendor marketing · 2026-10-26 · opened]
