from tabgeo_kit import *

T = Table('img025', hl=[8, 45, 96], vl=125, box=(19, 823), fs=21)
T.names(['x', "f'(x)"])
T.xrow([180, 378, 575, 770], ['-2', '0', '1', '3'])
T.signs(['', '+', '||', '-', '0', '+', ''], bar_dx=2.5, bar_y=(53, 88))
T.save()
