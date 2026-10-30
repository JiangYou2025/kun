---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/math/
title: "Math Foundations"
lead: "Calculus, linear algebra, probability and statistics, optimization and information theory — the mathematical language of predictive modeling. We only build the framework and explain the concepts, without deep derivations."
prev: /foundations/
next: /foundations/cs/
math: true
---

> This is a **concept map**: it points out what each area of mathematics "contains and where it is used". Building intuition is enough here; for systematic derivations, consult a dedicated textbook.

## 1. [Calculus](../calculus/)

The mathematics of "change", and the basis of optimization and training.

- **Limits and continuity**: grasping the idea of "approaching infinitely closely"
- **Derivatives / partial derivatives**: how sensitive a function is to changes in one variable
- **[Gradient](../gradient/) $\nabla f$**: the direction of steepest ascent of a multivariate function — the core of training [neural networks](../neural-network/)
- **[Chain rule](../chain-rule/)**: differentiating composite functions, the mathematical principle behind **[backpropagation](../backpropagation/)**
- **Integrals**: computing areas / accumulated quantities, needed to normalize probability densities

## 2. [Linear algebra](../linear-algebra/)

The "language" of data and models — everything is vectors and matrices.

- **Scalars / vectors / matrices / tensors**: the ways data is organized
- **[Matrix multiplication](../matrix-multiplication/)**: linear transformations, the essence of every layer of a neural network
- **Transpose, inverse, rank**: describing the structure of a matrix
- **[Norms](../norm/)**: $\ell_1$ (sparsity), $\ell_2$ (energy / error) measure "size"
- **Eigenvalues and eigenvectors**: stability, principal directions
- **Matrix decompositions ([PCA](../pca/) / [SVD](../svd/))**: dimensionality reduction and compression

## 3. [Probability and statistics](../probability-statistics/)

Tools for reasoning and deciding under **uncertainty**.

- **[Random variables](../random-variable/) and probability distributions**: discrete / continuous; normal, Bernoulli, Poisson
- **Expectation, variance, covariance**: center, spread, co-movement
- **Conditional probability and [Bayes' theorem](../bayes-theorem/)**: updating beliefs with new evidence
- **Law of large numbers and central limit theorem**: why "averages" and "normal distributions" are everywhere
- **Estimation**: [maximum likelihood](../maximum-likelihood/) (MLE), maximum a posteriori (MAP)
- **Hypothesis tests and confidence intervals**: deciding whether "a difference is significant"

## 4. [Optimization](../optimization/)

"Learning = minimizing the [loss](../loss-function/)": optimization is the bridge between mathematics and machine learning.

$$\theta^\* = \arg\min_\theta \; \mathcal{L}(\theta)$$

- **[Convex vs non-convex](../convex-optimization/)**: whether a unique global optimum exists
- **[Gradient descent](../gradient-descent/)**: iterate downhill along the negative gradient, $\theta \leftarrow \theta - \eta\,\nabla\mathcal{L}$
- **Stochastic / mini-batch gradient descent (SGD)**: estimating the gradient from small batches of samples
- **Constrained optimization and Lagrange multipliers**: optimization subject to constraints

## 5. [Information theory](../information-theory/)

Measures "amount of information" and "difference between distributions"; the origin of deep learning [loss functions](../loss-function/).

- **[Entropy](../entropy/)**: a measure of uncertainty
- **[Cross-entropy](../cross-entropy/)**: the most common loss for classification tasks
- **[KL divergence](../kl-divergence/)**: the "distance" between two distributions
- **Mutual information**: how much information two variables share

---

**Key terms:** [gradient](../gradient/), [chain rule](../chain-rule/), [matrix multiplication](../matrix-multiplication/), [norm](../norm/), [SVD](../svd/), [random variable](../random-variable/), [Bayes' theorem](../bayes-theorem/), [maximum likelihood](../maximum-likelihood/), [convex optimization](../convex-optimization/), [gradient descent](../gradient-descent/), [entropy](../entropy/), [cross-entropy](../cross-entropy/), [KL divergence](../kl-divergence/).
