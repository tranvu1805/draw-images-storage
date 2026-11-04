from graphs_kit import *
setfs(17)

# square OABC of side 4 cut by y = x^2/4; S2 (shaded) under the curve on [0;4]
fig, ax = win('img065', (71, 250), 40.75)
f = lambda x: x**2 / 4
fill_between(ax, f, 0, 4, color='#fbd3b4')
axes(ax, (-1.0, 5.5), (-0.96, 6.0), xname=None, yname=None, origin=None, lw=1.1)
seg(ax, [(0, 4), (4, 4), (4, 0)], lw=1.4)
curve(ax, f, -1.06, 4.93)
T(ax, 0.4, 5.85, '$y$', fs=18)
T(ax, 5.3, 0.4, '$x$', fs=18)
T(ax, 0.4, 4.45, '$A$')
T(ax, -0.4, 4.0, '$4$')
T(ax, 4.45, 4.0, '$B$')
T(ax, 4.45, 0.4, '$C$')
T(ax, -0.45, -0.5, '$O$')
T(ax, 4.0, -0.5, '$4$')
T(ax, 3.4, 5.0, r'$y=\dfrac{x^2}{4}$', ha='center')
T(ax, 1.5, 2.85, '$S_1$')
T(ax, 3.15, 1.3, '$S_2$')
save(fig, 'img065')
