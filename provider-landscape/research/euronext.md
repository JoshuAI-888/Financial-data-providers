# Euronext

## 1. Snapshot
- **Owner/parent:** Euronext N.V. — independent, publicly listed pan-European exchange group (Euronext Paris-listed itself); operates Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo and Paris exchanges plus Euronext Data Solutions.
- **Coverage:** Pan-European equities, fixed income, futures, currencies, indices, options and structured products across its seven home markets, with Level 1 and Level 2 (market depth) products.
- **Free tier:** Delayed market data is free of charge for internal-use-only purposes; real-time/redistribution data requires a paid licence.
- **Pricing model & ranges:** Published "Information Product Fee Schedule" governs redistribution/use fees; specific rates are not publicly summarized in search results — quote-based via My Market Data portal / datasolutions@euronext.com, with pricing, specs and agreements formally documented but not headline-priced.

## 2. Coverage
Euronext aggregates market data across its pan-European footprint (Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo, Paris) spanning cash equities, ETFs, fixed income, currencies, derivatives (futures/options), structured products and Euronext-branded indices. Depth includes both Level 1 (last price/trades/quotes) and Level 2 (order-book depth) real-time and delayed data, plus historical/end-of-day archives. As the exchange operator, Euronext is the primary/first-party source for its listed markets rather than an aggregator of third-party content.

## 3. Datasets
Differentiated holdings are exchange-native: real-time and historical trade/quote data across all Euronext markets, reference data for listed instruments, and Euronext's own index family. Delivered via the Euronext Data Hub / "My Market Data" portal. Historical depth is exchange-native (tied to Euronext's own trading history per market) rather than a purchased third-party archive, giving strong provenance but coverage limited to Euronext-listed venues (not a global multi-exchange content set).

## 4. APIs & technical integration
Euronext Web Services provides real-time, delayed and historical data via a REST-style web API (quotes, last price, trades, reference data) with client-side customization by asset type, time period and update speed. A newer WebSocket-based "Euronext Stream API" is available over the public internet for modern streaming applications. Connectivity infrastructure includes Optiq (Euronext's low-latency trading technology) and a microwave wireless network (e.g., London–Euronext data centre links) for ultra-low-latency access, plus 24/7 connectivity support. No public evidence of an MCP server or LLM-native integration.

## 5. Enabling technology
Euronext's core technology emphasis is trading-venue infrastructure (Optiq matching engine, microwave/fibre low-latency connectivity) extended into a "globally consistent data model" for its real-time datafeed, rather than public claims around AI/LLM features or entity-resolution tooling. As an exchange operator, its data-ops advantage is being the primary source of the trade/quote data itself (no ingestion/normalization dependency on third parties for its own markets).

## 6. Customer / user feedback
Independent user reviews are limited; most available material is Euronext's own marketing/technical documentation (connectivity, market-quality pages) rather than third-party review-site feedback. No structured G2/Capterra-style review base was found for Euronext market data specifically — feedback triangulation for this vendor is weaker than typical global providers, reflecting its B2B/exchange-membership customer base (member firms, data vendors, redistributors) rather than a broad self-serve developer audience.

## 7. Edge & positioning
- **Leads on:** First-party authority over pan-European exchange data across seven markets in one consolidated feed/data model; low-latency infrastructure (Optiq, microwave connectivity) purpose-built for trading firms; free delayed data lowers the bar for internal-use consumption.
- **Lags on:** Global/non-European coverage (Euronext-listed markets only); pricing transparency (no public rate card); breadth of proprietary analytics/estimates content compared to full-service data vendors; thin independent review/feedback footprint makes third-party validation difficult.
- **Best-for:** Trading firms, brokers and data redistributors needing authoritative, low-latency, first-party real-time or historical data specifically for Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo or Paris-listed instruments.

## 8. Provenance
- https://www.euronext.com/en/data/market-data/how-access-market-data — how to access Euronext market data (accessed 2026-08-14)
- https://www.euronext.com/en/data/market-data-pricing-specifications-and-agreements — pricing, specs and agreements portal (accessed 2026-08-14)
- https://www.euronext.com/en/data/how-access-market-data/web-services — Web Services API description (accessed 2026-08-14)
- https://www.euronext.com/en/products-services/euronext-stream-api — WebSocket Stream API (accessed 2026-08-14)
- https://www.euronext.com/en/data/market-data/market-data-pricing-policies — market data fees and policies (accessed 2026-08-14)
- https://www.euronext.com/en/technology/connectivity — connectivity / low-latency infrastructure overview (accessed 2026-08-14)
- https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/equities-market-data/euronext-market-data — third-party (LSEG) description of Euronext market data (accessed 2026-08-14)
- https://developer.ice.com/fixed-income-data-services/catalog/euronext — ICE developer portal listing of Euronext data (accessed 2026-08-14)
- Note: WebFetch to euronext.com pages was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches. An unrelated "Euronext FX" forex-broker review site surfaced in search is a different entity and was excluded.
