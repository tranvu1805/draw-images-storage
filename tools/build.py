"""Build figures from src/theory_review.

    tools/.venv/bin/python tools/build.py              # everything
    tools/.venv/bin/python tools/build.py img024 img188 # some ids
"""
import os, re, subprocess, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
SRC = os.path.join(REPO, 'src', 'theory_review')
sys.path.insert(0, TOOLS)
import drawkit  # noqa: E402

ids = sys.argv[1:] or sorted(f.rsplit('.', 1)[0] for f in os.listdir(SRC) if f.endswith(('.py', '.html')))
html = [i for i in ids if os.path.exists(os.path.join(SRC, f'{i}.html'))]
py = [i for i in ids if os.path.exists(os.path.join(SRC, f'{i}.py'))]
failed = []
for i in py:
    r = subprocess.run([sys.executable, os.path.join(SRC, f'{i}.py')], cwd=REPO,
                       env={**os.environ, 'PYTHONPATH': TOOLS}, capture_output=True, text=True)
    if r.returncode:
        failed.append(i)
        print(f'FAIL {i}\n{r.stderr[-1500:]}')
    else:
        print('built', i)
if html:
    r = subprocess.run(['node', os.path.join(TOOLS, 'render_html.mjs'), *html], cwd=REPO)
    if r.returncode:
        failed += html
    else:
        for i in html:
            head = open(os.path.join(SRC, f'{i}.html'), encoding='utf-8').readline()
            m = re.search(r'width:\s*(\d+)', head)
            drawkit.finalize(i, os.path.join(REPO, 'work', 'raw', f'{i}.png'), width=int(m.group(1)) if m else None)
            print('built', i)
missing = [i for i in ids if i not in py and i not in html]
if missing:
    print('no source for', ' '.join(missing))
sys.exit(1 if failed else 0)
