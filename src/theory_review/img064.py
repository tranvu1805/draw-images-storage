from graphs_kit import *
setfs(17)

# y = -x^3 + 3x^2 + 1: CT (0;1), CĐ (2;5); shaded: under the curve for 0 <= x <= 2
fig, ax = win('img064', (69, 241), 39.3)
f = lambda x: -x**3 + 3 * x**2 + 1
fill_between(ax, f, 0, 2, color='#fbd3b4')
axes(ax, (-1.55, 3.94), (-0.99, 6.0), xname=None, yname=None, origin=None, lw=1.1)
dash(ax, [(0, 5), (2, 5)], lw=1.1)
seg(ax, [(2, 0), (2, 5)], lw=1.2)
curve(ax, f, -1.12, 3.25)
ax.plot(2, 0, 'o', ms=4, color=INK, zorder=6)
T(ax, 0.35, 5.85, '$y$', fs=18)
T(ax, 3.75, 0.45, '$x$', fs=18)
T(ax, -0.3, 5.0, '$5$', ha='right')
T(ax, -0.3, 0.7, '$1$', ha='right')
T(ax, -0.35, -0.5, '$O$')
T(ax, 2.0, -0.5, '$2$')
save(fig, 'img064')
