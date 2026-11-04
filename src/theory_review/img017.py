from bio_kit import *

# resin identification code 03 (PVC): three chasing arrows around a rounded triangle
b = Board('img017', size=(146, 143), lw=1, font=30)
W = 10.0  # band width


def rounded_path(verts, radii, n=40):
    """Closed polyline through `verts` with filleted corners (start = middle of the last edge)."""
    pts = []
    m = len(verts)
    for i in range(m):
        P, V, N = (np.asarray(verts[(i + k) % m], float) for k in (-1, 0, 1))
        a, c = (P - V) / np.hypot(*(P - V)), (N - V) / np.hypot(*(N - V))
        th = np.arccos(np.clip(a @ c, -1, 1))
        r = radii[i]
        d = r / np.tan(th / 2)
        bis = (a + c) / np.hypot(*(a + c))
        C = V + bis * r / np.sin(th / 2)
        t0, t1 = V + a * d, V + c * d
        ang0, ang1 = np.arctan2(*(t0 - C)[::-1]), np.arctan2(*(t1 - C)[::-1])
        da = (ang1 - ang0 + np.pi) % (2 * np.pi) - np.pi
        for s in np.linspace(0, 1, n):
            pts.append(C + r * np.array([np.cos(ang0 + da * s), np.sin(ang0 + da * s)]))
    pts.append(pts[0])
    pts = np.array(pts)  # resample densely so straight edges have points too
    d = np.concatenate([[0], np.cumsum(np.hypot(*np.diff(pts, axis=0).T))])
    t = np.arange(0, d[-1], 0.5)
    return np.column_stack([np.interp(t, d, pts[:, 0]), np.interp(t, d, pts[:, 1])])


# centre line of the band: corners BL, top, BR; path starts on the bottom edge and runs left (clockwise on screen)
path = rounded_path([(23, 99), (77.5, -10), (132, 99)], [12, 12, 12])
start = np.argmin(np.where(path[:, 1] > 95, np.abs(path[:, 0] - 70), 1e9))
path = np.vstack([path[start:-1], path[:start + 1]])
seg = np.hypot(*np.diff(path, axis=0).T)
s = np.concatenate([[0], np.cumsum(seg)])


def at(si):
    i = np.clip(np.searchsorted(s, si) - 1, 0, len(seg) - 1)
    f = (si - s[i]) / seg[i]
    p = path[i] + f * (path[i + 1] - path[i])
    u = (path[i + 1] - path[i]) / seg[i]
    return p, u


def s_near(pt):
    return s[np.argmin(np.hypot(*(path - np.asarray(pt)).T))]


tails = [0.0, s_near((50, 45)), s_near((108, 56)), s[-1]]
HL, HW = 19, 11.5  # head length, half width
for k in range(3):
    s0, tip = tails[k], tails[k + 1] - 2.5
    base = tip - HL
    sel = (s > s0) & (s < base)
    p0, _ = at(s0)
    pb, ub = at(base)
    shaft = np.vstack([p0, path[sel], pb])
    b.ax.plot(shaft[:, 0], shaft[:, 1], color=INK, lw=b.pt(W), solid_capstyle='butt', solid_joinstyle='round',
              zorder=3)
    pt, _ = at(tip)
    nb = np.array([-ub[1], ub[0]])
    b.patch(Polygon([pb + nb * HW, pt, pb - nb * HW], closed=True, fc=INK, ec=INK, lw=0.3, joinstyle='miter'))
b.text(82, 69, '03', family='Arial', weight='bold', size=30)
b.text(84, 127, 'PVC', family='Arial', weight='bold', size=31)
b.keep_canvas()
b.save()
