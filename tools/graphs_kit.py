"""Helpers for the function-graph / chart figures (built on drawkit).

A graph is laid out in the original's pixel frame so the redraw takes the same
room: win(fid, origin_px, unit_px) makes a canvas whose data window covers the
whole original image, with (0, 0) at origin_px and unit_px pixels per unit.

    from graphs_kit import *
    fig, ax = win('img024', (167, 189), (53.5, 54))
    axes(ax, (-3.0, 3.0), (-2.65, 2.9))
    xt(ax, [-2, -1, 1, 2], style='dot'); yt(ax, [-2, -1, 1, 2], style='dot')
    curve(ax, lambda x: x**4 - 2*x**2 - 1, -2, 2)
    save(fig, 'img024')
"""
import json
import os

from drawkit import *  # noqa: F401,F403
from drawkit import INFO, INK, OUT, WORK, canvas, plt, np, tex, target_width, subject_of  # noqa: F401
from drawkit import save as trim_save  # noqa: F401
from PIL import Image

_META = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                    'work', 'meta.json'), encoding='utf-8'))
FS = 12  # default label size (pt)
DASH = (0, (4, 2.5))

__all__ = ['setfs', 'clip', 'win', 'axes', 'xt', 'yt', 'curve', 'seg', 'dash', 'vline', 'hline', 'T', 'pt', 'poly',
           'hermite', 'fill_between', 'FS', 'DASH', 'save', 'trim_save', 'np', 'plt', 'INK', 'tex', 'canvas', 'orig_size',
           'mn']


def save(fig, fid, colors=128):
    """Render the whole canvas (no trimming, so the frame and its white margins
    match the original's layout), resize to the app width, palette-compress."""
    os.makedirs(os.path.join(WORK, 'raw'), exist_ok=True)
    raw = os.path.join(WORK, 'raw', f'{fid}.png')
    fig.savefig(raw, dpi=300)
    plt.close(fig)
    im = Image.open(raw).convert('RGB')
    w = target_width(fid)
    im = im.resize((w, max(1, round(im.height * w / im.width))), Image.LANCZOS)
    out_dir = os.path.join(OUT, subject_of(fid))
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f'{fid}.png')
    im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dest, optimize=True)
    return dest


def setfs(n):
    """Default label size (pt) for this figure."""
    global FS
    FS = n


def orig_size(fid):
    return _META[fid]['orig_size']


def mn(v):
    """Number as math text with a real minus sign; v may already be a string."""
    if isinstance(v, str):
        return v
    if float(v).is_integer():
        v = int(v)
    return str(v)


def win(fid, origin, unit, size=None, aspect=None):
    """Canvas whose data window is the original image (pixel frame).

    origin: pixel (x, y) of the point (0, 0) in the original.
    unit: pixels per unit (ux, uy) or a single number.
    size: (W, H) of the frame in original pixels (default: the original size).
    """
    W, H = size or orig_size(fid)
    ux, uy = (unit, unit) if np.isscalar(unit) else unit
    ox, oy = origin
    fig, ax = canvas(fid, aspect=aspect or H / W)
    ax.set_xlim(-ox / ux, (W - ox) / ux)
    ax.set_ylim(-(H - oy) / uy, oy / uy)
    ax.set_aspect('auto')
    ax.set_axis_off()
    ax._px = (ox, oy, ux, uy)
    return fig, ax


def pt(ax, x, y):
    """Original pixel (x, y) -> data coordinates."""
    ox, oy, ux, uy = ax._px
    return (x - ox) / ux, (oy - y) / uy


def axes(ax, xr, yr, xname='x', yname='y', origin='O', opos=(-4, -3), lw=0.9, head=6, fs=None,
         xname_pos=None, yname_pos=None, xy=(0, 0), color=INK):
    """Axes with arrow heads: x axis on y=xy[1] over xr, y axis on x=xy[0] over yr.

    Labels are placed with offsets in points: xname below the arrow tip, yname
    left of the arrow tip, O at the origin (opos offset from origin).
    xname_pos / yname_pos: (dx, dy) offsets in points relative to the arrow tip,
    or data (x, y) when given as ('data', x, y).
    """
    fs = fs or FS
    X0, Y0 = xy
    hl, hw = head, head * 0.42
    for (a, b), horiz in ((xr, True), (yr, False)):
        if a is None:
            continue
        p0, p1 = ((a, Y0), (b, Y0)) if horiz else ((X0, a), (X0, b))
        ax.annotate('', xy=p1, xytext=p0, zorder=3,
                    arrowprops=dict(arrowstyle=f'-|>,head_length={hl / 10:.2f},head_width={hw / 10:.2f}',
                                    color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=10))
    if xname and xr[0] is not None:
        _place(ax, (xr[1], Y0), f'${xname}$', xname_pos or (-2, -5), 'right', 'top', fs + 1)
    if yname and yr[0] is not None:
        _place(ax, (X0, yr[1]), f'${yname}$', yname_pos or (-6, -1), 'right', 'top', fs + 1)
    if origin:
        _place(ax, (X0, Y0), f'${origin}$', opos, 'right', 'top', fs)


def _place(ax, xy, s, pos, ha, va, fs, **kw):
    if pos and pos[0] == 'data':
        return ax.text(pos[1], pos[2], s, ha=kw.pop('ha2', 'center'), va=kw.pop('va2', 'center'), fontsize=fs,
                       **kw)
    return ax.annotate(s, xy, xytext=pos, textcoords='offset points', ha=ha, va=va, fontsize=fs, **kw)


_POS = {  # where a tick label sits: offset (pt) and alignment
    'b': ((0, -4), 'center', 'top'), 'a': ((0, 4), 'center', 'bottom'),
    'bl': ((-2, -4), 'right', 'top'), 'br': ((2, -4), 'left', 'top'),
    'al': ((-2, 4), 'right', 'bottom'), 'ar': ((2, 4), 'left', 'bottom'),
    'l': ((-4, 0), 'right', 'center'), 'r': ((4, 0), 'left', 'center'),
    'lb': ((-4, -2), 'right', 'top'), 'lt': ((-4, 2), 'right', 'bottom'),
    'rb': ((4, -2), 'left', 'top'), 'rt': ((4, 2), 'left', 'bottom'),
}


def _tick(ax, horiz, vals, labels, pos, style, size, fs, dxy, Y0, lw, bg=False):
    fs = fs or FS
    vals = list(np.atleast_1d(vals))
    labels = labels if labels is not None else [None] * len(vals)
    if isinstance(labels, str):
        labels = [labels]
    if isinstance(pos, str) or pos is None:
        pos = [pos] * len(vals)
    for v, s, p in zip(vals, labels, pos):
        xy = (v, Y0) if horiz else (Y0, v)
        if style == 'dot':
            ax.plot(*xy, 'o', ms=size or 2.6, color=INK, zorder=6, mec='none')
        elif style == 'line':
            ax.plot(*xy, marker='|' if horiz else '_', ms=(size or 3.0) * 2, mew=lw, color=INK, zorder=6)
        if s == '':
            continue
        txt = f'${mn(v) if s is None else s}$'
        p = p or ('b' if horiz else 'l')
        if isinstance(p, tuple):
            if p[0] == 'data':
                ax.text(p[1], p[2], txt, ha='center', va='center', fontsize=fs)
                continue
            off, ha, va = p[:2], (p[2] if len(p) > 2 else 'center'), (p[3] if len(p) > 3 else 'center')
        else:
            off, ha, va = _POS[p]
        off = (off[0] + dxy[0], off[1] + dxy[1])
        ax.annotate(txt, xy, xytext=off, textcoords='offset points', ha=ha, va=va, fontsize=fs, zorder=7,
                    bbox=dict(fc='white', ec='none', pad=0.3) if bg else None)


def xt(ax, vals, labels=None, pos='b', style='line', size=None, fs=None, d=(0, 0), y0=0, lw=0.9, bg=False):
    """Ticks/labels on the x axis. labels: list of LaTeX strings ('' = no label).
    pos: key of _POS, ('data', x, y), or (dx, dy, ha, va) in points; one per value or shared.
    style: 'dot' | 'line' | None."""
    _tick(ax, True, vals, labels, pos, style, size, fs, d, y0, lw, bg)


def yt(ax, vals, labels=None, pos='l', style='line', size=None, fs=None, d=(0, 0), x0=0, lw=0.9, bg=False):
    _tick(ax, False, vals, labels, pos, style, size, fs, d, x0, lw, bg)


def clip(ax, artists, box):
    """Clip artists to the data rectangle box=(x0, x1, y0, y1)."""
    from matplotlib.patches import Rectangle
    x0, x1, y0, y1 = box
    r = Rectangle((x0, y0), x1 - x0, y1 - y0, transform=ax.transData, fc='none', ec='none')
    for a in artists:
        a.set_clip_path(r)
    return artists


def curve(ax, f, a, b, n=3000, lw=1.5, color=INK, big=1e3, box=None, **kw):
    """Plot y=f(x) on [a, b] (clipped by the window or box; |y|>big dropped)."""
    xs = np.linspace(a, b, n)
    with np.errstate(all='ignore'):
        ys = np.array([f(x) for x in xs], dtype=float)
    ys[np.abs(ys) > big] = np.nan
    ln = ax.plot(xs, ys, color=color, lw=lw, solid_joinstyle='round', **kw)
    if box:
        clip(ax, ln, box)
    return ln


def seg(ax, pts, lw=1.5, color=INK, **kw):
    pts = np.asarray(pts, dtype=float)
    return ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, **kw)


def dash(ax, pts, lw=0.9, color=INK, ls=DASH, **kw):
    """Dashed polyline through pts [(x, y), …]."""
    pts = np.asarray(pts, dtype=float)
    return ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, ls=ls, **kw)


def vline(ax, x, y0=None, y1=None, lw=1.0, ls='-', color=INK, **kw):
    a, b = ax.get_ylim()
    return ax.plot([x, x], [a if y0 is None else y0, b if y1 is None else y1], color=color, lw=lw, ls=ls, **kw)


def hline(ax, y, x0=None, x1=None, lw=1.0, ls='-', color=INK, **kw):
    a, b = ax.get_xlim()
    return ax.plot([a if x0 is None else x0, b if x1 is None else x1], [y, y], color=color, lw=lw, ls=ls, **kw)


def T(ax, x, y, s, fs=None, ha='center', va='center', bg=False, **kw):
    """Text at data (x, y); bg=True puts it on a white patch (over dashed lines)."""
    if bg:
        kw.setdefault('bbox', dict(fc='white', ec='none', pad=0.3))
        kw.setdefault('zorder', 7)
    return ax.text(x, y, s, ha=ha, va=va, fontsize=fs or FS, **kw)


def poly(cons, deg=None):
    """Polynomial through constraints.

    cons: list of (x, y) value constraints and (x, y, k) meaning f^(k)(x) = y.
    deg: degree (default len(cons) - 1). Least squares if over-determined.
    Returns a callable numpy poly1d.
    """
    deg = len(cons) - 1 if deg is None else deg
    A, rhs = [], []
    for c in cons:
        x, y = c[0], c[1]
        k = c[2] if len(c) > 2 else 0
        row = []
        for p in range(deg, -1, -1):  # highest power first
            if p < k:
                row.append(0.0)
            else:
                coef = 1.0
                for j in range(k):
                    coef *= (p - j)
                row.append(coef * x ** (p - k))
        A.append(row)
        rhs.append(y)
    c, *_ = np.linalg.lstsq(np.array(A), np.array(rhs, dtype=float), rcond=None)
    return np.poly1d(c)


def hermite(xs, ys, ms):
    """Piecewise cubic Hermite through (xs[i], ys[i]) with slopes ms[i]."""
    xs, ys, ms = map(lambda v: np.asarray(v, dtype=float), (xs, ys, ms))

    def f(x):
        i = int(np.clip(np.searchsorted(xs, x) - 1, 0, len(xs) - 2))
        h = xs[i + 1] - xs[i]
        t = (x - xs[i]) / h
        h00 = 2 * t**3 - 3 * t**2 + 1
        h10 = t**3 - 2 * t**2 + t
        h01 = -2 * t**3 + 3 * t**2
        h11 = t**3 - t**2
        return h00 * ys[i] + h10 * h * ms[i] + h01 * ys[i + 1] + h11 * h * ms[i + 1]
    return f


def fill_between(ax, f, a, b, g=lambda x: 0.0, n=600, color='#bdbdbd', hatch=None, lw=0, alpha=1.0, **kw):
    """Shade the region between y=f(x) and y=g(x) for x in [a, b]."""
    xs = np.linspace(a, b, n)
    y1 = np.array([f(x) for x in xs])
    y2 = np.array([g(x) for x in xs])
    if hatch:
        return ax.fill_between(xs, y1, y2, facecolor='none', edgecolor=color, hatch=hatch, lw=lw, **kw)
    return ax.fill_between(xs, y1, y2, facecolor=color, lw=lw, alpha=alpha, **kw)


def grid(ax, xr=None, yr=None, major=1.0, minor=None, cmaj='#d6d6d6', cmin='#eeeeee', lwmaj=0.6, lwmin=0.4):
    """Light graph-paper grid over xr × yr (default: the whole window)."""
    x0, x1 = xr or ax.get_xlim()
    y0, y1 = yr or ax.get_ylim()
    for step, c, lw in ((minor, cmin, lwmin), (major, cmaj, lwmaj)):
        if not step:
            continue
        for gx in np.arange(np.ceil(x0 / step) * step, x1 + 1e-9, step):
            ax.plot([gx, gx], [y0, y1], color=c, lw=lw, zorder=0)
        for gy in np.arange(np.ceil(y0 / step) * step, y1 + 1e-9, step):
            ax.plot([x0, x1], [gy, gy], color=c, lw=lw, zorder=0)


__all__ += ['grid']


def hatch(ax, xy, step, angle=45, lw=0.8, color=INK, aspect=1.0, zorder=1):
    """Hatch the polygon xy [(x, y), …] with parallel lines `step` apart (measured
    along x), at `angle` degrees on screen (aspect = screen units per data y unit /
    per data x unit, so 45° looks like 45°)."""
    from matplotlib.patches import Polygon
    xy = np.asarray(xy, dtype=float)
    poly = Polygon(xy, closed=True, fc='none', ec='none', transform=ax.transData)
    ax.add_patch(poly)
    x0, y0 = xy.min(axis=0)
    x1, y1 = xy.max(axis=0)
    k = np.tan(np.radians(angle)) / aspect  # dy/dx in data units
    span = (y1 - y0) / k if k else 0
    for c in np.arange(x0 - abs(span) - step, x1 + abs(span) + step, step):
        ln, = ax.plot([c, c + (y1 - y0 + 2) / k], [y0 - 1, y1 + 1], color=color, lw=lw, zorder=zorder)
        ln.set_clip_path(poly)
    return poly


def region(f, a, b, g=lambda x: 0.0, n=300):
    """Polygon between y=f(x) (top/bottom) and y=g(x) over [a, b]."""
    xs = np.linspace(a, b, n)
    top = [(x, f(x)) for x in xs]
    bot = [(x, g(x)) for x in xs[::-1]]
    return top + bot


__all__ += ['hatch', 'region']


def pchip(xs, ys):
    """Monotone piecewise-cubic interpolant (Fritsch–Carlson): no overshoot, flat at extrema."""
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    h = np.diff(xs)
    d = np.diff(ys) / h
    m = np.zeros_like(ys)
    for i in range(1, len(xs) - 1):
        if d[i - 1] * d[i] <= 0:
            m[i] = 0.0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    m[0], m[-1] = d[0], d[-1]
    return hermite(xs, ys, m)


__all__ += ['pchip']
