from tabgeo_kit import *
from matplotlib.patches import Polygon

P = {'E': (153, 62), 'A': (26, 225), 'B': (126, 278), 'C': (274, 200), 'D': (176, 150),
     'a': (26, 388), 'b': (126, 455), 'c': (274, 357), 'd': (176, 292)}
G = Geo('img084', P, fs=16, lw=1.6)
ax = G.ax
a, b, c, d = (G.p(k) for k in 'abcd')
# oblique frame of the platform: s along a->d, t along a->b, h up (all in px)
V = (d - a) / np.linalg.norm(d - a)
U = (b - a) / np.linalg.norm(b - a)
Ls, Lt = np.linalg.norm(d - a), np.linalg.norm(b - a)


def W(s, t, h):
    return a + s * V + t * U + np.array([0, -h])


# platform (slightly larger than the frame's base), 11 px thick
pa, pb, pc, pd = W(-10, -8, 0), W(-10, Lt + 8, 0), W(Ls + 10, Lt + 8, 0), W(Ls + 10, -8, 0)
dn = np.array([0, 11])
ax.add_patch(Polygon([pa, pb, pb + dn, pa + dn], closed=True, fc='#9aa3ab', ec=INK, lw=1.0, zorder=1))
ax.add_patch(Polygon([pb, pc, pc + dn, pb + dn], closed=True, fc='#b9c1c8', ec=INK, lw=1.0, zorder=1))
ax.add_patch(Polygon([pa, pb, pc, pd], closed=True, fc='#5d646b', ec=INK, lw=1.0, zorder=1))
G.seg('D', 'd', zorder=1.5)       # back post, hidden by the car lower down

# the car: a side profile (s, h) extruded across t0..t1, faces drawn back to front
s0, s1, t0, t1 = 15, 175, 30, 100
prof = [(0.00, 8), (0.00, 29), (0.06, 36), (0.22, 41), (0.40, 63), (0.94, 65), (1.00, 52), (1.00, 8)]
prof = [(s0 + q * (s1 - s0), h) for q, h in prof]
eye = np.array([-1.0, 1.012, 1.104])          # direction towards the viewer in (s, t, h)
faces = []
n = len(prof)
for i in range(n):
    (sa, ha), (sb, hb) = prof[i], prof[(i + 1) % n]
    nrm = np.array([-(hb - ha), 0, sb - sa])   # outward normal (profile listed clockwise)
    if nrm @ eye <= 0:
        continue
    quad = [W(sa, t0, ha), W(sb, t0, hb), W(sb, t1, hb), W(sa, t1, ha)]
    depth = -np.array([(sa + sb) / 2, (t0 + t1) / 2, (ha + hb) / 2]) @ eye
    glass = i == 3
    faces.append((depth, quad, '#dfe6ec' if glass else 'white'))
for depth, quad, fc in sorted(faces, key=lambda f: -f[0]):
    ax.add_patch(Polygon(quad, closed=True, fc=fc, ec=INK, lw=1.2, zorder=2))
side = [W(s, t1, h) for s, h in prof]
ax.add_patch(Polygon(side, closed=True, fc='white', ec=INK, lw=1.3, zorder=2.1))
q = lambda f, h: W(s0 + f * (s1 - s0), t1, h)
ax.add_patch(Polygon([q(0.26, 44), q(0.42, 60), q(0.91, 61), q(0.96, 46)], closed=True, fc='#dfe6ec',
                     ec=INK, lw=1.1, zorder=2.2))
for f in (0.55, 0.75):
    ax.plot(*zip(q(f, 44), q(f, 61)), color=INK, lw=1.1, zorder=2.3)
    ax.plot(*zip(q(f, 44), q(f + 0.01, 16)), color=INK, lw=0.9, zorder=2.3)
# headlight on the front face
hl = [W(s0, t1 - 4, 28), W(s0, t1 - 20, 28), W(s0, t1 - 20, 21), W(s0, t1 - 4, 21)]
ax.add_patch(Polygon(hl, closed=True, fc='#f0d77a', ec=INK, lw=0.8, zorder=2.3))
ph = np.linspace(0, 2 * np.pi, 60)
for sc in (42, 155):
    for r, fc in ((13, '#333333'), (6, '#e6e6e6')):
        pts = np.array([W(sc + r * np.cos(p), t1 + 1, 13 + r * np.sin(p)) for p in ph])
        ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.9, zorder=2.4))

# frame and slings
G.edges('A-B B-C C-D D-A A-a B-b C-c', zorder=3)
for k in 'ABCD':
    G.seg('E', k, zorder=3)
for k, t in (('A', 0.27), ('B', 0.27), ('D', 0.27), ('C', 0.33)):
    G.head('E', k, L=11, w=4.2, at=t)
for k in 'ABCD':
    G.dot(k, r=4)
# crane hook block
ax.plot([146, 146], [12, 30], color=INK, lw=1.4)
ax.plot([160, 160], [12, 30], color=INK, lw=1.4)
ax.add_patch(Polygon([(141, 28), (165, 28), (162, 50), (144, 50)], closed=True, fc='#e8c33a', ec=INK, lw=1.0,
                     zorder=3))
G.dot('E', r=6)
T = lambda x, y, s: G.text(x, y, s, fs=16)
T(103, 96, r'$\vec{F}_1$')
T(133, 123, r'$\vec{F}_2$')
T(183, 124, r'$\vec{F}_4$')
T(210, 92, r'$\vec{F}_3$')
G.labs({'A': ('w', 15), 'B': (235, 16), 'C': ('e', 15), 'D': (155, 17), 'E': (175, 20)})
G.save()
