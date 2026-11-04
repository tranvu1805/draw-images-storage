# Several chicken breeds produced by breeders from the wild junglefowl.
from photo_kit import *

fig, ax = board('img137', 100)            # y 0..40.4


def node(x, y, s, w, fc, ec):
    box(ax, x - w / 2, y - 4, w, 8, s, size=12, fc=fc, ec=ec, lw=1.2, r=2.0, weight='bold')


node(50, 33, 'Gà rừng', 26, '#fff1d6', '#b5651d')
node(14, 8, 'Gà chọi', 24, '#eef4fb', '#3d6fa8')
node(47, 6, 'Gà Đông Tảo', 31, '#eef4fb', '#3d6fa8')
node(82.5, 8, 'Gà tre Tân Châu', 34, '#eef4fb', '#3d6fa8')
for x1, y1 in ((20, 12.2), (47, 10.2), (76, 12.2)):
    arr(ax, 50 + (x1 - 50) * 0.25, 28.8, x1, y1, color='#7a4a1c', lw=1.4, head=8)
save(fig, 'img137')
