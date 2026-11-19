# Why does a string of numbers become a clean determinant?

## A small question first

Expand

$$x(x+1)(x+2)\cdots(x+v-1).$$

Call the coefficient of $x^j$ the unsigned Stirling number of the first kind, $c(v,j)$. For example,

$$x(x+1)(x+2)=x^3+3x^2+2x,$$

so $c(3,2)=3$. The paper places these numbers in a square matrix:

$$
B(n,k,m)=\det\!\left[c(n+m+i,n+j)\right]_{1\le i,j\le k}.
$$

Here $n,k\ge0$ and $m\ge1$; a $0\times0$ determinant is $1$. Kurkov’s OEIS A396563 entry records a nested-sum conjecture for $m=2$, approved in the 1 June 2026 revision. Why should its alternating signs, factorials, and squared differences reproduce this determinant?

## The key observation: view the matrix as a coefficient table

The first step is not to expand the determinant. Each entry is a coefficient of one common polynomial multiplied by a lower-degree polynomial whose leading coefficient is $1$. Replacing those auxiliary polynomials by $1,z,z^2,\ldots$ is a triangular change of basis with determinant $1$, so the determinant stays the same.

The new matrix consists of elementary symmetric polynomials in the fixed alphabet $1,2,\ldots,N$, where $N=n+m$. The dual Jacobi–Trudi identity identifies it with the Schur polynomial of the rectangle $(k^m)$:

$$B(n,k,m)=s_{(k^m)}(1,2,\ldots,n+m).$$

Think of a rectangle of boxes. Fill each row weakly from left to right and strictly down each column, using numbers from $1$ to $N$. Multiply the entries in each legal filling and add all those products. That sum is the Schur polynomial. Positivity and integrality of the determinant now have a visible reason.

## Where does the Vandermonde square come from?

The alternating-determinant formula for a Schur polynomial lets us choose $m$ elements of $1,\ldots,N$. For a chosen subset $S$, the denominator contains every difference between a chosen and an unchosen number. Package those differences with

$$P'(a),\qquad P(z)=\prod_{r=1}^{N}(z-r).$$

Differences within $S$ occur in pairs, leaving

$$\prod_{a<b\in S}(b-a)^2,$$

which is the conspicuous square in the nested sum. Write the chosen elements increasingly as $a_t$ and set

$$a_t=n-j_t+t.$$

This is a bijection with chains $n\ge j_1\ge\cdots\ge j_m\ge0$. The bijection explains the signs, factorials, and powers simultaneously; it is an all-parameter change of variables, not a finite check.

## A correction visible in one line

For $n=m=k=1$, the determinant is $c(3,2)=3$. An earlier printed subset formula defined weights only on $\{1\}$; extending the missing weights by zero gives $1$. The alphabet must have $N=a+b$ elements. The corrected weights are $-1$ and $2$, so

$$-1+2\cdot2=3.$$

The same alphabet-size mistake appears in a second-kind Stirling formula. Its left side is $S(4,2)=7$, while the printed alphabet produces the Schur value $25$. The explicit witness $7\ne25$ tells us to correct the input alphabet, while keeping the result and its attribution clear.

## Let the exponent become negative

Replace $n+k$ in the normalized nested sum by an arbitrary integer $a$. For $n,m\ge1$, there are three regimes:

- if $a\ge n$, the value is a rectangular Schur polynomial of width $a-n$;
- if $-m<a<n$, two rows in the alternating determinant have the same exponent, so the value is $0$;
- if $a=-m-r$ with $r\ge0$, inverting all variables gives a Schur polynomial with $n$ rows and $r$ columns, together with $(-1)^{nm}$ and a divisor $(N!)^{m+r}$.

The boundary $n=0$ is different: the only subset is the full alphabet, so the value is $(m!)^a$ for every integer $a$. This is why the vanishing interval requires the hypothesis $n\ge1$.

At $a=-m-1$, restoring the prefactors gives Kurkov’s second nested-sum identity in OEIS A132393, dated 24 May 2026. The reciprocal substitution is concrete: each cross difference satisfies $x_s-x_t=-x_sx_t(x_s^{-1}-x_t^{-1})$, and there are $nm$ such differences.

## What else can we read from the same picture?

The filling model gives a simple lower bound. Filling row $t$ entirely with $t$ contributes $(m!)^k$, so $B(n,k,m)\ge(m!)^k$; if $n=0$, that filling is unique and equality holds. The subset expansion writes the $k$-sequence as a finite sum of geometric sequences, recovering earlier rational generating functions and a linear recurrence, which need not be minimal. A second change of basis writes the same $B$ as a moment determinant of second-kind Stirling numbers.

The paper also collects companion recurrences, weighted row sums, and exponential generating functions for A132393. Keep two kinds of evidence separate: the all-parameter algebra proves why an identity holds, while exact rational arithmetic checks only the finite ranges explicitly listed in `checks.json`.

## Formal scope and limitations

The frozen Lean source states and proves the original three-parameter A396563 nested identity and the reciprocal-power A132393 identity. It does not automatically cover the Schur interpretation, the all-integer extension, the corrected second-kind alphabet, or every companion formula. The [precise chapter](statements.md) records each relationship: exact matches retain Lean links; the other paper results remain sourced, unbadged statements with shared formalization requests. 

::: {.film src="001-determinant-to-schur"}
This film follows the same chain through the $n=m=k=1$ correction and one reciprocal substitution: determinant, Schur polynomial, then Vandermonde square.
:::
