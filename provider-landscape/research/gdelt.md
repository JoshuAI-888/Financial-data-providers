# GDELT Project

## 1. Snapshot
- **Owner/parent:** The GDELT Project (Global Database of Events, Language, and Tone), created and led by Kalev Leetaru; historically supported by Google Jigsaw/Google Cloud and academic partners. An open, non-commercial research initiative. Positioning: the world's largest open, machine-readable catalogue of global news, events, tone and entities — "a free platform for monitoring the world's news."
- **Regions/language coverage:** Truly global. Monitors worldwide online news (print/broadcast/web) plus selected TV transcripts, **machine-translating ~65–100 languages in real time** — by far the deepest non-English and foreign-market coverage of any option in this cluster.
- **Free tier:** **YES — entirely free and open (the free/low-cost pick).** All datasets and APIs are free with no API key for the standard DOC/GEO/TV APIs; large-scale historical work runs on Google BigQuery (Google Cloud query costs apply, but the data itself is free) or via raw 15-minute CSV file downloads.
- **Pricing model & ranges:** No commercial pricing — free/open data. Only indirect cost is your own compute (BigQuery query charges, storage, engineering).

## 2. Data-domain coverage
- **Financial news:** Yes via general-news filtering — widely used for financial/geopolitical risk monitoring, supply-chain disruption and event detection.
- **General news:** Core — global online and broadcast news at massive scale.
- **Press releases/newswires:** Captured only where they appear in indexed web/media coverage; no dedicated newswire licensing.
- **Historical archive:** Deep — Events data back to 1979; GKG 2.0 from 2015; specialised collections span 215 years of books and ~21 billion words of academic literature.
- **Sentiment/analytics:** Yes — "tone" scores (emotional sentiment, numeric scale) plus emotion/theme measures per article.
- **Entity tagging:** Yes — the Global Knowledge Graph (GKG) extracts persons, organisations, locations, themes (GKG taxonomy) and events.

## 3. Datasets
- **GDELT Events** (CAMEO-coded actor/action event records, 1979+), **GKG 2.0** (article-level themes/entities/locations/tone, 2015+), **Visual GKG** (image processing), TV/broadcast datasets, and numerous special collections (academic literature, books, global difference graph).
- Sources: hundreds of thousands of worldwide outlets across 65+ translated languages.
- History depth: decades (1979+ events); ~12 TB+ total; updates **every 15 minutes**.
- Metadata: tone/emotion, themes, named entities, geolocation, source country/language, event codes.

## 4. APIs & technical integration
- **API type:** REST-style query APIs — **DOC 2.0 API** (rolling ~3-month article search, JSON/CSV/RSS output), **GEO 2.0 API**, **TV API** — plus **bulk** raw 15-minute CSV files, and **Google BigQuery** public datasets for large-scale/historical SQL analysis.
- **Auth:** None required for the public DOC/GEO/TV APIs; BigQuery uses a Google Cloud account.
- **Formats:** JSON, CSV, RSS, HTML; BigQuery tables; raw file archives.
- **Rate limits:** No formal key-based quota; informal "be reasonable" throttling on the hosted APIs.
- **Delivery:** Hosted API, raw file downloads, BigQuery (and thus onward to Databricks/Snowflake via your own pipeline).
- **MCP server:** No official GDELT MCP server, but active community servers exist (e.g. `cyanheads/gdelt-mcp-server`, STDIO/HTTP, filters for country/language/theme/tone) usable with Claude/OpenAI clients.

## 5. Enabling technology
- Real-time machine translation across 65+ languages; entity/theme/location extraction feeding the GKG; CAMEO event coding; tone/emotion scoring; image analysis (Visual GKG); and pre-extracted BigQuery helper tables (themes/persons/organizations/locations) for 10–100x faster queries. A heavy data-engineering platform rather than a turnkey product.

## 6. Customer / user feedback
- **Ratings:** No conventional G2/Trustpilot vendor score (it is an open dataset), but it is one of the most-cited news datasets in academic and quant research; comparison blogs consistently list it as the leading *free* news-data option.
- **Pros:** Free at scale, unmatched global/multilingual breadth, 15-minute latency, tone + entity + event structure, decades of history for backtesting.
- **Cons:** Noisy and requires significant data engineering; machine-translation and coding errors; no dedup/quality SLA; no licensed newswire text (links, not full articles); BigQuery costs for heavy use.
- **User segments:** Academics, data scientists, quant/geopolitical-risk researchers, journalists, NGOs.

## 7. Edge & positioning
- **Leads on:** cost (free), global/multilingual coverage, historical depth, and structured tone/entity/event signals — nothing else in this cluster matches its breadth at zero data cost.
- **Lags on:** turnkey usability, curated financial entity resolution (tickers), full-article licensing, and support/SLAs.
- **Best for:** budget-conscious quant/risk teams and researchers willing to engineer their own pipeline; the definitive **free** choice for global news-signal and sentiment work.

## 8. Provenance
- https://www.gdeltproject.org/data.html — official datasets & access methods (accessed 2026-08-11)
- https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/ — official DOC 2.0 API announcement (accessed 2026-08-11)
- https://blog.gdeltproject.org/a-compilation-of-gdelt-bigquery-demos/ — official BigQuery usage examples (accessed 2026-08-11)
- https://github.com/cyanheads/gdelt-mcp-server — community MCP server for GDELT (accessed 2026-08-11)
- https://dataresearchtools.com/gdelt-project-for-news-data-2026-free-alternative-to-newsapi/ — independent review as free NewsAPI alternative (accessed 2026-08-11)
- https://dataresearchtools.com/best-news-apis-comparison/ — independent GDELT vs peers comparison (accessed 2026-08-11)
