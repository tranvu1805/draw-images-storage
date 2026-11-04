from bio_kit import *

# quang điện trở (photoresistor), small blue icon
BL = '#1d6fb4'
b = Board('img003', size=(81, 64), lw=2.2)
b.patch(Circle((47.5, 39.5), 21.7, fc='none', ec=BL, lw=b.pt(2.2)))
b.rect(31, 34, 62.5, 45.5, ec=BL)
b.line((20, 40), (31, 40), color=BL)
b.line((62.5, 40), (70, 40), color=BL)
b.arrow(14.5, 16, 26.5, 26.5, color=BL, head=4, width=1.6)
b.arrow(19.5, 10.5, 32, 21.5, color=BL, head=4, width=1.6)
b.keep_canvas()
b.save()
