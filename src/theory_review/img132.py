from bio_kit import *

# wave = tóc quăn, vl = tóc thẳng; letters inside = blood groups
b = Board('img132', lw=1.1, font=20, r=16.5)
P = {
    '1': (61, 48, 'm', ''), '2': (149, 48, 'f', ''), '3': (284, 47, 'm', ''), '4': (370, 47, 'f', ''),
    '5': (51, 120, 'f', 'vl'), '6': (105, 120, 'f', 'vl'), 'T': (159, 118, 'm', 'wave'),
    'H': (271, 119, 'f', 'wave'), '9': (383, 119, 'm', 'vl'),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, sp=3.4 if pat == 'vl' else 4.2, plw=0.9)
b.mate('1', '2', y=49); b.kids(106, 49, 87, ['5', '6', 'T'])
b.mate('3', '4'); b.kids(327, 47, 86, ['H', '9'], xs=[270, 381])
b.mate('T', 'H', lw=0.9)
for x, y, s in [(60, 16, '1'), (149, 16, '2'), (282, 16, '3'), (370, 16, '4'), (20, 112, '5'), (81, 112, '6'),
                (357, 121, '9'), (158, 149, 'T'), (266, 149, 'H'), (367, 76, 'O')]:
    b.text(x, y, s)
for x, y, s in [(159, 118, 'A'), (271, 118, 'A'), (383, 120, 'O')]:
    b.text(x, y, s, bbox=dict(fc='white', ec='none', pad=0.6, alpha=0.85))
b.legend(447, 50, 'm', 'wave', 'Tóc quăn', dx=21, sp=4.2, plw=0.9)
b.legend(447, 103, 'm', 'vl', 'Tóc thẳng', dx=25, sp=3.4, plw=0.9)
b.save()
