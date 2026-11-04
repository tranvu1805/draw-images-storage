from graphs_kit import *

# histogram: number of fields by yield (t/ha), classes [5,5;5,7) … [6,5;6,7) with counts 3, 4, 6, 5, 5, 2
fid = 'img251'
fig, ax = win(fid, (145 - 5.5 * 166.7, 235), (166.7, 33.2))
X = lambda px: (px - 145) / 166.7 + 5.5  # original pixel column -> data x
x0, x1 = X(112), X(410)
for g in range(1, 7):
    ax.plot([x0, x1], [g, g], color='#c9c6d8', lw=1.3, zorder=0)
axes(ax, (x0, x1), (0, 6.93), xy=(x0, 0), xname=None, yname=None, origin=None, lw=1.3, head=8)
from matplotlib.patches import Rectangle
vals = [3, 4, 6, 5, 5, 2]
for i, v in enumerate(vals):
    ax.add_patch(Rectangle((5.5 + 0.2 * i, 0), 0.2, v, fc='#5bc4f0', ec='#2a5a74', lw=1.1, zorder=2))
yt(ax, list(range(0, 7)), [''] * 7, x0=x0, size=2.5)
for v in range(0, 7):
    ax.text(X(103), v, str(v), ha='right', va='center', fontsize=14)
for i in range(7):
    ax.text(5.5 + 0.2 * i, -0.3, f'{5.5 + 0.2 * i:.1f}'.replace('.', ','), ha='center', va='top', fontsize=13.5)
ax.text(X(3), 6.8, 'Số thửa ruộng', ha='left', va='center', fontsize=12.5)
ax.text(X(408), -0.9, 'Năng suất\n(tấn/ha)', ha='center', va='center', fontsize=14, linespacing=1.15)
save(fig, fid)
