---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 2015–16 · Computing"
permalink: /en/history/e/deep-rl/
title: "Deep Reinforcement Learning (DQN · AlphaGo, 2015–16)"
lead: "When perceptual inputs are too high-dimensional for hand-designed features, can deep networks approximate value and policy directly? DQN and AlphaGo answered yes."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

Reinforcement learning (RL) studies **sequential decision-making**: at each moment an agent observes a state, takes an action and receives a reward, with the goal of maximizing long-term return. This is in essence a time-series problem: actions affect the future distribution of states, and returns span long time horizons. The classical framework is the **Markov decision process (MDP)**, combined with temporal-difference methods such as Watkins's **Q-learning** of 1989. But for decades these methods were mostly confined to toy problems with low-dimensional, enumerable states.

### The problem

In real tasks the state is often high-dimensional raw perception: a single game frame has tens of thousands of pixels, and Go has about $$10^{170}$$ board positions. Tabular Q-learning cannot store or generalize over such enormous state spaces, and hand-designed features are laborious and brittle. **Could a function approximator learn the value function or policy directly from raw inputs?** Early attempts to use neural networks for RL often diverged: the targets kept moving, the data were highly correlated, and training was extremely unstable.

### Other approaches of the time (and their limits)

- **Linear function approximation + hand-crafted features**: good theoretical convergence, but expressive power is limited by the hand-made features, making pixel-level inputs hard to handle.
- **Model-based planning (Monte Carlo tree search, MCTS)**: used on its own in Go, it lacked good position evaluation, its search depth was limited, and its playing strength stayed at amateur level.
- **Early forms of policy gradient**: high variance and low sample efficiency, hard to train stably on high-dimensional perceptual tasks.

### Method

**DQN** uses a convolutional network to approximate the action value $$Q(s,a;\theta)$$ and introduces two stabilizing tricks: **experience replay** (breaking up correlations between samples) and a **target network** (a frozen copy of the parameters $$\theta^-$$ that provides stable targets). It minimizes the temporal-difference error:

$$ L(\theta)=\mathbb{E}\Big[\big(r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta)\big)^2\Big] $$

where $$\gamma$$ is the discount factor and $$r+\gamma\max_{a'}Q(\cdot;\theta^-)$$ is the bootstrapped return target. **AlphaGo**, by contrast, embeds deep networks inside search: a policy network $$p(a\mid s)$$ narrows the breadth of the search, a value network $$v(s)$$ shortens its depth, and MCTS combines the two, maintaining for each edge

$$ Q(s,a)+u(s,a),\qquad u(s,a)\propto \frac{P(s,a)}{1+N(s,a)} $$

which balances exploitation (high $$Q$$) against exploration (high prior $$P$$, low visit count $$N$$).

### Impact

DQN reached or exceeded human-level performance on 49 Atari games using **the same network and hyperparameters**, with only screen pixels and the score as input. In 2016 AlphaGo beat Lee Sedol 4:1, the first program to defeat a top professional on a full 19×19 Go board. The following year AlphaGo Zero went further, surpassing all its predecessors through self-play alone, without any human game records.

### Significance and outlook

Deep reinforcement learning showed that **deep networks can serve as value and policy approximators in sequential decision-making**, pushing RL from low-dimensional tables to high-dimensional raw perception. At its core it is kin to time series: both use the past to predict, and to optimize, the future. This thread leads on to later policy optimization, world models, and the paradigm of aligning large models ([../foundation-models/](../foundation-models/)) with RL. When we let an agent "learn to decide by watching the screen", the skeleton is still Q-learning's temporal difference plus this step of deep approximation.
