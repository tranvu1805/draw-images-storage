from bio_kit import *

# diode thường (rectifier diode)
b = Board('img006', size=(118, 51), lw=2.3, font=18)
b.line((15, 28.5), (104, 28.5))
b.patch(Polygon([(52.5, 17.5), (73, 28.5), (52.5, 39.5)], closed=True, fc=INK, ec=INK, lw=0.5, joinstyle='miter'))
b.line((73, 17.5), (73, 40))
b.text(35, 18.5, 'A', family='Arial')
b.text(89.5, 18.5, 'K', family='Arial')
b.keep_canvas()
b.save()
