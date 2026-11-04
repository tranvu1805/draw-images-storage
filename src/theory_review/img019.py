# Galvanic cell Zn | Zn2+ || H+ | H2 | Pt (standard hydrogen electrode), voltmeter reads 0,76 V.
from photo_kit import *

fig, ax = board('img019', 100)            # y 0..58.4
SOL, GLASS = '#dfe9f3', '#555555'


def beaker(x0, x1, y0=6, y1=31, level=25):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, level - y0, fc=SOL, ec='none', zorder=1))
    ax.plot([x0 - 1.2, x0, x0, x1, x1, x1 + 1.2], [y1, y1 - 1, y0, y0, y1 - 1, y1], color=GLASS, lw=1.5,
            solid_joinstyle='round', zorder=3)
    ax.plot([x0, x1], [level, level], color='#9db4cc', lw=0.8, zorder=2)


beaker(12, 42)
beaker(55, 85)
# salt bridge (inverted U tube)
for d, c, w in ((0, GLASS, 9.5), (0, '#f3f3f3', 7.0)):
    ax.plot([37.5, 37.5, 59.5, 59.5], [14, 35, 35, 14], color=c, lw=w, solid_joinstyle='round', zorder=4,
            solid_capstyle='butt')
ax.plot([36.6, 38.4], [14, 14], color=GLASS, lw=1.0, zorder=5)
ax.plot([58.6, 60.4], [14, 14], color=GLASS, lw=1.0, zorder=5)
# Zn rod
ax.add_patch(FancyBboxPatch((21.5, 9), 3, 39, boxstyle='round,pad=0,rounding_size=1.2', fc='#8d8d8d', ec='#333333',
                            lw=1.0, zorder=6))
ax.add_patch(Rectangle((22.3, 10), 0.8, 37, fc='#bdbdbd', ec='none', zorder=7))
# hydrogen electrode: glass tube with side inlet, Pt plate at the bottom
tx = 71
W2 = 3.0
ax.plot([tx - W2, tx - W2, tx - 4.4, tx - 4.4], [48, 19, 16, 9], color=GLASS, lw=1.3, zorder=6)
ax.plot([tx + W2, tx + W2, tx + 4.4, tx + 4.4], [40.5, 19, 16, 9], color=GLASS, lw=1.3, zorder=6)
ax.plot([tx + W2, tx + W2], [44, 48], color=GLASS, lw=1.3, zorder=6)
ax.plot([tx + W2, tx + 9.5], [40.5, 40.5], color=GLASS, lw=1.3, zorder=6)
ax.plot([tx + W2, tx + 9.5], [44, 44], color=GLASS, lw=1.3, zorder=6)
ax.add_patch(Rectangle((tx - W2 - 0.4, 46.6), 2 * W2 + 0.8, 2.2, fc='#777777', ec='#333333', lw=0.8, zorder=7))
ax.plot([tx, tx], [48, 14], color='#333333', lw=1.0, zorder=6)                # Pt wire
ax.add_patch(Polygon([(tx - 2.2, 12.5), (tx, 15.5), (tx + 2.2, 12.5), (tx, 9.5)], fc='#222222', ec='#222222',
                     zorder=7))
for bx_, by_ in [(tx + 1.2, 18), (tx - 1.2, 21), (tx + 1.0, 24), (tx + 6.2, 13), (tx + 7.2, 17)]:
    ax.add_patch(Circle((bx_, by_), 0.65, fc='white', ec='#555555', lw=0.7, zorder=7))
arr(ax, tx + 17, 42.2, tx + 10.2, 42.2, lw=1.1, head=6)
txt(ax, tx + 17.5, 42.2, '$\\mathrm{H_2}(g)$\n(1 bar)', size=12.5, ha='left', va='center', linespacing=1.15)
# wires + voltmeter
ax.plot([23, 23, 40], [48, 54, 54], color=INK, lw=1.2, zorder=5)
ax.plot([tx, tx, 58], [48.8, 54, 54], color=INK, lw=1.2, zorder=5)
box(ax, 40, 51.5, 18, 5, '0,76 V', size=12.5, lw=1.2, z=6)
txt(ax, 37.3, 56.6, '–', size=15, weight='bold')
txt(ax, 60.6, 56.8, '+', size=15, weight='bold')
txt(ax, 49, 48.5, 'Volt kế', size=12.5)
# labels
txt(ax, 0, 39, 'Thanh Zn', size=12.5, ha='left')
ax.plot([13.8, 21.4], [39, 39], color=INK, lw=0.8)
txt(ax, 48.5, 39, 'Cầu muối', size=12.5)
txt(ax, 48.5, 18, '298 K', size=12.5)
txt(ax, 89, 12.5, 'Mảnh Pt', size=12.5, ha='left')
ax.plot([tx + 1.5, 88.5], [12.5, 12.5], color=INK, lw=0.8, zorder=8)
txt(ax, 27, 2.2, '$\\mathrm{Zn^{2+}}(aq)$ 1,00 M', size=12.5)
txt(ax, 70, 2.2, '$\\mathrm{H^{+}}(aq)$ 1,00 M', size=12.5)
save(fig, 'img019')
