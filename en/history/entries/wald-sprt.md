---
updated: "2026-06-14"
layout: history
lang: en
era: "Timeline entry · 1945 · Mathematics"
permalink: /en/history/e/wald-sprt/
title: "Testing While Watching (Wald, 1945)"
lead: "No need to fix the sample size in advance — accumulate evidence with each new data point and conclude only when it crosses an upper or lower threshold. Sequential analysis saves samples and planted the seed of change-point detection."
math: true
---

> This is an entry in the timeline of the [history of time series](../../), part of [Prologue · Interdisciplinary Origins](../../foundations/).

### Background

During the Second World War, quality inspection in military production faced a practical pressure: sampling inspection was often destructive, so the fewer samples the better. The classical Neyman–Pearson test requires **fixing the sample size $$n$$ in advance** and then deciding in one go. Working in the wartime Statistical Research Group, Abraham Wald proposed a radically different paradigm — **sequential analysis**: let the sample size itself be a random variable, and decide as the data arrive. The sequential probability ratio test (SPRT), published in 1945, was the culmination of this idea.

### The problem

We must choose between two simple hypotheses $$H_0:\theta=\theta_0$$ and $$H_1:\theta=\theta_1$$, controlling the two error probabilities at $$\alpha,\beta$$. **Instead of fixing the sample size beforehand, can we decide after each new observation whether to "accept, reject, or look at one more", and so achieve the same error control with as few observations as possible?**

### Other approaches of the time (and their limits)

- **Fixed-sample-size Neyman–Pearson tests**: theoretically elegant with controllable error rates, but the sample size is set uniformly for the worst case, wasting many observations on average — costly in destructive testing.
- **Stopping early by experience**: the inspector watches the data and "stops when it looks good enough". This silently changes the actual error rate (the multiple-looks problem), distorting the nominal $$\alpha$$, with no theoretical guarantee.
- **Purely Bayesian posterior updating**: continuously updating the posterior is the right direction, but at the time there was no operational rule tying "when to stop, and which way to decide when stopping" to frequentist error control.

### Method

The SPRT accumulates the **log-likelihood ratio** one observation at a time. For independent observations $$x_1,x_2,\dots$$, define the cumulative statistic

$$ \Lambda_n=\sum_{i=1}^{n}\log\frac{f_{\theta_1}(x_i)}{f_{\theta_0}(x_i)} $$

Set two thresholds $$A=\log\dfrac{1-\beta}{\alpha},\quad B=\log\dfrac{\beta}{1-\alpha}$$ (so $$B<0<A$$). The stopping rule is:

$$ \text{if }\Lambda_n\ge A\Rightarrow\text{accept }H_1;\quad \Lambda_n\le B\Rightarrow\text{accept }H_0;\quad B<\Lambda_n<A\Rightarrow\text{take another observation} $$

This is an **optimal stopping** problem: the Wald–Wolfowitz theorem proves that, for given $$\alpha,\beta$$, the SPRT **simultaneously minimizes the expected sample size** under both hypotheses. $$\Lambda_n$$ is a random walk, the thresholds are absorbing barriers, and the average number of steps required can be estimated with Wald's identity.

### Impact

For the same error control, sequential tests typically need **about half** the average sample size of fixed-sample tests. More importantly, they brought into statistics the dynamic paradigm of "evidence accumulating over time, acting only once a threshold is crossed". Summing log-likelihood ratios is precisely the core of the later **cumulative sum (CUSUM) control chart**: reading "has something changed?" off the data stream in real time.

### Significance and outlook

Wald's cumulative log-likelihood ratio plus thresholds is the source of **change-point detection** and online monitoring. Let $$\Lambda_n$$ wander under the hypothesis that "the process is still normal", raise an alarm the moment it crosses the boundary, and you obtain Page's (1954) CUSUM and the prototype of modern streaming anomaly detection. From industrial quality control to structural breaks in financial markets, from network intrusion detection to real-time monitoring of time series, the idea of "accumulating evidence as you watch, and deciding optimally when to stop" traces all the way back to this step Wald took in 1945.
