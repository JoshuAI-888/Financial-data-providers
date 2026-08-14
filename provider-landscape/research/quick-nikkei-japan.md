# QUICK Corp (Nikkei Group)

## 1. Snapshot
- **Owner/parent:** QUICK Corp — a member of the Nikkei Group (Nikkei Inc.), Japan's dominant financial/business media company; QUICK was founded in 1971 as Quotation Information Center K.K. and renamed to the QUICK acronym in 1987.
- **Coverage:** Japan-focused financial market data — real-time price/quote data, company profiles, market depth, pre-opening quotes, corporate fundamentals, and Japan-specific alternative data.
- **Free tier:** No public free tier; core products (QUICK Professional terminal, QUICK Feed-API, QUICK Data Factory) are commercial/subscription services.
- **Pricing model & ranges:** Monthly-license pricing model referenced for its data feeds/news; specific rates not publicly published — quote-based via direct contact (e.g., for NQN/Nikkei QUICK News market-news pricing).

## 2. Coverage
QUICK is described as Japan's largest financial information vendor, providing an information infrastructure underpinning Japan's securities and financial markets. Its market-data coverage spans domestic securities exchanges — Tokyo Stock Exchange (via FLEX, Tdex+ feeds), the former Osaka Exchange (market information, J-GATE) and Japan's proprietary trading systems (PTS) — including price, company profile, market depth, pre-opening quote and reference price data. QUICK Consensus (analyst/macro forecast aggregation) has, since 2005, the widest coverage of Japanese equities including mid- and small-cap names — a notable differentiator versus foreign vendors whose Japan consensus coverage typically concentrates on large caps.

## 3. Datasets
Core proprietary content: QUICK Feed (a consolidated, record-based stock-price data feed spanning Japanese exchanges plus QUICK's own value-added data — company profiles, indices, related information); QUICK Consensus (broad-coverage analyst/earnings and macroeconomic forecast aggregation, notably deep in mid/small-cap Japanese names); NQN (Nikkei QUICK News) market news; and QUICK Data Factory, a marketplace-style platform aggregating Japanese alternative data both from QUICK itself and from third-party vendors. This alternative-data marketplace positioning is a distinguishing feature relative to the other regional providers in this set.

## 4. APIs & technical integration
QUICK Feed-API facilitates system-to-system data receipt from the consolidated QUICK Feed, deliverable over the internet or a dedicated leased line. A self-service developer portal provides data guides, user manuals, API testing tools, sample code and usage statistics in a single access point — a relatively modern, self-serve developer experience compared to some other regional vendors in this set. No public evidence of an MCP server or LLM-native integration; "QUICK Data Factory" functions as an alternative-data distribution platform rather than an LLM/AI product per se.

## 5. Enabling technology
Public materials describe QUICK Feed as a "first-rate high-speed feed" that incorporates exchange system/product changes in a timely manner, and highlight a self-service developer portal as core to its API strategy. QUICK Data Factory's alternative-data marketplace model (aggregating third-party vendor data alongside QUICK's own) suggests a data-ops/distribution-platform orientation rather than published AI/ML feature investment. No specific entity-resolution or AI/LLM capability disclosures were found.

## 6. Customer / user feedback
Independent customer-review coverage is limited (QUICK is enterprise/B2B, Japan-market-focused, with little English-language retail review presence). It is listed as a recognized data provider on the AlternativeData.org industry directory and on Datarade's provider marketplace, indicating industry recognition as a legitimate alternative-data source, though without detailed pros/cons user commentary surfaced in this research. Segments served, per its own positioning, include Japanese brokers' financial advisers (via the Qr1 terminal) and institutional/quant users of its consensus and alternative-data products.

## 7. Edge & positioning
- **Leads on:** Depth and breadth of Japanese equity market data, notably mid/small-cap analyst-consensus coverage since 2005 that exceeds typical foreign-vendor Japan coverage; long operating history (real-time terminal data since 1971) and deep exchange-system integration (TSE FLEX/Tdex+, former OSE J-GATE, PTS); a differentiated alternative-data marketplace (QUICK Data Factory) aggregating third-party Japan-specific datasets; self-service developer portal for API access.
- **Lags on:** Coverage is essentially Japan-only (no meaningful non-Japan market data found in this research); pricing opacity typical of the category; thin independent/English-language customer review base makes external validation difficult; Nikkei Group affiliation ties its market-news content closely to Nikkei's own editorial output rather than fully independent news sourcing.
- **Best-for:** Institutional investors, brokers and quant/alternative-data teams needing authoritative, exchange-grade Japanese equity market data (including deep mid/small-cap consensus coverage) or access to a curated marketplace of Japan-specific alternative datasets.

## 8. Provenance
- https://corporate.quick.co.jp/en/apis/ — QUICK APIs overview (accessed 2026-08-14)
- https://corporate.quick.co.jp/en/service/professional/ — QUICK Professional terminal product page (accessed 2026-08-14)
- https://corporate.quick.co.jp/data-factory/en/ — QUICK Data Factory alternative-data platform (accessed 2026-08-14)
- https://www.nikkei.co.jp/nikkeiinfo/en/global_services/quick.html — Nikkei Inc. description of QUICK as group company (accessed 2026-08-14)
- https://alternativedata.org/data_provider/quick-corp-a-nikkei-company/ — AlternativeData.org provider directory listing (accessed 2026-08-14)
- https://datarade.ai/data-providers/quick/profile — Datarade marketplace profile for QUICK (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/QUICK_Corp — QUICK Corp company background (Wikipedia, via search index; accessed 2026-08-14)
- https://datarade.ai/data-products/nqn-nikkei-quick-news-market-news-quick — NQN Nikkei QUICK News product listing (accessed 2026-08-14)
- Note: WebFetch to quick.co.jp and en.wikipedia.org was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches.
