from graphs_kit import *
setfs(18)

# y = f(x) = 0.404 (x + 2)(x - 1)(x - 3): roots -2, 1, 3; region between the curve and Ox on [-2;3] hatched
fig, ax = win('img197', (152, 222), (48.7, 49))
f = lambda x: 0.404 * (x + 2) * (x - 1) * (x - 3)
hatch(ax, region(f, -2, 3), 0.17, angle=74, lw=0.75)
axes(ax, (-3.02, 4.31), (-2.0, 3.92), xname=None, yname=None, origin=None, lw=1.4, head=8)
yt(ax, [-1, 1, 2, 3], [''] * 4, size=2.5)
curve(ax, f, -2.2, 3.57, lw=2.0)
T(ax, 0.42, 3.75, '$y$', fs=19)
T(ax, 4.2, 0.45, '$x$', fs=19)
T(ax, 2.55, 3.3, '$y=f(x)$')
T(ax, -2.35, 0.3, '$-2$', ha='center')
T(ax, -0.3, -0.42, '$O$')
T(ax, 0.9, -0.5, '$1$')
T(ax, 3.25, -0.48, '$3$')
save(fig, 'img197')
