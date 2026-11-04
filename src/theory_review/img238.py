from tabgeo_kit import *

T = Table('img238', hl=[3, 36, 74, 135], vl=79, fs=12.5, rule_x=(7, 594))
T.names(['t', "v'(t)", 'v(t)'])
T.xrow([171, 341, 505], ['0', '6', '10'])
for x0, x1 in ((79, 154), (525, 594)):  # outside the domain (0; 10)
    T.hatch(x0, x1, 36, 135, density='//////')
T.signs(['', '+', '0', '-', ''], gaps={1: 244, 3: 425})
T.values([(0, 117, '0', -3), (2, 87, '54'), (4, 117, '30', 3)])
T.save()
