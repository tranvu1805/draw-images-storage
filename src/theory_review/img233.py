from graphs_kit import *
setfs(16)

# y = -x^3 + 3x + 1: CT (-1;-1), CĐ (1;3), y-intercept 1 (no numbers shown in the original)
fig, ax = win('img233', (149, 219), (53, 54))
axes(ax, (-2.77, 3.42), (-2.02, 3.74), xname=None, yname=None, origin=None, lw=1.4, head=8)
curve(ax, lambda x: -x**3 + 3 * x + 1, -2.05, 2.04, lw=1.4)
T(ax, 0.4, 3.55, '$y$', fs=17)
T(ax, 3.2, 0.4, '$x$', fs=17)
T(ax, 0.3, -0.3, '$O$')
save(fig, 'img233')
