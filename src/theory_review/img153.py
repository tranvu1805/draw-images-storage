# Metaphase chromosome, parts numbered 1-4 (1 telomere, 2 short arm, 3 long arm, 4 centromere).
from photo_kit import *

fig, ax = board('img153', 100)            # y 0..161.8; 1 unit = 1.96 pt
cx, cy = 36, 106                          # centromere
DARK, BODY, BAND = '#3d4a35', '#8fa37d', '#5d7149'
K = 1.3                                   # horizontal spread


def chromatid(side):
    up = [(cx + side * 5 * K, cy + 1), (cx + side * 8 * K, cy + 12), (cx + side * 10.5 * K, cy + 28),
          (cx + side * 11 * K, cy + 40)]
    lo = [(cx + side * 5 * K, cy - 1), (cx + side * 8 * K, cy - 14), (cx + side * 9.5 * K, cy - 45),
          (cx + side * 9.5 * K, cy - 88)]
    for arm in (up, lo):
        curve(ax, arm, color=DARK, lw=36, z=2)
    for arm in (up, lo):
        curve(ax, arm, color=BODY, lw=32.5, z=3)
    return up, lo


ends = {}
for side in (-1, 1):
    ends[side] = chromatid(side)
    for y0, w in ((cy - 28, 2.2), (cy - 44, 3.0), (cy - 60, 2.2), (cy - 76, 2.6), (cy + 20, 2.4), (cy + 31, 1.8)):
        off = 8.6 if y0 < cy - 20 else 7.6 if y0 < cy else 10.6 if y0 > cy + 25 else 9.8
        x = cx + side * off * K
        ax.add_patch(Rectangle((x - 6.8, y0 - w / 2), 13.6, w, fc=BAND, ec='none', zorder=4))
ax.add_patch(Ellipse((cx, cy), 8, 8, fc=DARK, ec='none', zorder=5))   # centromere
for side in (-1, 1):
    up, lo = ends[side]
    for (x, y), d in ((up[-1], 1), (lo[-1], -1)):
        ax.add_patch(Ellipse((x, y + d * 2.6), 12.5, 5, fc='#4a5a3a', ec='none', zorder=4))

lab = dict(size=16, ha='left', va='center')
tip = (88, 157)
for side in (-1, 1):
    x, y = ends[side][0][-1]
    ax.plot([x + 2, tip[0] - 1], [y + 5, tip[1] - 1], color=INK, lw=1.2, zorder=6)
txt(ax, tip[0], tip[1], '1', **lab)
for y, s, x0 in ((cy + 25, '2', cx + 22), (cy, '4', cx + 3), (cy - 62, '3', cx + 20)):
    ax.plot([x0, 89], [y, y], color=INK, lw=1.2, zorder=6)
    txt(ax, 91, y, s, **lab)
save(fig, 'img153')
