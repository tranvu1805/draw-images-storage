from graphs_kit import *

# y = 2 + k/(x - x0): asymptotes and intercepts placed as in the original (no numbers shown)
fig, ax = win('img031', (139, 187), 29)
axes(ax, (-4.79, 9.69), (-5.24, 6.38), lw=0.8, opos=(-3, -4), yname_pos=(-5, 0))
x0, k = 88 / 29, 4.29
vline(ax, x0, lw=1.4)
hline(ax, 2, lw=1.4)
f = lambda x: 2 + k / (x - x0)
curve(ax, f, -4.8, x0 - 1e-3)
curve(ax, f, x0 + 1e-3, 9.9)
save(fig, 'img031')
