from tabgeo_kit import *
from matplotlib.patches import Ellipse, Polygon, FancyBboxPatch

cx, cy, rx, ry = 148, 222, 118, 23
th = np.radians([180, 61, 0, 247])                 # A, B, C, D on the rim of the plate
P = {k: (cx + rx * np.cos(t), cy - ry * np.sin(t)) for k, t in zip('ABCD', th)}
P['S'] = (147, 30)
G = Geo('img245', P, fs=19, lw=1.3)
ax = G.ax
t = np.linspace(0, np.pi, 80)
ax.add_patch(Polygon(np.c_[cx + rx * np.cos(t), cy + 33 * np.sin(t)], closed=True, fc='#e07a2a', ec=INK,
                     lw=1.0, zorder=1))
ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, fc='white', ec=INK, lw=1.4, zorder=2))
ax.add_patch(FancyBboxPatch((124, 18), 48, 13, boxstyle='round,pad=0,rounding_size=3', fc='#8c4a3c', ec=INK,
                            lw=0.8, zorder=4))
for k in 'ABCD':
    a, b = G.p('S'), G.p(k)
    z = 1.5 if k == 'B' else 5
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#a8935a', lw=3.0, zorder=z, solid_capstyle='round')
    ax.plot([a[0], b[0]], [a[1], b[1]], color='white', lw=1.2, ls=(0, (2.5, 2.5)), zorder=z)
for k in 'ABCD':
    G.dot(k, r=5)
G.text(147, 9, '$S$', fs=17, zorder=6)
G.labs({'A': ('w', 17), 'B': (50, 18), 'C': ('e', 17), 'D': (265, 26)})
G.save()
