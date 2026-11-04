from tabgeo_kit import *

P = {"A'": (80, 16), "B'": (232, 16), "D'": (22, 53), "C'": (177, 53),
     'A': (77, 155), 'B': (232, 155), 'D': (22, 192), 'C': (177, 192)}
G = Geo('img241', P, fs=15, lw=1.5)
G.edges("A'-B' A'-D' D'-C' C'-B' D'-D C'-C B'-B D-C C-B")
G.edges("A-A' A-B A-D", dashed=True)
for k in P:
    G.dot(k, r=4.5)
G.text(65, 10, f"${tex(chr(65) + chr(39))}$", fs=15)
G.labs({"B'": (30, 16), "D'": (150, 15), "C'": (95, 14), 'A': (140, 13), 'B': ('e', 14), 'D': (210, 14),
        'C': (-60, 13)})
G.save()
