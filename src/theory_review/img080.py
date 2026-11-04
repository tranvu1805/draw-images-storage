from graphs_kit import *
setfs(10)

# y = -x^3 + 3x^2 - 4: CT (0;-4), CĐ (2;0), crosses Ox at -1 (and touches at 2)
fig, ax = win('img080', (114, 129), 33.5)
hline(ax, 0, lw=1.0)
vline(ax, 0, lw=1.0)
xt(ax, [-3, -2, -1, 1, 2, 3, 4], pos='b', size=2.5, d=(-3, 0))
xt(ax, [0], ['0'], pos='bl', style=None, d=(-1, 0))
yt(ax, [3, 2, 1, -1, -2, -3, -4], size=2.5, d=(-1, -1))
curve(ax, lambda x: -x**3 + 3 * x**2 - 4, -1.36, 3.12, lw=1.8)
save(fig, 'img080')
