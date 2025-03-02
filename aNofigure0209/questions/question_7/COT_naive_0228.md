# Question 7: 3.6

Query Time: 2025-02-28 11:49:47.990488
Query Mode: naive with chain of thought

## Original Question
3.6  

用温度计测量容器内水温，发现需要1min才能指示实际水温的 $98\%$ ，假设温度计的传函为典型的一阶系统结构：  

$$
\frac{1}{T s+1}
$$  

求：  

$1.$ 该温度计指示出实际水温从 $10\%$ 变化到 $90\%$ 所需要的时间是多少？2. 如果容器加热，使水温以 $10\%$ /min的速度线性变化，温度计的稳态指示误差是多少？

## Answer (with Chain of Thought)
9 \):

\[ y(t) = 1 - e^{-t/T} \]

解方程：

\[ 0.1 = 1 - e^{-t_1/T}  \]
\[ e^{-t_1/T} = 0.9 \]
\[ t_1 = -T \ln(0.9) \]

\[ 0.9 = 1 - e^{-t_2/T} \] 
\[ e^{-t_2/T} = 0.1 \] 
\[ t_2 = -T \ln(0.1) \] 

### 计算时间间隔：

\[ \Delta t = t_2 - t_1  \]

插入已知常数 \( T \approx 0.256 \) min 及对数值：

\[ t_1 = -0.256 \ln(0.9) \approx 0.0256 \text{ min} \]
\[ t_2 = -0.256 \ln(0.1) \approx 0.59181 \text{ min} \]

所以：

\[ \Delta t = 0.59181 - 0.0256 \approx 0.5662 \text{ min} \]

#### 第3部分：稳态误差

对于线性变化10%/min，即斜率为0.1/min。

跟随响应系统：

\[ \theta_{\infty} = \frac{1}{T} \times 0.1 = \frac{1}{0.256} \times 0.1 \approx 0.39 \]

稳态误差：

\[ e_{ss} = \text{斜率} \times T \]

即：

\[ e_{ss} = 0.1 \times 0.256 = 0.0256 \min \]

换算为百分比误差：

\[ e_{ss} = 2.56\% \]

### 得出结论

1. 从10%到90%变化所需时间大约是0.5662分钟。
2. 稳态指示误差将达到2.56%。