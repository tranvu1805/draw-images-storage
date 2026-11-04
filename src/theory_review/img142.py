# Mutation caused by UV light: a DNA strand before / after, base T replaced by A.
from photo_kit import *

fig, ax = board('img142', 100)            # y 0..120.5
BASE = {'G': '#f2b16b', 'T': '#f2b16b', 'C': '#f2b16b', 'A': '#f06ba8'}


def strand(y0, bases, hl=None):
    # sugar-phosphate backbone (slanted ribbon) with four bases hanging below
    x0, x1, dy = 6, 96, 9
    ax.add_patch(Polygon([(x0, y0), (x1, y0 + dy), (x1, y0 + dy + 9), (x0, y0 + 9)], closed=True, fc='#c9d9ee',
                         ec='#5a7fa8', lw=0.9, zorder=1))
    for i, b in enumerate(bases):
        x = 16 + i * 22
        y = y0 + (x - x0) / (x1 - x0) * dy
        ax.add_patch(Circle((x - 6, y + 6.5), 1.8, fc='#f5e14a', ec='#555555', lw=0.5, zorder=3))   # phosphate
        ax.add_patch(Polygon(rot([[np.cos(a) * 3.6, np.sin(a) * 3.6] for a in np.radians(np.arange(90, 450, 72))],
                                 0, x + 2, y + 4.5), fc='#7d8fb8', ec='#333333', lw=0.6, zorder=3))  # sugar
        ax.plot([x + 2, x + 2], [y + 1, y - 6], color='#333333', lw=1.0, zorder=2)
        fc = BASE[b] if b != hl else BASE['A']
        ax.add_patch(Polygon([(x + 2 + 4.6 * np.cos(a), y - 10 + 4.6 * np.sin(a)) for a in
                              np.radians(np.arange(90, 450, 60))], fc=fc, ec='#333333', lw=0.7, zorder=3))
        txt(ax, x + 2, y - 10, b, size=10, weight='bold', zorder=4)


strand(84, 'GTGC')
strand(22, 'GAGC', hl='A')
txt(ax, 72, 116, 'DNA', size=11, weight='bold')
txt(ax, 4, 116, 'Tia UV', size=11, weight='bold', ha='left')
for i in range(3):   # UV rays, wavy, ending just above the strand
    xs = np.linspace(9 + i * 9, 21 + i * 9, 50)
    ys = 111 - (xs - xs[0]) * 0.85 + 1.1 * np.sin((xs - xs[0]) * 1.9)
    ax.plot(xs, ys, color='#8a3fc2', lw=1.1, zorder=5)
    arr(ax, xs[-1], ys[-1], xs[-1] + 2.2, ys[-1] - 2.2, color='#8a3fc2', lw=1.0, head=5)
ax.plot([76, 82], [113, 102.5], color=INK, lw=0.8)
arr(ax, 40, 70, 40, 45, lw=1.3, head=7)
ax.add_patch(Rectangle((1, 1), 98, 118, fc='none', ec='#555555', lw=0.8))
save(fig, 'img142')
