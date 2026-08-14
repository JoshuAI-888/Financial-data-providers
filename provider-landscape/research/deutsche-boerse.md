# Deutsche Börse / STOXX / Qontigo

## 1. Snapshot
- **Owner/parent:** Deutsche Börse Group (publicly listed, Frankfurt: DB1) — owns Deutsche Börse Market Data + Services (MDS), and Qontigo, the entity formed in 2019 combining STOXX Ltd. (indices) and Axioma (risk/portfolio analytics); Qontigo itself is now folded further into ISS STOXX following Deutsche Börse's acquisition of ISS.
- **Coverage:** German/European core (Xetra cash equities, Eurex derivatives) plus global index coverage via STOXX (10,000+ indices, incl. EURO STOXX 50, DAX family) licensed in 500-600+ markets/products worldwide.
- **Free tier:** No public free tier; real-time and most reference/index data require licensed subscriptions. Delayed/basic quote pages exist on public sites but bulk/API access is licensed.
- **Pricing model & ranges:** Licensing via Market Data Dissemination Agreements and published Price Lists (not summarized publicly in search results); index licensing for STOXX/DAX benchmarks is deal-specific (e.g., ETF/derivative issuers pay usage-based licence fees) — no public flat-rate card found.

## 2. Coverage
Deutsche Börse MDS distributes real-time and historical data from Deutsche Börse Group's own venues — Xetra (German cash equities) and Eurex (European derivatives) — plus index data from the DAX and STOXX families (now under ISS STOXX Index GmbH branding for some products) and STOXX DAX ESG/Thematic/Volatility/Fixed Income indices. STOXX itself calculates 10,000+ indices covering European and global equity markets, with the EURO STOXX 50 as its flagship benchmark; DAX covers the German blue-chip and broader market segments (MDAX, TecDAX, etc.). This gives Deutsche Börse/Qontigo very deep German-market first-party data plus very broad (but licensed/derived, not primary-exchange) global index coverage.

## 3. Datasets
Core proprietary assets: (1) Xetra/Eurex real-time and historical trade/reference data (first-party exchange data); (2) STOXX index family (10,000+ indices, global equity/fixed income/ESG/thematic/volatility benchmarks) licensed to 500+ (some sources cite 600+) companies as underlyings for ETFs, futures/options, structured products and passive funds; (3) Axioma portfolio/risk analytics models (factor risk models, portfolio optimization) now integrated with STOXX index construction (e.g., ESG-screened STOXX Factor Indices use the Axioma Portfolio Optimizer); (4) third-party ESG data integration (e.g., RepRisk data feeding Axioma analytics and STOXX index construction).

## 4. APIs & technical integration
Real-time information is delivered via a cloud-based WebSocket endpoint, marketed as removing the need for physical co-location/connectivity infrastructure. A broader "Deutsche Börse Group API Platform" aims to expose services across the trade lifecycle (trading, clearing, post-trading) via easy-to-consume APIs, reflecting an ongoing shift from legacy direct-feed/leased-line delivery toward modern cloud API access. Index data and reference/historical data are also available via traditional file-based/price-list-governed distribution. No public evidence of an MCP server; Axioma analytics historically integrate via desktop/enterprise risk-platform APIs rather than a lightweight public REST API.

## 5. Enabling technology
Deutsche Börse emphasizes "highest data quality and speed" from its own trading infrastructure (Xetra/Eurex) as the basis for downstream data quality claims, and is investing in cloud-based WebSocket delivery to modernize distribution. Qontigo/Axioma's differentiator is quantitative risk/portfolio analytics (factor models, optimization) now woven into STOXX's ESG and factor index construction — i.e., analytics-driven index design rather than passive index replication. No public AI/LLM-specific feature disclosure found; positioning centers on quantitative risk modeling and first-party trading-data provenance.

## 6. Customer / user feedback
No independent third-party review base was found (search results returned only Deutsche Börse's own marketing/technical pages, plus an unrelated "marketdata.app" review page that is a different company). Trade-press coverage (PR Newswire, ESG Today, ETF Strategy) documents active commercial traction for STOXX/Qontigo's ESG and factor-index licensing (e.g., STOXX ESG benchmark licensed to China's PSBC; RepRisk ESG data partnership; STOXX Factor Indices combining index + Axioma analytics), suggesting institutional/index-licensee demand is a validated growth area, though this is vendor-published rather than independently sourced customer sentiment.

## 7. Edge & positioning
- **Leads on:** First-party depth on German markets (Xetra/Eurex) with strong data-quality claims tied directly to exchange operation; STOXX's scale as a global index provider (10,000+ indices, 500+ licensees); differentiated analytics-driven index construction via Axioma risk models (esp. ESG/factor indices) — a combination (index + quant analytics) fewer regional providers offer.
- **Lags on:** Public pricing transparency (agreement/price-list-gated, not published); API modernization is described as in-progress (WebSocket/cloud shift) rather than fully mature/public self-serve; independent customer-review visibility is essentially absent, making external validation hard.
- **Best-for:** ETF issuers, structured-product manufacturers, and institutional investors needing licensed benchmark indices (esp. ESG/factor variants) combined with portfolio risk analytics, plus firms needing authoritative first-party German equity/derivatives market data.

## 8. Provenance
- https://www.mds.deutsche-boerse.com/mds-en/real-time-data — Deutsche Börse MDS real-time data overview (accessed 2026-08-14)
- https://www.mds.deutsche-boerse.com/mds-en/real-time-data/indices — STOXX/DAX indices real-time data product (accessed 2026-08-14)
- https://www.mds.deutsche-boerse.com/mds-en/real-time-data/Real-time-data-feeds — real-time feed technology description (accessed 2026-08-14)
- https://www.deutsche-boerse.com/dbg-en/markets-services/ps-technology/ps-api-platform — Deutsche Börse Group API Platform (accessed 2026-08-14)
- https://www.stoxx.com/web/dax-indices/about-us — Qontigo/STOXX/DAX company background (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/qontigo-licenses-stoxx-benchmark-for-esg-investing-in-china-to-psbc-301678371.html — STOXX ESG benchmark licensing example (accessed 2026-08-14)
- https://www.esgtoday.com/qontigo-integrates-esg-data-from-reprisk-into-portfolio-analytics-index-solutions/ — Qontigo/RepRisk ESG data integration (accessed 2026-08-14)
- https://stoxx.com/qontigo-combines-index-and-analytics-expertise-in-stoxx-factor-indices/ — STOXX + Axioma factor index construction (accessed 2026-08-14)
- Note: WebFetch to deutsche-boerse.com/mds/stoxx.com was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches.
