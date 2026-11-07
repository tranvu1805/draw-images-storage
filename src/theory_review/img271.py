from graphs_kit import *
setfs(16)

# y = -x^2 + 3 and y = x^2 - 2x - 1 meet at (-1;2) and (2;-1); region between them hatched
fig, ax = win('img271', (147, 180), 45.3)
f = lambda x: -x**2 + 3
g = lambda x: x**2 - 2 * x - 1
hatch(ax, region(f, -1, 2, g), 0.25, angle=-45, lw=0.8)
axes(ax, (-1.52, 3.0), (-2.49, 3.53), xname=None, yname=None, origin=None, lw=1.1)
dash(ax, [(-1, 0), (-1, 2)], lw=1.2)
dash(ax, [(2, 0.12), (2, -1)], lw=1.2)
curve(ax, f, -1.5, 2.21, lw=1.7)
curve(ax, g, -1.19, 3.0, lw=1.7)
T(ax, -0.35, 3.15, '$y$')
T(ax, 2.98, -0.35, '$x$')
T(ax, 2.0, 0.3, '$2$')
T(ax, -1.0, -0.33, '$-1$', bg=True)
T(ax, 0.22, -0.32, '$O$', bg=True)
T(ax, 2.0, 3.0, '$y=-x^2+3$')
T(ax, -1.0, -2.05, '$y=x^2-2x-1$', bg=True)
save(fig, 'img271')
