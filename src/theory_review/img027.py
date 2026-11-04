from tabgeo_kit import *

T = Table('img027', hl=[0, 32, 83, 191], vl=102, fs=15)
T.names(['x', "f'(x)", 'f(x)'], fs=21)
T.ax.texts[0].set_x(23)  # the original sets the x label flush left
T.xrow([138, 433, 701], ['-\\infty', '2', '+\\infty'])
T.signs(['', '+', '|', '+', ''])
T.values([(0, 174, '-1', -4), (2, 104, '+\\infty', -38), (2, 176, '-\\infty', 35), (4, 102, '-1', 3)])
T.save()
