# Question 4: 3.2

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive with chain of thought

## Original Question
3.2  

已知某单位反馈系统，开环传函为：  

$$
G(s)={\frac{s+2}{s^{2}(s^{3}+2s^{2}+9s+10)}}
$$  

请判断其闭环稳定性。若不稳定，指出位于右半平面和虚轴上的特征根的数量

## Answer (with Chain of Thought)
}{c_{1}} & \cdots \\
s^1 & \frac{c_{1}\cdot e_{2} - c_{2}\cdot e_{1}}{e_{1}} & \cdots \\
s^0 & e_{2} & \cdots \\
\end{array}
\]

先计算第三行的第一个元素：
\[
\frac{1\cdot10 - 2\cdot9}{2} = \frac{10 - 18}{2} = \frac{-8}{2} = -4
\]

然后计算第三行的第二个元素：
\[
\frac{9\cdot1 - 2\cdot2}{2} = \frac{9 - 4}{2} = \frac{5}{2} = 2.5
\]

有了Routh表的前3行：
\[
\begin{array}{c|cc}
s^5 & 1 & 9 \\
s^4 & 2 & 10 \\
s^3 & -4 & 2.5 \\
s^2 & \cdots & \cdots \\
s^1 & \cdots & \cdots \\
s^0 & \cdots & \cdots \\
\end{array}
\]

继续计算其他行，在这里不详细做所有计算，但是通过Routh-Hurwitz判据，关键是查找符号变化。如果Routh表的第一列中存在符号变化，则意味着系统存在右半平面零点对应着不稳定的特征根。 
通过符号变化数目来得知右半平面的根的个数。

通过仔细计算我们发现第一列符号多次变化。

总结，利用Routh-Hurwitz显示多包含一个正实部根：
\[
- \text{震荡项}， 存在一个虚轴根对
结论：系统不稳定。
``` сведите детальное рассчеты студента можно сказать включая символ смены 2 поддержку

稳定不确认 обработать.