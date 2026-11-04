from bio_kit import *
from matplotlib.patches import Arc

# phenol + nHCHO --(H+, t°)--> novolac repeat unit + nH2O
b = Board('img105', size=(495, 120), lw=1.1, font=15)
# phenol (the source drew the O-H bond without its label; OH restored)
V = b.ring((25, 68), 20, doubles=(5, 1, 3), off=3.2)
b.line(V[0], (25, 33), cap='round')
b.text(25, 25, 'OH')
b.text(77, 68, '+')
b.text(97, 68, 'nHCHO', ha='left')
b.arrow(172, 67, 251, 67, head=8, width=3, lw=1.1)
b.text(211, 46, r'H$^{+}$, t$^{\mathrm{o}}$')
# repeat unit
R = b.ring((306, 69), 20.5, doubles=(5, 1, 3), off=3.2)
b.line(R[0], (306, 36), cap='round')
b.text(310, 26, 'OH')
b.line(R[1], (266, R[1][1]), cap='butt')
b.line(R[5], (333, R[5][1]), cap='butt')
b.text(334, R[5][1], r'CH$_2$', ha='left')
b.line((361, R[5][1]), (396, R[5][1]), cap='butt')
for cx, t1, t2 in [(300, 125, 235), (354, -55, 55)]:
    b.patch(Arc((cx, 58), 54, 116, angle=0, theta1=t1, theta2=t2, color=INK, lw=b.pt(1.1)))
b.text(384, 90, 'n')
b.text(444, 63, '+')
b.text(456, 63, r'nH$_2$O', ha='left')
b.save()
