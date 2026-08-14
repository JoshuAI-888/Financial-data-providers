# FactSet

## 1. Snapshot
- **Category:** Financial content, analytics & workflow platform, expanding into cloud-native data delivery (Databricks Marketplace) and AI/agentic interfaces (MCP); recently added OMS/IBOR via acquisition.
- **Owner / parent:** FactSet Research Systems Inc., independent public company (NYSE: FDS).
- **HQ / footprint:** Norwalk, Connecticut, US. APAC: Sydney office since 1998, Melbourne office opened 2016; a combined ANZ team of 70+ client support, relationship-management and technical specialists; also runs an annual APAC Buy-Side Forum across Hong Kong, Tokyo, Sydney and Singapore.
- **Initial fit:** Very high as a data/content and AI-delivery layer; moderate (and largely unproven at this buyer's scale) as a full EDM/IBOR system — IBOR/OMS capability is a 2025 bolt-on acquisition (LiquidityBook), not a mature native master.
- **Positioning:** The broadest off-the-shelf multi-asset content catalogue among the two vendors evaluated here, now pushed directly into Databricks and exposed to LLMs via a production MCP suite — best read as a content + AI-interface layer alongside a core IDP, not a replacement for one.

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

## 8. Time-to-value, implementation, managed services & APAC support
FactSet has an established Implementation Services and Managed Services practice and a long-standing (since 1998) Sydney/Melbourne ANZ presence with 70+ dedicated staff, evidenced by two decades of local operating history and regular APAC forums. Specific 30–60 day PoV or 3–6 month foundation timelines for a Databricks-delivered content + MCP + IBOR combination were **not established from public sources** — this needs direct vendor validation given the IBOR/OMS capability is newly integrated.

## 9. Commercials, TCO, exit & vendor viability
FactSet reports strong, transparent subscription economics: Annual Subscription Value (ASV) of $2,405.6M at FY2025 year-end (Aug 2025), rising to $2,450.2M by Q2 FY2026 (+6.7% organic YoY), with 91% annual retention — solid evidence of vendor durability and reinvestment capacity (reflected in the LiquidityBook and AI-suite investment). Platform-vs-content pricing separation, published egress/derived-data terms, and 5-year TCO transparency were **not established from public sources** in this pass.

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

**Provisional 0–5 scores (12 domains):**
- Domain 1 (Investment data mastering): 2.0 (evidence: official docs)
- Domain 2 (Databricks & open architecture): 3.0 (evidence: official docs)
- Domain 3 (Time to value & implementation): 1.5 (evidence: sales/marketing)
- Domain 4 (Data quality & investment operations): 2.5 (evidence: official docs)
- Domain 5 (Public/private total portfolio): 1.0 (evidence: official docs)
- Domain 6 (IBOR & investment modelling): 2.0 (evidence: official docs)
- Domain 7 (AI & agent readiness): 3.0 (evidence: official docs)
- Domain 8 (Data coverage/currency/history): 3.0 (evidence: official docs)
- Domain 9 (Integration & user self-service): 2.0 (evidence: official docs)
- Domain 10 (Governance/security/data rights): 2.5 (evidence: official docs)
- Domain 11 (Commercials/TCO/exit): 2.0 (evidence: official docs)
- Domain 12 (Vendor viability/roadmap/support): 3.0 (evidence: official filings)

**Overall read:** FactSet is best positioned as a strategic **content + AI-interface layer** — its Databricks Marketplace presence and production MCP suite are genuinely ahead of the field for exposing licensed content to LLMs under governed entitlements — but it is not evidenced as a primary IDP: security/entity mastering is concordance-grade rather than golden-record, and its new IBOR/OMS (LiquidityBook) is an unproven, recently-integrated acquisition. Biggest risk for this buyer: relying on FactSet for IBOR or total-portfolio public/private mastering would be buying an M&A integration story, not a proven capability; biggest strength is AI/agent readiness combined with genuinely deep multi-asset content and long-standing ANZ presence.

## 11. Sources
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
