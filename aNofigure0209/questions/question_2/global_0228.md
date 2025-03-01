# Question 2: 2.2 求解如下微分方程

Query Time: 2025-02-28 11:49:47.990488
Query Mode: global

## Original Question
2.2 求解如下微分方程  

$$
{\frac{d^{2}y(t)}{d t^{2}}}+2{\frac{d y(t)}{d t}}+2y(t)=r(t)
$$  

其中，输入信号 $u(t)=\delta(t)$ , 并假设 $y(0)=y^{\prime}(0)=0$ , 求系统输出 $y(t)$

## Answer
要解决给定的微分方程
$$
\frac{d^2 y(t)}{d t^2} + 2 \frac{d y(t)}{d t} + 2 y(t) = r(t)
$$
的初值问题，我们需要求系统的零状态响应。在这种情况下，输入信号是狄拉克δ函数，即 $r(t) = \delta(t)$，并且初始条件为 \( y(0) = 0 \) 和 \( \frac{d y(0)}{d t} = 0 \)。

首先我们可以通过拉普拉斯变换来解决这个问题。应用拉普拉斯变换到方程的两边得到：

$$
\mathcal{L}\left\{\frac{d^2 y(t)}{d t^2}\right\} + 2 \mathcal{L}\left\{\frac{d y(t)}{d t}\right\} + 2 \mathcal{L}\left\{y(t)\right\} = \mathcal{L}\{r(t)\}
$$

由于初始条件 \( y(0) = 0 \) 和 \( \frac{d y(0)}{d t} = 0 \)，这可以简化为：

$$
s^2 Y(s) + 2s Y(s) + 2 Y(s) = 1
$$

因为 $\mathcal{L}\{\delta(t)\} = 1$。

将其整理为关于 \( Y(s) \) 的方程：

$$
Y(s) (s^2 + 2s + 2) = 1
$$

解得：

$$
Y(s) = \frac{1}{s^2 + 2s + 2}
$$

接下来我们需要做逆拉普拉斯变换来得到 \( y(t) \)。将 \( s^2 + 2s + 2 \) 分解因式：

$$
s^2 + 2s + 2 = (s + 1)^2 + 1
$$

所以，

$$
Y(s) = \frac{1}{(s + 1)^2 + 1}
$$

我们认出这是一个标准的拉普拉斯变换，

$$
\mathcal{L}^{-1}\left\{\frac{1}{(s + a)^2 + b^2}\right\} = e^{-at} \sin(bt)
$$

在这里， \( a = 1 \) 和 \( b = 1 \)。因此，

$$
y(t) = \mathcal{L}^{-1}\left\{\frac{1}{(s + 1)^2 + 1}\right\} = e^{-t} \sin(t)
$$

所以系统的响应 \( y(t) \) 在输入 \( u(t) = \delta(t) \) 初始条件 \( y(0)=0 \) 和 \( y'(0)=0 \) 下是：

$$
y(t) = e^{-t} \sin(t)
$$