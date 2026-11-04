from bio_kit import *

b = Board('img155', lw=1.8, font=23.5)
A = dict(style='->', head=12, width=6)
for x, g in [(190, 'A'), (405, 'B')]:
    b.text(x, 22, f'Gen {g}')
    b.text(x, 106, f'Enzim {g}')
    b.arrow(x, 36, x, 93, **A)
    b.arrow(x, 122, x, 180, **A)
b.text(13, 188, 'Chất trắng 1', ha='left')
b.arrow(139, 188, 229, 188, **A)
b.text(230, 188, 'Chất trắng 2', ha='left')
b.arrow(350, 188, 439, 188, **A)
b.text(441, 188, 'Chất đỏ', ha='left')
b.save()
