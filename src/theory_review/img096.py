from tabgeo_kit import *
from matplotlib.patches import Ellipse, Rectangle, Polygon

cx, cy, rx, ry = 87, 139, 73, 14
th = np.radians([180, 63, 0, 247])                 # A, B, C, D on the rim of the pan
P = {k: (cx + rx * np.cos(t), cy - ry * np.sin(t)) for k, t in zip('ABCD', th)}
P['S'] = (87, 23)
G = Geo('img096', P, fs=16, lw=1.2)
ax = G.ax
# pan: rim ellipse + shallow bowl underneath
t = np.linspace(0, np.pi, 80)
bowl = np.r_[np.c_[cx + rx * np.cos(t), cy + 20 * np.sin(t)]]
ax.add_patch(Polygon(bowl, closed=True, fc='#f2a65e', ec=INK, lw=1.0, zorder=1))
ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, fc='#f7c79a', ec=INK, lw=1.2, zorder=2))
# weight on the pan
wx, wy, wr, wh = 88, 141, 33, 12
ax.add_patch(Rectangle((wx - wr, wy - wh), 2 * wr, wh, fc='#f2a65e', ec='none', zorder=3))
ax.add_patch(Ellipse((wx, wy), 2 * wr, 14, fc='#f2a65e', ec=INK, lw=1.0, zorder=2.9))
ax.plot([wx - wr, wx - wr], [wy - wh, wy], color=INK, lw=1.0, zorder=3)
ax.plot([wx + wr, wx + wr], [wy - wh, wy], color=INK, lw=1.0, zorder=3)
ax.add_patch(Ellipse((wx, wy - wh), 2 * wr, 14, fc='#f8cfa6', ec=INK, lw=1.0, zorder=3.1))
# hanger
ax.add_patch(Rectangle((72, 16), 31, 7, fc='#8c2f39', ec=INK, lw=0.8, zorder=4))
# chains SA, SB, SC, SD (drawn as chain-like double strokes)
for k in 'ABCD':
    a, b = G.p('S'), G.p(k)
    z = 1.5 if k == 'B' else 5
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#8a7a4a', lw=2.6, zorder=z, solid_capstyle='round')
    ax.plot([a[0], b[0]], [a[1], b[1]], color='white', lw=1.0, ls=(0, (2, 2.2)), zorder=z)
for k in 'ABCD':
    G.dot(k, r=4.5)
G.labs({'B': (60, 14), 'C': ('e', 12), 'D': (260, 15)})
G.text(7, 146, '$A$', fs=15)
G.text(87, 9, '$S$', fs=14, zorder=6)
G.save()
