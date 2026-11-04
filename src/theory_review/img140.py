# Gene flow: individuals of two bird populations cross the mountain into the other population.
from photo_kit import *

fig, ax = board('img140', 100)            # y 0..47.7
RED2 = '#b3261e'
# mountain
mx = [24, 33, 38, 42, 44, 46, 48, 50, 53, 56, 59, 63, 70, 79]
my = [1, 8, 18, 30, 40, 44, 45.5, 43, 41, 33, 24, 14, 5, 1]
curve(ax, list(zip(mx, my)), color=INK, lw=1.3, z=1)
curve(ax, [(43.2, 35), (46, 34), (48, 36), (50.5, 33.5), (53, 35), (54.6, 37)], color=INK, lw=1.1, z=1)
# populations
for x, y in [(4, 12), (14, 12), (4, 3), (14, 3)]:
    bird(ax, x, y, 6, BLUE, facing=1)
for x, y in [(86, 12), (96, 12), (86, 3), (96, 3)]:
    bird(ax, x, y, 6, RED2, facing=-1)
# migrants: big birds leaving, small birds arriving on the other side
bird(ax, 10, 36, 12.5, BLUE, facing=1)
bird(ax, 90, 36, 12.5, RED2, facing=-1)
bird(ax, 76, 6, 6, BLUE, facing=-1)
bird(ax, 24, 6, 6, RED2, facing=1)
arr(ax, 8, 18.5, 10, 29, color=BLUE, lw=1.2, head=7)
arr(ax, 92, 18.5, 90, 29, color=RED2, lw=1.2, head=7)
arr(ax, 19, 39, 73, 11, color=BLUE, lw=2.2, head=11, z=6)
arr(ax, 81, 39, 27, 11, color=RED2, lw=2.2, head=11, z=6)
save(fig, 'img140')
