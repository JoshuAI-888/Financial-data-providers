#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the published pages from the research notes and requirement scores.

    python3 provider-landscape/tools/build_pages.py           # rebuild all pages
    python3 provider-landscape/tools/build_pages.py --check   # exit 1 if any page is stale

Source of truth (see REFRESH.md):

    idp-research/<vendor>.md        fact-sheets: narrative, snapshot fields, hard-gate reads,
                                    "Recent developments" line, dated + typed sources
    idp-research/reqscores_*.json   requirement-level scores (0-5, evidence-capped)
    idp-research/vendors.json       vendor order, segment, strategic-risk penalties, as-of dates
    idp-research/alignment_v3_1.json  v3.1 shortlist check: scope, gates A01-A14, domains/weights,
                                    ratings (weighted scores are computed here), use cases, concerns

        |  this script
        v

    provider-landscape/idp_evaluation.html                 (canonical copy; JSON blocks rewritten)
    idp_evaluation.html                                    (root copy, script path prefixed)
    provider-landscape/financial_data_providers_landscape.html  (canonical copy)
    financial_data_providers_landscape.html, index.html    (root copies)

Domain scores are never typed by hand: each is the mean of that domain's four requirement
scores, rounded to the nearest 0.5. Stdlib only.
"""
import argparse, glob, html, io, json, os, re, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
PL = os.path.dirname(HERE)                  # provider-landscape/
ROOT = os.path.dirname(PL)                  # repo root
RES = os.path.join(PL, "idp-research")

GATE_RE = re.compile(r"^-\s*G(\d{2})\b.*?:\s*\**\s*(PASS|FAIL|PARTIAL|UNKNOWN)\b", re.I)
URL_RE = re.compile(r"https?://[^\s\]<>\"'`]+")
TAG_RE = re.compile(r"\[(vendor|independent)\s*·\s*([^·\]]+?)\s*·\s*([^·\]]+?)\s*·\s*(opened|search-only)\s*\]\s*$", re.I)
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def human_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d %s %d" % (d, MONTHS[m - 1], y)


# ---------------------------------------------------------------- markdown -> html
def inline(s):
    s = html.escape(s, quote=True)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    return s


def render_blocks(lines):
    """Paragraphs and '-' bullet lists, the only constructs the fact-sheets use."""
    out, ul = [], False
    for ln in lines:
        if not ln.strip():
            continue
        if re.match(r"^\s*-\s+", ln):
            if not ul:
                out.append('<ul class="clean">')
                ul = True
            out.append("<li>%s</li>" % inline(re.sub(r"^\s*-\s+", "", ln).strip()))
        else:
            if ul:
                out.append("</ul>")
                ul = False
            out.append("<p class='fs-line'>%s</p>" % inline(ln.strip()))
    if ul:
        out.append("</ul>")
    return "\n".join(out)


def split_sections(md):
    """-> title, [(number, heading, [lines])]"""
    title, secs, cur = "", [], None
    for ln in md.splitlines():
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif ln.startswith("## "):
            m = re.match(r"##\s+(\d+)\.\s*(.*)", ln)
            cur = (int(m.group(1)) if m else 0, (m.group(2) if m else ln[3:]).strip(), [])
            secs.append(cur)
        elif cur is not None:
            cur[2].append(ln)
    return title, secs


# ---------------------------------------------------------------- fact-sheet parsing
def snapshot_field(lines, label):
    for ln in lines:
        m = re.match(r"^\s*-\s+\*\*%s:\*\*\s*(.*)$" % re.escape(label), ln)
        if m:
            return m.group(1).strip()
    return ""


def plain(s):
    return re.sub(r"\*\*?(.+?)\*\*?", r"\1", s)


def clip(s, n):
    s = plain(s)
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0].rstrip(",;:—– ")
    return cut + "…"


def parse_source(ln):
    m = URL_RE.search(ln)
    if not m:
        return None
    url = m.group(0).rstrip(".,;")
    while url.endswith(")") and url.count(")") > url.count("("):  # keep balanced parens, e.g. wiki/Aladdin_(BlackRock)
        url = url[:-1].rstrip(".,;")
    rest = ln.strip()[1:].strip()
    src = {"u": url}
    tm = TAG_RE.search(rest)
    if tm:
        side, typ, when, how = (g.strip() for g in tm.groups())
        src.update(ev=typ, evc="vendor" if side.lower() == "vendor" else "indep",
                   side=side.lower(), date=when, how=how.lower())
        rest = rest[:tm.start()].strip()
    acc = re.search(r"\(accessed ([0-9-]+)\)", rest)
    if acc:
        src["accessed"] = acc.group(1)
        rest = rest.replace(acc.group(0), "")
    t = rest.replace(url, "").strip()
    t = re.sub(r"^[\s—–:|-]+|[\s—–:|-]+$", "", t)
    src["t"] = t or url
    return src


def parse_factsheet(path):
    md = read(path)
    title, secs = split_sections(md)
    by_num = {n: (h, ls) for n, h, ls in secs}
    snap = by_num.get(1, ("", []))[1]
    gates = {}
    for n, h, ls in secs:
        if n == 10:
            for ln in ls:
                g = GATE_RE.match(ln.strip())
                if g:
                    gates[int(g.group(1))] = g.group(2).lower()
    sources = []
    for ln in by_num.get(11, ("", []))[1]:
        if ln.strip().startswith("-"):
            s = parse_source(ln)
            if s:
                sources.append(s)
    return {"title": title, "secs": secs, "snap": snap, "gates": gates, "sources": sources}


def vendor_html(fs, dom_scores, domain_names):
    parts = []
    for n, h, ls in fs["secs"]:
        if n == 11 or n == 0:
            continue
        label = re.sub(r"\s+—\s+.*$", "", h)            # drop "— PREVIEW" style suffixes
        if n == 10:
            ls = list(ls)
        parts.append('<div class="sec-label">%s</div>%s' % (html.escape(label, quote=False), render_blocks(ls)))
        if n == 10:
            items = "".join("<li>%s: %.1f</li>" % (html.escape(domain_names[i]), s) for i, s in enumerate(dom_scores))
            parts.append("<p class='fs-line'><b>Domain scores (computed from requirement scores — mean of four "
                         "requirements, nearest 0.5; provisional until a proof of value runs):</b></p>"
                         '<ul class="clean">%s</ul>' % items)
    return "".join(parts)


# ---------------------------------------------------------------- scores
def load_reqscores():
    cat, scores = {}, {}
    for f in sorted(glob.glob(os.path.join(RES, "reqscores*.json"))):
        j = json.loads(read(f))
        for rid, desc in j["requirements"].items():
            cat.setdefault(rid, desc)
        for rid, vs in j["scores"].items():
            for vid, s in vs.items():
                if vid in scores.setdefault(rid, {}):
                    raise SystemExit("duplicate score %s/%s in %s" % (rid, vid, f))
                scores[rid][vid] = s
    return cat, scores


def validate_score(rid, vid, s):
    caps = {"roadmap": 1.0, "sales": 2.0, "docs": 3.0, "demo": 3.5, "named-customer": 4.0, "sla": 4.5, "pov": 5.0, "none": 1.5}
    for k in ("s", "ev", "rel", "cite", "url", "type", "note"):
        if k not in s:
            raise SystemExit("%s/%s missing %s" % (rid, vid, k))
    if (s["s"] * 2) != int(s["s"] * 2) or not 0 <= s["s"] <= 5:
        raise SystemExit("%s/%s score %r not a 0.5 step in 0-5" % (rid, vid, s["s"]))
    cap = caps.get(s["ev"])
    if cap is not None and s["s"] > cap:
        raise SystemExit("%s/%s score %.1f exceeds the %s evidence cap %.1f" % (rid, vid, s["s"], s["ev"], cap))


# ---------------------------------------------------------------- page assembly
def replace_json_block(page, block_id, obj):
    pat = re.compile(r'(<script id="%s" type="application/json">)(.*?)(</script>)' % re.escape(block_id), re.S)
    if not pat.search(page):
        raise SystemExit("block %s not found" % block_id)
    payload = json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")
    return pat.sub(lambda m: m.group(1) + payload + m.group(3), page, count=1)


def replace_marked(page, name, content):
    pat = re.compile(r"(<!--gen:%s-->)(.*?)(<!--/gen:%s-->)" % (name, name), re.S)
    if not pat.search(page):
        raise SystemExit("marker gen:%s not found in page" % name)
    return pat.sub(lambda m: m.group(1) + content + m.group(3), page, count=1)


def build_idp(cfg, page):
    cat_desc, scores = load_reqscores()
    old_reqs = json.loads(re.search(r'<script id="idp-reqs" type="application/json">(.*?)</script>', page, re.S).group(1))
    dom_of = {rid: c["dom"] for rid, c in old_reqs["cat"].items()}
    data = json.loads(re.search(r'<script id="idp-data" type="application/json">(.*?)</script>', page, re.S).group(1))
    seg_label = {s["id"]: s["label"] for s in data["segments"]}
    domain_names = data["domainFull"]

    vendors, problems = [], []
    for v in cfg["vendors"]:
        vid = v["id"]
        fs = parse_factsheet(os.path.join(RES, v["file"]))
        per_dom = {}
        for rid in old_reqs["cat"]:
            s = scores.get(rid, {}).get(vid)
            if s is None:
                problems.append("missing requirement score %s for %s" % (rid, vid))
                continue
            validate_score(rid, vid, s)
            per_dom.setdefault(dom_of[rid], []).append(s["s"])
        dom = [round(sum(per_dom[i]) / len(per_dom[i]) * 2) / 2 for i in range(len(domain_names))]
        gates = [fs["gates"].get(i) for i in range(1, 23)]
        if None in gates:
            problems.append("%s: hard-gate reads missing for %s" % (v["file"], ", ".join("G%02d" % (i + 1) for i, g in enumerate(gates) if g is None)))
        snap = fs["snap"]
        typed = [s for s in fs["sources"] if "ev" in s]
        untyped = [s for s in fs["sources"] if "ev" not in s]
        typed.sort(key=lambda s: s.get("date", ""), reverse=True)
        rec = {
            "id": vid, "name": fs["title"], "seg": v["seg"], "segLabel": seg_label[v["seg"]],
            "cat": clip(snapshot_field(snap, "Category"), 200),
            "fit": clip(snapshot_field(snap, "Initial fit"), 160),
            "pos": clip(snapshot_field(snap, "Positioning"), 200),
            "html": vendor_html(fs, dom, domain_names),
            "sources": [{k: s[k] for k in ("t", "u", "ev", "evc") if k in s} for s in typed + untyped],
            "scores": dom, "gates": gates, "pen": v["pen"],
        }
        recent = snapshot_field(snap, "Recent developments")
        if recent:
            rec["recent"] = plain(recent)
        vendors.append(rec)
    if problems:
        raise SystemExit("Cannot build:\n  " + "\n  ".join(problems))

    data["vendors"] = vendors
    page = replace_json_block(page, "idp-data", data)
    reqs = {"cat": {rid: {"desc": cat_desc.get(rid, c["desc"]), "dom": c["dom"]} for rid, c in old_reqs["cat"].items()},
            "scores": {rid: {v["id"]: scores[rid][v["id"]] for v in cfg["vendors"]} for rid in old_reqs["cat"]}}
    page = replace_json_block(page, "idp-reqs", reqs)

    as_of = cfg["idp_as_of"]
    page = replace_marked(page, "idp-refresh", cfg["idp_refresh_note"].replace("{as_of}", human_date(as_of)))
    page = re.sub(r"researchBaseline:'[0-9-]+'", "researchBaseline:'%s'" % as_of[:7], page)
    return page


# ---------------------------------------------------------------- v3.1 shortlist alignment
ALIGN = os.path.join(RES, "alignment_v3_1.json")
GCELL = {"PASS": ("g-pass", "PASS"), "PARTIAL": ("g-partial", "PART"), "FAIL": ("g-fail", "FAIL"), "UNKNOWN": ("g-unknown", "?")}


def _e(s):
    return html.escape("" if s is None else str(s), quote=True)


def _table(head, rows, first_name=True):
    h = "".join("<th%s>%s</th>" % (' class="name"' if i == 0 and first_name else "", _e(x)) for i, x in enumerate(head))
    body = "".join("<tr>%s</tr>" % "".join(
        "<td%s>%s</td>" % (' class="name"' if i == 0 and first_name else "", c) for i, c in enumerate(r)) for r in rows)
    return '<div class="tbl-scroll"><table class="lined"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, body)


def align_scores(a):
    """Weighted scores are computed here from the ratings in alignment_v3_1.json, never typed."""
    rmap = a["rating_map"]
    vids = [v["id"] for v in a["vendors"]]
    n = len(a["domains"])
    sets = {"v3.1 proposed": [d["w"] for d in a["domains"]],
            "Equal": [1.0] * n,
            "Consultant lens (implied)": [d["w_consultant"] for d in a["domains"]]}
    num = {}
    for d in a["domains"]:
        for v in vids:
            r = d["ratings"].get(v)
            if r is None or r == "":
                continue
            s = r if isinstance(r, (int, float)) else rmap[r]
            num[(d["id"], v)] = float(s)
    res = {}
    for name, w in sets.items():
        res[name] = {}
        for v in vids:
            tw = sum(w[i] for i, d in enumerate(a["domains"]) if (d["id"], v) in num)
            ts = sum(w[i] * num[(d["id"], v)] for i, d in enumerate(a["domains"]) if (d["id"], v) in num)
            res[name][v] = ts / tw if tw else None
    assessed = {v: sum(d["w"] for d in a["domains"] if (d["id"], v) in num) / float(sum(d["w"] for d in a["domains"])) for v in vids}
    return num, res, assessed


def align_demand(a):
    """Use-case demand share per domain: primary priority at 100%, secondary at 50%."""
    fac = {"Core": 1.0, "Adjacent": 0.5, "Out": 0.0}
    pri, sec = {}, {}
    for u in a["usecases"]:
        p = u["value"] * u["urgency"] * fac[u["role"]]
        pri[u["primary"]] = pri.get(u["primary"], 0) + p
        if u.get("secondary"):
            sec[u["secondary"]] = sec.get(u["secondary"], 0) + p
    tot = sum(pri.values()) + 0.5 * sum(sec.values())
    return {d["id"]: (pri.get(d["id"], 0) + 0.5 * sec.get(d["id"], 0)) / tot if tot else 0 for d in a["domains"]}


def render_alignment(a):
    vids = [v["id"] for v in a["vendors"]]
    vl = {v["id"]: v["label"] for v in a["vendors"]}
    num, res, assessed = align_scores(a)
    wsum = float(sum(d["w"] for d in a["domains"]))
    out = []
    out.append('<div class="card"><div class="kicker">Shortlist check · as of %s</div>'
               '<h2 style="margin-top:4px">Aligning the criteria (v3.1) and testing an external shortlist</h2>'
               '<p>Three inputs were compared: the buyer&#x27;s strategic-rationale paper, its use-case register and selection '
               'criteria, and an external consultant&#x27;s shortlisting deliverable. They did not agree on what is being '
               'selected, and the consultant published no weights or numeric scores. v3.1 makes the scope decisions explicit, '
               'moves must-haves into pass/fail gates, consolidates 44 overlapping dimensions into 13 weighted domains, and '
               're-scores the five vendors the consultant assessed. <b>Provisional — read the caveats first.</b></p>'
               % _e(human_date(a["as_of"])))
    out.append(_table(["Input", "What it contains"], [[_e(i["doc"]), _e(i["what"])] for i in a["inputs"]]))
    out.append("</div>")
    out.append('<div class="card"><h3 style="margin-top:0">Caveats you should know</h3><ul>%s</ul></div>'
               % "".join("<li>%s</li>" % _e(c) for c in a["caveats"]))
    # results
    rows = []
    for name in res:
        order = sorted(vids, key=lambda v: -(res[name][v] or 0))
        rows.append([_e(name)] + ["%.2f%s" % (res[name][v], " <b>(#1)</b>" if v == order[0] else "") for v in vids])
    rows.append(["Share of v3.1 weight assessed"] + ["%d%%" % round(assessed[v] * 100) for v in vids])
    g_fail = {v: sum(1 for g in a["gates"] if g["status"][v] == "FAIL") for v in vids}
    g_unk = {v: sum(1 for g in a["gates"] if g["status"][v] == "UNKNOWN") for v in vids}
    rows.append(["Gate FAIL / UNKNOWN"] + ["%d / %d" % (g_fail[v], g_unk[v]) for v in vids])
    out.append('<div class="card"><h3 style="margin-top:0">Scoring result: weighted score (0–5) under three weight sets</h3>'
               '<p>Each vendor&#x27;s score is the weight-averaged rating over the domains where evidence exists. The ranking of the '
               'top two flips with the weight set: the external shortlist&#x27;s preferred platform leads only under its own '
               'implied lens (which emphasises embedded AI, MCP and unstructured data and leaves out viability, Databricks '
               'and TCO). Gaps under ~0.25 are inside the evidence noise. No vendor fails a gate on current evidence, but '
               'every vendor has 7–8 gates still UNKNOWN.</p>')
    out.append(_table(["Weight set"] + [vl[v] for v in vids], rows))
    out.append('<p class="tiernote">Rating map: %s. Demo ratings are the consultant&#x27;s Strong/Good/Limited judgements on '
               'vendor-run demos; numeric cells come from this repo&#x27;s public-evidence domain scores.</p></div>'
               % _e(", ".join("%s = %s" % kv for kv in a["rating_map"].items())))
    # domains
    rows = []
    for d in a["domains"]:
        cells = []
        for v in vids:
            r = d["ratings"].get(v)
            cells.append("—" if r in (None, "") else (_e(r) if isinstance(r, str) else "%.1f" % r) +
                         ("" if r in (None, "") or not isinstance(r, str) else " <span class=\"tiernote\">(%.1f)</span>" % a["rating_map"][r]))
        rows.append(["<b>%s</b> %s" % (_e(d["id"]), _e(d["name"])), "%d" % d["w"], "%.1f" % d["w_consultant"]] + cells)
    out.append('<div class="card"><h3 style="margin-top:0">Domains, weights and the rating behind each score</h3>'
               '<p>v3.1 weights are a proposal for a stakeholder points-budget workshop (each group spreads 100 points; the '
               'median is used). The consultant column is implied, assuming equal weight on its seven demo drivers, with '
               'security treated as a gate. “—” means not assessed by anyone.</p>')
    out.append(_table(["Domain", "v3.1 wt", "Consultant wt"] + [vl[v] for v in vids], rows))
    out.append('<h3>Why each weight, and where each rating comes from</h3>')
    out.append(_table(["Domain", "What the platform must show", "Why this weight", "Rating basis", "Consolidates"],
                      [["<b>%s</b>" % _e(d["id"]), _e(d["shows"]), _e(d["why"]), _e(d["basis"]), _e(d["consolidates"])] for d in a["domains"]]))
    out.append("</div>")
    # gates
    rows = []
    for g in a["gates"]:
        cells = ['<span class="gcell %s">%s</span>' % GCELL[g["status"][v]] for v in vids]
        rows.append(["<b>%s</b>" % _e(g["id"]), _e(g["req"]), _e(g["evidence"])] + cells + [_e(g["note"])])
    out.append('<div class="card"><h3 style="margin-top:0">v3.1 pass/fail gates (A01–A14)</h3>'
               '<p>These sit alongside the main G01–G22 gates and capture the must-haves that the buyer&#x27;s criteria '
               'rated HIGH but every credible vendor should meet anyway (scoring them only adds noise), plus three gates no '
               'input covered: Income Fund instrument model, CRIMS + Apex NZ ingestion, and Bloomberg licensing. UNKNOWN '
               'is not FAIL; it is a due-diligence item.</p>')
    out.append(_table(["Gate", "Requirement", "Evidence required"] + [vl[v] for v in vids] + ["Evidence notes"], rows))
    out.append("</div>")
    # scope
    out.append('<div class="card"><h3 style="margin-top:0">Scope decisions to make before scoring</h3>'
               '<p>The three inputs answer these differently. Decision 1 alone changes which vendors are eligible.</p>')
    out.append(_table(["Decision", "Rationale paper", "Use-case register", "Consultant", "v3.1 default", "Effect on scoring", "Status"],
                      [[_e(s["q"]), _e(s["rationale"]), _e(s["register"]), _e(s["consultant"]), "<b>%s</b>" % _e(s["v31"]), _e(s["effect"]), _e(s["status"])] for s in a["scope"]]))
    out.append("</div>")
    # use cases
    dem = align_demand(a)
    cnt = {r: sum(1 for u in a["usecases"] if u["role"] == r) for r in ("Core", "Adjacent", "Out")}
    rows = [["<b>%s</b> %s" % (_e(d["id"]), _e(d["name"])), "%.0f%%" % (100 * dem[d["id"]]), "%.0f%%" % (100 * d["w"] / wsum),
             "%+.0f pts" % (100 * (d["w"] / wsum - dem[d["id"]]))] for d in a["domains"]]
    out.append('<div class="card"><h3 style="margin-top:0">Use-case triage and weight cross-check</h3>'
               '<p>%d use cases: <b>%d Core</b> (the IDP must deliver), <b>%d Adjacent</b> (needs certified IDP data but runs in '
               'an AI layer, Databricks or a specialist system) and <b>%d Out</b>. Value and urgency are draft (1–5); priority = '
               'value × urgency × role factor (Core 1, Adjacent 0.5, Out 0). Demand share counts a use case&#x27;s primary domain '
               'at 100%% and secondary at 50%%. Use-case demand points even more strongly at core data, history, instrument '
               'coverage and calculations than the proposed weights do. Domains D11–D13 serve no use case directly, so they '
               'always look over-weighted on this test.</p>' % (len(a["usecases"]), cnt["Core"], cnt["Adjacent"], cnt["Out"]))
    out.append(_table(["Domain", "Use-case demand", "v3.1 weight", "Weight − demand"], rows))
    out.append('<details class="srcs"><summary>All %d use cases with triage</summary>%s</details></div>' % (
        len(a["usecases"]), _table(["UC", "Use case", "Horizon", "FRD tag", "Role", "Value", "Urgency", "Primary", "Secondary", "Why"],
                                   [[_e(u["id"]), _e(u["name"]), _e(u["horizon"]), _e(u["frd"]), _e(u["role"]), str(u["value"]), str(u["urgency"]),
                                     _e(u["primary"]), _e(u["secondary"]), _e(u["why"])] for u in a["usecases"]])))
    # concerns
    order = {"High": 0, "Med": 1, "Low": 2}
    cs = sorted(a["concerns"], key=lambda c: order.get(c["sev"], 3))
    out.append('<div class="card"><h3 style="margin-top:0">Concerns, corrections and questions to ask (%d)</h3>'
               '<p>High = could change the selection or create material risk; Med = must resolve in POC or due diligence; '
               'Low = correction or clarity.</p>' % len(cs))
    out.append(_table(["Severity", "Area", "Finding", "Evidence", "Question / action"],
                      [["<b>%s</b>" % _e(c["sev"]), _e(c["area"]), _e(c["finding"]), _e(c["evidence"]), _e(c["ask"])] for c in cs]))
    out.append("</div>")
    # sources
    rows = [[_e(s["topic"]), '<a href="%s" target="_blank" rel="noopener">%s</a>' % (_e(s["url"]), _e(s["title"])), _e(s["pub"]),
             _e(s["type"]), _e(s["date"]), _e(s["read"])] for s in a["sources"]]
    out.append('<div class="card"><h3 style="margin-top:0">Sources for this check (accessed 5 Nov 2026 unless stated)</h3>'
               '<p class="tiernote">“search-only” = seen in search results; page fetches were blocked in the research environment. '
               '“opened (repo)” = opened during the v3 refresh on 3 Nov 2026.</p>')
    out.append(_table(["Topic", "Source", "Publisher", "Type", "Published", "Read"], rows))
    out.append("</div>")
    return "\n".join(out)


def build_alignment(page):
    if "<!--gen:idp-align-->" not in page:
        return page
    a = json.loads(read(ALIGN))
    return replace_marked(page, "idp-align", render_alignment(a))


def build_landscape(cfg, page):
    for name in ("landscape-asof-hero", "landscape-asof-caveat", "landscape-asof-footer"):
        if ("<!--gen:%s-->" % name) in page:
            page = replace_marked(page, name, human_date(cfg["landscape_as_of"]))
    return page


def root_copy(page):
    """Root copies differ from provider-landscape/ only by the research-explorer.js path."""
    return page.replace('<script src="research-explorer.js"', '<script src="provider-landscape/research-explorer.js"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if any output would change")
    a = ap.parse_args()
    cfg = json.loads(read(os.path.join(RES, "vendors.json")))

    idp_src = os.path.join(PL, "idp_evaluation.html")
    land_src = os.path.join(PL, "financial_data_providers_landscape.html")
    idp = build_alignment(build_idp(cfg, read(idp_src)))
    land = build_landscape(cfg, read(land_src))
    outputs = {
        idp_src: idp,
        os.path.join(ROOT, "idp_evaluation.html"): root_copy(idp),
        land_src: land,
        os.path.join(ROOT, "financial_data_providers_landscape.html"): root_copy(land),
        os.path.join(ROOT, "index.html"): root_copy(land),
    }
    stale = []
    for p, s in outputs.items():
        cur = read(p) if os.path.exists(p) else None
        if cur != s:
            stale.append(os.path.relpath(p, ROOT))
            if not a.check:
                write(p, s)
    if a.check:
        if stale:
            print("Stale (run build_pages.py):\n  " + "\n  ".join(stale))
            sys.exit(1)
        print("All pages up to date.")
    else:
        print("Rebuilt: %s" % (", ".join(stale) if stale else "nothing changed"))


if __name__ == "__main__":
    main()
