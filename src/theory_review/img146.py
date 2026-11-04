# Types of habitat: (a) on land / in air, (b) in soil, (c) in water, (d) on/in another organism.
# img147 uses the same drawing (it imports draw() from this file).
from photo_kit import *


def draw(fid):
    fig, ax = board(fid, 100)            # y 0..82.2
    H = 82.2
    GROUND = 38
    # sky, sun, birds
    ax.add_patch(Rectangle((0, GROUND), 100, H - GROUND, fc='#d9eefb', ec='none', zorder=0))
    ax.add_patch(Circle((9, 73), 4.2, fc='#ffd54f', ec='#f2b705', lw=1.0, zorder=1))
    for a in range(0, 360, 30):
        r = np.radians(a)
        ax.plot([9 + 5.4 * np.cos(r), 9 + 7.2 * np.cos(r)], [73 + 5.4 * np.sin(r), 73 + 7.2 * np.sin(r)],
                color='#f2b705', lw=1.2, zorder=1)
    vbird(ax, 40, 72, 6)
    vbird(ax, 49, 76, 4.5)
    # soil (everything below the surface) with roots, worms, a burrow
    ax.add_patch(Rectangle((0, 0), 100, GROUND, fc='#8d5a3b', ec='none', zorder=0))
    for k in range(60):
        rng = np.random.default_rng(k)
        ax.add_patch(Ellipse((rng.uniform(52, 99), rng.uniform(1, GROUND - 4)), rng.uniform(1.5, 4),
                             rng.uniform(0.8, 2), fc='#7a4b30', ec='none', zorder=1))
    worm(ax, [(60, 22), (63, 24.5), (67, 22.5), (70, 24)])
    worm(ax, [(76, 9), (79, 12), (83, 10), (86, 12.5), (88, 11)])
    worm(ax, [(90, 27), (92.5, 24.5), (95, 26), (97, 23.5)])
    # grass surface
    ax.add_patch(Rectangle((0, GROUND - 1.2), 100, 3.0, fc='#7cb342', ec='none', zorder=2))
    for gx in np.arange(1, 100, 1.6):
        ax.plot([gx, gx + 0.5], [GROUND + 1.6, GROUND + 3.2], color='#558b2f', lw=0.8, zorder=2)
    # pond (cross-section) on the left
    t = np.linspace(0, np.pi, 80)
    basin = np.column_stack([28 - 25 * np.cos(t), GROUND + 0.5 - 27 * np.sin(t) ** 0.8])
    ax.add_patch(Polygon(np.vstack([basin, [(53, GROUND + 0.5), (3, GROUND + 0.5)]]), fc='#cfe0ea', ec='none',
                         zorder=3))
    water = np.column_stack([28 - 24 * np.cos(t), GROUND - 0.5 - 26 * np.sin(t) ** 0.8])
    ax.add_patch(Polygon(water, fc='#9fd0ef', ec='#5c9ccc', lw=0.9, zorder=4))
    ax.add_patch(Polygon(np.column_stack([28 - 24 * np.cos(t), GROUND - 0.5 - 26 * np.sin(t) ** 0.8]) * [1, 1],
                         fc='none', ec='#c2a272', lw=2.4, zorder=4))
    for x in (7, 10, 46, 49):
        reed(ax, x, GROUND - 6, 16, lean=(1 if x > 30 else -1) * 1.2, z=5)
    lilypad(ax, 16, GROUND - 0.5, 6, flower=True)
    lilypad(ax, 37, GROUND - 0.5, 7)
    frog(ax, 37, GROUND + 0.9, 3.4)
    fish(ax, 26, 26, 9, '#f4a63a', facing=1, stripes=True)
    fish(ax, 38, 19, 6, '#9aa86a', facing=-1)
    tadpole(ax, 17, 22, 3)
    tadpole(ax, 20, 19.5, 3)
    snail(ax, 28, 14.2, 3)
    # land: trees, deer, mushroom
    tree(ax, 66, GROUND + 1, 17, 8.5)
    tree(ax, 88, GROUND + 1, 13, 6.5, crown='#4f9a45')
    deer(ax, 79, GROUND + 1, 16, facing=-1)
    # (d): a zoom bubble on the deer's back showing ticks living on it
    bubble(ax, 89, 67, 7.5, (82, GROUND + 11.5))
    ax.add_patch(Circle((89, 67), 6.4, fc='#c98d55', ec='none', zorder=22))
    for k in range(14):
        a = np.radians(k * 26)
        ax.plot([89 + 1.2 * np.cos(a), 89 + 6.0 * np.cos(a)], [67 + 1.2 * np.sin(a) - 1, 67 + 6.0 * np.sin(a) - 1],
                color='#a8703f', lw=0.6, zorder=22)
    for (dx, dy, ang) in ((-2.2, 1.5, 60), (2.4, -1.6, 120)):
        beetle(ax, 89 + dx, 67 + dy, 4.2, '#5d1f1f', angle=ang, z=23, lw=0.6)
    # badges
    badge(ax, 56, 52, 'a')
    badge(ax, 76, 16, 'b')
    badge(ax, 28, 31, 'c')
    badge(ax, 79, 69, 'd')
    save(fig, fid)


if __name__ == '__main__':
    draw('img146')
