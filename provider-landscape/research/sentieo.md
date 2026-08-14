# Sentieo (an AlphaSense company)

## 1. Snapshot
- **Owner/parent:** Independent (founded 2012, San Francisco) until acquired by **AlphaSense** in May 2022; operates as a wholly-owned subsidiary/brand ("Sentieo, an AlphaSense company"). AlphaSense itself was founded 2011, is backed by Viking Global, BDT & MSD Partners, Alkeon, SoftBank Vision Fund 2, J.P. Morgan Growth Equity Partners and others, and was valued at ~$4B after a $650M raise in mid-2024 (also used to fund AlphaSense's $930M acquisition of Tegus, which had separately acquired BamSEC and Canalyst).
- **Coverage:** Filings from 68,000+ companies globally (SEC + international regulators), earnings-call/investor-conference transcripts, IR documents and press releases; Wall Street Insights broker research from ~1,000 sell-side/independent firms; an Expert Transcript Library (~200,000 transcripts across ~25,000 companies, originally built via Sentieo's GLG content redistribution deal). Combined AlphaSense platform indexes 500M+ third-party documents.
- **Free tier:** No public self-serve free tier; platform is sold on annual enterprise/professional contracts (demo/trial only via sales).
- **Pricing model & ranges:** Custom, quote-only, seat-based annual contracts. Public data points put most seats around **$10,000–$40,000+ per user/year**; one third-party estimate puts AlphaSense's median annual contract near **$18,375**, comparable to or below Bloomberg Terminal (~$24k/yr) and FactSet/LSEG Workspace (~$22k/yr). Requires direct sales contact for a quote.

## 2. Coverage
Global equities and credit research use case, historically strongest on **US-listed and large global-cap companies** given its broker-research and transcript sourcing. Company filings span SEC EDGAR plus major non-US regulators (documented at 68K+ companies), earnings call/IR transcripts, and press releases. Reviewers note international/private-company financial-statement depth is thinner than the document/transcript coverage — some G2 reviewers flag "financial data coverage could be more comprehensive, particularly for international markets." The 2024 Tegus acquisition materially deepened private-company and expert-call coverage.

## 3. Datasets
- Company filings (10-K/10-Q/8-K/proxy, global equivalents), transcripts of earnings calls and investor conferences, IR presentations, press releases.
- **Wall Street Insights**: aggregated broker/sell-side and independent research notes across sectors, industries and companies.
- **Expert Transcript Library**: investor-led expert-network call transcripts (~200K transcripts / ~25K companies) — largest such library reported by the company.
- Legacy Sentieo datasets: financial-model templates, a document/notebook workspace layer, and NLP-derived "Smart Summary" and "Heatmap" outputs for earnings transcripts, layered over the raw source documents rather than sold as standalone data.
- Post-merger, also inherits Tegus expert-call and private-company financial data, and Canalyst's standardized/normalized financial models.

## 4. APIs & technical integration
AlphaSense (parent) exposes a developer platform at `developer.alpha-sense.com`: **REST API** for auth/document management (base `https://api.alpha-sense.com`, Bearer-token auth via `/auth`) and a **GraphQL API** (`/gql` endpoint) for flexible querying, plus a JavaScript SDK. An **Ingestion/Content-Ingestion API** lets enterprise clients sync internal documents (research notes, models) into the shared workspace, with near-real-time processing/auto-tagging. This is Enterprise Intelligence tooling, not a public self-serve data API — access requires a contract, and technical support is via `apisupport@alpha-sense.com`. The end-user product itself is primarily a web application (search, notebook, Excel/Office plug-ins) rather than an API-first data feed.

## 5. Enabling technology
NLP/ML-driven document search and summarization: **Smart Summary** (categorizes and sentiment-tags earnings-call commentary by speaker and topic) and **Heatmap** (cross-company/peer-group sentiment and business-driver comparison over time), both built on Sentieo's original NLP stack, now folded into AlphaSense's broader generative-AI layer (AI-powered semantic search, "AI Assist"/summarization across the merged AlphaSense+Sentieo+Tegus corpus). Positioned as a high-recall semantic/AI search engine over unstructured text rather than a structured-data computation engine.

## 6. Customer / user feedback
Over 1,100 (Sentieo legacy) / far more post-merger customers, including 800+ institutional investment firms. G2 reviewers consistently praise document search speed/relevance and workflow time-savings from unifying filings, transcripts and broker research in one workspace. Criticism centers on (a) financial-data/international coverage gaps versus FactSet/Bloomberg, (b) high, opaque enterprise pricing requiring sales negotiation, and (c) post-acquisition product consolidation causing some feature/workflow disruption for legacy Sentieo users migrating to the AlphaSense UI.

## 7. Edge & positioning
- **Leads on:** semantic/NLP search across a huge unstructured corpus (filings + transcripts + broker research + expert calls) in one workspace; speed of finding a specific disclosure or quote across thousands of documents; AI-generated summarization of earnings calls.
- **Lags on:** structured, calculation-ready fundamental/market data depth (vs FactSet, Capital IQ, Bloomberg); transparent/self-serve pricing; non-US/emerging-market data depth.
- **Best-for:** buy-side/sell-side equity research and corporate-strategy teams doing qualitative document research, competitive intelligence and expert-call sourcing, who already have (or don't need) a separate structured-data terminal.

## 8. Provenance
- https://www.g2.com/products/sentieo-by-alphasense/reviews — G2 review summary, pricing signals (accessed 2026-08-14)
- https://www.centana.com/2022/05/10/alphasense-acquires-sentieo/ — 2022 Sentieo acquisition announcement (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/alphasense-completes-acquisition-of-tegus-302190934.html — 2024 Tegus acquisition, $930M/$650M raise (accessed 2026-08-14)
- https://www.alpha-sense.com/resources/product-articles/what-is-alphasense/ — platform overview, document coverage figures (accessed 2026-08-14)
- https://developer.alpha-sense.com/api/getting-started — REST/GraphQL API, auth endpoints (accessed 2026-08-14)
- https://www.alpha-sense.com/blog/product/smart-summaries-earnings-analysis/ — Smart Summaries NLP feature detail (accessed 2026-08-14)
- https://www.g2.com/compare/factset-investment-research-vs-sentieo-by-alphasense — competitive positioning vs FactSet (accessed 2026-08-14)
- https://elevatedsignal.com/compare/alphasense/ — pricing range estimates, median contract value (accessed 2026-08-14)

Note: WebFetch to alpha-sense.com, developer.alpha-sense.com and g2.com was egress-blocked in this environment; all facts above are triangulated from WebSearch result snippets across ≥2 independent secondary sources, not direct primary-source page fetches.
