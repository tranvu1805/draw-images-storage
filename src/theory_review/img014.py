from bio_kit import *

# glutamic acid, skeletal formula; wedge from the alpha carbon to NH2
b = Board('img014', size=(320, 151), lw=2.0, font=28)
C1, C2, C3, C4, C5 = (78, 60), (119, 84), (160, 60), (200, 84), (241, 60)
O1, O2 = (78, 15), (241, 15)
b.bond(C1, O1, 2, off=5, trim=(0, 11))
b.bond(C5, O2, 2, off=5, trim=(0, 11))
b.bond((52, 76), C1)
for p, q in [(C1, C2), (C2, C3), (C3, C4), (C4, C5)]:
    b.bond(p, q)
b.bond(C5, (272, 78))
b.wedge(C4, (200, 117), w=4.2)
b.text(78, 14, 'O')
b.text(241, 14, 'O')
b.text(52, 85, 'HO', ha='right')
b.text(270, 85, 'OH', ha='left')
b.text(200, 136, 'N')
b.text(210, 136, r'H$_2$', ha='left')
b.save()
