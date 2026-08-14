# Databricks Marketplace (Delta Sharing)

## 1. Snapshot
- **Owner/parent:** Databricks Inc. (private, San Francisco, CA). Positioning: an "open marketplace for data, analytics and AI assets" built on the open Delta Sharing protocol and Unity Catalog governance — Databricks pitches it as vendor-neutral distribution (recipients need not run Databricks), unlike single-cloud data exchanges (AWS Data Exchange, Snowflake Marketplace).
- **Coverage:** Traditional capital-markets data/analytics vendors (FactSet, S&P Global Market Intelligence, S&P Global Commodity Insights, LSEG, Moody's, Nasdaq, ICE Data Services, Morningstar, Dun & Bradstreet, Cotality, Bloomberg B-PIPE, Arcesium), plus alternative/geospatial data (SafeGraph, YipitData) and, since late 2025, an "MCP Marketplace" sub-catalog where the same vendors publish Model Context Protocol servers alongside raw Delta Sharing tables so AI agents can query live data in addition to bulk datasets.
- **Free tier:** The marketplace listing/browsing itself is free (no Databricks account needed to browse; a free workspace/trial is needed to request access). Many listings are "free samples" or free-to-list metadata/reference datasets; most financial-data-provider products are paid and gated behind the vendor's own commercial agreement — Databricks does not itself charge for the sharing mechanism.
- **Pricing model & ranges:** Delta Sharing bills the *provider* for storage of the shared data; the *recipient* pays only their own compute to query it — Databricks charges no data-transfer or platform fee for the exchange itself. Actual dataset price is set by each provider (subscription, per-seat, usage-based, or "contact for pricing"); Databricks compute is separately billed in DBUs (~US$0.07–US$0.91/DBU-hour depending on tier/cloud) if the recipient processes the data inside Databricks.

## 2. Coverage
- **Tier-1 market/reference data & analytics:** FactSet (estimates/consensus, fundamentals), LSEG (formerly Refinitiv — pricing, curves, MCP server for real-time content), S&P Global Market Intelligence (Marketplace Workbench, "Professionals" data, MCP server), S&P Global Commodity Insights, Moody's (600M+ company records, credit ratings, research via MCP), Nasdaq (incl. Nasdaq eVestment), ICE Data Services, Morningstar, Bloomberg (B-PIPE market data feed).
- **Credit, commercial & property intelligence:** Dun & Bradstreet (580M+ business records via Delta Sharing), Cotality (formerly CoreLogic — property/mortgage intelligence), Arcesium (post-trade/portfolio data infrastructure).
- **Alternative / geospatial data:** SafeGraph (places/foot-traffic), YipitData (web-scraped consumer/alt-data panels), plus assorted ESG, ratings and index providers listed under Databricks' "Financial Services" marketplace category.
- **MSCI**: appears in Databricks partner/ISV ecosystem material but no confirmed dedicated Marketplace *data* listing was found in this research pass (unverified — treat as a gap, not a confirmed listing).

## 3. Datasets
- Market data domains reachable: EOD and intraday pricing/quotes (via provider feeds like B-PIPE, LSEG, ICE), fundamentals and estimates/consensus (FactSet, S&P Capital IQ-style data), credit ratings and research (Moody's), commercial/business registry records (D&B), property and mortgage data (Cotality), consumer/alt-data panels (YipitData), foot-traffic/POI geospatial data (SafeGraph), and macro/commodity data (S&P Global Commodity Insights). No public-equity filings/EDGAR-specific product was identified as a discrete Marketplace listing.
- Delivery format is Delta tables (Parquet under the hood) queryable via Spark/SQL, or — for the newer MCP listings — a live tool-call interface rather than a bulk table, so "datasets" increasingly means both static tables and callable real-time endpoints from the same provider.

## 4. APIs & technical integration
- **Delta Sharing (data products):** open, REST-based protocol; recipients get a credential file (`.share`) and connect with any Delta Sharing client (Python `delta-sharing` library, Spark, Power BI, pandas) — no Databricks account required for "open" sharing. Databricks-to-Databricks sharing uses Unity Catalog identity federation instead of tokens, working across clouds/regions.
- **Databricks Marketplace UI:** consumer browses/requests listings from `marketplace.databricks.com` or in-workspace Marketplace UI; provider approves access, then the dataset appears as a read-only Unity Catalog catalog in the recipient's workspace (for UC-enabled workspaces) or via direct Delta Sharing token (for non-UC/external consumers).
- **MCP Marketplace listings (new, 2025–2026):** vendors (LSEG, S&P Global, Moody's, Dun & Bradstreet, Cotality) publish MCP servers discoverable and deployable from the same Marketplace UI; these run inside Databricks (via Agent Bricks / Databricks Apps) and are called by agents using standard MCP tool-call semantics rather than bulk SQL queries — positioned as the "live-query" counterpart to static Delta Sharing tables.
- Auth: Unity Catalog governs row/column access and audit logging for UC-native shares; MCP listings add per-tool authorization/consent scoping on top of UC.

## 5. Enabling technology
- **Delta Sharing:** open-source protocol (originated at Databricks, donated to Linux Foundation) for sharing live data without copying it — recipient queries the provider's storage directly (or a mirrored copy), so updates propagate without re-export/ETL.
- **Unity Catalog:** centralized metastore providing fine-grained governance (row/column-level ACLs), cross-workspace/cross-cloud lineage, and audit trail for every share — this is what lets Databricks claim compliance-grade provenance for regulated financial data.
- **MCP (as of the "MCP Marketplace" launch):** Databricks added MCP server hosting/governance (via Agent Bricks) on top of Unity Catalog so the same governance model (ACLs, lineage, audit) that applies to tables now also wraps agent tool calls into vendor data.
- Governance/security posture: no data replication required for Delta Sharing (reduces copy sprawl/attack surface); provider retains control of underlying storage; recipient compute is fully separate from provider compute (no shared cluster risk).

## 6. Customer / user feedback
- Governance praised: practitioners on peer-review sites report Unity Catalog "resolved a long-standing governance headache" by centralizing cross-workspace access control and automated lineage, seen as valuable for compliance-heavy use cases like financial data (PeerSpot/G2-style aggregated reviews, 2026).
- Platform value cited: independent ROI studies (cited by Databricks and repeated in review aggregators) claim 417–482% 3-year ROI with 4–6 month payback for the broader Databricks platform, though this reflects the platform generally, not the Marketplace specifically.
- Cost predictability flagged as a pain point: DBU-based consumption pricing (~US$0.15–0.91/DBU cited across tiers) makes budgeting harder for variable workloads — a caveat that carries over to any compute-heavy use of shared financial datasets.
- Complexity: reviewers note a real learning curve (Spark/Unity Catalog concepts: metastores, catalogs, external locations) before governance benefits are realized — relevant since Milford-style users evaluating this channel would need Databricks platform familiarity, not just API-key access.

## 7. Edge & positioning
- **Leads on:** cross-cloud, no-copy live data sharing with enterprise-grade governance (Unity Catalog lineage/ACLs); breadth of tier-1 vendor participation (FactSet, LSEG, S&P Global, Moody's, ICE, Morningstar) in one catalog; increasingly offers both bulk historical tables *and* live agentic (MCP) access from the same vendor listing.
- **Lags on:** pricing opacity (provider sets price, often "contact for pricing"; Databricks compute billed separately in DBUs); requires a Databricks/Unity-Catalog-capable environment to get full governance benefit; not a low-friction/self-serve API-key channel like a typical financial-data REST API — onboarding involves data-sharing agreements per vendor.
- **Best-for:** enterprises already standardized on Databricks/lakehouse architecture wanting governed, auditable access to multiple tier-1 financial-data vendors without building bespoke ETL per vendor; not well suited to a lightweight prototype or a single analyst wanting quick API access (FMP-style REST APIs remain simpler for that).

## 8. Provenance
- https://www.databricks.com/product/delta-sharing — Delta Sharing product overview, pricing model (accessed 2026-08-14)
- https://docs.databricks.com/en/marketplace/get-started-consumer-open.html — consumer onboarding, open vs UC sharing (accessed 2026-08-14)
- https://www.databricks.com/blog/2022/06/28/introducing-databricks-marketplace-an-open-marketplace-for-all-data-and-ai-assets.html — Marketplace launch announcement (accessed 2026-08-14)
- https://www.databricks.com/blog/mcp-marketplace-brings-real-time-intelligence-agentic-applications — MCP Marketplace launch, vendor list (accessed 2026-08-14)
- https://www.databricks.com/blog/mcp-powered-financial-ai-workflows-databricks — financial-services MCP partners (LSEG, FactSet, Nasdaq, Moody's, D&B, Cotality, S&P Global, Arcesium) (accessed 2026-08-14)
- https://marketplace.databricks.com/details/b8e65142-68df-4aca-912f-1063b5c08555/FactSet_FactSet-Estimates-Consensus — FactSet Estimates listing (accessed 2026-08-14)
- https://marketplace.databricks.com/provider/bb123ba0-f713-4a39-8c51-2daca088d1de/SP-Global-Market-Intelligence — S&P Global Market Intelligence provider page (accessed 2026-08-14)
- https://marketplace.databricks.com/details/9f22a80f-1107-4d59-a069-6c618c9a577a/SP-Global-Market-Intelligence_SP-Global-MCP-Server — S&P Global MCP Server listing (accessed 2026-08-14)
- https://www.lseg.com/en/solutions/ai-finance-solutions/updates/lseg-launches-mcp-server-databricks-marketplace-ai-ready-access — LSEG MCP server on Marketplace (accessed 2026-08-14)
- https://www.databricks.com/blog/2021/09/21/how-yipitdata-extracts-insights-from-alternative-data-using-delta-lake.html — YipitData alt-data on Delta Lake/Marketplace (accessed 2026-08-14)
- https://www.g2.com/products/databricks/reviews — practitioner review aggregation, cost/complexity themes (accessed 2026-08-14)
