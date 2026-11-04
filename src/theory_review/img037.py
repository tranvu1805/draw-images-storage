from tabgeo_kit import *
from matplotlib.patches import Ellipse, Polygon

BLUE = '#1f3fe0'
P = {'O': (141, 16), 'A': (70, 196), 'B': (101, 152), 'C': (222, 172), 'M': (141, 180)}
G = Geo('img037', P, fs=17, lw=1.0)
ax = G.ax
ax.plot([43, 242], [16, 16], color=INK, lw=5, solid_capstyle='round')   # ceiling
# lamp disc (two ellipses: bottom rim then top face)
cx, cy, rx, ry, th = 141, 180, 82, 33, 16
ax.add_patch(Ellipse((cx, cy + th), 2 * rx, 2 * ry, fc='#b9bcff', ec=INK, lw=1.2, zorder=1))
ax.add_patch(Polygon([(cx - rx, cy), (cx + rx, cy), (cx + rx, cy + th), (cx - rx, cy + th)], fc='#b9bcff',
                     ec='none', zorder=1))
ax.plot([cx - rx, cx - rx], [cy, cy + th], color=INK, lw=1.2, zorder=1)
ax.plot([cx + rx, cx + rx], [cy, cy + th], color=INK, lw=1.2, zorder=1)
ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, fc='#b9bcff', ec=INK, lw=1.2, zorder=1))
# strings O-A, O-B, O-C (A sits on the front rim)
P['A'] = (cx - rx * 0.86, cy + ry * 0.51 + 4)
P['B'] = (cx - rx * 0.49, cy - ry * 0.87)
P['C'] = (cx + rx * 0.99, cy - ry * 0.12)
for k in 'ABC':
    G.seg('O', k, lw=1.1)
G.seg('M', 'C', dashed=True, lw=1.4)
G.seg('M', (cx, cy + ry + th - 2), dashed=True, lw=1.4)
G.vec((cx, cy + ry + th - 2), (cx, 296), lw=1.8, L=13, w=5)
G.dot('M', r=6)
# tension forces along the strings
for k, t in (('A', 0.5), ('B', 0.75), ('C', 0.51)):
    G.vec('O', G.mid('O', k, t), lw=2.4, L=13, w=5, color=BLUE)
G.text(103, 62, r'$\vec{F}_1$', fs=17, color=BLUE)
G.text(150, 66, r'$\vec{F}_2$', fs=17, color=BLUE)
G.text(183, 56, r'$\vec{F}_3$', fs=17, color=BLUE)
G.text(158, 255, r'$\vec{P}$', fs=17)
for k, (x, y) in {'O': (163, 32), 'A': (85, 183), 'B': (115, 138), 'C': (238, 163)}.items():
    G.text(x, y, f'${k}$', fs=17)
G.save()
