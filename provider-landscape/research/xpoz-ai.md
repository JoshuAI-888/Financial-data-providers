# Xpoz.ai

## 1. Snapshot
- **Owner/parent:** Independent/private startup (Xpoz, developer org "XPOZpublic" on GitHub); no disclosed parent or public funding round found in research.
- **Coverage:** Social-media data across X/Twitter, Instagram, TikTok, and Reddit; index described as "billions of posts" / 1.5B+ publicly accessible posts, searchable by user, post, and trend.
- **Free tier:** Yes, but sources disagree on the exact terms. The pricing page (xpoz.ai/pricing) and several Xpoz blog posts describe the free tier as **"500 credits"**, elsewhere glossed as a **one-time allocation of up to ~75,000 results with no credit card required**. Separately, Xpoz's own GitHub SDK READMEs (TS and Python) and other Xpoz marketing pages state the free tier is **"100,000 results/month."** A no-signup 5-day trial token (max 5 items/call, read-only) is also offered independent of the main free tier. **This is a genuine, unresolved inconsistency across Xpoz's own properties** — treat "free tier size" as directionally ~100K results-equivalent but confirm current terms directly with Xpoz before relying on it.
- **Pricing model & ranges:** Credit-based metering, charged per query (not per row returned). Reported tiers: Free (500 credits / up to 100K results, terms vary by source), Pro $20/mo (30K credits per one source, 1M results per another), Max $200/mo (600K credits / 10M results per differing sources). Per-query costs cited: Reddit and Twitter/X = 2 credits/query, TikTok = 5 credits/query, Instagram = 12 credits/query. Overage: $0.80/1,000 credits (Pro), $0.40/1,000 credits (Max).

## 2. Coverage
X/Twitter, Instagram, TikTok, and Reddit only (four platforms; no LinkedIn, YouTube, Facebook, or forums identified). No disclosed geographic or language coverage limits beyond platform-native content. Marketed explicitly as a data pipe "for AI agents" rather than a general enterprise social-listening suite — narrower platform breadth than Meltwater/Brandwatch/Talkwalker but positioned for programmatic/agentic consumption.

## 3. Datasets
- Post/tweet search and discovery (content, engagement metrics, timestamps).
- User/profile search across all four platforms.
- Trend discovery.
- Platform-specific tool sets via the MCP server: 14 Twitter/X tools (user search, tweet discovery, replies, retweets, quote tweets), 9 Instagram tools, 9 Reddit tools (users, posts, comments, subreddits), 7 TikTok tools (creators, videos).
- Continuous brand/keyword monitoring (alerting-style tracking across platforms).
- Bot-detection scoring to flag coordinated/inauthentic activity (cited in finance use-case material).
- CSV bulk export (up to 500K rows per export cited in MCP docs).

## 4. APIs & technical integration
- **API type:** REST-style API plus a remote MCP server (`https://mcp.xpoz.ai/mcp`, Streamable HTTP) — explicitly positioned as MCP-native.
- **Auth:** OAuth 2.1 (Google as identity provider) for the MCP server; API-key auth (`XPOZ_API_KEY`) for direct SDK/API use, obtained at xpoz.ai/get-token. A no-signup trial token is available via `POST https://api.xpoz.ai/api/trial/token` (5-day validity, read-only, capped at 5 items/call).
- **SDKs:** Official TypeScript SDK (`npm install @xpoz/xpoz`, Node.js 18+, 42 typed data methods) and Python SDK (`pip install xpoz`), sharing one typed response model across platforms.
- **Response modes:** "Fast" (immediate, up to 300 items), "Paging" (full pagination), and "CSV" (bulk async export).
- **MCP clients supported:** Claude Code, Codex, Gemini CLI, Cursor, and other MCP-compatible clients; Xpoz also ships a dedicated Claude Code plugin (`xpoz-claude-code-plugins`) and Claude/agent "skills" packages on GitHub.

## 5. Enabling technology
Public detail is thin (no engineering blog or architecture disclosure surfaced). The product is built around a pre-indexed corpus of public social posts ("billions indexed") queried through structured search rather than live per-request scraping, with server-side pagination, field selection, and caching controls exposed in the SDKs. The MCP-native design (OAuth 2.1, Streamable HTTP transport) is the most distinctive technical choice — built specifically for LLM/agent consumption rather than as an API retrofitted with an MCP wrapper.

## 6. Customer / user feedback
No independent third-party reviews (G2, Trustpilot, Capterra) were found during this research — Xpoz appears to be a young, developer-facing product without an established review-site presence yet. Available "feedback" is limited to Xpoz's own marketing/use-case pages (e.g., a Polymarket Analyzer app description, a "detect market-moving tweets" use-case page) and third-party MCP directory listings (mcpservers.org, Glama) that catalog rather than review the product. Treat customer-feedback signal here as thin/unverified.

## 7. Edge & positioning
- **Leads on:** MCP-native architecture (few social-data vendors ship an official remote MCP server plus a Claude Code plugin out of the box); low entry price point and per-query (not per-row) credit pricing; developer ergonomics (typed SDKs, CSV export, fast/paging/CSV response modes).
- **Lags on:** Platform breadth (4 networks vs. enterprise listening tools' dozens of sources), no finance-tuned sentiment score or entity/event taxonomy (RavenPack/Dataminr-style), no disclosed enterprise compliance/SLA posture, and — notably — inconsistent public pricing/free-tier documentation across its own site.
- **Best-for:** Developers and AI-agent builders who want raw, queryable social post/profile data (especially for crypto/prediction-market and market-moving-tweet monitoring use cases) and are willing to build their own scoring/sentiment layer on top; not a fit for teams needing a governed, finance-grade sentiment score out of the box.

## 8. Provenance
- https://www.xpoz.ai/pricing/ — free/Pro/Max tiers, credit costs cited (accessed 2026-08-14)
- https://www.xpoz.ai/ — homepage: MCP-native positioning, platforms (accessed 2026-08-14)
- https://github.com/XPOZpublic/xpoz-mcp — MCP server README: tools, auth, trial token (accessed 2026-08-14)
- https://github.com/XPOZpublic/xpoz-ts-sdk — TS SDK README: 42 methods, credit model (accessed 2026-08-14)
- https://www.xpoz.ai/use-cases/detect-market-moving-tweets-before-the-market-does/ — market-moving-tweet use case (accessed 2026-08-14)
- https://www.xpoz.ai/apps/claude-skills/polymarket-analyzer/ — Polymarket sentiment-gap tool description (accessed 2026-08-14)
- https://github.com/XPOZpublic/xpoz-claude-code-plugins — Claude Code plugin for Xpoz MCP (accessed 2026-08-14)

**Note:** WebFetch to xpoz.ai, mcpservers.org, and aiagentslist.com was egress-blocked in this environment; findings on the pricing page rely on the WebSearch index (which itself surfaced conflicting figures from different Xpoz.ai sub-pages) plus GitHub README fetches. The free-tier "500 credits/one-time" vs. "100,000 results/month" discrepancy is a genuine cross-page inconsistency on Xpoz's own site, not a research artifact — flagged above rather than resolved.
