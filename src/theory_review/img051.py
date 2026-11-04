from tabgeo_kit import *
from matplotlib.patches import Polygon, Circle

P = {'E': (147, 52), 'A': (46, 190), 'B': (97, 209), 'C': (251, 199), 'D': (200, 181),
     'a': (46, 336), 'b': (97, 353), 'c': (251, 344), 'd': (200, 327)}
G = Geo('img051', P, fs=14, lw=1.6)
ax = G.ax
# platform under the frame
ax.add_patch(Polygon([P['a'], P['b'], P['c'], P['d']], closed=True, fc='#d6dde3', ec=INK, lw=1.0, zorder=1))
ax.add_patch(Polygon([P['b'], P['c'], (251, 352), (97, 361)], closed=True, fc='#aab6c0', ec=INK, lw=1.0, zorder=1))
ax.add_patch(Polygon([P['a'], P['b'], (97, 361), (46, 344)], closed=True, fc='#bcc7d0', ec=INK, lw=1.0, zorder=1))
G.seg('D', 'd', zorder=1.5)   # back post (hidden by the car lower down)

# the car, side view, facing left (simple line drawing)
o = np.array([80.0, 347.0])
ux = np.array([155.0, -15.0]) / 160 * 1.0
uy = np.array([-ux[1], -ux[0]]) / np.hypot(*ux)
L = lambda x, y: o + x * ux + y * uy
top = [(4, 12), (0, 22), (2, 36), (14, 46), (40, 52), (58, 56), (84, 77), (110, 82), (135, 80), (152, 72),
       (160, 54), (163, 36), (160, 12)]
body = G.spline([L(*q) for q in top], n=12)
ax.add_patch(Polygon(body, closed=True, fc='white', ec=INK, lw=1.4, zorder=2))
win = G.spline([L(*q) for q in [(64, 57), (86, 74), (110, 78), (133, 76), (147, 67), (150, 57)]], n=12)
ax.add_patch(Polygon(win, closed=True, fc='#dfe5ea', ec=INK, lw=1.1, zorder=2.1))
for (x0, y0), (x1, y1) in (((106, 57), (106, 78)), ((106, 57), (108, 20)), ((61, 55), (64, 22)),
                           ((150, 57), (150, 24))):
    ax.plot(*zip(L(x0, y0), L(x1, y1)), color=INK, lw=1.0, zorder=2.2)
ax.plot(*zip(L(92, 46), L(100, 46)), color=INK, lw=1.4, zorder=2.2)       # door handle
ax.add_patch(Polygon([L(2, 40), L(12, 44), L(10, 36), L(2, 34)], closed=True, fc='#f0d77a', ec=INK, lw=0.8,
                     zorder=2.2))
for wx in (29, 140):
    c = L(wx, 17)
    ax.add_patch(Circle(c, 17, fc='#333333', ec=INK, lw=1.0, zorder=2.3))
    ax.add_patch(Circle(c, 8, fc='#e6e6e6', ec=INK, lw=0.8, zorder=2.4))

# frame and slings
G.edges('A-B B-C C-D D-A A-a B-b C-c', zorder=3)
for k in 'ABCD':
    G.seg('E', k, zorder=3)
for k in 'ABCDabc':
    G.dot(k, r=4)
# vectors F1..F4 (heads on the slings)
for k in 'ABCD':
    G.head('E', k, L=10, w=4, at=0.35)
# pulley and hook
ax.plot([141, 141], [4, 28], color='#8a5a2b', lw=1.6)
ax.plot([157, 157], [4, 28], color='#8a5a2b', lw=1.6)
ax.add_patch(Circle((149, 28), 12, fc='#d29a62', ec='#8a5a2b', lw=1.2, zorder=3))
ax.add_patch(Circle((149, 28), 2.5, fc=INK, ec=INK, zorder=4))
ax.plot([149, 149], [28, 42], color=INK, lw=2.0, zorder=4)
t = np.linspace(0.0, 1.25 * np.pi, 30)
ax.plot(149 + 5.5 * np.cos(t + 0.3), 46 + 5.5 * np.sin(t + 0.3), color=INK, lw=2.0, zorder=4)
T = lambda x, y, s: G.text(x, y, s, fs=13)
T(97, 94, r'$\vec{F}_1$')
T(142, 117, r'$\vec{F}_2$')
T(153, 106, r'$\vec{F}_4$')
T(203, 98, r'$\vec{F}_3$')
G.labs({'A': ('w', 13), 'B': (230, 14), 'C': ('e', 12), 'D': (60, 14), 'E': (190, 13)})
G.save()
