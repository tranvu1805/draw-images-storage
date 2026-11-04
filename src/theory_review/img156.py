from bio_kit import *

b = Board('img156', lw=0.9, font=16)
A = dict(style='->', head=4, width=2.6)
for x, g in [(79, 'A'), (233, 'B'), (373, 'D')]:
    b.text(x, 21, f'Gen {g}')
    b.text(x, 64, f'Enzyme {g}')
    b.arrow(x - 1, 37, x - 1, 51, **A)
    b.arrow(x - 1, 81, x - 1, 95, **A)
R = dict(style='->', head=4.5, width=3)
y = 112
for x, s, gap in [(11, 'Chất không màu 1', 5), (165, 'Chất không màu 2', 9), (328, 'Sắc tố vàng', 5)]:
    x1 = b.extent(b.text(x, y, s, ha='left'))[1]
    b.arrow(x1 + gap, y, x1 + gap + 14, y, **R)
b.text(464, y, 'Sắc tố đỏ', ha='left')
b.save()
