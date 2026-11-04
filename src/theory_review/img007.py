from bio_kit import *
from matplotlib.patches import Arc

# chuông điện (electric bell), small blue icon
BL = '#1d6fb4'
b = Board('img007', size=(89, 43), lw=2.2)
b.line((7, 28), (36, 28), (36, 19), color=BL)
b.line((49, 19), (49, 28), (78, 28), color=BL)
b.line((23.5, 19), (63.5, 19), color=BL)
b.patch(Arc((43.5, 19), 40, 19, theta1=180, theta2=360, ec=BL, lw=b.pt(2.2)))
b.keep_canvas()
b.save()
