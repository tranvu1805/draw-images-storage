from bio_kit import *

# p-xylene --(O2, -H2O)--> terephthalic acid
b = Board('img020', size=(398, 213), lw=1.7, font=21)
# p-xylene
V = b.ring((60, 120), 31, doubles=(0, 2, 4))
b.line(V[0], (60, 60), cap='round')
b.line(V[3], (60, 180), cap='round')
b.text(51, 48, r'CH$_3$', ha='left')
b.text(51, 192, r'CH$_3$', ha='left')
# arrow with conditions
b.arrow(117, 118, 186, 118, style='->', head=9, width=4.5, lw=1.4)
b.text(151, 103, r'O$_2$', size=20)
b.text(149, 134, r'$-$ H$_2$O', size=20)
# terephthalic acid
W = b.ring((263, 111), 31, doubles=(0, 2, 4))
for v, cy, oy in [(W[0], 44, 25), (W[3], 178, 197)]:
    b.line(v, (263, cy), cap='round')
    b.bond((263, cy), (237, oy), 2, off=4.5, trim=(0, 3))
    b.bond((263, cy), (288, oy + (2 if oy < 100 else -2)), 1, trim=(0, 2))
    b.text(229, oy - 1, 'O')
    b.text(290, oy - 1, 'OH', ha='left')
b.keep_canvas()
b.save()
