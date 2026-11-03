# BlueMatrix

## 1. Snapshot
- **Owner/parent:** BlueMatrix, Inc. Thoma Bravo is the majority owner (strategic growth investment completed 4 Jan 2024). **Founded:** 1999 in New York by Skye Hauptman and Patricia Horotan. **HQ:** Durham, North Carolina, with offices in New York, London, Edinburgh, Auckland and Timisoara. **CEO:** David Nable (named 2026). **Positioning:** research publishing and distribution infrastructure for capital markets. Brokers and independent research firms author and distribute on it, and buy-side firms consume aggregated, entitled broker research through it.
- **M&A:** **RANOS** (Auckland NZ, APAC equity-research publishing platform, Jun 2025); **RMS Partners** from FactSet (research modelling/authoring platform, Sep 2025); agreed to acquire **Aiera** (live events, transcripts, governed AI access) on 8 Oct 2026, expected to close Q4 2026 subject to approvals.
- **Partnerships:** **Perplexity** (Jan 2026): pilot that lets entitled buy-side users query their subscribed broker research in Perplexity Enterprise. BlueMatrix stays the system of record for entitlements and the research isn't used for model training.
- **Regions/markets covered:** Global. 1,000+ financial institutions/research firms in 50+ countries; 7,000+ analysts publish on the platform. APAC presence strengthened through RANOS (NZ).
- **Free tier:** No. Enterprise licensing. About 400 brokers publish "open-access" research that needs no broker entitlement, but platform access is still licensed.
- **Pricing model & known ranges:** Enterprise subscription for both publisher (sell-side) and consumer (buy-side) products. **Not publicly disclosed.**

## 2. Data-domain coverage
- **fundamentals:** Not a structured-fundamentals vendor. Broker models can travel with research, and RMS adds model-building tooling for authors.
- **filings:** No.
- **transcripts/expert calls:** Not today. Arrives with Aiera (earnings calls, conferences, live events) once the deal closes.
- **qualitative research:** **Core.** Sell-side and independent broker research from 600+ entitled brokers plus ~400 open-access brokers, delivered through one feed.
- **private-company data:** No.
- **entity/knowledge graph:** Metadata-rich research records (RIXML tagging of issuer, analyst, sector, report type) support filtering and analytics. Not sold as a standalone entity graph.

## 3. Datasets
- **BlueMatrix Live / Consumption & Ingestion API (buy-side):** one real-time feed of entitled broker research across 600+ sell-side brokers plus ~400 open-access providers. BlueMatrix onboards brokers for the client, and the service advertises no rate limits.
- **Formats:** PDF, plain text, RIXML and HTML5, with charts and tables preserved for LLM and model ingestion.
- **Readership & consumption data:** aggregated readership across all providers. It supports MiFID II research-payment governance and 30/90-day embargo controls.
- **Sell-side publishing products:** Creator (authoring with AI assist), RMS (modelling and report building), Portal (white-label research hub with entitlements by firm, user or report), StreetContext/SCX (capital-markets email distribution), Portal Analyzer and email engagement analytics, MiFID II contracts/invoicing and broker-vote tools.
- **Sourcing method:** Aggregation and distribution of content authored by brokers and research firms. BlueMatrix doesn't produce research itself. The proprietary asset is the publisher network, the entitlement graph and readership data.

## 4. APIs & technical integration
- **APIs:** Consumption & Ingestion API for buy-side ingestion into data platforms, models and AI workflows.
- **MCP:** Yes. BlueMatrix advertises an MCP server for connecting entitled research to Claude and ChatGPT (originally slated for Q2 2025).
- **AI/LLM features:** BlueIQ Chat (cited Q&A across entitled research), intelligent search, saved "insight agents" that re-run on new content, and AI-assisted authoring. The Perplexity Enterprise pilot is a further channel.
- **Formats/delivery:** Web platform, API feed, email (SCX), white-label portal. No Snowflake or Databricks share is advertised, so ingestion into a lakehouse would be API-driven.
- **Entitlements:** Centralised per-broker entitlement requests, approvals and enforcement. This is the main integration value for a buy-side firm.

## 5. Enabling technology
- Multi-tenant publishing and distribution stack with entitlement enforcement at firm, user, content-type and report level.
- RIXML-based metadata standardisation across hundreds of publishers, so broker content arrives in one consistent structure.
- Readership telemetry across portal, email and API channels, which supports MiFID II research-valuation and broker-vote processes.
- AI layer (BlueIQ, MCP server, partner integrations) built on top of entitlements, so permissioning and attribution are preserved when AI tools consume research.

## 6. Customer / user feedback
- **Ratings:** Sparse public reviews. The TrustRadius listing carries no rating, and no G2 profile was found. Treat customer sentiment as unverified.
- **Recognition:** WatersTechnology "Best Research Provider" award listing.
- **Pros (vendor-reported/structural):** Broad broker coverage through one connection; entitlements and MiFID II readership handled centrally; long-standing sell-side incumbency (Oppenheimer cited as a long-term client).
- **Cons / risks:** Opaque pricing; value depends on which brokers a buyer already has entitlements with; three acquisitions in 18 months (RANOS, RMS, Aiera) bring integration risk; private-equity ownership.
- **User segments:** Sell-side banks and brokers, independent research boutiques, wealth managers, and buy-side asset managers consuming broker research.

## 7. Edge & positioning
- **Leads:** The most complete single connection to entitled sell-side research, with governance (entitlements, readership, MiFID II) built in, and an AI-distribution story (MCP, Perplexity, Aiera) that keeps broker IP and permissioning intact.
- **Lags:** Not a fundamentals, pricing or reference-data source; no lakehouse-native share advertised; little independent customer evidence; content quality depends on brokers.
- **Best for:** Buy-side firms that want broker research flowing into their research workflow, data platform and AI tools through one governed feed instead of per-broker portals and email.
- **Classification:** A data provider and **IDP data source** for the unstructured broker-research domain. It is **not** an investment data platform: no security/reference-data mastering, positions or EDM.

## 8. Provenance
- https://www.bluematrix.com/about-us — vendor: founding, HQ, leadership, product names (accessed 2026-11-03)
- https://home.bluematrix.com/consumption — vendor: Consumption & Ingestion API, broker counts, formats, MCP (accessed 2026-11-03)
- https://home.bluematrix.com/buyside — vendor: BlueMatrix Live for buy-side (accessed 2026-11-03)
- https://home.bluematrix.com/distribution — vendor: Portal, SCX, readership analytics, BlueIQ (accessed 2026-11-03)
- https://www.thomabravo.com/press-releases/thoma-bravo-completes-strategic-investment-in-bluematrix — vendor/investor: Thoma Bravo investment, Jan 2024 (accessed 2026-11-03)
- https://www.bluematrix.com/blog/bluematrix-acquires-ranos-to-accelerate-innovation-and-expand-its-asia-pacific-footprint — vendor: RANOS acquisition, Jun 2025 (accessed 2026-11-03)
- https://www.nbr.co.nz/deals/kiwi-investment-research-tech-firm-ranos-acquired-by-bluematrix — independent: NBR on RANOS deal (accessed 2026-11-03)
- https://www.thomabravo.com/press-releases/bluematrix-expands-global-reach-and-product-breadth-through-acquisition-of-rms — vendor/investor: RMS acquisition, Sep 2025 (accessed 2026-11-03)
- https://www.waterstechnology.com/emerging-technologies/7952708/bluematrix-acquires-factset%E2%80%99s-rms-partners-platform — independent: WatersTechnology on RMS deal (found by search, 2026-11-03)
- https://www.businesswire.com/news/home/20260113633321/en — vendor: Perplexity partnership, Jan 2026 (accessed 2026-11-03)
- https://dealroom.co/news/160968-thoma-bravo-backed-bluematrix-buys-aiera-to-govern-ai-research-distribut/ — independent: Aiera acquisition, Oct 2026 (accessed 2026-11-03)
- https://waterstechnology.com/node/4351846 — independent: WatersTechnology "Best Research Provider" award (found by search, 2026-11-03)
- https://tr-web.dev.trustradius.com/products/bluematrix/reviews — independent: TrustRadius listing, no rating (accessed 2026-11-03)
