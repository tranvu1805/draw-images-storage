from bio_kit import *

# điện trở cố định (fixed resistor), small blue icon
BL = '#1d6fb4'
b = Board('img004', size=(73, 38), lw=2.2)
b.rect(18.75, 16, 55.25, 29.6, ec=BL)
b.line((10, 23), (18.75, 23), color=BL)
b.line((55.25, 23), (63.5, 23), color=BL)
b.keep_canvas()
b.save()
