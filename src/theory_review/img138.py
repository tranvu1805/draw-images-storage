# Genetic drift: wind carries a few ladybirds to an island, then a fire leaves a few random survivors.
from photo_kit import *

fig, ax = board('img138', 100)            # y 0..32.5
LRED, LYEL, LGRN = '#d32f2f', '#f4d03f', '#2e7d32'
rng = np.random.default_rng(7)
S = 3.6


def cluster(cx, cy, cols, r=8.0):
    # place ladybirds on a jittered hex-like pattern inside a circle
    pts = [(0, 0)] + [(r * 0.5 * np.cos(a), r * 0.5 * np.sin(a)) for a in np.radians(np.arange(0, 360, 60) + 30)] + \
          [(r * np.cos(a), r * np.sin(a)) for a in np.radians(np.arange(0, 360, 36))]
    for (dx, dy), c in zip(pts, cols):
        ladybug(ax, cx + dx + rng.uniform(-0.6, 0.6), cy + dy + rng.uniform(-0.6, 0.6), S, c,
                angle=rng.uniform(0, 360), lw=0.5)


R, Y, G = LRED, LYEL, LGRN
cluster(11, 17, [Y, R, G, Y, R, Y, G, R, Y, R, G, R, Y, R, Y, R, R])                 # mainland: mixed
cluster(50, 17, [R, R, Y, R, G, R, R, Y, R, R, G, R, R, R, R, R, R])                 # new island population
cluster(89, 17, [R] * 17)                                                             # after the fire
# wind gusts (lines ending in curls) + the few dispersers
for x0, x1, y, r in ((20, 27, 30, 1.6), (21.5, 28.5, 27, 1.3), (20.5, 26.5, 24.4, 1.1)):
    t = np.linspace(-np.pi / 2, 1.3 * np.pi, 60)
    rr = r * (1 - (t + np.pi / 2) / (2.4 * np.pi) * 0.75)
    xs = np.concatenate([[x0], x1 + rr * np.cos(t)])
    ys = np.concatenate([[y - r], y + rr * np.sin(t)])
    ax.plot(xs, ys, color=INK, lw=1.0, solid_capstyle='round')
for (x, y), c in zip([(32, 30.8), (36, 29.8), (34, 27), (38.5, 27.2), (36.5, 24.3), (31.5, 25.2)], [Y, R, R, G, R, R]):
    ladybug(ax, x, y, S * 0.9, c, angle=rng.uniform(0, 360), lw=0.5)
# fire + survivors
th = np.linspace(0, 2 * np.pi, 80)
for k, (x0, h, w) in enumerate([(64, 6, 1.6), (66.5, 8.5, 2.0), (69.2, 7, 1.8), (71.8, 9, 2.1), (74.4, 6.5, 1.7),
                                 (76.6, 7.8, 1.8)]):
    xs = x0 + w * np.sin(th) * np.sin(th / 2) + 0.12 * h * (1 + np.cos(th)) / 2 * 3
    ys = 1.5 + h * (1 + np.cos(th)) / 2
    ax.add_patch(Polygon(np.column_stack([xs, ys]), fc='#ff7a00', ec='#e53935', lw=0.6, zorder=3))
    ax.add_patch(Polygon(np.column_stack([x0 + 0.55 * w * np.sin(th) * np.sin(th / 2) + 0.18 * h * (1 + np.cos(th)) / 2,
                                          1.5 + 0.5 * h * (1 + np.cos(th)) / 2]), fc='#ffd54f', ec='none', zorder=4))
for x, y in [(68, 26), (72, 27.6), (70, 23.5), (74.5, 24.5)]:
    ladybug(ax, x, y, S * 0.9, R, angle=rng.uniform(0, 360), lw=0.5)
ax.plot([73.2, 79], [28.4, 30.5], color=INK, lw=0.8)
ax.plot([75.6, 79], [25.6, 30.5], color=INK, lw=0.8)
txt(ax, 79.5, 30.8, 'Những cá thể\nsống sót', size=12, ha='left', va='center', linespacing=1.1)
# arrows + captions
for x0, x1 in ((22, 38.5), (61.5, 77.5)):
    ax.add_patch(FancyArrowPatch((x0, 13), (x1, 13), arrowstyle='simple,head_length=1.2,head_width=1.4,tail_width=0.55',
                                 mutation_scale=10, fc='#8a8a8a', ec='#6a6a6a', lw=0.6, zorder=2))
txt(ax, 30, 18.5, 'Gió thổi làm bọ rùa\nphát tán đến đảo', size=12.5, linespacing=1.15)
txt(ax, 69.5, 18.5, 'Hỏa hoạn tiêu diệt\ngần hết các cá thể', size=12.5, linespacing=1.15)
txt(ax, 11, 4.5, 'Quần thể ở đất liền', size=12.5)
txt(ax, 50, 4.5, 'Quần thể mới trên đảo', size=12.5)
txt(ax, 89, 3.6, 'Quần thể ở trên đảo\nsau hỏa hoạn', size=12.5, linespacing=1.1)
save(fig, 'img138')
