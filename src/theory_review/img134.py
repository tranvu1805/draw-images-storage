# Karyogram of a male with trisomy 21 (three copies of chromosome 21) - replaces a photo of a patient.
from photo_kit import *

fig, ax = board('img134', 100)            # y 0..110.5; 1 unit = 2 px
LEN = {1: 248, 2: 242, 3: 198, 4: 190, 5: 181, 6: 171, 7: 159, 8: 145, 9: 138, 10: 134, 11: 135, 12: 133, 13: 114,
       14: 107, 15: 102, 16: 90, 17: 83, 18: 80, 19: 59, 20: 64, 21: 47, 22: 51, 'X': 156, 'Y': 57}
CEN = {1: .48, 2: .39, 3: .46, 4: .27, 5: .27, 6: .36, 7: .38, 8: .31, 9: .33, 10: .3, 11: .39, 12: .27, 13: .15,
       14: .16, 15: .17, 16: .41, 17: .3, 18: .22, 19: .45, 20: .44, 21: .25, 22: .27, 'X': .39, 'Y': .2}
K = 0.104                                 # units per Mb
W = 3.0                                   # chromatid width
BODY, BAND = '#b9b9b9', '#4d4d4d'
rng = np.random.default_rng(21)


def chrom(x, ytop, key, color=BODY):
    L = LEN[key] * K
    c = CEN[key]
    ax.add_patch(FancyBboxPatch((x - W / 2, ytop - L), W, L, boxstyle=f'round,pad=0,rounding_size={W / 2 * 0.9}',
                                fc=color, ec='#333333', lw=0.5, zorder=3))
    for k in range(int(L / 4.5)):        # a few bands
        yb = ytop - L * rng.uniform(0.05, 0.95)
        ax.add_patch(Rectangle((x - W / 2 + 0.1, yb), W - 0.2, rng.uniform(0.35, 0.8), fc=BAND, ec='none',
                               alpha=0.75, zorder=4))
    yc = ytop - L * c
    for s in (-1, 1):                    # centromere notch
        ax.add_patch(Polygon([(x + s * (W / 2 + 0.2), yc + 0.9), (x + s * W * 0.18, yc), (x + s * (W / 2 + 0.2), yc - 0.9)],
                             fc='white', ec='none', zorder=5))


def pair(xc, ytop, key, n=2, lab=None, color=BODY, labcol=INK):
    xs = [xc + (k - (n - 1) / 2) * (W + 0.9) for k in range(n)]
    for k, x in enumerate(xs):
        chrom(x, ytop, key if not isinstance(key, tuple) else key[k], color)
    ybot = ytop - max(LEN[k_] for k_ in (key if isinstance(key, tuple) else (key,))) * K
    txt(ax, xc, ybot - 3.2, lab or str(key), size=8, color=labcol, zorder=6)
    return xs


rows = [[(1,), (2,), (3,), None, (4,), (5,)],
        [(6,), (7,), (8,), (9,), (10,), (11,), (12,)],
        [(13,), (14,), (15,), None, (16,), (17,), (18,)],
        [(19,), (20,), None, (21,), (22,), None, ('XY',)]]
tops, y = [], 109.5
for items in rows:
    tops.append(y)
    keys = [k for it in items if it for k in (('X', 'Y') if it[0] == 'XY' else it)]
    y -= max(LEN[k] for k in keys) * K + 8.2
rows = list(zip(tops, rows))
for ytop, items in rows:
    n = len(items)
    xs = np.linspace(8, 92, n)
    for x, it in zip(xs, items):
        if it is None:
            continue
        key = it[0]
        if key == 21:
            ax.add_patch(FancyBboxPatch((x - 7, ytop - LEN[21] * K - 6.6), 14, LEN[21] * K + 8.4,
                                        boxstyle='round,pad=0,rounding_size=1.5', fc='#fde3e1', ec='#d32f2f', lw=1.2,
                                        zorder=1))
            pair(x, ytop, 21, n=3, lab='21', labcol='#c62828')
        elif key == 'XY':
            pair(x, ytop, ('X', 'Y'), lab='XY')
        else:
            pair(x, ytop, key)
save(fig, 'img134')
