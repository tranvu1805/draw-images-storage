# draw-images-storage

Figures for the Theory Review app (grade-12 review quizzes), drawn from scratch.

- `theory_review/<subject>/<id>.png` — the published figures, served through
  jsDelivr: `https://cdn.jsdelivr.net/gh/tranvu1805/draw-images-storage@<ref>/theory_review/<subject>/<id>.png`
- `src/theory_review/<id>.py | .html` — the source of each figure
  (matplotlib, or an HTML fragment rendered with KaTeX)
- `tools/` — the shared drawing kit and build scripts
- `ATTRIBUTION.md` — the few figures that use third-party images, with their licences

Rebuild:

```sh
python3 -m venv tools/.venv && tools/.venv/bin/pip install matplotlib numpy pillow rdkit
(cd tools && npm install)
tools/.venv/bin/python tools/build.py            # all figures
tools/.venv/bin/python tools/build.py img024     # one figure
```

A rebuilt figure gets a new URL only when the app data is pointed at a new
ref (tag or commit), so published refs never change under the app.
