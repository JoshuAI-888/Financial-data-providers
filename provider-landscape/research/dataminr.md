# Dataminr

## 1. Snapshot
- **Owner/parent:** Independent/private (New York City, founded 2009). No parent company; investors include Goldman Sachs, Fidelity Investments, Valor Equity Partners, MSD Capital, NightDragon/HSBC (2025 $85M convertible + credit facility), and Fortress Investment Group ($100M convertible financing, 2025) for gen-AI/agentic product expansion. Total raised ~$1.24B; reported valuation ~$4.1B. Series F.
- **Coverage:** Real-time monitoring of 1M+ unique public data sources — social media, news wires, sensor/satellite data, public records, images, video, audio — in 150+ languages; global event/risk detection, not finance-sector-specific.
- **Free tier:** No. Enterprise-only, quote-based sales model with no public self-serve tier or trial found.
- **Pricing model & ranges:** Not publicly published; custom enterprise contracts. Third-party estimates put annual cost around $150,000–$300,000+/year, with per-user estimates cited around $500/month. Requires direct sales engagement for a quote.

## 2. Coverage
Global, cross-format event detection spanning social media, news wires, blogs, images/video/audio, sensor data, and public records, processed in 150+ languages via "Multi-Modal Fusion AI." Not limited to social/sentiment data — it spans physical security, geopolitical, cyber, supply-chain, and market-moving-event detection in one platform, positioned as the "institutional standard" for earliest-possible event/risk alerting rather than a finance-only sentiment feed.

## 3. Datasets
- Real-time event/alert stream identifying the "first credible signal" of an emerging event across all monitored source types.
- Financial-services-specific signal categories: market-moving events, company/executive risk events, supply-chain disruption, geopolitical and macro risk relevant to trading and portfolio risk management.
- Corporate/physical security and travel-risk alerting (used broadly across Fortune 50/100 and government customers, not just financial firms).
- Historical/backtest-style event archive (used alongside peers like RavenPack for systematic strategies, per third-party comparisons).

## 4. APIs & technical integration
- **API type:** Fully documented REST APIs for embedding Dataminr's alert/event outputs into partner platforms, dashboards, and automated routing/response systems (Dataminr API product, plus a public GitHub org "Dataminr-API").
- **Auth/delivery:** Enterprise-contract based; no public self-serve signup found. Also distributed via AWS Marketplace (Dataminr First Alert listing) and a Platform Partner Program for embedding into third-party tools.
- **MCP availability:** No official MCP server identified in research.
- **Integration model:** Positioned for connecting Dataminr's alert engine into a customer's own dashboards/workflows/response systems rather than as a raw queryable dataset.

## 5. Enabling technology
"Multi-Modal Fusion AI" — proprietary AI that correlates and cross-validates signals across text (150+ languages), image, video, audio, and sensor data in real time to detect the first credible signal of an emerging event, aiming to surface events before mainstream media reporting. Company messaging (2025 funding rounds) emphasizes an ongoing push into generative and agentic AI product features layered on top of the existing detection engine.

## 6. Customer / user feedback
Broad, large-scale enterprise/government adoption: reported customers include two-thirds of the Fortune 50, half of the Fortune 100, 100+ U.S. government agencies, and 20+ international governments; "most major banks already have it integrated" per third-party pricing commentary. G2 user rating around 4.5/5. Praised for real-time breaking-event coverage, single-pane-of-glass aggregation across many sources, and ease of use for alert triage. Recurring criticism: high subscription cost is a barrier for smaller firms; false positives occur (especially from fast-moving social signals) and every alert is described by users/newsrooms as "a lead requiring verification, not a confirmed fact"; alert explainability is limited by the complexity of the underlying AI, making it hard to justify individual alerts to stakeholders.

## 7. Edge & positioning
- **Leads on:** Speed/earliest-detection claim (>1M sources, cross-modal fusion), breadth beyond finance (physical security, geopolitical, government use cases), and sheer scale of institutional/government adoption — often cited as the incumbent "institutional standard" alongside RavenPack for event-driven signal detection.
- **Lags on:** Pricing accessibility/transparency (six-figure enterprise contracts only, no free or self-serve tier), explainability of AI-generated alerts, and finance-specific structured sentiment scoring (it is an event/alert detector, not a scored sentiment or entity-analytics feed like RavenPack/TipRanks).
- **Best-for:** Large banks, hedge funds, prop desks, corporate security/risk teams, and government agencies needing the earliest possible cross-source event alerting at enterprise budget and scale — not a fit for small teams, retail users, or anyone needing a transparent self-serve API.

## 8. Provenance
- https://www.dataminr.com/use-cases/financial-services/ — financial-services use case, coverage claims (accessed 2026-08-14; WebFetch blocked, relied on search index)
- https://github.com/Dataminr-API — public API org, confirms REST API product exists (accessed 2026-08-14)
- https://www.dataminr.com/press/announcement/dataminr-announces-100m-investment-from-fortress/ — Fortress $100M funding, gen-AI push (accessed 2026-08-14)
- https://www.dataminr.com/press/announcement/dataminr-secures-funding/ — $85M NightDragon/HSBC funding (accessed 2026-08-14)
- https://www.itqlick.com/dataminr/pricing — third-party pricing estimate ($150K-$300K+/yr) (accessed 2026-08-14)
- https://www.g2.com/products/dataminr/reviews — G2 rating (~4.5/5), pros/cons themes (accessed 2026-08-14)
- https://rolli.ai/blog/top-social-data-apis-for-quantitative-trading-2026/ — positions Dataminr vs. RavenPack as peers (accessed 2026-08-14)
- https://aws.amazon.com/marketplace/pp/prodview-7eav2xsxvnupy — Dataminr First Alert AWS Marketplace listing (accessed 2026-08-14)

**Note:** WebFetch to dataminr.com was egress-blocked in this environment; all findings rely on the WebSearch index and third-party secondary sources (press releases, review sites, marketplace listings) rather than direct page retrieval. Exact current pricing is not publicly disclosed by Dataminr and the figures above are third-party estimates.
