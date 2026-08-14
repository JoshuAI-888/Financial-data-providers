# Finchat / Fiscal.ai

## 1. Snapshot
- **Owner/parent:** Independent, privately held. Launched 2023 as **FinChat.io**, a conversational-AI interface for financial data; rebranded to **Fiscal.ai** in mid-2025 alongside a $10M Series A led by Portage Ventures (with Social Leverage and VanEck participating). Underlying fundamentals data is sourced/licensed from **S&P Global Market Intelligence**.
- **Coverage:** 100,000+ global public companies for core fundamentals/estimates (20+ years history); a smaller subset of roughly ~2,000 companies has deeper segment/KPI-level and earnings-transcript detail. Global, not US-only, though depth is concentrated in more widely-followed names.
- **Free tier:** Yes — free plan includes 10 years of annual financials, basic KPI data, one dashboard, stock screener, DCF modeling, and AI summaries; new users also get a bundled trial of paid tiers. Separately, a **free API trial** covers 25 companies and 250 calls/day.
- **Pricing model & ranges:** **Pro** ≈ $49/month ($468/year); **Max** ≈ $99/month ($948/year); both offer a 7-day trial. Enterprise/API access is custom-priced through direct sales beyond the free trial tier. Materially cheaper than Bloomberg-class terminals, positioned as a prosumer/small-institutional price point.
- **Rebrand note:** "Finchat" and "Fiscal.ai" refer to the same company/product — FinChat is the legacy/former name; Fiscal.ai is current. Some third-party reviews and the old "Plus"/"Pro" tier names still reference FinChat, causing minor naming confusion noted by reviewers.

## 2. Coverage
Broad global public-company coverage (100,000+ tickers) for standardized fundamentals and 20+ years of history — not US-only, a differentiator versus Motley Fool/Seeking Alpha. However, **earnings-call transcripts and granular segment/KPI data are concentrated in a smaller universe** (~2,000 companies), meaning deep transcript-linked analytics are not available for the long tail of global small-caps. No evidence found of native audio or slide-deck hosting — Fiscal.ai's transcript offering is a searchable, AI-queryable **text** layer over transcripts (and filings), not a media/audio platform like Aiera.

## 3. Datasets
- **Earnings-call transcripts** (searchable/queryable via AI copilot) alongside **SEC filings**, both integrated into the same natural-language interface.
- Standardized and as-reported **financial statements**, ratios, **segment and KPI-level data**, **analyst estimates**, dividend history, and institutional/insider ownership data.
- AI-generated **summaries** of filings/transcripts, cross-quarter **management-commentary comparison**, and structured extraction (e.g., "R&D spending trends across semiconductor peers" style comparison tables) — i.e., explicit KPI/guidance-extraction and thematic-comparison capability, more so than any other provider in this set.
- Stock screener and DCF modeling tools bundled around the data layer.
- No confirmed real-time/live transcript capability — Fiscal.ai operates on **published** transcripts and filings (T+hours/T+1 profile consistent with sourcing from S&P Global/standard transcript vendors), not live in-call capture like Aiera.

## 4. APIs & technical integration
Fiscal.ai has genuine developer-facing infrastructure: documented REST API (docs.fiscal.ai) covering company profiles, as-reported/standardized financials, ratios, KPIs, stock prices, filings, and transcripts; a free trial tier (25 companies, 250 calls/day); OAuth or API-key auth; webhooks; and notably a **Fiscal MCP (Model Context Protocol) server** plus native connectors for Claude, ChatGPT, Cursor, VS Code Copilot, Gemini CLI and other MCP/agentic-AI clients — the most "AI-agent-native" integration story of the four providers reviewed.

## 5. Enabling technology
Core positioning is a **conversational AI copilot** layered over licensed S&P Global Market Intelligence fundamentals plus transcripts/filings — natural-language Q&A, cross-document comparison, and structured-table generation from unstructured filing/transcript text. Marketing claims the copilot scores "2–4x higher than general LLMs" on FinanceBench (a finance-specific LLM benchmark), though this is a vendor-reported figure not independently re-verified in the sources gathered. The product architecture (chat interface + underlying licensed data warehouse + MCP server) reflects a genuinely AI-native build rather than a legacy data product with AI bolted on.

## 6. Customer / user feedback
Generally positive and triangulated across multiple review sources (Trustpilot ~24 reviews, third-party review blogs). Praised for: data quality/breadth ("like Bloomberg for retail investors"), being one of few tools with retail-accessible KPI-level segment data, strong UX, and workflow consolidation (fundamentals + charting + research in one place). Criticized for: **no real-time market/trading data**, comparatively **limited charting tools** versus dedicated terminal products (e.g., Koyfin), and a rebrand (FinChat→Fiscal.ai) that some reviewers found confusing, including tier-name changes (old Plus→Pro, old Pro→Max).

## 7. Edge & positioning
- **Leads on:** AI-native synthesis — genuine KPI/guidance extraction, cross-quarter management-commentary comparison, and structured table generation from transcripts/filings via natural language, plus the most modern developer/agent integration surface (MCP server, LLM-client connectors) of any provider reviewed.
- **Lags on:** No real-time/live transcript capture (post-publication only), deep KPI/transcript data limited to ~2,000 of its 100,000+ covered companies, and no audio/video capture.
- **Best-for:** Retail-to-prosumer and small-institutional analysts who want an AI copilot to interrogate transcripts and filings together with fundamentals (e.g., "compare guidance language across the last 4 quarters"), rather than users needing live in-call speed or the widest possible small-cap transcript breadth.

## 8. Provenance
- https://docs.fiscal.ai/docs/introduction — Official API documentation entry point (accessed 2026-08-14)
- https://docs.fiscal.ai/docs/api-reference — API reference, endpoint coverage (accessed 2026-08-14)
- https://fiscal.ai/api-terms/ — API terms, free-trial limits (25 companies/250 calls/day) (accessed 2026-08-14)
- https://www.wallstreetzen.com/blog/finchat-io-fiscal-ai-review/ — Rebrand history, pricing tiers, review (accessed 2026-08-14)
- https://fintechobserver.substack.com/p/fiscalai-the-ai-terminal-quietly — Series A funding, positioning vs Bloomberg (accessed 2026-08-14)
- https://quantbrainai.net/blog/fiscal-ai-review-jul-2026/ — Feature/coverage detail, FinanceBench claim (accessed 2026-08-14)
- https://www.trustpilot.com/review/fiscal.ai — Customer feedback triangulation (accessed 2026-08-14)
- https://daytradingtoolkit.com/reviews/finchat-review — Rebrand/tier-naming confusion, cons (charting, real-time data) (accessed 2026-08-14)
