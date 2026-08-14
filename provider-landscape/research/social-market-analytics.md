# Social Market Analytics (SMA)

## 1. Snapshot
- **Owner/parent:** Social Market Analytics, Inc. — Chicago-based independent company, founded 2012 by Joe Gits, Jeff Blaschak, and Kurt Myers. The company has also operated/rebranded under the name **Context Analytics Inc.** in industry references, though "Social Market Analytics" / "SMA" remains the primary brand for its flagship S-Factors product.
- **Coverage:** Institutional social-sentiment analytics derived primarily from Twitter/X data (and other social sources), covering equities and commodities; distributed to institutional and active-trader audiences via partners including Interactive Brokers, Fidelity, CBOE, and IHS Markit. Reports serving 4,000+ investors including top hedge funds and long-only asset managers.
- **Free tier:** No public self-serve free tier found; access is via institutional data subscriptions or bundled through broker/vendor partnerships (e.g., Interactive Brokers' research offerings), not direct self-signup.
- **Pricing model & ranges:** Not publicly published — institutional licensing model (per-seat/per-feed contracts negotiated directly or delivered through vendor partners such as Bloomberg-style terminal integrations, Interactive Brokers, and Fidelity's research marketplace). No public rate card identified.

## 2. Coverage
US-centric equity and commodity social-sentiment analytics, sourced primarily from Twitter/X activity (the company was an early, X-recognized case study — featured in Twitter's own 2016 "Twitter Data and the Financial Markets" blog post) and expanded to near-real-time coverage of commodities alongside its original equities focus. Positioned as one of a small handful of ticker-level social-sentiment specialists (alongside PsychSignal and iSentium) rather than a broad multi-asset or multi-source aggregator. Coverage breadth (number of tickers/entities) not independently confirmed in available sources — flagged as a research gap.

## 3. Datasets
- **S-Factors™:** a patented family of **seven sentiment metrics** derived from social-media (primarily Twitter/X) text, including the flagship **S-Score™** (a weighted, normalized representation of sentiment over a lookback period) and **S-Dispersion™** (a measure of tweet-source concentration contributing to the S-Score). Additional S-Factors quantify volume, sentiment momentum/change, and reliability/pervasiveness of signal.
- Delivered as a **near real-time, streaming, up-to-the-minute** sentiment feed for both equities and commodities.
- Backed by published research/whitepapers (including an Interactive Brokers-hosted white paper) claiming that measured sentiment changes reliably precede/correlate with price changes, and that larger sentiment swings associate with larger price moves.
- Patented scoring methodology is a specific differentiator versus competitors that use unpatented/generic NLP sentiment scoring.

## 4. APIs & technical integration
- **API type:** Streaming/real-time data feed (exact protocol not independently confirmed — described in marketing material as "streaming up-to-the-minute" delivery); also distributed through third-party platform integrations rather than purely direct API self-service.
- **Auth/delivery:** Distributed via institutional data-vendor channels — notably as a built-in **Interactive Brokers** third-party research/technology integration (available directly within IBKR's trading platform), and referenced by Fidelity's research-vendor directory. This vendor-embedded distribution model (versus a raw public API) appears to be SMA's primary go-to-market channel for individual/active-trader access.
- **MCP availability:** No official MCP server identified.
- **Direct developer documentation:** Not found in public search results beyond a FAQ/whitepaper PDF; suggests SMA is not primarily developer-self-serve oriented, consistent with its institutional/vendor-embedded distribution.

## 5. Enabling technology
Patented natural-language sentiment-scoring algorithm applied to real-time social-media (Twitter/X) text streams, producing normalized, weighted time-series sentiment metrics (the S-Factors family) rather than raw mention counts. Emphasis on statistical rigor — published methodology papers argue for predictive validity of sentiment shifts on subsequent price action — positioning SMA as a quantitative/academic-grounded sentiment vendor rather than a simple mention-counting tool.

## 6. Customer / user feedback
Limited independent review coverage found (this is a B2B/institutional product without consumer review-site presence). Distribution/partnership evidence serves as the strongest available proxy for market trust: embedding within Interactive Brokers' and Fidelity's platforms, plus historical association with CBOE and IHS Markit, indicates institutional credibility and multi-decade-plus staying power (founded 2012, still actively referenced in IBKR's current research offerings as of this research). Claimed user base of 4,000+ investors spanning hedge funds and long-only asset managers. No negative/critical independent reviews were surfaced in available search results — a notable gap given SMA's institutional, low-public-visibility positioning.

## 7. Edge & positioning
- **Leads on:** patented, academically-validated sentiment methodology (S-Factors/S-Score/S-Dispersion) with a long operating history (since 2012) and credible institutional distribution (Interactive Brokers, Fidelity, CBOE, IHS Markit) — a rare combination of "boutique specialist" credibility with broker-embedded reach.
- **Lags on:** transparency (no public pricing, limited public API documentation, no self-serve developer signup) and source diversity (primarily Twitter/X-centric versus RavenPack's 40,000+ multi-source, multi-language coverage).
- **Best-for:** institutional and active traders who already use Interactive Brokers or similar platforms and want an embedded, statistically-grounded social-sentiment signal for equities/commodities rather than a raw social-media firehose.

## 8. Provenance
- https://activetraders.socialmarketanalytics.com/pdfs/SMA_FAQ_PDF.pdf — official S-Factors FAQ/methodology PDF (accessed 2026-08-14)
- https://www.interactivebrokers.com/download/sma_white_paper.pdf — official/partner-hosted SMA white paper (accessed 2026-08-14)
- https://www.interactivebrokers.com/en/trading/sma-technology.php — Interactive Brokers product-integration page (accessed 2026-08-14)
- https://research2.fidelity.com/fidelity/research/reports/release2/Research/SMA.asp — Fidelity research-vendor listing (accessed 2026-08-14)
- https://www.socialmarketanalytics.com/2015/07/07/predictive-power-of-sma-s-factors/ — official company research post on predictive validity (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20150616005445/en/World-Leader-in-Predictive-Equities-Sentiment-Introduces-Near-Real-Time-Commodities-Sentiment-Analysis-for-Institutional-and-Active-Trader-Markets — press release on commodities-sentiment expansion (accessed 2026-08-14)
- https://blog.x.com/en_us/topics/insights/2016/twitter-data-and-the-financial-markets — Twitter/X's own blog featuring SMA as a case study (accessed 2026-08-14)
- https://alternativedata.org/data_provider/social-market-analytics/ — independent alt-data directory listing, partner/client claims (accessed 2026-08-14)

**Note:** WebFetch to socialmarketanalytics.com and interactivebrokers.com was egress-blocked in this environment; findings rely on the WebSearch index and cached/indexed content rather than direct page retrieval. Pricing and exact coverage-breadth figures were not found in public sources and are flagged as gaps.
