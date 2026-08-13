# ASX (Australian Securities Exchange)

## 1. Snapshot
- Owner/parent: **ASX Limited** (self-listed, ASX: ASX). HQ Sydney, Australia. Traced to 1987 amalgamation of six state exchanges; demutualised and listed 1998. Positioning: Australia's primary listing, cash-equity, derivatives and clearing venue and the authoritative source of Australian market data.
- **Regions/markets covered:** Australia only — ASX cash equities (ASX Trade, on NASDAQ OMX Genium INET), ASX 24 derivatives/futures (ASX Trade24), ETFs, warrants, interest-rate/fixed-income securities, and S&P/ASX index data. Dominant home-market authority for AU listed data; some competition on trading from Cboe Australia (ex-Chi-X), but ASX remains the reference venue.
- **Free tier:** Yes — 20-minute delayed cash-equity prices and 10-minute delayed derivatives prices are published free on asx.com.au; free 20-minute-delayed post-trade data is also offered.
- Pricing model & known ranges: Usage-based licensing under the **ASX Information & Technical Services Schedule of Fees**, billed per licensed use (per real-time display device/end-user, plus non-display/enterprise unit-of-count fees), reported monthly through DataBP. Exact per-user figures are set out in the fee schedule (PDF) but are not headline-published as a single rate; effectively "published in the fee schedule, quote-based for enterprise."

## 2. Data-domain coverage
- **Equities (real-time/delayed):** Level 1 (top of book) and Level 2 (full market depth) real-time; Level 1 also as a delayed service; EOD via vendors — the core product.
- **Derivatives:** ASX 24 futures/options (SPI 200, bank bills, bonds) real-time (10-min delayed public).
- **Indices:** S&P/ASX family (S&P/ASX 200, 50, 300, All Ordinaries) — calculated/published by S&P Dow Jones Indices under a JV with ASX.
- **Reference data:** instrument/security master, corporate-action and dividend data via ASX Reference Point / vendors.
- **Fundamentals:** company announcements and filings (Markit/ASX announcements platform); not a deep fundamentals vendor itself.
- **Corporate actions:** dividends, splits, entitlements distributed as data products.
- **Fixed income:** AGB/semi-government and listed debt quotes via ASX 24 and cash markets.
- **Macro:** not a macro provider.

## 3. Datasets
- Real-time top-of-book and full-depth order-book data for all ASX-operated cash and derivative markets; trade/quote and post-trade; index values and constituents; corporate actions and reference/security master; company announcements. History depth for tick/EOD is available via ASX archives and redistributors (multi-decade EOD through vendors). Proprietary assets: the ASX order book itself (definitive AU price formation) and the S&P/ASX index franchise (jointly with S&P DJI).

## 4. APIs & technical integration
- Direct: **ASX MarketSource** real-time feed, delivered over the premium ultra-low-latency **ASX ITCH** protocol (nanosecond time-stamping) with co-location in the Australian Liquidity Centre (ALC); FIX/OUCH for order entry (trading, not data). Delivery is a direct multicast/TCP feed for latency-sensitive firms.
- Indirect: most buy-side firms consume ASX data through vendor redistribution — **Bloomberg, LSEG/Refinitiv, FactSet, IRESS, Iress/EODHD** and others carry real-time, delayed or EOD ASX data.
- How a foreign buy-side firm accesses: either (a) take a vendor feed already carrying ASX (simplest — Bloomberg/LSEG/FactSet/IRESS), or (b) sign an ASX market-data agreement, connect to MarketSource directly or via an extranet, and self-report usage monthly through DataBP. Real-time professional use requires an ASX display/non-display licence regardless of route.

## 5. Enabling technology
- ASX Trade (NASDAQ OMX Genium INET) matching engine; ASX ITCH low-latency dissemination; Australian Liquidity Centre co-location and the ASX Net managed network. DataBP powers online data-licence administration and usage reporting. ASX has invested in cloud/managed connectivity for vendor and cloud delivery of reference and post-trade data.

## 6. Customer / user feedback
- As monopoly-adjacent domestic infrastructure, sentiment is functional rather than enthusiastic. Positives: authoritative, complete AU order-book data; strong co-lo and low-latency options; reliable reference data. Criticisms triangulated across industry press and market-data-cost commentary: exchange market-data and licensing fees are seen as expensive and administratively heavy (per-device reporting, audits), and the fee schedule is complex; competition concerns around ASX's central position recur in regulator (ASIC/ACCC) commentary. User segments: domestic and global banks, brokers, buy-side, trading firms, fintech/retail platforms, and data vendors redistributing the feed.

## 7. Edge & positioning
- Leads: definitive authority for Australian listed equities and derivatives — you cannot get canonical ASX price formation elsewhere; strong low-latency infrastructure and the S&P/ASX index franchise.
- Lags: no global reach (AU only); real-time access carries licensing cost and reporting friction; fundamentals/analytics are thin versus global vendors, so most users layer ASX data inside Bloomberg/LSEG/FactSet rather than consuming ASX direct. Best-for: any firm needing authoritative Australian market data — taken direct for latency-sensitive trading, or via a global vendor for research/portfolio use.

## 8. Provenance
- https://www.asx.com.au/connectivity-and-data/information-services/price-data/how-to-access-asx-price-data — ASX official access guide (accessed 2026-08-11)
- https://www.asx.com.au/connectivity-and-data/information-services/price-data/real-time-data — ASX real-time data/MarketSource (accessed 2026-08-11)
- https://www.asx.com.au/connectivity-and-data/information-services/price-data/delayed-price-data — ASX free delayed data (accessed 2026-08-11)
- https://www.asxonline.com/content/dam/asxonline/public/documents/market-information-product-and-services-guide.pdf — ASX information products & services guide (accessed 2026-08-11)
- https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/equities-market-data/australian-securities-exchange — LSEG ASX redistribution page (accessed 2026-08-11)
- https://www.interactivebrokers.com.au/en/pricing/market-data-pricing.php — Broker view of ASX data fees (accessed 2026-08-11)
- https://eodhd.com/asx-data — Independent vendor ASX data/API (accessed 2026-08-11)
