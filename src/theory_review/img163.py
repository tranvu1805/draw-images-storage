from graphs_kit import *
setfs(14)

# y = x^3 - 3x + 1: CĐ (-1;3), CT (1;-1); light grid (unit / 0.2) as in the original
fig, ax = win('img163', (139, 229), 56.5)
grid(ax, major=1, minor=0.2)
axes(ax, (-2.46, 2.85), (-2.02, 3.84), xname=None, yname=None, origin=None, lw=1.1)
curve(ax, lambda x: x**3 - 3 * x + 1, -2.12, 2.08, lw=2.2)
for x in (-2, -1, 1, 2):
    ax.plot(x, 0, 'o', ms=4, color=INK, zorder=6)
for y in (3, -1):
    ax.plot(0, y, 'o', ms=4, color=INK, zorder=6)
for x, s in [(-1.67, '$-2$'), (-0.75, '$-1$'), (1.2, '$1$'), (2.2, '$2$')]:
    T(ax, x, -0.32, s)
T(ax, -0.25, -0.2, '$O$')
T(ax, 2.7, -0.25, '$x$', fs=15)
T(ax, 0.23, 3.7, '$y$', fs=15)
T(ax, 0.28, 3.2, '$3$')
T(ax, 0.38, -0.82, '$-1$')
save(fig, 'img163')
