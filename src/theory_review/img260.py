from graphs_kit import *
setfs(14)

# y = -x^4 + 2x^2 + 1: CĐ (±1;2), CT (0;1)
fig, ax = win('img260', (140, 133), 41)
axes(ax, (-2.44, 2.98), (-1.1, 2.95), xname=None, yname=None, origin=None, lw=1.2, head=8)
dash(ax, [(-1, 0), (-1, 2), (1, 2), (1, 0)], lw=1.1)
curve(ax, lambda x: -x**4 + 2 * x**2 + 1, -1.67, 1.67, lw=1.6)
for p in [(-1, 2), (0, 2), (1, 2), (0, 1), (-1, 0), (1, 0)]:
    ax.plot(*p, 'o', ms=4, color=INK, mfc='white', mew=0.9, zorder=6)
T(ax, -0.3, 2.8, '$y$', fs=15)
T(ax, 2.8, -0.32, '$x$', fs=15)
T(ax, 0.2, 2.2, '$2$', ha='left')
T(ax, 0.24, 1.45, '$1$')
T(ax, -1.0, -0.3, '$-1$')
T(ax, -0.25, -0.3, '$O$')
T(ax, 1.0, -0.3, '$1$')
save(fig, 'img260')
