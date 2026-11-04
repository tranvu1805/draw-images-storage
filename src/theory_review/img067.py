from graphs_kit import *

# rectangular field; parabola from the two bottom corners with vertex at the middle of the top side;
# the region under the parabola is cross-hatched (grass)
fig, ax = win('img067', (0, 214), 1)
L, R, B, Tp = 5, 421, 6, 209
m = (L + R) / 2
f = lambda x: B + (Tp - B) * (1 - ((x - m) / (m - L))**2)
xs = np.linspace(L, R, 400)
from matplotlib.patches import Polygon
region = Polygon(np.c_[xs, [f(x) for x in xs]], closed=True, fc='none', ec='none', transform=ax.transData)
ax.add_patch(region)
for c in np.arange(-600, 900, 52):
    for s in (1, -1):
        ln, = ax.plot([c - 300, c + 300], [B - 300 * s, B + 300 * s], color='#86b4e3', lw=1.0)
        ln.set_clip_path(region)
curve(ax, f, L, R, lw=1.5, color='#33475b')
seg(ax, [(L, B), (R, B), (R, Tp), (L, Tp), (L, B)], lw=1.3, color='#333333')
save(fig, 'img067')
