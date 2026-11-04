# Joule's apparatus: a falling mass turns a paddle wheel in an insulated tank of water; thermometer, scale.
from photo_kit import *

fig, ax = board('img100', 100)            # y 0..121.6
WALL, WATER, METAL = '#5f5f5f', '#d6e8f5', '#c9c9c9'
# insulated tank
ax.add_patch(Rectangle((6, 4), 62, 74, fc=WALL, ec='#333333', lw=1.0, zorder=1))
ax.add_patch(Rectangle((11, 9), 52, 64, fc=WATER, ec='#333333', lw=0.8, zorder=2))
ax.add_patch(Rectangle((4, 76), 66, 5, fc='#4a4a4a', ec='#333333', lw=1.0, zorder=3))      # lid
# axle + paddles
ax.add_patch(Rectangle((34.5, 11), 5, 96, fc=METAL, ec='#333333', lw=0.8, zorder=4))
for y in (15, 30, 45, 60):
    ax.add_patch(Rectangle((15, y), 44, 6, fc='#ececec', ec='#333333', lw=0.8, zorder=5))
    ax.add_patch(Rectangle((34.5, y), 5, 6, fc='#8a8a8a', ec='#333333', lw=0.6, zorder=6))
# spool with string wound on it
ax.add_patch(Rectangle((28, 86), 18, 3, fc='#9a9a9a', ec='#333333', lw=0.8, zorder=6))
ax.add_patch(Rectangle((28, 102), 18, 3, fc='#9a9a9a', ec='#333333', lw=0.8, zorder=6))
ax.add_patch(Rectangle((31, 89), 12, 13, fc='#6f6f6f', ec='#333333', lw=0.8, zorder=6))
for y in np.arange(90, 101.5, 1.6):
    ax.plot([31, 43], [y, y + 0.8], color='#2a2a2a', lw=0.8, zorder=7)
# string over the pulley to the hanging mass
px, py, pr = 76, 99, 4.5
ax.plot([43, px], [99 + pr, py + pr], color=INK, lw=1.0, zorder=7)
ax.add_patch(Circle((px, py), pr, fc='white', ec=INK, lw=1.6, zorder=8))
ax.add_patch(Circle((px, py), 1.2, fc=INK, zorder=9))
ax.plot([px + pr, px + pr], [py, 74], color=INK, lw=1.0, zorder=7)
ax.add_patch(Rectangle((px + pr - 4.5, 66), 9, 8, fc='#d9d9d9', ec=INK, lw=1.2, zorder=8))
ax.plot([px, 92], [py, py + 3], color='#555555', lw=1.0, zorder=6)                         # pulley bracket
# vertical scale
ax.plot([92, 92], [14, 108], color=INK, lw=2.4, zorder=6)
for y in range(20, 106, 17):
    ax.plot([88, 96], [y, y], color=INK, lw=1.4, zorder=6)
# thermometer through the lid
ax.add_patch(FancyBboxPatch((14.5, 44), 3, 64, boxstyle='round,pad=0,rounding_size=1.4', fc='white', ec=INK,
                            lw=1.0, zorder=9))
ax.plot([16, 16], [46, 74], color='#d32f2f', lw=1.4, zorder=10)
ax.add_patch(Circle((16, 45.5), 2.0, fc='#d32f2f', ec=INK, lw=0.8, zorder=10))
for y in range(80, 106, 3):
    ax.plot([14.5, 16], [y, y], color='#555555', lw=0.5, zorder=10)
save(fig, 'img100')
