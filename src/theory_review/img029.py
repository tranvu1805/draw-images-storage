from tabgeo_kit import *

G = Geo('img029', {'A': (74, 289), 'B': (208, 289), 'C': (272, 218), 'D': (139, 218),
                   "A'": (41, 107), "B'": (176, 107), "C'": (239, 35), "D'": (107, 35)}, fs=19, lw=2.0)
G.edges("A-B B-B' A-A' C-C' A'-B' C'-D'")
G.edges("D-D' D-C", dashed=True)
G.vec('A', 'D', dashed=True, L=14, w=5.5)
G.vec("A'", "D'", L=14, w=5.5)
G.vec("B'", "C'", L=14, w=5.5)
G.vec('B', 'C', L=14, w=5.5)
G.labs({'A': ('s', 16), 'B': ('s', 16), 'C': ('e', 17), 'D': (-60, 20), "A'": ('w', 20), "B'": (-20, 18),
        "C'": ('n', 18), "D'": ('n', 18)})
G.save()
