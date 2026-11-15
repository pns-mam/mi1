#!/usr/bin/env python3
"""Build static HTML pages (into docs/) from README.md and the other Markdown files.

- README.md            -> docs/index.html (main page); Jupyter notebooks (.ipynb) are handled like .md files
- <dir>/<dir>.md       -> docs/<dir>/index.html (one page per folder)
- any other <dir>/x.md -> docs/<dir>/x.html (linked from the folder page)
- PDF, GIF, PNG... are copied as they are; links to .md files are rewritten.

Needs pandoc (>= 3). Math is rendered in the browser by MathJax.
Usage: python3 tools/build.py
"""
import os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
TOOLS = ROOT / "tools"
SKIP = {".git", ".github", "docs", "tools"}
SOURCES = {".md", ".ipynb"}
ASSETS = {".pdf", ".png", ".gif", ".jpg", ".jpeg", ".svg", ".csv"}
LOGOS = ["https://raw.githubusercontent.com/pns-mam/edp1/master/logo-pns.png",
         "http://caillau.perso.math.cnrs.fr/logo-pns.png"]
LINK = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")


def excluded():
    f = TOOLS / "exclude.txt"
    if not f.exists():
        return set()
    return {Path(l.strip()) for l in f.read_text().splitlines() if l.strip() and not l.startswith("#")}


def files():
    skip = excluded()
    for p in sorted(ROOT.rglob("*")):
        rel = p.relative_to(ROOT)
        if p.is_file() and not (set(rel.parts) & SKIP) and not rel.parts[0].startswith(".") and rel not in skip:
            yield rel


MAIN = {}   # folder -> Markdown file that gives the folder page


def pick_main(mds):
    for d in {m.parent for m in mds if m.parent != Path(".")}:
        cands = sorted(m for m in mds if m.parent == d)
        named = [m for m in cands if m.stem == d.name]
        MAIN[d] = named[0] if named else (cands[0] if len(cands) == 1 else None)


def page_of(rel):
    """Output path (relative to docs/) of a Markdown file."""
    if rel == Path("README.md"):
        return Path("index.html")
    if MAIN.get(rel.parent) == rel:
        return rel.parent / "index.html"
    return rel.with_suffix(".html")


def relurl(target, start_dir):
    u = os.path.relpath(target, start_dir).replace(os.sep, "/")
    return "./" if u == "." else u


def dirurl(target, start_dir):
    u = relurl(target, start_dir)
    return u if u.endswith("/") else u + "/"


def rewrite(text, rel, mds):
    here = rel.parent
    def sub(m):
        pre, url, post = m.groups()
        if url in LOGOS or url.endswith("/logo-pns.png") and url.startswith("http"):
            return pre + relurl("logo-pns.png", here) + post
        if re.match(r"^([a-z]+:|#)", url):
            return m.group(0)
        path, frag = (url.split("#", 1) + [""])[:2]
        tgt = (here / path)
        tgt = Path(os.path.normpath(tgt))
        if tgt in mds:                                   # link to a Markdown file
            out = page_of(tgt)
            u = dirurl(out.parent, here) if out.name == "index.html" else relurl(out, here)
        elif tgt.suffix == ".pdf" and MAIN.get(tgt.parent) is not None and MAIN[tgt.parent].stem == tgt.stem:
            u = dirurl(tgt.parent, here)                  # main PDF of a folder -> its page
        else:
            return m.group(0)                             # asset: same relative path
        return pre + u + ("#" + frag if frag else "") + post
    return LINK.sub(sub, text)


def nb_text(raw):
    """First markdown cell of a notebook (used only for the page title)."""
    import json
    for c in json.loads(raw).get("cells", []):
        if c.get("cell_type") == "markdown":
            return "".join(c.get("source", []))
    return ""


def title_of(text):
    heads = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("![") :
            continue
        if re.match(r"^#{1,6} ", s):
            if s.startswith("# "):
                heads.append(re.sub(r"[*_`]", "", s[2:]).strip())
            continue
        break
    return " – ".join(heads) or "EDP1"


def label(p):
    return p.stem


def nav(rel, mds, allfiles):
    if rel == Path("README.md"):
        return ""
    d = rel.parent
    here = page_of(rel)
    items = []
    for f in allfiles:
        if f.parent != d or f == rel:
            continue
        if f in mds:
            items.append((label(f), relurl(page_of(f), here.parent)))
        elif f.suffix == ".pdf":
            items.append((label(f) + " (PDF)", relurl(f, here.parent)))
    items = [f'<a href="{u}">{t}</a>' for t, u in items]
    home = relurl("index.html", here.parent)
    extra = (" · <span>Dans ce dossier :</span> " + " · ".join(items)) if items else ""
    return f'<nav><a href="{home}">← Accueil</a>{extra}</nav>'


def main():
    allfiles = list(files())
    mds = {f for f in allfiles if f.suffix in SOURCES}
    pick_main(mds)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / ".nojekyll").write_text("")
    shutil.copy(TOOLS / "style.css", OUT / "style.css")
    for f in allfiles:
        if f.suffix in ASSETS:
            (OUT / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / f, OUT / f)
    for rel in sorted(mds):
        raw = (ROOT / rel).read_text(encoding="utf-8")
        nb = rel.suffix == ".ipynb"
        if nb:   # absolute logo URLs inside notebooks -> local logo
            text = re.sub(r"https?://[^\s\"')]*/logo-pns\.png", lambda m: relurl("logo-pns.png", rel.parent), raw)
        else:
            text = rewrite(raw, rel, mds)
        out = OUT / page_of(rel)
        out.parent.mkdir(parents=True, exist_ok=True)
        root = os.path.relpath(OUT, out.parent).replace(os.sep, "/")
        root = "" if root == "." else root + "/"
        cmd = ["pandoc", "-f", "ipynb" if nb else "gfm+tex_math_dollars", "-t", "html5", "--standalone",
               "--template", str(TOOLS / "template.html"), "--mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
               "--highlight-style", "pygments",
               "-V", f"root={root}", "-V", f"pagetitle={title_of(nb_text(text) if nb else text)}", "-o", str(out)]
        subprocess.run(cmd, input=text.encode(), check=True)
        html = out.read_text(encoding="utf-8").replace("<!--NAV-->", nav(rel, mds, allfiles))
        out.write_text(html, encoding="utf-8")
        print(f"{rel} -> docs/{page_of(rel)}")


if __name__ == "__main__":
    sys.exit(main())
