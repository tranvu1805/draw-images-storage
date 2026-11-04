from graphs_kit import *
setfs(14)

# y = 2 - 3/(x + 1): TCĐ x=-1 (left of Oy), TCN y=2 (above Ox), cuts Ox at x>0 and Oy at y<0
fig, ax = win('img044', (169, 229), 28)
axes(ax, (-5.54, 6.18), (-2.68, 7.29), origin=None, lw=0.8, yname_pos=(3, 1), xname_pos=(-1, -4))
ax.texts[-1].set_ha('left')
dash(ax, [(-1, -2.43), (-1, 7.29)], lw=1.2)
dash(ax, [(-5.54, 2), (6.0, 2)], lw=1.2)
f = lambda x: 2 - 3 / (x + 1)
box = (-5.54, 6.1, -2.7, 7.29)
curve(ax, f, -5.54, -1.001, box=box)
curve(ax, f, -0.999, 6.1, box=box)
save(fig, 'img044')
