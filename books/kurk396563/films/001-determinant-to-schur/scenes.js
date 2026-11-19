'use strict';

SCENES.question = S => {
  const a = clamp(S.u / 0.8) * clamp((S.d - S.u) / 0.5);
  txt('KURK396563', W / 2, 180, {size: 28, fam: F.mono, w: 700, align: 'center', c: C.cyan, a, ls: 7});
  txt('x(x+1)(x+2)', W / 2, 330, {size: 72, fam: F.math, w: 700, align: 'center', c: C.white, a});
  txt('= x^3 + 3x^2 + 2x', W / 2, 430, {size: 48, fam: F.math, w: 600, align: 'center', c: C.now, a: at(S, 0, 0.5)});
  box(W / 2 - 200, 520, 400, 100, at(S, 1, 0.7), C.mag);
  txt('c(3,2) = 3', W / 2, 585, {size: 42, fam: F.mono, w: 800, align: 'center', c: C.white, a: at(S, 1, 0.7)});
};

SCENES.bridge = S => {
  const a = clamp(S.u / 0.5) * clamp((S.d - S.u) / 0.5);
  panel(90, 190, 760, 520, a, C.cyan, 'COEFFICIENT MATRIX');
  txt('c(n+m+i, n+j)', 470, 300, {size: 38, fam: F.math, w: 700, align: 'center', c: C.white, a});
  txt('triangular basis change', 470, 395, {size: 30, fam: F.disp, w: 600, align: 'center', c: C.now, a: at(S, 0, 0.6)});
  txt('1, 2, ..., N', 470, 500, {size: 46, fam: F.mono, w: 800, align: 'center', c: C.cyan, a: at(S, 0, 0.6)});
  panel(1030, 190, 800, 520, a, C.mag, 'RECTANGULAR SCHUR');
  txt('s_(k^m)(1,...,N)', 1430, 330, {size: 44, fam: F.math, w: 700, align: 'center', c: C.white, a: at(S, 1, 0.6)});
  for (let r = 0; r < 3; r++) for (let c = 0; c < 5; c++)
    box(1210 + c * 75, 420 + r * 75, 58, 58, at(S, 2, 0.6), r === 0 ? C.now : C.cyan);
  txt('legal box fillings', 1430, 665, {size: 28, fam: F.disp, w: 600, align: 'center', c: C.white, a: at(S, 2, 0.6)});
};

SCENES.vandermonde = S => {
  const a = clamp(S.u / 0.5) * clamp((S.d - S.u) / 0.5);
  panel(100, 180, 800, 550, a, C.cyan, 'SUBSET EXPANSION');
  const xs = [220, 350, 480, 610, 740];
  xs.forEach((x, i) => { dot(x, 360, 11, i === 1 || i === 3 ? C.now : C.dim, a); txt(String(i + 1), x, 425, {size: 26, fam: F.mono, align: 'center', c: C.white, a}); });
  txt('∏ (b-a)^2', 500, 560, {size: 48, fam: F.math, w: 700, align: 'center', c: C.now, a: at(S, 1, 0.6)});
  panel(1030, 180, 800, 550, a, C.mag, 'CHAIN COORDINATES');
  txt('a_t = n − j_t + t', 1430, 350, {size: 46, fam: F.math, w: 700, align: 'center', c: C.white, a: at(S, 2, 0.6)});
  txt('n ≥ j₁ ≥ ⋯ ≥ j_m ≥ 0', 1430, 490, {size: 38, fam: F.math, w: 600, align: 'center', c: C.cyan, a: at(S, 2, 0.6)});
  txt('Vandermonde square → nested sum', 1430, 635, {size: 28, fam: F.disp, w: 600, align: 'center', c: C.white, a: at(S, 2, 0.6)});
};

SCENES.correction = S => {
  const a = clamp(S.u / 0.5) * clamp((S.d - S.u) / 0.5);
  txt('n = m = k = 1', W / 2, 180, {size: 38, fam: F.mono, w: 700, align: 'center', c: C.cyan, a});
  box(250, 280, 500, 150, a, C.open); txt('zero-extended: 1', 500, 370, {size: 40, fam: F.mono, align: 'center', c: C.open, a});
  box(1170, 280, 500, 150, at(S, 1, 0.6), C.argued); txt('corrected: −1 + 2×2 = 3', 1420, 370, {size: 40, fam: F.mono, align: 'center', c: C.argued, a: at(S, 1, 0.6)});
  txt('S(4,2) = 7 ≠ 25', W / 2, 610, {size: 52, fam: F.math, w: 800, align: 'center', c: C.now, a: at(S, 2, 0.6)});
};

SCENES.reciprocal = S => {
  const a = clamp(S.u / 0.5) * clamp((S.d - S.u) / 0.5);
  panel(120, 190, 760, 500, a, C.cyan, 'INTEGER EXPONENTS');
  txt('n, m ≥ 1', 500, 260, {size: 28, fam: F.mono, align: 'center', c: C.cyan, a});
  txt('a ≥ n', 500, 330, {size: 42, fam: F.math, w: 700, align: 'center', c: C.white, a});
  txt('−m < a < n  →  0', 500, 455, {size: 40, fam: F.math, w: 700, align: 'center', c: C.now, a: at(S, 1, 0.6)});
  txt('a = −m − r', 500, 580, {size: 42, fam: F.math, w: 700, align: 'center', c: C.argued, a: at(S, 2, 0.6)});
  panel(1030, 190, 760, 500, a, C.mag, 'RECIPROCAL BRANCH');
  txt('x  ↦  x⁻¹', 1410, 330, {size: 52, fam: F.math, w: 800, align: 'center', c: C.white, a: at(S, 2, 0.6)});
  txt('(-1)^(nm)', 1410, 455, {size: 44, fam: F.math, w: 700, align: 'center', c: C.now, a: at(S, 2, 0.6)});
  txt('A132393', 1410, 590, {size: 44, fam: F.mono, w: 800, align: 'center', c: C.cyan, a: at(S, 3, 0.6)});
};

SCENES.close = S => {
  badgeQ(S, [[0, 'frozen Lean theorems', 'lean'], [1, 'one chain', 'argued']]);
  const a = clamp((S.u - 0.2) / 0.8) * clamp((S.d - S.u) / 0.7);
  txt('斯特林子式与整数指数', W/2, 320, {size: 62, fam:F.zh, w:800, align:'center', c:C.white, a});
  txt('Stirling minors and integer exponents', W/2, 415, {size: 42, fam:F.disp, w:700, align:'center', c:C.cyan, a});
  txt('Determinant → Schur → Vandermonde → reciprocals', W/2, 525, {size:30, fam:F.disp, align:'center', c:C.now, a});
  leanList(W/2, 650, a, {align:'center', size:23, gap:46});

};
