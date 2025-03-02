# Question 10: 4.3 综合题

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive

## Original Question
4.3 综合题  

1. 参考4.2节第3题，在绘制出系统根轨迹之后，分析回答以下问题：  

a) 该系统随着 $K^{*}$ 增加，是否会变得不稳定？为什么？b) 系统若要保持无超调，那么增益 $K^{*}$ 取值范围是？c) 系统阻尼比 $\zeta=0.707$ 时，系统的增益 $K^{*}$  

2. 参考4.2节第2题，若要求系统阻尼比 $\zeta>0.767$ ，结合根轨迹分析回答以下问题：  

a) 确定系统开环根轨迹增益的取值范围；  
b) 确定临界增益处，系统的闭环根的取值;  

c) 临界增益处，系统的复数极点是否是系统的主导极点，若是，请利用主导极点估算系统的各项性能参数  




1. 绘制Bode图  

$$
G(s)={\frac{10(0.5s+1)}{s(s+10)(s+25)}}
$$  

$$
G(s)={\frac{(0.5s+100)}{(s+2)(s+10)(s^{2}+s+25)}}
$$

## Answer
K \)
阻尼比 \( \zeta = 0.707 \) （45度线）常被称为最优阻尼比。根据根轨迹图，可以找到对应于45°线上的离散根位置的增益。使用Matlab命令 `sgrid(zeta_value, wn_value)` 可视化45度线并确定相交点的增益值。

### 问题2

若要求系统阻尼比 \( \zeta > 0.767 \)，结合根轨迹分析回答以下问题：

#### a) 确定系统开环根轨迹增益的取值范围；
对于给定的阻尼比 \( \zeta > 0.767 \)，找到根轨迹图中对应于该阻尼比线的增益\( K \)值范围，同样可以用Matlab命令 `sgrid(zeta_value, wn_value)` 来辅助分析。

#### b) 确定临界增益处，系统的闭环根的取值；
临界增益 \( K \) 是刚好使系统到达临界稳定的增益值（即边界增益）。这意味着在该增益下系统根位于虚轴上。通过根轨迹图确定该点的根。

#### c) 临界增益处，系统的复数极点是否是系统的主导极点？若是，请利用主导极点估算系统的各项性能参数。
若临界增益处的复数极点显著接近于其他根的极值并且主导主要系统行为，则这个极点是主导极点。通过主导极点估算系统的性能参数包括：
- 上升时间 \( t_r \)
- 超调量 \( M_p \)
- 调节时间 \( t_s \)
- 峰值时间 \( t_p \)

### 绘制Bode图

对于给出的传递函数：
\[ G(s) = \frac{10(0.5s+1)}{s(s+10)(s+25)} \]
\[ G(s) = \frac{(0.5s+100)}{(s+2)(s+10)(s^2+s+25)} \]

可以通过Matlab的 `bode(G)` 命令绘制波特图。

请使用Matlab代码，如下：
```matlab
% Define transfer function
G1 = tf([5 10], [1 35 250 0]);
G2 = tf([0.5 100], [1 13 25 250]);

% Plot bode plots
figure;
bode(G1);
title('Bode Plot of G1');
grid on;

figure;
bode(G2);
title('Bode Plot of G2');
grid on;
```

将会生成所需的波特图。

通过以上方法和计算，可以解决具体的系统根轨迹分析和绘制波特图的问题。