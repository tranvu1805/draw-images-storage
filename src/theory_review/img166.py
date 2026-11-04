from tabgeo_kit import *

T = Table('img166', hl=[7, 39, 71, 163], vl=60, fs=13, rule_x=(8, 435))
T.names(['x', "y'", 'y'])
T.xrow([88, 194, 300, 408], ['-\\infty', '0', '2', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''], gaps={1: 140, 3: 248, 5: 353})
T.values([(0, 153, '-\\infty'), (2, 89, '1'), (4, 151, '-3'), (6, 88, '0')])
T.save()
