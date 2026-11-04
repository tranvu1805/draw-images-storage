from graphs_kit import *

# B (mT) against t (s): (0;0) -> (1;150) -> (3;150) -> (4;500) -> (5;0); dotted grid (figure number dropped)
fid = 'img101'
fig, ax = win(fid, (86.5, 403.5), (94.5, 0.677), size=(704, 440))
G = dict(color='#9a9a9a', lw=0.9, ls=(0, (1.2, 2.2)), zorder=0)
for t in range(1, 6):
    ax.plot([t, t], [0, 500], **G)
for b in (150, 300, 450, 500):
    ax.plot([0, 5], [b, b], **G)
ap = dict(arrowstyle='-|>,head_length=1.0,head_width=0.4', color=INK, lw=1.3, shrinkA=0, shrinkB=0,
          mutation_scale=10)
ax.annotate('', xy=(6.4, 0), xytext=(0, 0), arrowprops=ap)
ax.annotate('', xy=(0, 578), xytext=(0, 0), arrowprops=ap)
ax.plot([0, 1, 3, 4, 5], [0, 150, 150, 500, 0], color='#222222', lw=2.0, solid_joinstyle='miter')
for b in (150, 300, 450, 500):
    ax.text(-0.15, b, str(b), ha='right', va='center', fontsize=15)
for t in range(1, 6):
    ax.text(t, -14, str(t), ha='center', va='top', fontsize=15)
ax.text(-0.08, -14, '0', ha='right', va='top', fontsize=15)
ax.text(-0.12, 568, '$B$ (mT)', ha='right', va='center', fontsize=15)
ax.text(6.25, -22, '$t$ (s)', ha='center', va='top', fontsize=15)
save(fig, fid)
