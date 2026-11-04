from tabgeo_kit import *

P = {'A': (148, 37), 'B': (50, 190), 'C': (93, 262), 'D': (259, 233)}
G = Geo('img048', P, fs=17, lw=1.7)
G.dash = (5, 4)
P = G.P
P['I'] = tuple(G.mid('A', 'B'))
P['J'] = tuple(G.mid('C', 'D'))
P['G'] = tuple(G.mid('I', 'J'))
G.edges('A-B A-D B-C C-D A-C')
G.edges('B-D I-J', dashed=True)
for k in 'ABCD':
    G.vec('G', k, dashed=True, L=12, w=4.5)
G.labs({'A': ('n', 20), 'B': ('w', 20), 'C': ('s', 22), 'D': (-20, 20), 'I': ('nw', 18), 'J': ('s', 20),
        'G': (20, 22)}, text=None)
G.save()
