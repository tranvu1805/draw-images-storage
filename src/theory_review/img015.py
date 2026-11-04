from bio_kit import *

# maltose: open-chain form (left) and cyclic form (right), perspective rings with wedge front bonds.
# The source image was cropped through C1 of the reducing unit in the cyclic form; that ring and its OH are completed.
b = Board('img015', size=(1000, 224), lw=1.6, font=19.5)
WW = 3.6  # half thickness of the front edge


def ring_unit(x0, c4='OH', c1=None):
    C4, C5, O, C1, C2, C3 = (x0, 91), (x0 + 44, 58), (x0 + 112, 58), (x0 + 159, 91), (x0 + 112, 124), (x0 + 45, 124)
    b.line(C4, C5, cap='round')
    b.line(C5, (O[0] - 8, 58))
    b.text(O[0], 60, 'O')
    b.line((O[0] + 8, 63), C1)
    b.wedge(C4, C3, w=WW)
    b.patch(Polygon([(C3[0], C3[1] - WW), (C2[0], C2[1] - WW), (C2[0], C2[1] + WW), (C3[0], C3[1] + WW)],
                    closed=True, fc=INK, ec=INK, lw=0.3))
    b.wedge(C1, C2, w=WW)
    # C6 (CH2OH)
    b.line(C5, (x0 + 44, 33), (x0 + 63, 21), cap='round')
    b.text(x0 + 66, 19, 'OH', ha='left')
    b.line(C3, (x0 + 45, 103)); b.text(x0 + 54, 92, 'OH')
    b.line(C2, (x0 + 112, 147)); b.text(x0 + 118, 156, 'OH')
    if c4 == 'OH':
        b.line(C4, (x0, 112)); b.text(x0 + 2, 125, 'OH')
    if c1 == 'OH':
        b.line(C1, (x0 + 186, 122)); b.text(x0 + 196, 132, 'OH')
    return C1


def glyco(C1):
    b.line(C1, (C1[0] + 31, C1[1] + 35))
    b.text(C1[0] + 38, C1[1] + 43, 'O')
    b.line((C1[0] + 45, C1[1] + 35), (C1[0] + 79, C1[1]))
    return C1[0] + 79


def open_unit(x0):
    C4, C5, C3, C2, C1 = (x0, 91), (x0 + 45, 57), (x0 + 45, 124), (x0 + 114, 124), (x0 + 162, 91)
    b.line(C4, C5, cap='round')
    b.line(C5, (x0 + 107, 57)); b.text(x0 + 110, 58, 'OH', ha='left')
    b.line(C5, (x0 + 45, 26), (x0 + 62, 15), cap='round'); b.text(x0 + 65, 13, 'OH', ha='left')
    b.wedge(C4, C3, w=WW)
    b.patch(Polygon([(C3[0], C3[1] - WW), (C2[0], C2[1] - WW), (C2[0], C2[1] + WW), (C3[0], C3[1] + WW)],
                    closed=True, fc=INK, ec=INK, lw=0.3))
    b.wedge(C1, C2, w=WW)
    b.line(C3, (x0 + 45, 103)); b.text(x0 + 54, 90, 'OH')
    b.line(C2, (x0 + 114, 148)); b.text(x0 + 120, 156, 'OH')
    b.bond(C1, (x0 + 193, 91), 2, off=4.2)
    b.text(x0 + 201, 92, 'O')


# open form
open_unit(glyco(ring_unit(10)))
b.text(200, 198, 'Dạng mở vòng của maltose', weight='bold', style='italic', size=22.5)
# cyclic form
ring_unit(glyco(ring_unit(543)), c4=None, c1='OH')
b.text(745, 198, 'Dạng mạch vòng của maltose', weight='bold', style='italic', size=22.5)
b.save()
