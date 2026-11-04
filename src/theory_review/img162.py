from graphs_kit import *
setfs(14)

# y = x^3 - 3x^2 + 1: CĐ (0;1), CT (2;-3)
fig, ax = win('img162', (63, 61), (26.5, 27))
axes(ax, (-1.62, 3.77), (-3.52, 1.81), xname=None, yname=None, origin=None, lw=1.1)
dash(ax, [(2, 0), (2, -3), (0, -3)])
curve(ax, lambda x: x**3 - 3 * x**2 + 1, -0.98, 3.0)
for p in [(0, 1), (0, 0), (2, 0), (2, -3), (0, -3)]:
    ax.plot(*p, 'o', ms=3.2, color=INK, zorder=6)
T(ax, 0.42, 1.65, '$y$', fs=15)
T(ax, 3.6, -0.4, '$x$', fs=15)
T(ax, -0.12, 1.3, '$1$', ha='right')
T(ax, 0.38, -0.4, '$O$')
T(ax, 2.0, 0.38, '$2$')
T(ax, -0.15, -3.0, '$-3$', ha='right')
save(fig, 'img162')
