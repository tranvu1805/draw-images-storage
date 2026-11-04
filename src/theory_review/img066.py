from tabgeo_kit import *

G = Geo('img066', {}, fs=16, lw=1.7)
ax = G.ax
# Hình 1: the log (cylinder) and the cutting plane through a diameter of the base, 45 degrees
cx, ty, by, rx, ry, h = 74, 27, 100, 54, 25, 40
th = np.linspace(0, 2 * np.pi, 200)
G.path(np.c_[cx + rx * np.cos(th), ty + ry * np.sin(th)])                       # top face
t = np.linspace(0, np.pi, 100)
G.path(np.c_[cx + rx * np.cos(t), by + ry * np.sin(t)])                         # bottom, front half
G.path(np.c_[cx + rx * np.cos(t), by - ry * np.sin(t)], dashed=True)            # bottom, back half
G.seg((cx - rx, ty), (cx - rx, by))
G.seg((cx + rx, ty), (cx + rx, by))
G.seg((cx, ty + 1), (cx, by + ry), dashed=True)                                 # axis + diameter
s = np.linspace(0, np.pi / 2, 60)                                               # cut ellipse (z = x)
G.path(np.c_[cx + rx * np.cos(s), by + ry * np.sin(s) - h * np.cos(s)])          # front part, visible
G.path(np.c_[cx + rx * np.cos(s), by - ry * np.sin(s) - h * np.cos(s)], dashed=True)
G.seg((cx, by), (cx + rx, by - h), dashed=True)
G.text(cx, 160, 'Hình 1', fs=16)
# Hình 2: the wedge
P1, P2, T, Bf = (257, 44), (268, 114), (341, 42), (343, 78)
G.seg(P1, P2)
G.curve([P1, (290, 31), (320, 25), (335, 29), T, (343, 60), Bf, (340, 95), (326, 106), (300, 111), P2])
G.curve([P2, (300, 93), (324, 68), T])          # edge of the cut face
G.curve([P1, (300, 51), (330, 63), Bf], dashed=True)   # hidden part of the base arc
G.text(290, 155, 'Hình 2', fs=16)
G.save()
