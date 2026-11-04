from tabgeo_kit import *

P = {'A': (72, 27), 'C': (253, 27), 'B': (115, 69), 'A\'': (28, 170), "C'": (208, 170), "B'": (70, 212)}
P['M'] = ((P['B'][0] + P["B'"][0]) / 2, (P['B'][1] + P["B'"][1]) / 2)
G = Geo('img243', P, fs=15, lw=1.5)
G.edges("A-C A-B B-C A-A' C-C' A'-B' B'-C' B-B' A-M")
G.edges("A'-C'", dashed=True)
for k in P:
    if k != 'M':
        G.dot(k, r=4.5)
G.dot('M', r=4.5, hollow=True)
G.labs({'A': (120, 15), 'C': ('e', 12), 'B': ('n', 13), 'M': ('e', 13), "A'": ('w', 15), "C'": ('e', 14),
        "B'": ('s', 14)})
G.save()
