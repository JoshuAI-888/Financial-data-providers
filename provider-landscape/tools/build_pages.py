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
    idp = build_idp(cfg, read(idp_src))
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
