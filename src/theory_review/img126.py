from bio_kit import *

H = 'adiag'  # bệnh P (hatched), black = bệnh Q
b = Board('img126', lw=1.1, font=14, r=6.5)
P = {
    'a': (50, 13, 'f', H), 'b': (85, 13, 'm', ''), 'c': (190, 13, 'f', ''), 'd': (222, 13, 'm', 'k'),
    'e': (43, 50, 'm', ''), 'f': (89, 50, 'f', H), 'g': (122, 50, 'm', ''), 'h': (148, 50, 'm', ''),
    'i': (183, 50, 'f', ''), 'j': (229, 50, 'm', ''),
    'k': (104, 74, 'm', H), 'l': (168, 74, 'f', ''),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, rx=6.5, ry=7.5, sp=2.4, plw=0.8)
b.mate('a', 'b'); b.kids(68, 13, 30, ['e', 'f'])
b.mate('c', 'd'); b.kids(207, 13, 30, ['i', 'j'])
b.mate('f', 'g'); b.line((105, 50), (105, b.top('k')))
b.mate('h', 'i'); b.line((168, 50), (168, b.top('l')))
mx = b.mate('k', 'l'); b.line((mx, 74), (mx, 88))
b.text(mx, 99, '?', size=13)
for y, s in [(15, 'I'), (49, 'II'), (76, 'III')]:
    b.text(14, y, s, size=14)
b.text(260, 10, 'Ghi chú:', ha='left', size=15)
for y, sx, pat, t in [(9, 'f', '', ': nữ bình thường'), (26, 'm', '', ': nam bình thường'),
                      (43, 'f', H, ': nữ mắc bệnh P'), (60, 'm', H, ': nam mắc bệnh P'), (77, 'm', 'k', ': nam mắc bệnh Q')]:
    b.legend(325, y, sx, pat, t, dx=8, size=15, s=6, rx=6.5, ry=7, sp=2.4, plw=0.8)
b.save()
