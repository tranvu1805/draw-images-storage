from bio_kit import *

b = Board('img157', lw=1.0, font=17.5)
A = dict(head=6, width=3)
for xg, xe, xa, ya, g in [(186, 180, 192, 99, 'K'), (330, 330, 333, 99, 'L'), (488, 490, 494, 104, 'M')]:
    b.text(xg, 22, f'Gen {g}')
    b.text(xe, 65, f'Enzim {g}')
    b.arrow(xg, 31, xg, 56, **A)
    b.arrow(xa, 75, xa, ya, **A)
y = 110
x1 = b.extent(b.text(7, y, 'Chất không màu', ha='left'))[1]
b.arrow(max(x1 + 6, 131), y, 185, y, **A)
x1 = b.extent(b.text(190, y, 'Chất không màu', ha='left'))[1]
b.arrow(x1, y, 376, y, **A)
x1 = b.extent(b.text(380, y, 'Sắc tố vàng', ha='left'))[1]
b.arrow(x1 + 3, y, 535, y, **A)
b.text(537, y, 'Sắc tố đỏ', ha='left')
b.save()
