# Daloopa

## 1. Snapshot
- **Owner/parent:** Independent, venture-backed (Daloopa, Inc.). **HQ:** New York, NY. **Founded:** 2019 by Thomas Li (ex-Point72 analyst), Jeremy Huang (ex-Airbnb/Meta) and Daniel Chen (ex-Microsoft). **Positioning:** AI-plus-human "financial data infrastructure" that extracts auditable, source-linked fundamentals, KPIs and guidance from filings, transcripts, IR decks and press releases for analysts and AI agents.
- **M&A:** No acquisitions; strategic backers include Morgan Stanley and Pavilion/Temasek's Pavilion Capital. Announced a partnership with Anthropic's Claude for Financial Services.
- **Regions/markets covered:** Global equities — the historical dataset covers 5,500+ public companies globally (broader than US-only), sourced from disclosed filings/decks. Deepest on US GAAP filers.
- **Free tier:** No standard self-serve free tier; free trial / demo via sales. A free Claude Code plugin (analysis "skills") exists but the underlying data requires a subscription/API key.
- **Pricing model & known ranges:** Enterprise subscription (platform + Excel add-in + API), quote-based; **not publicly disclosed.** Funding: ~$18M Series B (Aug 2025, Touring Capital, Morgan Stanley participating) plus a $13M strategic round (Jul 2025); a further ~$47M round was reported (Jun 2026, AlleyWatch), taking total raised to roughly $100M.

## 2. Data-domain coverage
- **fundamentals:** Core offering — income statement, balance sheet, cash flow, standardized and as-reported, every cell hyperlinked to the source page.
- **filings:** Ingests SEC filings (10-K/10-Q/8-K), press releases and investor presentations as extraction sources.
- **transcripts/expert calls:** Uses earnings-call transcripts as an extraction source for guidance/KPIs; not an expert-network provider.
- **qualitative research:** Management guidance and non-GAAP/operational KPIs captured; limited narrative research.
- **private-company data:** No — public filers only.
- **entity/knowledge graph:** Structured, ticker-linked line-item data; not a general knowledge graph.

## 3. Datasets
- Detailed line-item KPIs, segment data, non-GAAP metrics and management guidance — Daloopa markets "up to 10x more data points per company" than typical vendors, including granular operating metrics most feeds omit.
- History depth typically multi-year back to available filings; ~5,500+ companies globally.
- **Sourcing method:** Proprietary machine-learning extraction (parsing filings/tables/decks) with human analyst review (human-in-the-loop QA) and cell-level source hyperlinking for auditability.
- **Proprietary holdings:** The structured, source-linked KPI/guidance dataset and the model-refresh mapping that updates a user's own Excel model at earnings.

## 4. APIs & technical integration
- **API:** Structured REST endpoints for fundamentals, KPIs and SEC-filing data; API-key auth; JSON output; webhook-driven update automation for ingestion into data warehouses/internal apps.
- **Excel add-in:** Populates and one-click-refreshes native Excel models with source-linked data and formulas after earnings.
- **MCP server:** Yes — hosted MCP server (mcp.daloopa.com) exposing company fundamentals, KPIs and filings to LLM clients; a **new MCP connector for Microsoft 365 Copilot** was announced (2026). Claude Code plugin with ~10 analysis "skills."
- **AI/LLM features:** Positioned as grounding data for AI agents; Daloopa cites large retrieval-accuracy gains for agents grounded on its data vs. web retrieval.

## 5. Enabling technology
- Proprietary AI/ML extraction pipeline (document layout + table parsing + NLP) over filings, transcripts and IR decks.
- Human-in-the-loop analyst verification layer for accuracy; every data point retains a hyperlink to its exact source location for audit.
- Data-ops built around fast earnings-season model refresh and webhook update automation.

## 6. Customer / user feedback
- **Ratings:** Sparse on major review sites; FeaturedCustomers hosts ~15 customer references/testimonials; positive listings on Futurepedia and vendor directories (LSE Directory, idp-software). No large G2/Capterra sample.
- **Pros:** Auditability (cell-level source links), breadth/granularity of KPIs, fast model refresh at earnings, strong for AI-agent grounding.
- **Cons:** Enterprise pricing (no cheap self-serve tier), US-centric depth, limited independent third-party review volume.
- **User segments:** 160+ hedge funds, mutual funds and bulge-bracket banks; increasingly AI platforms (cited: Anthropic, OpenAI, Perplexity) using it as a grounding data layer.

## 7. Edge & positioning
- **Leads:** Depth of source-linked line-item fundamentals/KPIs and auditability — a differentiator versus black-box or web-scraped data; strong AI-agent grounding story and modern MCP/Excel integration.
- **Lags:** No expert calls/qualitative research, no private-company data, thinner outside US filers, limited public pricing/reviews.
- **Best for:** Fundamental analysts and quant/AI teams that need granular, auditable, model-ready fundamentals and KPIs delivered into Excel or LLM agents.

## 8. Provenance
- https://daloopa.com/products/api — official API product page (accessed 2026-08-11)
- https://docs.daloopa.com/docs/daloopa-mcp — official MCP server docs (accessed 2026-08-11)
- https://daloopa.com/products/mcp — official MCP product page (accessed 2026-08-11)
- https://techcrunch.com/2024/05/07/daloopa-trains-ai-to-automate-financial-analysts-workflows/ — TechCrunch founder/funding profile (accessed 2026-08-11)
- https://www.alleywatch.com/2026/06/daloopa-structured-financial-data-infrastructure-ai-investment-research-thomas-li/ — 2026 funding/coverage detail (accessed 2026-08-11)
- https://www.prnewswire.com/news-releases/daloopa-expands-financial-data-access-with-new-mcp-connector-for-microsoft-365-copilot-integration-bringing-trusted-financial-data-directly-into-ai-workflows-302810793.html — M365 Copilot MCP connector (accessed 2026-08-11)
- https://www.featuredcustomers.com/vendor/daloopa — customer references/testimonials (accessed 2026-08-11)
- https://londonstrategicedge.com/directory/fundamental-data/daloopa/ — independent vendor profile (accessed 2026-08-11)
