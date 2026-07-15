# Metric Glossary

> Auto-generated from `fmp_milford/glossary.py` (the single source of truth, also
> surfaced in the app as hover tooltips and the calculation modal). For each metric:
> **meaning**, what **good** looks like, what you're **targeting**, and the **alpha / trade** angle.

## Profitability

### Gross margin  (`gross_margin`)
- **Meaning:** Share of revenue left after the direct cost of goods/services.
- **What good looks like:** Higher and stable; wide gross margin signals pricing power or a cost moat.
- **What we're targeting:** Establish structural profitability and how much room exists to absorb cost shocks.
- **Alpha / what it trades:** Rising gross margin ahead of consensus often precedes earnings upgrades — a long signal.

### EBITDA margin  (`ebitda_margin`)
- **Meaning:** Operating cash profitability before D&A, interest and tax, as a % of sales.
- **What good looks like:** Higher; consistent with peers or expanding.
- **What we're targeting:** Compare operating profitability across capital structures and tax regimes.
- **Alpha / what it trades:** Margin inflection is a cleaner cross-border signal than net income, which FX and tax distort.

### Operating margin  (`operating_margin`)
- **Meaning:** EBIT as a % of revenue — profit after all operating costs.
- **What good looks like:** Higher and trending up; beating the peer median.
- **What we're targeting:** Judge core operating efficiency independent of financing.
- **Alpha / what it trades:** Operating leverage (margin rising faster than sales) compounds EPS — buy ahead of it.

### Net margin  (`net_margin`)
- **Meaning:** Bottom-line profit as a % of revenue.
- **What good looks like:** Higher; positive and stable. Negative = loss-making.
- **What we're targeting:** Final profitability after everything, incl. tax and interest.
- **Alpha / what it trades:** Best read relative to sector; a low-margin name that is structurally improving can re-rate hard.

### Return on equity  (`roe`)
- **Meaning:** Net income divided by shareholders' equity.
- **What good looks like:** >15% is strong, but check it isn't just leverage (see DuPont).
- **What we're targeting:** How much profit management generates on owners' capital.
- **Alpha / what it trades:** High, non-leverage-driven ROE that the market underpays for is the classic quality-value trade.

### Return on assets  (`roa`)
- **Meaning:** Net income divided by total assets.
- **What good looks like:** Higher; asset-light models score well.
- **What we're targeting:** Profit generated per dollar of assets, ignoring how they're financed.
- **Alpha / what it trades:** ROA gap vs peers flags who actually earns their asset base — short the laggards, own the leaders.

### Return on invested capital  (`roic`)
- **Meaning:** After-tax operating profit (NOPAT) over debt+equity−cash.
- **What good looks like:** >WACC (roughly >8-10%) means the company creates value; below, it destroys it.
- **What we're targeting:** The single best test of whether a business is worth owning.
- **Alpha / what it trades:** ROIC > WACC and rising, bought below intrinsic value, is the core compounder trade.

### Return on capital employed  (`roce`)
- **Meaning:** EBIT over capital employed (assets − current liabilities).
- **What good looks like:** Higher and above cost of capital; stable through the cycle.
- **What we're targeting:** Pre-tax capital efficiency, useful for cross-tax-regime comparison.
- **Alpha / what it trades:** ROCE trend separates genuine improvers from cyclical flatterers.

## Growth

### Revenue CAGR  (`revenue_cagr`)
- **Meaning:** Compound annual revenue growth over the history window.
- **What good looks like:** Higher, but durable growth beats a spiky number.
- **What we're targeting:** Establish the top-line trajectory and TAM capture.
- **Alpha / what it trades:** Durable growth the market prices as temporary is where growth alpha lives.

### EPS CAGR  (`eps_cagr`)
- **Meaning:** Compound annual growth in earnings per share.
- **What good looks like:** Higher than revenue growth = operating leverage + disciplined share count.
- **What we're targeting:** Per-share value creation, the thing shareholders actually own.
- **Alpha / what it trades:** EPS growth outrunning revenue signals leverage/buybacks — quality of the growth matters.

### Free-cash-flow CAGR  (`fcf_cagr`)
- **Meaning:** Compound annual growth in free cash flow.
- **What good looks like:** Positive and tracking earnings growth.
- **What we're targeting:** Whether growth is turning into real, distributable cash.
- **Alpha / what it trades:** FCF growth that lags EPS growth is a red flag; the reverse is a hidden-quality long.

## Liquidity

### Current ratio  (`current_ratio`)
- **Meaning:** Current assets over current liabilities.
- **What good looks like:** ~1.5-3x; comfortably above 1.
- **What we're targeting:** Short-term solvency — can it pay the next 12 months' bills.
- **Alpha / what it trades:** Mainly a risk filter; deteriorating liquidity precedes distress re-ratings.

### Quick ratio  (`quick_ratio`)
- **Meaning:** Liquid current assets (ex-inventory) over current liabilities.
- **What good looks like:** >1 means it can cover short-term liabilities without selling inventory.
- **What we're targeting:** Stricter liquidity test for inventory-heavy names.
- **Alpha / what it trades:** Risk screen for cyclicals/retail where inventory can be stranded.

### Interest coverage  (`interest_coverage`)
- **Meaning:** EBIT divided by interest expense.
- **What good looks like:** >4x comfortable; <2x fragile.
- **What we're targeting:** Can operating profit service the debt.
- **Alpha / what it trades:** Thin coverage into a rising-rate backdrop is a short/avoid; improving coverage de-risks a re-rating.

## Leverage

### Net debt / EBITDA  (`net_debt_ebitda`)
- **Meaning:** Net borrowings relative to operating cash profit.
- **What good looks like:** <2x conservative; >4x stretched (sector-dependent — utilities carry more).
- **What we're targeting:** Balance-sheet risk and refinancing headroom.
- **Alpha / what it trades:** De-leveraging stories re-rate as risk falls; over-levered names de-rate fast when growth stalls.

### Debt / equity  (`debt_to_equity`)
- **Meaning:** Total debt relative to equity.
- **What good looks like:** Lower; context by sector.
- **What we're targeting:** Capital-structure risk.
- **Alpha / what it trades:** Leverage amplifies both ROE and downside — pair with ROIC to judge quality of returns.

### Gearing  (`gearing`)
- **Meaning:** Debt as a share of total capital (debt+equity).
- **What good looks like:** Lower and stable.
- **What we're targeting:** Overall reliance on debt funding.
- **Alpha / what it trades:** Gearing trend flags capital-allocation discipline.

## Efficiency & cash conversion

### Asset turnover  (`asset_turnover`)
- **Meaning:** Revenue generated per dollar of assets.
- **What good looks like:** Higher; asset-light beats asset-heavy for a given margin.
- **What we're targeting:** How hard the asset base works (a DuPont driver of ROE).
- **Alpha / what it trades:** Improving turnover with steady margin lifts ROE — a quality signal the market lags.

### Cash conversion cycle  (`cash_conversion_cycle`)
- **Meaning:** Days to turn working-capital investment into cash (DSO+DIO−DPO).
- **What good looks like:** Lower/negative; a negative CCC funds growth with suppliers' money.
- **What we're targeting:** Working-capital efficiency and self-funding capacity.
- **Alpha / what it trades:** Structural CCC improvement frees cash and lifts FCF — under-appreciated quality.

### FCF conversion  (`fcf_conversion`)
- **Meaning:** Free cash flow as a % of net income — the single best earnings-quality tell.
- **What good looks like:** >80-100% consistently. Persistently low = earnings not backed by cash.
- **What we're targeting:** Whether reported profit is real, distributable cash.
- **Alpha / what it trades:** High, stable conversion the market ignores is prime quality-compounder alpha; falling conversion is an early short.

### OCF / EBITDA  (`ocf_ebitda`)
- **Meaning:** Operating cash flow as a % of EBITDA.
- **What good looks like:** Higher (>70%); low means working capital or accruals are leaking cash.
- **What we're targeting:** Cash backing of headline operating profit.
- **Alpha / what it trades:** Divergence between OCF and EBITDA flags aggressive accounting — a forensic short input.

### Capex / sales  (`capex_sales`)
- **Meaning:** Capital intensity — capex as a % of revenue.
- **What good looks like:** Lower for a given growth rate; but under-investment can mortgage the future.
- **What we're targeting:** How much reinvestment the model needs to grow.
- **Alpha / what it trades:** Capex cycles turn: peak-capex names can inflect to FCF harvest — a timing trade.

## Valuation

### Price / earnings  (`pe`)
- **Meaning:** Market cap over net income.
- **What good looks like:** Lower is cheaper, but only vs growth+quality; low P/E + low ROIC is a trap.
- **What we're targeting:** Headline valuation vs earnings.
- **Alpha / what it trades:** Cheap P/E with improving quality and estimate upgrades is the value re-rating trade.

### EV / EBITDA  (`ev_ebitda`)
- **Meaning:** Enterprise value over EBITDA — capital-structure-neutral valuation.
- **What good looks like:** Lower vs peers, adjusted for growth/margin.
- **What we're targeting:** Compare valuation across different leverage and tax regimes.
- **Alpha / what it trades:** The workhorse comp multiple; a name cheap on EV/EBITDA with high ROIC is a genuine opportunity, not a trap.

### EV / sales  (`ev_sales`)
- **Meaning:** Enterprise value over revenue.
- **What good looks like:** Lower for a given margin; the go-to when earnings are negative.
- **What we're targeting:** Value loss-making or early-stage names on revenue.
- **Alpha / what it trades:** Re-rating happens as margins arrive — EV/sales vs margin trajectory is the growth-value cross.

### Price / book  (`pb`)
- **Meaning:** Market cap over equity (book value).
- **What good looks like:** Lower, but only meaningful vs ROE.
- **What we're targeting:** Valuation vs accounting net worth (esp. financials/utilities).
- **Alpha / what it trades:** Low P/B + high ROE is the classic value screen; P/B alone misleads for asset-light models.

### Price / FCF  (`p_fcf`)
- **Meaning:** Market cap over free cash flow.
- **What good looks like:** Lower; a cash-based cheapness check.
- **What we're targeting:** Valuation against the cash owners can actually receive.
- **Alpha / what it trades:** Cheaper on P/FCF than P/E means high cash conversion the market underpays — a quality-value long.

### FCF yield  (`fcf_yield`)
- **Meaning:** Free cash flow divided by market cap — the cash return you buy.
- **What good looks like:** >5-6% attractive; the inverse of P/FCF.
- **What we're targeting:** Cash return on the equity you pay for.
- **Alpha / what it trades:** High FCF yield + growing FCF is the core cash-compounder buy signal.

### Dividend yield  (`dividend_yield`)
- **Meaning:** Dividend per share over price.
- **What good looks like:** Sustainable and covered by FCF; very high yields can signal risk.
- **What we're targeting:** Income contribution and capital-return discipline.
- **Alpha / what it trades:** Covered, growing yield supports total return; an unsustainable yield is a value trap / dividend-cut short.

### PEG ratio  (`peg`)
- **Meaning:** P/E divided by EPS growth rate.
- **What good looks like:** <1 suggests growth is cheap relative to the multiple.
- **What we're targeting:** Reconcile valuation with growth in one number.
- **Alpha / what it trades:** Low PEG with durable growth is the growth-at-a-reasonable-price (GARP) trade.

## Per share

### EPS  (`eps`)
- **Meaning:** Net income per share.
- **What good looks like:** Higher and growing.
- **What we're targeting:** Per-share earning power.
- **Alpha / what it trades:** EPS surprise + revision trend drives short-term price.

### Book value / share  (`bvps`)
- **Meaning:** Equity per share.
- **What good looks like:** Growing over time.
- **What we're targeting:** Accounting net worth per share.
- **Alpha / what it trades:** BVPS growth + high ROE compounds intrinsic value.

### Dividend / share  (`dps`)
- **Meaning:** Declared dividend per share.
- **What good looks like:** Growing and covered.
- **What we're targeting:** Income per share.
- **Alpha / what it trades:** Dividend-growth streaks attract re-rating from income buyers.

### Cash flow / share  (`cfps`)
- **Meaning:** Operating cash flow per share.
- **What good looks like:** Higher than EPS = clean earnings.
- **What we're targeting:** Cash earning power per share.
- **Alpha / what it trades:** CFPS > EPS confirms earnings quality.

## Quality scores

### Altman Z-score  (`altman_z`)
- **Meaning:** Bankruptcy-risk composite from five ratios.
- **What good looks like:** >2.99 safe · 1.81-2.99 grey · <1.81 distress.
- **What we're targeting:** Screen for financial-distress risk.
- **Alpha / what it trades:** Rising Z out of the distress zone is a turnaround long; falling into it is an early short.

### Piotroski F-score  (`piotroski_f`)
- **Meaning:** 0-9 count of improving fundamental signals.
- **What good looks like:** 8-9 strong · 0-2 weak.
- **What we're targeting:** Is the business fundamentally getting better year on year.
- **Alpha / what it trades:** High F-score among cheap stocks historically outperforms — a value+quality overlay.

### DuPont ROE  (`dupont_roe`)
- **Meaning:** ROE decomposed into margin x asset turnover x leverage.
- **What good looks like:** ROE driven by margin/turnover (quality) rather than leverage (fragile).
- **What we're targeting:** Understand WHY a company earns its ROE.
- **Alpha / what it trades:** Own high-quality-driven ROE; fade leverage-driven ROE that looks superficially similar.

## Risk (price-based)

### Total return (5y)  (`total_return`)
- **Meaning:** Price return over the window.
- **What good looks like:** Higher, but judge vs risk taken.
- **What we're targeting:** Realised performance.
- **Alpha / what it trades:** Context for mean-reversion vs momentum positioning.

### Annualised return  (`ann_return`)
- **Meaning:** Compounded yearly return.
- **What good looks like:** Higher relative to volatility.
- **What we're targeting:** Return per year.
- **Alpha / what it trades:** Numerator of risk-adjusted return; pair with vol.

### Annualised volatility  (`ann_vol`)
- **Meaning:** Standard deviation of returns, annualised.
- **What good looks like:** Lower for the same return.
- **What we're targeting:** How bumpy the ride is.
- **Alpha / what it trades:** Position-sizing input; low-vol anomaly favours owning lower-vol names.

### Downside volatility  (`downside_vol`)
- **Meaning:** Volatility of negative returns only.
- **What good looks like:** Lower.
- **What we're targeting:** Bad-side risk that investors actually care about.
- **Alpha / what it trades:** Sortino/downside focus separates genuinely defensive names from merely low-return ones.

### Beta  (`beta`)
- **Meaning:** Sensitivity to the benchmark (SPY).
- **What good looks like:** Context-dependent: <1 defensive, >1 aggressive.
- **What we're targeting:** Market-risk exposure and hedge sizing.
- **Alpha / what it trades:** Beta-timing (add high-beta into rallies, rotate to low-beta into stress) and portfolio hedging.

### Max drawdown  (`max_drawdown`)
- **Meaning:** Largest peak-to-trough decline.
- **What good looks like:** Shallower (closer to zero).
- **What we're targeting:** Worst-case pain the position inflicted.
- **Alpha / what it trades:** Drawdown depth/duration sets how large a position the book can stomach — sizing discipline.

### 12-month momentum  (`momentum_12m`)
- **Meaning:** Price return over ~12 months (skipping the last month).
- **What good looks like:** Positive and persistent.
- **What we're targeting:** Trend strength.
- **Alpha / what it trades:** Cross-sectional momentum is a durable factor — long winners, short losers.

### Sharpe ratio  (`sharpe`)
- **Meaning:** Excess return per unit of volatility.
- **What good looks like:** >1 good; higher is better.
- **What we're targeting:** Risk-adjusted return quality.
- **Alpha / what it trades:** Rank names on risk-adjusted return, not raw return, to build a more efficient book.

## Factors

### Value factor (z)  (`value`)
- **Meaning:** Cross-sectional cheapness score (cheap = high).
- **What good looks like:** Positive = cheaper than the universe.
- **What we're targeting:** Systematic cheapness rank.
- **Alpha / what it trades:** Value premium: tilt toward high-value-z, avoid crowded expensive names.

### Quality factor (z)  (`quality`)
- **Meaning:** Composite of ROIC, FCF conversion, margin, low leverage.
- **What good looks like:** Positive = higher quality.
- **What we're targeting:** Systematic quality rank.
- **Alpha / what it trades:** Quality premium: durable compounders outperform on a risk-adjusted basis.

### Growth factor (z)  (`growth`)
- **Meaning:** Composite of revenue and EPS growth.
- **What good looks like:** Positive = faster-growing.
- **What we're targeting:** Systematic growth rank.
- **Alpha / what it trades:** Growth tilt works when durable and not over-paid (combine with value).

### Momentum factor (z)  (`momentum`)
- **Meaning:** Standardised 12-month price momentum.
- **What good looks like:** Positive = trending up.
- **What we're targeting:** Systematic trend rank.
- **Alpha / what it trades:** Momentum factor: long the top, manage the reversal risk at extremes.

### Composite score  (`composite`)
- **Meaning:** Equal-weight average of value+quality+growth+momentum z-scores.
- **What good looks like:** Higher = better all-round on the four factors.
- **What we're targeting:** One-number multi-factor rank.
- **Alpha / what it trades:** A prototype systematic screen: the top decile is the deep-dive shortlist.

## Widget-level intent

Each dashboard widget also carries an *intent / good / target / alpha* explainer:

- **`pm_valuation`** — Give the PM a one-glance read of where every name trades vs its sector on the four multiples that matter. _Alpha:_ Buy cheap-and-high-return, avoid cheap-and-low-return — the core valuation-discipline trade.
- **`pm_quality_val`** — Plot cheapness (EV/EBITDA) against quality (ROIC) so the trade-off is visual. _Alpha:_ Top-left names are the highest-conviction longs; bottom-right are funding shorts/avoids.
- **`pm_commentary`** — Turn the numbers into a written brief a PM can read in 30 seconds, every claim traceable. _Alpha:_ Speeds conviction and surfaces the shortlist worth deep due-diligence first.
- **`pm_capital_return`** — Show income contribution across the book at a glance. _Alpha:_ Covered-yield compounders anchor total return; unsustainable yields are dividend-cut shorts.
- **`hoi_sector_heat`** — A capital-allocation heatmap: which theme is cheap, high-quality, growing, and clean on leverage. _Alpha:_ Top-down tilt toward the best risk-adjusted theme is a repeatable source of allocation alpha.
- **`hoi_cheap_quality`** — The intersection of the value and quality factors — the shortlist that is both cheap and good. _Alpha:_ Cheap+quality is the most reliable factor combination for forward excess return.
- **`hoi_risk_register`** — A governance view of everything tripping a distress, cash-quality, leverage or profitability flag. _Alpha:_ Avoiding blow-ups is negative-alpha-avoidance — often worth more than the next winner.
- **`pa_comps`** — The analyst workhorse: the full ratio set for all 32 names, percentile-shaded so best-in-class is obvious. _Alpha:_ Fast, consistent comps replace hours of spreadsheet work and surface mispriced quality.
- **`pa_dupont`** — Break ROE into margin x asset turnover x leverage to see HOW the return is earned. _Alpha:_ Own high-quality-driven ROE; short/avoid names whose ROE is just balance-sheet gearing.
- **`pa_fcf_trend`** — Track FCF-to-net-income over five years — the clearest earnings-quality signal. _Alpha:_ Deteriorating conversion is an early short; hidden high conversion is a quality-compounder long.
- **`qa_factors`** — A systematic value/quality/growth/momentum scorecard and composite rank. _Alpha:_ The top of the composite rank is a factor-tilted long book; the bottom funds it.
- **`qa_corr`** — Pairwise return correlations for signal and structure detection. _Alpha:_ High-correlation pairs enable relative-value/pairs trades; low correlation improves the book's efficiency.
- **`qa_perf`** — Measure how fast the free-tier API returns each dataset and how many names fit the daily cap. _Alpha:_ Data-ops reality check — governs refresh cadence and universe size for any live signal.
- **`pr_riskstats`** — Return, volatility, beta, drawdown and Sharpe for every name vs the benchmark. _Alpha:_ Building the book on Sharpe and drawdown, not headline return, raises realised risk-adjusted alpha.
- **`pr_drawdown`** — Show the growth-of-$100 path and the drawdown it took to get there. _Alpha:_ Drawdown-aware sizing keeps positions survivable through stress — the discipline that preserves alpha.
- **`pr_corr`** — The correlation matrix read for portfolio construction rather than signals. _Alpha:_ Combining uncorrelated return streams raises the book's Sharpe — diversification is the only free lunch.
