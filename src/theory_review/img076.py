from graphs_kit import *

# histogram of monthly salaries: relative frequencies (%) per class [6;8) … [14;16)
fid = 'img076'
fig, ax = win(fid, (113 - 6 * 21.4, 294), (21.4, 4.1))
px = lambda x: (x + 15.4) / 21.4  # original pixel column -> data x
x0, x1 = px(67), px(408)
for g in (10, 20, 30, 40, 50):
    ax.plot([x0, x1], [g, g], color='#555555', lw=1.0, zorder=0)
axes(ax, (x0, x1), (0, 69.8), xy=(x0, 0), xname=None, yname=None, origin=None, lw=1.0)
from matplotlib.patches import Rectangle
vals = [8, 24, 40, 16, 12]
for i, v in enumerate(vals):
    a = 6 + 2 * i
    ax.add_patch(Rectangle((a, 0), 2, v, fc='#dedede', ec=INK, lw=1.0, zorder=2))
    ax.text(a + 1, v + 0.6, f'{v}%', ha='center', va='bottom', fontsize=11.5)
for t in range(0, 51, 10):
    ax.text(px(62), t, str(t), ha='right', va='center', fontsize=11.5)
for t in range(6, 17, 2):
    ax.text(t, -1.6, str(t), ha='center', va='top', fontsize=11.5)
ax.text(px(408), -1.6, 'Lương (triệu đồng)', ha='center', va='top', fontsize=11.5)
ax.text(px(31), 62, 'Tần số\ntương đối\n(%)', ha='center', va='center', fontsize=10.5, linespacing=1.1)
save(fig, fid)
