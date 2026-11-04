# Three delivery drones A, B, C; the segments between them are the distances d1 = AB, d2 = BC, d3 = AC.
from photo_kit import *

fig, ax = board('img247', 100)            # y 0..63.6
LINE = '#d32f2f'


def drone(x, y, s, name, loff):
    ink = '#333333'
    for dx, dy in ((-0.62, 0.26), (0.62, 0.26), (-0.5, -0.2), (0.5, -0.2)):
        ax.plot([x, x + dx * s], [y + 0.05 * s, y + dy * s + 0.05 * s], color=ink, lw=2.0, zorder=3)
        ax.plot([x + dx * s] * 2, [y + dy * s + 0.05 * s, y + dy * s + 0.13 * s], color=ink, lw=1.4, zorder=3)
        ax.add_patch(Ellipse((x + dx * s, y + dy * s + 0.15 * s), 0.5 * s, 0.1 * s, fc='#cfd8dc', ec=ink, lw=0.7,
                             zorder=4, alpha=0.95))
    ax.add_patch(FancyBboxPatch((x - 0.22 * s, y - 0.2 * s), 0.44 * s, 0.32 * s,
                                boxstyle=f'round,pad=0,rounding_size={0.05 * s}', fc='#f39c32', ec=ink, lw=0.9,
                                zorder=5))
    ax.add_patch(Ellipse((x, y + 0.14 * s), 0.34 * s, 0.1 * s, fc='#9e9e9e', ec=ink, lw=0.8, zorder=6))
    for dx in (-0.16, 0.16):   # skids
        ax.plot([x + dx * s, x + dx * s * 1.4], [y - 0.2 * s, y - 0.32 * s], color=ink, lw=1.0, zorder=2)
        ax.plot([x + dx * s * 1.4 - 0.1 * s, x + dx * s * 1.4 + 0.1 * s], [y - 0.32 * s] * 2, color=ink, lw=1.4,
                zorder=2)
    txt(ax, x + loff[0], y + loff[1], f'${name}$', size=15, weight='bold', zorder=8)


A, B, C = (18, 15), (42, 47), (79, 27)
for (p, q), lab, off in (((A, B), '$d_1$', (-4.5, 1.5)), ((B, C), '$d_2$', (1.5, 4.0)), ((A, C), '$d_3$', (1, -4))):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=LINE, lw=1.4, zorder=1)
    txt(ax, (p[0] + q[0]) / 2 + off[0], (p[1] + q[1]) / 2 + off[1], lab, size=14, color=LINE)
drone(*A, 21, 'A', (-12, -5))
drone(*B, 21, 'B', (-13, 2))
drone(*C, 21, 'C', (12, -5))
save(fig, 'img247')
