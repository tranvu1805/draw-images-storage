from graphs_kit import *

# temperature–time sketch: Đường 3 has a melting plateau at t_c (crystalline), Đường 2 rises smoothly
# (amorphous), Đường 1 is horizontal then vertical then rising. Coordinates in the original's pixel frame.
fid = 'img099'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
P = lambda x, y: (x, H - y)
ap = dict(arrowstyle='-|>,head_length=0.9,head_width=0.4', color=INK, lw=1.6, shrinkA=0, shrinkB=0,
          mutation_scale=10)
ax.annotate('', xy=P(47, 18), xytext=P(47, 212), arrowprops=ap)
ax.annotate('', xy=P(287, 210), xytext=P(44, 210), arrowprops=ap)
tc = 131
dash(ax, [P(55, tc), P(112, tc)], lw=1.0, ls=(0, (3, 3)))
# Đường 3 (solid): rise, plateau at t_c, rise
x3 = [82, 96, 104, 112, 120, 200, 212, 222, 230]
y3 = [172, 162, 146, 134, 131, 131, 126, 108, 78]
from matplotlib.path import Path
from matplotlib.patches import PathPatch
def smooth(xs, ys):
    t = np.linspace(0, 1, len(xs))
    tt = np.linspace(0, 1, 400)
    m = lambda v: hermite(t, v, np.gradient(v, t))
    fx, fy = m(np.array(xs, float)), m(np.array(ys, float))
    return np.array([fx(u) for u in tt]), np.array([fy(u) for u in tt])
sx, sy = smooth([82, 92, 100, 108, 116, 125, 160, 195, 205, 214, 222, 230],
                [172, 168, 156, 140, 132, 131, 131, 131, 129, 121, 104, 78])
ax.plot(sx, H - sy, color=INK, lw=2.3)
# Đường 2 (round dots): smooth rise from the start to the liquid
qx, qy = smooth([88, 125, 160, 190, 213], [171, 152, 131, 106, 82])
ax.plot(qx, H - qy, color=INK, lw=3.2, ls=(0, (0.1, 2.2)), dash_capstyle='round')
# Đường 1 (dashes): horizontal, vertical at x = 183, then rising
ax.plot(*zip(P(92, 173), P(183, 173), P(183, 113), P(226, 80)), color=INK, lw=2.0, ls=(0, (2.0, 2.2)))
# leader lines
for a, b in [((148, 103), (163, 127)), ((222, 117), (237, 133)), ((183, 160), (196, 172))]:
    ax.plot(*zip(P(*a), P(*b)), color=INK, lw=0.9)
kw = dict(fontsize=17, ha='center', va='center')
ax.text(*P(130, 92), 'Đường 2', **kw)
ax.text(*P(283, 138), 'Đường 3', **kw)
ax.text(*P(243, 178), 'Đường 1', **kw)
ax.text(*P(242, 60), 'Lỏng', **kw)
ax.text(*P(82, 195), 'Rắn', **kw)
ax.text(*P(253, 240), 'Thời gian', **kw)
ax.text(*P(46, 236), '0', **kw)
ax.text(*P(19, 58), 'Nhiệt độ', rotation=90, **kw)
ax.text(*P(29, 133), '$t_c$', **kw)
save(fig, fid)
