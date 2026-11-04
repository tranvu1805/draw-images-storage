"""Helpers for the schematic replacements of illustrations / photos.

    from photo_kit import *
    fig, ax = board('img139', 100)           # x 0..100, y 0..100*aspect, y up, equal units
    beetle(ax, 20, 30, 6, GREEN, angle=30)
    txt(ax, 50, 5, 'Quần thể A')
    save(fig, 'img139')

photo(fid, src, crop=None) resizes a downloaded photo to the target width and
writes theory_review/<subject>/<fid>.jpg (quality 85). The raw downloads live
in work/downloads/<fid>/ (gitignored); if missing, photo() keeps the existing jpg.
"""
import os

import drawkit as _dk
from drawkit import *  # noqa: F401,F403
from matplotlib.patches import (Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle,  # noqa: F401
                                Wedge, PathPatch, Arc)
from matplotlib.path import Path  # noqa: F401
from PIL import Image

__all__ = ['board', 'txt', 'box', 'arr', 'beetle', 'ladybug', 'bird', 'fish', 'poly', 'photo', 'tex', 'plt', 'np',
           'INK', 'save', 'Circle', 'Ellipse', 'Polygon', 'Rectangle', 'Wedge', 'FancyBboxPatch', 'FancyArrowPatch',
           'PathPatch', 'Path', 'Arc', 'target_width', 'rot', 'curve', 'GREEN', 'BROWN', 'RED', 'BLUE', 'YELLOW',
           'GREY']

GREEN = '#2e7d32'
BROWN = '#c8915a'
RED = '#c62828'
BLUE = '#1e63c4'
YELLOW = '#f2c318'
GREY = '#d9d9d9'


def board(fid, W=100, aspect=None, width_px=None):
    """Canvas with data coords x in [0, W], y in [0, W*aspect] (y up, equal units)."""
    fig, ax = canvas(fid, aspect=aspect, width_px=width_px)
    a = aspect or _dk.INFO[fid]['aspect']
    ax.set_xlim(0, W)
    ax.set_ylim(0, W * a)
    ax.set_aspect('equal')
    ax.set_axis_off()
    return fig, ax


def txt(ax, x, y, s, size=12, ha='center', va='center', color=INK, **kw):
    return ax.text(x, y, s, fontsize=size, ha=ha, va=va, color=color, **kw)


def box(ax, x, y, w, h, s=None, size=12, fc='white', ec=INK, lw=1.2, r=0.0, z=2, **kw):
    """Rectangle with lower-left (x, y); optional centred text."""
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}' if r else 'square,pad=0',
                       fc=fc, ec=ec, lw=lw, zorder=z)
    ax.add_patch(p)
    if s is not None:
        ax.text(x + w / 2, y + h / 2, s, fontsize=size, ha='center', va='center', zorder=z + 1, **kw)
    return p


def arr(ax, x0, y0, x1, y1, color=INK, lw=1.4, head=8, rad=0.0, z=4, style='-|>', **kw):
    """Arrow in data coords; head in points; rad bends it (connectionstyle arc3)."""
    p = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=f'{style},head_length={head * 0.1},head_width={head * 0.05}',
                        mutation_scale=10, color=color, lw=lw, zorder=z, shrinkA=0, shrinkB=0,
                        connectionstyle=f'arc3,rad={rad}', **kw)
    ax.add_patch(p)
    return p


def rot(pts, angle, cx=0, cy=0):
    a = np.radians(angle)
    c, s = np.cos(a), np.sin(a)
    pts = np.asarray(pts, float)
    x, y = pts[:, 0], pts[:, 1]
    return np.column_stack([cx + c * x - s * y, cy + s * x + c * y])


def poly(ax, pts, fc='none', ec=INK, lw=1.0, z=2, closed=True, **kw):
    p = Polygon(np.asarray(pts), closed=closed, fc=fc, ec=ec, lw=lw, zorder=z, **kw)
    ax.add_patch(p)
    return p


def curve(ax, pts, color=INK, lw=1.2, z=2, n=60, **kw):
    """Smooth curve through points (Catmull-Rom)."""
    P = np.asarray(pts, float)
    P = np.vstack([P[0], P, P[-1]])
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        t = np.linspace(0, 1, n)[:, None]
        out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2 +
                          (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    C = np.vstack(out)
    return ax.plot(C[:, 0], C[:, 1], color=color, lw=lw, zorder=z, solid_capstyle='round', **kw)[0]


# ---------------------------------------------------------------- glyphs

def beetle(ax, x, y, s, color, angle=0, z=5, lw=0.8):
    """Top view of a beetle (head pointing to `angle` degrees, 90 = up); s = body length."""
    ink = '#3b2a1a'
    a = angle - 90
    # legs
    for side in (-1, 1):
        for k, (ly, dx, dy) in enumerate([(0.12, 0.42, 0.22), (-0.02, 0.46, 0.0), (-0.16, 0.42, -0.22)]):
            pts = rot([[side * 0.18 * s, ly * s], [side * dx * s, (ly + dy * 0.5) * s],
                       [side * (dx + 0.06) * s, (ly + dy) * s]], a, x, y)
            ax.plot(pts[:, 0], pts[:, 1], color=ink, lw=lw, zorder=z - 1, solid_capstyle='round')
    # antennae
    for side in (-1, 1):
        pts = rot([[side * 0.06 * s, 0.42 * s], [side * 0.2 * s, 0.6 * s], [side * 0.3 * s, 0.66 * s]], a, x, y)
        ax.plot(pts[:, 0], pts[:, 1], color=ink, lw=lw * 0.8, zorder=z - 1)
    # head + pronotum + elytra
    hx, hy = rot([[0, 0.36 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((hx, hy), 0.2 * s, 0.14 * s, angle=a, fc=ink, ec=ink, lw=lw * 0.5, zorder=z))
    px, py = rot([[0, 0.24 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((px, py), 0.34 * s, 0.2 * s, angle=a, fc=color, ec=ink, lw=lw, zorder=z + 1))
    ex, ey = rot([[0, -0.06 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((ex, ey), 0.44 * s, 0.56 * s, angle=a, fc=color, ec=ink, lw=lw, zorder=z + 1))
    seam = rot([[0, 0.17 * s], [0, -0.33 * s]], a, x, y)
    ax.plot(seam[:, 0], seam[:, 1], color=ink, lw=lw * 0.8, zorder=z + 2)
    # highlight
    gx, gy = rot([[-0.1 * s, 0.04 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((gx, gy), 0.08 * s, 0.18 * s, angle=a, fc='white', ec='none', alpha=0.55, zorder=z + 2))


def ladybug(ax, x, y, s, color, angle=0, z=5, lw=0.8, spots=True):
    """Top view of a ladybird (round shell with black spots)."""
    ink = '#1a1a1a'
    a = angle - 90
    for side in (-1, 1):
        for ly, dx, dy in [(0.12, 0.36, 0.14), (-0.02, 0.4, 0.0), (-0.16, 0.36, -0.14)]:
            pts = rot([[side * 0.2 * s, ly * s], [side * dx * s, (ly + dy) * s], [side * (dx + 0.07) * s,
                                                                                       (ly + dy * 1.6) * s]], a, x, y)
            ax.plot(pts[:, 0], pts[:, 1], color=ink, lw=lw, zorder=z - 1, solid_capstyle='round')
    for side in (-1, 1):
        pts = rot([[side * 0.05 * s, 0.36 * s], [side * 0.14 * s, 0.5 * s]], a, x, y)
        ax.plot(pts[:, 0], pts[:, 1], color=ink, lw=lw * 0.8, zorder=z - 1)
    hx, hy = rot([[0, 0.28 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((hx, hy), 0.3 * s, 0.18 * s, angle=a, fc=ink, ec=ink, zorder=z))
    ex, ey = rot([[0, -0.04 * s]], a, x, y)[0]
    ax.add_patch(Ellipse((ex, ey), 0.56 * s, 0.6 * s, angle=a, fc=color, ec=ink, lw=lw, zorder=z + 1))
    seam = rot([[0, 0.24 * s], [0, -0.33 * s]], a, x, y)
    ax.plot(seam[:, 0], seam[:, 1], color=ink, lw=lw * 0.8, zorder=z + 2)
    if spots:
        for sx, sy in [(-0.14, 0.08), (0.14, 0.08), (-0.15, -0.14), (0.15, -0.14), (-0.06, -0.24), (0.06, -0.24)]:
            cx, cy = rot([[sx * s, sy * s]], a, x, y)[0]
            ax.add_patch(Circle((cx, cy), 0.055 * s, fc=ink, ec='none', zorder=z + 2))


def bird(ax, x, y, s, color, facing=1, z=5, lw=0.9):
    """Small side-view songbird standing; s = body length, facing 1 = right."""
    f = facing
    ink = '#222222'
    # tail
    poly(ax, [(x - f * 0.25 * s, y + 0.05 * s), (x - f * 0.62 * s, y + 0.28 * s), (x - f * 0.55 * s, y + 0.12 * s)],
         fc=color, ec=ink, lw=lw * 0.7, z=z)
    ax.add_patch(Ellipse((x, y + 0.12 * s), 0.62 * s, 0.4 * s, angle=f * 12, fc=color, ec=ink, lw=lw * 0.8,
                         zorder=z + 1))
    ax.add_patch(Circle((x + f * 0.28 * s, y + 0.36 * s), 0.16 * s, fc=color, ec=ink, lw=lw * 0.8, zorder=z + 2))
    ax.add_patch(Ellipse((x + f * 0.02 * s, y + 0.13 * s), 0.3 * s, 0.16 * s, angle=-f * 10, fc='none', ec=ink,
                         lw=lw * 0.7, zorder=z + 2))
    poly(ax, [(x + f * 0.42 * s, y + 0.4 * s), (x + f * 0.58 * s, y + 0.35 * s), (x + f * 0.42 * s, y + 0.3 * s)],
         fc='#f0b400', ec=ink, lw=lw * 0.5, z=z + 3)
    ax.add_patch(Circle((x + f * 0.32 * s, y + 0.4 * s), 0.035 * s, fc='black', ec='none', zorder=z + 3))
    for dx in (-0.05, 0.08):
        ax.plot([x + f * dx * s, x + f * (dx - 0.02) * s], [y - 0.06 * s, y - 0.28 * s], color=ink, lw=lw,
                zorder=z)
        ax.plot([x + f * (dx - 0.02) * s, x + f * (dx + 0.06) * s], [y - 0.28 * s, y - 0.28 * s], color=ink,
                lw=lw, zorder=z)


def fish(ax, x, y, s, color, facing=1, z=5, lw=0.8, stripes=False):
    f = facing
    ink = '#222222'
    poly(ax, [(x - f * 0.38 * s, y), (x - f * 0.62 * s, y + 0.2 * s), (x - f * 0.62 * s, y - 0.2 * s)], fc=color,
         ec=ink, lw=lw * 0.7, z=z)
    ax.add_patch(Ellipse((x, y), 0.85 * s, 0.38 * s, fc=color, ec=ink, lw=lw, zorder=z + 1))
    ax.add_patch(Circle((x + f * 0.26 * s, y + 0.04 * s), 0.035 * s, fc='black', ec='none', zorder=z + 2))
    ax.plot([x + f * 0.15 * s, x + f * 0.13 * s], [y + 0.12 * s, y - 0.1 * s], color=ink, lw=lw * 0.7, zorder=z + 2)
    if stripes:
        for dx in (-0.15, -0.02):
            ax.plot([x + f * dx * s] * 2, [y + 0.15 * s, y - 0.15 * s], color='#333333', lw=lw * 1.4, zorder=z + 2)


# ---------------------------------------------------------------- photos



def photo(fid, src, crop=None, quality=85):
    """Resize a downloaded photo (opened with PIL only) to the target width -> <fid>.jpg."""
    out_dir = os.path.join(_dk.OUT, _dk.subject_of(fid))
    dest = os.path.join(out_dir, f'{fid}.jpg')
    if not os.path.exists(src):
        print(f'{fid}: source {src} not present, keeping {dest}')
        return dest
    im = Image.open(src)
    im.load()
    im = im.convert('RGB')
    if crop:  # fractions (left, top, right, bottom)
        l, t, r, b = crop
        im = im.crop((round(l * im.width), round(t * im.height), round(r * im.width), round(b * im.height)))
    w = _dk.target_width(fid)
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    os.makedirs(out_dir, exist_ok=True)
    png = os.path.join(out_dir, f'{fid}.png')
    if os.path.exists(png):
        os.remove(png)
    im.save(dest, 'JPEG', quality=quality, optimize=True, progressive=True)
    return dest


# ---------------------------------------------------------------- scene glyphs (habitats, pond)

def tree(ax, x, yg, h, r, crown='#3f8f3a', trunk='#7b4a26', z=3):
    ax.add_patch(Polygon([(x - r * 0.12, yg), (x + r * 0.12, yg), (x + r * 0.07, yg + h), (x - r * 0.07, yg + h)],
                         fc=trunk, ec='#4a2c14', lw=0.6, zorder=z))
    for dx, dy, k in ((0, 0.2, 1.0), (-0.55, -0.15, 0.7), (0.55, -0.12, 0.72), (-0.3, 0.55, 0.62), (0.32, 0.55, 0.6)):
        ax.add_patch(Circle((x + dx * r, yg + h + dy * r), r * k, fc=crown, ec='#2b6a27', lw=0.6, zorder=z + 1))


def deer(ax, x, yg, s, facing=1, color='#b5733c', z=5):
    f = facing
    ink = '#4a2c14'
    by = yg + 0.55 * s
    for dx in (-0.32, -0.22, 0.24, 0.34):   # legs
        ax.plot([x + f * dx * s, x + f * dx * s * 1.05], [by, yg], color=color, lw=2.6, zorder=z,
                solid_capstyle='butt')
        ax.plot([x + f * dx * s * 1.05] * 2, [yg, yg + 0.05 * s], color=ink, lw=2.6, zorder=z, solid_capstyle='butt')
    ax.add_patch(Ellipse((x, by + 0.08 * s), 0.85 * s, 0.32 * s, fc=color, ec=ink, lw=0.7, zorder=z + 1))
    ax.add_patch(Polygon([(x + f * 0.2 * s, by + 0.14 * s), (x + f * 0.37 * s, by + 0.52 * s),
                          (x + f * 0.5 * s, by + 0.47 * s), (x + f * 0.44 * s, by + 0.0 * s)], fc=color, ec=ink,
                         lw=0.7, zorder=z + 1))
    ax.add_patch(Ellipse((x + f * 0.53 * s, by + 0.53 * s), 0.3 * s, 0.15 * s, angle=-f * 25, fc=color, ec=ink,
                         lw=0.7, zorder=z + 2))
    ax.add_patch(Ellipse((x + f * 0.42 * s, by + 0.6 * s), 0.07 * s, 0.13 * s, angle=f * 30, fc=color, ec=ink,
                         lw=0.6, zorder=z + 2))   # ear
    for k in (-1, 1):   # antlers
        b = np.array([x + f * (0.47 + 0.03 * k) * s, by + 0.6 * s])
        ax.plot([b[0], b[0] - f * 0.06 * s * k, b[0] - f * 0.02 * s * k], [b[1], b[1] + 0.2 * s, b[1] + 0.32 * s],
                color=ink, lw=1.0, zorder=z + 1)
        ax.plot([b[0] - f * 0.05 * s * k, b[0] + f * 0.04 * s], [b[1] + 0.14 * s, b[1] + 0.22 * s], color=ink,
                lw=0.9, zorder=z + 1)
    ax.add_patch(Circle((x + f * 0.58 * s, by + 0.55 * s), 0.018 * s, fc='black', zorder=z + 3))
    ax.add_patch(Ellipse((x - f * 0.42 * s, by + 0.14 * s), 0.08 * s, 0.12 * s, fc='white', ec=ink, lw=0.5,
                         zorder=z + 2))   # tail


def vbird(ax, x, y, s, color='#333333', z=6):
    t = np.linspace(0, 1, 20)
    ax.plot(x - s * (1 - t) * 0.5, y + s * 0.18 * np.sin(np.pi * t), color=color, lw=1.4, zorder=z)
    ax.plot(x + s * t * 0.5, y + s * 0.18 * np.sin(np.pi * (1 - t)), color=color, lw=1.4, zorder=z)


def frog(ax, x, y, s, z=7):
    ink = '#1f5e1f'
    ax.add_patch(Ellipse((x, y), 0.9 * s, 0.55 * s, fc='#5cb85c', ec=ink, lw=0.7, zorder=z))
    for dx in (-0.2, 0.2):
        ax.add_patch(Circle((x + dx * s, y + 0.27 * s), 0.13 * s, fc='#5cb85c', ec=ink, lw=0.6, zorder=z + 1))
        ax.add_patch(Circle((x + dx * s, y + 0.29 * s), 0.06 * s, fc='black', zorder=z + 2))
    for dx in (-1, 1):
        ax.add_patch(Ellipse((x + dx * 0.42 * s, y - 0.18 * s), 0.35 * s, 0.18 * s, fc='#4cae4c', ec=ink, lw=0.6,
                             zorder=z - 1))
    ax.plot([x - 0.14 * s, x + 0.14 * s], [y + 0.05 * s, y + 0.05 * s], color=ink, lw=0.7, zorder=z + 1)


def lilypad(ax, x, y, w, flower=False, z=5):
    ax.add_patch(Wedge((x, y), w / 2, 20, 340, fc='#4caf50', ec='#2e7d32', lw=0.6, zorder=z,
                       transform=ax.transData))
    if flower:
        for a in range(0, 360, 45):
            ax.add_patch(Ellipse((x + 0.1 * w * np.cos(np.radians(a)), y + 0.12 * w + 0.06 * w * np.sin(np.radians(a))),
                                 0.16 * w, 0.08 * w, angle=a, fc='#fde047', ec='#d4a106', lw=0.4, zorder=z + 1))
        ax.add_patch(Circle((x, y + 0.13 * w), 0.05 * w, fc='#f59e0b', zorder=z + 2))


def reed(ax, x, y0, h, lean=0.0, z=4, head=True):
    ax.plot([x, x + lean], [y0, y0 + h], color='#4d7c2a', lw=1.3, zorder=z)
    if head:
        ax.add_patch(Ellipse((x + lean * 0.88, y0 + h * 0.85), 0.9, 3.0, angle=-np.degrees(np.arctan2(lean, h)),
                             fc='#7b4a26', ec='none', zorder=z + 1))
    ax.add_patch(Polygon([(x, y0), (x + 1.2 + lean * 0.3, y0 + h * 0.6), (x + 0.3, y0)], fc='#5f9632', ec='none',
                         zorder=z))


def snail(ax, x, y, s, z=6):
    ax.add_patch(Ellipse((x + 0.15 * s, y - 0.18 * s), 0.9 * s, 0.22 * s, fc='#d9b48f', ec='#7a5230', lw=0.5,
                         zorder=z))
    t = np.linspace(0, 5 * np.pi, 120)
    r = 0.3 * s * (1 - t / (5.6 * np.pi))
    ax.add_patch(Circle((x, y), 0.32 * s, fc='#b07a4a', ec='#6b4423', lw=0.6, zorder=z + 1))
    ax.plot(x + r * np.cos(t), y + r * np.sin(t), color='#6b4423', lw=0.5, zorder=z + 2)


def worm(ax, pts, z=4, lw=3.2):
    curve(ax, pts, color='#9c5a5a', lw=lw + 1, z=z)
    curve(ax, pts, color='#e8a3a3', lw=lw, z=z + 1)


def duck(ax, x, y, s, facing=1, body='#8d6e4f', head='#2e7d32', z=7):
    f = facing
    ink = '#3e2a17'
    ax.add_patch(Ellipse((x, y + 0.18 * s), 0.9 * s, 0.38 * s, fc=body, ec=ink, lw=0.7, zorder=z))
    ax.add_patch(Polygon([(x - f * 0.38 * s, y + 0.22 * s), (x - f * 0.58 * s, y + 0.36 * s),
                          (x - f * 0.42 * s, y + 0.1 * s)], fc=body, ec=ink, lw=0.6, zorder=z))
    ax.add_patch(Ellipse((x - f * 0.02 * s, y + 0.22 * s), 0.42 * s, 0.17 * s, fc='#6d4c33', ec=ink, lw=0.5,
                         zorder=z + 1))
    ax.add_patch(Polygon([(x + f * 0.26 * s, y + 0.3 * s), (x + f * 0.32 * s, y + 0.55 * s),
                          (x + f * 0.4 * s, y + 0.55 * s), (x + f * 0.38 * s, y + 0.28 * s)], fc=head, ec=ink, lw=0.5,
                         zorder=z + 1))
    ax.add_patch(Circle((x + f * 0.36 * s, y + 0.6 * s), 0.12 * s, fc=head, ec=ink, lw=0.6, zorder=z + 2))
    ax.add_patch(Polygon([(x + f * 0.45 * s, y + 0.62 * s), (x + f * 0.62 * s, y + 0.56 * s),
                          (x + f * 0.45 * s, y + 0.54 * s)], fc='#f2b61f', ec=ink, lw=0.4, zorder=z + 3))
    ax.add_patch(Circle((x + f * 0.39 * s, y + 0.64 * s), 0.025 * s, fc='black', zorder=z + 3))
    ax.plot([x - 0.5 * s, x + 0.5 * s], [y, y], color='#7fb2dc', lw=0.9, zorder=z + 3)


def turtle(ax, x, y, s, facing=1, z=6):
    f = facing
    ink = '#2f4a1f'
    for dx in (-0.25, 0.25):
        ax.add_patch(Ellipse((x + dx * s, y - 0.12 * s), 0.18 * s, 0.12 * s, fc='#8bab5f', ec=ink, lw=0.5, zorder=z))
    ax.add_patch(Circle((x + f * 0.5 * s, y + 0.02 * s), 0.11 * s, fc='#8bab5f', ec=ink, lw=0.6, zorder=z))
    ax.add_patch(Wedge((x, y - 0.08 * s), 0.45 * s, 0, 180, fc='#5d7b3a', ec=ink, lw=0.7, zorder=z + 1))
    for a in (45, 90, 135):
        ax.plot([x, x + 0.45 * s * np.cos(np.radians(a))], [y - 0.08 * s, y - 0.08 * s + 0.45 * s *
                                                              np.sin(np.radians(a))], color=ink, lw=0.5, zorder=z + 2)


def tadpole(ax, x, y, s, facing=1, z=6):
    ax.add_patch(Ellipse((x, y), 0.4 * s, 0.3 * s, fc='#37474f', ec='none', zorder=z))
    t = np.linspace(0, 1, 20)
    ax.plot(x - facing * (0.2 + 0.6 * t) * s, y + 0.06 * s * np.sin(t * 9), color='#37474f', lw=1.0, zorder=z)


def bubble(ax, x, y, r, tail_to, fc='#fffbe6', ec='#888888', z=20):
    tx, ty = tail_to
    a = np.arctan2(ty - y, tx - x)
    p1 = (x + r * np.cos(a + 0.35), y + r * np.sin(a + 0.35))
    p2 = (x + r * np.cos(a - 0.35), y + r * np.sin(a - 0.35))
    ax.add_patch(Polygon([p1, (tx, ty), p2], fc=fc, ec=ec, lw=0.9, zorder=z))
    ax.add_patch(Circle((x, y), r, fc=fc, ec=ec, lw=0.9, zorder=z + 1))
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=fc, lw=2.0, zorder=z + 1)


def badge(ax, x, y, s, r=2.4, size=12, z=30):
    ax.add_patch(Circle((x, y), r, fc='#c62828', ec='white', lw=1.0, zorder=z))
    ax.text(x, y - 0.1, s, fontsize=size, ha='center', va='center', color='white', weight='bold', zorder=z + 1)


__all__ += ['tree', 'deer', 'vbird', 'frog', 'lilypad', 'reed', 'snail', 'worm', 'duck', 'turtle', 'tadpole',
            'bubble', 'badge']
