from bio_kit import *

# quạt trần (ceiling fan), small blue icon: bow-tie with a centre dot
BL = '#1d6fb4'
b = Board('img010', size=(95, 46), lw=2.2)
b.line((13, 11), (83, 37), color=BL)
b.line((13, 37), (83, 11), color=BL)
b.line((13, 11), (13, 37), color=BL, cap='round')
b.line((83, 11), (83, 37), color=BL, cap='round')
b.patch(Circle((48, 24), 4.6, fc=BL, ec=BL, lw=0.3), z=4)
b.keep_canvas()
b.save()
