from bio_kit import *

# 'dash' = bệnh G, 'x' = bệnh H; II-6 has both
b = Board('img116', lw=1.4, font=10, r=7.5)
P = {
    'a': (68, 20, 'f', ''), 'b': (112, 20, 'm', ''), 'c': (183, 20, 'f', 'dash'), 'd': (226, 20, 'm', 'x'),
    '1': (50, 59, 'm', ''), '2': (78, 59, 'f', 'x'), '3': (103, 59, 'f', ''), '4': (126, 59, 'm', 'dash'),
    '5': (166, 59, 'f', ''), '6': (242, 59, 'f', 'dash x'),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, sp=4.4)
    if n.isdigit():
        b.text(x, 77, n)
b.kids(b.mate('a', 'b'), 20, 39, ['1', '2', '3', '4'])
b.kids(b.mate('c', 'd'), 20, 39, ['5', '6'])
mx = b.mate('4', '5')
b.line((mx, 59), (mx, 93))
b.text(mx, 105, '?', size=15, weight='bold')
for y, s in [(23, 'I'), (60, 'II'), (104, 'III')]:
    b.text(14, y, s, size=15, weight='bold')
b.text(283, 22, 'Quy ước :', ha='left', size=13)
for y, sx, pat, t in [(22, 'm', '', 'Nam bình thường'), (43, 'm', 'dash', 'Nam bị bệnh G'),
                      (63, 'm', 'x', 'Nam bị bệnh H'), (93, 'f', '', 'Nữ bình thường'),
                      (116, 'f', 'dash', 'Nữ bị bệnh G'), (143, 'f', 'x', 'Nữ bị bệnh H')]:
    b.legend(360, y, sx, pat, t, dx=14, size=14, s=7, r=7, sp=4.2)
b.save()
