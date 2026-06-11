#!/usr/bin/env python3
"""Static validation for the Jekyll site: front matter, permalinks, prev/next,
internal-link resolution, and a content-presence report. No Ruby/Jekyll needed.

Run from repo root:  python scripts/check_pages.py
"""
import os, re, sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEURL = "/kun"  # from _config.yml

# Folders/files that carry front matter pages
SCAN_DIRS = ["course", "foundations", "zh", "en", "fr", "history"]
SCAN_ROOT_FILES = ["index.html", "nature-of-time.md", "paradoxes.md", "prehistory.md"]

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def parse_front_matter(text):
    """Return (dict, body). Flat `key: value` only — enough for this site."""
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm, body = {}, text[m.end():]
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        if line[0] in " \t":  # nested (e.g. metadata children) — ignore
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def iter_pages():
    paths = []
    for d in SCAN_DIRS:
        dd = os.path.join(ROOT, d)
        if not os.path.isdir(dd):
            continue
        for cur, _, files in os.walk(dd):
            for f in files:
                if f.endswith((".md", ".html")):
                    paths.append(os.path.join(cur, f))
    for f in SCAN_ROOT_FILES:
        p = os.path.join(ROOT, f)
        if os.path.isfile(p):
            paths.append(p)
    return sorted(paths)


def norm(permalink):
    """Normalize a permalink to a comparable key: no baseurl, trailing slash kept."""
    pl = permalink
    if pl.startswith(BASEURL):
        pl = pl[len(BASEURL):]
    if not pl.startswith("/"):
        pl = "/" + pl
    if not pl.endswith("/") and "." not in pl.rsplit("/", 1)[-1]:
        pl += "/"
    return pl


def resolve_relative(src_permalink, href):
    """Resolve a relative markdown href against the source page's permalink."""
    base = src_permalink if src_permalink.endswith("/") else src_permalink.rsplit("/", 1)[0] + "/"
    parts = base.strip("/").split("/") if base.strip("/") else []
    for seg in href.split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if parts:
                parts.pop()
        else:
            parts.append(seg)
    out = "/" + "/".join(parts)
    if not out.endswith("/") and "." not in parts[-1] if parts else True:
        out += "/"
    return out


def main():
    pages = iter_pages()
    by_path = {}
    permalinks = {}        # normalized permalink -> path
    errors, warnings = [], []

    for p in pages:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        fm, body = parse_front_matter(text)
        by_path[rel] = (fm, body)
        if fm is None:
            # index.html files may legitimately have front matter; flag only scanned content md
            if rel.endswith(".md"):
                warnings.append(f"{rel}: no front matter")
            continue
        # required keys
        for key in ("layout", "permalink"):
            if key not in fm and not (rel.endswith("index.html")):
                warnings.append(f"{rel}: missing front-matter key '{key}'")
        if "permalink" in fm:
            k = norm(fm["permalink"])
            if k in permalinks:
                errors.append(f"DUPLICATE permalink {k}: {rel} vs {permalinks[k]}")
            else:
                permalinks[k] = rel
        # math flag check
        if ("$$" in body or re.search(r"(?<!\\)\$[^$\n]+\$", body)) and fm.get("math") not in ("true", "True"):
            warnings.append(f"{rel}: uses $ math but no 'math: true'")

    plset = set(permalinks)

    # prev/next chain resolution (front-matter values are absolute permalinks OR refs)
    # In course/ & foundations/ they are absolute (/course/05/). In zh/ they are `ref` slugs.
    def ref_to_permalink(val, src_lang_dir):
        # zh/en/fr pages use bare ref slugs like "frontier-2026"
        if val.startswith("/"):
            return norm(val)
        return norm(f"/{src_lang_dir}/{val}/")

    for rel, (fm, body) in by_path.items():
        if not fm:
            continue
        src_pl = norm(fm["permalink"]) if "permalink" in fm else None
        lang_dir = rel.split("/", 1)[0] if "/" in rel else ""
        for key in ("prev", "next"):
            if key in fm and fm[key]:
                target = ref_to_permalink(fm[key], lang_dir)
                if target not in plset:
                    errors.append(f"{rel}: {key} -> {fm[key]} resolves to {target} (NOT FOUND)")

    # internal markdown link resolution for the foundations + course index + zh journey
    focus = [r for r in by_path if r.startswith("foundations/")] + [
        "course/index.md", "zh/math-ml-foundations.md",
    ]
    for rel in focus:
        if rel not in by_path:
            continue
        fm, body = by_path[rel]
        if not fm or "permalink" not in fm:
            continue
        src_pl = norm(fm["permalink"])
        for href in LINK_RE.findall(body):
            u = urlparse(href)
            if u.scheme or href.startswith("#") or href.startswith("mailto:"):
                continue
            if href.startswith("http"):
                continue
            target = href.split("#")[0]
            if not target:
                continue
            if target.startswith("/"):
                resolved = norm(target)
            else:
                resolved = resolve_relative(src_pl, target)
            # github blob links etc already filtered; only check site-internal
            if resolved not in plset:
                errors.append(f"{rel}: link [{href}] -> {resolved} (NOT FOUND)")

    # ---- report ----
    print("=" * 60)
    print("PAGES FOUND:", len(pages))
    print("PERMALINKS:", len(permalinks))
    print("=" * 60)

    print("\n--- COURSE LECTURES (course/) ---")
    for rel in sorted(by_path):
        if rel.startswith("course/") and rel.endswith(".md"):
            fm, body = by_path[rel]
            title = fm.get("title", "?") if fm else "?"
            words = len(body.split())
            print(f"  {rel:22} {words:5d} words  {title}")

    print("\n--- FOUNDATIONS (foundations/) ---")
    for rel in sorted(by_path):
        if rel.startswith("foundations/"):
            fm, body = by_path[rel]
            title = fm.get("title", "?") if fm else "?"
            words = len(body.split())
            print(f"  {rel:30} {words:5d} words  {title}")

    print("\n--- SITE JOURNEY (zh/) ---")
    for rel in sorted(by_path):
        if rel.startswith("zh/"):
            fm, body = by_path[rel]
            words = len(body.split())
            print(f"  {rel:34} {words:5d} words")

    print("\n--- EN / FR PARITY vs ZH ---")
    zh_refs = {r[3:] for r in by_path if r.startswith("zh/") and r != "zh/index.html"}
    for lang in ("en", "fr"):
        have = {r[3:] for r in by_path if r.startswith(lang + "/") and r != f"{lang}/index.html"}
        missing = sorted(zh_refs - have)
        print(f"  {lang}: has {sorted(have)}")
        if missing:
            print(f"      MISSING vs zh: {missing}")

    print("\n" + "=" * 60)
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print("  ⚠ ", w)
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print("  ✗ ", e)
        sys.exit(1)
    print("\n✓ No broken links / duplicate permalinks / unresolved prev-next.")


if __name__ == "__main__":
    main()
