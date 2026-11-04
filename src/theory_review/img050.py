from tabgeo_kit import *

P = {'a': (6, 10), 'b': (234, 10), 'c': (234, 237), 'd': (6, 237),
     't': (120, 51), 'r': (192, 124), 'u': (120, 196), 'l': (48, 124)}
G = Geo('img050', P, fs=19, lw=1.1)
G.poly('a b c d', lw=1.5)
G.edges('a-t b-t b-r c-r c-u d-u d-l a-l t-r r-u u-l l-t')
G.text(120, 254, r'$6\ \mathrm{dm}$', fs=19)
G.save()
