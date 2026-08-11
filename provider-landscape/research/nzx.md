# NZX (New Zealand's Exchange)

## 1. Snapshot
- Owner/parent: **NZX Limited** (self-listed, NZX: NZX). HQ Wellington, New Zealand; roots to 19th-century regional exchanges, consolidated as NZX in 2003. Positioning: New Zealand's sole registered securities exchange and the authoritative source of NZ market data; also a diversified operator (Smartshares/SuperLife funds, Wealth Technologies, dairy derivatives).
- **Regions/markets covered:** New Zealand only — NZX Main Board equities, NZX Debt Market (NZDX), NZX Derivatives/NZCX (dairy and equity derivatives), Fonterra Shareholders' Market, and the S&P/NZX index family. Small home market but the definitive NZ venue.
- **Free tier:** Yes — delayed prices, tables, announcements and charts are available on nzx.com; real-time is licensed.
- Pricing model & known ranges: Licensed market data, direct from NZX or via authorised vendors/distributors; fees are quote/agreement-based and not publicly headline-disclosed. Data enquiries via data@nzx.com.

## 2. Data-domain coverage
- **Equities (real-time/delayed):** NZX Main Board real-time Level 1 and market-depth; delayed public feed — the core product.
- **Fixed income:** NZX Debt Market (NZDX) quotes and reference.
- **Derivatives:** NZX/NZCX equity and dairy derivatives (e.g. milk-price futures) market data.
- **Indices:** S&P/NZX family (headline **S&P/NZX 50**) — since 2015 calculated, published and distributed by S&P Dow Jones Indices under a strategic partnership; NZX co-brands.
- **Reference data:** security master, corporate actions, announcements.
- **Corporate actions:** dividends, capital changes distributed with the feed.
- **Fundamentals / macro:** not a fundamentals or macro vendor; company disclosures flow through the NZX announcements platform.

## 3. Datasets
- Real-time and delayed price/depth across equities, debt and derivatives; index values and constituents; company announcements; reference and corporate-action data. Feed products include Real-Time and Delayed price XML feeds, Tables, Announcements and Charts, plus Nasdaq ME **ITCH** and the **NZX Market Depth Feed (MDF)**. History depth is shallow relative to large markets but complete for NZ; deeper history via redistributors. Proprietary assets: the NZX order book (definitive NZ prices) and the S&P/NZX index franchise. (Note: NZX Wealth Technologies is a wealth-admin/custody software business, distinct from the exchange market-data feed.)

## 4. APIs & technical integration
- Feed types: Nasdaq ME ITCH real-time feed and NZX Market Depth Feed (MDF); XML feed products (real-time/delayed prices, tables, announcements, charts); packaged data delivered securely to client systems. NZX runs on a Nasdaq-powered trading/data platform.
- Delivery: direct from NZX, through licensed vendors/distributors, or as packaged data products.
- How a foreign buy-side firm accesses: NZX data is redistributed by global vendors — **Bloomberg, LSEG/Refinitiv, FactSet, IRESS, and ICE** (ICE lists NZX in its fixed-income/data catalog) — so most offshore firms simply take it inside an existing terminal. Direct access requires an NZX market-data licence (contact data@nzx.com) and connection to the ITCH/MDF feed or an XML product.

## 5. Enabling technology
- Trading and market-data platform supplied by **Nasdaq** (matching engine and ITCH dissemination); MDF for depth. NZX partners with S&P DJI for index calculation. Data-ops centre on the Nasdaq ME stack plus XML product delivery and vendor redistribution; scale is modest, so infrastructure is largely vendor-provided rather than bespoke low-latency.

## 6. Customer / user feedback
- Feedback is thin (small market). Positives: single authoritative NZ source; clean integration with global vendors; Nasdaq-based platform is standard and interoperable. Criticisms triangulated from NZ market commentary: limited liquidity and breadth constrain the data's standalone value; NZX as a business has faced periodic scrutiny over market-operation performance and technology outages (e.g. 2020 DDoS-related trading halts) which reflect on infrastructure resilience. User segments: NZ banks/brokers, KiwiSaver and fund managers, Australian buy-side, index/ETF providers, and global vendors redistributing the feed.

## 7. Edge & positioning
- Leads: the only authoritative source of New Zealand listed equity, debt and derivatives data, plus the S&P/NZX index franchise. Lags: tiny universe and liquidity, shallow native history, no global reach, and real-time licensing friction — offshore firms almost always consume NZX via Bloomberg/LSEG/FactSet/IRESS rather than direct. Best-for: NZ-focused managers and index/ETF products needing canonical NZ prices; for a global buy-side firm, take NZX through an existing vendor feed.

## 8. Provenance
- https://www.nzx.com/services/products-tools/data-connectivity — NZX data & connectivity overview (accessed 2026-08-11)
- https://www.nzx.com/services/data-connectivity/nzx-market-data/vendors-distributors — NZX authorised vendors/distributors (accessed 2026-08-11)
- https://www.nzx.com/products/nzx-info — NZX data products (accessed 2026-08-11)
- https://developer.ice.com/fixed-income-data-services/catalog/new-zealand-exchange-nzx — ICE NZX redistribution catalog (accessed 2026-08-11)
- https://www.spglobal.com/spdji/en/indices/equity/sp-nzx-50-index/ — S&P/NZX 50 index (S&P DJI) (accessed 2026-08-11)
- https://en.wikipedia.org/wiki/S%26P/NZX_50 — S&P/NZX 50 background & partnership (accessed 2026-08-11)
- https://en.wikipedia.org/wiki/NZX — NZX corporate/ownership overview (accessed 2026-08-11)
