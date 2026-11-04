"""Shared drawing kit for the Theory Review figures.

Every figure has an id (img001 … img271). A figure's source is
src/theory_review/<id>.py (matplotlib, uses this module) or <id>.html
(rendered by render_html.mjs). The finished PNG lands in
theory_review/<subject>/<id>.png, resized to the width the app already
lays out for that figure, so it shows at the same size on screen.

Typical source file:

    from drawkit import *
    fig, ax = canvas('img024', aspect=0.9)
    xy_axes(ax, (-2.6, 2.6), (-2.6, 3.2), xticks=[-2, -1, 1, 2], yticks=[-2, -1, 1, 2])
    plot_fn(ax, lambda x: x**4 - 2*x**2 - 1, -2.1, 2.1)
    save(fig, 'img024')
"""
import json
import os
import sys

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
WORK = os.path.join(REPO, 'work')
OUT = os.path.join(REPO, 'theory_review')
INFO = json.load(open(os.path.join(TOOLS, 'figures.json'), encoding='utf-8'))

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 11,
    'mathtext.fontset': 'stix',
    'axes.unicode_minus': True,
    'lines.linewidth': 1.3,
    'lines.solid_capstyle': 'round',
    'savefig.facecolor': 'white',
    'figure.facecolor': 'white',
    'hatch.linewidth': 0.8,
})
INK = '#111111'
PX_PER_IN = 100  # final pixels per inch: 11 pt text ends up ~15 px tall

__all__ = ['tex', 'plt', 'np', 'INK', 'canvas', 'save', 'xy_axes', 'plot_fn', 'guide', 'dot', 'label',
           'arrow', 'solid', 'bbt', 'target_width', 'subject_of', 'INFO']


def tex(s):
    """Math-mode string with textbook primes: A' -> A′ (mathtext's ' is tiny)."""
    return s.replace("'", r'\prime ')


def subject_of(fid):
    return INFO[fid]['subject']


def target_width(fid):
    return INFO[fid]['width']


def canvas(fid, aspect=None, width_px=None, axis=False):
    """Figure sized so the final PNG keeps ~100 px per inch at the app's width.

    aspect = height / width (default: the original figure's aspect, so it
    takes the same room on screen). Returns (fig, ax); the axes fill the
    figure and are switched off unless axis=True.
    """
    aspect = aspect or INFO[fid]['aspect']
    w = (width_px or target_width(fid)) / PX_PER_IN
    w = max(w, 1.0)
    fig = plt.figure(figsize=(w, w * aspect))
    ax = fig.add_axes([0, 0, 1, 1])
    if not axis:
        ax.set_axis_off()
    return fig, ax


def save(fig, fid, width=None, pad=0.06, colors=None):
    """Render at 300 dpi, trim, resize to the target width, write the PNG."""
    os.makedirs(os.path.join(WORK, 'raw'), exist_ok=True)
    raw = os.path.join(WORK, 'raw', f'{fid}.png')
    fig.savefig(raw, dpi=300, bbox_inches='tight', pad_inches=pad)
    plt.close(fig)
    return finalize(fid, raw, width=width, colors=colors)


def finalize(fid, raw, width=None, colors=None, margin=0.02):
    """Trim white borders (keep a small margin), resize, palette-compress."""
    im = Image.open(raw).convert('RGB')
    # bounding box of non-white pixels
    gray = im.convert('L').point(lambda v: 255 if v < 250 else 0)
    box = gray.getbbox()
    if box:
        m = int(max(im.size) * margin) + 2
        box = (max(0, box[0] - m), max(0, box[1] - m), min(im.width, box[2] + m), min(im.height, box[3] + m))
        im = im.crop(box)
    w = width or target_width(fid)
    if im.width != w:
        im = im.resize((w, max(1, round(im.height * w / im.width))), Image.LANCZOS)
    n = colors or 128
    out_dir = os.path.join(OUT, subject_of(fid))
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f'{fid}.png')
    im.quantize(colors=n, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dest, optimize=True)
    return dest


# ---------------------------------------------------------------- 2D graphs

def xy_axes(ax, xlim, ylim, xticks=(), yticks=(), xticklabels=None, yticklabels=None,
            origin='O', xname='x', yname='y', grid=False, aspect='equal', fontsize=11,
            tick_len=0.015, label_offset=None, ticklabel_pos=None):
    """Textbook-style axes through the origin with arrow heads.

    xticks / yticks: positions with a tick mark and a label (label = number
    unless xticklabels/yticklabels give LaTeX strings). grid=True draws a
    light unit grid. Returns ax.
    """
    (x0, x1), (y0, y1) = xlim, ylim
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    if aspect:
        ax.set_aspect(aspect)
    ax.set_axis_off()
    if grid:
        for gx in np.arange(np.ceil(x0), np.floor(x1) + 1):
            ax.plot([gx, gx], [y0, y1], color='#cccccc', lw=0.6, zorder=0)
        for gy in np.arange(np.ceil(y0), np.floor(y1) + 1):
            ax.plot([x0, x1], [gy, gy], color='#cccccc', lw=0.6, zorder=0)
    ap = dict(arrowstyle='-|>,head_length=0.5,head_width=0.22', color=INK, lw=1.0, shrinkA=0, shrinkB=0)
    ax.annotate('', xy=(x1, 0), xytext=(x0, 0), arrowprops=ap, zorder=3)
    ax.annotate('', xy=(0, y1), xytext=(0, y0), arrowprops=ap, zorder=3)
    span = max(x1 - x0, y1 - y0)
    off = label_offset or span * 0.035
    if xname:
        ax.text(x1 - off * 0.3, -off * 1.2, f'${xname}$', ha='right', va='top', fontsize=fontsize + 1)
    if yname:
        ax.text(off * 0.8, y1 - off * 0.3, f'${yname}$', ha='left', va='top', fontsize=fontsize + 1)
    if origin:
        ax.text(-off * 0.6, -off * 0.6, f'${origin}$', ha='right', va='top', fontsize=fontsize)
    tl = span * tick_len
    for i, t in enumerate(xticks):
        ax.plot([t, t], [-tl, tl], color=INK, lw=1.0)
        s = xticklabels[i] if xticklabels else _num(t)
        ax.text(t, -off * 0.9, f'${s}$', ha='center', va='top', fontsize=fontsize)
    for i, t in enumerate(yticks):
        ax.plot([-tl, tl], [t, t], color=INK, lw=1.0)
        s = yticklabels[i] if yticklabels else _num(t)
        ax.text(-off * 0.7, t, f'${s}$', ha='right', va='center', fontsize=fontsize)
    return ax


def _num(v):
    if float(v).is_integer():
        v = int(v)
    return str(v).replace('-', '-')


def plot_fn(ax, f, a, b, n=800, color=INK, lw=1.5, ylim=None, **kw):
    """Plot y=f(x) on [a, b]; points outside ylim are masked (for asymptotes)."""
    xs = np.linspace(a, b, n)
    with np.errstate(all='ignore'):
        ys = np.array([f(x) for x in xs], dtype=float)
    if ylim is None:
        ylim = ax.get_ylim()
    ys[(ys < ylim[0] - 0.5) | (ys > ylim[1] + 0.5)] = np.nan
    return ax.plot(xs, ys, color=color, lw=lw, **kw)


def guide(ax, x, y, color=INK, lw=0.9):
    """Dashed projections of (x, y) onto both axes."""
    ax.plot([x, x], [0, y], ls=(0, (3, 2)), color=color, lw=lw)
    ax.plot([0, x], [y, y], ls=(0, (3, 2)), color=color, lw=lw)


def dot(ax, x, y, r=3.2, color=INK, hollow=False):
    ax.plot([x], [y], 'o', ms=r, color=color, mfc='white' if hollow else color, zorder=5)


def label(ax, x, y, s, ha='center', va='center', size=11, **kw):
    """Text in math italics when wrapped in $…$; plain otherwise."""
    return ax.text(x, y, s, ha=ha, va=va, fontsize=size, **kw)


def arrow(ax, x0, y0, x1, y1, color=INK, lw=1.1, head=0.45, **kw):
    ap = dict(arrowstyle=f'-|>,head_length={head},head_width={head * 0.45}', color=color, lw=lw,
              shrinkA=0, shrinkB=0)
    ap.update(kw)
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=ap)


# ---------------------------------------------------------------- solid geometry

def solid(ax, pts, edges='', dashed='', labels=None, dots=False, size=12, lw=1.3, off=0.06,
          color=INK):
    """Wireframe of a solid in a 2D projection.

    pts: {'A': (x, y), "A'": (x, y), …}. edges / dashed: space separated
    pairs written as 'A-B' (use '-' between names, since names may have ').
    labels: {'A': 'sw'} compass direction for a label, or None to place every
    label away from the centroid. Returns ax.
    """
    ax.set_aspect('equal')
    ax.set_axis_off()

    def pairs(s):
        return [p.split('-') for p in s.split()] if s else []

    for a, b in pairs(edges):
        ax.plot(*zip(pts[a], pts[b]), color=color, lw=lw, solid_capstyle='round')
    for a, b in pairs(dashed):
        ax.plot(*zip(pts[a], pts[b]), color=color, lw=lw * 0.85, ls=(0, (4, 3)))
    xs = np.array([p[0] for p in pts.values()])
    ys = np.array([p[1] for p in pts.values()])
    cx, cy = xs.mean(), ys.mean()
    span = max(np.ptp(xs), np.ptp(ys)) or 1
    d = span * off
    comp = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0), 'ne': (.75, .75), 'nw': (-.75, .75),
            'se': (.75, -.75), 'sw': (-.75, -.75)}
    for name, (x, y) in pts.items():
        if labels is not None and name not in labels:
            continue
        where = (labels or {}).get(name)
        if where:
            ux, uy = comp[where]
        else:
            vx, vy = x - cx, y - cy
            n = np.hypot(vx, vy) or 1
            ux, uy = vx / n, vy / n
        ax.text(x + ux * d, y + uy * d, f'${tex(name)}$', ha='center', va='center', fontsize=size)
        if dots:
            dot(ax, x, y, r=2.6)
    ax.margins(0.08)
    return ax


# ---------------------------------------------------------------- variation tables

def bbt(fid, xs, signs, ys=None, names=('x', "f'(x)", 'f(x)'), col0=0.55, step=None, row_h=(0.3, 0.3, 0.85),
        size=12.5, border=False, width_px=None):
    """Bảng biến thiên / bảng xét dấu.

    xs: column values as LaTeX, e.g. ['-\\infty', '-1', '1', '+\\infty'].
    signs: 2*len(xs)-1 entries on the grid "x0, gap, x1, gap, …":
           at an x position '0', '||' (undefined: double bar through the
           lower rows) or ''; in a gap '+', '-' or ''.
    ys: list of (pos, level, text) or (pos, level, text, side) where pos is
        the grid index (even = under an x, odd = in a gap), level is
        'top' | 'bot' | 'mid', side 'L' / 'R' places the value just left or
        right of a '||' column. Consecutive values are joined by arrows,
        except across a '||'. ys=None draws only the first two rows.
    names: labels of the rows (LaTeX).
    Returns (fig, ax, X) where X(pos) gives the x coordinate of a grid
    position, for extra decorations.
    """
    n = len(xs)
    assert len(signs) == 2 * n - 1, 'signs must have 2*len(xs)-1 entries'
    rows = 3 if ys is not None else 2
    W = width_px or target_width(fid)
    k = min(1.35, max(0.85, W / 500))  # bigger tables get bigger text, like the originals
    size = size * k
    hs = [h * k for h in row_h[:rows]]
    total_h = sum(hs)
    col0 = col0 * k
    inner = 0.35 * k
    width = W / PX_PER_IN
    step = step or (width - col0 - 2 * inner) / (2 * n - 2)
    fig = plt.figure(figsize=(width, total_h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_xlim(0, width)
    ax.set_ylim(0, total_h)

    def X(p):
        return col0 + inner + p * step

    tops = [total_h]
    for h in hs:
        tops.append(tops[-1] - h)
    # grid lines
    lw = 1.0
    ax.plot([col0, col0], [0, total_h], color=INK, lw=lw)
    for t in tops[1:-1]:
        ax.plot([0, width], [t, t], color=INK, lw=lw)
    if border:
        ax.plot([0, width, width, 0, 0], [0, 0, total_h, total_h, 0], color=INK, lw=lw)
    # row names
    for r in range(rows):
        cy = (tops[r] + tops[r + 1]) / 2
        ax.text(col0 / 2, cy, f'${tex(names[r])}$', ha='center', va='center', fontsize=size)
    # x row
    cy0 = (tops[0] + tops[1]) / 2
    for i, v in enumerate(xs):
        ax.text(X(2 * i), cy0, f'${v}$', ha='center', va='center', fontsize=size)
    # sign row
    cy1 = (tops[1] + tops[2]) / 2
    bars = []
    for p, s in enumerate(signs):
        if s == '||':
            bars.append(p)
            for dx in (-0.025, 0.025):
                ax.plot([X(p) + dx * k] * 2, [0, tops[1]], color=INK, lw=0.9)
        elif s:
            txt = {'-': '$-$', '+': '$+$', '0': '$0$'}.get(s, f'${s}$')
            ax.text(X(p), cy1, txt, ha='center', va='center', fontsize=size)
    # value row
    if ys is not None:
        y_lo, y_hi = tops[3], tops[2]
        lev = {'top': y_hi - 0.17 * k, 'bot': y_lo + 0.17 * k, 'mid': (y_hi + y_lo) / 2}
        pts = []
        for item in ys:
            p, level, text = item[:3]
            side = item[3] if len(item) > 3 else None
            x = X(p) + (-0.1 * k if side == 'L' else 0.1 * k if side == 'R' else 0)
            ha = 'right' if side == 'L' else 'left' if side == 'R' else 'center'
            ax.text(x, lev[level], f'${text}$', ha=ha, va='center', fontsize=size)
            pts.append((p, x, lev[level], side, ha))
        def eff(p, side):
            return p - 0.25 if side == 'L' else p + 0.25 if side == 'R' else p

        for (p0, x0, y0, s0, h0), (p1, x1, y1, s1, h1) in zip(pts, pts[1:]):
            a, b = eff(p0, s0), eff(p1, s1)
            if any(a < q < b for q in bars):
                continue  # never draw an arrow across a double bar
            ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                        arrowprops=dict(arrowstyle='-|>,head_length=0.45,head_width=0.18', color=INK, lw=0.9,
                                        shrinkA=9, shrinkB=9))
    return fig, ax, X
