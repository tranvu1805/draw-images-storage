from tabgeo_kit import *

P = {'S': (131, 32), 'A': (107, 184), 'B': (27, 264), 'C': (187, 264), 'D': (267, 184)}
P['O'] = ((P['A'][0] + P['C'][0]) / 2, (P['A'][1] + P['C'][1]) / 2)
P['G'] = (P['S'][0] + 0.7 * (P['O'][0] - P['S'][0]), P['S'][1] + 0.7 * (P['O'][1] - P['S'][1]))
G = Geo('img033', P, fs=16, lw=1.3)
G.edges('S-B S-C S-D B-C C-D')
G.edges('S-A A-B A-D A-C B-D S-O', dashed=True)
for k in P:
    G.dot(k, r=4.5)
G.labs({'S': ('n', 18), 'A': ('w', 16), 'B': ('s', 18), 'C': ('s', 18), 'D': ('ne', 20), 'O': ('s', 18),
        'G': ('w', 18)})
G.save()
