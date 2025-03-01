# Question 6: 3.4

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive with chain of thought

## Original Question
3.4  

单位反馈控制系统开环传函为：  

$$
G(s)={\frac{100}{s(s+10)}}
$$  

$1.$ 求三个误差系数： $K_{p},K_{v},K_{a}$ 2. 当参考输入为 $\textstyle r(t)=1+t+a t^{2}$ 时，闭环系统的稳态误差

## Answer (with Chain of Thought)
K_a = \lim_{s \to 0} s^2 \cdot \frac{100}{s(s + 10)} = \lim_{s \to 0} \frac{100s}{s + 10} = \lim_{s \to 0} \frac{100 \cdot 0}{10} = 0 \]

### 第2步：计算稳态误差

参考输入 \( r(t) = 1 + t + at^2 \) 分为三部分：
1. 常数输入：\( r(t) = 1 \)
2. 斜坡输入：\( r(t) = t \)
3. 抛物线输入：\( r(t) = at^2 \)

稳态误差公式：
\[ e_{ss} = \lim_{s \to 0} \frac{1}{1 + G(s)H(s)} \]

#### 1. 常数输入 \( r(t) = 1 \)

\[ e_{ss,1} = \frac{1}{1 + K_p} = \frac{1}{1 + \infty} = 0 \]

#### 2. 斜坡输入 \( r(t) = t \)

\[ e_{ss,2} = \frac{1}{K_v} = \frac{1}{10} \]

#### 3. 抛物线输入 \( r(t) = at^2 \)

\[ e_{ss,3} = \frac{1}{K_a} \]
但是因为 \( K_a = 0 \)，抛物线输入的稳态误差是无限大的，因为系统无法跟随加速度输入。

### 最终稳态误差：

总的稳态误差：
\[ e_{ss} = e_{ss,1} + e_{ss,2} + e_{ss,3} = 0 + \frac{1}{10} + \infty = \infty \]

综上所述：

1. 三个误差系数为：
   \[ K_p = \infty, K_v = 10, K_a = 0 \]

2. 当参考输入为 \( r(t) = 1 + t + at^2 \) 时，闭环系统的稳态误差为 \(\infty\)。

答案总结：

1. 三个误差系数 \(K_p = \infty, K_v = 10, K_a = 0\)
2. 闭环系统的稳态误差为 \(\infty\)。