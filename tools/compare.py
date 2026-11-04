"""Side-by-side review sheet: original (left) vs redrawn (right).

    tools/.venv/bin/python tools/compare.py img024 img025 …  -> work/compare/<first>_<last>.png
Originals are read from the local audit folder (never copied into this repo).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
ORIG = '/Users/vincent/AndroidStudioProjects/theory_review/quiz-scraper/exam_subjects/image_audit/originals'
INFO = json.load(open(os.path.join(TOOLS, 'figures.json')))
ids = sys.argv[1:]
CW, CH, LH = 520, 380, 22
font = ImageFont.load_default(size=16)


def load(p):
    src = Image.open(p).convert('RGBA')
    im = Image.new('RGB', src.size, 'white')
    im.paste(src, mask=src.split()[3])
    return im


sheet = Image.new('RGB', (CW * 2, (CH + LH) * len(ids)), 'white')
d = ImageDraw.Draw(sheet)
for r, i in enumerate(ids):
    y = r * (CH + LH)
    orig = next((os.path.join(ORIG, f) for f in os.listdir(ORIG) if f.startswith(i + '.')), None)
    d_out = os.path.join(REPO, 'theory_review', INFO[i]['subject'])
    new = next((os.path.join(d_out, f) for f in sorted(os.listdir(d_out)) if f.startswith(i + '.')), None) \
        if os.path.isdir(d_out) else None
    for c, p in enumerate([orig, new]):
        x = c * CW
        d.rectangle([x, y, x + CW - 1, y + CH + LH - 1], outline='red')
        if p and os.path.exists(p):
            im = load(p)
            d.text((x + 4, y + 2), f"{i} {'original' if c == 0 else 'new'} {im.size[0]}x{im.size[1]}", fill='blue', font=font)
            im.thumbnail((CW - 8, CH - 6))
            sheet.paste(im, (x + 4, y + LH + 2))
        else:
            d.text((x + 4, y + 2), f'{i} missing', fill='red', font=font)
os.makedirs(os.path.join(REPO, 'work', 'compare'), exist_ok=True)
out = os.path.join(REPO, 'work', 'compare', f'{ids[0]}_{ids[-1]}.png')
sheet.save(out)
print(out)
