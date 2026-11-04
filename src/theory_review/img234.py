from graphs_kit import *
setfs(12)

# y = x + 1/(x - 1): TCĐ x = 1, TCX y = x, centre B(1;1); CĐ (0;-1), CT (2;3)
fig, ax = win('img234', (97, 182), 26.5)
axes(ax, (-3.47, 4.72), (-3.7, 6.19), xname=None, yname=None, origin=None, lw=1.0)
box = (-3.47, 4.72, -3.5, 5.94)
vline(ax, 1, -3.5, 5.94, lw=1.2)
curve(ax, lambda x: x, -3.47, 4.72, lw=1.0, box=box)
f = lambda x: x + 1 / (x - 1)
curve(ax, f, -3.47, 0.999, box=box, lw=1.4)
curve(ax, f, 1.001, 4.72, box=box, lw=1.4)
xt(ax, [-3, -2, -1, 1, 2, 3, 4], [''] * 7, size=2.5)
yt(ax, [-2, -1, 1, 2, 3, 4, 5], [''] * 7, size=2.5)
for x in (-3, -2, 1, 2, 3, 4):
    T(ax, x + (0.15 if x == 1 else 0), -0.55, f'${x}$')
T(ax, -1.0, 0.45, '$-1$')
T(ax, -0.25, 0.4, '$O$')
for y in (1, 2, 3, 4, 5):
    T(ax, -0.3, y, f'${y}$', ha='right')
for y in (-1, -2):
    T(ax, -0.2, y + (0.3 if y == -1 else -0.1), f'${y}$', ha='right')
T(ax, 5.05, 0.0, '$x$', fs=14)
T(ax, -0.15, 6.5, '$y$', fs=14)
T(ax, 0.6, 5.0, '$x=1$', rotation=90, fs=12)
T(ax, -2.95, -2.35, '$y=x$', rotation=45, fs=12)
save(fig, 'img234')
