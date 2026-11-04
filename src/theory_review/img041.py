from tabgeo_kit import *

# The source table had f increasing from 3 up to 1 on (0;+inf); fixed to a minimum f(0) = -3.

T = Table('img041', hl=[7, 58, 108, 253], vl=99, box=(12, 731), fs=17)
T.names(['x', "f'(x)", 'f(x)'])
T.xrow([143, 324, 506, 687], ['-\\infty', '-1', '0', '+\\infty'])
T.signs(['', '-', '||', '-', '0', '+', ''], bar_dx=1.6)
T.values([(0, 132, '-1'), (2, 230, '-\\infty', -38), (2, 132, '+\\infty', 38), (4, 230, '-3'), (6, 132, '1')])
T.save()
