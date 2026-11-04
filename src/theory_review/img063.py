# Three forces applied at one corner of a table: F1 and F2 in the table-top plane, F3 vertical.
from photo_kit import *

fig, ax = board('img063', 100)            # y 0..77.9
WOOD, WOOD2, WOOD3, EDGE = '#f6dc8f', '#e7c062', '#d9a845', '#7a5c1e'
A, B, C, D = map(np.array, ([8.0, 44.0], [64.0, 33.0], [96.0, 50.0], [40.0, 61.0]))
th = np.array([0, 3.5])
leg_h = 30
# legs (back-left hidden behind the apron)
for P, w, fc in ((C, 3.2, WOOD3), (A, 3.6, WOOD2), (B, 3.6, WOOD2)):
    x = P[0] - (0 if P is A else w)
    ax.add_patch(Rectangle((x, P[1] - leg_h), w, leg_h, fc=fc, ec=EDGE, lw=0.9, zorder=2 if P is C else 4))
# aprons
ax.add_patch(Polygon([A, B, B - th, A - th], fc=WOOD2, ec=EDGE, lw=0.9, zorder=5))
ax.add_patch(Polygon([B, C, C - th, B - th], fc=WOOD3, ec=EDGE, lw=0.9, zorder=5))
ax.add_patch(Polygon([A, B, C, D], fc=WOOD, ec=EDGE, lw=1.0, zorder=6))
# forces at corner A
F1 = A + 0.92 * (B - A)
F2 = A + np.array([10.0, 13.5])
F3 = A + np.array([0, 33])
for P, s, off in ((F1, '$\\overrightarrow{F_1}$', (-1.5, 4.5)), (F2, '$\\overrightarrow{F_2}$', (3.2, 2.8)),
                  (F3, '$\\overrightarrow{F_3}$', (-5, -3))):
    arr(ax, A[0], A[1], P[0], P[1], color='#c62828', lw=2.0, head=10, z=10)
    txt(ax, P[0] + off[0], P[1] + off[1], s, size=14, zorder=11)
ax.add_patch(Circle(A, 0.9, fc='#c62828', ec='none', zorder=11))
save(fig, 'img063')
