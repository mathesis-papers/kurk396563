# 从斯特林行列式到舒尔多项式：整数指数与两条 OEIS 猜想

Haobo Ma（Chrono AI，Singapore）与 Wenlin Zhang（Chrono AI，Singapore；National University of Singapore，Singapore）研究一个看似杂乱的交替嵌套和。它其实是一个小型行列式：把第一类斯特林数排成矩阵，行列式的值正好是一个矩形舒尔多项式。这个桥梁解释了符号、阶乘和范德蒙德平方从哪里来，并把指数从非负整数延伸到所有整数。

本书先用例子讲清问题和机制，再在[精确陈述](statements.md)中给出全部参数、边界情况和证明思路。精确结果附有对应证明与参与任务；两条嵌套恒等式可直接查看 Lean 源码。

作者的原始论文是公开的 CC BY 4.0 版本 2（2026-11-05）。文中引用 Merca 2014 的行列式恒等式（[DOI 10.1007/s10998-014-0034-3](https://doi.org/10.1007/s10998-014-0034-3)）以及 Amdeberhan–Ekhad 2022 的 [arXiv:2206.13244](https://arxiv.org/abs/2206.13244v1)。

- [故事与证明机制](story.md)
- [精确陈述、边界与逐条比较](statements.md)
- [学术 Beamer 演示稿](../slides/kurkov-stirling/deck.toml)
- [同一故事的讲解影片](../films/001-determinant-to-schur/film.json)
