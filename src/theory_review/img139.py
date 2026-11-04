# Gene flow: a brown beetle migrates from the brown population into the green one.
from photo_kit import *

fig, ax = board('img139', 100)            # y 0..40.2
ax.add_patch(Circle((20, 20), 18.5, fc=GREY, ec='none', zorder=0))
ax.add_patch(Circle((80, 20), 18.5, fc=GREY, ec='none', zorder=0))
for x, y, a in [(15, 31, 80), (29, 28, 60), (7, 20, 120), (21, 18, 100), (12, 8, 70), (29, 9, 40)]:
    beetle(ax, x, y, 11, GREEN, angle=a)
for x, y, a in [(77, 31, 110), (91, 26, 80), (71, 18, 130), (87, 12, 60), (77, 7, 100)]:
    beetle(ax, x, y, 11, BROWN, angle=a)
beetle(ax, 51, 20, 11, BROWN, angle=170)               # the migrant
arr(ax, 64, 23, 40, 16, color=RED, lw=3.2, head=11, rad=-0.15, z=8)
save(fig, 'img139')
