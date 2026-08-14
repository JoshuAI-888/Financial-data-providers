# TipRanks

## 1. Snapshot
- **Owner/parent:** Majority-owned by Prytek (an international technology holding group), which acquired ~80% of TipRanks in a deal valuing the company at ~$200M (Prytek was an early investor and led TipRanks' $77M raise in April 2021 before increasing its stake). Remaining ~20% held by institutional investors (e.g., More Investment House, Analyst). Israeli fintech, founded 2012 by Uri Gruenbaum (CEO) and Gilad Gat (CTO).
- **Coverage:** Sell-side analyst ratings/price targets, insider trading, hedge-fund positioning, blogger/news sentiment, technicals, options, ETFs, commodities, forex, and crypto — primarily US markets on the core consumer product, with a newer API library extending to European large caps (e.g., BP, Volkswagen, Siemens, HSBC, Vodafone).
- **Free tier:** Yes for the developer/MCP API layer — a free API key is available with no credit card (via /dev/signup or the MCP connector), though rate limits are modest and scale with subscription tier (free-key monthly allowances reported at 50 calls, rising to 100/200 for Premium/Ultimate subscribers). The core consumer product (Premium/Ultimate) is paid-only; the separate **enterprise data API is not self-serve** and requires a commercial/sales arrangement.
- **Pricing model & ranges:** Consumer subscriptions: Premium $360/year, Ultimate $600/year (no monthly option; 30-day money-back guarantee). Enterprise/institutional data API: custom-quoted, licensed to 100+ banks, brokers, and exchanges — no public rate card found.

## 2. Coverage
Best known for its proprietary **Smart Score** (1-10, blending analyst-consensus-weighted-by-track-record, insider activity, hedge-fund positioning, blogger sentiment, news sentiment, technicals, retail "crowd wisdom," and fundamentals via an AI/ML-weighted model; scores of 8-10 = Outperform, 4-7 = Neutral, 1-3 = Underperform). Core strength is the **analyst-attribution layer**: individual analyst-level track records, success rates, and firm affiliations, not just consensus numbers. Primarily US-equity-centric with an expanding European large-cap API library; retail/consumer product claims 50M+ monthly users, with tipranks.com itself drawing 10M+ monthly visitors.

## 3. Datasets
- Analyst ratings & price targets: flexible search by symbol/analyst/date range, point-in-time snapshots (for backtesting/compliance), and Buy/Hold/Sell consensus aggregation at ticker/analyst/firm level.
- Smart Score (1-10 composite signal) with underlying factor breakdown.
- Analyst directory: ranked profiles, historical success rates, firm affiliations.
- Insider trading data with linked SEC filings.
- Blogger and news sentiment.
- Hedge-fund and institutional/congressional trading activity.
- Technicals, options, ETFs, commodities, forex, crypto, earnings, and general market news (via the MCP connector's broader data surface).

## 4. APIs & technical integration
- **API type:** REST/JSON API (developer signup) plus a hosted MCP connector at `mcp.tipranks.com`.
- **Auth:** API-key based for the developer API; OAuth (sign in with TipRanks account, approve scopes) or API key for the MCP connector. All MCP tools are read-only (cannot place trades or modify account data).
- **MCP availability:** Yes — official, actively marketed ("Bring TipRanks into every investment conversation") remote MCP server supporting Claude, ChatGPT, and Cursor, plus listing in the ChatGPT plugin directory (no developer-mode setup required there). Setup advertised as "ready in 60 seconds, one URL."
- **Distribution:** Also licensed through third-party data platforms (e.g., Financial Modeling Prep offers TipRanks-powered analyst-ratings/price-target endpoints), and via unofficial community/scraper wrappers (GitHub `tipranks-api-v2`, Apify/ScrapingBee scrapers) — evidence that no comprehensive official public API existed for some data historically, though the direct MCP/API offering has since expanded.
- **Enterprise API:** Separate "TipRanks Enterprise" institutional data product (enterprise.tipranks.com) for banks/brokers/exchanges — not self-serve.

## 5. Enabling technology
Proprietary AI/NLP pipeline: natural-language processing sifts blogger commentary, news flow, and "millions of daily stock transactions" (insider, hedge-fund, retail activity) to compute the Smart Score; TipRanks does not publicly disclose exact factor weightings, describing them as based on "historical predictive value" and updated in real time as new data arrives. The differentiating technology is less the NLP itself and more the analyst-accountability data layer — systematically tracking and back-testing individual analysts' historical accuracy to weight their current calls.

## 6. Customer / user feedback
Strong consumer-side reputation: ~1,569 Trustpilot reviews with a 4.3 TrustScore ("Excellent"). Client base includes Nasdaq, Robinhood, CIBC, Morgan Stanley, TD, E*TRADE, Interactive Brokers, Santander, and TMX (100+ banks/brokers/exchanges cited as enterprise-API licensees). Positive feedback centers on the unique analyst-accountability/track-record angle. Recurring complaints on Trustpilot/review sites: portfolio-sync issues, being rate-limited/"locked out" after checking too many stocks in a day, surprise tier upgrades, difficulty cancelling and slow refunds, and data-accuracy gaps for certain non-US tickers/ETFs. TipRanks itself cautions that Smart Score is backtested and not a guarantee of future performance.

## 7. Edge & positioning
- **Leads on:** Analyst-level accountability and track-record scoring — a data layer most peers (RavenPack, Dataminr, generic sentiment vendors) don't offer; broad enterprise distribution (100+ banks/brokers/exchanges) plus a genuinely accessible consumer product and MCP connector.
- **Lags on:** Depth of raw social/text data compared to dedicated social-listening or news-analytics vendors (it aggregates and scores rather than provides the underlying social corpus); non-US coverage still expanding (Europe only so far); enterprise API is quote-only/non-transparent like most peers in this landscape.
- **Best-for:** Retail and semi-professional investors wanting a single blended "is the crowd/street bullish" signal with drill-down to individual analyst credibility, and platforms (brokerages, fintechs) wanting to embed analyst-ratings/Smart-Score widgets via API or MCP rather than build sentiment scoring from scratch.

## 8. Provenance
- https://site.financialmodelingprep.com/datasets/analyst-ratings-tipranks — third-party licensing of TipRanks analyst data (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://mcp.tipranks.com/ — official MCP connector: auth, data scope, supported clients (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://www.tipranks.com/news/labs/bring-tipranks-into-every-investment-conversation-introducing-mcp — official MCP launch announcement (accessed 2026-08-14)
- https://enterprise.tipranks.com — enterprise API product page (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://www.calcalistech.com/ctechnews/article/byhoe8jq0 — Prytek acquisition/ownership details (accessed 2026-08-14)
- https://www.stockbrokers.com/review/tools/tipranks — consumer pricing (Premium/Ultimate), review commentary (accessed 2026-08-14)
- https://www.trustpilot.com/review/tipranks.com — Trustpilot rating (4.3, ~1,569 reviews) and complaint themes (accessed 2026-08-14)
- https://www.tipranks.com/glossary/s/smart-score — Smart Score methodology/factor description (accessed 2026-08-14)

**Note:** WebFetch to tipranks.com, mcp.tipranks.com, enterprise.tipranks.com, and site.financialmodelingprep.com was egress-blocked in this environment; findings rely on the WebSearch index and third-party secondary sources rather than direct page retrieval. Exact enterprise-API pricing and current free-key rate limits should be reconfirmed directly.
