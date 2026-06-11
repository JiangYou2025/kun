---
updated: "2026-06-11"
layout: lecture
lang: zh
permalink: /foundations/lstm/
title: "LSTM"
no_comments: true
math: true
---

> 出自[深度学习基础](../dl/) · [基础课总览](../)

**长短期记忆网络（LSTM, Long Short-Term Memory）** 是一种特殊的 [RNN](../rnn/)，它用一条"细胞状态"高速公路和三道"门"来主动决定记住什么、忘掉什么，从而能记住很长的依赖关系，缓解了朴素 RNN 的[梯度消失](../vanishing-exploding-gradient/)难题。

## 直观理解

朴素 RNN 的记忆每一步都要被 $\tanh$ 反复"揉捏"，越传越淡，几十步后就几乎什么都不剩了。LSTM 换了个思路：单独开一条**细胞状态**（cell state）$c_t$ 作为"记忆主干道"，信息可以在上面**近乎原样地直行**，少受干扰。

那记忆该怎么增删？LSTM 安排了三个**门**（gate），每个门是一个输出 $0\sim1$ 的小开关：

- **遗忘门**：决定旧记忆里哪些要丢掉（0=全忘，1=全留）；
- **输入门**：决定本步的新信息有多少写进记忆；
- **输出门**：决定从记忆里读出多少作为当前输出。

打个比方：$c_t$ 是一条传送带，遗忘门负责把带上不要的货物拿走，输入门负责往带上放新货物，输出门负责决定这一刻给外面看哪些货。

## 门控方程

设当前输入 $x_t$、上一步隐藏状态 $h_{t-1}$。三个门和候选记忆如下（$\sigma$ 是 Sigmoid [激活函数](../activation-function/)，输出 $0\sim1$）：

$$
\begin{aligned}
f_t &= \sigma\!\big(W_f [h_{t-1}, x_t] + b_f\big) &\text{(遗忘门)}\\
i_t &= \sigma\!\big(W_i [h_{t-1}, x_t] + b_i\big) &\text{(输入门)}\\
o_t &= \sigma\!\big(W_o [h_{t-1}, x_t] + b_o\big) &\text{(输出门)}\\
\tilde{c}_t &= \tanh\!\big(W_c [h_{t-1}, x_t] + b_c\big) &\text{(候选记忆)}
\end{aligned}
$$

然后更新细胞状态和隐藏状态：

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
\qquad
h_t = o_t \odot \tanh(c_t)
$$

逐符号解释：

- $[h_{t-1}, x_t]$：把上一步记忆和当前输入**拼接**成一个长向量。
- $f_t, i_t, o_t$：三个门向量，每个分量都在 $0\sim1$ 之间，逐元素地当"开关"。
- $\tilde{c}_t$：本步想写入的"候选新记忆"，取值 $(-1,1)$。
- $\odot$：**逐元素相乘**（Hadamard 积），就是把门当成阀门去缩放每一维。
- $c_t$：细胞状态，$=$（旧记忆按 $f_t$ 保留）$+$（新记忆按 $i_t$ 写入）。
- $h_t$：对外输出的隐藏状态，是细胞状态经 $\tanh$ 后按 $o_t$ 读出的部分。
- $W_\ast, b_\ast$：各门各自的权重与偏置，所有时间步共享。

## 细胞状态为什么能记住长期信息

关键在 $c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$ 这条**加法**式更新。

回忆 RNN 的麻烦：$\partial h_t / \partial h_{t-1}$ 里反复乘 $W_h$ 和 $\tanh'$，连乘后趋于 0。而 LSTM 沿细胞状态求导时：

$$
\frac{\partial c_t}{\partial c_{t-1}} = f_t
$$

如果遗忘门 $f_t \approx 1$，梯度就**几乎原样地往回传**，连乘很多步也不会塌缩到 0。这条"加法 + 接近 1 的门"通路被称为**常数误差传送带（CEC）**，正是 LSTM 能记住几百步前信息、且不易梯度消失的根本原因。

直观上：信息在 $c_t$ 上"直行"而非"反复被矩阵乘和挤压"，所以能走得远。

## 一个具体例子

假设细胞状态某一维当前是 $c_{t-1} = 0.8$（代表"句子开头是个复数主语"这条信息）。这一步：

- 遗忘门 $f_t = 0.95$ → 决定基本保留这条信息；
- 输入门 $i_t = 0.10$，候选 $\tilde{c}_t = 0.5$ → 只写入一点点新信息；
- 输出门 $o_t = 0.60$。

则：

$$
c_t = 0.95\times 0.8 + 0.10\times 0.5 = 0.76 + 0.05 = 0.81
$$

$$
h_t = 0.60 \times \tanh(0.81) \approx 0.60 \times 0.670 = 0.402
$$

记忆 $0.8 \to 0.81$ 几乎没变——"复数主语"被稳稳带到后面，等真正用到（比如决定动词单复数）时再通过输出门读出。PyTorch 里直接调用：

```python
import torch, torch.nn as nn

lstm = nn.LSTM(input_size=1, hidden_size=16, num_layers=1, batch_first=True)
x = torch.randn(8, 96, 1)             # (批=8, 96个时间步, 1维特征)
out, (h_n, c_n) = lstm(x)
print(out.shape)             # (8, 96, 16): 每步的隐藏状态
print(h_n.shape, c_n.shape)  # 最后一步的 h 和 c
```

## 在时间序列预测中的意义

LSTM 在 Transformer 流行之前，是**长序列预测的标准答案**：它能记住远处的趋势与周期（如年度季节性），又比朴素 RNN 稳定得多，广泛用于销量、电力、气象等预测。

但它仍**继承了 RNN 的顺序计算**——必须一步步算，长序列训练慢、推理慢，做很长的预测视野时依然吃力。这促使人们转向可并行、能跨尺度的结构：[Transformer](../transformer/)，以及本站主打的 **Kernel U-Net（KUN）**。KUN 借鉴 [U-Net](../u-net/) 的多分辨率思想，在多个时间尺度上同时建模，既绕开了"逐步递推"的速度瓶颈，又能更好地捕捉长程结构。

## 小结

- LSTM = RNN + **细胞状态 $c_t$** + **遗忘/输入/输出三道门**。
- 记忆更新是**加法**：$c_t = f_t\odot c_{t-1} + i_t\odot\tilde{c}_t$，门控决定记什么、忘什么、读什么。
- $\partial c_t/\partial c_{t-1} = f_t \approx 1$ 形成常数误差传送带，**缓解梯度消失**，能记长依赖。
- 仍是顺序模型、不易并行——长视野预测推动了 [Transformer](../transformer/) 与多尺度的 KUN。

[← 深度学习基础](../dl/) · [基础课总览](../)
