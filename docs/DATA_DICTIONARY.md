# Data Dictionary

> Auto-generated from `fmp_milford/config.py` + the normalized record shape. Covers
> (1) FMP endpoints used, (2) the canonical company record, (3) computed metric outputs.

**Universe:** 32 US-listed names across 4 themes. **Benchmark:** SPY. **Daily call budget:** 250. **History:** ~5y (free tier).

## 1. FMP endpoints (stable API)

| key | path | params | free tier? | feeds |
|---|---|---|---|---|
| `profile` | `/profile` | symbol | ✓ free | reference, logo, price, mktcap, beta, sector |
| `income_statement` | `/income-statement` | period=annual, limit=5 | ✓ free | revenue, margins, EPS, EBITDA |
| `balance_sheet` | `/balance-sheet-statement` | period=annual, limit=5 | ✓ free | assets, equity, debt, working capital |
| `cash_flow` | `/cash-flow-statement` | period=annual, limit=5 | ✓ free | OCF, capex, FCF, dividends paid, buybacks |
| `ratios` | `/ratios` | period=annual, limit=5 | ✓ free | cross-check ratios |
| `key_metrics` | `/key-metrics` | period=annual, limit=5 | ✓ free | ROIC, per-share, EV metrics |
| `financial_growth` | `/financial-growth` | period=annual, limit=5 | ✓ free | growth rates |
| `financial_scores` | `/financial-scores` | symbol | ✓ free | Altman Z, Piotroski (cross-check) |
| `dividends` | `/dividends` | symbol | ✓ free | dividend history / yield |
| `prices_eod` | `/historical-price-eod/full` | symbol | ✓ free | EOD OHLCV -> returns/vol/beta/drawdown |
| `analyst_estimates` | `/analyst-estimates` | period=annual, limit=5 | verify/gated | forward estimates (likely Premium+) |
| `price_target` | `/price-target-summary` | symbol | verify/gated | price targets (likely Premium+) |
| `grades` | `/grades` | symbol | verify/gated | analyst ratings (likely Premium+) |

Per-company pull uses: `profile`, `income_statement`, `balance_sheet`, `cash_flow`, `key_metrics`, `financial_growth`, `financial_scores`, `dividends`, `prices_eod` (~9 calls/company → ~27 companies/day on free tier).

## 2. Canonical company record (normalized; demo and live share this shape)

| field | type | unit | source | notes |
|---|---|---|---|---|
| `ticker` | str | — | profile | Exchange symbol / join key |
| `name` | str | — | profile.companyName | Legal/common name |
| `sector` | str | — | config UNIVERSE (theme) | Milford theme bucket |
| `industry` | str | — | profile.industry | FMP industry label |
| `currency` | str | — | profile.currency | Reporting/trading currency (USD on free tier) |
| `price` | float | $ | profile.price | Latest EOD price |
| `shares_out` | float | count | profile.sharesOutstanding | Shares outstanding |
| `market_cap` | float | $m | profile.marketCap | Market capitalisation |
| `beta` | float | — | profile.beta | Vendor beta (we also compute our own) |
| `years` | list[int] | — | statements | Fiscal years available (<=5 on free tier) |
| `income[y]` | dict | $m | income-statement | revenue, gross_profit, operating_income, ebitda, dep_amort, interest_expense, net_income, shares, eps |
| `balance[y]` | dict | $m | balance-sheet-statement | total_assets, current_assets, cash, inventory, receivables, total_liabilities, current_liabilities, total_debt, total_equity, retained_earnings, payables |
| `cash_flow[y]` | dict | $m | cash-flow-statement | operating_cf, capex, free_cash_flow, dividends_paid, buybacks |
| `dividend_per_share` | float | $ | dividends | TTM dividend per share |
| `dividend_yield` | float | % | derived | dps / price |
| `prices` | dict | $ | historical-price-eod/full | {start, freq='W', closes:[...]} weekly EOD closes |
| `fmp_scores` | dict | — | financial-scores | Vendor Altman Z / Piotroski (cross-check) |
| `source` | str | — | — | 'FMP /stable/' or 'DEMO (synthetic)' |
| `retrieved` | iso ts | — | — | Extraction timestamp (provenance) |

## 3. Computed metric outputs

Each metric is a dict `{value, formula, inputs, steps, unit, good}` (see `transform.py`). Plain-language meaning/target/alpha for every one is in [GLOSSARY.md](GLOSSARY.md). Keys:

`gross_margin`, `ebitda_margin`, `operating_margin`, `net_margin`, `roe`, `roa`, `roic`, `roce`, `revenue_cagr`, `eps_cagr`, `fcf_cagr`, `current_ratio`, `quick_ratio`, `interest_coverage`, `net_debt_ebitda`, `debt_to_equity`, `gearing`, `asset_turnover`, `cash_conversion_cycle`, `fcf_conversion`, `ocf_ebitda`, `capex_sales`, `pe`, `ev_ebitda`, `ev_sales`, `pb`, `p_fcf`, `fcf_yield`, `dividend_yield`, `peg`, `eps`, `bvps`, `dps`, `cfps`, `altman_z`, `piotroski_f`, `dupont_roe`, `total_return`, `ann_return`, `ann_vol`, `downside_vol`, `beta`, `max_drawdown`, `momentum_12m`, `sharpe`, `value`, `quality`, `growth`, `momentum`, `composite`
