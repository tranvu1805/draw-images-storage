from tabgeo_kit import *
from matplotlib.patches import Rectangle, Polygon, Circle

G = Geo('img035', {'A': (61, 47), 'C': (140, 47), 'D': (140, 175), 'B': (140, 283)}, fs=18, lw=1.4)
ax = G.ax
ax.add_patch(Rectangle((61, 8), 79, 316, fc='#8fd9a3', ec='none', zorder=0))   # the river
for x in (61, 140):
    ax.plot([x, x], [8, 324], color='#8a5a2b', lw=1.6, zorder=1)                # banks
# a small rowing boat left of A
ax.add_patch(Polygon([(16, 44), (56, 44), (50, 52), (22, 52)], closed=True, fc=INK, ec=INK, zorder=2))
ax.add_patch(Circle((36, 30), 3.2, fc=INK, ec=INK, zorder=2))
ax.plot([36, 34], [33, 44], color=INK, lw=2.2)
ax.plot([24, 46], [50, 32], color=INK, lw=1.4)
for y in (57, 61):
    ax.plot([22, 50], [y, y], color=INK, lw=0.8)
G.seg('A', 'C')
G.vec('A', 'D', lw=1.4, L=12, w=4.5)
G.vec('A', 'B', lw=1.4, L=12, w=4.5)
# 8 km dimension
for y in (47, 283):
    G.seg((163, y), (192, y), lw=1.0)
G.vec((175, 188), (175, 47), lw=1.0, L=10, w=3.6)
G.vec((175, 216), (175, 283), lw=1.0, L=10, w=3.6)
G.text(176, 202, '8 km', fs=17)
G.text(110, 27, '3 km', fs=15)
G.labs({'A': (35, 14), 'C': ('e', 10), 'D': ('e', 10), 'B': ('e', 10)})
G.save()
