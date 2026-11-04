from graphs_kit import *
setfs(14)

# y = f'(x) = -1 - x^2 (x-1)(x-2) q(x), q > 0: f' = -1 at x = 0 (touch), 1, 2; max near x = 1.64
fig, ax = win('img049', (70, 70), (50, 48))
axes(ax, (-0.9, 3.0), (-2.7, 1.25), xname=None, yname=None, origin=None)
fp = lambda x: -1 - x**2 * (x - 1) * (x - 2) * (0.87 + 0.12 * (x - 1.4)**2)
dash(ax, [(1, 0), (1, -1)])
dash(ax, [(2, 0), (2, -1)])
dash(ax, [(0, -1), (2, -1)])
curve(ax, fp, -0.56, 2.24)
xm = 1.64
for p in [(0, -1), (1, -1), (2, -1), (xm, fp(xm))]:
    ax.plot(*p, 'o', ms=3.5, color=INK, mec='none', zorder=6)
T(ax, -0.25, 1.15, '$y$', fs=15, ha='right')
T(ax, 2.95, 0.3, '$x$', fs=15)
T(ax, -0.2, 0.3, '$O$')
T(ax, 1, 0.3, '$1$')
T(ax, 2, 0.3, '$2$')
T(ax, -0.12, -0.9, '$-1$', ha='right')
save(fig, 'img049')
