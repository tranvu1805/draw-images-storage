from tabgeo_kit import *

# the original labels the sign row f(x) (sic) - kept as is
T = Table('img171', hl=[6, 47, 91], vl=47, fs=11.5, rule_x=(9, 529))
T.names(['x', 'f(x)'], dy=[-6, 2])
T.xrow([63, 164, 279, 393, 502], ['-\\infty', '1', '2', '3', '+\\infty'], dy=-4)
T.signs(['', '-', '0', '+', '0', '-', '0', '+', ''], dy=2, gaps={1: 108, 3: 216, 5: 340, 7: 452})
T.save()
