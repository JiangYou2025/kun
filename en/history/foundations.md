---
updated: "2026-06-01"
layout: history
lang: en
era: "Prologue · Interdisciplinary roots (1900–today)"
permalink: /en/history/foundations/
title: "Interdisciplinary Roots: Mathematics, Physics, Cybernetics and Modern Crossovers"
lead: "Time-series methods did not come out of nowhere: they arose from the confluence of several currents — mathematics, statistical physics, control and communication engineering — and extend all the way to sequential decision-making and scientific computing. This chapter traces these roots discipline by discipline: each thread starts from the foundations laid in the early 20th century, yet each reaches into the present day."
math: true
next: /history/01/
---

In the first half of the 20th century, three seemingly unrelated fields independently took up "quantities that evolve randomly over time": mathematicians sought rigorous foundations and limit theorems for stochastic processes; physicists described systems driven by random forces, such as Brownian motion; communication and control engineers needed to predict signals in noise and design feedback. They eventually converged on a common language — the stationary stochastic process — which became the bedrock of time-series analysis.

---

## I. Mathematicians: making "stochastic processes" rigorous

Early statistics could only describe data; it lacked a rigorous probabilistic foundation. By what right can we use a **single** observed trajectory to estimate the mean and correlations of the entire process? To answer that, one must first define the "stochastic process" itself. This thread was carried out by a group of mathematicians, many of whom were driven precisely by **randomness in finance and gambling** — mathematical finance and stochastic processes have been one and the same story from the very beginning.

**Kolmogorov (1933): axiomatization and the ergodic theorem.** Kolmogorov axiomatized probability through measure theory, laying the foundation for stochastic processes; his **forward/backward equations** (Kolmogorov forward/backward equations) extended discrete Markov chains to continuous diffusion processes, giving continuous-time processes such as Brownian motion rigorous analytical tools. Combined with **ergodic theory** (Birkhoff, von Neumann), we obtain the crucial guarantee — for an **ergodic stationary process**, the time average converges to the ensemble (expected) average:

$$ \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T} f(X_t) \;=\; \mathbb{E}\big[f(X)\big]\quad \text{(a.s.)} $$

The left-hand side is the sample average over the **one and only** series we have in hand; the right-hand side is the theoretical expectation. The ergodic theorem guarantees they are equal — this is the fundamental mathematical premise that makes "estimating autocorrelation, mean and variance from historical data" legitimate. Without it, statistical inference as a whole would have no footing.

**Markov: memorylessness, the backbone of everything.** The "Markov property" proposed by **Markov** (1906) — the future depends only on the present, not on the more distant past —

$$ \Pr(X_{t+1}\mid X_t, X_{t-1},\dots) = \Pr(X_{t+1}\mid X_t) $$

compresses a high-dimensional history into a single "current state", with transitions chained together by the **Chapman–Kolmogorov equation** $$P_{t+s}=P_t\,P_s$$. This "memoryless" assumption is the most deeply hidden and most widely reused skeleton in time series: it underpins **AR / state-space models and the Kalman filter** ([Chapter 4](../04/)), **hidden Markov models (HMMs)** for speech and sequence labeling, **Markov decision processes** for sequential decision-making (see reinforcement learning in Section IV below), and **MCMC** in modern Bayesian computation. A single phrase — "the future looks only at the present" — runs through the next hundred years.

**Bachelier (1900): the birth of mathematical finance.** Five years before Einstein, the French mathematician **Louis Bachelier**, in his doctoral thesis *Théorie de la spéculation* (The Theory of Speculation), modeled stock prices for the first time with a **random walk / Brownian motion**, writing the price as a sum of independent random increments:

$$ S_t = S_0 + \sigma W_t,\qquad W_t-W_s\sim\mathcal N(0,\,t-s) $$

From this he concluded that "the best forecast of the price is the current price" — the embryo of the **martingale** and of the later **efficient market hypothesis** — and derived results strikingly close to modern option pricing. This was both the **founding work of mathematical finance** and the first mathematical model of Brownian motion (for its physical counterpart, see Einstein in the next section).

**Lévy: independent increments and heavy tails.** **Paul Lévy** systematically studied **processes with independent stationary increments** (**Lévy processes**, of which Brownian motion and the Poisson process are special cases), characterized their distributions through **characteristic functions**, and gave the general form of the **stable distribution**:

$$ \log \mathbb{E}\,e^{i u X} = i\gamma u - \tfrac12\sigma^2 u^2 + \int_{\mathbb R}\big(e^{iux}-1-iux\,\mathbf 1_{|x|<1}\big)\,\nu(dx) $$

The final jump measure $$\nu$$ allows for **heavy tails** and sudden jumps — explaining why real financial returns are far more "fat-tailed" than the normal distribution and why extreme swings occur so often, and directly foreshadowing the [ARCH/GARCH volatility models of the 1980s](../06/) and jump-diffusions. Lévy was also one of the founders of **martingale** theory.

**Doob (1953): a martingale is a fair game.** In *Stochastic Processes*, **Joseph Doob** developed the **martingale** into a complete theory. A martingale is a "fair game" — the conditional expectation of the next value is exactly the current value:

$$ \mathbb{E}\big[X_{t+1}\mid \mathcal F_t\big] = X_t $$

Its financial meaning runs deep: if discounted prices are a martingale, then **no predictable, stable arbitrage exists**. The **Doob decomposition** splits any sequence into "predictable trend + martingale", which is precisely the probabilistic version of the time-series decomposition into "signal + unpredictable innovation"; the **optional stopping theorem** became a tool for exercising American options and for sequential decision-making. The martingale thus became the mathematical core of the **efficient market hypothesis** and **arbitrage-free pricing**.

**Itô (1944/1951): stochastic calculus.** Ordinary calculus breaks down on Brownian motion — $$W_t$$ is nowhere differentiable and its quadratic variation is not zero ($$d\langle W\rangle_t = dt$$). **Kiyoshi Itô** invented **stochastic calculus** and gave the famous **Itô's lemma**: for a diffusion $$dX_t=\mu\,dt+\sigma\,dW_t$$,

$$ df(X_t)=\Big(f_t+\mu f_x+\tfrac12\sigma^2 f_{xx}\Big)dt+\sigma f_x\,dW_t $$

That extra term $$\tfrac12\sigma^2 f_{xx}$$ (coming from the quadratic variation) is exactly the watershed between stochastic and classical calculus. Using it to solve **geometric Brownian motion** $$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$$ gives

$$ S_t=S_0\exp\!\Big[(\mu-\tfrac12\sigma^2)\,t+\sigma W_t\Big] $$

— the engine of **Black–Scholes (1973) option pricing** and of nearly every continuous-time financial model.

**Khinchin: time domain and frequency domain.** Khinchin went on to give the **Wiener–Khinchin theorem**: the autocovariance $$\gamma_k$$ and the power spectrum $$S(\omega)$$ of a stationary process form a Fourier-transform pair:

$$ S(\omega)=\sum_{k=-\infty}^{\infty}\gamma_k\, e^{-i\omega k} $$

It makes "correlation structure in the time domain" equivalent to "energy distribution in the frequency domain": periodicities hidden in a series show up as peaks in the spectrum $$S(\omega)$$. This is the theoretical cornerstone of **spectral analysis** (periodograms, harmonic analysis).

Stationarity, ergodicity and spectral representation — these three mathematical tools lifted time series from "empirical description" to "a theory of stochastic processes that supports inference".

**From stochastic processes to financial mathematics, and back to time series.** This machinery — Bachelier's random walk, Lévy's heavy tails, Doob's martingales, Itô's stochastic calculus — bore fruit in the 1970s as **mathematical finance**: geometric Brownian motion + Itô's lemma gave **Black–Scholes–Merton option pricing**, the Ornstein–Uhlenbeck process gave the **Vasicek interest-rate model**, and Harrison–Kreps–Pliska (1979–81) used **equivalent martingale measures** to prove that "no arbitrage ⟺ there exists a measure under which discounted prices are martingales", establishing the **fundamental theorem of asset pricing**. Back in discrete-time series, the same ideas reappear in another language: **random walk / martingale → unit roots and tests of market efficiency** (ADF and cointegration in [Chapter 6](../06/)), **OU process → mean reversion in AR(1)**, **Lévy heavy tails → volatility clustering and ARCH/GARCH**, **Mandelbrot's fractional Brownian motion and long-range dependence → ARFIMA long-memory models**. Mathematical finance and time series are two branches of one and the same tree of stochastic processes.

**New mathematics for the 21st century: paths, signatures and roughness.** Stochastic analysis did not stop there. The **Feynman–Kac formula** (Kac, 1949, derived from Feynman's **path integral**) writes the solution of a parabolic PDE as an expectation over random paths, making the Black–Scholes PDE and martingale pricing two sides of the same coin; **Malliavin calculus** (1976) developed tools for "differentiating with respect to randomness", used to characterize the densities of SDE solutions and to compute hedging sensitivities (the Greeks). In the 21st century, **Terry Lyons's theory of rough paths (1998)** provided a rigorous framework for differential equations driven by highly irregular signals; its central object is the path's **signature** — a sequence of iterated-integral tensors:

$$ S(X)_{0,t} = \Big(\,1,\ \int dX,\ \iint dX\otimes dX,\ \iiint dX\otimes dX\otimes dX,\ \dots\Big) $$

It encodes a trajectory as a **universal feature**: any functional of the path can be approximated linearly from its signature. This line now feeds directly back into machine learning for time series — **signature kernels** and **Neural CDEs / neural rough differential equations** (Kidger, Salvi, Cass, Oberhauser and others, 2020s) use it to handle **irregularly sampled sequences with missing values** elegantly; and **rough volatility (Gatheral–Jaisson–Rosenbaum, 2014–2018)** discovered that the trajectory of market volatility is in fact a **fractional Brownian motion** with Hurst exponent $$H<\tfrac12$$, bringing Mandelbrot's half-century-old intuitions about heavy tails and long memory back to the cutting edge of financial modeling. From Bachelier's random walk to Lyons's signatures, the mathematical thread of stochastic processes continues to supply a steady stream of new tools for today's time series.

---

## II. Physicists: stochastic dynamics, chaos and scaling laws

How do you write equations for a system that is **continually perturbed by random forces** yet has an intrinsic tendency to return (a suspended particle, a voltage in thermal noise)?

Following Bachelier's random walk of prices (see the previous section), Einstein and Smoluchowski (1905) developed the theory of Brownian motion, which corresponds mathematically to the **Wiener process** (independent Gaussian increments $$W_t-W_s\sim\mathcal N(0,\,t-s)$$). Langevin (1908) wrote down an equation with a friction term and a random force:

$$ m\frac{dv}{dt} = -\gamma\, v + \eta(t) $$

Ornstein–Uhlenbeck (1930) recast it as a mean-reverting stochastic differential equation:

$$ dX_t = -\theta X_t\, dt + \sigma\, dW_t $$

$$-\theta X_t$$ is the deterministic restoring force pulling $$X$$ back toward its mean, and $$\sigma\,dW_t$$ is the random perturbation. Discretizing it with step $$\Delta$$ yields exactly the most familiar model in statistics, **AR(1)**:

$$ X_t = \phi X_{t-1} + \varepsilon_t,\qquad \phi=e^{-\theta\Delta} $$

In other words, the physicist's "friction + thermal noise" and the statistician's "autoregression" are **two languages for the same thing**. The closer $$\phi$$ is to 1, the slower the reversion and the longer the memory.

This line leads directly to interest-rate models in finance (Vasicek) and to mean-reversion strategies in pairs trading, and it made stochastic differential equations the standard tool for continuous-time time series.

But **after 1930**, physicists' contributions to time series went far beyond "mean reversion". They brought three entirely new worldviews: **deterministic chaos**, **scaling laws and long-range memory**, and **treating dynamical systems as linear operators**.

**Deterministic chaos: a random appearance, a deterministic core.** In 1963, the meteorologist **Edward Lorenz** discovered in a simplified convection model that three completely deterministic equations

$$ \dot x=\sigma(y-x),\qquad \dot y=x(\rho-z)-y,\qquad \dot z=xy-\beta z $$

could produce trajectories that **never repeat and are extremely sensitive to initial conditions** — "the flap of a butterfly's wings in Brazil may set off a tornado in Texas". Two neighboring trajectories separate exponentially as $$|\delta(t)|\approx|\delta_0|\,e^{\lambda t}$$ (with $$\lambda$$ the largest Lyapunov exponent), which sets a **fundamental horizon** on prediction: even with a perfect model, errors grow exponentially. Chaos gave time-series researchers a subversive insight — **a seemingly random series may be driven by a low-dimensional deterministic system** rather than by a stochastic process.

**Reconstructing the whole system from one series: Takens embedding.** In 1981, **Floris Takens**'s **delay embedding theorem** reached a startling conclusion: from **univariate** observations $$x_t$$ alone, build the delay coordinates

$$ \mathbf y_t=\big(x_t,\,x_{t-\tau},\,x_{t-2\tau},\dots,x_{t-(m-1)\tau}\big) $$

and as long as the embedding dimension $$m$$ is large enough ($$m>2d$$, with $$d$$ the dimension of the attractor), $$\mathbf y_t$$ is **diffeomorphic** to the attractor of the original system — a single scalar time series fully preserves the geometry of a multidimensional dynamical system. From this grew an entire field of **nonlinear time-series analysis**: **Grassberger–Procaccia (1983)** used the correlation integral $$C(r)\sim r^{D_2}$$ to estimate the **correlation dimension** and judge whether a system is low-dimensional; **Lyapunov exponents** estimated directly from data measure the strength of chaos; **Farmer–Sidorowich (1987)** and **Sugihara–May (1990)** used local nearest neighbors for **nonlinear prediction** and, on that basis, distinguished "chaos" from "pure noise". This current met neural networks head-on at the **1992 Santa Fe Time Series Prediction Competition** and became one of the sources of modern nonlinear forecasting.

**Scaling laws and long-range memory: 1/f noise and fractals.** Physicists noticed early on that **long-range correlation** and **scale invariance** are ubiquitous in nature. The hydrologist **Hurst (1951)** found in Nile water levels that the rescaled range satisfies $$\mathbb E[R(n)/S(n)]\sim n^{H}$$, where $$H>\tfrac12$$ signals **long memory** far beyond what independence would allow — the empirical starting point of Mandelbrot's **fractional Brownian motion** (covariance $$\propto|t|^{2H}+|s|^{2H}-|t-s|^{2H}$$). The **1/f noise** found everywhere in physics (power spectrum $$S(f)\sim f^{-\beta}$$) is the frequency-domain face of the same phenomenon. **Peng et al. (1994)** proposed **detrended fluctuation analysis (DFA)**: $$F(n)\sim n^{\alpha}$$, still a standard tool for extracting long-range correlation from heart rates, DNA and financial series, and one that supplied physical intuition for the **long-memory ARFIMA** models and fractional differencing of [Chapter 6](../06/).

**Econophysics: treating markets as statistical-mechanical systems.** In the 1990s, **Mantegna and Stanley** and others founded **econophysics**, using the scaling, power laws and critical phenomena of statistical mechanics to study financial series and characterize the **fat tails**, **volatility clustering** and **multifractality** of returns; **Bouchaud** and others modeled markets in the language of interacting particles and disordered systems. They arrive at the same place as [GARCH](../06/) by a different road, but try to answer "why".

**Linearizing nonlinear dynamical systems: the Koopman operator.** The last thread goes back to an insight of **Koopman (1931)**: rather than tracking the nonlinear state, observe the **linear** operator acting on **observable functions**, $$(\mathcal K g)(x)=g(F(x))$$. After lying dormant for decades, it was revived by **Mezić (2005)** and put into practice through **dynamic mode decomposition (DMD, Schmid 2010)** — extracting **coherent modes and frequencies** from high-dimensional time series (fluids, video, sensor networks), turning "nonlinear prediction" back into a "linear spectral problem"; today it is being combined with deep learning (Koopman autoencoders).

What physicists left to time series is a worldview quite different from that of statistics: a series is not necessarily a sample of a stochastic process; it may also be **the projection of deterministic chaos**, **the scaling of a critical system**, or **a low-dimensional observation of high-dimensional dynamics**.

---

## III. Cybernetics and communication engineering: from filtering to deep state spaces

Wartime anti-aircraft fire control needed to **predict in real time** an aircraft's future position from noisy radar echoes — an engineering problem of optimal prediction and filtering in noise.

In *Cybernetics* (1948), Norbert Wiener unified feedback, information and prediction as "cybernetics", and gave the frequency-domain **Wiener optimal linear filter** (the Wiener–Hopf solution):

$$ H(\omega) = \frac{S_{xy}(\omega)}{S_{xx}(\omega)} $$

$$S_{xx}$$ is the power spectrum of the input (signal + noise), and $$S_{xy}$$ is the cross-spectrum between input and target. The formula designs the filter from "the ratio of signal to noise energy at each frequency": bands with a high signal-to-noise ratio are kept, bands dominated by noise are suppressed — the origin of modern signal processing.

In the same year as Wiener, **Shannon (1948)**'s **information theory** introduced entropy, channel capacity and the **Nyquist–Shannon sampling theorem**, establishing the informational limits of "signal — noise — prediction". Its direct descendants are **linear predictive coding (LPC)** — compressing speech with AR models (Itakura, Atal, 1970s) — and the **Viterbi algorithm (1967)**: optimal decoding over hidden Markov models and convolutional codes by dynamic programming, still a pillar of speech recognition and communications today.

Engineering then developed **system identification** (Åström, Ljung and others, 1970s–80s): fitting dynamic models (ARX, ARMAX) directly from input–output data, arriving by a different road at the same place as the Box–Jenkins approach in statistics. In fact, Box himself came from a chemical-engineering and quality-control background, and the subtitle of his famous book is *Forecasting and **Control***.

But cybernetics' contribution to time series did not stop in the 1980s — quite the opposite: **many of the latest advances bear the stamp of control theory**.

**Nonlinear, non-Gaussian filtering: from the EKF to particle filters.** The Kalman filter assumes linearity and Gaussianity; reality is often neither. Engineers first used the **extended Kalman filter (EKF)** and the **unscented Kalman filter (UKF, Julier–Uhlmann 1997)** for local linearization, then **particle filters / sequential Monte Carlo** (Gordon–Salmond–Smith 1993) approximated **arbitrary** posterior distributions with a swarm of weighted samples, freeing themselves entirely from the Gaussian assumption; the **ensemble Kalman filter (EnKF, Evensen 1994)** and **4D-Var** became the core of **data assimilation** in numerical weather prediction — fusing tens of millions of observations into the model state in real time, which connects directly to the spatiotemporal forecasting of Section V below.

**Controlling by predicting: model predictive control (MPC).** In the 1970s–80s, industry introduced **MPC** (DMC, Cutler–Ramaker 1980): at each step, use a dynamic model to **predict a stretch ahead**, solve for the optimal future control sequence, apply only the first step, then roll forward and repeat. It embeds "time-series forecasting" directly into closed-loop decision-making and still dominates chemical engineering, energy and robotics; **subspace identification (N4SID, Van Overschee–De Moor 1994)** estimates state-space matrices directly from data.

**The 2000s: bridging past and future.** In the 21st century, control and signal processing kept pushing the boundaries of time series: **echo state networks / reservoir computing (Jaeger 2001; Jaeger–Haas 2004)** use a randomly fixed dynamical "reservoir" plus a single linear readout to predict chaotic series at very low training cost, injecting dynamical-systems intuition into recurrent networks; **compressed sensing (Donoho, Candès–Romberg–Tao, 2006)** proved that sparse signals can be reconstructed exactly from far fewer samples than Nyquist requires, reshaping signal acquisition and denoising; **particle MCMC (Andrieu–Doucet–Holenstein, 2010)** embedded sequential Monte Carlo inside MCMC, making parameter inference for nonlinear state-space models feasible. These works carry on the state-estimation tradition of Kalman and particle filtering and lay the groundwork for the next wave of "deep state spaces".

**The return of cybernetics: deep state-space models (S4, Mamba).** The most striking "new development" is the revival of control-theoretic ideas within deep learning. **HiPPO (Gu et al., 2020)** used optimal polynomial projections to derive a continuous-time state equation $$\dot{\mathbf x}(t)=A\mathbf x(t)+B u(t)$$ that compresses long histories online; **S4 (2021)** discretized this **linear state-space model (SSM)** into a deep layer that can be computed efficiently with the FFT, overtaking Transformers on **very long sequence** benchmarks; **Mamba (2023)** went further by introducing **selectivity** (letting $$A,B,C$$ vary with the input) and a linear-time scan, becoming one of the workhorses of long-sequence modeling. The state space Kalman wrote down in 1960 has, after a sixty-year detour, returned to the forefront of time series — only this time the matrices are no longer derived from physics but **learned** by gradient descent.

The core ideas that cybernetics left to time series — **state space + recursive filtering** (brought together by Kalman in [Chapter 4](../04/)), **feedback and online updating**, and **closing the decision loop with prediction** — carried time series from "offline fitting" all the way to "real-time, adaptive and controllable". And one step beyond "feedback" lies **decision**: what to do while the series has not yet ended is the subject of the next section.

---

## IV. Sequential decision-making: optimal stopping and reinforcement learning

The theme of the first three sections was **prediction** — given the past, estimate the future. But time series also raise another question: while the series is still unfolding, **when to act, and what action to take**, to be optimal? This thread of "sequential decision-making" likewise spans mathematics, control and computer science.

**Wald (1945): sequential analysis and optimal stopping.** For wartime quality inspection, **Abraham Wald** introduced **sequential analysis** and the **sequential probability ratio test (SPRT)**: instead of fixing the sample size in advance, decide after each observation whether to "accept / reject / look at one more". This opened the problem of **optimal stopping** — together with Doob's martingales and the **Snell envelope**, one can prove "where to stop" so as to maximize expected payoff. The **exercise of American options** in finance and **change-point detection** in industrial monitoring are its direct descendants.

**Robbins (1952): the multi-armed bandit.** **Herbert Robbins**'s "sequential design of experiments" introduced the **multi-armed bandit**: trading off between "exploiting the known best" and "exploring the unknown" so as to minimize cumulative **regret**; the **Gittins index (1979)** gave the optimal policy in tractable cases. This is the theoretical core of online learning, A/B testing and recommender systems.

**Bellman (1957): dynamic programming and Markov decision processes.** **Richard Bellman** generalized sequential decision-making into the **Markov decision process (MDP)**, solved by **dynamic programming**, whose core is the **Bellman optimality equation**:

$$ V^*(s)=\max_{a}\Big[\,r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\,V^*(s')\,\Big] $$

It breaks "long-run optimality" recursively into "current reward + discounted future optimum", and is the common foundation of optimal control and reinforcement learning — growing directly out of the memoryless assumption of **Markov** in Section I.

**Reinforcement learning: from TD to AlphaGo.** When the environment model $$P$$ is unknown, **Sutton and Barto**'s **temporal-difference learning (TD, 1988)** and **Watkins's Q-learning (1989)** let an agent approximate $$V^*$$ and $$Q^*$$ directly from experience by **bootstrapping**; with deep networks as function approximators, **DQN (2015)** on Atari and **AlphaGo (2016)** on Go ignited **deep reinforcement learning**. For time series, RL upgrades "prediction" to "decision": trade execution, inventory replenishment, dynamic pricing, and even using RL to **fine-tune forecasting models themselves**.

---

## V. When time series become fields: PDEs, simulation and neural operators

Generalize a one-dimensional time series to a **field that evolves over time** (a temperature field, a velocity field, a price surface), and what describes it is no longer an ODE/SDE but a **partial differential equation (PDE)**. The most famous is the **Navier–Stokes equation** describing fluids:

$$ \frac{\partial \mathbf u}{\partial t}+(\mathbf u\cdot\nabla)\mathbf u=-\frac1\rho\nabla p+\nu\nabla^2\mathbf u+\mathbf f $$

Weather, oceans, turbulence, structural stress — these spatiotemporal dynamics have traditionally been solved by **numerical simulation**: finite differences / finite elements / spectral methods, the core of CFD and CAD/engineering simulation. But the finer the mesh, the more expensive the computation.

Machine learning offers a new path: **physics-informed neural networks (PINNs, Raissi 2019)** write the PDE residual directly into the loss and fit the solution with a network; **neural operators** — **DeepONet (Lu, 2019)** and the **Fourier neural operator (FNO, Li, 2020)** — go further, learning a **mapping from functions to functions** $$\mathcal G:a\mapsto u$$ (parameters/initial and boundary conditions ↦ solution), and once trained can roll out an entire spatiotemporal evolution far faster than numerical solvers. The culmination is **data-driven weather forecasting**: **FourCastNet (2022)**, **GraphCast (2023)** and **Pangu-Weather** use a single network to produce medium-range forecasts that rival or even surpass traditional numerical models — essentially **spatiotemporal time-series forecasting at global scale**.

This thread meets the book's main line in [Chapter 10](../10/): KUN's ideas of **hierarchical, multi-scale, pluggable kernels** share the same lineage as the neural operator's aim of handling multi-scale spatiotemporal structure.

---

## The confluence of currents

| Source | Key figures | Contributions | Legacy for time series |
|------|----------|------|----------------------|
| Mathematics | Bachelier, Kolmogorov, Lévy, Doob, Itô, Lyons | Random walk, axiomatization of probability, martingales, stochastic calculus, spectral representation, rough paths and signatures | Stationarity, inferability, efficient markets / no arbitrage, continuous-time finance, universal features of sequences |
| Physics | Einstein, Langevin, Uhlenbeck, Lorenz, Takens, Hurst | Brownian motion, stochastic differential equations, deterministic chaos, delay embedding, scaling laws | Continuous-time models, physical meaning of AR(1), nonlinear dynamical prediction, long-range correlation |
| Control / communications | Shannon, Wiener, Kalman, Gordon, Gu | Information theory, optimal/nonlinear filtering, state space, MPC, deep SSMs | Recursive estimation, data assimilation, model predictive control, S4/Mamba |
| Sequential decision-making | Wald, Robbins, Bellman, Sutton·Barto | Optimal stopping, multi-armed bandits, dynamic programming, reinforcement learning | Sequential testing, change-point detection, decision-oriented forecasting |
| Spatiotemporal / scientific computing | Navier–Stokes, Raissi, Lu, Li | PDEs, numerical simulation, PINNs, neural operators | Spatiotemporal forecasting, data-driven weather/fluid prediction |

> The rigor of mathematics, the stochastic dynamics and chaos of physics, the filtering and feedback of engineering, the "when to act" of sequential decision-making, and finally the scientific computing that generalizes sequences into fields — together these currents have upheld the next hundred years of time-series methods. Next, starting from [autoregression in the 1920s](../01/), we formally enter the main statistical line.

---

**Key terms:** stationarity · ergodic theorem · Markov property · martingale · Lévy processes and heavy tails · stochastic calculus / Itô's lemma · geometric Brownian motion · efficient market hypothesis · path integral / Feynman–Kac · rough paths and path signatures · rough volatility · Wiener–Khinchin theorem · Wiener process · Ornstein–Uhlenbeck process · Langevin equation · deterministic chaos · Lyapunov exponent · Takens delay embedding · correlation dimension · long-range correlation / Hurst exponent · DFA · 1/f noise · econophysics · Koopman operator / DMD · Wiener filter · system identification · information theory / sampling theorem (Shannon) · Viterbi algorithm · particle filter / SMC · ensemble Kalman / data assimilation · model predictive control (MPC) · echo state networks / reservoir computing · compressed sensing · particle MCMC · deep state-space models (HiPPO / S4 / Mamba) · Markov decision process · sequential analysis / optimal stopping · multi-armed bandit · dynamic programming / Bellman equation · reinforcement learning · partial differential equations / Navier–Stokes · physics-informed neural networks (PINN) · neural operators (DeepONet / FNO) · data-driven weather forecasting
