from graphs_kit import *

# bar chart: number of days by number of online bookings
fid = 'img072'
W, H = orig_size(fid)
fig, _ = canvas(fid)
_.remove()
ax = fig.add_axes([60 / W, 1 - 250 / H, (403 - 60) / W, (250 - 47) / H])
cats = ['[1;6)', '[6;11)', '[11;16)', '[16;21)', '[21;26)']
vals = [14, 30, 25, 18, 5]
xs = np.arange(5)
ax.bar(xs, vals, width=0.36, color=INK, zorder=3)
for x, v in zip(xs, vals):
    ax.text(x, v + 1.2, str(v), ha='center', va='bottom', fontsize=14, fontweight='bold')
ax.set_ylim(0, 35)
ax.set_xlim(-0.52, 4.45)
ax.set_yticks(range(0, 36, 5))
ax.set_yticklabels([str(v) for v in range(0, 36, 5)], fontsize=16)
ax.set_xticks(xs)
ax.set_xticklabels(cats, fontsize=14)
ax.tick_params(length=0, pad=5)
ax.yaxis.grid(True, color='#555555', lw=1.0, zorder=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_ylabel('Số ngày', fontsize=15, fontweight='bold', labelpad=6)
ax.set_xlabel('Số lượt đặt bàn', fontsize=15, fontweight='bold', labelpad=4)
ax.set_title('Số lượt khách đặt bàn trực tuyến', fontsize=15, fontweight='bold', pad=14)
save(fig, fid)
