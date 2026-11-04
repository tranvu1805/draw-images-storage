from tabgeo_kit import *

T = Table('img038', hl=[6, 58, 100], vl=65, box=(18, 395), fs=14)
T.names(['x', "y'"])
T.xrow([89, 183, 278, 371], ['-\\infty', '3', '7', '+\\infty'])
T.signs(['', '+', '0', '-', '0', '+', ''])
T.save()
