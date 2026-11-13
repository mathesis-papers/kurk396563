# Corrected Stirling formulas and integer exponents

Haobo Ma — ChronoAI Pte Ltd, Singapore  
Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore

4 November 2026 · Revision 2 · CC BY 4.0

## Results

The note gives a normalized proof of the conjecture in OEIS A396563, FORMULA,
approved revision 15 (1 June 2026), and an integer-exponent extension. Its
Stirling-minor Schur evaluation is credited to Merca (2014, Theorem 2.1) and
Amdeberhan–Ekhad (2022, Theorem 2). The latter paper's subset weights and
second-kind alphabet receive explicit corrections and counterexamples.

For n,m >= 1, the normalized nested sum F(n,m;a), defined in the note, equals
s_((a-n)^m)(1,...,n+m) when a >= n; vanishes when -m < a < n; and equals
(-1)^(nm) s_((-a-m)^n)(1,...,n+m) / ((n+m)!)^(-a) when a <= -m.
For n=0 it is (m!)^a instead. The reciprocal family includes Kurkov's A132393
FORMULA conjecture of 24 May 2026. A second-kind moment determinant, the
previously known rational row generating functions, and the companion
recurrences and weighted sums have complete written deductions.

The coverage table identifies the established prior formulas, the proved
corollaries, the four corrected statements and the separate formulas outside
the note's scope. The bibliography provides scientific references.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively use a LaTeX installation with the packages listed in `note.tex`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in the TeX source; BibTeX is unnecessary.

## Exact comparisons

Python 3 with its standard library is sufficient:

```sh
python3 verify.py > reproduced-checks.json
```

Compare the resulting JSON with `checks.json`. The checker uses rational
arithmetic throughout. It compares seven expressions on 245 nonnegative
Stirling-minor parameter triples, 35 reciprocal-power cases, 49 empty-sum
cases, all 42 displayed A396563 array cells and 135 distinct-alphabet cases.
Further comparisons cover 336 integer-exponent chain cases, 175 mixed-sign
rational-alphabet cases, 195 rational row-series coefficients, 105 companion
recurrence pairs, 540 homogeneous weighted-row cases, and 225 coefficients
each for the corrected column e.g.f. and the shifted Riordan pair. Forty-six
of the integer-exponent cases cover the exceptional n=0 boundary.

The checker also compares the four explicit correction examples: subset
weights give 3 rather than 1; the second-kind alphabet gives 7 rather than
25; the column e.g.f. coefficient is 1/2 rather than 1; and the printed
Riordan pair gives 1 rather than 0 at row 1, column 0.

## Mathematical coverage

The following pinned declarations have the literal two OEIS nested identities:

- [KurkovStirlingMinorVandermondeSum.result](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean): B(n,k,m) equals the A396563 sum for all n,k >= 0, m >= 1.
- [KurkovNestedStirlingIdentity.result](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S1/Recurrence/Algebraic/KurkovNestedStirlingIdentity.lean): the A132393 prefactor times its nested sum equals c(n+m+1,m+1), for all n >= 0, m >= 1.

The corrected formulas, all-integer-exponent family, Schur interpretation,
moment determinant, generating functions and other corollaries have written
proofs in the note. The finite comparisons establish the stated finite ranges;
they are distinct from those universal arguments.

## Files and license

`note.tex` is the only main TeX source. The source archive also contains this
README, `metadata.json`, `verify.py` and the expected `checks.json`.

Copyright 2026 Haobo Ma and Wenlin Zhang. Licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0).
