#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the source register: one row per unique URL cited in the research notes and the pages.

    python3 provider-landscape/tools/build_register.py
        -> provider-landscape/source_register.csv

Columns
    url            the cited URL
    providers      provider / vendor ids that cite it (file stem, or page entry id)
    date           publication date from the source tag, else the access date recorded in the note
    date_kind      published | accessed | none
    source_type    evidence type from the tag (Official release note, News, ...), else blank
    authorship     vendor | independent | unclassified
    authorship_basis  tagged (written in the note) | heuristic (domain rule) | none
    access         opened | search-only — how the researcher reached the source
    access_basis   tagged | method-note (Aug 2026 notes say URLs were search-sourced, not fetched)
    cited_in       notes / pages that contain it
    link_status    ok | dead | blocked | unchecked   (from link_check.csv, written by check_links.py)
    http_status    last HTTP status or error from the link check
    checked_at     when the link check ran

Stdlib only. Rows from an existing link_check.csv are merged in, so re-running after a link
check keeps the results.
"""
import csv, glob, io, json, os, re
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
PL = os.path.dirname(HERE)
ROOT = os.path.dirname(PL)
OUT = os.path.join(PL, "source_register.csv")
CHECK = os.path.join(PL, "link_check.csv")

URL_RE = re.compile(r"https?://[^\s\"'<>\\)\]]+")
TAG_RE = re.compile(r"\[(vendor|independent)\s*·\s*([^·\]]+?)\s*·\s*([^·\]]+?)\s*·\s*(opened|search-only)\s*\]", re.I)
ACC_RE = re.compile(r"accessed\s+(\d{4}-\d{2}(?:-\d{2})?)")
DATE_RE = re.compile(r"\((\d{4}-\d{2}-\d{2})\)")

PR_WIRES = ("prnewswire.com", "businesswire.com", "globenewswire.com", "einpresswire.com", "accesswire.com",
            "newswire.ca", "medianet.com.au", "cision.com", "kyodonewsprwire.jp")
INDEPENDENT = ("a-teaminsight.com", "waterstechnology.com", "wikipedia.org", "g2.com", "trustpilot.com",
               "reddit.com", "capterra.com", "trustradius.com", "gartner.com", "forrester.com", "ft.com",
               "reuters.com", "bloomberg.com/news", "wsj.com", "cnbc.com", "techcrunch.com", "sec.gov",
               "assetservicingtimes.com", "thetradenews.com", "fintechfutures.com", "finextra.com/newsarticle",
               "investordaily.com.au", "superreview.com.au", "funds-europe.com", "investmentnews.com",
               "cutterassociates.com", "celent.com", "burton-taylor.com", "costbench.com", "vendr.com",
               "crunchbase.com", "cbinsights.com", "pitchbook.com", "zoominfo.com", "theorg.com", "builtin.com",
               "news.ycombinator.com", "medium.com", "substack.com", "github.com/topics", "hackernoon.com")
SKIP = ("json-schema.org", "://www.w3.org", "fonts.googleapis", "fonts.gstatic")


def host(u):
    h = urlparse(u).netloc.lower()
    return h[4:] if h.startswith("www.") else h


def clean(u):
    return u.rstrip(".,;:'\"")


def heuristic_side(url, provider):
    h = host(url)
    if any(w in h for w in PR_WIRES):
        return "vendor"
    if any(i in (h + urlparse(url).path) for i in INDEPENDENT):
        return "independent"
    tok = re.sub(r"[^a-z]", "", provider.split("-")[0].lower())
    if tok and len(tok) >= 4 and tok in h.replace("-", "").replace(".", ""):
        return "vendor"
    return "unclassified"


def main():
    rows = {}

    def add(url, provider, where, tag=None, accessed=None, method_note=False):
        url = clean(url)
        if any(s in url for s in SKIP) or len(url) < 12:
            return
        r = rows.setdefault(url, {"url": url, "providers": set(), "cited_in": set(), "date": "", "date_kind": "none",
                                  "source_type": "", "authorship": "", "authorship_basis": "none",
                                  "access": "", "access_basis": ""})
        r["providers"].add(provider)
        r["cited_in"].add(where)
        if tag:
            side, typ, when, how = (g.strip() for g in tag.groups())
            r.update(authorship=side.lower(), authorship_basis="tagged", source_type=typ, access=how.lower(), access_basis="tagged")
            if re.match(r"\d{4}", when):
                if r["date_kind"] != "published" or when > r["date"]:
                    r["date"], r["date_kind"] = when, "published"
        if accessed and r["date_kind"] != "published" and accessed > r["date"]:
            r["date"], r["date_kind"] = accessed, "accessed"
        if not r["access"] and method_note:
            r["access"], r["access_basis"] = "search-only", "method-note"

    # research notes (source of truth)
    for f in sorted(glob.glob(os.path.join(PL, "idp-research", "*.md")) + glob.glob(os.path.join(PL, "research", "*.md"))):
        rel = os.path.relpath(f, ROOT)
        stem = os.path.splitext(os.path.basename(f))[0]
        for line in io.open(f, encoding="utf-8").read().splitlines():
            for u in URL_RE.findall(line):
                tag = TAG_RE.search(line)
                acc = ACC_RE.search(line) or DATE_RE.search(line)
                # Notes written before the v3 refresh state that URLs were search-sourced, not fetched.
                add(u, stem, rel, tag, acc.group(1) if acc else None, method_note=not tag)

    # pages (anything cited only in a page still gets a row)
    for page in ("idp_evaluation.html", "financial_data_providers_landscape.html"):
        p = os.path.join(PL, page)
        t = io.open(p, encoding="utf-8").read()
        for bid in ("idp-data", "ext-data"):
            m = re.search(r'<script id="%s" type="application/json">(.*?)</script>' % bid, t, re.S)
            if not m:
                continue
            d = json.loads(m.group(1))
            for v in d.get("vendors", []) + d.get("ext", []) + d.get("earnings", []):
                for s in v.get("sources", []):
                    add(s["u"], v["id"], "provider-landscape/" + page)
            for k, lst in d.get("coreLinks", {}).items():
                for s in lst:
                    add(s["u"], k, "provider-landscape/" + page)
        for u in URL_RE.findall(t):
            u = clean(u)
            if u not in rows:
                add(u, "page", "provider-landscape/" + page)

    checks = {}
    if os.path.exists(CHECK):
        with io.open(CHECK, encoding="utf-8") as fh:
            for c in csv.DictReader(fh):
                checks[c["url"]] = c

    cols = ["url", "providers", "date", "date_kind", "source_type", "authorship", "authorship_basis",
            "access", "access_basis", "cited_in", "link_status", "http_status", "checked_at"]
    with io.open(OUT, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for url in sorted(rows):
            r = rows[url]
            prov = sorted(r["providers"] - {"page"}) or ["page"]
            if r["authorship_basis"] == "none":
                side = heuristic_side(url, prov[0])
                r["authorship"], r["authorship_basis"] = side, ("heuristic" if side != "unclassified" else "none")
            c = checks.get(url, {})
            w.writerow({**{k: r.get(k, "") for k in cols}, "providers": ";".join(prov), "cited_in": ";".join(sorted(r["cited_in"])),
                        "access": r["access"] or "unknown", "link_status": c.get("link_status", "unchecked"),
                        "http_status": c.get("http_status", ""), "checked_at": c.get("checked_at", "")})
    n = len(rows)
    tagged = sum(1 for r in rows.values() if r["authorship_basis"] == "tagged")
    print("source_register.csv: %d URLs (%d with tagged authorship/type/date, %d link-checked)" % (n, tagged, sum(1 for u in rows if u in checks)))


if __name__ == "__main__":
    main()
