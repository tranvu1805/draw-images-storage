from tabgeo_kit import *

T = Table('img088', hl=[2, 29, 65, 156], vl=44, fs=14, rule_x=(6, 445))
T.names(['x', "y'", 'y'])
T.xrow([77, 246, 435], ['-\\infty', '-2', '+\\infty'])
T.signs(['', '+', '||', '+', ''], bar_dx=1.6, bar_y=(34, 156))
T.values([(0, 138, '3', -10), (2, 81, '+\\infty', -24), (2, 140, '-\\infty', 28), (4, 81, '-3', -10)])
T.save()
