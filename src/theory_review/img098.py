# Four ways of placing a thermometer in a beaker of water (A: bulb on the bottom, B: bulb in the middle
# of the water, C: bulb at the surface, D: tilted, bulb near the bottom) - positions kept as in the source.
from photo_kit import *

fig, ax = board('img098', 100)            # y 0..32.7
Y0, Y1, LEV = 6.0, 24.5, 19.0             # beaker bottom, rim, water level
HW = 7.5                                  # half width


def beaker(c):
    ax.add_patch(Rectangle((c - HW, Y0), 2 * HW, LEV - Y0, fc='#dcebf6', ec='none', zorder=1))
    ax.plot([c - HW, c + HW], [LEV, LEV], color='#9cc1de', lw=0.9, zorder=2)
    ax.add_patch(FancyBboxPatch((c - HW, Y0), 2 * HW, Y1 - Y0, boxstyle='round,pad=0,rounding_size=1.2',
                                fc='none', ec='#555555', lw=1.2, zorder=5))
    ax.plot([c - HW - 0.9, c + HW + 0.9], [Y1, Y1], color='#555555', lw=1.8, zorder=6, solid_capstyle='round')
    ax.add_patch(Rectangle((c - HW - 0.9, Y1 - 0.9), 2 * HW + 1.8, 0.9, fc='white', ec='none', zorder=4))


def thermometer(bulb, top):
    b, t = np.array(bulb, float), np.array(top, float)
    d = (t - b) / np.linalg.norm(t - b)
    n = np.array([-d[1], d[0]])
    w = 0.42
    body = [b + n * w, t + n * w, t - n * w, b - n * w]
    ax.add_patch(Polygon(body, fc='#f7f7f7', ec='#555555', lw=0.7, zorder=7))
    L = np.linalg.norm(t - b)
    for k in range(4, int(L / 0.9)):
        p = b + d * k * 0.9
        q = p + n * (0.42 if k % 5 == 0 else 0.25)
        ax.plot([p[0], q[0]], [p[1], q[1]], color='#666666', lw=0.4, zorder=8)
    m = b + d * 5.0
    ax.plot([b[0], m[0]], [b[1], m[1]], color='#d32f2f', lw=1.2, zorder=8)
    ax.add_patch(Circle(b, 0.85, fc='#d9534f', ec='#555555', lw=0.7, zorder=9))


xs = [12.5, 37.5, 62.5, 87.5]
for c in xs:
    beaker(c)
thermometer((xs[0], Y0 + 0.85), (xs[0], 32))            # A: bulb touching the bottom
thermometer((xs[1], 12.0), (xs[1], 32))                 # B: bulb in the middle of the water
thermometer((xs[2], LEV), (xs[2], 32))                  # C: bulb at the water surface
thermometer((xs[3] - 4.2, 8.6), (xs[3] + 7.0, 31.5))    # D: tilted, bulb near the bottom
for c, s in zip(xs, 'ABCD'):
    txt(ax, c, 2, f'Hình {s}.', size=13)
save(fig, 'img098')
