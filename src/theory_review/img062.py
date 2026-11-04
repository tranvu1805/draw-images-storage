from tabgeo_kit import *
from matplotlib.patches import Polygon

P = {'P': (63, 98), 'Q': (273, 240), 'O': (63, 240)}
P['A'] = (185, 98 + (185 - 63) * (240 - 98) / (273 - 63))
G = Geo('img062', P, fs=17, lw=1.4)
ax = G.ax
ax.add_patch(Polygon([P['P'], P['O'], P['Q']], closed=True, fc='#c8c8c8', ec='none', zorder=0))
G.seg('P', 'Q', lw=1.5)
ax.plot([63, 63], [22, 240], color=INK, lw=3.2, solid_capstyle='butt')     # the two banks
ax.plot([61.4, 307], [240, 240], color=INK, lw=3.2, solid_capstyle='butt')
for k in 'PAQ':
    G.dot(k, r=9)
G.lab('A', (55), d=17)
G.text(40, 132, 'Bờ', fs=15)
G.text(40, 155, 'dọc', fs=15)
G.text(164, 259, 'Bờ ngang', fs=15)
G.text(122, 187, 'Khu nuôi', fs=15, weight='bold', style='italic')
G.text(115, 210, 'cá riêng', fs=15, weight='bold', style='italic')
G.save()
