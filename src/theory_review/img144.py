# Cladogram (diagonal): lamprey ... chimpanzee with derived traits marked on the stem.
from photo_kit import *

fig, ax = board('img144', 100)            # y 0..66.4
T = 54                                    # tip height
R, E = np.array([28.0, 1.0]), np.array([97.0, 44.0])
u = (E - R) / np.linalg.norm(E - R)
nrm = np.array([-u[1], u[0]])
bd = np.array([-0.62, 1.0])               # branch direction (up-left)
names = ['Lươn', 'Cá rô', 'Kỳ nhông', 'Thằn lằn', 'Bồ câu', 'Chuột']
fr = [0.08, 0.22, 0.36, 0.50, 0.64, 0.80]
nodes = [R + f * (E - R) for f in fr]
ax.plot([R[0], E[0]], [R[1], E[1]], color=INK, lw=1.6, solid_capstyle='round')
tips = []
for i, (n, s) in enumerate(zip(nodes, names)):
    t = (T - n[1]) / bd[1]
    tip = n + t * bd
    tips.append(tip)
    ax.plot([n[0], tip[0]], [n[1], tip[1]], color=INK, lw=1.4, solid_capstyle='round')
    txt(ax, tip[0], T + (2.4 if i % 2 == 0 else 6.6), s, size=11, weight='bold')
txt(ax, E[0] - 2, E[1] + 3.2, 'Tinh tinh', size=11, weight='bold', ha='center')


def tick(p, s, off, ha='center'):
    ax.plot([p[0] - nrm[0] * 1.8, p[0] + nrm[0] * 1.8], [p[1] - nrm[1] * 1.8, p[1] + nrm[1] * 1.8], color=INK,
            lw=1.7)
    txt(ax, p[0] + off[0], p[1] + off[1], s, size=11, weight='bold', ha=ha, va='top', linespacing=1.05)


mid = lambda a, b: (nodes[a] + nodes[b]) / 2
tick(mid(0, 1), 'Hàm', (1.5, -3.2))
tick(mid(1, 2), 'Phổi', (1.5, -3.2))
tick(mid(2, 3), 'Móng\nngón tay', (0.2, -3.0), ha='left')
tick(mid(4, 5), 'Lông, tuyến\nvú', (0.2, -3.0), ha='left')
# feathers: tick on the pigeon branch
p = nodes[4] + 0.35 * (tips[4] - nodes[4])
bu = bd / np.linalg.norm(bd)
bn = np.array([bu[1], -bu[0]])
ax.plot([p[0] - bn[0] * 1.8, p[0] + bn[0] * 1.8], [p[1] - bn[1] * 1.8, p[1] + bn[1] * 1.8], color=INK, lw=1.7)
txt(ax, p[0] - 2.8, p[1] + 0.5, 'Lông vũ', size=11, weight='bold', ha='right', va='center')
save(fig, 'img144')
