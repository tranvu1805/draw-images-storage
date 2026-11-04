"""Helpers for the variation/sign tables and geometry figures (tables & geometry group).

Tables are laid out in the original figure's pixel frame (x right, y DOWN from the
top), so column positions and row heights can be taken straight from the layout
of the original; the drawing itself is done from scratch.

    from tabgeo_kit import *
    T = Table('img026', hl=[6, 59, 118, 326], vl=145, box=(7, 785), fs=21)
    T.xrow([188, 338, 526, 743], ['-1', '0', '2', '3'])
    T.signs(['', '+', '0', '-', '0', '+', ''])
    T.values([(0, 290, '0'), (2, 136, '5'), (4, 240, '1'), (6, 190, '4')])
    T.save()
"""
import os

import numpy as np
from PIL import Image
from drawkit import plt, tex, INK, save, target_width, INFO, WORK, OUT, subject_of

__all__ = ['Table', 'Geo', 'np', 'plt', 'tex', 'INK', 'save', 'save_fit', 'save_frame', 'arrow3']


def save_frame(fig, fid, colors=128):
    """Save the whole figure frame (the original's pixel frame, so the same layout
    and white space as the original), resized to the target width."""
    os.makedirs(os.path.join(WORK, 'raw'), exist_ok=True)
    raw = os.path.join(WORK, 'raw', f'{fid}.png')
    fig.savefig(raw, dpi=300)
    plt.close(fig)
    im = Image.open(raw).convert('RGB')
    W = target_width(fid)
    im = im.resize((W, max(1, round(im.height * W / im.width))), Image.LANCZOS)
    out_dir = os.path.join(OUT, subject_of(fid))
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f'{fid}.png')
    im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dest, optimize=True)
    return dest


def save_fit(fig, fid, aspect=None, margin=0.03, colors=128):
    """Like drawkit.save, but after trimming the white border the image is padded
    (centred) back to the original's aspect ratio, so the figure takes exactly the
    same room in the app while the drawing itself fills it as much as possible."""
    os.makedirs(os.path.join(WORK, 'raw'), exist_ok=True)
    raw = os.path.join(WORK, 'raw', f'{fid}.png')
    fig.savefig(raw, dpi=300, bbox_inches='tight', pad_inches=0.02)
    plt.close(fig)
    im = Image.open(raw).convert('RGB')
    gray = im.convert('L').point(lambda v: 255 if v < 250 else 0)
    box = gray.getbbox()
    if box:
        im = im.crop(box)
    aspect = aspect or INFO[fid]['aspect']
    m = int(max(im.size) * margin) + 2
    w, h = im.width + 2 * m, im.height + 2 * m
    if h / w < aspect:
        h = round(w * aspect)
    else:
        w = round(h / aspect)
    canvas = Image.new('RGB', (w, h), 'white')
    canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    W = target_width(fid)
    canvas = canvas.resize((W, max(1, round(W * aspect))), Image.LANCZOS)
    out_dir = os.path.join(OUT, subject_of(fid))
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f'{fid}.png')
    canvas.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dest, optimize=True)
    return dest


def _clip(c0, c1, b0, b1):
    """Segment c0->c1 shortened so it starts outside box b0 and ends outside box b1."""
    c0, c1 = np.array(c0, float), np.array(c1, float)
    d = c1 - c0

    def exit_t(c, d, b):
        x0, x1, y0, y1 = b
        ts = []
        for k, (lo, hi) in enumerate(((x0, x1), (y0, y1))):
            if abs(d[k]) > 1e-9:
                for v in (lo, hi):
                    t = (v - c[k]) / d[k]
                    if t > 0:
                        ts.append(t)
        # smallest positive t where we cross a side beyond which we're outside
        best = 0.0
        for t in sorted(ts):
            p = c + t * d
            if x0 - 1e-6 <= p[0] <= x1 + 1e-6 and y0 - 1e-6 <= p[1] <= y1 + 1e-6:
                best = t
                break
        return best

    t0 = exit_t(c0, d, b0)
    t1 = 1 - exit_t(c1, -d, b1)
    return c0 + t0 * d, c0 + t1 * d


class Table:
    """Variation / sign table in the original's pixel frame.

    hl: y of the horizontal rules (top to bottom). The first and last are the
        top and bottom of the table; they are drawn only when box is given
        (box=(x_left, x_right) draws the full outer border).
    rule_x: (x0, x1) extent of the inner horizontal rules (default: box or the
        whole width).
    vl: x of the vertical rule after the names column; it runs from vl_y[0] to
        vl_y[1] (default: the whole table height).
    fs: font size in points (≈ digit height in px of the original × 1.06).
    """

    def __init__(self, fid, hl, vl, box=None, fs=18, W=None, H=None, rule_x=None, vl_y=None, lw=1.0,
                 name_x=None, draw_top=None, draw_bottom=None):
        self.fid = fid
        ow, oh = INFO[fid]['width'], round(INFO[fid]['width'] * INFO[fid]['aspect'])
        self.W, self.H = W or ow, H or oh
        self.fig = plt.figure(figsize=(self.W / 100, self.H / 100))
        ax = self.ax = self.fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()
        ax.set_xlim(0, self.W)
        ax.set_ylim(self.H, 0)
        self.hl, self.vl, self.box, self.fs, self.lw = list(hl), vl, box, fs, lw
        x0, x1 = rule_x or (box if box else (0, self.W))
        self.rx = (x0, x1)
        top, bot = self.hl[0], self.hl[-1]
        draw_top = box is not None if draw_top is None else draw_top
        draw_bottom = box is not None if draw_bottom is None else draw_bottom
        for k, y in enumerate(self.hl):
            if (k == 0 and not draw_top) or (k == len(self.hl) - 1 and not draw_bottom):
                continue
            ax.plot([x0, x1], [y, y], color=INK, lw=lw, solid_capstyle='butt')
        if box:
            ax.plot([box[0], box[0]], [top, bot], color=INK, lw=lw)
            ax.plot([box[1], box[1]], [top, bot], color=INK, lw=lw)
        vy = vl_y or (top, bot)
        ax.plot([vl, vl], vy, color=INK, lw=lw, solid_capstyle='butt')
        self.name_x = name_x or ((box[0] if box else 0) + vl) / 2
        self.cols = []
        self.bars = []
        self.items = []

    # rows -----------------------------------------------------------------
    def row(self, r):
        return self.hl[r], self.hl[r + 1]

    def cy(self, r):
        a, b = self.row(r)
        return (a + b) / 2

    def text(self, x, y, s, ha='center', va='center', fs=None, math=True, **kw):
        return self.ax.text(x, y, f'${s}$' if math else s, ha=ha, va=va, fontsize=fs or self.fs, color=INK, **kw)

    def names(self, names, dy=None, fs=None):
        for r, n in enumerate(names):
            if n is None:
                continue
            self.text(self.name_x, self.cy(r) + (dy[r] if dy else 0), tex(n), fs=fs or self.fs * 1.12)

    def X(self, p):
        """x of a grid position: even p = under an x value, odd = midway in the gap."""
        if p % 2 == 0:
            return self.cols[p // 2]
        return (self.cols[p // 2] + self.cols[p // 2 + 1]) / 2

    def xrow(self, xs, vals, dy=0, ha=None):
        """x values; xs = pixel x of each column (centre of the value)."""
        self.cols = list(xs)
        for i, (x, v) in enumerate(zip(xs, vals)):
            h = ha[i] if ha else 'center'
            self.text(x, self.cy(0) + dy, v, ha=h)

    def signs(self, signs, row=1, dy=0, gaps=None, bar_y=None, bar_dx=2.5):
        """signs on the 2n-1 grid. '||' = double bar through all lower rows,
        '||s' = double bar only through this row, '||t' = a short ‖ glyph.
        gaps: optional explicit x for odd positions (when the sign is not midway).
        bar_y: (y0, y1) explicit vertical extent of the bars."""
        y = self.cy(row) + dy
        for p, s in enumerate(signs):
            x = self.X(p) if not (gaps and p % 2 and gaps.get(p) is not None) else gaps[p]
            if s in ('||', '||s'):
                y0 = self.hl[row]
                y1 = self.hl[-1] if s == '||' else self.hl[row + 1]
                if bar_y:
                    y0, y1 = bar_y
                for dx in (-bar_dx, bar_dx):
                    self.ax.plot([x + dx] * 2, [y0, y1], color=INK, lw=self.lw, solid_capstyle='butt')
                if s == '||':
                    self.bars.append(x)
            elif s == '|':
                y0, y1 = bar_y or (self.hl[row], self.hl[-1])
                self.ax.plot([x] * 2, [y0, y1], color=INK, lw=self.lw * 2.2, solid_capstyle='butt')
                self.bars.append(x)
            elif s == '||t':
                self.text(x, y, r'\Vert')
            elif s:
                txt = {'-': '-', '+': '+', '0': '0'}.get(s, s)
                self.text(x, y, txt)

    def values(self, vals, arrows=True, pad=5, lw=1.1, head=None, skip=(), fs=None):
        """vals: (p, y, text[, dx[, ha]]). p = grid position (x = X(p) + dx), y = pixel y.
        Consecutive values are joined by arrows (except across a '||' bar and
        for index pairs listed in skip)."""
        ts = []
        r = self.fig.canvas.get_renderer()
        for v in vals:
            p, y, s = v[:3]
            dx = v[3] if len(v) > 3 else 0
            ha = v[4] if len(v) > 4 else 'center'
            x = (self.X(p) if p is not None else 0) + dx
            t = self.text(x, y, s, ha=ha, fs=fs)
            ts.append((x, y, t))
        boxes = []
        inv = self.ax.transData.inverted()
        for x, y, t in ts:
            bb = t.get_window_extent(renderer=r)
            (ax0, ay0), (ax1, ay1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
            xa, xb = sorted((ax0, ax1))
            ya, yb = sorted((ay0, ay1))
            boxes.append(((xa + xb) / 2, (ya + yb) / 2, (xa - pad, xb + pad, ya - pad, yb + pad)))
        if not arrows:
            return boxes
        for k in range(len(boxes) - 1):
            if k in skip:
                continue
            (cx0, cy0, b0), (cx1, cy1, b1) = boxes[k], boxes[k + 1]
            if any(min(cx0, cx1) < bx < max(cx0, cx1) for bx in self.bars):
                continue
            p0, p1 = _clip((cx0, cy0), (cx1, cy1), b0, b1)
            self.arrow(p0, p1, lw=lw, head=head or min(9, 0.5 * self.fs))
        return boxes

    def arrow(self, p0, p1, lw=1.0, head=9):
        self.ax.annotate('', xy=tuple(p1), xytext=tuple(p0),
                         arrowprops=dict(arrowstyle='-|>,head_length=0.55,head_width=0.22', color=INK, lw=lw,
                                         shrinkA=0, shrinkB=0, mutation_scale=head * 1.6))

    def hatch(self, x0, x1, y0, y1, density='/////'):
        from matplotlib.patches import Rectangle
        self.ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, hatch=density, lw=self.lw,
                                    edgecolor=INK))

    def save(self, fit=False, **kw):
        return save_fit(self.fig, self.fid, **kw) if fit else save_frame(self.fig, self.fid, **kw)


# ---------------------------------------------------------------- geometry in pixel frame

class Geo:
    """Line drawing in the original's pixel frame (y down), for geometry figures.

    P: {'A': (x, y), …} pixel coordinates read off the original's layout.
    """

    def __init__(self, fid, P=None, W=None, H=None, fs=13, lw=1.2):
        self.fid = fid
        ow, oh = INFO[fid]['width'], round(INFO[fid]['width'] * INFO[fid]['aspect'])
        self.W, self.H = W or ow, H or oh
        self.fig = plt.figure(figsize=(self.W / 100, self.H / 100))
        ax = self.ax = self.fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()
        ax.set_xlim(0, self.W)
        ax.set_ylim(self.H, 0)
        ax.set_aspect('equal')
        self.P = dict(P or {})
        self.fs, self.lw = fs, lw

    def p(self, k):
        return np.array(self.P[k], float) if isinstance(k, str) else np.array(k, float)

    def seg(self, a, b, dashed=False, lw=None, color=INK, **kw):
        a, b = self.p(a), self.p(b)
        if dashed == 'dot':
            self.ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=(lw or self.lw) * 1.5, ls=(0, (0.01, 2.6)),
                         dash_capstyle='round', **kw)
            return
        ls = (0, getattr(self, 'dash', (4, 3))) if dashed is True else (dashed or '-')
        self.ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=(lw or self.lw) * (0.85 if dashed else 1),
                     ls=ls, solid_capstyle='round', **kw)

    def spline(self, pts, n=24, closed=False):
        """Points of a Catmull-Rom spline through pts (no drawing)."""
        P = [self.p(q) for q in pts]
        if closed:
            P = [P[-1]] + P + [P[0], P[1]]
        else:
            P = [2 * P[0] - P[1]] + P + [2 * P[-1] - P[-2]]
        out = []
        for i in range(1, len(P) - 2):
            p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
            for t in np.linspace(0, 1, n, endpoint=False):
                out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2 +
                                  (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
        out.append(P[-2])
        return np.array(out)

    def curve(self, pts, dashed=False, lw=None, color=INK, n=24, closed=False, **kw):
        """Smooth Catmull-Rom curve through the given points (names or (x, y))."""
        P = [self.p(q) for q in pts]
        if closed:
            P = [P[-1]] + P + [P[0], P[1]]
        else:
            P = [2 * P[0] - P[1]] + P + [2 * P[-1] - P[-2]]
        out = []
        for i in range(1, len(P) - 2):
            p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
            for t in np.linspace(0, 1, n, endpoint=False):
                out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2 +
                                  (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
        out.append(P[-2])
        out = np.array(out)
        if dashed == 'dot':
            ls, lw_ = (0, (0.01, 2.6)), (lw or self.lw) * 1.5
        elif dashed:
            ls, lw_ = (0, getattr(self, 'dash', (4, 3))), (lw or self.lw) * 0.85
        else:
            ls, lw_ = '-', lw or self.lw
        self.ax.plot(out[:, 0], out[:, 1], color=color, lw=lw_, ls=ls, solid_capstyle='round',
                     dash_capstyle='round' if dashed == 'dot' else 'butt', **kw)
        return out

    def path(self, xy, dashed=False, lw=None, color=INK, **kw):
        """Polyline through an (N, 2) array."""
        xy = np.asarray(xy, float)
        ls = (0, getattr(self, 'dash', (4, 3))) if dashed else '-'
        self.ax.plot(xy[:, 0], xy[:, 1], color=color, lw=(lw or self.lw) * (0.85 if dashed else 1), ls=ls,
                     solid_capstyle='round', **kw)

    def edges(self, s, dashed=False, **kw):
        for pr in s.split():
            a, b = pr.split('-')
            self.seg(a, b, dashed=dashed, **kw)

    def poly(self, names, dashed=False, closed=True, **kw):
        ns = names.split() if isinstance(names, str) else names
        for a, b in zip(ns, ns[1:] + ([ns[0]] if closed else [])):
            self.seg(a, b, dashed=dashed, **kw)

    def lab(self, name, where=None, d=10, text=None, fs=None, **kw):
        """Label point `name` (math italic) offset d px towards compass `where` or an angle in degrees."""
        comp = {'n': 90, 's': 270, 'e': 0, 'w': 180, 'ne': 45, 'nw': 135, 'se': 315, 'sw': 225,
                'nne': 67, 'nnw': 113, 'ene': 22, 'wnw': 158, 'ese': 338, 'wsw': 202, 'sse': 293, 'ssw': 247}
        x, y = self.p(name)
        if where is None:
            ang = 90
        elif isinstance(where, str):
            ang = comp[where]
        else:
            ang = where
        r = np.radians(ang)
        s = text if text is not None else f'${tex(name)}$'
        self.ax.text(x + d * np.cos(r), y - d * np.sin(r), s, ha='center', va='center', fontsize=fs or self.fs,
                     color=INK, **kw)

    def labs(self, spec, d=10, **kw):
        """spec: {'A': 'sw', …} (or {'A': ('sw', 14)} with its own distance)."""
        for k, w in spec.items():
            if isinstance(w, tuple):
                self.lab(k, w[0], d=w[1], **kw)
            else:
                self.lab(k, w, d=d, **kw)

    def text(self, x, y, s, fs=None, ha='center', va='center', color=INK, **kw):
        return self.ax.text(x, y, s, ha=ha, va=va, fontsize=fs or self.fs, color=color, **kw)

    def dot(self, name, r=3.0, hollow=False):
        x, y = self.p(name)
        self.ax.plot([x], [y], 'o', ms=r, color=INK, mfc='white' if hollow else INK, zorder=5)

    def head(self, a, b, L=11, w=4.2, color=INK, at=1.0):
        """Filled arrow head pointing a->b with its tip at a + at*(b-a)."""
        from matplotlib.patches import Polygon
        a, b = self.p(a), self.p(b)
        u = (b - a) / np.linalg.norm(b - a)
        n = np.array([-u[1], u[0]])
        tip = a + (b - a) * at
        base = tip - u * L
        self.ax.add_patch(Polygon([tip, base + n * w, base - n * w], closed=True, fc=color, ec=color, lw=0.6,
                                  zorder=4))

    def vec(self, a, b, dashed=False, lw=None, L=11, w=4.2, color=INK, at=1.0):
        """Vector a->b: a segment (dashed if asked) with a filled head at b (or at a+at*(b-a))."""
        a_, b_ = self.p(a), self.p(b)
        u = (b_ - a_) / np.linalg.norm(b_ - a_)
        end = a_ + (b_ - a_) * at - u * L * 0.6
        self.seg(a_, end if at == 1.0 else b_, dashed=dashed, lw=lw, color=color)
        self.head(a_, b_, L=L, w=w, color=color, at=at)

    def mid(self, a, b, t=0.5):
        return self.p(a) * (1 - t) + self.p(b) * t

    def right_angle(self, o, a, b, s=8, lw=0.9):
        o, a, b = self.p(o), self.p(a), self.p(b)
        u = (a - o) / np.linalg.norm(a - o) * s
        v = (b - o) / np.linalg.norm(b - o) * s
        pts = np.array([o + u, o + u + v, o + v])
        self.ax.plot(pts[:, 0], pts[:, 1], color=INK, lw=lw)

    def save(self, fit=False, **kw):
        return save_fit(self.fig, self.fid, **kw) if fit else save_frame(self.fig, self.fid, **kw)


def arrow3(ax, p0, p1, lw=1.2, head=10, color=INK):
    ax.annotate('', xy=tuple(p1), xytext=tuple(p0),
                arrowprops=dict(arrowstyle='-|>,head_length=0.6,head_width=0.24', color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=head * 1.6))
