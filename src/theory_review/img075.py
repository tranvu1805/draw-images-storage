# Hip roof of a house: a sketch of the house (left) and the roof polyhedron on Oxyz (right).
from photo_kit import *

fig, ax = board('img075', 100)            # y 0..34.3

# ---------------------------------------------------------------- house sketch (left)
hO = np.array([31.0, 8.5])
hx, hy, hz = np.array([-1.55, 0.25]), np.array([0.62, -0.5]), np.array([0.0, 1.45])
P = lambda x, y, z: hO + x * hx + y * hy + z * hz
Wd, Hw, Hr = 4.0, 4.6, 8.6                   # half depth, wall height, ridge height
# walls: hx points left, so the house runs x = 0 (right end) .. 13 (left end)
X0, X1 = 0.0, 13.0
front = [P(X0, Wd, 0), P(X1, Wd, 0), P(X1, Wd, Hw), P(X0, Wd, Hw)]
end = [P(X1, -Wd, 0), P(X1, Wd, 0), P(X1, Wd, Hw), P(X1, -Wd, Hw)]
poly(ax, end, fc='#b5653f', ec='#5a2f1c', lw=0.8, z=2)
poly(ax, front, fc='#c4734b', ec='#5a2f1c', lw=0.8, z=2)
# brick hint lines on the walls
for k in range(1, 9):
    z = Hw * k / 9
    ax.plot(*zip(P(X0, Wd, z), P(X1, Wd, z)), color='#a75b37', lw=0.4, zorder=2)
    ax.plot(*zip(P(X1, -Wd, z), P(X1, Wd, z)), color='#9a5332', lw=0.4, zorder=2)
# stone base
poly(ax, [P(X0, Wd, 0), P(X1, Wd, 0), P(X1, Wd, 0.7), P(X0, Wd, 0.7)], fc='#9e9e9e', ec='#555555', lw=0.5, z=3)
poly(ax, [P(X1, -Wd, 0), P(X1, Wd, 0), P(X1, Wd, 0.7), P(X1, -Wd, 0.7)], fc='#8e8e8e', ec='#555555', lw=0.5, z=3)
# garage doors, door, windows on the front wall


def opening(xa, xb, za, zb, fc, ec='#555555', lines=0):
    poly(ax, [P(xa, Wd, za), P(xb, Wd, za), P(xb, Wd, zb), P(xa, Wd, zb)], fc=fc, ec=ec, lw=0.6, z=4)
    for k in range(1, lines + 1):
        z = za + (zb - za) * k / (lines + 1)
        ax.plot(*zip(P(xa, Wd, z), P(xb, Wd, z)), color='#b8ad8c', lw=0.4, zorder=5)


opening(12.4, 9.6, 0.7, 3.6, '#e9dfc0', lines=4)
opening(9.0, 6.0, 0.7, 3.6, '#e9dfc0', lines=4)
opening(5.2, 4.2, 0.7, 3.4, '#6b2a1a')
for xa in (3.4, 2.2, 1.0):
    opening(xa, xa - 0.8, 1.8, 3.4, '#5b7fae')
# hip roof: eaves overhang, ridge
e = 0.6
c = [P(X0 - e, -Wd - e, Hw), P(X1 + e, -Wd - e, Hw), P(X1 + e, Wd + e, Hw), P(X0 - e, Wd + e, Hw)]
r0, r1 = P(X0 + 3.4, 0, Hr), P(X1 - 3.4, 0, Hr)
ROOF, ROOF2, ROOF3 = '#b4532a', '#c9643a', '#9c4421'
poly(ax, [c[0], c[1], r1, r0], fc=ROOF3, ec='#4a1f0e', lw=0.8, z=6)               # back slope
poly(ax, [c[3], c[0], r0], fc=ROOF3, ec='#4a1f0e', lw=0.8, z=6)                    # right hip
poly(ax, [c[3], c[2], r1, r0], fc=ROOF2, ec='#4a1f0e', lw=0.8, z=7)               # front slope
poly(ax, [c[2], c[1], r1], fc=ROOF, ec='#4a1f0e', lw=0.8, z=7)                    # left hip
for k in range(1, 7):   # tile rows
    t = k / 7
    a, b = c[3] + (r0 - c[3]) * t, c[2] + (r1 - c[2]) * t
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#8f3c1b', lw=0.4, zorder=8)
    a, b = c[2] + (r1 - c[2]) * t, c[1] + (r1 - c[1]) * t
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#7f3517', lw=0.4, zorder=8)
# fascia
ax.plot(*zip(c[3], c[2], c[1]), color='#e8e8e8', lw=1.6, zorder=8)

# ---------------------------------------------------------------- roof on Oxyz (right)
O = np.array([55.5, 12.0])
ex, ey, ez = np.array([-3.25, 0.42]), np.array([1.3, -2.25]), np.array([0.38, 3.9])
Q = lambda x, y, z: O + x * ex + y * ey + z * ez
pts = {'O': (0, 0, 0), 'S': (0, 0, 3), 'K': (-8, 0, 3), 'M': (2, -2, 0), 'N': (2, 2, 0), 'I': (2, 0, 0),
       'D': (0, -2, 0), 'A': (0, 2, 0), 'B': (-8, 2, 0), 'C': (-8, -2, 0), 'E': (-10, 2, 0), 'F': (-10, -2, 0)}
p = {k: Q(*v) for k, v in pts.items()}
LW = 1.1
for a, b in [s.split('-') for s in 'S-M S-N S-A S-K K-E K-B M-N N-A A-B B-E'.split()]:
    ax.plot(*zip(p[a], p[b]), color=INK, lw=LW, zorder=10, solid_capstyle='round')
for a, b in [s.split('-') for s in 'S-D M-D D-C C-F F-E K-C K-F S-O O-I O-A'.split()]:
    ax.plot(*zip(p[a], p[b]), color=INK, lw=LW * 0.85, ls=(0, (3.5, 2.5)), zorder=10)
# axes beyond the solid
for a, end, name, off in (('I', Q(4.6, 0, 0), 'x', (-1.2, 0.2)), ('A', Q(0, 4.4, 0), 'y', (1.0, -0.6)),
                          ('S', Q(0, 0, 4.6), 'z', (1.2, -0.3))):
    arr(ax, p[a][0], p[a][1], end[0], end[1], lw=1.0, head=6, z=9)
    txt(ax, end[0] + off[0], end[1] + off[1], f'${name}$', size=12)
lab = {'S': ('$S(0;0;3)$', (0.6, 1.1), 'left'), 'K': ('$K$', (0, 1.3), 'center'), 'M': ('$M(2;-2;0)$', (-0.8, 0.4), 'right'),
       'N': ('$N$', (-1.0, -0.8), 'right'), 'I': ('$I(2;0;0)$', (-0.9, -1.0), 'right'), 'D': ('$D$', (-0.5, 1.2), 'right'),
       'O': ('$O$', (0.9, 0.2), 'left'), 'A': ('$A(0;2;0)$', (0.7, 0.3), 'left'),
       'B': ('$B(-8;2;0)$', (-0.8, -1.4), 'center'), 'C': ('$C$', (-0.8, 1.0), 'center'),
       'F': ('$F$', (1.0, 0.4), 'left'), 'E': ('$E(-10;2;0)$', (0.5, -1.3), 'left')}
for k, (s, (dx, dy), ha) in lab.items():
    txt(ax, p[k][0] + dx, p[k][1] + dy, s, size=10.5, ha=ha, zorder=12)
save(fig, 'img075')
