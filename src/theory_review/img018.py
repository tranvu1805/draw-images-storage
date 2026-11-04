from graphs_kit import *
from matplotlib.ticker import MultipleLocator

# mass spectrum of ester X (base peak m/z 31, molecular ion m/z 60)
fid = 'img018'
W, H = orig_size(fid)
fig, _ = canvas(fid)
_.remove()
ax = fig.add_axes([86 / W, 1 - 266 / H, (581 - 86) / W, (266 - 8) / H])
peaks = {12: 0.6, 13: 1.0, 14: 1.9, 15: 19.0, 16: 0.6, 17: 0.5, 18: 1.2, 28: 5.0, 29: 45.3, 30: 5.8,
         31: 100.0, 32: 45.7, 43: 0.4, 44: 1.2, 45: 0.6, 59: 0.4, 60: 37.6, 61: 0.8}
for mz, v in peaks.items():
    ax.plot([mz, mz], [0, v], color=INK, lw=1.6, solid_capstyle='butt')
ax.set_xlim(10, 70)
ax.set_ylim(0, 100)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.tick_params(which='major', length=5, width=0.9, labelsize=15, direction='out')
ax.tick_params(which='minor', length=2.5, width=0.7, direction='out')
for s in ax.spines.values():
    s.set_linewidth(0.9)
ax.set_xlabel('$m/z$', fontsize=16, labelpad=0)
ax.set_ylabel('Cường độ tương đối (%)', fontsize=15, labelpad=3)
save(fig, fid)
