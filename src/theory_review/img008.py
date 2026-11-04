from bio_kit import *

# đèn sợi đốt (incandescent lamp), small blue icon
BL = '#1d6fb4'
b = Board('img008', size=(101, 44), lw=2.2)
c, r = (50, 22.5), 14
b.patch(Circle(c, r, fc='none', ec=BL, lw=b.pt(2.3)))
k = r * 0.7071
b.line((c[0] - k, c[1] - k), (c[0] + k, c[1] + k), color=BL, lw=2.3)
b.line((c[0] - k, c[1] + k), (c[0] + k, c[1] - k), color=BL, lw=2.3)
b.line((5, 22.5), (36, 22.5), color=BL, lw=1.9)
b.line((64, 22.5), (95, 22.5), color=BL, lw=1.9)
b.keep_canvas()
b.save()
