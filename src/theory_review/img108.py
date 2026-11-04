# Flag of ASEAN: blue field, red disc with a white ring, ten yellow paddy stalks bound together.
from photo_kit import *

fig, ax = board('img108', 150, aspect=2 / 3)     # x 0..150, y 0..100
BLUE, RED, YEL = '#163a99', '#e0261d', '#f8d40f'
ax.add_patch(Rectangle((0, 0), 150, 100, fc=BLUE, ec='none'))
cx, cy, R = 75, 50, 32
ax.add_patch(Circle((cx, cy), R + 2.6, fc='white', ec='none'))
ax.add_patch(Circle((cx, cy), R, fc=RED, ec='none'))
t = np.linspace(-1, 1, 160)
H = 20
sp = 1.75 + 1.95 * np.abs(t) ** 1.6                 # local spacing of the stalks
for i in range(10):
    o = i - 4.5
    xc = cx + o * sp
    hw = 0.3 * sp
    pts = np.vstack([np.column_stack([xc - hw, cy + H * t]), np.column_stack([xc + hw, cy + H * t])[::-1]])
    ax.add_patch(Polygon(pts, fc=YEL, ec='none', zorder=3))
save(fig, 'img108')
