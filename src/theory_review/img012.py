from graphs_kit import *
from matplotlib.patches import Wedge

# labour structure by economic sector, 2010 and 2021 (%), laid out in the original's pixel frame
fid = 'img012'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
ax.set_aspect('equal')
P = lambda x, y: (x, H - y)
C = ['#8cc63f', '#fff59d', '#f4a7c9']  # state / non-state / foreign-invested
EC = dict(ec='#555555', lw=0.8)


def pie(cx, cy, vals, labels, pos):
    a = 90.0
    for v, c in zip(vals, C):
        da = 360 * v / sum(vals)
        ax.add_patch(Wedge(P(cx, cy), 145, a - da, a, fc=c, **EC))
        a -= da
    for s, (x, y) in zip(labels, pos):
        ax.text(*P(x, y), s, ha='center', va='center', fontsize=13 if s == '3,5' else 15)


pie(205, 155, [10.2, 86.3, 3.5], ['10,2', '86,3', '3,5'], [(232, 57), (205, 215), (191, 27)])
pie(540, 155, [8.1, 82.6, 9.3], ['8,1', '82,6', '9,3'], [(572, 45), (540, 215), (498, 57)])
ax.text(*P(205, 328), 'Năm 2010', ha='center', va='center', fontsize=17)
ax.text(*P(540, 328), 'Năm 2021', ha='center', va='center', fontsize=17)
for (y, text), c in zip([(103, 'Khu vực kinh tế\nNhà nước'), (177, 'Khu vực kinh tế\nngoài Nhà nước'),
                         (252, 'Khu vực kinh tế\ncó vốn đầu tư nước ngoài')], C):
    ax.add_patch(Wedge(P(733, y), 38, -38, 38, fc=c, **EC))
    ax.text(*P(786, y), text, ha='left', va='center', fontsize=14, linespacing=1.35)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
save(fig, fid)
