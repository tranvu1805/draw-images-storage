# Dented table-tennis ball (a) put into a cup of hot water (b) becomes round again.
from photo_kit import *

fig, ax = board('img097', 100)            # y 0..34.2
for x0 in (2, 54):
    box(ax, x0, 1, 44, 32, fc='#f3f3f3', ec='#bdbdbd', lw=0.8, z=0)


def ball(cx, cy, r, dent=False, z=5):
    th = np.linspace(0, 2 * np.pi, 361)
    rr = np.full_like(th, r)
    if dent:   # push the outline in between 15 and 85 degrees
        a0, a1 = np.radians(12), np.radians(88)
        m = (th > a0) & (th < a1)
        rr[m] -= r * 0.24 * np.sin((th[m] - a0) / (a1 - a0) * np.pi) ** 1.4
    pts = np.column_stack([cx + rr * np.cos(th), cy + rr * np.sin(th)])
    ax.add_patch(Polygon(pts, fc='white', ec='none', zorder=z))
    ax.add_patch(Circle((cx + r * 0.22, cy - r * 0.25), r * 0.7, fc='#ededed', ec='none', zorder=z))
    ax.add_patch(Circle((cx - r * 0.12, cy + r * 0.05), r * 0.6, fc='white', ec='none', zorder=z))
    if dent:
        ax.add_patch(Ellipse((cx + r * 0.42, cy + r * 0.42), r * 0.8, r * 0.48, angle=-45, fc='#c8c8c8', ec='none',
                             zorder=z + 1))
        ax.add_patch(Ellipse((cx + r * 0.5, cy + r * 0.5), r * 0.55, r * 0.26, angle=-45, fc='#aaaaaa', ec='none',
                             zorder=z + 1))
    ax.add_patch(Polygon(pts, fc='none', ec='#666666', lw=1.1, zorder=z + 2))


ball(24, 18, 7.5, dent=True)
txt(ax, 24, 5, 'Hình a', size=13, weight='bold')
# cup of hot water
cx = 74
ax.add_patch(Polygon([(cx - 10.6, 21.5), (cx + 10.6, 21.5), (cx + 9, 6), (cx - 9, 6)], fc='#cfe5f7', ec='none',
                     zorder=1))
ax.plot([cx - 10.6, cx + 10.6], [21.5, 21.5], color='#7fb2dc', lw=1.0, zorder=2)
ball(cx, 24.4, 5.2, z=3)
ax.plot([cx - 11, cx - 9, cx + 9, cx + 11], [26, 6, 6, 26], color='#555555', lw=1.3, zorder=6)
ax.add_patch(Arc((cx + 11.2, 16), 7, 10, theta1=-90, theta2=90, color='#555555', lw=2.2, zorder=6))
for k, x in enumerate((cx - 9, cx + 8.5)):
    ys = np.linspace(27.5, 32, 30)
    ax.plot(x + 0.8 * np.sin((ys - 27.5) * 2.2 + k), ys, color='#9a9a9a', lw=1.0, zorder=6)
txt(ax, cx, 11, 'nước nóng', size=11.5, color='#2f5f8a', zorder=7)
txt(ax, cx + 17.5, 5, 'Hình b', size=13, weight='bold')
arr(ax, 40, 6, 58, 13, lw=2.6, head=11, rad=0.35, z=8)
save(fig, 'img097')
