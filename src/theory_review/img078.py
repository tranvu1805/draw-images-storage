from graphs_kit import *
setfs(16)

# y = x^2/(x - 1) = x + 1 + 1/(x - 1) (a = 0, b = -1): TCĐ x = 1, TCX y = x + 1 through (0;1), (1;2); CĐ at O
fig, ax = win('img078', (107, 218), 30.5)
axes(ax, (-3.51, 5.93), (-2.69, 7.05), xname=None, yname=None, origin=None, lw=1.1)
box = (-3.6, 5.6, -2.69, 6.8)
dash(ax, [(1, -2.69), (1, 6.8)], lw=1.1)
curve(ax, lambda x: x + 1, -3.6, 5.6, lw=1.0, ls=(0, (2.5, 2)), box=box)
dash(ax, [(0, 2), (1, 2)])
f = lambda x: x + 1 + 1 / (x - 1)
curve(ax, f, -3.6, 0.999, box=box)
curve(ax, f, 1.001, 5.6, box=box)
for p in [(0, 2), (1, 2), (0, 1), (0, 0)]:
    ax.plot(*p, 'o', ms=4, color=INK, zorder=6)
T(ax, 0.3, 6.9, '$y$', fs=17)
T(ax, 5.75, 0.45, '$x$', fs=17)
T(ax, -0.25, 2.0, '$2$', ha='right')
T(ax, -0.25, 1.0, '$1$', ha='right')
T(ax, 0.35, 0.4, '$O$')
T(ax, 1.25, -2.15, '$x=1$', ha='left')
save(fig, 'img078')
