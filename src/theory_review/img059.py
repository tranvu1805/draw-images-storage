from graphs_kit import *
setfs(16)

# y = x - 1 + k/(x - 2) = (x^2 - 3x + 2 + k)/(x - 2), k = 1.74: TCĐ x = 2, TCX y = x - 1
fig, ax = win('img059', (66, 197), 28)
axes(ax, (-2.07, 7.04), (-6.04, 6.39), xname=None, yname=None, origin=None, lw=1.1)
k = 1.74
box = (-2.1, 7.04, -6.04, 6.39)
f = lambda x: x - 1 + k / (x - 2)
vline(ax, 2, -6.04, 6.39, lw=1.4)
curve(ax, lambda x: x - 1, -2.07, 7.1, lw=1.1, box=box)
curve(ax, f, -2.07, 1.999, box=box)
curve(ax, f, 2.001, 7.04, box=box)
for x in (2 - k**0.5, 2 + k**0.5):
    dash(ax, [(x, 0), (x, f(x))], lw=1.1)
    ax.plot(x, f(x), 'o', ms=4.5, color=INK, zorder=6)
T(ax, -0.55, 5.95, '$y$', fs=17)
T(ax, 6.6, 0.5, '$x$', fs=17)
T(ax, -0.35, 0.4, '$O$')
T(ax, 1.15, -0.6, '$1$')
T(ax, -0.2, -1.1, '$-1$', ha='right')
T(ax, 2.5, -0.95, '$2$')
save(fig, 'img059')
