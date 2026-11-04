from tabgeo_kit import *

T = Table('img169', hl=[0, 36, 77, 141], vl=44, fs=12.5, rule_x=(7, 315))
T.names(['x', "y'", 'y'])
T.xrow([59, 140, 218, 299], ['-\\infty', '0', '2', '+\\infty'])
T.signs(['', '-', '0', '+', '0', '-', ''], gaps={1: 103, 3: 180, 5: 258})
T.values([(0, 92, '+\\infty'), (2, 116, '0'), (4, 90, '4'), (6, 117, '-\\infty', -4)])
T.save()
