from graphs_kit import *
setfs(14)

# shape of y = x^3 - 2024x (odd cubic, a > 0, two extrema symmetric about O); drawn as y = x^3 - 3x
fig, ax = win('img077', (100, 99), (41, 42))
axes(ax, (-2.44, 2.44), (-2.19, 2.24), xname=None, yname=None, origin=None)
curve(ax, lambda x: x**3 - 3 * x, -2.03, 2.03)
T(ax, 0.18, 2.12, '$y$', ha='left', fs=15)
T(ax, 2.35, -0.3, '$x$', fs=15)
T(ax, -0.25, -0.3, '$O$')
save(fig, 'img077')
