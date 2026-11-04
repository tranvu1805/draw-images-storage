from graphs_kit import *
setfs(17)

# even curve: f(0) = 2 (CĐ), CT (±2;-2), passes (±3;4)  (sextic fitted to these points)
fig, ax = win('img207', (111, 114), (25.6, 17))
a, b, c = -0.0011111, 0.2588889, -2.0177778
f = lambda x: a * x**6 + b * x**4 + c * x**2 + 2
axes(ax, (-4.34, 4.65), (-3.41, 6.59), xname=None, yname=None, origin=None, lw=1.4, head=8)
dash(ax, [(-3, 0), (-3, 4), (3, 4), (3, 0)], lw=1.3)
dash(ax, [(-2, 0), (-2, -2), (2, -2), (2, 0)], lw=1.3)
curve(ax, f, -3.2, 3.2, lw=1.8)
for x in (-3, 3):
    ax.plot(x, 4, 'o', ms=4, color=INK, zorder=6)
T(ax, -0.55, 6.15, '$y$', fs=18)
T(ax, 4.3, 0.95, '$x$', fs=18)
T(ax, 0.55, 4.6, '$4$')
T(ax, 0.45, 2.45, '$2$')
T(ax, -2.2, 0.75, '$-2$')
T(ax, 2.0, 0.75, '$2$')
T(ax, -3.5, -0.95, '$-3$')
T(ax, -0.55, -0.95, '$O$')
T(ax, 3.0, -0.95, '$3$')
T(ax, -0.15, -2.85, '$-2$', ha='right')
save(fig, 'img207')
