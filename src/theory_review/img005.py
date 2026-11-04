from bio_kit import *

# diode ổn áp (Zener): bent cathode bar
b = Board('img005', size=(107, 52), lw=2.4, font=18)
b.line((6, 24.5), (96, 24.5))
b.patch(Polygon([(44, 13.5), (63, 24.5), (44, 35.5)], closed=True, fc=INK, ec=INK, lw=0.5, joinstyle='miter'))
b.line((54, 4), (63, 9.5), (63, 40), (73, 46))
b.text(25, 15, 'A', family='Arial')
b.text(81, 15, 'K', family='Arial')
b.keep_canvas()
b.save()
