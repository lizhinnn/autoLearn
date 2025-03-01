# Question 1: 2.1 求以下信号的Laplace变换表达式

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive

## Original Question
2.1 求以下信号的Laplace变换表达式  

$$
\begin{array}{l}{1.{\:y}(t)=2+3t+4t^{2}}\ {2.{\:y}(t)=1-e^{-\frac{t}{T}}}\end{array}
$$

## Answer
- \( \mathcal{L}\{e^{-\frac{t}{T}}\} = \frac{1}{s + \frac{1}{T}} \)

因此：
\[
\mathcal{L}\{1\} = \frac{1}{s}
\]
\[
\mathcal{L}\{e^{-\frac{t}{T}}\} = \frac{1}{s + \frac{1}{T}}
\]

将这些结果相减：
\[
\mathcal{L}\{1 - e^{-\frac{t}{T}}\} = \frac{1}{s} - \frac{1}{s + \frac{1}{T}}
\]

综上所述，给定信号的拉普拉斯变换表达式分别为：
1. \( y(t) = 2 + 3t + 4t^2 \) 对应的拉普拉斯变换为：
\[
\mathcal{L}\{2 + 3t + 4t^2\} = \frac{2}{s} + \frac{3}{s^2} + \frac{8}{s^3}
\]

2. \( y(t) = 1 - e^{-\frac{t}{T}} \) 对应的拉普拉斯变换为：
\[
\mathcal{L}\{1 - e^{-\frac{t}{T}}\} = \frac{1}{s} - \frac{1}{s + \frac{1}{T}}
\]