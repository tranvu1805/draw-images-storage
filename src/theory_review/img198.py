from graphs_kit import *
setfs(18)

# y = x^3 - 6x (red) and y = x^2 (blue); region between them for -2 <= x <= 3 shaded
fig, ax = win('img198', (159, 239), (41.5, 20.5))
f = lambda x: x**3 - 6 * x
g = lambda x: x**2
fill_between(ax, f, -2, 3, g=g, color='#fbd3b4')
axes(ax, (-3.59, 4.89), (-6.59, 11.07), xname=None, yname=None, origin=None, lw=1.4, head=8)
dash(ax, [(-2, 0), (-2, 4), (0, 4)], lw=1.4, ls=(0, (4, 3)))
dash(ax, [(3, 0), (3, 9), (0, 9)], lw=1.4, ls=(0, (4, 3)))
curve(ax, g, -3.37, 3.33, color='#1f3fd0', lw=1.8)
curve(ax, f, -2.9, 3.13, color='#c0141c', lw=1.8)
T(ax, 0.48, 10.75, '$y$', fs=19)
T(ax, 4.65, 1.3, '$x$', fs=19)
T(ax, -0.5, 9.0, '$9$', ha='right')
T(ax, 0.25, 4.0, '$4$', ha='left')
T(ax, -1.8, -1.25, '$-2$')
T(ax, -0.5, -1.2, '$O$')
T(ax, 3.0, -1.2, '$3$')
save(fig, 'img198')
