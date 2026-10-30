---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/dl/
title: "Deep Learning Fundamentals"
lead: "Neural networks, backpropagation, optimizers, common architectures and training practice — the engine behind modern forecasting models. A framework of concepts only."
prev: /foundations/ml/
next: /foundations/
math: true
---

> This is a **concept map**: it points out "what deep learning is made of, how it is trained, and which architectures exist". In-depth mathematics and implementation are left to dedicated textbooks.

## 1. What a [neural network](../neural-network/) is made of

- **[Neuron](../neuron/)**: a weighted sum plus a bias, passed through a nonlinearity
- **Layers and networks**: neurons stack into layers, layers stack into networks
- **[Forward propagation](../forward-propagation/)**: the input is transformed layer by layer into the output
- **[Activation functions](../activation-function/)**: ReLU, Sigmoid, Tanh, GELU — they introduce **nonlinearity**; without it the whole network collapses into a [linear model](../linear-model/)

$$h = \sigma(Wx + b)$$

## 2. How to train: [backpropagation](../backpropagation/)

- **[Loss function](../loss-function/)**: measures the gap between prediction and truth
- **Backpropagation**: uses the **[chain rule](../chain-rule/)** to pass the error back from the output layer, layer by layer, computing the gradient of every parameter
- **[Automatic differentiation](../autodiff/)**: the framework does the differentiation for you (you only write the forward pass)
- **[Optimizers](../optimizer/)**: SGD, Momentum, RMSProp, **[Adam](../adam/)** (the most widely used)
- **[Learning rate](../learning-rate/)**: the most important hyperparameter — too large and training diverges, too small and it crawls

## 3. Preventing [overfitting](../overfitting/)

Deep models have enormous numbers of parameters, so generalization is the central challenge.

- **[Dropout](../dropout/)**: randomly drop neurons during training
- **[Batch normalization (BatchNorm)](../batchnorm/) / layer normalization (LayerNorm)**: stabilize training
- **[Early stopping](../early-stopping/)**: stop when the validation set gets worse
- **Data augmentation / weight decay**: further regularization

## 4. Common [architectures](../architectures/)

| Architecture | Good at | Time-series relevance |
|------|------|-------------|
| **MLP / fully connected** | General purpose | DLinear, N-BEATS |
| **CNN** | Local patterns | TCN, convolutional forecasters |
| **RNN / LSTM / GRU** | Sequences, memory | Classic sequence forecasting |
| **Transformer / attention** | Long-range dependencies | Modern sequence models |
| **U-Net** | Multiple scales | **Kernel U-Net (KUN)** |

## 5. [Training practice](../training-practice/)

- **[Batch size](../batch/)** and **epochs**
- **[GPU](../gpu/) acceleration**: makes training large models feasible
- **Gradient problems**: vanishing / exploding gradients and their remedies (residual connections, normalization, gradient clipping)
- **Transfer learning and pre-training**: reuse representations already learned

> Link to the main course: Lectures 12–14 apply these architectures to time series forecasting, culminating in this repository's **Kernel U-Net (KUN)**.

---

**Key terms:** [neuron](../neuron/), [activation function](../activation-function/), [forward propagation](../forward-propagation/), [backpropagation](../backpropagation/), [automatic differentiation](../autodiff/), [Adam](../adam/), [learning rate](../learning-rate/), [Dropout](../dropout/), [BatchNorm](../batchnorm/), [early stopping](../early-stopping/), [MLP](../mlp/), [CNN](../cnn/), [RNN](../rnn/) / [LSTM](../lstm/), [Transformer](../transformer/), [attention](../attention/), [U-Net](../u-net/), [GPU](../gpu/), [vanishing / exploding gradients](../vanishing-exploding-gradient/).
