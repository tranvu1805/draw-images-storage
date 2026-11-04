from graphs_kit import *
setfs(16)

# y = x^4 - 2x^2: CĐ (0;0), CT (±1;-1), min = -1
fig, ax = win('img087', (130, 81), 60)
axes(ax, (-2.0, 1.78), (-1.52, 0.8), xname=None, yname=None, origin=None, lw=1.1)
dash(ax, [(-1, 0), (-1, -1), (1, -1), (1, 0)], lw=1.1)
curve(ax, lambda x: x**4 - 2 * x**2, -1.55, 1.55)
xt(ax, [-1, 1], ['', ''])
yt(ax, [-1], [''])
T(ax, -0.2, 0.75, '$y$', fs=17)
T(ax, 1.75, -0.3, '$x$', fs=17)
T(ax, -0.9, 0.32, '$-1$')
T(ax, 0.25, 0.27, '$O$')
T(ax, 1.0, 0.3, '$1$')
T(ax, 0.1, -1.3, '$-1$', ha='left')
save(fig, 'img087')
