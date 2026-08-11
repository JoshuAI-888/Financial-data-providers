# Kaiko

## 1. Snapshot
- **Owner/parent:** Independent (privately held); CEO & co-controlling shareholder Ambre Soubiran. HQ **Paris, France** (Bourse district), with offices in New York, London and Singapore. **Founded 2014**. Positioning: the institutional-grade market-data, analytics and indices backbone for digital assets, built for funds, banks, exchanges and regulators.
- **Coverage:** **100+ centralised and decentralised exchanges**, ~**35,000+ instrument pairs**, spot and derivatives; tick-level trade history back to **2010** and Level-2 order-book snapshots since ~2015. Regulated reference-rate indices across leading blockchains.
- **Free tier:** **No public free tier.** Access is commercial/bespoke; limited data can be seen via docs/sample endpoints but there is no self-serve free plan. (Flag: not a fit for zero-budget/retail use.)
- **Pricing model & ranges:** **Not publicly disclosed** — fully bespoke enterprise contracts scoped by assets, instruments, data type, granularity, live-vs-historical access and usage rights. Widely described as premium/enterprise pricing requiring a sales conversation.

## 2. Data-domain coverage
- **Market data (spot/derivatives):** Yes — core strength; tick trades, L1/L2 order books, OHLCV, derivatives (funding, open interest, implied vol, Greeks).
- **On-chain:** Yes — Kaiko On-chain product line (blockchain activity, DEX data).
- **Reference/metadata:** Yes — normalised instrument/exchange reference data.
- **Indices:** Yes — Kaiko Indices administers regulated crypto reference rates and benchmarks (ETF/ETP NAV, derivatives settlement, structured products).
- **DeFi:** Yes — DEX trade data and lending-protocol coverage (e.g. Aave/Compound/Maker).
- **Research/analytics:** Yes — market microstructure, liquidity and volatility analytics; published research.
- **Institutional/regulatory-grade:** Yes — SOC-2 Type II, EU BMR benchmark administration, MiCA-aligned; distribution partnership with Deutsche Börse Market Data + Services.

## 3. Datasets
- Tick-level trades (from 2010), full-depth and snapshot **Level-2 order books** (from ~2015), OHLCV/VWAP, derivatives metrics (funding, OI, liquidations, options IV surfaces and Greeks), DeFi/DEX trades, on-chain data, and a family of **reference rates/benchmark indices**.
- History depth is a differentiator — one of the deepest tick/order-book archives in the market.
- Proprietary holdings: regulated Kaiko reference rates/fixings and normalised cross-exchange datasets; index methodologies built to institutional/IOSCO-style standards.

## 4. APIs & technical integration
- **API types:** Kaiko REST (historical + reference), **Kaiko Stream** (real-time WebSocket and gRPC), plus **flat-file / cloud delivery**.
- **Delivery:** AWS S3, and **data-warehouse shares (Snowflake, BigQuery)**; daily CSV to AWS/Azure/GCP; distribution via Deutsche Börse network. On-chain reference rates can be published directly to smart contracts (hourly updates by default).
- **Auth/formats:** API-key auth; JSON (REST/stream) and CSV (bulk); normalised schemas across venues.
- **Rate limits:** Contract/plan-dependent, not publicly posted.
- **MCP availability:** No official Kaiko MCP server identified as of Aug 2026.

## 5. Enabling technology
- Collects tick-level trade and order-book data directly from 100+ CEXs/DEXs with continual venue/asset onboarding; heavy normalisation into consistent cross-exchange schemas.
- Index/benchmark methodology engineered for auditability and manipulation resistance (volume weighting, outlier handling) under EU BMR / IOSCO principles — a core reason institutions and ETP issuers select it.
- Data-ops posture: SOC-2 Type II, transparent methodology docs, T+1 historical delivery pipelines suited to risk, compliance and quant research.

## 6. Customer / user feedback
- Triangulated (CoinAPI comparison, Datarade profile, Spark, CME/Deutsche Börse references): consistently rated **best-in-class for institutional/regulated use** and market microstructure; the delivery architecture itself is often the buying case.
- **Pros:** depth of history, order-book quality, regulatory credentials, flexible enterprise delivery (S3/Snowflake/stream).
- **Cons:** premium bespoke pricing, no self-serve/free tier, less friendly for small product teams or developers who want transparent published prices.
- **Segments:** hedge funds, banks, exchanges, ETP/index issuers, regulators — not retail.

## 7. Edge & positioning
- **Leads on:** institutional-grade market data (tick + L2 order books), regulated indices/reference rates, auditable methodology, and enterprise delivery. Deutsche Börse partnership reinforces institutional trust.
- **Lags on:** accessibility/price transparency and self-serve/free access; developers wanting quick free keys look elsewhere (CoinGecko/CoinMarketCap/CoinAPI).
- **Best-for:** regulated institutions needing auditable pricing, benchmarks, and deep microstructure/order-book history. Firmly **institutional-grade**, not free/retail.

## 8. Provenance
- https://www.kaiko.com/ — Official site, positioning (accessed 2026-08-11)
- https://www.kaiko.com/about-kaiko — Company/HQ background (accessed 2026-08-11)
- https://www.kaiko.com/indices/reference-rates — Regulated index methodology (accessed 2026-08-11)
- https://www.kaiko.com/products/l1-l2-data — Order-book data product (accessed 2026-08-11)
- https://www.coinapi.io/blog/coinapi-vs-kaiko-crypto-market-data-comparison — Independent competitor comparison (accessed 2026-08-11)
- https://www.cmegroup.com/solutions/market-tech-and-data-services/technology-vendor-services/kaiko.html — Institutional distribution reference (accessed 2026-08-11)
- https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-partners-with-Kaiko-to-extend-its-market-data-offering-in-the-crypto-sector-3126576 — Deutsche Börse partnership (accessed 2026-08-11)
- https://www.crunchbase.com/person/ambre-soubiran — Founder/leadership profile (accessed 2026-08-11)
