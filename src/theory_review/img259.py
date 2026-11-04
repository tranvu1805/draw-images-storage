from tabgeo_kit import *

T = Table('img259', hl=[2, 52, 97], vl=59, fs=11.5, rule_x=(3, 580))
T.names(['x', "y'"], dy=[10, 2])
T.xrow([80, 194, 324, 437, 564], ['-\\infty', '-\\dfrac{1}{2}', '2', '3', '+\\infty'], dy=6)
T.signs(['', '+', '0', '-', '0', '+', '0', '+', ''], dy=0, gaps={1: 131, 3: 260, 5: 390, 7: 505})
T.save()
