---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1988–89 · Computing"
permalink: /en/history/e/td-qlearning/
title: "Temporal Difference and Q-learning (Sutton · Barto · Watkins, 1988–89)"
lead: "No need to wait for the dust to settle before learning — by using \"the current prediction\" to correct \"the previous prediction\", an agent bootstraps its way step by step through a sequence towards future rewards."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

How can an agent learn to make good sequential decisions through repeated interaction with its environment? [Bellman's dynamic programming](../bellman-dp/) had long provided the equations of optimality, but it requires a **known model of the environment** (transition probabilities and rewards) and a sweep over the entire state space — in reality the model is often unknown and the state space far too large. On the other side, supervised learning requires a correct-answer label for every action, yet in sequential decision-making whether an action was good is often revealed only much later by the final outcome — **rewards are delayed**. Predicting future cumulative reward is itself a time series problem.

### The problem

The agent experiences only a sequence of "state–action–immediate reward", with rewards that are sparse and lagging. **How can it learn online to predict long-term reward, and choose optimal actions accordingly, without knowing the environment's model and without waiting until an entire episode is over?**

### Other approaches of the time (and their limits)

- **Dynamic programming ([Bellman](../bellman-dp/))**: theoretically optimal, but requires a known model and a sweep over the full state space; in practice the model is unknown and the dimensionality too high.
- **Monte Carlo methods**: wait until an episode ends, then update using the actual cumulative return. Unbiased, but learning must wait until the end, the variance is high, and it is ill-suited to continuing tasks.
- **Supervised learning**: needs correct labels at every step. In sequential tasks with delayed rewards, such labels simply cannot be obtained.

### Method

Sutton and Barto proposed **temporal-difference (TD) learning**: instead of waiting for the outcome, use **the prediction at the next moment** to correct **the prediction at this moment** — that is, bootstrapping. Let $$V(s)$$ be the value estimate of state $$s$$; after observing the immediate reward $$r_{t+1}$$ and the next state $$s_{t+1}$$, update by the **TD error**:

$$ V(s_t) \leftarrow V(s_t) + \alpha\,\big[\,\underbrace{r_{t+1} + \gamma\, V(s_{t+1}) - V(s_t)}_{\text{TD error }\delta_t}\,\big] $$

where $$\alpha$$ is the learning rate and $$\gamma\in[0,1)$$ the discount factor. The quantity in brackets is exactly the difference between "the current one-step prediction target" and "the old estimate"; it plays the role of a **prediction error** — the same idea as the innovation in [Yule](../yule-ar/)'s series and the prediction error in [system identification](../system-identification/). Watkins went further with **Q-learning**, which directly learns the state–action value $$Q(s,a)$$ and **needs no model of the environment**:

$$ Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha\,\Big[\, r_{t+1} + \gamma \max_{a} Q(s_{t+1},a) - Q(s_t,a_t)\,\Big] $$

The $$\max_a$$ in the formula lets it approach the solution of the Bellman optimality equation directly. Watkins proved that, under suitable conditions, Q-learning converges to the optimal action value $$Q^*$$ — a milestone of model-free optimal control.

### Impact

TD and Q-learning let an agent learn long-term rewards online from nothing but a stream of experience, with no model and no waiting for the end. They became the algorithmic core of reinforcement learning, underpinning a series of breakthroughs from TD-Gammon's backgammon to the later deep Q-networks (DQN) playing Atari, and AlphaGo.

### Significance and outlook

TD learning unified "predicting the future" and "learning from prediction errors" within sequential decision-making. Its bootstrapping idea is thought to match the reward-prediction-error signal of dopamine in the brain remarkably well, linking machine learning and neuroscience. In spirit it is akin to [MPC](../mpc/)'s "use predictions to guide the current decision" — except that one relies on a model and rolling optimization, the other on bootstrapped learning from experience. Learning to predict and control from delayed rewards remains, to this day, the engine of reinforcement learning and even of general-purpose agents.
