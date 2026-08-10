# Financial Data & Intelligence Provider Landscape

**Independent, vendor-neutral research · compiled 10 Aug 2026**

A comparative deep-dive on the major financial market-data and intelligence providers, spanning
**public equity, private equity & venture, fixed income & credit, and adjacent products** (indexes,
ratings, ESG, risk analytics, alternative data). It covers, for each provider: datasets, APIs &
technical integration, enabling technology, customer feedback, and where each one leads vs. lags.

This is a standalone study framed generically across the asset classes an institutional multi-asset
manager engages in and expands toward — it is **not** investment advice, a procurement
recommendation, or affiliated with any provider named.

## The deliverable

- **[`financial_data_providers_landscape.html`](financial_data_providers_landscape.html)** — the
  interactive report. Self-contained (inlined CSS/JS, **no external requests**), theme-aware
  (light/dark), with a sortable cross-asset capability map, per-provider deep-dives, asset-class
  "who-leads-and-why" views, a technical-integration comparison, a customer-feedback synthesis, and
  an API-native challenger tier. Open it in any modern browser.

## Providers covered

| Cluster | Providers |
|---|---|
| Cross-asset terminals | Bloomberg · LSEG/Refinitiv · FactSet |
| Fundamentals & ratings | S&P Global Market Intelligence · Moody's · Morningstar |
| Private markets | PitchBook · Preqin · CB Insights · With Intelligence |
| Indexes / risk / FI infrastructure | MSCI · ICE Data Services · Nasdaq/eVestment |
| API-native challengers (comparative tier) | FMP · Polygon.io · Intrinio · Finnhub · Xignite |

## Headline findings

- **No single winner.** Leadership fragments by asset class: Bloomberg/ICE in fixed income,
  PitchBook/Preqin in private markets, S&P in fundamentals, Moody's in credit risk, MSCI in
  equity indexes/factor risk, Nasdaq eVestment in manager selection.
- **Why winners won:** proprietary evaluated/computed data, network effects, at-scale research
  operations, decades-deep franchise histories, and regulatory/workflow embedding.
- **Runners-up lose a dimension, not the war** — e.g. LSEG/FactSet trail Bloomberg on FI depth and
  the messaging network; Preqin trails PitchBook on deal granularity but leads on fund performance.
- **Consolidation is intensifying** (BlackRock→Preqin, S&P→With Intelligence, MSCI→Burgiss,
  Morningstar→PitchBook), pushing buyers toward a portfolio of specialists over a single terminal.

## Audit trail

The full per-provider fact-sheets — each with an eight-section structure and a dated source list —
are in [`research/`](research/). They are the evidence base the HTML report is assembled from.

## Method & limitations

Researched from public sources: vendor product/API/developer docs and press for technical facts;
G2 / TrustRadius / Gartner Peer Insights / Capterra and analyst commentary for sentiment, triangulated
across ≥2 sources (several review pages were inaccessible from the research environment). **Pricing is
approximate** (enterprise vendors don't publish list prices) and **review scores are indicative**.
Figures are point-in-time as of 10 Aug 2026. See the report's *Methodology* tab for full detail.
