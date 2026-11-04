from graphs_kit import *
setfs(17)

# y = -x^3 + 3x - 2 = -(x-1)^2 (x+2): CT (-1;-4), CĐ (1;0), y-intercept -2
fig, ax = win('img054', (139, 105), 40)
axes(ax, (-3.1, 2.65), (-4.8, 2.55), xname=None, yname=None, origin=None)
dash(ax, [(-1, 0), (-1, -4), (0, -4)], lw=1.1)
curve(ax, lambda x: -x**3 + 3 * x - 2, -2.22, 2.2)
yt(ax, [1, -1, -2], ['', '', ''])
T(ax, -0.5, 2.25, '$y$', fs=18)
T(ax, 2.45, -0.6, '$x$', fs=18)
T(ax, -0.25, 1.0, '$1$', ha='right')
T(ax, -0.32, -0.6, '$O$')
T(ax, -2.6, -0.6, '$-2$')
T(ax, -1.06, -0.6, '$-1$', ha='right')
T(ax, 1.0, -0.6, '$1$')
T(ax, -0.1, -2.0, '$-2$', ha='right', bg=True)
T(ax, -0.1, -4.4, '$-4$', ha='right')
save(fig, 'img054')
