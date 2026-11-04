from graphs_kit import *

# four cubic shapes (I)-(IV), drawn in the original's pixel frame
fid = 'img236'
W, H = orig_size(fid)
fig, ax = win(fid, (0, H), 1)
Y = lambda y: H - y
AX = dict(xname=None, yname=None, origin=None, lw=1.0, head=7)


def panel(ox, oy, x0, x1, name, nx, f, a, b):
    axes(ax, (x0, x1), (Y(166), Y(12)), xy=(ox, Y(oy)), **AX)
    T(ax, ox + 11, Y(26), '$y$', fs=10)
    T(ax, x1 - 7, Y(oy - 14), '$x$', fs=10)
    curve(ax, f, a, b, lw=1.3)
    T(ax, nx, Y(206), name, fs=12, fontweight='bold')


# (I) a > 0, two extrema
p1 = pchip([29, 33, 37, 41, 46, 52, 60, 66, 70, 74, 77, 80, 83, 87, 91],
           [Y(v) for v in [166, 122, 89, 70, 65, 70, 89, 104, 110.5, 113, 111, 103, 89, 58, 8]])
panel(74, 89, 15, 152, '(I)', 102, p1, 29, 91)
# (II) a < 0, two extrema (minimum on Ox)
p2 = pchip([195, 200, 205, 208, 211, 214, 217, 221, 227, 234, 240, 246, 250, 253, 258],
           [Y(v) for v in [10, 50, 85, 98, 105, 107.5, 104.5, 96, 84, 68, 62, 67, 84, 108, 166]])
panel(227, 108, 164, 318, '(II)', 265, p2, 195, 258)
# (III) a > 0, increasing (y = aX^3 + cX through O)
panel(394, 89, 335, 470, '(III)', 430, lambda x: Y(89) + 0.00556 * (x - 394)**3 + 0.9 * (x - 394), 372, 416)
# (IV) a < 0, horizontal inflection on Oy
panel(533, 115, 485, 618, '(IV)', 565, lambda x: Y(115) + 24 - 0.004885 * (x - 533)**3, 507, 558)
save(fig, fid)
