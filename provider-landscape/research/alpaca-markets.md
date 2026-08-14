# Alpaca (Alpaca Markets)

## 1. Snapshot
- **Owner/parent:** Independent, privately held. Founded 2017 by **Yoshi Yokokawa and Hitoshi Harada**. Operates as a FINRA-registered US broker-dealer (Alpaca Securities LLC) with its own self-clearing entity (Alpaca Clearing), which became a DTCC member (2023), fully self-clearing (2024), and gained OCC + FICC memberships plus Nasdaq Exchange membership (2025). Backed by ~$400M+ cumulative funding; raised a further **$135M** (2026, led by Peak XV) to expand "agent-first"/AI-native brokerage infrastructure. Supports 10M+ downstream brokerage accounts across hundreds of fintechs/institutions in 40+ countries via its broker-dealer-as-a-service model.
- **Coverage:** US-listed equities/ETFs (5,000+ symbols), 20+ crypto pairs, and US options — all US-market-only (no NZX/ASX/LSE/HKEX/SGX/KRX/TWSE), consistent with the same "US-listed only" constraint this repo already documents for FMP.
- **Free tier:** Yes — **Basic (free)** plan: real-time IEX-only equity data (not full consolidated SIP tape), 15-minute-delayed SIP data, options indicative feed only, unlimited historical data (5+ years), 200 requests/minute, commission-free stock/options/crypto trading via API.
- **Pricing model & ranges:** Freemium + flat subscription. **Basic = $0/month**. **Algo Trader Plus = $99/month** — full real-time SIP equities feed, full OPRA real-time options feed, up to 10,000 requests/minute. Trading itself (stocks, options, crypto) is commission-free on self-directed API accounts at both tiers; revenue comes from data subscriptions, payment-for-order-flow/spreads, margin/interest, and broker-dealer-as-a-service fees to fintech partners.

## 2. Coverage
Purely US market data/execution (equities, ETFs, options, crypto) — directly comparable in scope-limitation to FMP's free tier as documented in this repo (US-listed, no Milford home-exchange coverage). Real-time depth is gated by feed: Basic tier gets only the IEX-only equities feed (not the full consolidated SIP tape) and delayed (15-min) SIP, while full real-time SIP + OPRA options requires the $99/mo Algo Trader Plus tier. Historical data (5+ years, OHLCV bars/trades/quotes) is available at both tiers, effectively unlimited on symbol count.

## 3. Datasets
- Equity bars/candles (OHLCV), trades, and quotes — real-time (IEX or full SIP depending on tier) and historical.
- Crypto market data (20+ pairs) — real-time and historical, not tier-gated the same way as equities.
- Options chains and quotes — indicative feed (Basic) vs full OPRA real-time feed (Algo Trader Plus).
- Corporate actions, and trading/account/order-management data (positions, order history) via the separate Trading API (as opposed to the Market Data API).
- News data feed (Benzinga-sourced, separate add-on in the broader Alpaca data stack).

## 4. APIs & technical integration
API-first, developer-oriented: **REST** endpoints for historical/reference data and order/account management, **WebSocket** and **SSE** streams for real-time market data and order updates. Official SDKs in **Python (alpaca-py, requires 3.10+), Go, Node.js, and C#**; extensive community libraries beyond that. Clear operational split between the **Trading API** (orders, positions, account) and the **Market Data API** (bars/trades/quotes/streaming). Widely used for algorithmic trading strategy backtesting and live execution — praised as one of the best-documented retail-accessible trading APIs. This is the most "FMP-like" of the four providers in this set: comparable REST/rate-limit/tiered-access shape, but combined with an actual brokerage/execution layer FMP does not have.

## 5. Enabling technology
Full-stack, self-clearing brokerage-as-a-service infrastructure (not just a data reseller) — Alpaca owns clearing (DTCC/OCC/FICC memberships, Nasdaq exchange membership) rather than routing through a third-party clearing firm, which differentiates its cost structure and latency versus other API brokers. Recent (2025-2026) strategic direction is explicitly "agent-first"/AI-native brokerage infrastructure — positioning its API/infrastructure stack as the execution layer for AI trading agents and tokenized-market products, per its 2026 funding-round messaging.

## 6. Customer / user feedback
Strong reputation among algorithmic-trading developers: rated ~4.1/5 by trading-review sites, consistently praised for well-documented APIs/SDKs, ease of building and backtesting strategies, and zero-commission execution. Recurring complaints: intermittent outages and execution/message delays during volatile periods, a minimal/sometimes unintuitive web UI (poor discoverability, e.g. users report difficulty finding billing info), limited customer support (GitHub-issue/community-first rather than phone support), and some reports of automation "roadblocks"/restrictions that complicate simple strategy testing.

## 7. Edge & positioning
- **Leads on:** developer experience (REST+WebSocket+SDKs), zero-commission execution bundled with the data API (unique among this set — the others are pure data/document plays), self-clearing infrastructure lowering costs, free tier generous enough for real backtesting/prototyping.
- **Lags on:** no fundamentals/financial-statement data (pure market data + execution, not a "coverage of company financials" provider like FMP), thin customer support, real-time equities data gated behind IEX-only unless paying for SIP, US-market-only scope.
- **Best-for:** developers and fintechs building algorithmic trading, backtesting, or embedded-brokerage products who need combined real-time/historical market data AND commission-free order execution in one API — not a fit for fundamental/financial-statement research (would need to be paired with a provider like FMP for that).

## 8. Provenance
- https://alpaca.markets/data — Market Data API overview, tiers (accessed 2026-08-14, fetch blocked, via search snippet)
- https://docs.alpaca.markets/us/docs/about-market-data-api — feed/rate-limit specifics (accessed 2026-08-14, fetch blocked, via search snippet)
- https://alpaca.markets/about-us — company founding, founders (accessed 2026-08-14)
- https://alpaca.markets/blog/alpaca-secures-occ-and-ficc-memberships-to-power-multi-asset-self-clearing-for-partners/ — self-clearing/OCC/FICC milestones (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20260716033634/en/Alpaca-Raises-$135-Million-to-Scale-Agent-First-Brokerage-Infrastructure-for-Tokenized-Markets-and-AI-Native-Financial-Services — 2026 funding round, strategic direction (accessed 2026-08-14)
- https://github.com/alpacahq/alpaca-py — official Python SDK, coverage confirmation (accessed 2026-08-14)
- https://brokerchooser.com/broker-reviews/alpaca-trading-review — pros/cons, ratings (accessed 2026-08-14)
- https://tradingtoolshub.com/review/alpaca/ — pricing tiers, outage/support complaints (accessed 2026-08-14)

Note: WebFetch to alpaca.markets and docs.alpaca.markets was egress-blocked in this environment; facts above are triangulated from WebSearch result snippets across ≥2 independent sources, not direct page fetches.
