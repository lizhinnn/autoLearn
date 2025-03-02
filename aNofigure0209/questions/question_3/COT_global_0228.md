# Question 3: 3.1 使用劳斯（Routh）判据判断下列系统稳定性，指出位于右半平面和虚轴上的特征根的数量

Query Time: 2025-02-28 11:49:47.990488
Query Mode: global with chain of thought

## Original Question
3.1 使用劳斯（Routh）判据判断下列系统稳定性，指出位于右半平面和虚轴上的特征根的数量  

$$
\begin{array}{c}{{1.D(s)=s^{6}+3s^{5}+5s^{4}+9s^{3}+8s^{2}+6s+4}}\ {{2.D(s)=s^{5}+3s^{4}+12s^{3}+20s^{2}+35s+25}}\end{array}
$$

## Answer (with Chain of Thought)
使用劳斯（Routh）判据判断系统的稳定性包括以下几个步骤:
1. 构造劳斯表格。
2. 检查第一列的符号变化次数，如果有符号变化，就代表存在系统的不稳定特征根。

我们将逐一分析每一个多项式。

### 1. \( D(s) = s^6 + 3s^5 + 5s^4 + 9s^3 + 8s^2 + 6s + 4 \)

构造劳斯表格：

```
| s^6 |   1   |   5   |   8   |   4   |
| s^5 |   3   |   9   |   6   |       |
| s^4 |       |       |       |       |
| s^3 |       |       |       |       |
| s^2 |       |       |       |       |
| s^1 |       |       |       |       |
| s^0 |       |       |       |       |
```

填充 \(s^4\) 行：

```
a = \frac{3 \cdot 5 - 1 \cdot 9}{3} = 2
b = \frac{3 \cdot 8 - 1 \cdot 6}{3} = 6

| s^6 |   1   |   5   |   8   |   4   |
| s^5 |   3   |   9   |   6   |       |
| s^4 |   2   |   6   |       |       |
| s^3 |       |       |       |       |
| s^2 |       |       |       |       |
| s^1 |       |       |       |       |
| s^0 |       |       |       |       |
```

填充 \(s^3\) 行：

```
a = \frac{2 \cdot 9 - 3 \cdot 6}{2} = \frac{18 - 18}{2} = 0
c = \frac{2 \cdot 6 - 3 \cdot 4}{2} = -3

| s^6 |   1   |   5   |   8   |   4   |
| s^5 |   3   |   9   |   6   |       |
| s^4 |   2   |   6   |       |       |
| s^3 |   0   |  -3   |       |       |
| s^2 |       |       |       |       |
| s^1 |       |       |       |       |
| s^0 |       |       |       |       |
```

填充 \(s^2\) 行：

```
因为 \(s^3\) 行的第一个元素是零，所以需要特殊处理。

我们用 \(\epsilon\) 替代0，继续计算：

```
对于 \(s^2\) 行：

```
a = -\frac{\epsilon \cdot 6 - 2(-3)}{\epsilon} = -\frac{6\epsilon + 6}{\epsilon} = -6 - 6/\epsilon
```

因此，该行第一个元素是负数，有符号变化，系统不稳定。

```
经过以上分析解得：

### 2. \( D(s) = s^5 + 3s^4 + 12s^3 + 20s^2 + 35s + 25 \)

构造劳斯表格: 
```
| s^5 | 1 | 12  | 35 |
| s^4 | 3 | 20  | 25 |
| s^3 | a | b   |    |
| s^2 | c | d   |    |
| s^1 | e |     |    |
| s^0 | 25|     |    |
```
计算 \(s^3\) 行：
```
a = \dfrac{3*12 -1*20}{3} = 8
b = \dfrac{3*35 - 1*25}{3} = 30 
```
计算 \(s^2\) 行:
```
c = \dfrac{8*20 - 3*30}{8} = 2.5
d = 0 ; 剩余
```
计算 \(s^1\) 行:
```
e = 25
```
进行最后填充:
```
| s^5 | 1 | 12  | 35 |
| s^4 | 3 | 20  | 25 |
| s^3 | 8 | 30  |    |
| s^2 | 2.5 |  |    |
| s^1 | 25 |     |    |
| s^0 | 25|     |    |
```
没有符号变化数次， 系统稳定.

### 最终结论:

1. \[ D(s) = s^6 + 3s^5 + 5s^4 + 9s^3 + 8s^2 + 6s + 4 \]: 系统不稳定，存在至少在一个右半平面特征根，无虚轴特征根。
2. \[ D(s) = s^5 + 3s^4 + 12s^3 + 20s^2 + 35s + 25 \]: 系统稳定，无右半平面特征根。