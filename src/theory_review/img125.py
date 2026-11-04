from bio_kit import *

M = '#880015'
b = Board('img125', lw=1.2, font=19, r=15.5)
P = {
    'u': (30, 81, 'm', M), 'g': (106, 85, 'f', ''), 'gh': (199, 85, 'm', ''),
    'mil': (328, 85, 'f', M), 'fil': (431, 85, 'm', ''),
    '1': (147, 148, 'f', ''), '2': (311, 152, 'm', ''), 's': (414, 150, 'f', M), 'c': (219, 225, 'f', ''),
}
for n, (x, y, sx, pat) in P.items():
    b.person(n, x, y, sx, pat, rx=12.5, ry=15)
# siblings drawn without parents: bracket over the square and the circle
b.line((30, b.top('u')), (30, 35), (104, 35), (104, 70.5))
b.mate('g', 'gh'); b.line((151, 85), (151, 148 - 15 * np.sqrt(1 - (4 / 12.5) ** 2)))
b.mate('mil', 'fil'); b.kids(381, 85, 117, ['2', 's'])
b.mate('1', '2', y=149); b.line((219, 149), (219, b.top('c')))
b.text(115, 148, '1', color=M, family='DejaVu Sans')
b.text(342, 152, '2', color=M, family='DejaVu Sans')
b.save()
