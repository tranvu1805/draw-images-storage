from tabgeo_kit import *

T = Table('img068', hl=[8, 61, 92, 223], vl=69, box=(6, 524), fs=14)
T.names(['x', "y'", 'y'])
T.xrow([100, 231, 362, 493], ['-\\infty', '-2', '\\dfrac{1}{2}', '+\\infty'])
T.signs(['', '-', '0', '+', '0', '-', ''])
T.values([(0, 109, '2'), (2, 205, '1'), (4, 109, '6'), (6, 205, '2')])
T.save()
