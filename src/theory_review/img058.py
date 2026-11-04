from tabgeo_kit import *

T = Table('img058', hl=[12, 75, 129, 256], vl=75, box=(9, 507), fs=15)
T.names(['x', "y'", 'y'])
T.xrow([123, 294, 471], ['-\\infty', '3', '+\\infty'])
T.signs(['', '-', '||', '-', ''], bar_dx=2.8, gaps={1: 199, 3: 409})
T.values([(0, 148, '2', -29), (2, 245, '-\\infty', -23), (2, 145, '+\\infty', 26), (4, 242, '2', 21)])
T.save()
