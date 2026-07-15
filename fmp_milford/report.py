"""
Self-contained interactive HTML report generator.

Produces ONE offline .html file (all CSS/JS/data inline, no external requests) with:
  - top navigation: Overview + one tab per role + Data & Performance + Methodology
  - global controls: company multi-select (grouped by sector) + range sliders that
    filter every table/chart (the "navigation slider / multi-company compare" spec)
  - company logos (monogram SVG fallback offline; real FMP logos when live+embedded)
  - every widget shows Source + Last-updated + DEMO/LIVE badge (provenance)
  - every computed figure opens an expandable panel with formula + inputs + steps
  - vanilla-JS SVG charts: scatter, bar, lines, correlation heatmap, sector heatmap
  - theme-aware (light/dark, with manual toggle), responsive
"""

from __future__ import annotations
import json
from datetime import datetime, timezone

from .config import UNIVERSE, SECTOR_COLORS, BENCHMARK
from .glossary import METRIC_GLOSSARY


def _logo_svg(ticker: str, color: str) -> str:
    txt = ticker[:4]
    fs = 13 if len(txt) <= 3 else 10
    return (f"<svg viewBox='0 0 40 40' width='34' height='34' xmlns='http://www.w3.org/2000/svg'>"
            f"<rect width='40' height='40' rx='9' fill='{color}'/>"
            f"<text x='20' y='25' font-size='{fs}' fill='#fff' text-anchor='middle' "
            f"font-family='ui-sans-serif,system-ui,sans-serif' font-weight='700'>{txt}</text></svg>")


def _build_blob(dataset, tr, insights, perf):
    companies = dataset["companies"]
    profiles = {t: {"name": c["name"], "sector": c["sector"], "industry": c["industry"],
                    "price": c["price"], "market_cap": c["market_cap"], "beta": c["beta"],
                    "currency": c["currency"]} for t, c in companies.items()}
    logos = {t: (companies[t].get("logo") or _logo_svg(t, SECTOR_COLORS.get(companies[t]["sector"], "#666")))
             for t in companies}
    return {
        "meta": {"mode": tr["mode"], "retrieved": tr["retrieved"],
                 "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                 "benchmark": BENCHMARK,
                 "universe_count": len(companies)},
        "universe": UNIVERSE,
        "sector_colors": SECTOR_COLORS,
        "profiles": profiles,
        "logos": logos,
        "metrics": tr["metrics"],
        "risk": tr["risk"],
        "factors": tr["factors"],
        "correlation": tr["correlation"],
        "insights": insights,
        "glossary": METRIC_GLOSSARY,
        "perf": perf or [],
    }


def render_html(dataset, tr, insights, perf=None) -> str:
    blob = _build_blob(dataset, tr, insights, perf)
    data_json = json.dumps(blob, ensure_ascii=False).replace("</", "<\\/")
    return HTML.replace("/*__DATA__*/", data_json)


def write_report(path, dataset, tr, insights, perf=None) -> str:
    html = render_html(dataset, tr, insights, perf)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


# ===========================================================================
# The single-file HTML/CSS/JS template. Data injected at /*__DATA__*/.
# ===========================================================================
HTML = r"""<!doctype html>
<html lang="en" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Milford · FMP Free-Tier Investment Intelligence</title>
<style>
:root{
  --bg:#f6f7f9; --panel:#ffffff; --ink:#1a1f27; --muted:#5b6673; --line:#e3e7ec;
  --accent:#2E86AB; --good:#1B998B; --bad:#d1495b; --warn:#E8871E; --chip:#eef2f6;
  --shadow:0 1px 3px rgba(20,30,50,.08),0 6px 20px rgba(20,30,50,.05);
}
:root[data-theme="dark"]{
  --bg:#0f141b; --panel:#161d27; --ink:#e8edf3; --muted:#9aa7b6; --line:#26303c;
  --accent:#4aa8d0; --good:#3fc4b0; --bad:#e0687a; --warn:#f0a828; --chip:#1e2732;
  --shadow:0 1px 3px rgba(0,0,0,.4),0 8px 26px rgba(0,0,0,.35);
}
@media (prefers-color-scheme:dark){
  :root[data-theme="auto"]{
    --bg:#0f141b; --panel:#161d27; --ink:#e8edf3; --muted:#9aa7b6; --line:#26303c;
    --accent:#4aa8d0; --good:#3fc4b0; --bad:#e0687a; --warn:#f0a828; --chip:#1e2732;
    --shadow:0 1px 3px rgba(0,0,0,.4),0 8px 26px rgba(0,0,0,.35);
  }
}
*{box-sizing:border-box}
body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  background:var(--bg);color:var(--ink);font-size:14px;line-height:1.5}
a{color:var(--accent)}
header{position:sticky;top:0;z-index:40;background:var(--panel);border-bottom:1px solid var(--line);
  box-shadow:var(--shadow)}
.hbar{display:flex;align-items:center;gap:14px;padding:12px 20px;flex-wrap:wrap}
.brand{font-weight:800;font-size:16px;letter-spacing:.2px}
.brand span{color:var(--accent)}
.badge{font-size:11px;font-weight:700;padding:3px 8px;border-radius:20px;background:var(--chip);color:var(--muted)}
.badge.demo{background:#E8871E22;color:var(--warn)}
.badge.live{background:#1B998B22;color:var(--good)}
.spacer{flex:1}
.tabs{display:flex;gap:4px;padding:0 12px 10px;flex-wrap:wrap}
.tab{padding:8px 14px;border-radius:9px;cursor:pointer;color:var(--muted);font-weight:600;white-space:nowrap}
.tab:hover{background:var(--chip)}
.tab.active{background:var(--accent);color:#fff}
.controls{background:var(--panel);border-bottom:1px solid var(--line);padding:12px 20px;
  display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start}
.ctl-title{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);margin-bottom:6px;font-weight:700}
.chips{display:flex;gap:6px;flex-wrap:wrap;max-width:640px}
.chip{font-size:11px;padding:4px 9px;border-radius:16px;background:var(--chip);cursor:pointer;
  border:1px solid transparent;user-select:none}
.chip.on{border-color:var(--accent);color:var(--accent);font-weight:700}
.chip.sector{font-weight:700}
.slider{display:flex;flex-direction:column;min-width:180px}
.slider input{width:180px}
.slider .val{font-variant-numeric:tabular-nums;color:var(--accent);font-weight:700}
main{padding:20px;max-width:1400px;margin:0 auto}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,520px),1fr));gap:18px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 16px 12px;
  box-shadow:var(--shadow);overflow:hidden}
.card.wide{grid-column:1/-1}
.card h3{margin:0 0 2px;font-size:15px}
.sub{color:var(--muted);font-size:12.5px;margin:0 0 10px}
.prov{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:11px;color:var(--muted);
  border-top:1px dashed var(--line);margin-top:10px;padding-top:8px}
.prov b{color:var(--ink);font-weight:600}
.notes{font-size:12.5px;color:var(--muted);margin-top:8px;background:var(--chip);border-radius:8px;padding:8px 10px}
details.explain{margin-top:8px;border:1px solid var(--line);border-radius:8px;overflow:hidden}
details.explain>summary{cursor:pointer;padding:8px 10px;font-size:12px;font-weight:700;color:var(--accent);
  background:var(--chip);list-style:none;user-select:none}
details.explain>summary::-webkit-details-marker{display:none}
details.explain>summary::before{content:"▸ ";}
details.explain[open]>summary::before{content:"▾ ";}
details.explain .exwrap{padding:10px 12px;font-size:12.5px;display:grid;gap:7px}
details.explain .exwrap b{color:var(--ink)}
details.explain .exwrap .lbl{display:inline-block;min-width:150px;color:var(--accent);font-weight:700}
.gloss{margin-top:12px;border-top:1px dashed var(--line);padding-top:10px;font-size:12.5px;display:grid;gap:6px}
.gloss .lbl{color:var(--accent);font-weight:700}
th .qm{color:var(--accent);font-weight:700;cursor:help;margin-left:2px}
.tbl-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th,td{padding:6px 8px;text-align:right;white-space:nowrap;border-bottom:1px solid var(--line)}
th:first-child,td:first-child{text-align:left;position:sticky;left:0;background:var(--panel)}
th{cursor:pointer;color:var(--muted);font-weight:700;user-select:none;position:sticky;top:0;background:var(--panel)}
th:hover{color:var(--ink)}
td.num{font-variant-numeric:tabular-nums;cursor:pointer}
td.num:hover{outline:1px solid var(--accent);outline-offset:-1px;border-radius:4px}
tr.med td{font-weight:700;background:var(--chip)}
.co{display:flex;align-items:center;gap:8px}
.co small{color:var(--muted)}
.flagchip{display:inline-block;font-size:10.5px;font-weight:700;padding:2px 7px;border-radius:12px;
  background:#d1495b22;color:var(--bad);margin:1px}
.para{margin:0 0 10px;padding-left:12px;border-left:3px solid var(--accent)}
.para .csrc{display:block;font-size:11px;color:var(--muted);margin-top:3px}
.legend{display:flex;gap:12px;flex-wrap:wrap;font-size:11px;color:var(--muted);margin-top:6px}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:4px;vertical-align:-1px}
.modal-bg{position:fixed;inset:0;background:rgba(10,14,20,.55);display:none;z-index:80;align-items:center;justify-content:center;padding:20px}
.modal-bg.show{display:flex}
.modal{background:var(--panel);border:1px solid var(--line);border-radius:14px;max-width:520px;width:100%;
  padding:18px 20px;box-shadow:var(--shadow);max-height:82vh;overflow:auto}
.modal h4{margin:0 0 2px;font-size:15px}
.modal .formula{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--chip);
  padding:8px 10px;border-radius:8px;font-size:12.5px;margin:10px 0}
.modal .kv{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:12.5px}
.modal .kv .k{color:var(--muted)}
.modal ol{margin:8px 0 0;padding-left:20px}
.modal .x{float:right;cursor:pointer;color:var(--muted);font-weight:700}
.svgwrap{width:100%;overflow-x:auto}
svg .ax{stroke:var(--line)} svg .axt{fill:var(--muted);font-size:10px}
svg .gl{stroke:var(--line);stroke-dasharray:2 3}
.hint{font-size:11px;color:var(--muted);margin-top:4px}
.kpis{display:flex;gap:14px;flex-wrap:wrap}
.kpi{background:var(--chip);border-radius:12px;padding:12px 14px;min-width:150px}
.kpi .n{font-size:22px;font-weight:800}
.kpi .l{font-size:11.5px;color:var(--muted)}
.toggle{cursor:pointer;padding:6px 10px;border-radius:8px;background:var(--chip);font-weight:700;font-size:12px}
</style>
</head>
<body>
<header>
  <div class="hbar">
    <div class="brand">Milford · <span>FMP</span> Free-Tier Intelligence</div>
    <span id="modeBadge" class="badge">…</span>
    <span class="badge" id="uniBadge">…</span>
    <div class="spacer"></div>
    <div class="toggle" id="themeBtn">◐ Theme</div>
  </div>
  <div class="tabs" id="tabs"></div>
</header>

<div class="controls">
  <div>
    <div class="ctl-title">Compare companies (click to toggle · sector headers toggle groups)</div>
    <div class="chips" id="coChips"></div>
  </div>
  <div class="slider">
    <div class="ctl-title">Min market cap ($bn)</div>
    <input id="mcapSlider" type="range" min="0" max="500" step="10" value="0">
    <div class="hint">≥ <span class="val" id="mcapVal">0</span> bn</div>
  </div>
  <div class="slider">
    <div class="ctl-title">Min composite z-score</div>
    <input id="compSlider" type="range" min="-3" max="3" step="0.25" value="-3">
    <div class="hint">≥ <span class="val" id="compVal">-3.00</span></div>
  </div>
  <div class="slider">
    <div class="ctl-title" id="selCountTitle">Selected</div>
    <div class="hint"><span class="val" id="selCount">0</span> names · <a href="#" id="selAll">all</a> · <a href="#" id="selNone">none</a></div>
  </div>
</div>

<main id="view"></main>
<div class="modal-bg" id="modalBg"><div class="modal" id="modal"></div></div>

<script>
const DATA = /*__DATA__*/;
const T2S = {}; Object.entries(DATA.universe).forEach(([s,ts])=>ts.forEach(t=>T2S[t]=s));
const ALL = Object.keys(DATA.profiles);
const ROLES = Object.keys(DATA.insights);
const state = {selected:new Set(ALL), minMcap:0, minComp:-3, tab:"Overview"};

// ---------- helpers ----------
function fmtNum(v,unit){
  if(v===null||v===undefined||Number.isNaN(v)) return "<span style='color:var(--muted)'>n/a</span>";
  if(unit==="%") return (v*100).toFixed(1)+"%";
  if(unit==="x") return v.toFixed(2)+"x";
  if(unit==="$") return "$"+v.toFixed(2);
  if(unit==="days") return v.toFixed(0)+"d";
  if(unit==="/9") return v.toFixed(0)+"/9";
  return (Math.abs(v)>=100? v.toFixed(0): v.toFixed(2));
}
function look(domain,t,key){
  if(domain==="factors"){const v=DATA.factors[t]?DATA.factors[t][key]:null; return {value:v,formula:"Cross-sectional factor z-score (equal-weight average of standardised signals)",inputs:{},steps:["Standardised across the 32-name universe"],unit:"",good:"high"};}
  const d = DATA[domain]||DATA.metrics; const o=d[t]?d[t][key]:null; return o||{value:null};
}
function activeTickers(){
  return ALL.filter(t=>state.selected.has(t)
    && (DATA.profiles[t].market_cap/1000)>=state.minMcap
    && ((DATA.factors[t] && DATA.factors[t].composite!=null? DATA.factors[t].composite: 99)>=state.minComp));
}
function pctRank(vals,v,good){
  const xs=vals.filter(x=>x!=null).sort((a,b)=>a-b); if(!xs.length||v==null) return null;
  let r=xs.filter(x=>x<=v).length/xs.length; return good==="low"? 1-r: r;
}
function shade(p){
  if(p==null) return "transparent";
  return `rgba(${Math.round(210-150*p)},${Math.round(90+120*p)},110,${(0.12+0.30*Math.abs(p-0.5)*2).toFixed(2)})`;
}
function el(tag,cls,html){const e=document.createElement(tag); if(cls)e.className=cls; if(html!=null)e.innerHTML=html; return e;}
function escAttr(s){return (s==null?"":String(s)).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;");}

// ---------- modal (calculation logic) ----------
function openCalc(c,label,source,metricKey){
  const m=document.getElementById("modal");
  let kv=""; for(const [k,v] of Object.entries(c.inputs||{})) kv+=`<div class="k">${k}</div><div>${typeof v==="number"? v.toLocaleString():v}</div>`;
  let steps=(c.steps||[]).map(s=>`<li>${s}</li>`).join("");
  const g = metricKey && DATA.glossary ? DATA.glossary[metricKey] : null;
  const gloss = g ? `<div class="gloss">
      <div><span class="lbl">What it means.</span> ${g.meaning}</div>
      <div><span class="lbl">What good looks like.</span> ${g.good}</div>
      <div><span class="lbl">What we're targeting.</span> ${g.target}</div>
      <div><span class="lbl">Alpha / what it trades.</span> ${g.alpha}</div></div>` : "";
  m.innerHTML=`<span class="x" onclick="closeModal()">✕</span>
    <h4>${label}</h4>
    <div class="sub">Value: <b>${fmtNum(c.value,c.unit)}</b></div>
    <div class="formula">${c.formula||""}</div>
    ${kv?`<div class="ctl-title">Inputs</div><div class="kv">${kv}</div>`:""}
    ${steps?`<div class="ctl-title" style="margin-top:10px">Calculation steps</div><ol>${steps}</ol>`:""}
    ${gloss}
    <div class="prov"><span>Source: <b>${source||""}</b></span></div>`;
  document.getElementById("modalBg").classList.add("show");
}
function closeModal(){document.getElementById("modalBg").classList.remove("show");}
document.getElementById("modalBg").addEventListener("click",e=>{if(e.target.id==="modalBg")closeModal();});

// ---------- provenance + card scaffold ----------
function provLine(ins){
  const badge = ins.mode==="DEMO"?'<span class="badge demo">DEMO DATA</span>':'<span class="badge live">LIVE</span>';
  return `<div class="prov">${badge}<span>Source: <b>${ins.source}</b></span><span>· Last updated: <b>${ins.last_updated||DATA.meta.retrieved}</b></span></div>`;
}
function card(ins,bodyNode){
  const wide=["metric_table","heatmap_matrix","lines","sector_heatmap","flag_table","perf_table"].includes(ins.widget);
  const c=el("div","card"+(wide?" wide":""));
  c.appendChild(el("h3",null,ins.title));
  c.appendChild(el("p","sub",ins.subtitle||""));
  c.appendChild(bodyNode);
  if(ins.notes) c.appendChild(el("div","notes","<b>How to use:</b> "+ins.notes));
  c.insertAdjacentHTML("beforeend",explainerHtml(ins));
  c.insertAdjacentHTML("beforeend",provLine(ins));
  return c;
}
function explainerHtml(ins){
  const e=ins.explainer; if(!e) return "";
  return `<details class="explain"><summary>What this means &amp; how it earns alpha</summary><div class="exwrap">
    <div><span class="lbl">Intent</span> ${e.intent}</div>
    <div><span class="lbl">What good looks like</span> ${e.good}</div>
    <div><span class="lbl">What we're targeting</span> ${e.target}</div>
    <div><span class="lbl">Alpha / what it trades</span> ${e.alpha}</div>
  </div></details>`;
}
function coCell(t){
  const p=DATA.profiles[t];
  return `<div class="co">${DATA.logos[t]}<div><div>${t}</div><small>${p.name}</small></div></div>`;
}

// ---------- renderers ----------
function metricTable(ins){
  const P=ins.payload, cols=P.columns, dom=P.source_domain;
  let rows=activeTickers();
  if(P.filter){ rows=rows.filter(t=>Object.entries(P.filter).every(([k,mn])=>{const v=look(dom,t,k).value; return v!=null && v>=mn;})); }
  const colVals={}; cols.forEach(col=>colVals[col.key]=rows.map(t=>look(dom,t,col.key).value));
  let sortKey=P.sort_by||cols[0].key, sortDir=P.sort_dir||"desc";
  const wrap=el("div","tbl-wrap"); const tbl=el("table");
  function draw(){
    rows.sort((a,b)=>{const va=look(dom,a,sortKey).value, vb=look(dom,b,sortKey).value;
      if(va==null)return 1; if(vb==null)return -1; return sortDir==="asc"? va-vb: vb-va;});
    let h="<thead><tr><th>Company</th>"+cols.map(c=>{
      const g=(DATA.glossary&&DATA.glossary[c.key])||null;
      const tip=g?`${g.label}: ${g.meaning}  ·  Good: ${g.good}`:c.label;
      const qm=g?`<span class="qm" title="${escAttr(tip)}">?</span>`:"";
      return `<th data-k="${c.key}" title="${escAttr(tip)}">${c.label}${sortKey===c.key?(sortDir==="asc"?" ▲":" ▼"):""}${qm}</th>`;
    }).join("")+"</tr></thead>";
    let body="";
    rows.forEach(t=>{
      body+="<tr><td>"+coCell(t)+"</td>";
      cols.forEach(c=>{
        const o=look(dom,t,c.key); const p=(P.shade_pct)?pctRank(colVals[c.key],o.value,c.good):null;
        const bg=P.shade_pct?`style="background:${shade(p)}"`:"";
        body+=`<td class="num" ${bg} data-t="${t}" data-k="${c.key}">${fmtNum(o.value,c.unit)}</td>`;
      });
      body+="</tr>";
    });
    if(P.sector_median){
      let mr='<tr class="med"><td>▸ Universe median</td>';
      cols.forEach(c=>{const xs=colVals[c.key].filter(x=>x!=null).sort((a,b)=>a-b);
        const md=xs.length?xs[Math.floor(xs.length/2)]:null; mr+=`<td class="num">${fmtNum(md,c.unit)}</td>`;});
      body+=mr+"</tr>";
    }
    tbl.innerHTML=h+"<tbody>"+body+"</tbody>";
    tbl.querySelectorAll("th[data-k]").forEach(th=>th.onclick=()=>{const k=th.dataset.k;
      if(sortKey===k)sortDir=sortDir==="asc"?"desc":"asc"; else{sortKey=k;sortDir="desc";} draw();});
    tbl.querySelectorAll("td.num").forEach(td=>td.onclick=()=>{const o=look(dom,td.dataset.t,td.dataset.k);
      const col=cols.find(c=>c.key===td.dataset.k); openCalc(o,`${td.dataset.t} · ${col.label}`,ins.source,td.dataset.k);});
  }
  draw(); wrap.appendChild(tbl); return wrap;
}

function fmtN(v){return v==null?"n/a":(Math.abs(v)>=100?v.toFixed(0):v.toFixed(2));}
function sectorLegend(){return Object.entries(DATA.sector_colors).map(([s,c])=>`<span><span class="dot" style="background:${c}"></span>${s}</span>`).join("");}

function scatter(ins){
  const P=ins.payload, dom=P.source_domain||"metrics"; const ts=activeTickers();
  const W=720, H=380, m={l:52,r:20,t:16,b:40};
  const xs=ts.map(t=>look(dom,t,P.x_key).value), ys=ts.map(t=>look(dom,t,P.y_key).value);
  const xv=xs.filter(v=>v!=null), yv=ys.filter(v=>v!=null);
  const xmin=Math.min(...xv),xmax=Math.max(...xv),ymin=Math.min(...yv),ymax=Math.max(...yv);
  const sizes=ts.map(t=>DATA.profiles[t].market_cap), smax=Math.max(...sizes);
  const sx=v=>m.l+(v-xmin)/((xmax-xmin)||1)*(W-m.l-m.r);
  const sy=v=>H-m.b-(v-ymin)/((ymax-ymin)||1)*(H-m.t-m.b);
  let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" preserveAspectRatio="xMidYMid meet">`;
  for(let i=0;i<=4;i++){const gy=m.t+i/4*(H-m.t-m.b); s+=`<line class="gl" x1="${m.l}" y1="${gy}" x2="${W-m.r}" y2="${gy}"/>`;}
  s+=`<line class="ax" x1="${m.l}" y1="${H-m.b}" x2="${W-m.r}" y2="${H-m.b}"/><line class="ax" x1="${m.l}" y1="${m.t}" x2="${m.l}" y2="${H-m.b}"/>`;
  ts.forEach((t,i)=>{ if(xs[i]==null||ys[i]==null)return;
    const r=6+Math.sqrt(sizes[i]/smax)*20, col=DATA.sector_colors[DATA.profiles[t].sector]||"#888";
    s+=`<circle cx="${sx(xs[i]).toFixed(1)}" cy="${sy(ys[i]).toFixed(1)}" r="${r.toFixed(1)}" fill="${col}" fill-opacity="0.55" stroke="${col}"><title>${t} · ${P.x_label}: ${fmtN(xs[i])} · ${P.y_label}: ${(ys[i]*100).toFixed(1)}%</title></circle>`;
    s+=`<text x="${sx(xs[i]).toFixed(1)}" y="${(sy(ys[i])-r-2).toFixed(1)}" text-anchor="middle" class="axt" font-weight="700">${t}</text>`;});
  s+=`<text x="${(W/2)}" y="${H-6}" text-anchor="middle" class="axt">${P.x_label}</text>`;
  s+=`<text transform="translate(12,${H/2}) rotate(-90)" text-anchor="middle" class="axt">${P.y_label}</text></svg>`;
  const box=el("div"); box.appendChild(el("div","svgwrap",s)); box.appendChild(el("div","legend",sectorLegend())); return box;
}

function bar(ins){
  const P=ins.payload,dom=P.source_domain||"metrics"; let ts=activeTickers();
  ts=ts.filter(t=>look(dom,t,P.key).value!=null).sort((a,b)=>look(dom,b,P.key).value-look(dom,a,P.key).value);
  const max=Math.max(...ts.map(t=>look(dom,t,P.key).value),0.0001);
  let rows=ts.map(t=>{const v=look(dom,t,P.key).value,col=DATA.sector_colors[DATA.profiles[t].sector];
    return `<div style="display:flex;align-items:center;gap:8px;margin:3px 0"><div style="width:52px;font-weight:700">${t}</div>
      <div style="flex:1;background:var(--chip);border-radius:6px"><div style="width:${(v/max*100).toFixed(1)}%;background:${col};height:16px;border-radius:6px"></div></div>
      <div style="width:60px;text-align:right;font-variant-numeric:tabular-nums">${(v*100).toFixed(1)}%</div></div>`;}).join("");
  return el("div",null,rows||"<div class='notes'>No selected names.</div>");
}

function sectorHeatmap(ins){
  const P=ins.payload,cols=P.columns,data=P.data,secs=Object.keys(data);
  const colVals={}; cols.forEach(c=>colVals[c.key]=secs.map(s=>data[s][c.key]));
  const wrap=el("div","tbl-wrap"),tbl=el("table");
  let h="<thead><tr><th>Theme</th>"+cols.map(c=>`<th>${c.label}</th>`).join("")+"</tr></thead><tbody>";
  secs.forEach(s=>{h+=`<tr><td><span class="dot" style="background:${DATA.sector_colors[s]}"></span>${s}</td>`;
    cols.forEach(c=>{const v=data[s][c.key],p=pctRank(colVals[c.key],v,c.good);
      const unit=(["ev_ebitda","net_debt_ebitda"].includes(c.key))?"x":"%";
      h+=`<td class="num" style="background:${shade(p)}">${fmtNum(v,unit)}</td>`;});h+="</tr>";});
  tbl.innerHTML=h+"</tbody>"; wrap.appendChild(tbl); return wrap;
}

function flagTable(ins){
  const rows=ins.payload.rows;
  if(!rows.length) return el("div","notes","No names currently trip any risk flag.");
  const wrap=el("div","tbl-wrap"),tbl=el("table");
  let h="<thead><tr><th>Company</th><th style='text-align:left'>Theme</th><th style='text-align:left'>Flags</th></tr></thead><tbody>";
  rows.forEach(r=>{h+=`<tr><td>${coCell(r.ticker)}</td><td style='text-align:left'>${r.sector}</td>
    <td style='text-align:left'>${r.flags.map(f=>`<span class="flagchip">${f}</span>`).join("")}</td></tr>`;});
  tbl.innerHTML=h+"</tbody>"; wrap.appendChild(tbl); return wrap;
}

function dupont(ins){
  const data=ins.payload.data; const ts=activeTickers().filter(t=>data[t]&&data[t].roe!=null);
  const box=el("div");
  if(!ts.length){box.appendChild(el("div","notes","No selected names with ROE."));return box;}
  const pick=el("select"); pick.style.cssText="margin-bottom:10px;padding:6px;border-radius:8px;background:var(--chip);color:var(--ink);border:1px solid var(--line)";
  ts.forEach(t=>pick.appendChild(el("option",null,`${t} — ${DATA.profiles[t].name}`)));
  const chart=el("div"); box.appendChild(pick); box.appendChild(chart);
  function med(key){const xs=ts.map(t=>data[t][key]).filter(x=>x!=null).sort((a,b)=>a-b);return xs.length?xs[Math.floor(xs.length/2)]:null;}
  function draw(){const t=(pick.value||"").split(" — ")[0]||ts[0]; const d=data[t];
    const parts=[["Net margin",d.net_margin,med("net_margin"),"%"],["Asset turnover",d.asset_turnover,med("asset_turnover"),"x"],
      ["Equity multiplier",d.equity_multiplier,med("equity_multiplier"),"x"],["= ROE",d.roe,med("roe"),"%"]];
    chart.innerHTML=parts.map(([l,v,mv,u])=>{const disp=v==null?"n/a":(u==="%"?(v*100).toFixed(1)+"%":v.toFixed(2)+"x");
      const mdisp=mv==null?"n/a":(u==="%"?(mv*100).toFixed(1)+"%":mv.toFixed(2)+"x");
      const w=Math.min(100,Math.abs((u==="%"?v*100:v*20))||0);
      return `<div style="margin:6px 0"><div style="display:flex;justify-content:space-between"><b>${l}</b><span>${disp} <small style="color:var(--muted)">(peer med ${mdisp})</small></span></div>
        <div style="background:var(--chip);border-radius:6px"><div style="width:${w}%;height:12px;border-radius:6px;background:${l.includes('ROE')?'var(--accent)':'var(--good)'}"></div></div></div>`;}).join("");
  }
  pick.onchange=draw; draw(); return box;
}

function lines(ins){
  const S=ins.payload.series; const box=el("div");
  const isPerf = S[Object.keys(S)[0]] && S[Object.keys(S)[0]].cum!==undefined;
  let linesMode="cum";
  let keys=Object.keys(S).filter(k=>activeTickers().includes(k) || (isPerf && k===DATA.meta.benchmark));
  if(isPerf){const toggle=el("div","legend",`<span class="toggle" id="lm_cum">Growth of $100</span> <span class="toggle" id="lm_dd">Drawdown</span>`);box.appendChild(toggle);}
  const chart=el("div","svgwrap"); box.appendChild(chart);
  const W=760,H=340,m={l:46,r:40,t:14,b:26};
  function series(k){return isPerf? (linesMode==="dd"?S[k].dd:S[k].cum) : S[k].y;}
  function draw(){
    const sel=keys.slice(0,10);
    if(!sel.length){chart.innerHTML="<div class='notes'>No selected names.</div>";return;}
    let allv=[]; sel.forEach(k=>series(k).forEach(v=>{if(v!=null)allv.push(v);}));
    const ymin=Math.min(...allv),ymax=Math.max(...allv);
    const n=Math.max(...sel.map(k=>series(k).length));
    const sx=i=>m.l+i/((n-1)||1)*(W-m.l-m.r), sy=v=>H-m.b-(v-ymin)/((ymax-ymin)||1)*(H-m.t-m.b);
    let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" preserveAspectRatio="xMidYMid meet">`;
    for(let i=0;i<=4;i++){const gy=m.t+i/4*(H-m.t-m.b),vv=ymax-(ymax-ymin)*i/4;
      s+=`<line class="gl" x1="${m.l}" y1="${gy}" x2="${W-m.r}" y2="${gy}"/><text x="4" y="${gy+3}" class="axt">${isPerf&&linesMode==="dd"?vv.toFixed(0)+"%":vv.toFixed(0)}</text>`;}
    sel.forEach(k=>{const col=k===DATA.meta.benchmark?"#888":(DATA.sector_colors[(S[k].sector)]||"#4aa8d0");
      const ys=series(k); let d=""; ys.forEach((v,i)=>{if(v==null)return; d+=(d?"L":"M")+sx(i).toFixed(1)+" "+sy(v).toFixed(1)+" ";});
      s+=`<path d="${d}" fill="none" stroke="${col}" stroke-width="${k===DATA.meta.benchmark?2.4:1.6}" ${k===DATA.meta.benchmark?'stroke-dasharray="5 3"':''}/>`;
      const li=ys.length-1; if(ys[li]!=null) s+=`<text x="${(sx(li)+3).toFixed(1)}" y="${(sy(ys[li])+3).toFixed(1)}" class="axt" font-weight="700" fill="${col}">${k}</text>`;});
    s+="</svg>"; chart.innerHTML=s;
  }
  draw();
  if(isPerf){box.querySelector("#lm_cum").onclick=()=>{linesMode="cum";draw();};box.querySelector("#lm_dd").onclick=()=>{linesMode="dd";draw();};}
  box.appendChild(el("div","hint",isPerf?"Dashed = "+DATA.meta.benchmark+" benchmark · up to 10 selected names":"Values = FCF ÷ Net income by fiscal year · up to 10 selected names"));
  return box;
}

function heatmapMatrix(ins){
  const M=ins.payload.matrix; const ts=activeTickers();
  const wrap=el("div","tbl-wrap"),tbl=el("table"); tbl.style.fontSize="10.5px";
  let h="<thead><tr><th></th>"+ts.map(t=>`<th style="text-align:center">${t}</th>`).join("")+"</tr></thead><tbody>";
  ts.forEach(a=>{h+=`<tr><td>${a}</td>`;ts.forEach(b=>{const v=(M[a]?M[a][b]:null);
    const g=v==null?0:(v+1)/2; const bg=v==null?"transparent":`rgba(${Math.round(220-140*g)},${Math.round(80+120*g)},120,${(0.15+0.5*Math.abs(v)).toFixed(2)})`;
    h+=`<td class="num" style="background:${bg};text-align:center" title="${a}/${b}: ${v}">${v==null?"":v.toFixed(2)}</td>`;});h+="</tr>";});
  tbl.innerHTML=h+"</tbody>"; wrap.appendChild(tbl);
  const box=el("div"); box.appendChild(wrap);
  box.appendChild(el("div","hint","Green = positively correlated · red = low/negative. Read for pairs (signals) and diversification (construction)."));
  return box;
}

function commentary(ins){
  const box=el("div");
  ins.payload.paragraphs.forEach(p=>box.appendChild(el("div","para",`${p.text}<span class="csrc">Source: ${p.source}</span>`)));
  return box;
}

function perfTable(ins){
  const box=el("div");
  if(!DATA.perf||!DATA.perf.length){
    box.appendChild(el("div","notes","No live performance data in DEMO mode. Run <b>python run.py --live</b> with FMP_API_KEY on a network-open machine to record real per-endpoint latency, payload size and HTTP status here. perf.py times every call, so you can see exactly how fast the free tier responds and how many companies fit inside 250 calls/day."));
    return box;
  }
  const wrap=el("div","tbl-wrap"),tbl=el("table");
  let h="<thead><tr><th style='text-align:left'>Endpoint</th><th>HTTP</th><th>Latency (ms)</th><th>Bytes</th><th>OK</th></tr></thead><tbody>";
  DATA.perf.forEach(r=>{h+=`<tr><td style='text-align:left'>${r.endpoint}</td><td class="num">${r.status}</td><td class="num">${r.latency_ms}</td><td class="num">${(r.bytes||0).toLocaleString()}</td><td class="num">${r.ok?"✓":"✗"}</td></tr>`;});
  tbl.innerHTML=h+"</tbody>"; wrap.appendChild(tbl); box.appendChild(wrap); return box;
}

const RENDER={metric_table:metricTable,scatter:scatter,bar:bar,sector_heatmap:sectorHeatmap,
  flag_table:flagTable,dupont:dupont,lines:lines,heatmap_matrix:heatmapMatrix,commentary:commentary,perf_table:perfTable};
function renderInsight(ins){
  let body; try{ body=RENDER[ins.widget](ins); }catch(e){ body=el("div","notes","Render note: "+e.message); }
  return card(ins,body);
}

// ---------- overview + methodology ----------
function overview(){
  const wrap=el("div");
  const k=el("div","card wide");
  k.innerHTML=`<h3>What this is</h3><p class="sub">FMP <b>free tier</b> is US-listed only, EOD, ~5y history, 250 calls/day.
    None of Milford's home exchanges (NZX/ASX/LSE/HKEX/SGX/KRX/TWSE) are reachable here — so this portal uses FMP as a
    <b>US-listed comparables + fundamental-modelling sandbox</b>. Universe: 32 US names across your four themes.</p>`;
  const flags=DATA.insights["Head of Investment"].find(i=>i.id==="hoi_risk_register").payload.rows.length;
  const kp=el("div","kpis");
  kp.innerHTML=`
    <div class="kpi"><div class="n">${DATA.meta.universe_count}</div><div class="l">Companies · 4 themes</div></div>
    <div class="kpi"><div class="n">${ROLES.length}</div><div class="l">Role dashboards</div></div>
    <div class="kpi"><div class="n">${flags}</div><div class="l">Names on risk register</div></div>
    <div class="kpi"><div class="n">${DATA.meta.mode}</div><div class="l">Data mode</div></div>`;
  k.appendChild(kp); wrap.appendChild(k);
  const g=el("div","grid");
  g.appendChild(renderInsight(DATA.insights["Head of Investment"].find(i=>i.id==="hoi_sector_heat")));
  g.appendChild(renderInsight(DATA.insights["Portfolio Manager"].find(i=>i.id==="pm_quality_val")));
  wrap.appendChild(g); return wrap;
}
function methodology(){
  const c=el("div","card wide");
  c.innerHTML=`<h3>Methodology, provenance & upgrade path</h3>
   <div class="notes"><b>Free-tier reality:</b> US-listed only · EOD prices · ~5y annual statements · 250 API calls/day · 500MB/30d.
   To cover Milford's actual book: <b>Premium</b> adds LSE + 30y history + intraday; <b>Ultimate</b> adds ASX/NZX/HKEX/SGX/KRX/TWSE + earnings transcripts + 13F + bulk.</div>
   <p class="sub" style="margin-top:10px"><b>Every metric</b> is computed by us from the statements (not ingested) so the logic is transparent and consistent across names —
   click any number to see its formula, inputs and steps. <b>Every widget</b> shows its source endpoints and last-updated time.</p>
   <p class="sub"><b>Data mode:</b> ${DATA.meta.mode==="DEMO"?"synthetic demo data (this environment blocks FMP egress). Run <b>python run.py --live</b> with FMP_API_KEY on a network-open machine to populate real data + real API latency — identical layout.":"live FMP data."}</p>
   <div class="tbl-wrap"><table><thead><tr><th style="text-align:left">Metric family</th><th style="text-align:left">Examples</th><th style="text-align:left">FMP endpoints</th></tr></thead><tbody>
   <tr><td style="text-align:left">Profitability</td><td style="text-align:left">ROIC, ROE, margins</td><td style="text-align:left">income + balance-sheet</td></tr>
   <tr><td style="text-align:left">Cash quality</td><td style="text-align:left">FCF conversion, OCF/EBITDA</td><td style="text-align:left">cash-flow + income</td></tr>
   <tr><td style="text-align:left">Valuation</td><td style="text-align:left">P/E, EV/EBITDA, FCF yield</td><td style="text-align:left">profile + statements</td></tr>
   <tr><td style="text-align:left">Quality scores</td><td style="text-align:left">Altman Z, Piotroski F</td><td style="text-align:left">statements (+financial-scores cross-check)</td></tr>
   <tr><td style="text-align:left">Risk</td><td style="text-align:left">vol, beta, drawdown, Sharpe</td><td style="text-align:left">historical-price-eod</td></tr>
   </tbody></table></div>`;
  return c;
}

// ---------- shell ----------
function renderTabs(){
  const t=document.getElementById("tabs"); t.innerHTML="";
  ["Overview",...ROLES,"Data & Performance","Methodology"].forEach(name=>{
    const d=el("div","tab"+(state.tab===name?" active":""),name); d.onclick=()=>{state.tab=name;renderTabs();renderView();};
    t.appendChild(d);});
}
function renderView(){
  const v=document.getElementById("view"); v.innerHTML="";
  if(state.tab==="Overview"){v.appendChild(overview());return;}
  if(state.tab==="Methodology"){v.appendChild(methodology());return;}
  if(state.tab==="Data & Performance"){
    const g=el("div","grid");
    g.appendChild(renderInsight(DATA.insights["Quantitative Analyst"].find(i=>i.id==="qa_perf")));
    g.appendChild(methodology()); v.appendChild(g); return;}
  const g=el("div","grid");
  DATA.insights[state.tab].forEach(ins=>g.appendChild(renderInsight(ins)));
  v.appendChild(g);
}
function renderControls(){
  const c=document.getElementById("coChips"); c.innerHTML="";
  Object.entries(DATA.universe).forEach(([s,ts])=>{
    const sc=el("span","chip sector on",s.replace(" & ","&")); sc.style.background=DATA.sector_colors[s]+"22";
    sc.onclick=()=>{const anyOff=ts.some(t=>!state.selected.has(t)); ts.forEach(t=>anyOff?state.selected.add(t):state.selected.delete(t)); syncChips();renderView();};
    c.appendChild(sc);
    ts.forEach(t=>{const ch=el("span","chip"+(state.selected.has(t)?" on":""),t); ch.dataset.t=t;
      ch.onclick=()=>{state.selected.has(t)?state.selected.delete(t):state.selected.add(t);syncChips();renderView();}; c.appendChild(ch);});
  });
  updateSel();
}
function syncChips(){document.querySelectorAll("#coChips .chip[data-t]").forEach(ch=>ch.classList.toggle("on",state.selected.has(ch.dataset.t)));updateSel();}
function updateSel(){document.getElementById("selCount").textContent=activeTickers().length;}
function bindControls(){
  const ms=document.getElementById("mcapSlider"),cs=document.getElementById("compSlider");
  ms.oninput=()=>{state.minMcap=+ms.value;document.getElementById("mcapVal").textContent=ms.value;syncChips();renderView();};
  cs.oninput=()=>{state.minComp=+cs.value;document.getElementById("compVal").textContent=(+cs.value).toFixed(2);syncChips();renderView();};
  document.getElementById("selAll").onclick=e=>{e.preventDefault();ALL.forEach(t=>state.selected.add(t));syncChips();renderView();};
  document.getElementById("selNone").onclick=e=>{e.preventDefault();state.selected.clear();syncChips();renderView();};
  document.getElementById("themeBtn").onclick=()=>{const r=document.documentElement;
    r.dataset.theme=r.dataset.theme==="dark"?"light":(r.dataset.theme==="light"?"auto":"dark");};
}

// ---------- init ----------
(function init(){
  const mb=document.getElementById("modeBadge");
  mb.textContent=DATA.meta.mode==="DEMO"?"DEMO DATA":"LIVE";
  mb.className="badge "+(DATA.meta.mode==="DEMO"?"demo":"live");
  document.getElementById("uniBadge").textContent=DATA.meta.universe_count+" US names · generated "+DATA.meta.generated;
  renderTabs(); renderControls(); bindControls(); renderView();
})();
</script>
</body>
</html>"""
