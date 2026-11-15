# Site generation

`python3 tools/build.py` (needs pandoc >= 3) builds the static site into `docs/`:

- `README.md` gives the main page `docs/index.html`;
- each folder gets a page `docs/<folder>/index.html` made from `<folder>/<folder>.md` (or from its only `.md` file); the other `.md` files of the folder become extra pages linked from the folder page, and PDF / GIF / PNG files are copied;
- links to `.md` files are rewritten to the HTML pages; math is rendered by MathJax in the browser.

The workflow `.github/workflows/pages.yml` runs this script on every push to `main` and commits `docs/`. Do not edit `docs/` by hand. GitHub Pages is set to serve the branch `main`, folder `/docs`.

To keep a file off the site, list its path (one per line) in `tools/exclude.txt`.
