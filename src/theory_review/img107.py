from bio_kit import *

# sucrose (Haworth): glucose C1 -O- fructose C2, alpha-1,2-glycoside; carbon numbering in blue
b = Board('img107', size=(272, 140), lw=1.1, font=15.5)
BLUE, RED = '#4a8fd0', '#e0262b'
TH = 3.4  # front (thick) ring bonds


def num(x, y, s):
    b.text(x, y, s, color=BLUE, size=10.5)


# --- glucose ring
C5, O5, C1, C2, C3, C4 = (43, 69), (82, 69), (107, 88), (82, 107), (42, 107), (17, 88)
b.line(C5, (76, 69))
b.text(82, 69, 'O')
b.line((88, 73), C1)
b.line(C1, C2, lw=TH, cap='round')
b.line(C2, C3, lw=TH, cap='round')
b.line(C3, C4, lw=TH, cap='round')
b.line(C4, C5)
b.line(C5, (43, 59)); b.text(61, 52, r'CH$_2$OH')
b.line(C5, (43, 74)); b.text(43, 80, 'H')
b.line((17, 79), (17, 99)); b.text(17, 72, 'H'); b.text(23, 109, 'OH')
b.line((42, 100), (42, 121)); b.text(52, 94, 'OH'); b.text(43, 128, 'H')
b.line((82, 98), (82, 120)); b.text(83, 92, 'H'); b.text(89, 127, 'OH')
b.line(C1, (107, 75)); b.text(108, 68, 'H')
num(43, 40, '6'); num(37, 64, '5'); num(10, 87, '4'); num(48, 115, '3'); num(88, 113, '2'); num(113, 85, '1')
# --- glycosidic oxygen
b.line(C1, (121, 97), color=RED)
b.text(127, 102, 'O', color=RED, size=17)
F2 = (143, 87)
b.line((133, 97), F2, color=RED)
# --- fructose ring
FO, F5, F4, F3 = (183, 73), (221, 87), (207, 109), (157, 109)
b.line(F2, (177, 75))
b.text(183, 73, 'O')
b.line((189, 75), F5)
b.line(F5, F4, lw=TH, cap='round')
b.line(F4, F3, lw=TH, cap='round')
b.line(F3, F2, lw=TH, cap='round')
b.line(F2, (143, 66)); b.text(164, 59, r'CH$_2$OH')
b.line((158, 102), (158, 121)); b.text(160, 96, 'H'); b.text(165, 129, 'OH')
b.line((207, 102), (207, 121)); b.text(195, 96, 'HO'); b.text(209, 128, 'H')
b.line((221, 79), (221, 98)); b.text(222, 72, 'H'); b.text(223, 102, r'CH$_2$OH', ha='left')
num(143, 47, '1'); num(137, 83, '2'); num(152, 114, '3'); num(215, 114, '4'); num(217, 81, '5'); num(229, 90, '6')
# --- label
b.text(189, 18, r'$\alpha$-1,2-glycoside')
b.arrow(141, 27, 120, 91, color=BLUE, lw=0.9, head=6, width=2.6)
b.save()
