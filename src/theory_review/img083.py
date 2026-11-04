# Room 8 m x 6 m x 4 m: fan A on the 8 m wall, fan B on the 6 m wall, axes Oxyz at a floor corner.
from photo_kit import *

fig, ax = board('img083', 100)            # y 0..67
EDGE = '#8a8a8a'
# back wall (x along it, to the left), right wall (y towards the viewer)
BL, BR, TL, TR = (6, 18), (72, 18), (6, 50), (72, 50)
NB, NT = (97, 3), (97, 65)                # near end of the right wall (y = 6 m)
poly(ax, [(0, 0), (100, 0), NB, BR, BL, (0, 10)], fc='#efe4d2', ec='none', z=0)          # floor
poly(ax, [(0, 67), (100, 67), NT, TR, TL, (0, 58)], fc='#fafafa', ec='none', z=0)       # ceiling
poly(ax, [(0, 10), BL, TL, (0, 58)], fc='#e9e9e9', ec='none', z=0)                      # left wall
poly(ax, [BL, BR, TR, TL], fc='#f4f4f4', ec=EDGE, lw=0.9, z=1)                           # back wall (8 m)
poly(ax, [BR, NB, NT, TR], fc='#e3e3e3', ec=EDGE, lw=0.9, z=1)                           # right wall (6 m)
ax.plot([0, BL[0]], [10, BL[1]], color=EDGE, lw=0.9)
ax.plot([0, TL[0]], [58, TL[1]], color=EDGE, lw=0.9)


def back(x, z):        # x in m from O to the left, z in m up
    return BR[0] - (BR[0] - BL[0]) * x / 8, BR[1] + (TR[1] - BR[1]) * z / 4


def side(y, z):        # bilinear on the right wall, y in m towards the viewer
    t = y / 6
    b = np.array(BR) + t * (np.array(NB) - np.array(BR))
    tp = np.array(TR) + t * (np.array(NT) - np.array(TR))
    return tuple(b + (tp - b) * z / 4)


def fan(c, r, sx=1.0, label=None, loff=(0, 0)):
    cx, cy = c
    ax.add_patch(Ellipse((cx, cy), 2 * r * sx, 2 * r, fc='white', ec='#555555', lw=0.9, zorder=5))
    for k in range(5):
        a = np.radians(90 + 72 * k)
        b = np.linspace(a - 0.42, a + 0.42, 12)
        pts = [(cx, cy)] + [(cx + 0.92 * r * sx * np.cos(t), cy + 0.92 * r * np.sin(t)) for t in b]
        ax.add_patch(Polygon(pts, fc='#f08a24', ec='#c25e0c', lw=0.5, zorder=6))
    ax.add_patch(Ellipse((cx, cy), 0.6 * r * sx, 0.6 * r, fc='#333333', ec='none', zorder=7))
    for k in range(8):
        a = np.radians(22.5 * k)
        ax.plot([cx - r * sx * np.cos(a), cx + r * sx * np.cos(a)], [cy - r * np.sin(a), cy + r * np.sin(a)],
                color='#777777', lw=0.35, zorder=8)
    if label:
        txt(ax, cx + loff[0], cy + loff[1], label, size=14, weight='bold')


fan(back(4, 3), 4.6, label='$A$', loff=(-7.5, 0))
fan(side(3, 2.5), 4.6, sx=0.62, label='$B$', loff=(-5.5, 3.5))
# 8 m dimension
y8 = back(0, 1.6)[1]
arr(ax, 39, y8, BL[0] + 0.3, y8, color='#d32f2f', lw=1.3, head=7)
arr(ax, 39, y8, BR[0] - 0.3, y8, color='#d32f2f', lw=1.3, head=7)
txt(ax, 39, y8 + 3.2, '8 m', size=13, color='#d32f2f')
# axes
O = np.array(BR, float)
arr(ax, *O, 46, BR[1], lw=1.6, head=8, z=9)
arr(ax, *O, 72, 47, lw=1.6, head=8, z=9)
yend = O + 0.92 * (np.array(NB) - O)
arr(ax, *O, *yend, lw=1.6, head=8, z=9)
txt(ax, O[0] - 2.2, O[1] - 2.6, '$O$', size=13)
txt(ax, 47, BR[1] + 2.6, '$x$', size=13)
txt(ax, 69.8, 46, '$z$', size=13)
txt(ax, yend[0] - 1, yend[1] - 2.8, '$y$', size=13)
save(fig, 'img083')
