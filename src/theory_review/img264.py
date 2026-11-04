from graphs_kit import *
setfs(13)

# y = x^3 - 3x + 1: CĐ (-1;3), CT (1;-1)
fig, ax = win('img264', (178, 167), (31, 25.8))
axes(ax, (-5.03, 4.97), (-3.02, 6.16), xname=None, yname=None, origin=None, lw=1.6, head=8)
xt(ax, [-4, -2, 2, 4], [''] * 4, size=3.5, lw=1.2)
yt(ax, [-2, 2, 4], [''] * 3, size=3.5, lw=1.2)
DOT = (0, (1, 1.5))
dash(ax, [(-1, 0), (-1, 3), (0, 3)], ls=DOT)
dash(ax, [(0, -1), (1, -1), (1, 0)], ls=DOT)
curve(ax, lambda x: x**3 - 3 * x + 1, -2.19, 2.29, lw=1.3)
for p in [(-1, 3), (0, 3), (-1, 0), (1, 0), (0, -1), (1, -1)]:
    ax.plot(*p, 'o', ms=4, color=INK, zorder=6)
for x in (-4, -2, 2, 4):
    T(ax, x, -0.6, f'${x}$')
for y in (4, 2, -2):
    T(ax, -0.25, y, f'${y}$', ha='right')
T(ax, 0.6, 5.8, '$y$', fs=14)
T(ax, 4.7, 0.6, '$x$', fs=14)
save(fig, 'img264')
