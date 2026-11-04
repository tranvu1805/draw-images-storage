from graphs_kit import *

# F2 phenotype proportions (%) by plant height, with the bell curve through the bar tops
fid = 'img154'
W, H = orig_size(fid)
fig, _ = canvas(fid)
_.remove()
ax = fig.add_axes([51 / W, 1 - 166 / H, (355 - 51) / W, (166 - 50) / H])
hs = np.arange(100, 181, 10)
vals = [0.390625, 3.125, 10.9375, 21.875, 27.34375, 21.875, 10.9375, 3.125, 0.390625]
labels = ['0.390625', '3.125', '10.9375', '21.875', '27.34375', '21.875', '10.9375', '3.125', '0.390625']
ax.bar(hs, vals, width=4.2, color='#8c8c8c', edgecolor=INK, lw=0.8, zorder=2)
xs = np.linspace(97, 183, 400)
# smooth bell through the binomial(8, 1/2) tops (Gaussian with the same mean and variance)
g = lambda x: 27.34375 * np.exp(-((x - 140) / 10) ** 2 / 4)
ax.plot(xs, g(xs), color=INK, lw=0.9, zorder=3)
for h, v, s in zip(hs, vals, labels):
    ax.text(h, v + 1.0, s, ha='center', va='bottom', fontsize=8, fontweight='bold', zorder=4)
ax.set_xlim(95, 184)
ax.set_ylim(0, 30)
ax.set_yticks(range(0, 31, 5))
ax.set_xticks(hs)
ax.tick_params(labelsize=8.5, length=3, width=0.8, direction='out')
for t in ax.get_xticklabels() + ax.get_yticklabels():
    t.set_fontweight('bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for s in ('left', 'bottom'):
    ax.spines[s].set_linewidth(0.9)
ax.text(0.02, 1.03, 'Tỉ lệ %', transform=ax.transAxes, ha='left', va='bottom', fontsize=9, fontweight='bold')
ax.set_xlabel('Kiểu hình (cm)', fontsize=9, fontweight='bold', labelpad=6)
save(fig, fid)
