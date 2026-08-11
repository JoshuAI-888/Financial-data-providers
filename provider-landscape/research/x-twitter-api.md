# X (Twitter) API

## 1. Snapshot
- Owner/parent: X Corp. (folded into Elon Musk's xAI in 2025); HQ Bay Area, Texas. The X API v2 is the primary programmatic gateway to X/Twitter's social graph and post stream. Positioning: the canonical firehose for public-square social data, repriced repeatedly since the 2023 paid-API overhaul.
- **Access/region notes:** global; subject to X ToS. Data-residency and content-moderation rules vary by jurisdiction.
- **Free tier:** Effectively discontinued for new developers. As of ~6 Feb 2026, X moved new developers to **pay-per-use credits** by default; the old free tier (~1,500 posts/month write, ~50 reads/24h, no search) is closed to new signups. Free access is now granted only case-by-case to "for-good public utility" apps.
- Pricing model & known ranges (verify on x.com before quoting):
  - **Pay-per-use (new default, 2026):** buy credits; ~**$0.005/post read**, ~**$0.010/user read**, ~**$0.015/post created** (~$0.20 if the post contains a URL/link); post reads **capped ~2M/month**.
  - **Legacy fixed tiers (closed to new signups, existing subscribers migrating):** Basic ~**$200/mo**, Pro ~**$5,000/mo**.
  - **Enterprise:** contact-sales, custom; reported entry ~**$42,000/mo**+.

## 2. Data-domain coverage
- social posts: yes — core product (post lookup, search, filtered/sampled stream, timelines).
- sentiment scores: no — raw content only; consumers run their own NLP.
- retail-trader signals: indirect — cashtag ($TICKER) search and volume are widely used as retail-attention proxies.
- political/insider trades: no.
- options flow: no.
- crypto social: yes (as a subset of general posts; crypto Twitter is a major sentiment source but unlabeled).

## 3. Datasets
- Captured: posts, replies, quotes, reposts, likes/engagement counts, user profiles, follows, lists, spaces metadata, media, and (on higher tiers) full-archive search back to 2006.
- History depth: full-archive search gated to Pro/Enterprise; lower tiers get recent (~7-day) search or none.
- Coverage breadth: global public posts. Proprietary scores: none from the API itself.
- Sourcing: first-party from the platform.

## 4. APIs & technical integration
- API type: REST (v2 endpoints) plus streaming (filtered stream, sampled stream) and, at Enterprise, firehose/PowerTrack-style volume.
- Auth: OAuth 2.0 (App-only Bearer + user context / PKCE); OAuth 1.0a for some legacy write flows.
- Formats: JSON.
- Rate limits: per-endpoint and tier-dependent; pay-per-use adds hard credit/read caps (~2M reads/mo).
- ToS/redistribution: strict — no redistribution of raw content or derived datasets without permission; storage/hydration and off-platform display heavily restricted; scraping prohibited by ToS.
- MCP server: no official X MCP server; several community/third-party MCP wrappers exist around the v2 API.

## 5. Enabling technology
- The API exposes raw social data; enabling tech (NLP, sentiment, ticker entity-mapping) lives with consumers or third-party vendors. Cashtag entity annotations and context annotations exist in v2 payloads to help map posts to entities/topics.

## 6. Customer / user feedback
- Segments: quants/hedge funds (alt-data sentiment), academics/researchers, social-media tools, brand/marketing analytics.
- Pros: unmatched breadth and real-time reach of the public conversation; rich metadata; official streaming.
- Cons (widely voiced across developer blogs and communities since 2023): repeated, unpredictable price hikes; removal of the affordable middle; opaque and shifting terms; research access sharply curtailed; the 2026 pay-per-use shift adds cost uncertainty. Many sentiment vendors have diversified away from X as the sole source.

## 7. Edge & positioning
- Leads: real-time breadth and cultural centrality of the feed; the default place market-moving chatter appears first.
- Lags: cost, terms volatility, and hostility to academic/redistribution use; no built-in analytics.
- Best-for: well-funded quants and vendors that need first-party real-time social data and can absorb metered/enterprise pricing.
- Free pick? No — not a viable free option for new builders in 2026.

## 8. Provenance
- https://docs.x.com/x-api/getting-started/about-x-api — official X API overview/tiers (accessed 2026-08-11)
- https://www.socialcrawl.dev/blog/x-twitter-api-2026 — 2026 credit pricing breakdown (accessed 2026-08-11)
- https://postproxy.dev/blog/x-api-pricing-2026/ — all tiers incl. legacy prices (accessed 2026-08-11)
- https://www.xpoz.ai/blog/guides/understanding-twitter-api-pricing-tiers-and-alternatives/ — $0–$42K tier comparison (accessed 2026-08-11)
- https://api.sorsa.io/blog/is-twitter-api-free — free-tier discontinuation, pay-per-use (accessed 2026-08-11)
- https://www.blotato.com/blog/twitter-api-pricing — tier and rate-limit guide (accessed 2026-08-11)
