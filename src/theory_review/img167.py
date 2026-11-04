from tabgeo_kit import *

T = Table('img167', hl=[0, 34, 71, 171], vl=75, fs=12.5, rule_x=(4, 547))
T.names(['x', "y'", 'y'])
T.xrow([103, 236, 387, 522], ['-\\infty', '-3', '1', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''], gaps={1: 152, 3: 312, 5: 456})
T.values([(0, 151, '-\\infty', -5), (2, 85, '42', 3), (4, 150, '10'), (6, 87, '+\\infty')])
T.save()
