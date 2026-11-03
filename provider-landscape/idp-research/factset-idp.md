# FactSet

## 1. Snapshot
- **Category:** Financial content, analytics & workflow platform, expanding into cloud-native data delivery (Databricks Marketplace) and AI/agentic interfaces (MCP); recently added OMS/IBOR via acquisition.
- **Owner / parent:** FactSet Research Systems Inc., independent public company (NYSE: FDS).
- **HQ / footprint:** Norwalk, Connecticut, US. APAC: Sydney office since 1998, Melbourne office opened 2016; a combined ANZ team of 70+ client support, relationship-management and technical specialists; also runs an annual APAC Buy-Side Forum across Hong Kong, Tokyo, Sydney and Singapore.
- **Initial fit:** Very high as a data/content and AI-delivery layer; moderate (and largely unproven at this buyer's scale) as a full EDM/IBOR system — IBOR/OMS capability is a 2025 bolt-on acquisition (LiquidityBook), not a mature native master.
- **Positioning:** The broadest off-the-shelf multi-asset content catalogue among the two vendors evaluated here, now pushed directly into Databricks and exposed to LLMs via a production MCP suite — best read as a content + AI-interface layer alongside a core IDP, not a replacement for one.
- **Recent developments:** 25 Aug 2026: FactSet MCP suite announced as live in Google Gemini Enterprise for Financial Services (GA status unstated); 22 Sep 2026: agreed to buy BCC Group; FY2026 organic ASV +7.0%, retention above 95%, 650+ clients engaged with MCP; Databricks MCP Marketplace partner since late 2025.

## 2. Investment-domain mastering
FactSet's mastering story is concordance and crosswalking, not golden-record security/entity/price mastering in the EDM sense. The **Concordance Service** uses a proprietary matching algorithm against FactSet's Entity Master, People, and Symbology databases to resolve client identifiers to FactSet's proprietary IDs (with candidate lists and confidence scores, not an authoritative merge), and the **Symbology API** cross-maps to industry-standard identifiers. Content breadth is genuinely wide: equities, ETFs, fixed income (corporate/government/agency/municipal bonds, terms & conditions, prices, analytics), ownership, mutual funds, and 20+ years of consensus estimates across 19,000+ companies and 90+ countries; multi-asset risk-model coverage spans equity, fixed income, currency and commodity. Private-equity/GP-LP lifecycle mastering is not evidenced. This is native, licensed content delivery with configurable cross-referencing — not operational security-master mastering with survivorship/golden-record governance; point-in-time history depth was not independently confirmed in this research pass.

## 3. Databricks & open architecture
FactSet is the more Databricks-committed of the two vendors: it markets a dedicated **"FactSet via Databricks"** product, has multiple datasets (e.g., FactSet Standardized Economics, FactSet Estimates - Consensus) listed directly on Databricks Marketplace, and is the subject of a Databricks blog post on jointly implementing an enterprise GenAI platform. Databricks Marketplace listings are Delta Sharing-based by Databricks' own architecture, implying share-in-place rather than bulk file replication, though FactSet-specific Unity Catalog integration details and bidirectional (write-back) APIs were not confirmed from public sources. Net: strengthens rather than duplicates a Databricks estate, but the depth of native integration (vs. Databricks-hosted read replicas) needs vendor confirmation in a PoV.

## 4. IBOR & investment modelling
FactSet acquired **LiquidityBook** in February 2025 (~$246.5M) specifically to add order management (OMS) and investment-book-of-record (IBOR) capability, now being integrated into the FactSet Workstation to link research/portfolio construction with order creation, execution and the middle office. This is a genuine IBOR offering, not marketing language — but it is a recent acquisition still being integrated, with no named reference confirming production IBOR use at an asset-owner scale comparable to this buyer, and no evidence yet of proven multi-asset/multi-market (ANZ/Asia) IBOR performance.

## 5. Data quality & investment operations
FactSet operates a **Data as a Service (DaaS)** offering with pipeline quality checks for completeness before data reaches downstream systems, customizable validation rules, and unification of multi-source identifiers into a common security/entity model. **Managed Services** (including "PaSS – Managed Services" and Implementation Services) extend to performance, attribution, risk, reporting and corporate-actions data management. This is real, named data-operations tooling, though evidence of dedicated exception-workflow/reconciliation depth comparable to a core EDM was not established from public sources.

## 6. Public/private total portfolio
This is FactSet's weakest evidenced domain for this buyer's use case. Ownership and mutual-fund reference feeds exist, but no public evidence was found of a unified public+private total-portfolio model, GP/LP fund lifecycle (commitments/calls/distributions/NAV), or private-document extraction comparable to MSCI's PADP. Treat private-markets total-portfolio capability as **not established from public sources** — likely a gap relative to MSCI for this specific requirement.

## 7. AI & agent readiness
FactSet's strongest domain. It markets itself as first to announce a **production-grade MCP server "sans intermediary"** — direct, governed access to FactSet content for LLMs/agentic applications without custom integration — alongside a broader AI-ready suite (unstructured-data MCP, vectorized data API, Event Hub, Intelligent Document Service). A **Portfolio Analytics MCP** was announced as a **limited release** (explicitly not full GA), expanding governed performance/attribution/risk access into agentic workflows. FactSet's published **GenAI Governance and Security Policy** states user prompts/responses are not used to fine-tune or auto-train any LLM, content usage is licensed/entitlement-scoped, and non-curated content is opt-in/opt-out via connectors. **Maturity: Core content MCP marketed as production/GA; Portfolio Analytics MCP explicitly limited release; model-independence and entitlement language present but third-party audit not confirmed.**

**Nov 2026 update:** on 25 Aug 2026 FactSet and Google Cloud announced FactSet's AI-Ready Data MCPs (portfolio analytics, data feeds, fixed income and derivatives, scenario, collateral and bond total-return tools) as live in Gemini Enterprise for Financial Services; GA vs preview was not stated and deployment is via account team. The Portfolio Analytics MCP remains a limited release (26 Jun 2026). On the Q4 FY2026 call (30 Sep 2026) management said 650+ clients were engaged with MCP.

## 8. Time-to-value, implementation, managed services & APAC support
FactSet has an established Implementation Services and Managed Services practice and a long-standing (since 1998) Sydney/Melbourne ANZ presence with 70+ dedicated staff, evidenced by two decades of local operating history and regular APAC forums. Specific 30–60 day PoV or 3–6 month foundation timelines for a Databricks-delivered content + MCP + IBOR combination were **not established from public sources** — this needs direct vendor validation given the IBOR/OMS capability is newly integrated.

## 9. Commercials, TCO, exit & vendor viability
FactSet reports strong, transparent subscription economics: Annual Subscription Value (ASV) of $2,405.6M at FY2025 year-end (Aug 2025), rising to $2,450.2M by Q2 FY2026 (+6.7% organic YoY), with high annual retention (above 95% of ASV in FY2026) — solid evidence of vendor durability and reinvestment capacity (reflected in the LiquidityBook and AI-suite investment). Platform-vs-content pricing separation, published egress/derived-data terms, and 5-year TCO transparency were **not established from public sources** in this pass.

**Nov 2026 update:** FY2026 (to 31 Aug 2026, reported 30 Sep 2026): revenue $2,476.3M, organic ASV $2,568.2M (+7.0%), annual ASV retention above 95% (the earlier 91% figure used a different basis and is superseded). Sanoke Viswanathan has been CEO since Sep 2025. FactSet agreed to acquire BCC Group (real-time data infrastructure) on 22 Sep 2026. Renewals are moving to 3+ year enterprise agreements; AI pricing is a subscription base with consumption tiers, described as early. No new Arcesium availability or Databricks news.

## 10. Evidence, maturity & provisional scores

**Hard-gate read (G01–G22):**
- G01 (native multi-asset incl. PE): PARTIAL — deep equities/FI/estimates, PE lifecycle unconfirmed
- G02 (security/entity/price mastering): PARTIAL — concordance/crosswalk, not golden-record master
- G03 (intraday position/near-real-time txns): PARTIAL — new IBOR/OMS via LiquidityBook, unproven at scale
- G04 (5yr history + point-in-time): PARTIAL — deep history confirmed, point-in-time unconfirmed
- G05 (IDP-as-master, Databricks consumes): PARTIAL — content flows in, mastering role unclear
- G06 (open/native Databricks integration): PASS — dedicated product + marketplace listings
- G07 (bidirectional API): PARTIAL — strong read APIs, write-back unconfirmed
- G08 (business users self-extend model): UNKNOWN — not established from public sources
- G09 (buyer uses own LLMs): PASS — MCP marketed as model-independent, LLM-agnostic access
- G10 (permission-aware MCP/agent interface): PASS — production MCP server, governed access
- G11 (field-level provenance/lineage/override/audit): PARTIAL — DaaS quality checks, no field-level audit confirmed
- G12 (full export on exit): UNKNOWN — not established from public sources
- G13 (AI/LLM rights governable): PASS — published GenAI Governance & Security Policy
- G14 (credible APAC/ANZ support): PASS — 70+ staff, Sydney (1998)/Melbourne (2016)
- G15 (30–60 day PoV): UNKNOWN — not established from public sources
- G16 (3–6 month production foundation): UNKNOWN — not established from public sources
- G17 (07:00 validated-portfolio SLA): UNKNOWN — not established from public sources
- G18 (ops retains exception/override control): PARTIAL — DaaS customizable checks, override depth unclear
- G19 (institutional security architecture): PARTIAL — inferred from scale, not directly documented
- G20 (5-yr TCO transparency): UNKNOWN — not established from public sources
- G21 (critical function not roadmap-dependent): PARTIAL — Portfolio Analytics MCP and IBOR both recent/limited-release
- G22 (controlled write-back to downstream systems): UNKNOWN — not established from public sources


**Overall read:** FactSet is best positioned as a strategic **content + AI-interface layer** — its Databricks Marketplace presence and production MCP suite are genuinely ahead of the field for exposing licensed content to LLMs under governed entitlements — but it is not evidenced as a primary IDP: security/entity mastering is concordance-grade rather than golden-record, and its new IBOR/OMS (LiquidityBook) is an unproven, recently-integrated acquisition. Biggest risk for this buyer: relying on FactSet for IBOR or total-portfolio public/private mastering would be buying an M&A integration story, not a proven capability; biggest strength is AI/agent readiness combined with genuinely deep multi-asset content and long-standing ANZ presence.

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- https://www.factset.com/lp/model-context-protocol — FactSet MCP server — model-independent [vendor · Official docs · 2026-08-14 · search-only]
- https://www.databricks.com/blog/mcp-powered-financial-ai-workflows-databricks — Databricks MCP Marketplace — FactSet [vendor · Platform-standards docs · 2026-08-14 · search-only]
- https://www.factset.com/marketplace/catalog/product/factset-via-databricks — dedicated FactSet-via-Databricks product page (accessed 2026-08-14)
- https://www.factset.com/marketplace/catalog/product/model-context-protocol — FactSet Core MCP Server product page (accessed 2026-08-14)
- https://www.factset.com/marketplace/catalog/product/portfolio-analytics-mcp — Portfolio Analytics MCP, limited release (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-meets-demand-ai-ready-data-first-announce-mcp-sans — first production MCP server announcement (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-expands-model-context-protocol-suite-portfolio-analytics — MCP suite expansion to portfolio analytics (accessed 2026-08-14)
- https://www.databricks.com/blog/factset-genai — Databricks blog on FactSet enterprise GenAI platform (accessed 2026-08-14)
- https://marketplace.databricks.com/details/c6c9e6f7-f302-42be-83f5-36e278a69d06/FactSet_FactSet-Standardized-Economics — FactSet dataset on Databricks Marketplace (accessed 2026-08-14)
- https://marketplace.databricks.com/details/b8e65142-68df-4aca-912f-1063b5c08555/FactSet_FactSet-Estimates-Consensus — FactSet estimates dataset on Databricks Marketplace (accessed 2026-08-14)
- https://www.factset.com/marketplace/catalog/product/factset-concordance-service — Concordance Service (entity/security crosswalk) (accessed 2026-08-14)
- https://developer.factset.com/api-catalog/symbology-api — Symbology API for identifier resolution (accessed 2026-08-14)
- https://www.factset.com/marketplace/catalog/product/investment-book-of-record-ibor — FactSet IBOR product page (accessed 2026-08-14)
- https://www.globenewswire.com/news-release/2025/02/10/3023260/7768/en/FactSet-Acquires-LiquidityBook.html — LiquidityBook acquisition for OMS/IBOR (accessed 2026-08-14)
- https://www.sec.gov/Archives/edgar/data/1013237/000101323725000036/fdspressrelease-factsetacq.htm — SEC filing on LiquidityBook acquisition (accessed 2026-08-14)
- https://www.factset.com/news/factset-launches-data-as-a-service-to-streamline-data-management-in — Data as a Service (DaaS) quality/validation capability (accessed 2026-08-14)
- https://www.factset.com/marketplace/catalog/product/pass-managed-services — Managed Services offering (accessed 2026-08-14)
- https://www.factset.com/GenAI-Governance-and-Security — GenAI governance, AI data-use rights policy (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-celebrates-20-years-australia — 20 years in Australia, Sydney office since 1998 (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-expands-australia-operations-opens-office-melbourne — Melbourne office opening 2016 (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-unveils-2025-apac-buy-side-forum-shaping-future-finance — APAC Buy-Side Forum Sydney/HK/Tokyo/Singapore (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-reports-results-fourth-quarter-and-fiscal-2025 — FY2025 ASV $2,405.6M, retention 91% (accessed 2026-08-14)
- https://investor.factset.com/news-releases/news-release-details/factset-reports-results-first-quarter-fiscal-2026 — Q2 FY2026 ASV $2,450.2M (accessed 2026-08-14)
- https://www.googlecloudpresscorner.com/2026-08-25-FactSets-AI-Ready-MCP-Integration-Now-Live-in-Gemini-Enterprise-for-Financial-Services — FactSet's AI-Ready MCP Integration Now Live in Gemini Enterprise for Financial Services (Google Cloud Press Corner (FactSet/Google release); accessed 2026-11-03) [vendor · Vendor marketing · 2026-08-25 · opened]
- https://www.googlecloudpresscorner.com/2026-06-30-FactSet-Announces-Strategic-Partnership-with-Google-Cloud-to-Bring-Advanced-AI-to-Financial-Intelligence — FactSet Announces Strategic Partnership with Google Cloud to Bring Advanced AI to Financial Intelligence (Google Cloud Press Corner; accessed 2026-11-03) [vendor · Vendor marketing · 2026-06-30 · opened]
- https://www.sec.gov/Archives/edgar/data/0001013237/000162828026063888/fdsq42026earningsrelease.htm — FactSet Q4 and FY2026 earnings release (Form 8-K exhibit) (SEC EDGAR; accessed 2026-11-03) [independent · Official filings · 2026-09-30 · opened]
- https://www.webull.com/news/15672802116584448 — FactSet (FDS) Q4 2026 Earnings Call Transcript (Webull (transcript aggregator); accessed 2026-11-03) [independent · News · 2026-09-30 · opened]
- https://investor.factset.com/news-releases/news-release-details/factset-announces-ceo-succession-plan — FactSet Announces CEO Succession Plan (FactSet IR; accessed 2026-11-03) [vendor · Official release note · 2025-06-03 · opened]
- https://www.cutterassociates.com/insights/newsmaker-a-first-look-at-the-factset-arcesium-collaboration-for-the-buy-side — Newsmaker: A First Look at the FactSet-Arcesium Collaboration for the Buy-Side (Cutter Associates; accessed 2026-11-03) [independent · Independent research · 2025-12-12 · opened]
- https://finviz.com/news/394194/factset-marks-a-new-era-in-enterprise-real-time-market-data-as-it-acquires-bcc-group-international — FactSet Marks a New Era in Enterprise Real-Time Market Data as It Acquires BCC Group International (Finviz (GlobeNewswire release repost); accessed 2026-11-03) [vendor · Official release note · 2026-09-22 · opened]
- https://www.arcesium.com/press-release/factset-and-arcesium-debut-tech-to-unite-front-middle-and-back-office-workflows — FactSet and Arcesium Debut Tech To Unite Front, Middle, and Back Office Workflows (Arcesium; accessed 2026-11-03) [vendor · Official release note · 2025-12-03 · opened]
- https://www.thetradenews.com/msci-veteran-joins-factset-to-head-up-business-in-australia-and-new-zealand/ — MSCI veteran joins FactSet to head up business in Australia and New Zealand (The TRADE; accessed 2026-11-03) [independent · News · 2020-11-16 · opened]
- https://a-teaminsight.com/blog/factset-pushes-deeper-into-enterprise-market-data-infrastructure-with-bcc-group-acquisition/?brand=madi — FactSet pushes deeper into enterprise market data infrastructure with BCC Group acquisition (A-Team Insight; accessed 2026-11-03) [independent · News · 2026-09 · search-only]
