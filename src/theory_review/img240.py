from tabgeo_kit import *

P = {'S': (127, 31), 'A': (24, 205), 'B': (84, 274), 'C': (248, 207)}
G = Geo('img240', P, fs=17, lw=1.6)
G.edges('S-A S-B S-C A-B B-C')
G.edges('A-C', dashed=True)
for k in P:
    G.dot(k, r=5)
G.labs({'S': ('n', 17), 'A': (170, 14), 'B': ('s', 18), 'C': ('e', 16)})
G.save()
