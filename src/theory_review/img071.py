from tabgeo_kit import *

RED, BLUE = '#e0201b', '#3a4fe0'
O = np.array([158, 179.0])
ex, ey, ez = np.array([-51, 35.0]), np.array([72, 2.0]), np.array([0, -58.0])   # unit vectors on screen
P = {'O': O, 'K': O + 2 * ez, 'N': O + ex + 2 * ey}
P['M'] = P['N'] + 2 * ez
G = Geo('img071', P, fs=16, lw=1.5)
G.vec(O, O + 2.2 * ex, lw=1.5, L=12, w=4.5, color='#333333')
G.vec(O, O + 2.6 * ey, lw=1.5, L=12, w=4.5, color='#333333')
G.vec(O, O + 2.65 * ez, lw=1.5, L=12, w=4.5, color='#333333')
for e in (ex, ey, ez):
    G.vec(O, O + e, lw=2.2, L=12, w=4.5, color=RED)
G.seg('K', 'M')
G.seg('M', 'N')
G.dash = (6, 4)
for a, b in (('O', 'N'), (O + ex, 'N'), (O + 2 * ey, 'N')):
    G.seg(a, b, dashed=True, color=BLUE, lw=1.6)
for k in 'KMN':
    G.dot(k, r=6)
G.text(150, 22, '$z$', fs=17, weight='bold')
G.text(343, 198, '$y$', fs=17)
G.text(37, 249, '$x$', fs=17)
G.text(144, 173, '$O$', fs=16)
G.text(166, 56, '$K$(0;0;2)', fs=14, ha='left')
G.text(259, 98, '$M$', fs=14, ha='left')
G.text(274, 233, '$N$(1;2;0)', fs=14)
G.save()
