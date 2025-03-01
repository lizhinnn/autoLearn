# Question 9: 4.2 绘制以下系统的根轨迹

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive

## Original Question
4.2 绘制以下系统的根轨迹  

1. 系统开环传函为：  

$$
G(s)H(s)={\frac{K^{*}(s+2)}{s(s+1)(s+10)}}
$$  

2. 系统开环传函为：  

$$
G(s)H(s)={\frac{K^{*}}{s(s+2)(s+8)}}
$$  

3. 系统开环传函为：  

$$
G(s)H(s)={\frac{K^{*}(s+1)}{s(s+2)(s+8)}}
$$

## Answer
的零点和极点：
- 零点：无
- 极点：\( s = 0, -2, -8 \)

根轨迹的特性：
- 所有根轨迹将趋向于无穷大，因为没有零点。
- 有3个极点，因此有3条根轨迹。

根轨迹图形：
在复平面上标出极点（用×表示），然后画出从极点出发的轨迹。

\[
\begin{aligned}
&\text{根轨迹}\left\{\begin{array}{ccccccc}
&\times & \quad & \quad & \times & \quad & \times \\
& (0) & \quad & (-2) &\quad & (-8)
\end{array}\right.
\end{aligned}
\]

### 3. 系统开环传递函数：\[ G(s)H(s) = \frac{K(s+1)}{s(s+2)(s+8)} \]

开环传递函数的零点和极点：
- 零点：\( s = -1 \)
- 极点：\( s = 0, -2, -8 \)

根轨迹的特性：
- 根轨迹从每个极点开始，并朝向零点。
- 1条额外的根轨迹将趋向于无穷远。

根轨迹图形：
在复平面上标出极点（用×表示）和零点（用○表示），然后画出从极点出发的轨迹。

\[
\begin{aligned}
&\text{根轨迹}\left\{\begin{array}{ccccccc}
&\times & \quad & \times & \quad & \times \\
& (0) & \quad & (-2) & \quad & (-8) \\
& \quad & ○(-1)
\end{array}\right.
\end{aligned}
\]

这些图形应该用专业的绘图工具来精确绘制以更好地精确展示出根轨迹。实际绘制根轨迹的一般方法包括手动绘图与使用控制理论软件包如MATLAB等。