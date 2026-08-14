# Unusual Whales

## 1. Snapshot
- **Owner/parent:** Independent, founder-run; small team, no outside/VC funding (self-funded/bootstrapped since founding). Founded 2020, started as a project tracking US congressional stock trading before expanding into options flow and dark-pool data.
- **Coverage:** US-listed equities and options markets — real-time options flow (sweeps, blocks, unusual activity), dark-pool/off-exchange prints, US Congressional and Senate stock-trading disclosures (STOCK Act filings), Greek exposure, volatility, and market-maker/insider tracking. Retail-accessible, US-market-only focus.
- **Free tier:** Yes (limited) — a $0/month plan with basic alerts, delayed (~15-20 min) dark-pool data, and restricted mobile-app access; full real-time data and API access require a paid plan.
- **Pricing model & ranges:** Consumer subscription tiers plus separate API pricing. Free tier at $0; Premium/basic paid plan reported around **$50/month** unlocking real-time alerts, full dark-pool data, advanced options-chain filtering, complete congressional-trading history, and full API access. Historical full-market options-trade data sold separately at **~$250/month**. 15-minute-delayed data offered at reduced pricing across endpoints. Enterprise pricing available on request (contact sales).

## 2. Coverage
US-market-only alternative-data platform (no international exchange coverage — consistent with the FMP free-tier US-comparables constraint this repo already operates under). Core domains: (1) real-time options order flow and "unusual" activity detection sourced from exchange feeds, (2) dark-pool/off-exchange block-trade prints, (3) Congressional/Senate stock-trade disclosures parsed from STOCK Act filings (politician tracking, e.g., high-profile names surfaced within hours of disclosure), and (4) supplementary market-structure data (Greek exposure, implied volatility, analyst price targets, news). No dedicated social-sentiment or crypto vertical — positioning is retail-facing "follow the smart/insider money" alternative data, not general news or social sentiment.

## 3. Datasets
- **Options flow:** real-time sweep/block/unusual-activity detection with Greeks, implied volatility, and options-chain analytics.
- **Dark pool flow:** off-exchange block-trade prints and volume, exposing large institutional transactions not immediately visible on lit exchanges.
- **Congressional/political trades:** STOCK Act disclosure filings for US House and Senate members, parsed and ticker-linked, with reported extended historical depth (multi-year) and reportedly hours-fast turnaround after official disclosure (notably faster than the ~45-day lag flagged for competitor Quiver Quantitative).
- **Market-maker/institutional tracking, news, and analyst data:** supplementary datasets bundled into the platform and API.
- Delivery latency: real-time on paid tiers; 15-20 minute delay on free tier.

## 4. APIs & technical integration
- **API type:** REST API with 100+ documented endpoints (api.unusualwhales.com/docs) covering options flow, dark pool, congressional trading, Greek exposure, volatility, and more.
- **Auth:** API key-based.
- **Formats:** JSON via REST; also offers WebSocket streaming (gated to an "API Advanced" tier) and Kafka access for high-throughput/enterprise integration — an unusually rich delivery stack for a retail-priced product.
- **MCP availability:** Yes — Unusual Whales publishes an official **MCP server**, explicitly marketed alongside the public API ("Market Data API & MCP Server"), a notable differentiator versus most peer providers in this landscape which lack MCP support.
- **Rate limits/ToS:** Tier-gated (WebSocket/Kafka reserved for higher/Advanced tiers); historical full-market options data sold as a separate add-on (~$250/month) rather than bundled.

## 5. Enabling technology
Real-time ingestion and pattern-detection engine over exchange-level options order-flow data (sweep/block/unusual-activity classification) combined with automated parsing of official government disclosure filings (STOCK Act) for congressional-trade matching, and aggregation of off-exchange/dark-pool print data. Emphasis is on fast, accurate data-pipeline engineering (turning public/exchange filings into ticker-linked, queryable records quickly) rather than proprietary NLP/sentiment modeling — closer in kind to Quiver Quantitative's aggregation approach, but with materially faster congressional-disclosure turnaround and a much richer options/dark-pool dataset.

## 6. Customer / user feedback
Triangulated across Trustpilot, Reddit community reviews, and independent review sites (Traders Agency, Bullish Bears, Pure Power Picks, Find My Moat). **Pros:** widely regarded as the most complete and affordable retail options-flow/dark-pool platform; congressional-trade tracker is repeatedly cited as the standout differentiator (filings surfaced within hours); real-time, continuously-scanning data delivery; strong API/WebSocket/Kafka/MCP technical stack for a retail-priced product; credited with real-world impact (2021 Congressional Trading Report cited by ABC News, Bloomberg, Reuters, and referenced in Congressional hearings, reportedly spurring proposed legislation). **Cons:** alerts flag unusual activity but do not predict price direction — interpreting institutional flow (hedges vs. speculative bets) requires trader expertise; not beginner-friendly (lacks educational/basic-analysis tooling); best suited to intermediate/advanced options traders. User base: retail options traders, prosumer quants, journalists/researchers tracking political trading, and bot/algo builders using the API.

## 7. Edge & positioning
- **Leads on:** speed and completeness of US options-flow + dark-pool + congressional-trade data at retail-accessible pricing; richest technical delivery stack (REST/WebSocket/Kafka/MCP) among comparably-priced alt-data platforms; congressional-disclosure turnaround materially faster than peers.
- **Lags on:** international/non-US coverage (none), social/news-sentiment analytics (not a core offering), and beginner accessibility/educational tooling — raw data requires trading expertise to interpret.
- **Best-for:** intermediate-to-advanced options and momentum traders wanting real-time flow/dark-pool/political-trading signals via a well-documented API, at a fraction of institutional alt-data pricing.

## 8. Provenance
- https://unusualwhales.com/pricing — official pricing plans (accessed 2026-08-14)
- https://api.unusualwhales.com/docs — official API documentation (accessed 2026-08-14)
- https://unusualwhales.com/public-api — official API/MCP server product page (accessed 2026-08-14)
- https://unusualwhales.com/information/what-is-unusual-whales — official company/product overview (accessed 2026-08-14)
- https://unusualwhales.com/congress-trading-report-2024 — official congressional-trading research report (accessed 2026-08-14)
- https://purepowerpicks.com/unusual-whales-review/ — independent product review (accessed 2026-08-14)
- https://www.forbes.com/sites/investor-hub/article/what-is-unusual-whales/ — independent Forbes overview article (accessed 2026-08-14)
- https://tradingtoolshub.com/blog/unusual-whales-pricing-guide-2026/ — independent pricing breakdown (accessed 2026-08-14)

**Note:** WebFetch to unusualwhales.com was egress-blocked in this environment; findings rely on the WebSearch index and third-party review sites rather than direct page retrieval.
