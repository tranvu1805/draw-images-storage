from bio_kit import *

# điện trở nhiệt (thermistor), small blue icon
BL = '#1d6fb4'
b = Board('img002', size=(66, 46), lw=2.2)
b.rect(13.5, 13, 49.5, 27.5, ec=BL)
b.line((5, 20.5), (13.5, 20.5), color=BL)
b.line((49.5, 20.5), (57.5, 20.5), color=BL)
b.line((13.5, 30.5), (24, 30.5), (44.5, 9.5), color=BL)
b.keep_canvas()
b.save()
