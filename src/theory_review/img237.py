from tabgeo_kit import *

T = Table('img237', hl=[2, 29, 60, 130], vl=45.5, fs=11.5, rule_x=(5, 502))
T.names(['x', "y'", 'y'], dy=[0, 0, -11])
T.xrow([71, 275, 478], ['-\\infty', '1', '+\\infty'])
T.signs(['', '-', '||', '-', ''], bar_dx=1.6, gaps={1: 161, 3: 389})
T.values([(0, 71, '-1', -3), (2, 118, '-\\infty', -25), (2, 72, '+\\infty', 24), (4, 117, '-1', 5)])
T.save()
