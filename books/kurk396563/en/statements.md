# Results, proofs and contribution opportunities

Write $c(v,j)$ for the unsigned first-kind Stirling number and $S(v,j)$ for the second-kind Stirling number. Thus

$$x(x+1)\cdots(x+v-1)=\sum_jc(v,j)x^j.$$

Empty determinants and products equal $1$. For $n,k\ge0$ and $m\ge1$, let $N=n+m$ and define

$$
\begin{gathered}
B(n,k,m)=\det M,\\
M_{ij}=c(n+m+i,n+j),\\
1\le i,j\le k.
\end{gathered}
$$

The following notation separates the factors of the nested sum so they remain readable. Let $\mathcal C(n,m)$ contain the chains $n\ge j_1\ge\cdots\ge j_m\ge0$, and put

$$H(n,m)=\prod_{t=1}^m(n+t-1)!,$$

$$\sigma(j)=\sum_tj_t,\qquad V(j)=\prod_{q<p}(j_q-j_p+p-q)^2,$$

$$U_t(j_t;a)=\frac{(n+t-1)_{\underline{j_t}}(n-j_t+t)^a}{(j_t+m-t)!},$$

$$W(j;a)=V(j)\prod_{t=1}^mU_t(j_t;a).$$

All power bases are positive, so every integer $a$ is permitted. The normalized sum is

$$F(n,m;a)=\frac{1}{H(n,m)}\sum_{j\in\mathcal C(n,m)}(-1)^{\sigma(j)}W(j;a).$$

Here $(u)_{\underline j}=u!/(u-j)!$. The precise proofs and original numbering are in the [public manuscript, version 2](https://github.com/mathesis-papers/kurk396563/blob/2132cfbb25c70bb023a452badd1a3c49b34dbaa2/manuscript/note.tex). The statements below retain that numbering; the separate nested-sum clause has a narrower Lean proof scope than the full first theorem.

::: {.remark #s1 title="A rectangular Schur polynomial"}
For $n,k\ge0$ and $m\ge1$,

$$B(n,k,m)=s_{(k^m)}(1,\ldots,n+m).$$

$$B(n,k,m)=F(n,m;n+k).$$

The same identity extends to $m=0$ by empty-product conventions. The rectangular partition $(k^m)$ has $m$ rows of length $k$.

Source: Theorem 1. The determinant-to-Schur clause is prior work of M. Merca (2014, Theorem 2.1) and T. Amdeberhan–S. B. Ekhad (2022, Theorem 2). The present paper gives the exact chain normalization and extends the exponent to all integers. The Schur clause and $m=0$ boundary have a [focused formalization request](https://github.com/the-omega-institute/trureturing-requests/issues/262).
:::

::: proof
Set $F_0(z)=z\prod_{a=1}^{N}(z+a)$ and $Q_{i-1}(z)=\prod_{a=N+1}^{N+i-1}(z+a)$. The matrix entry is $[z^{n+j}]F_0Q_{i-1}$. Replacing the monic polynomials $Q_0,\ldots,Q_{k-1}$ by $1,z,\ldots,z^{k-1}$ is a triangular basis change with determinant $1$. The resulting matrix has entries $e_{m+i-j}(1,\ldots,N)$; dual Jacobi–Trudi identifies its determinant with $s_{(k^m)}$.

Expanding the bialternant along the $m$ rectangular rows gives the subset formula. For $P(z)=\prod_{a=1}^{N}(z-a)$, its weights use $P'(a)=(-1)^{N-a}(a-1)!(N-a)!$. Each selected pair contributes the sign and squared difference in $V$. The bijection $a_t=n-j_t+t$ between increasing subsets and decreasing chains gives exactly $H$ and $U_t$, proving the displayed equality. At $m=0$, the original matrix is lower triangular with diagonal $1$ and the sum has its single empty term.
:::

::: {.theorem #s1-literal title="The nested-sum clause" mathesis="collected:kurk396563:2:s1" lean="D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result"}
For all natural $n,k$ and $m\ge1$,

$$B(n,k,m)=F(n,m;n+k).$$
:::

::: proof
With the definitions above expanded, this is the exact equality proved by the linked Lean declaration. Its statement does not include the Schur-polynomial clause or $m=0$.
:::

::: {.remark #s2 title="Corrected subset weights" mathesis="collected:kurk396563:2:s2"}
For $a\ge1$ and $b,r\ge0$, let $N=a+b$, $P(z)=\prod_{j=1}^N(z-j)$, and

$$\widetilde A_i=\frac{(-1)^{N-i}i^N}{N!}\binom Ni.$$

$$\widetilde A_i=\frac{i^{N-1}}{P'(i)}\quad(1\le i\le N).$$

Set $\beta_r(A,b)=\det[c(A+i,b+j)]_{1\le i,j\le r}$. The corrected formula is

$$\beta_r(a+b,b)=(-1)^{\binom a2}\sum_{1\le i_1<\cdots<i_a\le N}Z(i),$$

$$Z(i)=\prod_{u<v}(i_v-i_u)^2\prod_{t=1}^a\widetilde A_{i_t}i_t^{r-a+1}.$$

Source: Corollary 2. Each weight times $i^{r-a+1}$ equals $i^{b+r}/P'(i)$, so the same subset expansion proves the result. At $(a,b,r)=(1,1,1)$ the corrected value is $-1+2\cdot2=3$; zero-extending the printed weights gives $1$. [Contribute the remaining formal proof](https://github.com/the-omega-institute/trureturing-requests/issues/257).
:::

::: {.remark #s3 title="Every integer exponent" mathesis="collected:kurk396563:2:s3"}
For $n,m\ge1$, $N=n+m$ and integer $a$, there are three regimes.

For $a\ge n$,

$$F(n,m;a)=s_{((a-n)^m)}(1,\ldots,N).$$

For $-m<a<n$,

$$F(n,m;a)=0.$$

For $a=-m-r$ with $r\ge0$,

$$F(n,m;a)=\frac{(-1)^{nm}}{(N!)^{m+r}}\,s_{(r^n)}(1,\ldots,N).$$

The separate boundary is $F(0,m;a)=(m!)^a$ for every integer $a$.

Source: Corollary 3. [Contribute the integer-exponent extension](https://github.com/the-omega-institute/trureturing-requests/issues/258).
:::

::: proof
For distinct nonzero $x_1,\ldots,x_N$, the subset expression is the quotient of an alternant with row exponents $a+m-1,\ldots,a,n-1,\ldots,0$ by the ordinary Vandermonde. If $-m<a<n$, these exponent intervals overlap, so two rows coincide. The positive branch is the Schur alternant. For the negative branch, invert each variable in the $nm$ cross differences: the resulting sign is $(-1)^{nm}$. The complementary-rectangle identity then gives the factor $(N!)^{-(m+r)}$ and the rectangle $(r^n)$. If $n=0$, the full alphabet is the only subset, giving $(m!)^a$.
:::

::: {.remark #s4 title="A second-kind moment determinant" mathesis="collected:kurk396563:2:s4"}
For $n,k\ge0$, $m\ge1$ and $N=n+m$, let $A$ be the $m\times m$ matrix

$$A_{ij}=S(n+k+i+j+1,N).$$

The indices satisfy $0\le i,j<m$.

Then

$$B(n,k,m)=(-1)^{\binom m2}\det A.$$

Here $S(u,v)=0$ for $u<v$. Source: Corollary 4. This is distinct from the corrected second-kind alphabet discussed in the story. [Contribute the moment determinant proof](https://github.com/the-omega-institute/trureturing-requests/issues/263).
:::

::: proof
For $P(z)=\prod_{t=1}^N(z-t)$, put $M_\ell=\sum_{t=1}^Nt^\ell/P'(t)$. Partial fractions give

$$\sum_{\ell\ge0}M_\ell z^\ell=\frac{z^{N-1}}{\prod_{t=1}^N(1-tz)}.$$

Thus $M_\ell=S(\ell+1,N)$, including the zero range. Cauchy–Binet expands $\det[M_{n+k+i+j}]$ as the squared-Vandermonde subset sum. Comparing it with the first-kind subset formula supplies exactly $(-1)^{\binom m2}$.
:::

::: {.remark #s5 title="Rational generating functions and a recurrence" mathesis="collected:kurk396563:2:s5"}
Fix $n\ge0,m\ge1$. For each $m$-subset $S$ of $\{1,\ldots,N\}$, put

$$\lambda_S=\prod_{s\in S}s,\qquad D_S=\prod_{s\in S,t\notin S}(s-t).$$

As a formal power series,

$$\sum_{k\ge0}B(n,k,m)z^k=\sum_{|S|=m}\frac{\lambda_S^n}{D_S(1-\lambda_Sz)}.$$

The sequence is annihilated by $\prod_{|S|=m}(E-\lambda_S)$, where $E$ shifts $k$ to $k+1$. Repeated subset products are allowed; the resulting order need not be minimal.

Source: Corollary 5, recovering the earlier denominator in Amdeberhan–Ekhad, Theorem 1. Sum a geometric series for each subset; each corresponding shift factor annihilates its exponential sequence. [Contribute this consequence](https://github.com/the-omega-institute/trureturing-requests/issues/260).
:::

::: {.theorem #s6 title="Kurkov's reciprocal identity in A132393" mathesis="collected:kurk396563:2:s6" lean="D5/S1/Recurrence/Algebraic/KurkovNestedStirlingIdentity.result"}
For $n\ge0,m\ge1$, define

$$R=(-1)^{nm}HF.$$

Here $R=R(n,m)$, $H=H(n,m)$, and $F=F(n,m;-m-1)$.

$$Q(n,m)=\prod_{t=1}^m(n+t)^t.$$

Then

$$c(N+1,m+1)=N!\,Q(n,m)R(n,m).$$
:::

::: proof
This is source Corollary 6 and Kurkov's 24 May 2026 FORMULA conjecture. Expanding $F$ gives the exact signed reciprocal chain sum in the linked Lean source. In the written proof, variable inversion gives $R=H e_n(1,\ldots,N)/(N!)^{m+1}$; the elementary-symmetric expression equals $c(N+1,m+1)$ and $QH=(N!)^m$. These two identities give the displayed result, including $n=0$.
:::

::: {.remark #s7 title="Classical companion identities" mathesis="collected:kurk396563:2:s7"}
For $v\ge k\ge1$,

$$c(v,k)=e_{v-k}(1,\ldots,v-1),$$

$$\sum_{v\ge k}c(v,k)\frac{t^v}{v!}=\frac{(-\log(1-t))^k}{k!}.$$

For $v\ge0$, as a polynomial identity in $b,x$,

$$\sum_{k=0}^vc(v,k)b^kx^{v-k}=\prod_{j=0}^{v-1}(b+jx).$$

For $v>k\ge1$,

Define

$$L_1(v,k)=\sum_{j=2}^{v-k+1}\binom{-k}{j}(-1)^j\!c(v,k+j-1).$$

Then $(v-k)c(v,k)=L_1(v,k)$. Similarly, define

$$L_2(v,k)=\sum_{j=2}^{v-k+1}(j-2)!\binom vj c(v-j+1,k).$$

Then $(v-k)c(v,k)=L_2(v,k)$.

For $v\ge1$, with $H_v=\sum_{j=1}^v1/j$,

$$\sum_kkc(v,k)=v!H_v,$$

$$\sum_k(k\mathbin{\pm}1)c(v,k)=v!(H_v\mathbin{\pm}1),$$

$$\sum_kkc(v,v-k)=v!(v-H_v).$$

Source: Corollary 7. The row polynomial proves the elementary formula and the weighted evaluations. Comparing coefficients in $\sum_vR_v(x)t^v/v!=(1-t)^{-x}$, where $R_v(x)=\prod_{j=0}^{v-1}(x+j)$, gives the column exponential generating function. The two recurrence proofs compare coefficients in $xR_v(x+1)=(x+v)R_v(x)$ and in $(t+(1-t)\log(1-t))G'_k$, with $G_k=(-\log(1-t))^k/k!$. Evaluating $R_v(1)$ and $R'_v(1)$ gives the harmonic sums.

These are attributed earlier identities: the manuscript cites Lang and Deléham's OEIS formulas, the Quaintance–Gould notes attributing the row recurrence to Hagen, Petrov's 2025 column proof, ploosu2's 2025 proofs and K. Lee's 2026 combinatorial proofs. [Contribute the remaining formal statements](https://github.com/the-omega-institute/trureturing-requests/issues/261).
:::

## Additional correction and evidence

The unnumbered second-kind correction in §2 is

$$\det[S(A+i,b+j)]_{i,j=1}^r=s_{((A-b)^r)}(1,\ldots,b+r).$$

Its hypotheses are $A\ge b\ge0,r\ge1$. It has its [own contribution request](https://github.com/the-omega-institute/trureturing-requests/issues/259), separate from the moment determinant above. The witness is $S(4,2)=7$, while the printed alphabet gives $s_{(2)}(1,2,3)=25$.

The two linked Lean declarations prove the literal nested identities. The Schur evaluation, integer extension, moment determinant, corrections and companion results retain their written proofs and focused contribution links. Finite exact-arithmetic checks support their stated parameter ranges; they do not replace the universal proofs.

Prior sources: [Merca, Theorems 2.1–2.2](https://doi.org/10.1007/s10998-014-0034-3); [Amdeberhan–Ekhad, Theorems 1–3](https://arxiv.org/abs/2206.13244v1); [Tamvakis on Schur polynomials](https://doi.org/10.4171/LEM/58-1-7); [A396563](https://oeis.org/A396563/internal); [A132393](https://oeis.org/A132393/internal).
