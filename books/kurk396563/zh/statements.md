# 精确结果、证明与参与方向

记 $c(v,j)$ 为无符号第一类斯特林数，$S(v,j)$ 为第二类斯特林数。因此

$$x(x+1)\cdots(x+v-1)=\sum_jc(v,j)x^j.$$

空行列式与空乘积都取 $1$。对 $n,k\ge0,m\ge1$，令 $N=n+m$，并定义

$$
\begin{gathered}
B(n,k,m)=\det M,\\
M_{ij}=c(n+m+i,n+j),\\
1\le i,j\le k.
\end{gathered}
$$

为使嵌套和易于阅读，先分别定义它的因子。令 $\mathcal C(n,m)$ 为所有满足 $n\ge j_1\ge\cdots\ge j_m\ge0$ 的链，并置

$$H(n,m)=\prod_{t=1}^m(n+t-1)!,$$

$$\sigma(j)=\sum_tj_t,\qquad V(j)=\prod_{q<p}(j_q-j_p+p-q)^2,$$

$$U_t(j_t;a)=\frac{(n+t-1)_{\underline{j_t}}(n-j_t+t)^a}{(j_t+m-t)!},$$

$$W(j;a)=V(j)\prod_{t=1}^mU_t(j_t;a).$$

幂的底数都是正数，所以整数指数 $a$ 可以为负。归一化嵌套和为

$$F(n,m;a)=\frac{1}{H(n,m)}\sum_{j\in\mathcal C(n,m)}(-1)^{\sigma(j)}W(j;a).$$

这里 $(u)_{\underline j}=u!/(u-j)!$。[公开论文第 2 版](https://github.com/mathesis-papers/kurk396563/blob/2132cfbb25c70bb023a452badd1a3c49b34dbaa2/manuscript/note.tex)包含完整证明与原文编号。下面保留原文编号；首条定理的完整表述比它单独的嵌套和等式具有更广的数学范围。

::: {.remark #s1 title="矩形舒尔多项式"}
对 $n,k\ge0,m\ge1$，

$$B(n,k,m)=s_{(k^m)}(1,\ldots,n+m).$$

$$B(n,k,m)=F(n,m;n+k).$$

按空乘积约定，同一等式也延伸到 $m=0$。分拆 $(k^m)$ 是具有 $m$ 行、每行 $k$ 格的矩形。

来源：原文定理 1。行列式到舒尔多项式的等式是 M. Merca（2014，定理 2.1）和 T. Amdeberhan–S. B. Ekhad（2022，定理 2）的既有结果。本文给出逐项链和的精确归一化，并把指数推广到所有整数。舒尔等式与 $m=0$ 边界有[单独的形式化任务](https://github.com/the-omega-institute/trureturing-requests/issues/262)。
:::

::: proof
令 $F_0(z)=z\prod_{a=1}^{N}(z+a)$、$Q_{i-1}(z)=\prod_{a=N+1}^{N+i-1}(z+a)$。矩阵元素是 $[z^{n+j}]F_0Q_{i-1}$。把首一多项式 $Q_0,\ldots,Q_{k-1}$ 换成 $1,z,\ldots,z^{k-1}$，是行列式为 $1$ 的三角换基。所得矩阵的元素是 $e_{m+i-j}(1,\ldots,N)$；对偶 Jacobi–Trudi 恒等式把其行列式识别为 $s_{(k^m)}$。

沿双交替式的 $m$ 个矩形行展开，得到子集公式。令 $P(z)=\prod_{a=1}^N(z-a)$，权重中的导数是 $P'(a)=(-1)^{N-a}(a-1)!(N-a)!$。每对选中的元素贡献 $V$ 中的符号与平方差。换元 $a_t=n-j_t+t$ 是升序子集与下降链之间的双射，准确产生 $H$ 与 $U_t$，从而得到等式。$m=0$ 时，原矩阵是对角元为 $1$ 的下三角矩阵；嵌套和只有一个空项。
:::

::: {.theorem #s1-literal title="嵌套和等式" mathesis="collected:kurk396563:2:s1" lean="D5/S3/Combinatorics/BinomialBases/KurkovStirlingMinorVandermondeSum.result"}
对所有自然数 $n,k$ 与 $m\ge1$，

$$B(n,k,m)=F(n,m;n+k).$$
:::

::: proof
展开上面的定义后，这正是所链接 Lean 声明证明的等式。该声明不包含舒尔多项式等式与 $m=0$ 边界。
:::

::: {.remark #s2 title="修正的子集权重" mathesis="collected:kurk396563:2:s2"}
对 $a\ge1,b,r\ge0$，令 $N=a+b$、$P(z)=\prod_{j=1}^N(z-j)$，并置

$$\widetilde A_i=\frac{(-1)^{N-i}i^N}{N!}\binom Ni.$$

$$\widetilde A_i=\frac{i^{N-1}}{P'(i)}\quad(1\le i\le N).$$

令 $\beta_r(A,b)=\det[c(A+i,b+j)]_{1\le i,j\le r}$。修正公式为

$$\beta_r(a+b,b)=(-1)^{\binom a2}\sum_{1\le i_1<\cdots<i_a\le N}Z(i),$$

$$Z(i)=\prod_{u<v}(i_v-i_u)^2\prod_{t=1}^a\widetilde A_{i_t}i_t^{r-a+1}.$$

来源：原文推论 2。每个权重乘以 $i^{r-a+1}$ 后等于 $i^{b+r}/P'(i)$，所以同一个子集展开给出证明。$(a,b,r)=(1,1,1)$ 时，修正值为 $-1+2\cdot2=3$；把印刷公式中未定义的权重补成零会给出 $1$。[参与剩余形式化](https://github.com/the-omega-institute/trureturing-requests/issues/257)。
:::

::: {.remark #s3 title="所有整数指数" mathesis="collected:kurk396563:2:s3"}
设 $n,m\ge1$、$N=n+m$，$a$ 为整数。结果分为三段。

当 $a\ge n$，

$$F(n,m;a)=s_{((a-n)^m)}(1,\ldots,N).$$

当 $-m<a<n$，

$$F(n,m;a)=0.$$

当 $a=-m-r$、$r\ge0$，

$$F(n,m;a)=\frac{(-1)^{nm}}{(N!)^{m+r}}\,s_{(r^n)}(1,\ldots,N).$$

另外，对任意整数 $a$，边界值为 $F(0,m;a)=(m!)^a$。

来源：原文推论 3。[参与整数指数推广的形式化](https://github.com/the-omega-institute/trureturing-requests/issues/258)。
:::

::: proof
对互异非零的 $x_1,\ldots,x_N$，子集表达式是一个交替式除以普通范德蒙德行列式；其行指数为 $a+m-1,\ldots,a,n-1,\ldots,0$。若 $-m<a<n$，两个指数区间重叠，行列式便有重复行。正指数分支是舒尔交替式。负指数分支对 $nm$ 个交叉差分别取倒数，产生符号 $(-1)^{nm}$；补矩形恒等式随后给出 $(N!)^{-(m+r)}$ 与矩形 $(r^n)$。若 $n=0$，只有完整字母表这一个子集，其值为 $(m!)^a$。
:::

::: {.remark #s4 title="第二类斯特林数的矩行列式" mathesis="collected:kurk396563:2:s4"}
对 $n,k\ge0,m\ge1$，令 $N=n+m$，定义 $m\times m$ 矩阵 $A$：

$$A_{ij}=S(n+k+i+j+1,N).$$

下标范围为 $0\le i,j<m$。

则

$$B(n,k,m)=(-1)^{\binom m2}\det A.$$

当 $u<v$ 时，$S(u,v)=0$。来源：原文推论 4。这个结果不同于故事中提到的第二类字母表修正。[参与矩行列式的形式化](https://github.com/the-omega-institute/trureturing-requests/issues/263)。
:::

::: proof
对 $P(z)=\prod_{t=1}^N(z-t)$，令 $M_\ell=\sum_{t=1}^Nt^\ell/P'(t)$。部分分式给出

$$\sum_{\ell\ge0}M_\ell z^\ell=\frac{z^{N-1}}{\prod_{t=1}^N(1-tz)}.$$

所以 $M_\ell=S(\ell+1,N)$，也包括应为零的范围。Cauchy–Binet 把 $\det[M_{n+k+i+j}]$ 展开成带范德蒙德平方的子集和。与第一类子集公式比较，符号正好是 $(-1)^{\binom m2}$。
:::

::: {.remark #s5 title="有理生成函数与递推" mathesis="collected:kurk396563:2:s5"}
固定 $n\ge0,m\ge1$。对 $\{1,\ldots,N\}$ 的每个 $m$ 元子集 $S$，令

$$\lambda_S=\prod_{s\in S}s,\qquad D_S=\prod_{s\in S,t\notin S}(s-t).$$

作为形式幂级数，

$$\sum_{k\ge0}B(n,k,m)z^k=\sum_{|S|=m}\frac{\lambda_S^n}{D_S(1-\lambda_Sz)}.$$

该序列被 $\prod_{|S|=m}(E-\lambda_S)$ 消去，其中 $E$ 把 $k$ 移到 $k+1$。不同子集的乘积可以相同，所得递推阶数不一定最小。

来源：原文推论 5，恢复了 Amdeberhan–Ekhad 定理 1 的既有分母。对每个子集求几何级数；相应的移位因子消去其指数序列，便得结论。[参与该推论的形式化](https://github.com/the-omega-institute/trureturing-requests/issues/260)。
:::

::: {.theorem #s6 title="Kurkov 在 A132393 中的倒数恒等式" mathesis="collected:kurk396563:2:s6" lean="D5/S1/Recurrence/Algebraic/KurkovNestedStirlingIdentity.result"}
对 $n\ge0,m\ge1$，定义

$$R=(-1)^{nm}HF.$$

这里 $R=R(n,m)$、$H=H(n,m)$、$F=F(n,m;-m-1)$。

$$Q(n,m)=\prod_{t=1}^m(n+t)^t.$$

则

$$c(N+1,m+1)=N!\,Q(n,m)R(n,m).$$
:::

::: proof
这是原文推论 6，也是 Kurkov 于 2026 年 5 月 24 日提出的 FORMULA 猜想。展开 $F$ 后，得到所链接 Lean 源码中的逐字带符号倒数链和。书面证明中，变量取倒数给出 $R=H e_n(1,\ldots,N)/(N!)^{m+1}$；基本对称多项式等于 $c(N+1,m+1)$，且 $QH=(N!)^m$。两式合起来得到结论，也覆盖 $n=0$。
:::

::: {.remark #s7 title="经典伴随恒等式" mathesis="collected:kurk396563:2:s7"}
对 $v\ge k\ge1$，

$$c(v,k)=e_{v-k}(1,\ldots,v-1),$$

$$\sum_{v\ge k}c(v,k)\frac{t^v}{v!}=\frac{(-\log(1-t))^k}{k!}.$$

对 $v\ge0$，有关于 $b,x$ 的多项式恒等式

$$\sum_{k=0}^vc(v,k)b^kx^{v-k}=\prod_{j=0}^{v-1}(b+jx).$$

对 $v>k\ge1$，

定义

$$L_1(v,k)=\sum_{j=2}^{v-k+1}\binom{-k}{j}(-1)^j\!c(v,k+j-1).$$

则 $(v-k)c(v,k)=L_1(v,k)$。类似地，定义

$$L_2(v,k)=\sum_{j=2}^{v-k+1}(j-2)!\binom vj c(v-j+1,k).$$

则 $(v-k)c(v,k)=L_2(v,k)$。

对 $v\ge1$，记 $H_v=\sum_{j=1}^v1/j$，则

$$\sum_kkc(v,k)=v!H_v,$$

$$\sum_k(k\mathbin{\pm}1)c(v,k)=v!(H_v\mathbin{\pm}1),$$

$$\sum_kkc(v,v-k)=v!(v-H_v).$$

来源：原文推论 7。行多项式给出基本对称公式与加权值。令 $R_v(x)=\prod_{j=0}^{v-1}(x+j)$，在 $\sum_vR_v(x)t^v/v!=(1-t)^{-x}$ 中比较系数，得到列的指数生成函数。两条递推分别在 $xR_v(x+1)=(x+v)R_v(x)$ 与 $(t+(1-t)\log(1-t))G'_k$ 中比较系数，其中 $G_k=(-\log(1-t))^k/k!$。最后用 $R_v(1)$ 与 $R'_v(1)$ 得到调和数行和。

这些都是有明确归因的既有恒等式：原文引用了 Lang 和 Deléham 的 OEIS 公式、Quaintance–Gould 中归因于 Hagen 的行递推、Petrov 的 2025 年列证明、ploosu2 的 2025 年证明，以及 K. Lee 的 2026 年组合证明。[参与剩余命题的形式化](https://github.com/the-omega-institute/trureturing-requests/issues/261)。
:::

## 另一项修正与证据

第 2 节中未编号的第二类字母表修正为

$$\det[S(A+i,b+j)]_{i,j=1}^r=s_{((A-b)^r)}(1,\ldots,b+r).$$

假设是 $A\ge b\ge0,r\ge1$。它有[自己的参与任务](https://github.com/the-omega-institute/trureturing-requests/issues/259)，不同于上面的矩行列式。具体见证是 $S(4,2)=7$，而印刷字母表给出 $s_{(2)}(1,2,3)=25$。

两条所链接 Lean 声明证明的是逐字嵌套恒等式。舒尔求值、整数推广、矩行列式、修正公式与伴随结果分别保留书面证明和具体参与链接。有限精确算术检查支持其列明的参数范围，不替代全参数证明。

既有来源：[Merca，定理 2.1–2.2](https://doi.org/10.1007/s10998-014-0034-3)；[Amdeberhan–Ekhad，定理 1–3](https://arxiv.org/abs/2206.13244v1)；[Tamvakis 的舒尔多项式介绍](https://doi.org/10.4171/LEM/58-1-7)；[A396563](https://oeis.org/A396563/internal)；[A132393](https://oeis.org/A132393/internal)。
