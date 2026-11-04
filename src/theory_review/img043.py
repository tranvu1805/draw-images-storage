from tabgeo_kit import *

G = Geo('img043', {'S': (124, 22), 'A': (124, 197), 'B': (37, 283), 'C': (210, 283), 'D': (298, 197)},
        fs=17, lw=1.7)
G.edges('S-B S-C S-D B-C C-D')
G.edges('S-A A-B A-D', dashed=True)
G.labs({'S': (125, 14), 'A': (155, 15), 'B': ('sw', 16), 'C': (-60, 16), 'D': ('e', 15)})
G.save()
