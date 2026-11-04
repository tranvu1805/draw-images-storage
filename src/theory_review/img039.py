from graphs_kit import *
setfs(18)

# y = x^3 - 3x^2 + 3: CĐ (0;3), CT (2;-1)
fig, ax = win('img039', (84, 202), (43.5, 44))
axes(ax, (-1.1, 4.0), (-1.5, 3.95), xname=None, yname=None, origin=None)
dash(ax, [(0, -1), (2, -1), (2, 0)])
curve(ax, lambda x: x**3 - 3 * x**2 + 3, -1.07, 3.1)
for p in [(0, 0), (2, 0), (0, -1), (2, -1)]:
    ax.plot(*p, 'o', ms=3, color=INK, mec='none', zorder=6)
T(ax, 0.42, 3.92, '$y$')
T(ax, 3.95, -0.42, '$x$')
T(ax, -0.52, 3.12, '$3$')
T(ax, 2.0, 0.37, '$2$')
T(ax, -0.28, -0.3, '$O$')
T(ax, -0.15, -1.0, '$-1$', ha='right')
save(fig, 'img039')
