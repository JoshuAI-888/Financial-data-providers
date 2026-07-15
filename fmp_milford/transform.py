"""
Metric engine: turns normalized company records (demo or live FMP) into the full
set of investment metrics, each carrying its formula + inputs + step-by-step logic
so the report can render an expandable "show calculation" panel for every figure.

Also computes cross-sectional factor z-scores and price-based risk analytics.

Design: metrics are plain dicts (JSON-embeddable) via `calc(...)`:
  {value, formula, inputs, steps, unit, good}  where good in {"high","low"} marks
  which direction is favourable (drives colour + ranking).
"""

from __future__ import annotations
import math
import statistics as st
from datetime import date, timedelta


def calc(value, formula, inputs, steps, unit="", good="high"):
    return {"value": value, "formula": formula, "inputs": inputs, "steps": steps, "unit": unit, "good": good}


def sdiv(a, b):
    try:
        if a is None or b in (None, 0):
            return None
        return a / b
    except Exception:
        return None


def cagr(first, last, periods):
    if first is None or last is None or first <= 0 or last <= 0 or periods <= 0:
        return None
    return (last / first) ** (1 / periods) - 1


# ---------------------------------------------------------------------------
# Per-company fundamental metrics (latest FY)
# ---------------------------------------------------------------------------
def company_metrics(c: dict) -> dict:
    yrs = c["years"]
    y, y0 = yrs[-1], yrs[0]
    inc, bal, cf = c["income"], c["balance"], c["cash_flow"]
    I, B, F = inc[y], bal[y], cf[y]
    Ip = inc[yrs[-2]] if len(yrs) > 1 else I
    Bp = bal[yrs[-2]] if len(yrs) > 1 else B

    rev, ni, ebitda = I["revenue"], I["net_income"], I["ebitda"]
    ebit = I["operating_income"]
    gp, da, intr = I["gross_profit"], I["dep_amort"], I["interest_expense"]
    assets, equity, debt, cash = B["total_assets"], B["total_equity"], B["total_debt"], B["cash"]
    ca, cl, inv, rec, pay = B["current_assets"], B["current_liabilities"], B["inventory"], B["receivables"], B["payables"]
    ocf, capex, fcf = F["operating_cf"], F["capex"], F["free_cash_flow"]
    shares, eps = I["shares"], I["eps"]
    mcap, price = c["market_cap"], c["price"]
    net_debt = debt - cash
    ev = mcap + net_debt
    tax_rate = 0.21
    nopat = ebit * (1 - tax_rate)
    invested_capital = debt + equity - cash
    avg_equity = (equity + Bp["total_equity"]) / 2
    avg_assets = (assets + Bp["total_assets"]) / 2

    m = {}
    # --- Profitability ---
    m["gross_margin"] = calc(sdiv(gp, rev), "Gross profit / Revenue",
        {"gross_profit": gp, "revenue": rev}, [f"{gp:,.0f} / {rev:,.0f}"], "%")
    m["ebitda_margin"] = calc(sdiv(ebitda, rev), "EBITDA / Revenue",
        {"ebitda": ebitda, "revenue": rev}, [f"{ebitda:,.0f} / {rev:,.0f}"], "%")
    m["operating_margin"] = calc(sdiv(ebit, rev), "Operating income / Revenue",
        {"operating_income": ebit, "revenue": rev}, [f"{ebit:,.0f} / {rev:,.0f}"], "%")
    m["net_margin"] = calc(sdiv(ni, rev), "Net income / Revenue",
        {"net_income": ni, "revenue": rev}, [f"{ni:,.0f} / {rev:,.0f}"], "%")
    m["roe"] = calc(sdiv(ni, avg_equity), "Net income / Average equity",
        {"net_income": ni, "avg_equity": round(avg_equity, 1)},
        [f"avg equity = ({equity:,.0f}+{Bp['total_equity']:,.0f})/2 = {avg_equity:,.0f}", f"{ni:,.0f} / {avg_equity:,.0f}"], "%")
    m["roa"] = calc(sdiv(ni, avg_assets), "Net income / Average assets",
        {"net_income": ni, "avg_assets": round(avg_assets, 1)}, [f"{ni:,.0f} / {avg_assets:,.0f}"], "%")
    m["roic"] = calc(sdiv(nopat, invested_capital), "NOPAT / Invested capital  (NOPAT = EBIT x (1-tax))",
        {"ebit": ebit, "tax_rate": tax_rate, "nopat": round(nopat, 1), "debt": debt, "equity": equity, "cash": cash},
        [f"NOPAT = {ebit:,.0f} x (1-{tax_rate}) = {nopat:,.0f}",
         f"Invested capital = {debt:,.0f}+{equity:,.0f}-{cash:,.0f} = {invested_capital:,.0f}",
         f"{nopat:,.0f} / {invested_capital:,.0f}"], "%")
    m["roce"] = calc(sdiv(ebit, assets - cl), "EBIT / (Total assets - Current liabilities)",
        {"ebit": ebit, "total_assets": assets, "current_liabilities": cl},
        [f"{ebit:,.0f} / ({assets:,.0f}-{cl:,.0f})"], "%")

    # --- Growth (5y CAGR) ---
    n = len(yrs) - 1
    m["revenue_cagr"] = calc(cagr(inc[y0]["revenue"], rev, n), f"({n}y revenue CAGR)",
        {"first": inc[y0]["revenue"], "last": rev, "years": n},
        [f"({rev:,.0f}/{inc[y0]['revenue']:,.0f})^(1/{n}) - 1"], "%")
    m["eps_cagr"] = calc(cagr(inc[y0]["eps"], eps, n), f"({n}y EPS CAGR)",
        {"first": inc[y0]["eps"], "last": eps, "years": n}, [f"({eps}/{inc[y0]['eps']})^(1/{n}) - 1"], "%")
    m["fcf_cagr"] = calc(cagr(cf[y0]["free_cash_flow"], fcf, n), f"({n}y FCF CAGR)",
        {"first": cf[y0]["free_cash_flow"], "last": fcf, "years": n}, ["(last/first)^(1/n)-1"], "%")

    # --- Liquidity ---
    m["current_ratio"] = calc(sdiv(ca, cl), "Current assets / Current liabilities",
        {"current_assets": ca, "current_liabilities": cl}, [f"{ca:,.0f} / {cl:,.0f}"], "x", "high")
    m["quick_ratio"] = calc(sdiv(ca - inv, cl), "(Current assets - Inventory) / Current liabilities",
        {"current_assets": ca, "inventory": inv, "current_liabilities": cl}, [f"({ca:,.0f}-{inv:,.0f}) / {cl:,.0f}"], "x", "high")
    m["interest_coverage"] = calc(sdiv(ebit, intr), "EBIT / Interest expense",
        {"ebit": ebit, "interest_expense": intr}, [f"{ebit:,.0f} / {intr:,.0f}"], "x", "high")

    # --- Leverage ---
    m["net_debt_ebitda"] = calc(sdiv(net_debt, ebitda), "(Total debt - Cash) / EBITDA",
        {"total_debt": debt, "cash": cash, "ebitda": ebitda}, [f"({debt:,.0f}-{cash:,.0f}) / {ebitda:,.0f}"], "x", "low")
    m["debt_to_equity"] = calc(sdiv(debt, equity), "Total debt / Total equity",
        {"total_debt": debt, "total_equity": equity}, [f"{debt:,.0f} / {equity:,.0f}"], "x", "low")
    m["gearing"] = calc(sdiv(debt, debt + equity), "Total debt / (Debt + Equity)",
        {"total_debt": debt, "total_equity": equity}, [f"{debt:,.0f} / ({debt:,.0f}+{equity:,.0f})"], "%", "low")

    # --- Efficiency ---
    m["asset_turnover"] = calc(sdiv(rev, assets), "Revenue / Total assets",
        {"revenue": rev, "total_assets": assets}, [f"{rev:,.0f} / {assets:,.0f}"], "x", "high")
    dso = sdiv(rec * 365, rev); dio = sdiv(inv * 365, rev * 0.7); dpo = sdiv(pay * 365, rev * 0.7)
    ccc = None if None in (dso, dio, dpo) else dso + dio - dpo
    m["cash_conversion_cycle"] = calc(ccc, "DSO + DIO - DPO (days)",
        {"DSO": round(dso, 1) if dso else None, "DIO": round(dio, 1) if dio else None, "DPO": round(dpo, 1) if dpo else None},
        ["DSO=receivables*365/rev", "DIO=inventory*365/COGS", "DPO=payables*365/COGS"], "days", "low")

    # --- Cash conversion (the quality tell) ---
    m["fcf_conversion"] = calc(sdiv(fcf, ni), "Free cash flow / Net income",
        {"free_cash_flow": fcf, "net_income": ni}, [f"{fcf:,.0f} / {ni:,.0f}"], "%", "high")
    m["ocf_ebitda"] = calc(sdiv(ocf, ebitda), "Operating cash flow / EBITDA",
        {"operating_cf": ocf, "ebitda": ebitda}, [f"{ocf:,.0f} / {ebitda:,.0f}"], "%", "high")
    m["capex_sales"] = calc(sdiv(capex, rev), "Capex / Revenue (capital intensity)",
        {"capex": capex, "revenue": rev}, [f"{capex:,.0f} / {rev:,.0f}"], "%", "low")

    # --- Valuation ---
    m["pe"] = calc(sdiv(mcap, ni) if ni > 0 else None, "Market cap / Net income",
        {"market_cap": mcap, "net_income": ni}, [f"{mcap:,.0f} / {ni:,.0f}"], "x", "low")
    m["ev_ebitda"] = calc(sdiv(ev, ebitda), "Enterprise value / EBITDA  (EV = mcap + net debt)",
        {"market_cap": mcap, "net_debt": round(net_debt, 1), "ev": round(ev, 1), "ebitda": ebitda},
        [f"EV = {mcap:,.0f}+{net_debt:,.0f} = {ev:,.0f}", f"{ev:,.0f} / {ebitda:,.0f}"], "x", "low")
    m["ev_sales"] = calc(sdiv(ev, rev), "Enterprise value / Revenue",
        {"ev": round(ev, 1), "revenue": rev}, [f"{ev:,.0f} / {rev:,.0f}"], "x", "low")
    m["pb"] = calc(sdiv(mcap, equity), "Market cap / Total equity",
        {"market_cap": mcap, "total_equity": equity}, [f"{mcap:,.0f} / {equity:,.0f}"], "x", "low")
    m["p_fcf"] = calc(sdiv(mcap, fcf) if fcf > 0 else None, "Market cap / Free cash flow",
        {"market_cap": mcap, "free_cash_flow": fcf}, [f"{mcap:,.0f} / {fcf:,.0f}"], "x", "low")
    m["fcf_yield"] = calc(sdiv(fcf, mcap), "Free cash flow / Market cap",
        {"free_cash_flow": fcf, "market_cap": mcap}, [f"{fcf:,.0f} / {mcap:,.0f}"], "%", "high")
    m["dividend_yield"] = calc(c["dividend_yield"] / 100.0, "Dividend per share / Price",
        {"dps": c["dividend_per_share"], "price": price}, [f"{c['dividend_per_share']} / {price}"], "%", "high")
    growth_pct = m["eps_cagr"]["value"]
    m["peg"] = calc(sdiv(m["pe"]["value"], growth_pct * 100) if (m["pe"]["value"] and growth_pct and growth_pct > 0) else None,
        "P/E / EPS growth %", {"pe": m["pe"]["value"], "eps_growth_%": round(growth_pct * 100, 1) if growth_pct else None},
        ["PEG < 1 = growth cheap vs earnings"], "x", "low")

    # --- Per share ---
    m["eps"] = calc(eps, "Net income / Shares", {"net_income": ni, "shares": shares}, [f"{ni:,.0f} / {shares:,.0f}"], "$", "high")
    m["bvps"] = calc(sdiv(equity, shares), "Equity / Shares", {"equity": equity, "shares": shares}, [f"{equity:,.0f} / {shares:,.0f}"], "$", "high")
    m["dps"] = calc(c["dividend_per_share"], "Declared dividend per share", {"dps": c["dividend_per_share"]}, ["from dividends feed"], "$", "high")
    m["cfps"] = calc(sdiv(ocf, shares), "Operating cash flow / Shares", {"ocf": ocf, "shares": shares}, [f"{ocf:,.0f} / {shares:,.0f}"], "$", "high")

    # --- DuPont identity ---
    npm, ato, em = sdiv(ni, rev), sdiv(rev, avg_assets), sdiv(avg_assets, avg_equity)
    dp = None if None in (npm, ato, em) else npm * ato * em
    m["dupont_roe"] = calc(dp, "Net margin x Asset turnover x Equity multiplier",
        {"net_margin": round(npm, 4) if npm else None, "asset_turnover": round(ato, 3) if ato else None,
         "equity_multiplier": round(em, 3) if em else None},
        [f"{npm:.3f} x {ato:.3f} x {em:.3f}" if dp else "n/a"], "%", "high")

    # --- Quality scores ---
    m["altman_z"] = _altman_z(rev, ebit, mcap, ca, cl, assets, B["retained_earnings"], B["total_liabilities"])
    m["piotroski_f"] = _piotroski(inc, bal, cf, yrs)

    return m


def _altman_z(rev, ebit, mcap, ca, cl, assets, retained, tot_liab):
    A = sdiv(ca - cl, assets); Bx = sdiv(retained, assets); C = sdiv(ebit, assets)
    D = sdiv(mcap, tot_liab); E = sdiv(rev, assets)
    if None in (A, Bx, C, D, E):
        return calc(None, "Altman Z", {}, ["insufficient data"], "", "high")
    z = 1.2 * A + 1.4 * Bx + 3.3 * C + 0.6 * D + 1.0 * E
    return calc(round(z, 2), "1.2·(WC/TA) + 1.4·(RE/TA) + 3.3·(EBIT/TA) + 0.6·(Mcap/TL) + 1.0·(Sales/TA)",
        {"WC/TA": round(A, 3), "RE/TA": round(Bx, 3), "EBIT/TA": round(C, 3), "Mcap/TL": round(D, 3), "Sales/TA": round(E, 3)},
        ["> 2.99 safe · 1.81–2.99 grey · < 1.81 distress"], "", "high")


def _piotroski(inc, bal, cf, yrs):
    if len(yrs) < 2:
        return calc(None, "Piotroski F", {}, ["needs 2y"], "/9", "high")
    y, yp = yrs[-1], yrs[-2]
    I, Ip, B, Bp, F, Fp = inc[y], inc[yp], bal[y], bal[yp], cf[y], cf[yp]
    roa = sdiv(I["net_income"], B["total_assets"]); roa_p = sdiv(Ip["net_income"], Bp["total_assets"])
    signals = {
        "ROA>0": I["net_income"] > 0,
        "OCF>0": F["operating_cf"] > 0,
        "ROA improving": (roa or 0) > (roa_p or 0),
        "OCF>NI (accruals)": F["operating_cf"] > I["net_income"],
        "Lower leverage": sdiv(B["total_debt"], B["total_assets"]) < sdiv(Bp["total_debt"], Bp["total_assets"]),
        "Higher current ratio": sdiv(B["current_assets"], B["current_liabilities"]) > sdiv(Bp["current_assets"], Bp["current_liabilities"]),
        "No dilution": I["shares"] <= Ip["shares"] * 1.01,
        "Higher gross margin": sdiv(I["gross_profit"], I["revenue"]) > sdiv(Ip["gross_profit"], Ip["revenue"]),
        "Higher asset turnover": sdiv(I["revenue"], B["total_assets"]) > sdiv(Ip["revenue"], Bp["total_assets"]),
    }
    score = sum(1 for v in signals.values() if v)
    return calc(score, "Sum of 9 fundamental signals (0–9)", {k: bool(v) for k, v in signals.items()},
        ["8–9 strong · 0–2 weak"], "/9", "high")


# ---------------------------------------------------------------------------
# Price-based risk analytics
# ---------------------------------------------------------------------------
def _returns(closes):
    return [closes[i] / closes[i - 1] - 1 for i in range(1, len(closes))]


def risk_metrics(c: dict, bench: dict) -> dict:
    closes = c["prices"]["closes"]; bcl = bench["prices"]["closes"]
    n = min(len(closes), len(bcl))
    closes, bcl = closes[-n:], bcl[-n:]
    r, rb = _returns(closes), _returns(bcl)
    ann = 52.0
    tot_ret = closes[-1] / closes[0] - 1
    ann_ret = (1 + tot_ret) ** (ann / len(r)) - 1 if len(r) else None
    vol = st.pstdev(r) * math.sqrt(ann) if len(r) > 1 else None
    downside = [x for x in r if x < 0]
    dvol = st.pstdev(downside) * math.sqrt(ann) if len(downside) > 1 else None
    var_b = st.pvariance(rb) if len(rb) > 1 else None
    cov = sum((a - st.mean(r)) * (b - st.mean(rb)) for a, b in zip(r, rb)) / len(r) if len(r) else None
    beta = sdiv(cov, var_b)
    # max drawdown
    peak, mdd = closes[0], 0.0
    for p in closes:
        peak = max(peak, p)
        mdd = min(mdd, p / peak - 1)
    # 12m momentum (last 52 weeks, skip most recent 4)
    mom = closes[-5] / closes[-57] - 1 if len(closes) > 57 else (closes[-1] / closes[0] - 1)
    sharpe = sdiv((ann_ret - 0.03), vol) if (ann_ret is not None and vol) else None
    return {
        "total_return": calc(tot_ret, "P_end / P_start - 1 (5y)", {"P_start": closes[0], "P_end": closes[-1]}, [], "%", "high"),
        "ann_return": calc(ann_ret, "Annualised total return", {"periods_wk": len(r)}, [], "%", "high"),
        "ann_vol": calc(vol, "Std(weekly returns) x sqrt(52)", {"weeks": len(r)}, [], "%", "low"),
        "downside_vol": calc(dvol, "Std(negative weekly returns) x sqrt(52)", {}, [], "%", "low"),
        "beta": calc(beta, "Cov(stock, benchmark) / Var(benchmark)", {"benchmark": bench["ticker"]}, [], "", "low"),
        "max_drawdown": calc(mdd, "Max peak-to-trough decline", {}, [], "%", "high"),
        "momentum_12m": calc(mom, "12-month price return (skip last month)", {}, [], "%", "high"),
        "sharpe": calc(sharpe, "(Ann return - 3%) / Ann vol", {"rf": 0.03}, [], "x", "high"),
    }


def correlation_matrix(dataset: dict) -> dict:
    tickers = list(dataset["companies"].keys())
    series = {}
    minlen = min(len(dataset["companies"][t]["prices"]["closes"]) for t in tickers)
    for t in tickers:
        cl = dataset["companies"][t]["prices"]["closes"][-minlen:]
        series[t] = _returns(cl)
    mat = {}
    for a in tickers:
        mat[a] = {}
        for b in tickers:
            ra, rb = series[a], series[b]
            if len(ra) < 2:
                mat[a][b] = None; continue
            ma, mb = st.mean(ra), st.mean(rb)
            cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb)) / len(ra)
            sa, sb = st.pstdev(ra), st.pstdev(rb)
            mat[a][b] = round(cov / (sa * sb), 2) if sa and sb else None
    return mat


# ---------------------------------------------------------------------------
# Cross-sectional factor z-scores
# ---------------------------------------------------------------------------
def _zscores(values: dict):
    vals = [v for v in values.values() if v is not None]
    if len(vals) < 2:
        return {k: 0.0 for k in values}
    mu, sd = st.mean(vals), st.pstdev(vals)
    if sd == 0:
        return {k: 0.0 for k in values}
    return {k: ((v - mu) / sd if v is not None else None) for k, v in values.items()}


def factor_scores(metrics_by_ticker: dict, risk_by_ticker: dict) -> dict:
    tickers = list(metrics_by_ticker.keys())

    def col(getter):
        return {t: getter(t) for t in tickers}

    # Value: cheaper = higher score -> invert ev/ebitda & pe, use fcf_yield direct
    ev = _zscores(col(lambda t: metrics_by_ticker[t]["ev_ebitda"]["value"]))
    pe = _zscores(col(lambda t: metrics_by_ticker[t]["pe"]["value"]))
    fy = _zscores(col(lambda t: metrics_by_ticker[t]["fcf_yield"]["value"]))
    # Quality: roic, fcf_conversion, net_margin, low leverage
    roic = _zscores(col(lambda t: metrics_by_ticker[t]["roic"]["value"]))
    fcfc = _zscores(col(lambda t: metrics_by_ticker[t]["fcf_conversion"]["value"]))
    nm = _zscores(col(lambda t: metrics_by_ticker[t]["net_margin"]["value"]))
    lev = _zscores(col(lambda t: metrics_by_ticker[t]["net_debt_ebitda"]["value"]))
    # Growth
    rg = _zscores(col(lambda t: metrics_by_ticker[t]["revenue_cagr"]["value"]))
    eg = _zscores(col(lambda t: metrics_by_ticker[t]["eps_cagr"]["value"]))
    # Momentum
    mo = _zscores(col(lambda t: risk_by_ticker[t]["momentum_12m"]["value"]))

    def avg(*ds):
        out = {}
        for t in tickers:
            xs = [d[t] for d in ds if d.get(t) is not None]
            out[t] = round(sum(xs) / len(xs), 2) if xs else None
        return out

    value = avg({t: (-ev[t] if ev[t] is not None else None) for t in tickers},
                {t: (-pe[t] if pe[t] is not None else None) for t in tickers}, fy)
    quality = avg(roic, fcfc, nm, {t: (-lev[t] if lev[t] is not None else None) for t in tickers})
    growth = avg(rg, eg)
    momentum = mo
    composite = avg(value, quality, growth, momentum)
    return {t: {"value": value[t], "quality": quality[t], "growth": growth[t],
                "momentum": momentum[t], "composite": composite[t]} for t in tickers}


def transform_all(dataset: dict) -> dict:
    companies = dataset["companies"]
    metrics = {t: company_metrics(c) for t, c in companies.items()}
    risk = {t: risk_metrics(c, dataset["benchmark"]) for t, c in companies.items()}
    factors = factor_scores(metrics, risk)
    corr = correlation_matrix(dataset)
    return {"metrics": metrics, "risk": risk, "factors": factors, "correlation": corr,
            "mode": dataset.get("mode", "DEMO"), "retrieved": dataset.get("retrieved")}
