from graphs_kit import *
setfs(14)

# y = x^4 - 2x^2 - 1: CĐ (0;-1), CT (±1;-2); light grid (0.5 / 0.1) as in the original
fig, ax = win('img164', (170, 105), 92)
grid(ax, major=0.5, minor=0.1)
axes(ax, (-1.85, 2.01), (-2.07, 1.01), xname=None, yname=None, origin=None, lw=1.1)
curve(ax, lambda x: x**4 - 2 * x**2 - 1, -1.66, 1.66, lw=2.2)
for p in [(-1, 0), (1, 0), (0, -2)]:
    ax.plot(*p, 'o', ms=4, color=INK, zorder=6)
T(ax, 0.12, 0.92, '$y$', ha='left', fs=15)
T(ax, 1.95, -0.12, '$x$', fs=15)
T(ax, -0.3, -0.12, '$O$')
T(ax, -0.85, -0.37, '$-1$')
T(ax, 1.15, -0.37, '$1$')
T(ax, 0.3, -0.87, '$-1$')
T(ax, 0.3, -1.85, '$-2$')
save(fig, 'img164')
