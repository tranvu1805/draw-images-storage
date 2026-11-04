# A freshwater lake community: many species living together (plants, insects, fish, amphibians,
# reptiles, birds, molluscs). Cross-section of a lake with its banks.
from photo_kit import *

fig, ax = board('img148', 100)            # y 0..63.8
H = 63.8
SURF = 41.0
# sky + far bank with trees
ax.add_patch(Rectangle((0, 40), 100, H - 40, fc='#d6ecfa', ec='none', zorder=0))
ax.add_patch(Polygon([(0, 40), (0, 52), (20, 54), (45, 51), (70, 54), (100, 52), (100, 40)], fc='#8bc34a',
                     ec='none', zorder=1))
for x, h, r, c in ((6, 9, 6.5, '#3f8f3a'), (17, 11, 7, '#4f9a45'), (31, 8, 5.5, '#3f8f3a'), (73, 10, 6.5, '#4f9a45'),
                   (86, 12, 7.5, '#3f8f3a'), (97, 8, 5.5, '#4f9a45')):
    tree(ax, x, 50, h, r, crown=c, z=1)
# soil + basin
ax.add_patch(Polygon([(0, 0), (100, 0), (100, SURF), (0, SURF)], fc='#8d5a3b', ec='none', zorder=2))
for xa, xb in ((0, 8.5), (91.5, 100)):   # grass on the near banks
    ax.add_patch(Polygon([(xa, SURF - 1.5), (xb, SURF - 1.5), (xb, SURF + 1.5), (xa, SURF + 1.5)], fc='#7cb342',
                         ec='none', zorder=2))
t = np.linspace(0, np.pi, 100)
xs = 50 - 43 * np.cos(t)
ys = SURF - 31 * np.sin(t) ** 0.7
ax.add_patch(Polygon(np.column_stack([xs, ys]), fc='#8fc6ea', ec='#c2a272', lw=2.4, zorder=3))
ax.add_patch(Polygon(np.column_stack([50 - 41 * np.cos(t), SURF - 0.2 - 4 * np.sin(t) ** 0.3]), fc='#b3dbf4',
                     ec='none', zorder=3))
ax.plot([7, 93], [SURF, SURF], color='#5c9ccc', lw=1.0, zorder=4)
# reeds / cattails at the edges, submerged plants
for x, lean in ((9, -1.0), (11, -0.4), (13, 0.3), (87, 0.4), (89, 1.0), (91, -0.3)):
    reed(ax, x, SURF - 6, 17, lean=lean, z=6)
rng = np.random.default_rng(4)
for x0 in (20, 23, 33, 58, 62, 79, 82):
    yb = SURF - 30 * np.sin(np.arccos((50 - x0) / 43)) ** 0.7 + 1
    hh = rng.uniform(10, 16)
    ys_ = np.linspace(yb, yb + hh, 30)
    ax.plot(x0 + 0.8 * np.sin(ys_ * 0.6), ys_, color='#3d8b37', lw=1.2, zorder=4)
    for yy in np.arange(yb + 2, yb + hh, 3):
        ax.add_patch(Ellipse((x0 + 0.8 * np.sin(yy * 0.6) + 1.2, yy), 2.2, 0.8, angle=30, fc='#4caf50', ec='none',
                             zorder=4))
# surface: water lilies, frog, ducks, snake, dragonfly
lilypad(ax, 18, SURF, 5, flower=True, z=7)
lilypad(ax, 24.5, SURF, 6, z=7)
lilypad(ax, 31, SURF, 4.5, flower=True, z=7)
frog(ax, 24.5, SURF + 1.4, 3.6, z=8)
duck(ax, 62, SURF, 7, facing=-1, z=8)
for k, x in enumerate((70, 74.5, 79)):
    duck(ax, x, SURF, 3.6, facing=-1, body='#f5d142', head='#f5d142', z=8)
sx = np.linspace(40, 50, 60)
ax.plot(sx, SURF + 0.6 + 0.7 * np.sin(sx * 1.6), color='#3a3a3a', lw=2.6, zorder=8, solid_capstyle='round')
ax.add_patch(Ellipse((50.6, SURF + 1.2), 2.2, 1.3, fc='#3a3a3a', zorder=9))
for k in (-1, 1):   # dragonfly
    ax.add_patch(Ellipse((54 + k * 1.6, 49.5), 3.2, 0.9, angle=k * 12, fc='#cfe8ff', ec='#5b8db8', lw=0.5, zorder=8))
    ax.add_patch(Ellipse((54 + k * 1.5, 48.7), 2.8, 0.8, angle=-k * 12, fc='#cfe8ff', ec='#5b8db8', lw=0.5, zorder=8))
ax.plot([54, 54], [46.5, 50.5], color='#1e5aa8', lw=1.6, zorder=9)
# in the water: fish, tadpoles, a turtle on a sunken log, water beetle
fish(ax, 47, 24, 11, '#d9a441', facing=1)
fish(ax, 30, 34, 5.5, '#f08a24', facing=1)
fish(ax, 36, 30.5, 5, '#f08a24', facing=-1)
fish(ax, 70, 33, 6, '#9aa86a', facing=-1, stripes=True)
for x, y in ((20, 30), (23, 28.5), (21, 26)):
    tadpole(ax, x, y, 2.6)
ax.add_patch(Polygon([(59, 15), (87, 27.5), (88, 25), (60, 12.5)], fc='#6d4c33', ec='#4a3322', lw=0.8, zorder=5))
turtle(ax, 76, 24.6, 6, facing=1, z=6)
beetle(ax, 41, 36, 3.2, '#2f3b2f', angle=200, z=6, lw=0.5)
# bottom: mussels and a snail
for x, y in ((36, 13.2), (42, 12.0), (49, 11.6)):
    ax.add_patch(Ellipse((x, y), 4.2, 2.0, angle=8, fc='#7d6e63', ec='#3f3631', lw=0.7, zorder=6))
    ax.add_patch(Ellipse((x - 0.5, y + 0.3), 1.8, 0.6, angle=8, fc='#c9bdb3', ec='none', zorder=7))
snail(ax, 27, 16.3, 3)
save(fig, 'img148')
