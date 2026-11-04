from bio_kit import *
from matplotlib.patches import FancyBboxPatch

# đèn huỳnh quang (fluorescent lamp), small blue icon
BL = '#1d6fb4'
b = Board('img009', size=(101, 36), lw=2.2)
b.patch(FancyBboxPatch((25, 7.5), 49, 19, boxstyle='round,pad=0,rounding_size=9.5', fc='none', ec=BL,
                       lw=b.pt(2.2)))
b.line((7, 17), (25, 17), color=BL)
b.line((74, 17), (91, 17), color=BL)
b.line((40.5, 12.5), (58, 20.5), color=BL)
b.line((40.5, 24), (57.5, 12), color=BL)
b.keep_canvas()
b.save()
