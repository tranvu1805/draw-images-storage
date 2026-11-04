from graphs_kit import *
setfs(14)

# y = x^3 - 3x^2 + 2: CĐ (0;2), CT (2;-2), through (1;0), (-1;-2); light grid as in the original
fig, ax = win('img073', (98, 195), 48.75)
grid(ax, major=1, minor=0.2)
axes(ax, (-2.01, 4.96), (-2.5, 3.96), xname=None, yname=None, origin=None, lw=1.1)
dash(ax, [(0, -2), (2, -2), (2, 0)], lw=1.3)
curve(ax, lambda x: x**3 - 3 * x**2 + 2, -1.07, 3.21)
for x in (-1, 0, 1):
    ax.plot(x, 0, 'o', ms=4, color=INK, zorder=6)
T(ax, 0.25, 3.75, '$y$', fs=15)
T(ax, 4.75, 0.25, '$x$', fs=15)
T(ax, 0.17, 2.2, '$2$')
T(ax, -1.1, 0.22, '$-1$')
T(ax, 0.25, -0.28, '$O$')
T(ax, 1.08, 0.22, '$1$')
T(ax, 2.0, 0.22, '$2$')
T(ax, -0.15, -2.0, '$-2$', ha='right')
save(fig, 'img073')
