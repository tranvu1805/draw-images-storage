from bio_kit import *

b = Board('img114', lw=1.1, font=14, r=6.5)
SQ = 'dots bs'  # straight hair + colour-blind male (dotted square with a thick diagonal)
P = {
    '1': (67, 10, 'f', ''), '2': (114, 10, 'm', ''),
    '3': (61, 50, 'f', ''), '4': (91, 50, 'm', ''), '5': (130, 50, 'f', ''), '6': (174, 50, 'm', ''),
    '7': (212, 50, 'f', ''), '8': (264, 50, 'm', ''),
    '9': (132, 86, 'm', SQ), '10': (174, 86, 'm', ''), '11': (214, 86, 'f', ''), '12': (260, 86, 'm', SQ),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, rx=7, ry=6, sp=3.3)
LAB = {'1': (67, 23), '2': (114, 23), '3': (61, 64), '4': (91, 64), '5': (130, 64), '6': (176, 64),
       '7': (212, 64), '8': (262, 64), '9': (132, 100), '10': (176, 100), '11': (220, 100), '12': (260, 100)}
for n, (x, y) in LAB.items():
    b.text(x, y, n)
b.kids(b.mate('1', '2'), 10, 33, ['3', '4', '5'])
b.kids(b.mate('5', '6'), 50, 68, ['9', '10'])
b.kids(b.mate('7', '8'), 50, 67, ['11', '12'])
mx = b.mate('10', '11')
b.line((mx, 86), (mx, 97))
b.text(mx + 1, 107, '?', weight='bold')
for y, s in [(12, 'I'), (50, 'II'), (86, 'III')]:
    b.text(20, y, s, size=13)
b.text(370, 10, 'Quy ước:', ha='left', size=13)
for y, sx, pat, t in [(37, 'm', '', ': Nam tóc quăn và không bị mù màu'), (52, 'f', '', ': Nữ tóc quăn và không bị mù màu'),
                      (66, 'm', SQ, ': Nam tóc thẳng và bị mù màu')]:
    b.legend(376, y, sx, pat, t, dx=6, size=13, s=5.5, rx=6, ry=5, sp=3)
b.save()
