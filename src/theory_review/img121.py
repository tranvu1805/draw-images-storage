from bio_kit import *

# black = mù màu + máu khó đông, '/' hatch = máu khó đông; III-1..3 carry a horizontal strike line as in the source
b = Board('img121', lw=1.2, font=17, r=13)
HC = '#555555'
P = {
    'I1': (113, 22, 'm', 'k'), 'I2': (187, 22, 'f', ''),
    'II1': (150, 74, 'f', ''), 'II2': (223, 75, 'm', 'diag'),
    'III1': (81, 145, 'm', 'k strike'), 'III2': (149, 146, 'f', 'strike'), 'III3': (217, 146, 'f', 'diag strike'),
    'III4': (290, 147, 'm', 'diag'),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, sp=4.2, pc=HC, plw=0.9)
LAB = [(113, 49, '1'), (186, 49, '2'), (149, 96, '1'), (226, 99, '2'), (80, 174, '1'), (149, 174, '2'),
       (217, 174, '3'), (290, 174, '4')]
for x, y, s in LAB:
    b.text(x, y, s)
b.mate('I1', 'I2'); b.line((150, 22), (150, b.top('II1')))
b.mate('II1', 'II2'); b.kids(186, 75, 111, ['III1', 'III2', 'III3', 'III4'])
for y, s in [(17, 'I'), (77, 'II'), (145, 'III')]:
    b.text(28, y, s, size=16)
b.legend(372, 35, 'm', 'k', None)
b.legend(372, 82, 'm', 'diag', None, sp=4.2, pc=HC, plw=0.9)
b.legend(413, 81, 'f', 'diag', None, sp=4.2, pc=HC, plw=0.9)
b.legend(372, 127, 'f', '', None)
b.legend(414, 127, 'm', '', None)
for x, y, t in [(440, 36, 'Mù màu và máu khó đông'), (441, 79, 'Máu khó đông'), (448, 124, 'Không bị bệnh')]:
    b.text(x, y, t, ha='left', size=17, weight='bold')
b.save()
