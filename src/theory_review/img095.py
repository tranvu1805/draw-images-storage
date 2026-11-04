from graphs_kit import *
setfs(14)

# y = (x - 1)^2 (x + 2) = x^3 - 3x + 2: CĐ (-1;4), CT (1;0), y-intercept 2, root -2
fig, ax = win('img095', (79, 170), 34)
axes(ax, (-2.32, 2.88), (-1.21, 4.91), xname=None, yname=None, origin=None, lw=1.0)
dash(ax, [(-1, 4), (0, 4)])
curve(ax, lambda x: (x - 1)**2 * (x + 2), -2.15, 2.1)
T(ax, 0.25, 4.7, '$y$', fs=15)
T(ax, 2.75, 0.45, '$x$', fs=15)
T(ax, 0.3, 4.0, '$4$')
T(ax, 0.32, 2.05, '$2$')
T(ax, -0.4, 0.45, '$O$')
T(ax, -1.5, -0.42, '$-2$')
T(ax, 1.2, -0.42, '$1$')
save(fig, 'img095')
