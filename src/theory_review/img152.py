from bio_kit import *
from matplotlib.patches import FancyBboxPatch  # noqa: F401

# Point mutations: template (3'->5'), coding (5'->3'), mRNA and polypeptide for the normal gene and 4 forms.
b = Board('img152', size=(1417, 840), lw=1.6, font=27)
PAIR = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
GENES = {
    'Gene bình thường': ('TACTTCAAACCGATT', 'ATGAAGTTTGGCTAA', 'AUGAAGUUUGGCUAA', ['Met', 'Lys', 'Phe', 'Gly'], 12),
    'Dạng 1': ('TACTTCAAGCCGATT', 'ATGAAGTTCGGCTAA', 'AUGAAGUUCGGCUAA', ['Met', 'Lys', 'Phe', 'Gly'], 12),
    'Dạng 2': ('TACATCAAACCGATT', 'ATGTAGTTTGGCTAA', 'AUGUAGUUUGGCUAA', ['Met'], 3),
    'Dạng 3': ('TACTTCAAACCCATT', 'ATGAAGTTTGGGTAA', 'AUGAAGUUUGGGUAA', ['Met', 'Lys', 'Phe', 'Gly'], 12),
    'Dạng 4': ('TACTTCAATCCGATT', 'ATGAAGTTAGGCTAA', 'AUGAAGUUAGGCUAA', ['Met', 'Lys', 'Leu', 'Gly'], 12),
}
for t, c, m, aa, stop in GENES.values():  # sanity: strands complementary, mRNA = coding with U
    assert ''.join(PAIR[x] for x in t) == c and c.replace('T', 'U') == m and m[stop:stop + 3] in ('UAA', 'UAG', 'UGA')

MRNA = '#cfcfcf'
BAR = '#4d4d4d'


def brace(x0, x1, y, h, lw=1.6):
    """Curly brace under [x0, x1] opening upwards, tip pointing down at y + h."""
    t = np.linspace(0, 0.5, 120)
    k = 60
    half = 1 / (1 + np.exp(-k * t)) + 1 / (1 + np.exp(-k * (t - 0.5)))
    ys = np.concatenate([half, half[::-1]]) - 0.5
    xs = np.concatenate([t, 1 - t[::-1]])
    b.ax.plot(x0 + xs * (x1 - x0), y + ys * h, color=INK, lw=b.pt(lw), zorder=3)


def gene(name, x0, y0, bw, bh, label_xy=None, font=27):
    t, c, m, aa, stop = GENES[name]
    rows = [(y0, t, "3′", "5′", 'white'), (y0 + bh + 7, c, "5′", "3′", 'white'),
            (y0 + 2 * bh + 18, m, "5′", "3′", MRNA)]
    for y, seq, left, right, fc in rows:
        for i, base in enumerate(seq):
            b.rect(x0 + i * bw, y, x0 + (i + 1) * bw, y + bh, fc=fc, lw=1.4)
            b.text(x0 + (i + 0.5) * bw, y + bh / 2 + 1, base, size=font)
        b.text(x0 - 7, y + bh / 2, left, ha='right', size=font - 1, weight='bold')
        b.text(x0 + len(seq) * bw + 7, y + bh / 2, right, ha='left', size=font - 1, weight='bold')
    ym = rows[2][0] + bh
    # polypeptide bar
    yb = ym + 16
    for j, a in enumerate(aa):
        xa = x0 + 3 * j * bw
        b.rect(xa, yb, xa + 3 * bw, yb + bh + 2, fc=BAR, ec='white', lw=1.0)
        b.text(xa + 1.5 * bw, yb + (bh + 2) / 2, a, size=font - 1, weight='bold', color='white')
    # stop codon
    xs0, xs1 = x0 + stop * bw + 2, x0 + (stop + 3) * bw - 2
    brace(xs0, xs1, ym + 4, 16)
    xc = (xs0 + xs1) / 2
    b.text(xc, ym + 38, 'Mã', size=font - 1, weight='bold')
    b.text(xc, ym + 64, 'kết thúc', size=font - 1, weight='bold')
    if label_xy:
        b.text(*label_xy, name, size=font + 3, weight='bold')
    return ym


gene('Gene bình thường', 432, 42, 46, 34)
b.text(232, 101, 'Gene bình thường', size=30, weight='bold')
# hollow arrow down
ax_, ay = 712, 240
b.patch(Polygon([(ax_ - 9, ay), (ax_ + 9, ay), (ax_ + 9, ay + 30), (ax_ + 20, ay + 30), (ax_, ay + 52),
                 (ax_ - 20, ay + 30), (ax_ - 9, ay + 30)], closed=True, fc='white', ec=INK, lw=b.pt(1.6),
                joinstyle='miter'))
gene('Dạng 1', 92, 318, 38, 32, label_xy=(377, 528))
gene('Dạng 2', 792, 318, 38, 32, label_xy=(1077, 528))
gene('Dạng 3', 92, 580, 38, 32, label_xy=(377, 790))
gene('Dạng 4', 792, 580, 38, 32, label_xy=(1077, 790))
b.save()
