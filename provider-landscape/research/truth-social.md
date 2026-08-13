# Truth Social API (Truth API)

## 1. Snapshot
- Owner/parent: Trump Media & Technology Group (TMTG, Nasdaq: DJT); HQ Sarasota, Florida; platform launched Feb 2022, built on a fork of the open-source **Mastodon** codebase. Positioning: a paid, licensed real-time data feed of market-moving Truth Social posts sold to Wall Street.
- **Access/region notes:** The consumer social network is global (web/iOS/Android, with some countries restricted historically). The commercial "Truth API" data product is a B2B licensing arrangement, not a self-serve global developer platform.
- **Free tier:** No. There is **no official free/public developer API**, no self-serve API keys, no documented public endpoints, no OAuth app registration for third parties, and no published rate limits or support channel. Community access relies on unofficial scraping of the Mastodon-derived endpoints or third-party scrapers.
- Pricing model & known ranges: The official **Truth API** (announced 16 Jul 2026, launched 1 Aug 2026) is sold via institutional licensing agreements. Reporting puts pricing at **up to ~$100,000/month** for low-latency access to posts from the highest-ranking accounts. It is TMTG's first data-licensing product, pitched as a high-margin recurring revenue stream. No public price card.

## 2. Data-domain coverage
- social posts: yes — real-time posts ("Truths") from the highest-ranking Truth Social accounts, including President Trump.
- sentiment scores: no — raw posts only; no scoring provided by TMTG.
- retail-trader signals: no.
- political/insider trades: no (but the posts themselves are frequently market-moving political/policy signals).
- options flow: no.
- crypto social: no.

## 3. Datasets
- Captured: machine-readable text posts, timestamps, and account identifiers from top-ranked accounts. Marketed as delivering posts to subscribers **milliseconds before** they reach the public feed, with 24/7 coverage and a **historical archive dating back to 2022**.
- Coverage breadth: limited to Truth Social's own network (not cross-platform). Sourcing method: first-party from TMTG's platform infrastructure.
- Proprietary scores/signals: none — the value proposition is latency and exclusivity, not analytics.

## 4. APIs & technical integration
- API type: licensed low-latency, machine-readable B2B feed aimed at high-frequency/algorithmic trading firms; delivery mechanics not publicly documented.
- Auth/formats/rate limits: not publicly disclosed (private contracts).
- ToS/redistribution: platform ToS historically restricted commercial scraping (a coding org publicly sought legal counsel over scraping concerns). The official feed is license-gated; redistribution governed by contract.
- Community libraries: because the app is a Mastodon fork, unofficial wrappers and scrapers exist (e.g. ScrapeCreators, SocialCrawl, and open-source Mastodon-style clients) that read profile/post endpoints without OAuth. These are unsupported and legally grey.
- MCP server: none known (official or community).

## 5. Enabling technology
- Underlying platform is a Mastodon (ActivityPub) fork. The Truth API layer adds low-latency fan-out/prioritized delivery of top-account posts. No NLP, entity-to-ticker mapping, or sentiment tooling is offered by TMTG — buyers apply their own NLP/LLM pipelines to the raw text.

## 6. Customer / user feedback
- Target/actual users: high-frequency and algorithmic trading firms, institutional desks, and media/analytics vendors. As a brand-new (Aug 2026) product there is little independent user feedback yet.
- Pros (per reporting): unique first-party access to a demonstrably market-moving feed; low latency; historical archive.
- Cons/criticism: very high price; single-source/narrow coverage; conflict-of-interest and reliability concerns given the political nature; no developer ecosystem; consumer app historically criticized for outages and moderation. Community/free access is scraping-only and fragile.

## 7. Edge & positioning
- Leads: exclusivity and latency on Trump/Truth Social posts specifically — a niche but genuinely price-sensitive signal for event-driven trading.
- Lags: everything else — no analytics, no breadth, no free/developer tier, no transparency.
- Best-for: event-driven/HFT desks that specifically trade headlines from Trump and top Truth Social accounts and can afford five-figure monthly licensing.
- Free pick? No — not free, and the only free route (scraping) is unsupported and ToS-risky.

## 8. Provenance
- https://thehill.com/policy/technology/5972998-trump-media-technology-group-launch-truth-api/ — Truth API launch reporting (accessed 2026-08-11)
- https://www.nbcnews.com/politics/donald-trump/truth-social-launches-service-selling-faster-access-trump-posts-rcna590419 — service selling faster post access (accessed 2026-08-11)
- https://www.cnbc.com/2026/07/16/trump-truth-social-wall-street-traders-api.html — paid data service for traders (accessed 2026-08-11)
- https://www.stocktitan.net/news/DJT/trump-media-and-technology-group-launches-truth-api-a-new-licensed-ua4pyh02fjbe.html — TMTG official launch (licensed feed) (accessed 2026-08-11)
- https://www.heise.de/en/news/API-access-for-Truth-Social-Faster-access-to-Trump-s-posts-for-a-fee-11368968.html — paid faster access reporting (accessed 2026-08-11)
- https://scrapecreators.com/truthsocial-api — third-party scraper (no official API) (accessed 2026-08-11)
- https://www.socialcrawl.dev/platforms/truthsocial — community scrape access notes (accessed 2026-08-11)
