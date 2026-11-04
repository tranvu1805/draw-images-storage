# Rectangular cladogram of chordates with ancestral / derived traits and annotations.
from photo_kit import *

fig, ax = board('img145', 100)            # y 0..54.4
LW = 1.5
C = '#1f78c8'                             # tree lines
PUR, GRN, DOT = '#7b3fa0', '#22a845', '#d62828'
XE = 74                                   # where the tip lines end
taxa = [('Cá lưỡng tiêm\n(Ngoài nhóm)', 51.5), ('Cá mút đá', 44), ('Cá hồi', 37), ('Ếch', 30), ('Cá sấu', 23),
        ('Sư tử', 15.5)]
nx = [10, 22, 34, 45.5, 57]                # node x positions (root ... crocodile/lion)
y4 = (taxa[4][1] + taxa[5][1]) / 2
y3 = (taxa[3][1] + y4) / 2
y2 = (taxa[2][1] + y3) / 2
y1 = (taxa[1][1] + y2) / 2
y0 = (taxa[0][1] + y1) / 2
ny = [y0, y1, y2, y3, y4]
seg = lambda x0, y0_, x1, y1_: ax.plot([x0, x1], [y0_, y1_], color=C, lw=LW, solid_capstyle='projecting')
seg(3, y0, nx[0], y0)
children = [(taxa[0][1], y1), (taxa[1][1], y2), (taxa[2][1], y3), (taxa[3][1], y4), (taxa[4][1], taxa[5][1])]
for i, (ya, yb) in enumerate(children):
    seg(nx[i], ya, nx[i], yb)
    seg(nx[i], ya, XE, ya)                                    # upper child goes to a tip
    seg(nx[i], yb, nx[i + 1] if i < 4 else XE, yb)            # lower child: next node (or the lion tip)
for (s, y) in taxa:
    txt(ax, XE + 1.5, y, s, size=11, ha='left', va='center', linespacing=1.15)
ax.add_patch(Circle((3, y0), 0.8, fc=DOT, ec='none', zorder=5))
ax.add_patch(Circle((nx[1], y1), 0.8, fc=DOT, ec='none', zorder=5))


def mark(x, y, color, s, dy=1.6, size=10):
    ax.add_patch(Rectangle((x - 0.45, y - 1.6), 0.9, 3.2, fc=color, ec='none', zorder=5))
    if s:
        txt(ax, x, y + dy, s, size=size, va='bottom', linespacing=1.15, zorder=7,
            bbox=dict(fc='white', ec='none', pad=0.6))


mark(16, y1, PUR, 'Có\nxương\nsống')
mark(28, y2, PUR, 'Hàm\nbản\nlề')
mark(39.5, y3, PUR, None)
txt(ax, 40.3, y3 + 1.4, '4 chi', size=10, va='bottom', ha='left', zorder=7, bbox=dict(fc='white', ec='none', pad=0.6))
mark(51, y4, PUR, 'Màng\nối')
mark(65, taxa[5][1], GRN, None)
txt(ax, 64, taxa[5][1] + 1.8, 'Lông\nmao', size=10, va='bottom', linespacing=1.15, zorder=7, bbox=dict(fc='white', ec='none', pad=0.6))
# rotation symbol at the crocodile / lion node
ax.add_patch(Arc((nx[4], y4), 3.2, 5.0, theta1=110, theta2=250, color='#666666', lw=1.8, zorder=6))
# annotations
txt(ax, 8, 30.5, 'Điểm phân\nnhánh', size=10, va='top', linespacing=1.15)
ax.plot([11.5, nx[1] - 0.6], [30.6, y1 - 0.4], color=INK, lw=0.7)
txt(ax, 19, 19.5, 'Đặc điểm\ntổ tiên', size=10, va='top', linespacing=1.15)
ax.plot([24, 28], [19.5, y2 - 1.6], color=INK, lw=0.7)
ax.plot([24, 39.5], [18.5, y3 - 1.6], color=INK, lw=0.7)
txt(ax, 40, 9.5, 'Giữ nguyên\ngiá trị nếu\nthay đổi vị trí\nquanh trục', size=10, va='top', linespacing=1.15)
ax.plot([43.5, nx[4] - 1.8], [10.3, y4 - 1.5], color=INK, lw=0.7)
txt(ax, 65, 9.5, 'Đặc điểm\nphát sinh', size=10, va='top', linespacing=1.15)
ax.plot([65, 65], [9.6, taxa[5][1] - 1.7], color=INK, lw=0.7)
save(fig, 'img145')
