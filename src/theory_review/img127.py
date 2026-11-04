from bio_kit import *

BR = '#b97a57'
b = Board('img127', lw=2.0, font=13, r=11)
P = {
    '1a': (33, 33, 'f', ''), '2a': (89, 33, 'm', BR), '1b': (156, 33, 'f', ''), '2b': (208, 33, 'm', ''),
    '3': (58, 98, 'm', ''), '4': (130, 98, 'f', BR), '5': (183, 98, 'm', ''), '6': (225, 98, 'm', ''),
    '7': (266, 98, 'm', BR),
    '8': (30, 167, 'm', ''), '9': (73, 167, 'm', ''), '10': (127, 167, 'f', BR), '11': (181, 167, 'f', BR),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat)
    b.text(x + 1, y + {33: 19, 98: 23, 167: 25}[y], n, weight='bold')
GROUPS = [(34, 13, 'AB'), (90, 13, 'O'), (157, 13, 'A'), (208, 13, 'O'), (55, 79, 'B'), (125, 79, 'A'),
          (177, 79, 'A'), (219, 79, 'A'), (260, 79, 'A'), (22, 149, 'AB'), (66, 149, 'B'), (121, 149, 'A'),
          (174, 149, 'O')]
for x, y, s in GROUPS:
    b.text(x, y, s, weight='bold', size=12.5)
b.mate('1a', '2a'); b.line((59, 33), (59, b.top('3')))
b.mate('1b', '2b'); b.kids(183, 33, 63, ['4', '5', '6', '7'])
b.mate('3', '4'); b.kids(97, 98, 135, ['8', '9', '10', '11'])
b.text(441, 26, 'Quy ước:', weight='bold', size=12)
for x, y, sx, pat in [(328, 50, 'm', ''), (354, 50, 'f', ''), (328, 75, 'm', BR), (354, 75, 'f', BR)]:
    b.legend(x, y, sx, pat, None)
b.text(380, 50, 'Nam  Nữ không bị bệnh', ha='left', weight='bold', size=11.5)
b.text(380, 75, 'Nam  Nữ bị bệnh', ha='left', weight='bold', size=11.5)
for i, (g, t) in enumerate([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')]):
    b.text(347, 118 + 15 * i, f'{g} - nhóm máu {t}', ha='left', weight='bold', size=12)
b.save()
