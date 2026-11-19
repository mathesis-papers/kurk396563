# Corrected formulas and integer exponents for Amdeberhan–Ekhad (2022): Kurkov's OEIS A396563 FORMULA conjecture, revision 15 (1 June 2026)

**Authors:** Haobo Ma, Wenlin Zhang

We extend the Stirling determinant formulas of Merca (2014) and Amdeberhan–Ekhad (2022), giving a corrected subset expansion and a normalized proof of Kurkov's OEIS A396563 FORMULA conjecture, approved revision 15 (1 June 2026). The minor equals s_(k^m)(1,2,...,n+m) for all n,k >= 0, m >= 1; allowing every integer exponent yields a vanishing interval and an entire reciprocal-power family, including Kurkov's A132393 FORMULA conjecture (24 May 2026). We recover the earlier rational row generating functions and give a second-kind moment determinant. We also correct the alphabet in their second-kind Schur evaluation. Companion recurrences and two generating-function normalizations are treated with explicit attribution and coverage.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [kurk396563](https://mathesis-omega-research.apps.chrono-ai.fun/papers/kurk396563?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Corrected formulas and integer exponents for Amdeberhan–Ekhad (2022): Kurkov's OEIS A396563 FORMULA conjecture, revision 15 (1 June 2026). Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/kurk396563?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |
| Corollary (s7) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/0eae8e045cb2ba958e2097dbac034f62f9c1dd7a/D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/kurk396563/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/kurk396563/kurk396563/zh/) · [Read in English](https://papers.trureturing.org/kurk396563/kurk396563/en/)

[Slides](https://papers.trureturing.org/kurk396563/kurk396563/slides/) ([sources](books/kurk396563/slides/)) · [Videos](https://papers.trureturing.org/kurk396563/kurk396563/films/) ([sources](books/kurk396563/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/kurk396563/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `s1-literal` | same | `D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result` |
| `s2` | variant | `D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result` |
| `s3` | variant | `D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result` |
| `s4` | variant | `D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result` |
| `s5` | variant | `D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result` |
| `s6` | same | `D5/S1/Recurrence/Algebraic/KurkovNestedStirlingIdentity.result` |
| `s7` | variant | `D5/S1/Recurrence/Algebraic/KurkovNestedStirlingIdentity.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/kurk396563/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
