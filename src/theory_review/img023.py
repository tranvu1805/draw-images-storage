from graphs_kit import *
from matplotlib.patches import Wedge, Rectangle

# GDP structure by sector of a fictional country X, 2015 and 2020 (% GDP; each year sums to 100).
# Laid out in the original's pixel frame.
fid = 'img023'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
ax.set_aspect('equal')
P = lambda x, y: (x, H - y)
C = ['#24418f', '#e3232b', '#f4ab3c']  # agriculture / industry / services
R = 105


def pie(cx, cy, vals):
    a = 90.0
    for v, c in zip(vals, C):
        da = 360 * v / sum(vals)
        ax.add_patch(Wedge(P(cx, cy), R, a - da, a, fc=c, ec='white', lw=0.6))
        a -= da


def callout(text, inner, corner, end, label_xy):
    ax.plot(*zip(P(*inner), P(*corner), P(*end)), color=INK, lw=1.6, solid_capstyle='butt')
    ax.text(*P(*label_xy), text, ha='center', va='center', fontsize=15)


pie(236, 164.5, [18.17, 38.58, 43.25])
pie(679.5, 164.5, [14.70, 41.15, 44.15])
callout('18,17', (300, 112), (318, 80), (380, 80), (349, 66))
callout('38,58', (300, 222), (318, 255), (380, 255), (349, 241))
callout('43,25', (145, 128), (127, 95), (71, 95), (99, 81))
callout('14,70', (738, 98), (755, 71), (814, 71), (785, 57))
callout('41,15', (742, 222), (759, 255), (823, 255), (791, 241))
callout('44,15', (584, 170), (568, 136), (514, 136), (541, 122))
ax.text(*P(236, 28), 'Năm 2015', ha='center', va='center', fontsize=15)
ax.text(*P(686, 28), 'Năm 2020', ha='center', va='center', fontsize=15)
for x, c, s in [(44, C[0], 'Nông, lâm, ngư nghiệp'), (312, C[1], 'Công nghiệp, xây dựng'), (591, C[2], 'Dịch vụ')]:
    ax.add_patch(Rectangle(P(x, 300), 12, 12, fc=c, ec='none'))
    ax.text(*P(x + 19, 294), s, ha='left', va='center', fontsize=14.5)
ax.text(*P(930, 294), '(Đơn vị: % GDP)', ha='right', va='center', fontsize=14.5)
ax.text(*P(472, 330), 'Cơ cấu ngành kinh tế của quốc gia X năm 2015 và năm 2020', ha='center', va='center',
        fontsize=15.5, style='italic')
ax.set_xlim(0, W)
ax.set_ylim(0, H)
save(fig, fid)
