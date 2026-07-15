"""
Role-based insight builders (>=3 per role) + rule-based Portfolio Manager commentary.

Each insight is a JSON-embeddable dict the report renders. Table insights *reference*
metric keys (report.py looks up DATA.metrics/risk/factors) to avoid duplicating the
calculation logic that powers the expandable "show calculation" panels.

Provenance: every insight carries `source` (which FMP endpoints feed it) and
`last_updated`; DEMO mode labels the synthetic origin explicitly.
"""

from __future__ import annotations
import statistics as st
from .config import UNIVERSE, ticker_to_sector, BENCHMARK
from .glossary import INSIGHT_EXPLAINERS

# Which FMP endpoints feed each analytic domain (for provenance labels)
SRC = {
    "valuation": "profile + income-statement + balance-sheet + cash-flow",
    "fundamental": "income-statement + balance-sheet + cash-flow",
    "quality": "income-statement + balance-sheet + cash-flow + financial-scores",
    "growth": "income-statement + financial-growth",
    "risk": "historical-price-eod/full (+ SPY benchmark)",
    "factor": "profile + statements + historical-price-eod",
    "dividend": "dividends + profile",
}


def _src(mode: str, domain: str) -> str:
    ep = SRC.get(domain, domain)
    return (f"DEMO (synthetic) — mirrors FMP: {ep}" if mode == "DEMO"
            else f"FMP /stable/ : {ep}")


def _median(xs):
    xs = [x for x in xs if x is not None]
    return round(st.median(xs), 4) if xs else None


def _sector_medians(metrics, keys):
    out = {}
    for sector, tickers in UNIVERSE.items():
        out[sector] = {}
        for k, dom in keys:
            out[sector][k] = _median([metrics[t][k]["value"] for t in tickers])
    return out


def build_insights(dataset, tr) -> dict:
    metrics, risk, factors = tr["metrics"], tr["risk"], tr["factors"]
    companies = dataset["companies"]
    mode = tr["mode"]
    ts = tr["retrieved"]
    t2s = ticker_to_sector()
    tickers = list(companies.keys())

    def ins(id, title, subtitle, widget, domain, payload, notes):
        return {"id": id, "title": title, "subtitle": subtitle, "widget": widget,
                "source": _src(mode, domain), "last_updated": ts, "mode": mode,
                "payload": payload, "notes": notes,
                "explainer": INSIGHT_EXPLAINERS.get(id)}

    out = {"Portfolio Manager": [], "Head of Investment": [], "Portfolio Analyst": [],
           "Quantitative Analyst": [], "Performance & Risk Analyst": []}

    # ---------------- Portfolio Manager ----------------
    out["Portfolio Manager"].append(ins(
        "pm_valuation", "Peer valuation snapshot",
        "Where each name trades vs its sector median — P/E, EV/EBITDA, FCF yield, dividend yield.",
        "metric_table", "valuation",
        {"source_domain": "metrics",
         "columns": [
             {"key": "pe", "label": "P/E", "unit": "x", "good": "low"},
             {"key": "ev_ebitda", "label": "EV/EBITDA", "unit": "x", "good": "low"},
             {"key": "fcf_yield", "label": "FCF yield", "unit": "%", "good": "high"},
             {"key": "dividend_yield", "label": "Div yield", "unit": "%", "good": "high"},
             {"key": "roic", "label": "ROIC", "unit": "%", "good": "high"},
         ], "scope": "all", "sort_by": "ev_ebitda", "sort_dir": "asc",
         "sector_median": True},
        "Read cheapness against quality — a low EV/EBITDA alongside high ROIC is a genuine opportunity; "
        "low multiple + low ROIC is usually a value trap."))

    out["Portfolio Manager"].append(ins(
        "pm_quality_val", "Quality vs valuation",
        "Is the cheapness earned? X = EV/EBITDA (cheap → left), Y = ROIC (quality → up). Bubble = market cap.",
        "scatter", "valuation",
        {"x_key": "ev_ebitda", "y_key": "roic", "size": "market_cap", "source_domain": "metrics",
         "x_label": "EV/EBITDA (x)", "y_label": "ROIC (%)"},
        "Top-left = cheap & high-return (best). Bottom-right = expensive & low-return (avoid). "
        "The diagonal is fair value."))

    out["Portfolio Manager"].append(ins(
        "pm_commentary", "Auto-generated PM commentary",
        "Narrative derived deterministically from the metrics below — every claim is traceable to a number.",
        "commentary", "valuation",
        {"paragraphs": _pm_commentary(metrics, risk, factors, t2s)},
        "Rule-based, reproducible. Expand any figure in the tables to see the exact calculation behind a sentence."))

    out["Portfolio Manager"].append(ins(
        "pm_capital_return", "Capital-return snapshot",
        "Dividend yield by name — income contribution across the book.",
        "bar", "dividend",
        {"key": "dividend_yield", "source_domain": "metrics", "label": "Dividend yield (%)", "sort_dir": "desc"},
        "Blend of yield + reinvestment. Utilities anchor income; AI/robotics contribute growth, not yield."))

    # ---------------- Head of Investment ----------------
    sm = _sector_medians(metrics, [("ev_ebitda", "valuation"), ("roic", "quality"),
                                    ("revenue_cagr", "growth"), ("net_debt_ebitda", "quality"),
                                    ("fcf_conversion", "quality")])
    out["Head of Investment"].append(ins(
        "hoi_sector_heat", "Sector aggregates heatmap",
        "Median valuation, quality, growth and leverage by theme — where to lean in and lean out.",
        "sector_heatmap", "fundamental",
        {"data": sm, "columns": [
            {"key": "ev_ebitda", "label": "EV/EBITDA", "good": "low"},
            {"key": "roic", "label": "ROIC", "good": "high"},
            {"key": "revenue_cagr", "label": "Rev CAGR", "good": "high"},
            {"key": "fcf_conversion", "label": "FCF conv.", "good": "high"},
            {"key": "net_debt_ebitda", "label": "ND/EBITDA", "good": "low"}]},
        "Capital-allocation lens: favour themes combining reasonable multiples with high ROIC and clean cash conversion."))

    out["Head of Investment"].append(ins(
        "hoi_cheap_quality", "Cheap-and-quality screen",
        "Names scoring positively on BOTH value and quality factors (z > 0).",
        "metric_table", "factor",
        {"source_domain": "factors",
         "columns": [{"key": "value", "label": "Value z", "good": "high"},
                     {"key": "quality", "label": "Quality z", "good": "high"},
                     {"key": "growth", "label": "Growth z", "good": "high"},
                     {"key": "composite", "label": "Composite", "good": "high"}],
         "scope": "all", "sort_by": "composite", "sort_dir": "desc",
         "filter": {"value": 0.0, "quality": 0.0}},
        "The intersection of cheap and good — the shortlist that merits deep due-diligence first."))

    out["Head of Investment"].append(ins(
        "hoi_risk_register", "Risk-flag register",
        "Names tripping distress / cash-quality / leverage / profitability flags.",
        "flag_table", "quality",
        {"rows": _risk_flags(metrics, t2s, companies)},
        "Governance view — anything here needs a thesis for why the flag is temporary, or it stays off the buy list."))

    # ---------------- Portfolio Analyst ----------------
    out["Portfolio Analyst"].append(ins(
        "pa_comps", "Quality-scored comparables grid",
        "The workhorse: full ratio set, percentile-shaded vs the 32-name universe. Sort any column.",
        "metric_table", "fundamental",
        {"source_domain": "metrics", "shade_pct": True,
         "columns": [
             {"key": "gross_margin", "label": "Gross m.", "unit": "%", "good": "high"},
             {"key": "operating_margin", "label": "Op m.", "unit": "%", "good": "high"},
             {"key": "net_margin", "label": "Net m.", "unit": "%", "good": "high"},
             {"key": "roe", "label": "ROE", "unit": "%", "good": "high"},
             {"key": "roic", "label": "ROIC", "unit": "%", "good": "high"},
             {"key": "revenue_cagr", "label": "Rev CAGR", "unit": "%", "good": "high"},
             {"key": "fcf_conversion", "label": "FCF conv.", "unit": "%", "good": "high"},
             {"key": "net_debt_ebitda", "label": "ND/EBITDA", "unit": "x", "good": "low"},
             {"key": "ev_ebitda", "label": "EV/EBITDA", "unit": "x", "good": "low"},
             {"key": "pe", "label": "P/E", "unit": "x", "good": "low"},
             {"key": "altman_z", "label": "Altman Z", "unit": "", "good": "high"},
             {"key": "piotroski_f", "label": "Piotroski", "unit": "/9", "good": "high"},
         ], "scope": "all", "sort_by": "roic", "sort_dir": "desc"},
        "Percentile shading turns 32×12 numbers into an instant read: dark-green cells are the best-in-universe."))

    out["Portfolio Analyst"].append(ins(
        "pa_dupont", "DuPont ROE bridge",
        "Decompose ROE = Net margin × Asset turnover × Equity multiplier (select a company to compare vs peers).",
        "dupont", "fundamental",
        {"data": {t: {
            "net_margin": metrics[t]["net_margin"]["value"],
            "asset_turnover": metrics[t]["asset_turnover"]["value"],
            "equity_multiplier": (metrics[t]["dupont_roe"]["inputs"].get("equity_multiplier")),
            "roe": metrics[t]["roe"]["value"]} for t in tickers}},
        "Separates *how* a company earns its ROE — fat margins vs asset efficiency vs leverage. Leverage-driven ROE is lower quality."))

    out["Portfolio Analyst"].append(ins(
        "pa_fcf_trend", "FCF conversion trend (5y)",
        "Free cash flow ÷ net income over time — the single best tell for earnings quality.",
        "lines", "quality",
        {"series": _fcf_trend(companies)},
        "Persistently > 80% = high-quality earnings. Utilities dip on heavy capex; asset-light names convert best."))

    # ---------------- Quantitative Analyst ----------------
    out["Quantitative Analyst"].append(ins(
        "qa_factors", "Multi-factor composite",
        "Value / Quality / Growth / Momentum z-scores and the equal-weighted composite, ranked.",
        "metric_table", "factor",
        {"source_domain": "factors",
         "columns": [{"key": "value", "label": "Value", "good": "high"},
                     {"key": "quality", "label": "Quality", "good": "high"},
                     {"key": "growth", "label": "Growth", "good": "high"},
                     {"key": "momentum", "label": "Momentum", "good": "high"},
                     {"key": "composite", "label": "Composite", "good": "high"}],
         "scope": "all", "sort_by": "composite", "sort_dir": "desc", "shade_pct": True},
        "Prototype for a systematic screen. On free tier the universe is US-only and capped at 250 calls/day — "
        "fine for research, not for a daily full-market factor run."))

    out["Quantitative Analyst"].append(ins(
        "qa_corr", "Return correlation matrix",
        "Pairwise weekly-return correlations across the 32 names.",
        "heatmap_matrix", "risk",
        {"matrix": tr["correlation"]},
        "Cluster detection for pair trades and diversification. Semis cluster tightly; utilities are the diversifier."))

    out["Quantitative Analyst"].append(ins(
        "qa_perf", "API extraction performance",
        "Latency, payload size and status for each free-tier endpoint (your 'how fast can we get data' test).",
        "perf_table", "risk",
        {"placeholder": True},
        "Populated live by the perf harness (perf.py). Governs how large a universe you can refresh inside the daily cap."))

    # ---------------- Performance & Risk Analyst ----------------
    out["Performance & Risk Analyst"].append(ins(
        "pr_riskstats", "Return / risk statistics",
        f"Annualised return, volatility, beta vs {BENCHMARK}, max drawdown and Sharpe (5y weekly).",
        "metric_table", "risk",
        {"source_domain": "risk",
         "columns": [{"key": "ann_return", "label": "Ann ret", "unit": "%", "good": "high"},
                     {"key": "ann_vol", "label": "Ann vol", "unit": "%", "good": "low"},
                     {"key": "beta", "label": "Beta", "unit": "", "good": "low"},
                     {"key": "max_drawdown", "label": "Max DD", "unit": "%", "good": "high"},
                     {"key": "sharpe", "label": "Sharpe", "unit": "x", "good": "high"},
                     {"key": "momentum_12m", "label": "12m mom", "unit": "%", "good": "high"}],
         "scope": "all", "sort_by": "sharpe", "sort_dir": "desc"},
        "Risk-adjusted lens. Low-beta utilities dampen drawdown; high-beta semis/robotics drive both upside and tail risk."))

    out["Performance & Risk Analyst"].append(ins(
        "pr_drawdown", "Drawdown & cumulative return",
        "Cumulative growth of $100 and drawdown path (select names to compare).",
        "lines", "risk",
        {"series": _perf_series(companies, dataset["benchmark"])},
        "Sizing lens — depth and duration of drawdowns tells you how much of a position the book can stomach."))

    out["Performance & Risk Analyst"].append(ins(
        "pr_corr", "Diversification matrix",
        "Same correlation matrix, read for portfolio construction rather than signals.",
        "heatmap_matrix", "risk",
        {"matrix": tr["correlation"]},
        "Low/negative correlations are the raw material for diversification. Utilities vs semis is the natural hedge pair here."))

    return out


# ---------------------------------------------------------------------------
# Rule-based Portfolio-Manager commentary
# ---------------------------------------------------------------------------
def _pm_commentary(metrics, risk, factors, t2s):
    ranked = sorted(factors.items(), key=lambda kv: (kv[1]["composite"] is not None, kv[1]["composite"] or -9), reverse=True)
    top = [t for t, _ in ranked[:3]]
    bottom = [t for t, _ in ranked[-3:]]
    cheap_quality = [t for t in factors if (factors[t]["value"] or -9) > 0.5 and (factors[t]["quality"] or -9) > 0.5]
    best_fcf = sorted(metrics, key=lambda t: (metrics[t]["fcf_conversion"]["value"] or -9), reverse=True)[:3]
    best_roic = sorted(metrics, key=lambda t: (metrics[t]["roic"]["value"] or -9), reverse=True)[:3]
    distress = [t for t in metrics if (metrics[t]["altman_z"]["value"] or 99) < 1.81]
    neg_fcf = [t for t in metrics if (metrics[t]["fcf_conversion"]["value"] or 1) < 0]
    lossmaking = [t for t in metrics if (metrics[t]["net_margin"]["value"] or 1) < 0]
    high_lev = [t for t in metrics if (metrics[t]["net_debt_ebitda"]["value"] or 0) > 4]

    P = []
    P.append({"text":
        f"On the equal-weighted value+quality+growth+momentum composite, the strongest names are "
        f"{', '.join(top)}, while {', '.join(bottom)} screen weakest. Composite is the average of four "
        f"cross-sectional z-scores, so it is relative to this 32-name universe, not an absolute call.",
        "source": "factors (profile + statements + prices)"})
    if cheap_quality:
        P.append({"text":
            f"Cheap AND high-quality (value z>0.5 and quality z>0.5): {', '.join(cheap_quality)}. "
            f"These are where a re-rating is most likely to be earned rather than a value trap.",
            "source": "factors"})
    P.append({"text":
        f"Highest returns on capital: {', '.join(best_roic)} (ROIC "
        f"{', '.join(_fmt_pct(metrics[t]['roic']['value']) for t in best_roic)}). "
        f"Best cash conversion (FCF/NI): {', '.join(best_fcf)}. High ROIC with high cash conversion is the "
        f"combination that compounds.",
        "source": "income-statement + balance-sheet + cash-flow"})
    flags = []
    if distress: flags.append(f"Altman-Z distress zone: {', '.join(distress)}")
    if neg_fcf: flags.append(f"negative FCF conversion: {', '.join(neg_fcf)}")
    if lossmaking: flags.append(f"loss-making: {', '.join(lossmaking)}")
    if high_lev: flags.append(f"ND/EBITDA > 4x: {', '.join(high_lev)}")
    if flags:
        P.append({"text": "Watch-items — " + "; ".join(flags) + ". Each needs a specific thesis for why the "
                          "flag is transitory before it earns a position.", "source": "quality screens"})
    return P


def _fmt_pct(v):
    return "n/a" if v is None else f"{v*100:.0f}%"


def _risk_flags(metrics, t2s, companies):
    rows = []
    for t, m in metrics.items():
        fl = []
        if (m["altman_z"]["value"] or 99) < 1.81: fl.append("Altman-Z distress")
        if (m["fcf_conversion"]["value"] or 1) < 0: fl.append("Neg. FCF conversion")
        if (m["net_margin"]["value"] or 1) < 0: fl.append("Loss-making")
        if (m["net_debt_ebitda"]["value"] or 0) > 4: fl.append("High leverage")
        if (m["interest_coverage"]["value"] or 99) < 3: fl.append("Thin interest cover")
        if fl:
            rows.append({"ticker": t, "name": companies[t]["name"], "sector": t2s[t], "flags": fl})
    return rows


def _fcf_trend(companies):
    series = {}
    for t, c in companies.items():
        yrs = c["years"]
        pts = []
        for y in yrs:
            ni = c["income"][y]["net_income"]; fcf = c["cash_flow"][y]["free_cash_flow"]
            pts.append(None if ni == 0 else round(fcf / ni, 3))
        series[t] = {"x": yrs, "y": pts, "sector": c["sector"]}
    return series


def _perf_series(companies, bench):
    """Cumulative growth of $100 (weekly) + drawdown path, downsampled to keep size sane."""
    out = {}
    def cum_and_dd(closes):
        step = max(1, len(closes) // 130)  # downsample to ~130 points
        cl = closes[::step]
        base = cl[0]
        cum = [round(100 * x / base, 2) for x in cl]
        peak, dd = cl[0], []
        for x in cl:
            peak = max(peak, x)
            dd.append(round((x / peak - 1) * 100, 2))
        return cum, dd
    for t, c in companies.items():
        cum, dd = cum_and_dd(c["prices"]["closes"])
        out[t] = {"cum": cum, "dd": dd, "sector": c["sector"]}
    bcum, bdd = cum_and_dd(bench["prices"]["closes"])
    out[bench["ticker"]] = {"cum": bcum, "dd": bdd, "sector": "Benchmark"}
    return out
