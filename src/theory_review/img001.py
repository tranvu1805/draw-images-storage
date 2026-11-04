from bio_kit import *

# biến trở (variable resistor), small blue icon
BL = '#1d6fb4'
b = Board('img001', size=(66, 45), lw=2.2)
b.rect(15, 20, 50.5, 33.5, ec=BL)
b.line((6, 27.5), (15, 27.5), color=BL)
b.line((50.5, 27.5), (59, 27.5), color=BL)
b.arrow(32.5, 3, 32.5, 19.3, color=BL, head=4.5, width=1.8)
b.keep_canvas()
b.save()
