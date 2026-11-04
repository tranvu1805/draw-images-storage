from tabgeo_kit import *

T = Table('img041', hl=[7, 58, 108, 253], vl=99, box=(12, 731), fs=17)
T.names(['x', "f'(x)", 'f(x)'])
T.xrow([143, 324, 506, 687], ['-\\infty', '-1', '0', '+\\infty'])
T.signs(['', '-', '||', '-', '||s', '+', ''], bar_dx=1.6)
T.values([(0, 132, '-1'), (2, 230, '-\\infty', -38), (2, 132, '+\\infty', 38), (4, 230, '3'), (6, 132, '1')])
T.save()
