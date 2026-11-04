from tabgeo_kit import *

P = {'S': (234, 40), 'A': (139, 248), 'B': (30, 376), 'C': (323, 375), 'D': (432, 248)}
P['O'] = ((P['A'][0] + P['C'][0]) / 2, (P['A'][1] + P['C'][1]) / 2)
G = Geo('img246', P, fs=21, lw=1.5)
G.dash = (6, 4)
G.edges('S-B S-C S-D B-C C-D')
G.edges('S-A A-B A-D A-C B-D', dashed=True)
for k in P:
    G.dot(k, r=5)
G.labs({'S': (45, 20), 'A': (20, 21), 'B': ('s', 22), 'C': (-45, 24), 'D': (40, 22), 'O': (172, 34)})
G.save()
