# Question 2: 2.2 求解如下微分方程

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive

## Original Question
2.2 求解如下微分方程  

$$
{\frac{d^{2}y(t)}{d t^{2}}}+2{\frac{d y(t)}{d t}}+2y(t)=r(t)
$$  

其中，输入信号 $u(t)=\delta(t)$ , 并假设 $y(0)=y^{\prime}(0)=0$ , 求系统输出 $y(t)$

## Answer
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