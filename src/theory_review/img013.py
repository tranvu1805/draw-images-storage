from graphs_kit import *

# growth of rice area, yield and output (1990 = 100%), 1990-2020; drawn in the original's pixel frame
fid = 'img013'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
P = lambda x, y: (x, H - y)
X = lambda yr: 57 + (yr - 1990) * 22.34
Yv = lambda v: H - (348 - v * 1.25)
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
ap = dict(arrowstyle='-|>,head_length=0.8,head_width=0.32', color=INK, lw=1.6, shrinkA=0, shrinkB=0,
          mutation_scale=10)
ax.annotate('', xy=P(752, 348), xytext=P(57, 348), arrowprops=ap)
ax.annotate('', xy=P(57, 8), xytext=P(57, 348), arrowprops=ap)
for v in range(0, 251, 50):
    ax.plot([X(1990) - 5, X(1990)], [Yv(v)] * 2, color=INK, lw=1.2)
    ax.text(X(1990) - 10, Yv(v), str(v), ha='right', va='center', fontsize=15, fontweight='bold')
for yr in years:
    ax.plot([X(yr)] * 2, [Yv(0), Yv(0) - 5], color=INK, lw=1.2)
    ax.text(X(yr), H - 378, str(yr), ha='center', va='center', fontsize=15, fontweight='bold')
ax.text(*P(37, 14), '%', ha='center', va='center', fontsize=14)
ax.text(*P(775, 336), 'Năm', ha='center', va='center', fontsize=14, style='italic', fontweight='bold')
series = [
    ('Diện tích', 's', [100, 112.0, 126.9, 121.3, 123.9, 129.5, 120.5],
     [(165, 225), (275, 206), (389, 215), (500, 213), (614, 206), (729, 223)]),
    ('Năng suất', '^', [100, 116.0, 133.4, 153.7, 167.9, 181.1, 184.6],
     [(208, 187), (275, 159), (389, 140), (500, 121), (614, 102), (729, 100)]),
    ('Sản lượng', 'o', [100, 129.8, 169.2, 186.4, 208.1, 234.5, 222.4],
     [(167, 162), (275, 118), (389, 98), (500, 75), (614, 40), (729, 54)]),
]
for name, mk, vals, pos in series:
    ax.plot([X(y) for y in years], [Yv(v) for v in vals], color='#222222', lw=1.4, marker=mk, ms=7.5,
            mfc='#222222', mec='#222222', zorder=3)
    for v, (px, py) in zip(vals[1:], pos):
        ax.text(*P(px, py), f'{v:.1f}'.replace('.', ','), ha='center', va='center', fontsize=14.5,
                bbox=dict(fc='white', ec='none', pad=0.6), zorder=4)
for (x0, name, mk) in [(104, 'Diện tích', 's'), (312, 'Năng suất', '^'), (531, 'Sản lượng', 'o')]:
    ax.plot([x0, x0 + 32], [H - 422] * 2, color='#222222', lw=1.4)
    ax.plot(x0 + 16, H - 422, marker=mk, ms=7.5, color='#222222')
    ax.text(x0 + 40, H - 422, name, ha='left', va='center', fontsize=15)
save(fig, fid)
