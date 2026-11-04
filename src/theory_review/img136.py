# Homologous organs: forelimb bones of human, whale and bat, colour-coded by bone type.
from photo_kit import *

fig, ax = board('img136', 100)            # y 0..54.5
HUM, RAD, ULN, CAR, MET, PHA = '#9b8fd1', '#f5a142', '#d9662b', '#f7d23e', '#5cb85c', '#3a8fd9'
z = [10]


def bone(p0, p1, w, color):
    z[0] += 1
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color='#4a4a4a', lw=w + 1.1, solid_capstyle='round', zorder=z[0])
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=w, solid_capstyle='round', zorder=z[0])


def digit(start, direction, lens, w_met, w_ph):
    """metacarpal then phalanges along a direction (deg, 0 = right, -90 = down)."""
    p = np.array(start, float)
    for k, L in enumerate(lens):
        a = np.radians(direction[k] if isinstance(direction, (list, tuple)) else direction)
        q = p + L * np.array([np.cos(a), np.sin(a)])
        bone(p, q, w_met if k == 0 else w_ph, MET if k == 0 else PHA)
        p = q + 0.25 * np.array([np.cos(a), np.sin(a)])
    return p


def carpals(cx, cy, n=6, r=0.75, dx=1.5):
    for i in range(n):
        x = cx + (i % 3 - 1) * dx
        y = cy + (0.8 if i < 3 else -0.8)
        ax.add_patch(Circle((x, y), r, fc=CAR, ec='#4a4a4a', lw=0.6, zorder=40))


# ---------------- human (vertical arm)
hx = 42
ax.add_patch(Polygon([(hx - 3.8, 53), (hx + 3.8, 53), (hx + 3.6, 36), (hx + 4.4, 22), (hx + 5.5, 18), (hx + 6.5, 7),
                      (hx - 5.8, 7), (hx - 6.2, 15), (hx - 4.2, 21), (hx - 3.6, 36)], fc='#f6dfd2', ec='#e0b8a8',
                     lw=0.8, zorder=1, joinstyle='round'))
bone((hx, 52), (hx, 37.5), 6.5, HUM)
bone((hx - 1.4, 35.5), (hx - 1.4, 22.5), 3.6, RAD)
bone((hx + 1.4, 35.5), (hx + 2.0, 22.5), 3.6, ULN)
carpals(hx + 0.3, 20.4)
for k, (x0, ang, lens) in enumerate([(-2.8, -118, [3.6, 2.4, 2.0]), (-1.3, -96, [4.6, 2.6, 1.8, 1.4]),
                                     (0.2, -90, [4.8, 2.8, 2.0, 1.4]), (1.6, -84, [4.5, 2.6, 1.8, 1.3]),
                                     (3.0, -72, [3.8, 2.2, 1.5, 1.2])]):
    digit((hx + x0, 18.6), ang, lens, 2.2, 1.9)
# ---------------- whale (paddle)
wx = 65
sv = np.linspace(0, 1, 120)
hw = 7.2 * sv ** 0.3 * (1 - sv) ** 0.75 * 1.5 + 2.6 * (1 - sv) ** 4
cxs = wx + 1.2 - 2.5 * sv ** 1.5
ys = 53 - 49 * sv
fl = np.vstack([np.column_stack([cxs - hw, ys]), np.column_stack([cxs + hw * 0.85, ys])[::-1]])
ax.add_patch(Polygon(fl, fc='#cfe6f5', ec='#8fb9d8', lw=0.9, zorder=1))
bone((wx + 2.2, 51.5), (wx + 1.2, 45), 7.5, HUM)
bone((wx + 2.6, 43.2), (wx + 2.2, 37.6), 4.6, RAD)
bone((wx - 0.4, 43.2), (wx - 0.6, 37.6), 4.6, ULN)
carpals(wx + 0.9, 35.2, r=0.85, dx=1.7)
for x0, ang, n in [(-2.2, -104, 4), (-0.6, -97, 7), (1.0, -93, 9), (2.6, -90, 6), (4.0, -84, 3)]:
    digit((wx + x0 + 0.2, 33), ang, [3.0] + [2.0] * n, 2.0, 1.7)
# ---------------- bat (wing)
bx = 88
bone((98.5, 52), (bx + 4, 40), 5.0, HUM)
bone((bx + 3.2, 38.6), (bx - 6.5, 28.6), 3.2, RAD)
bone((bx + 2.6, 37.4), (bx - 1.5, 33.8), 1.6, ULN)
carpals(bx - 7.6, 27.8, n=3, r=0.75, dx=1.3)
digit((bx - 9.0, 28.4), [140, 150], [2.0, 1.8], 1.6, 1.4)                          # thumb
tips = [digit((bx - 8.6, 27.0), [-112, -114, -117], [6.5, 4.8, 2.6], 1.8, 1.3),
        digit((bx - 7.4, 26.6), [-86, -88, -90], [9.0, 5.5, 3.5], 1.8, 1.3),
        digit((bx - 6.4, 26.6), [-62, -66, -70], [8.8, 5.2, 3.2], 1.8, 1.3),
        digit((bx - 5.4, 27.0), [-36, -40, -44], [8.8, 4.6, 2.6], 1.8, 1.3)]
wrist = np.array([bx - 7.6, 27.8])
mem = [(99.5, 47.5), (bx + 3.5, 39.5), tuple(wrist), tuple(tips[0])]
for a, b in zip(tips, tips[1:]):
    m = (a + b) / 2
    mem.append(tuple(m + (wrist - m) * 0.28))
    mem.append(tuple(b))
mem += [(99.5, tips[3][1] - 1.5)]
ax.add_patch(Polygon(mem, fc='#d5d5d5', ec='#9a9a9a', lw=0.8, zorder=1, joinstyle='round'))
# ---------------- labels
labels = [('Xương cánh', 46, (hx - 3.4, 46)), ('Xương quay', 39, (hx - 2.6, 32)), ('Xương trụ', 32, (hx + 1.6, 27)),
          ('Xương cổ bàn', 25, (hx - 1.4, 20.4)), ('Xương bàn', 18, (hx - 2.0, 16.5)), ('Xương ngón', 11,
                                                                                          (hx - 2.6, 10))]
for s, y, (px, py) in labels:
    txt(ax, 0.5, y, s, size=10.5, ha='left')
    ax.plot([21.5, px], [y, py], color=INK, lw=0.7, zorder=60)
for x, s in ((hx, 'Người'), (wx + 1, 'Cá voi'), (bx + 2, 'Dơi')):
    txt(ax, x, 2.2, s, size=11.5, weight='bold')
save(fig, 'img136')
