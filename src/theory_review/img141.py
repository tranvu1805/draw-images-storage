# Genetic drift: a random event (a foot stepping on beetles) changes allele frequencies.
from photo_kit import *

fig, ax = board('img141', 100)            # y 0..46.6
R = 14.5
for cx in (16, 50, 84):
    ax.add_patch(Circle((cx, 15), R, fc=GREY, ec='none', zorder=0))
rng = np.random.default_rng(3)


def pop(cx, cols):
    spots = [(-8, 6), (0, 9), (8, 5), (-10, -3), (-2, 1), (6, -3), (-6, -9), (3, -10), (10, -10), (12, 2)]
    for (dx, dy), c in zip(spots, cols):
        beetle(ax, cx + dx, 15 + dy, 7.4, c, angle=rng.uniform(0, 360), lw=0.6)


G, B = GREEN, BROWN
pop(16, [G, B, G, B, B, G, B, B, B, B])                 # before
pop(50, [G, B, G, B, B, B, B, B, B, B][:10])            # being stepped on
pop(84, [B, B, G, B, B, B, B, B, B][:9])                # after: frequencies changed
# leg + shoe stepping on the middle population
ax.add_patch(Polygon([(41, 47), (51, 47), (52, 33), (43, 33)], fc='#8c8c8c', ec='#444444', lw=0.8, zorder=9))
star = [(51 + (10 if k % 2 == 0 else 5) * np.cos(t), 19.5 + (4.2 if k % 2 == 0 else 2) * np.sin(t))
        for k, t in enumerate(np.linspace(0, 2 * np.pi, 25)[:-1])]
ax.add_patch(Polygon(star, fc='#ffd21f', ec='#e09b00', lw=0.8, zorder=9))
t = np.linspace(-np.pi / 2, np.pi / 2, 12)
toe = [(60 + 3.2 * np.cos(a), 24 + 3.2 * np.sin(a)) for a in t]
shoe = [(42, 21), (49, 21), (51, 22.5)] + toe + [(56, 28), (53, 31), (52, 34), (43, 34), (42, 30)]
ax.add_patch(Polygon(shoe, fc='#111111', ec='#111111', lw=0.8, zorder=10, joinstyle='round'))
ax.add_patch(Polygon([(42, 21), (47, 21), (47, 24), (42, 24)], fc='#333333', ec='none', zorder=11))   # heel
ax.plot([50, 62], [23.3, 23.3], color='#666666', lw=0.7, zorder=11)
ax.plot([53, 57.5], [30, 26.5], color='#777777', lw=0.7, zorder=11)                 # lacing
for x0 in (31.5, 65.5):
    arr(ax, x0, 15, x0 + 3, 15, lw=1.4, head=7, z=12)
save(fig, 'img141')
