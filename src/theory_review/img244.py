from tabgeo_kit import *

P = {"A'": (91, 20), "C'": (309, 20), "B'": (177, 107), 'A': (46, 241), 'C': (266, 241), 'B': (133, 325)}
G = Geo('img244', P, fs=21, lw=2.0)
G.edges("A'-C' A'-B' B'-C' A'-A C'-C B'-B A-B B-C")
G.edges('A-C', dashed=True)
G.dash = (6, 5)
G.labs({"A'": ('w', 25), "C'": ('e', 25), "B'": (-35, 28), 'A': ('w', 24), 'C': ('e', 20), 'B': ('s', 25)})
G.save()
