#!/usr/bin/env python3
"""Translation status + validation for the en/fr mirrors of the Chinese pages.

For every Chinese source page it computes the expected en/fr target file and
permalink, then reports which targets are missing and, for existing targets:
wrong permalink/lang, leftover Chinese characters, and internal links that do
not resolve to a page of the built site.

Run from repo root:
  python scripts/check_i18n.py              # summary + problems
  python scripts/check_i18n.py --todo       # also list missing targets
  python scripts/check_i18n.py FILE...      # check only these target files
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "fr")
SOURCE_DIRS = ["course", "foundations", "history", "tasks", "prehistory",
               "nature-of-time", "paradoxes", "applications"]
SOURCE_ROOT_FILES = ["prehistory.md", "nature-of-time.md", "paradoxes.md", "applications.md"]
ZH_ONLY = ["zh/kernel-u-net.md", "zh/linear-autoregression.md",
           "zh/math-ml-foundations.md", "zh/prediction-in-action.md",
           # the original trilingual intro, since rewritten in Chinese
           "zh/index.html", "zh/time-series.md", "zh/forecasting.md", "zh/kun.md"]

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CJK_RE = re.compile(r"[㐀-鿿豈-﫿]")
MD_LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
HREF_RE = re.compile(r"""href=["']([^"'{]+)["']""")
LIQUID_URL_RE = re.compile(r"""\{\{\s*['"](/[^'"]*)['"]\s*\|\s*relative_url""")


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def front_matter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if line and line[0] not in " \t#" and ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text[m.end():]


def sources():
    out = []
    for d in SOURCE_DIRS:
        for cur, _, files in os.walk(os.path.join(ROOT, d)):
            out += [rel(os.path.join(cur, f)) for f in files if f.endswith(".md")]
    out += [f for f in SOURCE_ROOT_FILES + ZH_ONLY if os.path.isfile(os.path.join(ROOT, f))]
    return sorted(out)


def target_path(src, lang):
    return lang + "/" + (src[3:] if src.startswith("zh/") else src)


def target_permalink(src_permalink, lang):
    if src_permalink.startswith("/zh/"):
        return "/" + lang + src_permalink[3:]
    return "/" + lang + src_permalink


def all_permalinks():
    """Every permalink in the site (pages + static assets), normalized."""
    pls = set()
    skip = {"_site", "node_modules", "vendor", "notebooks", ".git", ".jekyll-cache"}
    for cur, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
        for f in files:
            p = os.path.join(cur, f)
            r = rel(p)
            if r.startswith("assets/"):
                pls.add("/" + r)
                continue
            if not f.endswith((".md", ".html")) or r.startswith("_"):
                continue
            with open(p, encoding="utf-8") as fh:
                fm, _ = front_matter(fh.read())
            if fm.get("permalink"):
                pls.add(norm(fm["permalink"]))
    return pls


def norm(u):
    u = u.split("#")[0].split("?")[0]
    if u.startswith("/kun/"):
        u = u[4:]
    if not u.startswith("/"):
        u = "/" + u
    if not u.endswith("/") and "." not in u.rsplit("/", 1)[-1]:
        u += "/"
    return u


def resolve(base, href):
    parts = [p for p in base.strip("/").split("/") if p]
    for seg in href.split("#")[0].split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if parts:
                parts.pop()
        else:
            parts.append(seg)
    return norm("/" + "/".join(parts))


def check_target(path, src, lang, permalinks):
    problems = []
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        text = fh.read()
    fm, body = front_matter(text)
    with open(os.path.join(ROOT, src), encoding="utf-8") as fh:
        sfm, _ = front_matter(fh.read())
    want = target_permalink(sfm.get("permalink", ""), lang)
    if norm(fm.get("permalink", "")) != norm(want):
        problems.append(f"permalink {fm.get('permalink')!r} != {want!r}")
    if fm.get("lang") != lang:
        problems.append(f"lang {fm.get('lang')!r} != {lang!r}")
    for k in ("layout", "math", "prev", "next", "ref"):
        if sfm.get(k) != fm.get(k):
            problems.append(f"front matter {k}: {fm.get(k)!r} (source has {sfm.get(k)!r})")
    cjk = [l.strip()[:60] for l in text.splitlines() if CJK_RE.search(l)]
    if cjk:
        problems.append(f"{len(cjk)} line(s) still contain Chinese, e.g. {cjk[0]!r}")
    page = norm(fm.get("permalink", want))
    links = [(h, resolve(page, h)) for h in MD_LINK_RE.findall(body) + HREF_RE.findall(body)
             if not re.match(r"^(https?:|mailto:|#|data:|javascript:)", h)]
    links += [(h, norm(h)) for h in LIQUID_URL_RE.findall(body)]
    for h, r in links:
        if r not in permalinks:
            problems.append(f"broken link {h} -> {r}")
        elif not r.startswith(("/" + lang + "/", "/assets/")):
            problems.append(f"link leaves the {lang} tree: {h} -> {r}")
    return problems


def main(argv):
    todo = "--todo" in argv
    only = {a.replace("\\", "/") for a in argv if not a.startswith("--")}
    permalinks = all_permalinks()
    srcs = sources()
    missing, bad, ok = [], {}, 0
    for src in srcs:
        for lang in LANGS:
            tgt = target_path(src, lang)
            if only and tgt not in only:
                continue
            if not os.path.isfile(os.path.join(ROOT, tgt)):
                missing.append(tgt)
                continue
            probs = check_target(tgt, src, lang, permalinks)
            if probs:
                bad[tgt] = probs
            else:
                ok += 1
    total = ok + len(bad) + len(missing)
    print(f"targets: {total}  ok: {ok}  with problems: {len(bad)}  missing: {len(missing)}")
    for tgt, probs in sorted(bad.items()):
        print(f"\n{tgt}")
        for p in probs:
            print("   - " + p)
    if todo and missing:
        print("\nmissing:")
        for m in missing:
            print("   " + m)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
