"""Helpers for the biology pedigrees / diagrams (and other line-art figures).

All coordinates are in the ORIGINAL image's pixel space, read off the
original: x to the right, y DOWN. Sizes (line widths, fonts, radii) are in
original pixels too, so a figure can be laid out with the same proportions.

    from bio_kit import *
    b = Board('img112')                       # canvas = original size, y down
    b.person('1', 167, 16, 'm', s=12)         # square, half side 12
    b.person('2', 223, 16, 'f', r=12)         # circle
    b.person('6', 296, 100, 'm', 'k')         # filled black
    mx = b.mate('1', '2')                     # marriage line, returns its middle x
    b.kids(mx, 16, 64, ['3', '4', '6'])       # drop, sibship bar at y=64, kid lines
    b.text(126, 19, '1')
    b.save()

Patterns (pat=, space separated, combinable):
    'k'            black fill        '#b87a56' / 'gray' / any colour: solid fill
    'diag' 'adiag' '/' or '\\' hatch lines   'vl' 'hl'  vertical / horizontal lines
    'grid'         vl + hl           'xhatch'  diag + adiag
    'check'        fine checkerboard 'dots'    dotted  'wave'  wavy lines  'dash'  short dashes
    'plus'         + cross to edges  'x'       X cross to corners
    'bs' 'fs'      one thick diagonal (\\ or /)
    'vdiv' 'hdiv'  single centre divider line
    'strike'       horizontal line through the centre, sticking out both sides
    'half-l' 'half-r' 'half-t' 'half-b'  half filled black
    Pattern options: sp= (line spacing, px), pc= (pattern colour), plw= (pattern line width)

Also: line / text / arrow / rect, chemistry helpers bond (single, double,
ring-style double), wedge, ring (Kekulé hexagon), extent (text width, to
place arrows after text), keep_canvas (keep the original's margins for
small icons).
"""
import json
import os

import drawkit as _dk
from drawkit import *  # noqa: F401,F403
from matplotlib.patches import Rectangle, Ellipse, Polygon, Circle  # noqa: F401

META = json.load(open(os.path.join(_dk.WORK, 'meta.json'), encoding='utf-8'))

__all__ = ['Board', 'META', 'INK', 'np', 'plt', 'tex', 'Rectangle', 'Ellipse', 'Polygon', 'Circle']


class Board:
    def __init__(self, fid, size=None, lw=1.2, font=13, r=10):
        W, H = size or META[fid]['orig_size']
        self.fid, self.W, self.H = fid, W, H
        self.fig, self.ax = canvas(fid, aspect=H / W)
        self.ax.set_xlim(0, W)
        self.ax.set_ylim(H, 0)
        self.k = self.fig.get_size_inches()[0] * 72 / W  # points per unit (canvas() is >= 1 inch wide)
        self.lw, self.font, self.r = lw, font, r
        self.people = {}

    # ------------------------------------------------------------ primitives
    def pt(self, px):
        return px * self.k

    def line(self, *pts, lw=None, color=INK, ls='-', z=2, cap='butt', **kw):
        xs, ys = zip(*pts)
        return self.ax.plot(xs, ys, color=color, lw=self.pt(lw or self.lw), ls=ls, zorder=z,
                            solid_capstyle=cap, solid_joinstyle='miter', dash_capstyle='butt', **kw)[0]

    def text(self, x, y, s, size=None, ha='center', va='center', color=INK, weight='normal',
             style='normal', family=None, **kw):
        kw = dict(kw)
        if family:
            kw['family'] = family
        return self.ax.text(x, y, s, fontsize=self.pt(size or self.font), ha=ha, va=va, color=color,
                            fontweight=weight, fontstyle=style, zorder=6, **kw)

    def extent(self, t):
        """(x0, x1) of a text object in data coordinates."""
        bb = t.get_window_extent(renderer=self.fig.canvas.get_renderer())
        inv = self.ax.transData.inverted()
        (xa, _), (xb, _) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        return min(xa, xb), max(xa, xb)

    def arrow(self, x0, y0, x1, y1, lw=None, color=INK, head=8, width=None, style='-|>', z=3):
        """Arrow from (x0,y0) to (x1,y1); head length / half width in px."""
        w = width or head * 0.4
        ap = dict(arrowstyle=f'{style},head_length={self.pt(head):.3f},head_width={self.pt(w):.3f}',
                  mutation_scale=1, color=color, lw=self.pt(lw or self.lw), shrinkA=0, shrinkB=0,
                  joinstyle='miter', capstyle='butt')
        self.ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=ap, zorder=z)

    # ------------------------------------------------------------ chemistry
    def bond(self, p, q, order=1, off=2.6, side=0, trim=(0, 0), lw=None, inner=0.8, color=INK):
        """Bond p->q. order 2: side=0 centred pair, side=+1/-1 second line on the
        left/right of p->q (ring style, shortened by `inner`). trim: px cut off
        each end (to clear atom labels)."""
        p, q = np.asarray(p, float), np.asarray(q, float)
        d = q - p
        L = np.hypot(*d)
        u = d / L
        n = np.array([-u[1], u[0]])
        p1, q1 = p + u * trim[0], q - u * trim[1]
        if order == 1:
            self.line(p1, q1, lw=lw, color=color, cap='round')
        elif side == 0:
            for s in (-0.5, 0.5):
                self.line(p1 + n * off * s, q1 + n * off * s, lw=lw, color=color, cap='round')
        else:
            self.line(p1, q1, lw=lw, color=color, cap='round')
            sh = (1 - inner) / 2 * L
            self.line(p + u * max(sh, trim[0]) + n * off * side, q - u * max(sh, trim[1]) + n * off * side, lw=lw,
                      color=color, cap='round')

    def wedge(self, p, q, w=4, color=INK):
        """Solid wedge, narrow at p, half-width w at q."""
        p, q = np.asarray(p, float), np.asarray(q, float)
        u = (q - p) / np.hypot(*(q - p))
        n = np.array([-u[1], u[0]])
        self.patch(Polygon([p, q + n * w, q - n * w], closed=True, fc=color, ec=color, lw=0.3), z=3)

    def patch(self, p, z=3):
        self.ax.add_patch(p)
        p.set_zorder(z)
        return p

    def rect(self, x0, y0, x1, y1, fc='none', ec=INK, lw=None, z=3, **kw):
        return self.patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, ec=ec, lw=self.pt(lw or self.lw),
                                    joinstyle='miter', **kw), z)

    # ------------------------------------------------------------ people
    def _shape(self, sex, x, y, hx, hy, **kw):
        if sex == 'm':
            return Rectangle((x - hx, y - hy), 2 * hx, 2 * hy, joinstyle='miter', **kw)
        if sex == 'f':
            return Ellipse((x, y), 2 * hx, 2 * hy, **kw)
        if sex == 'u':
            return Polygon([(x, y - hy), (x + hx, y), (x, y + hy), (x - hx, y)], closed=True,
                           joinstyle='miter', **kw)
        raise ValueError(sex)

    def person(self, name, x, y, sex='m', pat='', s=None, r=None, rx=None, ry=None, lw=None,
               sp=None, pc=INK, plw=None, lab=None, text=None, lsize=None, lcolor=INK, lweight='normal',
               ec=INK):
        """Draw one individual. sex: 'm' square (half side s), 'f' circle/ellipse
        (r or rx/ry), 'u' diamond (half diagonal s). lab: label position as
        (dx, dy) offset from the centre (text = name unless text= is given)."""
        if sex == 'f':
            hx = rx or r or self.r
            hy = ry or r or self.r
        elif sex == 'u':
            hx = rx or s or r or self.r
            hy = ry or s or r or self.r
        else:
            hx = hy = s or r or self.r
        lw = lw or self.lw
        toks = pat.split()
        fill = 'white'
        for t in toks:
            if t == 'k':
                fill = INK
            elif t.startswith('#') or t in ('gray', 'grey', 'brown', 'maroon', 'lightgray'):
                fill = {'gray': '#b9b9b9', 'grey': '#b9b9b9', 'lightgray': '#d6d6d6', 'brown': '#b87a56',
                        'maroon': '#7a0e1e'}.get(t, t)
        base = self.patch(self._shape(sex, x, y, hx, hy, fc=fill, ec='none', lw=0), z=3)
        self._pattern(base, toks, x, y, hx, hy, sp, pc, plw or lw * 0.75)
        self.patch(self._shape(sex, x, y, hx, hy, fc='none', ec=ec, lw=self.pt(lw)), z=5)
        if 'strike' in toks:
            e = hx * 0.9
            self.line((x - hx - e, y), (x + hx + e, y), lw=lw, z=5)
        self.people[name] = dict(x=x, y=y, hx=hx, hy=hy, sex=sex)
        if lab is not None:
            dx, dy = lab
            self.text(x + dx, y + dy, text if text is not None else name, size=lsize, color=lcolor,
                      weight=lweight)
        return self.people[name]

    def _pattern(self, base, toks, x, y, hx, hy, sp, pc, plw):
        ax = self.ax
        x0, x1, y0, y1 = x - hx, x + hx, y - hy, y + hy
        items = []
        sp = sp or 3.2
        lwp = self.pt(plw)

        def L(xs, ys, w=lwp):
            items.append(ax.plot(xs, ys, color=pc, lw=w, zorder=4, solid_capstyle='butt')[0])

        for t in toks:
            if t in ('diag', '/', 'adiag', '\\', 'xhatch'):
                dirs = {'diag': [1], '/': [1], 'adiag': [-1], '\\': [-1], 'xhatch': [1, -1]}[t]
                span = (x1 - x0) + (y1 - y0)
                for d in dirs:
                    for c in np.arange(-span, span, sp * 1.4142):
                        # y-down image: '/' goes up to the right -> y decreases as x grows
                        if d == 1:
                            L([x0 + c, x0 + c + span], [y1, y1 - span])
                        else:
                            L([x0 + c, x0 + c + span], [y0, y0 + span])
            elif t in ('vl', 'grid'):
                for c in np.arange(x - (int(hx / sp)) * sp, x1 + 1e-6, sp):
                    L([c, c], [y0 - 1, y1 + 1])
            if t in ('hl', 'grid'):
                for c in np.arange(y - (int(hy / sp)) * sp, y1 + 1e-6, sp):
                    L([x0 - 1, x1 + 1], [c, c])
            elif t == 'check':
                for i, cx in enumerate(np.arange(x0, x1, sp)):
                    for j, cy in enumerate(np.arange(y0, y1, sp)):
                        if (i + j) % 2 == 0:
                            items.append(self.patch(Rectangle((cx, cy), sp, sp, fc=pc, ec='none', lw=0), z=4))
            elif t == 'dots':
                pts = []
                for j, cy in enumerate(np.arange(y0 + sp * 0.5, y1, sp)):
                    off = sp * 0.5 if j % 2 else 0
                    for cx in np.arange(x0 + sp * 0.25 + off, x1, sp):
                        pts.append((cx, cy))
                xs, ys = zip(*pts)
                items.append(ax.plot(xs, ys, 'o', ms=self.pt(plw * 1.3), color=pc, mec='none', zorder=4)[0])
            elif t == 'dash':  # short vertical dashes, staggered rows
                for j, cy in enumerate(np.arange(y0 + sp * 0.6, y1, sp * 1.1)):
                    off = sp * 0.5 if j % 2 else 0
                    for cx in np.arange(x0 + sp * 0.4 + off, x1, sp):
                        L([cx, cx], [cy - sp * 0.3, cy + sp * 0.3], w=lwp * 1.2)
            elif t == 'wave':
                amp = sp * 0.28
                xs = np.linspace(x0 - 2, x1 + 2, 200)
                for cy in np.arange(y0 + sp * 0.5, y1 + sp, sp):
                    L(xs, cy + amp * np.sin((xs - x0) / (sp * 0.32)), w=lwp * 0.8)
            elif t == 'plus':
                L([x, x], [y0, y1], self.pt(self.lw))
                L([x0, x1], [y, y], self.pt(self.lw))
            elif t == 'x':
                c = 0.7071 if isinstance(base, Ellipse) else 1.0
                L([x - hx * c, x + hx * c], [y - hy * c, y + hy * c], self.pt(self.lw))
                L([x - hx * c, x + hx * c], [y + hy * c, y - hy * c], self.pt(self.lw))
            elif t in ('bs', 'fs'):  # one thick diagonal: bs = top-left to bottom-right
                c = 0.7071 if isinstance(base, Ellipse) else 1.0
                ya, yb = (y - hy * c, y + hy * c) if t == 'bs' else (y + hy * c, y - hy * c)
                L([x - hx * c, x + hx * c], [ya, yb], self.pt(self.lw * 2.2))
            elif t == 'vdiv':
                L([x, x], [y0, y1], self.pt(self.lw))
            elif t == 'hdiv':
                L([x0, x1], [y, y], self.pt(self.lw))
            elif t.startswith('half-'):
                side = t[5:]
                box = {'l': (x0, y0, hx, 2 * hy), 'r': (x, y0, hx, 2 * hy), 't': (x0, y0, 2 * hx, hy),
                       'b': (x0, y, 2 * hx, hy)}[side]
                items.append(self.patch(Rectangle(box[:2], box[2], box[3], fc=INK, ec='none', lw=0), z=4))
        for it in items:
            it.set_clip_path(base)

    def edge(self, name, side):
        p = self.people[name]
        return p['x'] + (p['hx'] if side == 'r' else -p['hx'])

    def top(self, name):
        p = self.people[name]
        return p['y'] - p['hy']

    def mate(self, a, b, y=None, lw=None, double=False):
        """Marriage line between two people (left/right order is automatic)."""
        A, B = self.people[a], self.people[b]
        if A['x'] > B['x']:
            a, b, A, B = b, a, B, A
        y = A['y'] if y is None else y
        xa, xb = self.edge(a, 'r'), self.edge(b, 'l')
        if double:
            self.line((xa, y - 1.5), (xb, y - 1.5), lw=lw)
            self.line((xa, y + 1.5), (xb, y + 1.5), lw=lw)
        else:
            self.line((xa, y), (xb, y), lw=lw)
        return (xa + xb) / 2

    def kids(self, x, y_from, bar_y, names, lw=None, xs=None):
        """Drop from (x, y_from) to the sibship bar at bar_y, then a line down
        to the top of each child. xs: optional x of each child's line."""
        kx = xs or [self.people[n]['x'] for n in names]
        if y_from is not None:
            self.line((x, y_from), (x, bar_y), lw=lw)
        lo, hi = min(kx + [x]), max(kx + [x])
        if hi - lo > 0.5:
            self.line((lo, bar_y), (hi, bar_y), lw=lw, cap='projecting')
        for n, cx in zip(names, kx):
            self.line((cx, bar_y), (cx, self.top(n)), lw=lw)

    def legend(self, x, y, sex, pat, text, dx=None, size=None, **kw):
        """Legend row: symbol at (x, y) and text starting dx to the right."""
        p = self.person(f'_leg{len(self.people)}', x, y, sex, pat, **kw)
        if text:
            self.text(x + (dx if dx is not None else p['hx'] + 4), y, text, size=size, ha='left')
        return p

    def keep_canvas(self, box=None):
        """Faint corner specks so the trim keeps the whole original canvas
        (same margins / aspect as the original); invisible after downscaling."""
        x0, y0, x1, y1 = box or (0.5, 0.5, self.W - 0.5, self.H - 0.5)
        self.ax.plot([x0, x1, x0, x1], [y0, y0, y1, y1], 's', ms=0.25, color='#f6f6f6', mec='none', zorder=0)

    def ring(self, center, r, doubles=(), start=90, off=4.0, inner=0.75, lw=None, n=6):
        """Regular polygon ring (vertex 0 at angle `start`, counter-clockwise on
        screen); doubles: indices i of edges (vertex i -> i+1) drawn with an inner
        second line. Returns the vertex list."""
        cx, cy = center
        V = [(cx + r * np.cos(np.radians(start + 360 / n * i)), cy - r * np.sin(np.radians(start + 360 / n * i)))
             for i in range(n)]
        for i in range(n):
            p, q = np.array(V[i]), np.array(V[(i + 1) % n])
            self.line(p, q, lw=lw, cap='round')
            if i in doubles:
                m = (p + q) / 2
                c = np.array(center)
                toward = (c - m) / np.hypot(*(c - m))
                sh = (1 - inner) / 2
                a, bq = p + (q - p) * sh, q - (q - p) * sh
                self.line(a + toward * off, bq + toward * off, lw=lw, cap='round')
        return V

    def save(self, **kw):
        return save(self.fig, self.fid, **kw)
