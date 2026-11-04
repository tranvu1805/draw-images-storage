from graphs_kit import *
setfs(16)

# y = 9 - x^2; rectangle ABCD with A(-2;0), B(2;0), C(2;5), D(-2;5) shaded
fig, ax = win('img074', (92, 223), (19.7, 18.9))
from matplotlib.patches import Rectangle
ax.add_patch(Rectangle((-2, 0), 4, 5, fc='#e4e4e4', ec='none', zorder=1))
axes(ax, (-4.06, 5.48), (-1.11, 11.27), xname=None, yname=None, origin=None, lw=1.1)
curve(ax, lambda x: 9 - x**2, -3.12, 3.12)
seg(ax, [(-2, 0), (-2, 5), (2, 5), (2, 0)], lw=1.4)
T(ax, 0.75, 11.0, '$y$', fs=17)
T(ax, 5.2, -0.8, '$x$', fs=17)
T(ax, -0.4, 9.7, '$9$')
T(ax, -2.6, 5.0, '$D$')
T(ax, 2.6, 5.0, '$C$')
T(ax, -3.2, 0.6, '$-3$', ha='right')
T(ax, 3.2, 0.6, '$3$', ha='left')
T(ax, -2.0, -0.8, '$A$')
T(ax, -0.7, -0.8, '$O$')
T(ax, 1.9, -0.8, '$B$')
save(fig, 'img074')
