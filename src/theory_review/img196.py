from graphs_kit import *
setfs(18)

# y = f(x) below Ox on [-3;1], above on [1;2]; region between the curve and Ox on [-3;2] hatched.
# The original's x axis is not to scale (1 and 2 sit close together); positions follow the original.
fid = 'img196'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
Y = lambda y: H - y
xs = [25, 37, 60, 80, 100, 120, 140, 160, 180, 200, 215, 234, 250, 270, 290, 310, 325, 339, 350, 360, 367, 380, 386]
ys = [280, 256, 230, 215, 205, 198, 195, 196, 197, 198, 200, 199, 196, 190, 178, 160, 136, 106, 85, 64, 49, 14, 0]
ys = [Y(v) for v in ys]
m = np.gradient(ys, xs)
f = hermite(xs, ys, m)
X3, X1, X2, AX = 37, 339, 367, Y(106)
hatch(ax, region(f, X3, X2, lambda x: AX), 11, lw=0.8)
seg(ax, [(X3, AX), (X3, f(X3))], lw=1.4)
seg(ax, [(X2, AX), (X2, f(X2))], lw=1.4)
axes(ax, (0, 432), (Y(285), Y(3)), xy=(234, AX), xname=None, yname=None, origin=None, lw=1.3, head=8)
curve(ax, f, 25, 386, lw=2.0)
ax.plot(234, AX, 'o', ms=4.5, color=INK, zorder=6)
T(ax, 218, Y(12), '$y$')
T(ax, 418, Y(126), '$x$')
T(ax, 22, Y(93), '$-3$')
T(ax, 216, Y(92), '$O$')
T(ax, 318, Y(93), '$1$')
T(ax, 369, Y(122), '$2$')
save(fig, fid)
