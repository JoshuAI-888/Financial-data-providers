# Quiver Quantitative

## 1. Snapshot
- **Owner/parent:** Quiver Quantitative, LLC (independent, founder-run). **HQ:** United States. **Founded:** ~2020 (founders including James Kardatzke). Positioning: consumer-friendly alternative-data platform that "democratizes" non-traditional datasets — most famous for tracking US congressional stock trading — and exposes them through a single API.
- **Access/region notes.** Web dashboards + API; data is overwhelmingly US-centric (US Congress, SEC/insider filings, US government contracts, US-listed equities). Retail-accessible pricing, unlike most alt-data vendors.
- **Free tier:** yes (limited). Much of the flagship content (congressional trading dashboards, WSB/Reddit trackers) is viewable free on the website; a free API tier exists but with restricted endpoints, capacity and history. Deeper/bulk and insider data sit behind paid tiers.
- **Pricing model & known ranges:** consumer subscription plus tiered API. Website **Premium ~$10/month** for full dashboards. **API access from ~$30/month**; insider-trading via API reported behind a higher (~$75/month) tier; higher tiers for bulk/history. Enterprise/redistribution priced by quote. (Ranges from public reviews and the API pricing page; treat exact numbers as approximate.)

## 2. Data-domain coverage
- **Social posts:** partial — WallStreetBets / Reddit mention counts and retail sentiment trackers (aggregated, not raw post feeds).
- **Sentiment scores:** partial — WSB mention/sentiment and app-rating trends as sentiment proxies.
- **Retail-trader signals:** yes — WSB mentions, off-exchange (dark-pool proxy) activity, app-download/rating trends.
- **Political/insider trades:** yes — the core franchise: US House & Senate trading disclosures plus SEC Form 4 insider transactions; also lobbying, government contracts, patents, executive comp.
- **Options flow:** no.
- **Crypto social:** no (equity/alt-data focus).

## 3. Datasets
- Captures: US congressional/Senate trades, corporate insider (Form 4) transactions, lobbying disclosures, federal government contract awards, corporate patent filings (USPTO), executive compensation, institutional & ETF holdings / top shareholders, off-exchange (retail-flow) volume, app ratings, WSB/Reddit mentions, and a news feed.
- History depth: multi-year back to ~2014–2016 for congressional and several datasets; varies per dataset.
- Coverage breadth: US-listed universe; strength is the **breadth of distinct alt-data domains in one API**, not depth on any single one.
- Proprietary scores/signals: strategy backtests and aggregated tracker scores; congressional-trade matching claimed >99% accuracy by parsing official filings directly.
- Sourcing method: parses primary/official disclosures (House/Senate clerk filings, SEC EDGAR, USASpending, USPTO) plus scrapes of Reddit/app stores — aggregation of public records rather than exclusive proprietary capture.

## 4. APIs & technical integration
- **API type:** REST/JSON. Base URL `https://api.quiverquant.com/`; versioned paths (`/beta`, `/v1`) with both **bulk historical** dataset endpoints and **live ticker-specific** lookups.
- **Auth:** Bearer token API key.
- **Formats:** JSON; official Python package (`quiverquant`) available.
- **Rate limits:** tier-dependent; free/low tiers throttled, higher tiers raise limits and unlock bulk endpoints and more history.
- **ToS/redistribution:** personal/internal use on standard tiers; redistribution and commercial resale require an enterprise agreement. Note the inherent **~45-day disclosure lag** on congressional trades — a data-latency constraint, not a licensing one.
- **MCP availability:** no official MCP server noted (community wrappers only); also distributed via QuantConnect for backtesting.

## 5. Enabling technology
- Document parsing/OCR and normalization of heterogeneous government filings into ticker-linked records; entity→ticker mapping across politicians, issuers and contractors. Reddit/NLP mention counting for WSB trackers. Strategy backtesting engine layered on the datasets. Emphasis is data engineering/aggregation over heavy proprietary ML.

## 6. Customer / user feedback
- Triangulated across QuantVPS review, Find My Moat, SignalScope and Tracefour comparisons. **Pros:** unusually cheap and accessible for alt-data; one API spanning many exotic datasets; strong, accurate congressional-trade coverage; good for retail/prosumer quants and content creators. **Cons:** disclosure/reporting lag (congressional ~45 days) limits short-term edge; datasets are aggregations of public records so not exclusive; insider and bulk data gated behind higher tiers; documentation and support are lighter than institutional vendors; some datasets shallow. User segments: retail quants, fintech app builders, journalists/researchers, and small funds wanting cheap alt-data.

## 7. Edge & positioning
- **Leads** on price/accessibility and on being the go-to congressional-trading source with broad alt-data breadth in a single, cheap API. **Lags** on latency (inherent to disclosure windows), exclusivity (public-record based), and institutional-grade SLAs/depth. **Best-for:** low-cost access to congressional/insider + WSB alt-data for retail and small-fund research. **Free pick:** yes — one of the most genuinely accessible free/cheap alt-data sources, with the caveat that the free tier is capped and the freshest edge is limited by disclosure lag.

## 8. Provenance
- https://www.quiverquant.com/api/ — official API setup/overview (accessed 2026-08-11)
- https://api.quiverquant.com/ — official API base/docs portal (accessed 2026-08-11)
- https://api.quiverquant.com/pricing/ — official API pricing tiers (accessed 2026-08-11)
- https://www.quiverquant.com/news/Introducing+four+new+API+endpoints — official endpoint announcement (accessed 2026-08-11)
- https://github.com/Quiver-Quantitative/python-api — official Python client (accessed 2026-08-11)
- https://www.quantconnect.com/docs/v2/writing-algorithms/datasets/quiver-quantitative/us-congress-trading — third-party dataset integration docs (accessed 2026-08-11)
- https://www.quantvps.com/blog/quiver-quantitative-review — independent review (accessed 2026-08-11)
- https://tracefour.com/compare/quiver — independent comparison/alternatives (accessed 2026-08-11)
