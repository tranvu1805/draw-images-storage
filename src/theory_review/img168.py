from tabgeo_kit import *

T = Table('img168', hl=[3, 35, 73, 172], vl=68, fs=12.5, rule_x=(11, 499))
T.names(['x', "y'", 'y'])
T.xrow([91, 274, 466], ['-\\infty', '-2', '+\\infty'])
T.signs(['', '+', '||', '+', ''], bar_dx=2.2, gaps={1: 193, 3: 355})
T.values([(0, 152, '2', -4), (2, 88, '+\\infty', -22), (2, 153, '-\\infty', 27), (4, 86, '2')])
T.save()
