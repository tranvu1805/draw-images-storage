from bio_kit import *

b = Board('img143', lw=2.6, font=19)
tips = {'A': (21, 30), 'B': (67, 30), 'C': (101, 30), 'D': (142, 30), 'E': (204, 30), 'F': (269, 30), 'G': (310, 30)}
AB, CD, ABCD = (44, 57), (119, 56), (78, 102)
FG, EFG, ROOT = (288, 56), (246, 101), (161, 137)
for path in [(tips['A'], AB, ABCD), (tips['B'], AB), (tips['C'], CD), (tips['D'], CD, ABCD, ROOT),
             (tips['E'], EFG), (tips['F'], FG), (tips['G'], FG, EFG, ROOT)]:
    b.line(*path, cap='round')
for n, (x, y) in tips.items():
    b.text(x + (1 if n in 'D' else 0), 15, n, weight='bold')
b.save()
