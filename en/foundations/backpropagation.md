---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/backpropagation/
title: "Backpropagation"
no_comments: true
math: true
---

> Part of [Deep Learning Fundamentals](../dl/) · [Foundations overview](../)

**Backpropagation** is the algorithm that efficiently computes the [gradient](../gradient/) of the [loss function](../loss-function/) with respect to **every single weight** in a network. At heart it is the systematic application of the **[chain rule](../chain-rule/)** to a multilayer network: the error flows "backward" from the output layer, layer by layer, telling each parameter along the way "which direction you should move, and by how much".

## Intuition

After [forward propagation](../forward-propagation/) has produced a prediction, we get an error (the loss). The question is: with thousands upon thousands of weights in the network, **whose fault is it, and how much**?

Imagine a production line that turns out a defective product. We trace responsibility back from the finished product: first see how much the last step contributed to the error, then how that step was affected by the one before it… all the way back, apportioning the "blame" proportionally to every station. Backpropagation is this **automatic blame-tracing system** — it computes a gradient for each weight, expressing "if this weight grows a little, how will the loss change".

The key insight: **differentiating with respect to each weight separately is far too slow** (there are millions of parameters). Backpropagation cleverly **reuses intermediate results**, computing all the gradients in a single back-to-front sweep at a cost roughly equal to one extra forward pass.

## The chain rule: derivation across layers

Let the loss be $\mathcal{L}$. We want $\dfrac{\partial \mathcal{L}}{\partial W^{(l)}}$ and $\dfrac{\partial \mathcal{L}}{\partial b^{(l)}}$. Recall the forward formulas $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$.

Define each layer's **error term** $\delta^{(l)} = \dfrac{\partial \mathcal{L}}{\partial z^{(l)}}$, which expresses "the effect on the loss of a change in this layer's pre-activation value".

**Output layer** (layer $L$):

$$
\delta^{(L)} = \frac{\partial \mathcal{L}}{\partial a^{(L)}} \odot \sigma'\big(z^{(L)}\big)
$$

**Recurse backward layer by layer** (this is the core recurrence of backpropagation):

$$
\delta^{(l)} = \big( W^{(l+1)\top}\, \delta^{(l+1)} \big) \odot \sigma'\big(z^{(l)}\big)
$$

Once every layer's $\delta^{(l)}$ is known, the gradients are simple:

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}} = \delta^{(l)}\, a^{(l-1)\top},
\qquad
\frac{\partial \mathcal{L}}{\partial b^{(l)}} = \delta^{(l)}
$$

Notation:

- $\delta^{(l)}$: the error signal of layer $l$ (same dimension as the number of [neurons](../neuron/) in that layer).
- $W^{(l+1)\top}$: the **transpose** of the next layer's weight matrix — it "maps" the error from layer $l+1$ back to layer $l$.
- $\odot$: **element-wise multiplication** (the Hadamard product).
- $\sigma'(z^{(l)})$: the **derivative** of the [activation function](../activation-function/) at this layer, which decides whether the signal can flow back smoothly.
- $a^{(l-1)}$: the previous layer's activations, saved during forward propagation.

Note the repeated product of $\sigma'(z^{(l)})$ terms — it is the very root of [vanishing / exploding gradients](../vanishing-exploding-gradient/): the more layers, the more derivatives get multiplied together.

## A concrete example

Consider the simplest two-layer chain: $z_1 = w_1 x$, $a_1 = \sigma(z_1)$, $z_2 = w_2 a_1$, $\hat y = z_2$, with loss $\mathcal{L} = \tfrac12 (\hat y - y)^2$. Let $\sigma$ be the Sigmoid.

Compute from back to front:

$$
\frac{\partial \mathcal{L}}{\partial \hat y} = \hat y - y
\;\Rightarrow\;
\delta_2 = \hat y - y
$$

$$
\frac{\partial \mathcal{L}}{\partial w_2} = \delta_2 \cdot a_1
$$

Propagate back one layer:

$$
\delta_1 = (w_2 \cdot \delta_2)\cdot \sigma'(z_1),
\qquad
\frac{\partial \mathcal{L}}{\partial w_1} = \delta_1 \cdot x
$$

Plug in numbers: $x=1,\, w_1=0.5,\, w_2=2,\, y=1$. Forward: $z_1=0.5$, $a_1=\sigma(0.5)\approx0.622$, $\hat y = 2\times0.622=1.244$.

Backward: $\delta_2 = 1.244-1 = 0.244$; $\partial\mathcal{L}/\partial w_2 = 0.244\times0.622 \approx 0.152$.
Sigmoid derivative $\sigma'(z_1)=a_1(1-a_1)=0.622\times0.378\approx0.235$.
$\delta_1 = 2\times0.244\times0.235 \approx 0.115$; $\partial\mathcal{L}/\partial w_1 = 0.115\times1 = 0.115$.

```python
import numpy as np
sig = lambda z: 1/(1+np.exp(-z))
x, w1, w2, y = 1.0, 0.5, 2.0, 1.0
z1 = w1*x; a1 = sig(z1); yhat = w2*a1          # forward
d2 = yhat - y                                   # output error
gw2 = d2*a1
d1 = w2*d2*(a1*(1-a1))                           # propagate back one layer
gw1 = d1*x
print(round(gw1,3), round(gw2,3))               # 0.115 0.152
```

{% include fviz/backprop-graph.html %}

## Why it matters / where it is used

- **Without backpropagation there would be no modern deep learning.** It makes training networks with millions of parameters computationally feasible.
- The gradients it produces are handed to an [optimizer](../optimizer/) (such as [Adam](../adam/)), which updates the weights according to the [learning rate](../learning-rate/): $W \leftarrow W - \eta\, \partial\mathcal{L}/\partial W$.
- In practice you almost never have to write it by hand — [automatic differentiation](../autodiff/) frameworks do it for you. But only by understanding its recurrence can you diagnose problems such as non-convergence or exploding gradients.

## Common misconceptions

- **"Backpropagation = [gradient descent](../gradient-descent/)"** — no. Backpropagation only **computes the gradients**; how to use them to update the parameters is the [optimizer](../optimizer/)'s job.
- **"It learns the parameters"** — it does not update parameters; it only supplies directional information.
- **"It has nothing to do with forward propagation"** — quite the opposite: it **relies heavily** on the intermediate values $a^{(l)}, z^{(l)}$ saved by forward propagation.

[← Deep Learning Fundamentals](../dl/) · [Foundations overview](../)
