from graphs_kit import *
setfs(15)

# y = f'(x) = (x - 1)(x - 2)(x - 3): sign changes at 1, 2, 3; light unit grid lines as in the original
fig, ax = win('img170', (69, 193), 97)
for x in (1, 2, 3, 4):
    vline(ax, x, lw=1.6, color='#dcdcdc', zorder=0)
for y in (1, -1):
    hline(ax, y, lw=1.6, color='#dcdcdc', zorder=0)
axes(ax, (-0.71, 4.53), (-1.34, 1.97), xname=None, yname=None, origin=None, lw=1.3)
curve(ax, lambda x: (x - 1) * (x - 2) * (x - 3), 0.58, 3.53, lw=1.8)
for x in range(0, 5):
    T(ax, x + (0.12 if x == 0 else 0), -0.17, f'${x}$')
for y in (1, 0, -1):
    T(ax, -0.1, y + (0.12 if y == 0 else 0), f'${y}$', ha='right')
save(fig, 'img170')
