from tabgeo_kit import *

T = Table('img235', hl=[9, 33, 58, 167], vl=50, fs=12, rule_x=(12, 433))
T.names(['x', "y'", 'y'], dy=[0, 0, -16])
T.xrow([68, 184, 309, 416], ['-\\infty', '-1', '3', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''], gaps={1: 130, 3: 245, 5: 355})
T.values([(0, 159, '-\\infty'), (2, 93, '1'), (4, 118, '-\\dfrac{29}{3}', -3), (6, 66, '+\\infty')])
T.save()
