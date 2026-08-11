# Reddit API + ApeWisdom

## 1. Snapshot
- Two things bundled: (a) **Reddit's official Data API** (Reddit, Inc.; HQ San Francisco) — the source, and (b) **ApeWisdom** (apewisdom.io) — a free third-party tracker that scans Reddit (esp. r/wallstreetbets) and exposes trending-ticker mention counts via a keyless public API. Positioning: the canonical free window into retail/WSB attention.
- **Access/region notes:** global. Reddit API requires OAuth + registered app; ApeWisdom requires nothing.
- **Free tier:**
  - **Reddit API:** yes for non-commercial/personal/research use — ~**100 queries/min per OAuth client** (10 req/min unauthenticated), rolling 10-min average. Commercial use is **not** free.
  - **ApeWisdom:** yes — fully free, **no signup, no API key**, public JSON endpoints.
- Pricing model & known ranges:
  - Reddit commercial: **~$0.24 per 1,000 API calls**, manual approval; reported entry ~**$12,000/mo for ~50M calls**; 2–4 week use-case review, approval not guaranteed.
  - ApeWisdom: free (no paid tier for the API).

## 2. Data-domain coverage
- social posts: yes — Reddit API returns posts/comments/subreddit data; ApeWisdom aggregates mentions.
- sentiment scores: partial — Reddit API is raw text (run your own NLP); **ApeWisdom returns mention COUNTS, not true sentiment** (important limitation).
- retail-trader signals: yes — WSB/stocks/options/crypto subreddit trending tickers, mention deltas, upvotes; ApeWisdom "gainers" surfaces newly viral tickers.
- political/insider trades: no.
- options flow: no.
- crypto social: yes — ApeWisdom covers crypto subreddits (CryptoCurrency, Bitcoin, SatoshiStreetBets) and 4chan /biz.

## 3. Datasets
- ApeWisdom trending endpoint: per-ticker name, current mentions, mentions 24h ago, today's rank, yesterday's rank, total upvotes; filterable by community group (all / stocks / crypto) or individual subreddit. Updated frequently; shallow public history (recent window), though mention-history views exist on the site.
- Reddit API: full post/comment/subreddit corpus (subject to rate limits), user and listing data; deep coverage of the actual discussion text.
- Proprietary scores: ApeWisdom's rank/gainer deltas; no proprietary sentiment model.

## 4. APIs & technical integration
- ApeWisdom: REST, JSON, keyless, no auth; e.g. filter + page params on the trending endpoint. Very light rate expectations (be polite). ToS: free including for many uses, but it is itself derived from Reddit data — redistribution should respect Reddit's terms.
- Reddit: REST, JSON; OAuth 2.0 required; per-client rate limits; strict Data API Terms governing commercial use, storage, and redistribution (post-2023 crackdown). Bulk/commercial requires signed agreement.
- MCP server: no official Reddit or ApeWisdom MCP; community Reddit MCP servers (e.g. via Apify actors) exist.

## 5. Enabling technology
- ApeWisdom: ticker extraction/normalization from free-text posts and mention aggregation with rank/delta computation. No ML sentiment. Reddit API: none beyond raw delivery; entity-to-ticker mapping and sentiment are the consumer's job.

## 6. Customer / user feedback
- Segments: retail traders, indie quants, students, researchers, and sentiment vendors sourcing WSB signal cheaply.
- Pros: ApeWisdom is repeatedly cited as the **best free, keyless Reddit mention tracker**; dead-simple; good for meme-stock attention spikes. Reddit API is authoritative and rich.
- Cons: ApeWisdom = mentions not sentiment, no SLA, thin history; Reddit official API is expensive/gated for any commercial use and its 2023 pricing move alienated developers. Both are noisy and prone to manipulation/pump behavior.

## 7. Edge & positioning
- Leads: cheapest credible read on retail/WSB attention (ApeWisdom); authoritative raw corpus (Reddit).
- Lags: no true sentiment scoring for free; commercial Reddit access is costly and bureaucratic.
- Best-for: retail-attention/meme-stock monitoring on a zero budget (ApeWisdom); serious pipelines that can pay/negotiate (Reddit direct).
- Free pick? **Yes — ApeWisdom is the standout free social-sentiment pick** in this cluster (with the mentions-not-sentiment caveat).

## 8. Provenance
- https://apewisdom.io/api/ — ApeWisdom free API docs (accessed 2026-08-11)
- https://apewisdom.io/ — trending Reddit stocks tracker (accessed 2026-08-11)
- https://www.socialcrawl.dev/blog/reddit-data-api-2026 — Reddit API pricing/rate limits (accessed 2026-08-11)
- https://prowlo.com/blog/reddit-api-pricing — $0.24/1K calls, free tier (accessed 2026-08-11)
- https://prowlo.com/blog/reddit-data-api — commercial terms & approval (accessed 2026-08-11)
- https://adanos.org/insights/blog/best-reddit-stock-sentiment-trackers-2026/ — free vs paid trackers compared (accessed 2026-08-11)
