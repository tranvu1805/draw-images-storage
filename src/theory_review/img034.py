from tabgeo_kit import *

P = {'B': (90, 231), 'C': (251, 231), 'D': (296, 183), 'A': (135, 183),
     "B'": (90, 87), "C'": (251, 87), "D'": (296, 38), "A'": (135, 38)}
G = Geo('img034', P, fs=16, lw=1.3)
G.edges("B-C C-D D-D' B-B' C-C' B'-C' C'-D' D'-A' A'-B'")
G.edges("A-B A-D A-A'", dashed=True)
for k in P:
    G.dot(k, r=3.5)
G.labs({'A': ('w', 17), 'B': ('sw', 20), 'C': ('s', 18), 'D': ('e', 18), "A'": ('nw', 18), "B'": ('w', 20),
        "C'": (-30, 22), "D'": ('ne', 18)})
G.save()
