from tabgeo_kit import *

P = {'A': (35, 124), 'B': (280, 124), 'C': (347, 35), 'D': (106, 35),
     "A'": (35, 243), "B'": (280, 243), "C'": (347, 153), "D'": (106, 153)}
G = Geo('img047', P, fs=17, lw=2.6)
G.edges("A-B B-C C-D D-A A-A' B-B' C-C' A'-B' B'-C'")
G.edges("D-D' D'-C' D'-A'", dashed='dot')
for k in P:
    G.dot(k, r=5)
G.labs({'A': ('w', 18), 'B': (120, 22), 'C': ('n', 20), 'D': ('n', 20), "A'": (-110, 24), "B'": (-50, 22),
        "C'": (-40, 24), "D'": (-55, 24)})
G.save()
