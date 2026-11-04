from tabgeo_kit import *
from matplotlib.patches import Rectangle

G = Geo('img036', {}, fs=17, lw=1.5)
ax = G.ax
x0, x1, y0, y1, c = 90, 268, 10, 189, 36   # sheet 12 cm, cut squares of side x
for xa in (x0, x1 - c):
    for ya in (y0, y1 - c):
        ax.add_patch(Rectangle((xa, ya), c, c, fc='#d4d4d4', ec='none'))
ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec=INK, lw=1.5))
for x in (x0 + c, x1 - c):
    G.seg((x, y0), (x, y1))
for y in (y0 + c, y1 - c):
    G.seg((x0, y), (x1, y))


def dim(x, ya, yb, t=7):
    G.seg((x - t, ya), (x + t, ya), lw=1.1)
    G.seg((x - t, yb), (x + t, yb), lw=1.1)
    G.vec((x, (ya + yb) / 2), (x, ya), lw=1.1, L=8, w=3.2)
    G.vec((x, (ya + yb) / 2), (x, yb), lw=1.1, L=8, w=3.2)


dim(79, y0, y1)
dim(280, y0, y0 + c)
G.text(43, 102, r'$12\ \mathrm{cm}$', fs=18)
G.text(315, 28, r'$x\ \mathrm{cm}$', fs=18)
# the box (no lid)
B = {'a': (351, 189), 'b': (511, 189), 'c': (582, 125), 'd': (421, 125),
     'e': (351, 153), 'f': (511, 153), 'g': (582, 89), 'h': (421, 89)}
G.P.update(B)
G.edges('a-b b-f f-e e-a e-h h-g g-f b-c c-g')
G.edges('a-d d-c d-h', dashed=True)
G.save()
