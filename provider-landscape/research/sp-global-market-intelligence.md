# S&P Global Market Intelligence

## 1. Snapshot
- **Owner/parent:** Division of S&P Global Inc. (NYSE: SPGI). **HQ:** New York, NY. Market Intelligence traces to S&P + IHS Markit heritage (merged 2022); Compustat launched 1962.
- **Scale signal:** Market Intelligence segment revenue >$4.5B (2024); part of ~$14B+ S&P Global. AI arm Kensho acquired 2018 (~$550M).
- **Positioning one-liner:** Deepest fundamentals + estimates + private-company + credit-ratings franchise, delivered via the Capital IQ Pro desktop and Xpressfeed/Marketplace feeds; a Bloomberg/FactSet workflow rival strongest on fundamental and reference data breadth.
- **Pricing model:** Enterprise, negotiated, not publicly disclosed. Per-seat Capital IQ Pro estimates range widely (third-party figures ~$13k–$40k+/user/yr; feeds/enterprise deals far higher). Configured per customer by seats, modules, datasets, real-time exchange data, and delivery channel.

## 2. Asset-class coverage
- **Public equity:** Best-in-class. Compustat + Capital IQ fundamentals on 150k+ public companies; consensus/detailed estimates, ownership, transactions, transcripts, filings. Deep US and global.
- **Private equity / VC:** Strong. 10M+ private companies (Capital IQ + Private Company financials); M&A/transactions, corporate relationships, key developments. (Note: private-markets deal intelligence overlaps with peers like PitchBook/Preqin, covered elsewhere.)
- **Fixed income & credit:** Strong via RatingsDirect (S&P Global Ratings credit ratings + research on Capital IQ Pro), credit risk indicators (market-derived signals, PD), fixed-income reference/pricing, leveraged loan & CLO (LCD heritage).
- **Other:** S&P Dow Jones Indices (sister division, separate); S&P Global Ratings; commodities/energy (Platts, Commodity Insights sister division); ESG/Sustainable1; supply chain (Panjiva); Kensho AI datasets; alternative & third-party data via Marketplace.

## 3. Datasets
- **Compustat** — flagship standardized fundamentals; 80k+ companies globally, 3,000+ data items; North America history to 1950, standardized annual/interim to 1979, **point-in-time snapshots since 1987** (survivorship/restatement-bias-free) — the quant-research standard.
- **Capital IQ financials** — as-reported + standardized; 150k+ public, 10M+ private.
- **Estimates** — consensus + detailed broker estimates; point-in-time estimate history captured since Aug 2016, ~2-hourly updates with timestamps.
- **RatingsDirect / S&P Global Ratings** — issuer & issue credit ratings + rationale, incl. global issuers, US public finance, structured finance histories.
- Ownership, transactions/M&A, key developments, transcripts (Kensho-transcribed), filings, corporate relationships, supply-chain (Panjiva), leveraged loan (LCD).

## 4. APIs & technical integration
- **Capital IQ Pro** — flagship web/desktop terminal with Office (Excel/PowerPoint) plug-in.
- **Xpressfeed** — bulk data-feed management; 200+ datasets; zipped packages via SFTP or Xpressfeed Web Service; relational/point-in-time delivery for warehousing.
- **ClariFI** — quant alpha-research & portfolio platform; RESTful JSON **ClariFI API** for raw + analytical data.
- **S&P Global Marketplace** — dataset discovery/licensing storefront; GenAI search (2024).
- **Cloud:** Snowflake Marketplace and cloud-to-cloud delivery; AWS/Databricks-oriented distribution. Kensho AI-ready textual data API (beta) for transcripts/filings.
- **Auth/format:** enterprise API keys/OAuth; CSV/JSON/relational; mostly EOD/intraday reference data (real-time exchange feeds separately licensed). Redistribution tightly licensed per contract.

## 5. Enabling technology
- **Kensho** (S&P Global AI arm): FinAI stack — Scribe (financial speech-to-text/transcripts), Link (entity resolution/mapping to S&P IDs), Extract, Classify, NERD (named-entity), and ChatIQ (GenAI natural-language access to Capital IQ data).
- **Entity/symbology:** proprietary company/security master (S&P Capital IQ IDs, CIQ tickers); Kensho Link for third-party entity matching — a core differentiator.
- **Cloud strategy:** feed + warehouse-native delivery (Snowflake/cloud endpoints); LLM-ready data packaging; Marketplace for data-as-a-service.

## 6. Customer / user feedback
- **G2:** S&P Capital IQ Pro ~4.3/5 (broadly "comprehensive data, good UX"; page egress-blocked, triangulated via search snippets and SoftwareAdvice/Capterra summaries).
- **TrustRadius / SoftwareAdvice / Capterra:** consistently positive on data breadth; 100+ reviews aggregate across compare pages.
- **PROS:** unrivaled fundamental + private-company depth; Excel plug-in and screening; reliable, widely used in IB/PE/research; strong transcripts/filings.
- **CONS:** cluttered/steep-learning-curve UI; premium price and opaque negotiation; some real-time/market-data gaps vs Bloomberg; module-based licensing frustration.
- **Segments:** investment banking, PE/VC, corporate development, asset managers, academic/quant researchers (Compustat via WRDS).

## 7. Edge & positioning
- **Leads:** fundamentals & estimates (Compustat point-in-time is the quant gold standard); private-company breadth (10M+); combined ratings + fundamentals + private data under one roof; entity resolution (Kensho Link). Why: 60+ years of standardized history + IHS Markit reference-data merger + in-house AI.
- **Lags:** real-time trading/markets terminal experience trails Bloomberg; charting/news immediacy and chat/community weaker; UI modernization ongoing; ESG ratings less dominant than MSCI/Sustainalytics.

## 8. Provenance
- https://www.spglobal.com/market-intelligence/en/solutions/products/estimates — Estimates product (2026-08-10)
- https://pages.marketintelligence.spglobal.com/SP-Capital-IQ-Pro-Data-Coverage.html — Capital IQ Pro / Xpressfeed coverage (2026-08-10)
- https://en.wikipedia.org/wiki/Compustat — Compustat history/coverage (2026-08-10)
- https://www.marketplace.spglobal.com/en/datasets/compustat-financials-(8) — Compustat dataset detail (2026-08-10)
- https://www.spglobal.com/market-intelligence/en/solutions/products/clarifi — ClariFI + REST API (2026-08-10)
- https://press.spglobal.com/2022-02-17-S-P-Global-Market-Intelligence-Launches-Enhanced-RatingsDirect — RatingsDirect on CIQ Pro (2026-08-10)
- https://kensho.com/solutions/core-ai-capabilities — Kensho FinAI stack (2026-08-10)
- https://press.spglobal.com/2024-02-06-S-P-Global-Launches-Generative-AI-Search-on-the-S-P-Global-Marketplace — Marketplace GenAI search (2026-08-10)
- https://www.geminiq.com/blog/capital-iq-pricing-cost-explained — pricing estimates (2026-08-10)
- https://s29.q4cdn.com/690959130/files/doc_downloads/2025/07/S-P-Global-Investor-Fact-Book-with-2024-financials-Published-7-22-2025.pdf — segment revenue (2026-08-10)
