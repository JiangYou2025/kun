---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/reinforcement-learning/
title: "Reinforcement Learning"
no_comments: true
math: true
---

> Part of [Machine Learning Fundamentals](../ml/) · [Foundations overview](../)

**Reinforcement Learning (RL)** is the third major paradigm of [machine learning](../ml/): an **agent** keeps interacting with an **environment** and adjusts its behaviour according to the **rewards** it receives, with the goal of learning a **policy** that **maximizes the long-term cumulative reward**.

## Intuition

Imagine you are **training a puppy**. You don't hand it a manual; instead, when it does the right thing (sits down) it gets a treat, and when it does the wrong thing it gets nothing. Over time the puppy "figures out" on its own that "sit → treat", and sits down more and more readily.

Reinforcement learning is exactly this kind of **trial and error** learning:

- No one tells the agent "what the right answer is" (this is where it differs fundamentally from supervised learning);
- It can only find its way by **trying actions, observing the consequences, and collecting rewards**;
- And the reward is often **delayed** — you cannot tell whether a step was good or bad until several steps later.

This is precisely what makes reinforcement learning both fascinating and hard: from **delayed, sparse feedback** it must learn the wisdom behind a long chain of decisions.

## Principle: the RL framework

Reinforcement learning abstracts the problem as a loop between the agent and the environment:

1. The agent observes the current **state** $s$;
2. It picks an **action** $a$ according to its **policy** $\pi(a\mid s)$;
3. The environment returns a **reward** $r$ and a new state $s'$;
4. Go back to step 1 and repeat.

$$ s_0 \xrightarrow{a_0} (r_1, s_1) \xrightarrow{a_1} (r_2, s_2) \xrightarrow{a_2} \cdots $$

The **goal** is not to maximize the immediate $r$, but the **cumulative discounted reward** from now on, called the **return**:

$$ G_t = \sum_{k\ge 0} \gamma^k\, r_{t+k} = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots $$

Here $\gamma\in[0,1]$ is the **discount factor**: the closer $\gamma$ is to 1, the more "far-sighted" the agent is and the more it values the future; the closer to 0, the more "short-sighted" it is, caring only about the present.

To measure "how good it is to be in a given state", we introduce the **value function**:

$$ V^\pi(s) = \mathbb{E}_\pi[\,G_t \mid s_t = s\,] $$

It gives the average return obtained by starting from state $s$ and acting according to policy $\pi$. A finer-grained version is the **action-value function** $Q^\pi(s,a)$, the expected return of "taking action $a$ in state $s$ first, then following $\pi$". At the heart of many [algorithms](../algorithms/) is the idea of **estimating $Q$ and then, at every step, picking the action with the largest $Q$**.

This whole mathematical framework has a name: the **Markov Decision Process (MDP)** — "Markov" meaning that "the future depends only on the current state, not on how you got there".

## A concrete example: solving a maze

Picture a robot looking for the exit of a maze:

- **State** $s$: the cell the robot is currently in;
- **Action** $a$: up, down, left, right;
- **Reward** $r$: $-1$ for hitting a wall, $-0.1$ per step (to encourage shortcuts), $+10$ for reaching the exit;
- **Policy** $\pi$: which way to go from each cell.

At first the robot bumps around at random, but once it has reached the exit and collected the $+10$, that "benefit" **propagates backward cell by cell** through the value function, gradually raising the value of cells close to the exit. After many rounds, the robot has learned a nearly optimal route. This is what algorithms such as **Q-learning** do.

## Exploration and exploitation

Reinforcement learning has an unavoidable dilemma — the **exploration vs exploitation** tradeoff:

- **Exploitation**: choose the best action known so far and collect the reward safely;
- **Exploration**: try actions you haven't tried yet, which might reveal a better path.

Exploiting without exploring can leave you stuck in a suboptimal solution; exploring without exploiting means you never learn a stable policy. A common approach is **ε-greedy**: with a small probability $\varepsilon$ explore at random, and the rest of the time exploit the best action.

## Comparison with the other paradigms

Reinforcement learning is quite different from the two paradigms you have already met:

- Versus [supervised learning](../supervised-learning/): supervised learning has ready-made **labels** (every input has a reference answer); RL has **no labels**, only **delayed rewards**, and its own actions influence the data it sees next.
- Versus [unsupervised learning](../unsupervised-learning/): unsupervised learning looks for **structure** in unlabelled data ([clustering](../clustering/), dimensionality reduction), whereas RL learns **how to act**, guided by a **reward signal**.

Common algorithms and milestones: tabular **Q-learning**, **policy gradient** methods that optimize the policy directly, **DQN**, which approximates $Q$ with a [neural network](../neural-network/), and **AlphaGo**, which beat the human Go champion — all products of reinforcement learning ideas.

## Relevance to time series forecasting

To be frank: **for the task of "simply predicting future values", reinforcement learning is rarely used** — forecasting is essentially **supervised learning** (historical data as inputs, the actual future values as labels).

Where reinforcement learning really comes in is in downstream problems of **making a sequence of decisions based on forecasts**, which naturally have the structure "actions affect the future, rewards arrive late":

- **Trading / portfolios**: decide buys, sells and positions from market forecasts; profit and loss is the reward;
- **Inventory / replenishment**: after forecasting demand, decide how much stock to order; both stockouts and overstock are costs;
- **Dynamic pricing**: adjust prices in real time from demand forecasts; revenue is the reward;
- **Resource scheduling**: allocate compute/power according to load forecasts.

In these settings, "forecasting" is the upstream **perception**, while reinforcement learning handles the downstream **action**. Two caveats, though: RL usually needs a **simulator/environment** for repeated trial and error (random experimentation in the real world is too costly), and it is **very data-hungry**.

In one sentence: **use supervised learning to forecast; consider reinforcement learning only for acting on the forecasts**.

## Summary

- Reinforcement learning = an agent learns a **policy** through **trial-and-error interaction** with an environment, maximizing the **long-term cumulative reward**.
- Core elements: state $s$, action $a$, reward $r$, policy $\pi(a\mid s)$, return $G_t=\sum_k \gamma^k r_{t+k}$, value functions $V^\pi/Q^\pi$.
- Its mathematical backbone is the **Markov Decision Process (MDP)**; its central difficulty is the **exploration–exploitation tradeoff**.
- Key difference from supervised learning: **no labels, only delayed rewards**, and actions change the future data.
- In time series: **forecasting relies on supervised learning, while decision problems that "act on the forecasts" — trading, replenishment, pricing — are where RL shines**.

Further reading: [Supervised learning](../supervised-learning/) · [Unsupervised learning](../unsupervised-learning/) · [Linear models](../linear-model/) · [Decision trees](../decision-tree/) · [Ensembles / GBDT](../ensemble-gbdt/) · [SVM](../svm/)

---

[← Machine Learning Fundamentals](../ml/) · [Foundations overview](../)
