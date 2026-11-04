from tabgeo_kit import *

T = Table('img265', hl=[4, 29, 56, 130], vl=51, fs=12.5, rule_x=(10, 370))
T.names(['x', "y'", 'y'], dy=[0, 0, -2])
T.xrow([69, 152, 263, 356], ['-\\infty', '-1', '3', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''], gaps={1: 103, 3: 208, 5: 316})
T.values([(0, 125, '-\\infty', -14, 'left'), (2, 78, '4', 5), (4, 116, '-2', -1), (6, 64, '+\\infty')])
T.save()
