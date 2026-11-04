from tabgeo_kit import *

T = Table('img052', hl=[21, 54, 95, 236], vl=78, box=(14, 673), fs=17)
T.names(['x', "f'(x)", 'f(x)'])
T.xrow([103, 272, 471, 648], ['-\\infty', '0', '2', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''], gaps={1: 175, 3: 377, 5: 575})
T.values([(0, 225, '-\\infty', -4), (2, 113, '4', 5), (4, 209, '0'), (6, 112, '+\\infty')])
T.save()
