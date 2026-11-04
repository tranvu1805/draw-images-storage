from graphs_kit import *
setfs(14)

# y = x^3/4 - 3x^2/4 + 2: CĐ (0;2), CT (2;1), through (-2;-3) and (4;6)
fig, ax = win('img040', (173, 221), (42, 33))
axes(ax, (-2.86, 4.4), (-3.55, 6.6), xname=None, yname=None, origin=None)
f = lambda x: x**3 / 4 - 3 * x**2 / 4 + 2
dash(ax, [(-2, 0), (-2, -3), (0, -3)])
dash(ax, [(0, 1), (2, 1), (2, 0)])
dash(ax, [(0, 6), (4, 6), (4, 0)])
curve(ax, f, -2.12, 4.1)
for p in [(-2, -3), (2, 1), (4, 6)]:
    ax.plot(*p, 'o', ms=5, color=INK, zorder=6)
T(ax, -0.3, 6.0, '$6$', ha='right')
T(ax, -0.3, 2.35, '$2$', ha='right')
T(ax, -0.3, 1.0, '$1$', ha='right')
T(ax, 0.25, -3.0, '$-3$', ha='left')
T(ax, -2.4, 0.4, '$-2$')
T(ax, 0.3, -0.45, '$O$')
T(ax, 2, -0.6, '$2$')
T(ax, 4, -0.6, '$4$')
T(ax, 4.45, 0.25, '$x$', fs=15, ha='left')
T(ax, 0.2, 6.45, '$y$', fs=15, ha='left')
save(fig, 'img040')
