from graphs_kit import *

# y = x^3 - 4x + 1 (answer A); window and extrema as in the original
fig, ax = win('img030', (161, 236), 46.5)
axes(ax, (-3.08, 3.72), (-2.8, 4.75), origin=None, yname_pos=(-5, 0))
curve(ax, lambda x: x**3 - 4 * x + 1, -2.37, 2.37)
save(fig, 'img030')
