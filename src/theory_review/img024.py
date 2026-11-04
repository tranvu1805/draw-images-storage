from graphs_kit import *
setfs(13)

fig, ax = win('img024', (167, 189), (53.5, 54))
axes(ax, (-3.03, 3.0), (-2.65, 2.98), opos=(-5, -4))
f = lambda x: x**4 - 2 * x**2 - 1
for x in (-1, 1):
    dash(ax, [(x, 0), (x, -2)])
dash(ax, [(-1, -2), (1, -2)])
curve(ax, f, -1.8, 1.8)
xt(ax, [-2, -1, 1, 2], d=(0, -1), style='dot', size=3.2, bg=True)
xt(ax, [0], [''], style='dot', size=3.2)
yt(ax, [2, 1], style='dot', size=3.2)
yt(ax, [-1], pos='lt', style='dot', size=3.2)
yt(ax, [-2], pos=(0, 0), style='dot', size=3.2, bg=True)
save(fig, 'img024')
