---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/adam/
title: "Adam"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

**Adam (Adaptive Moment Estimation)** est aujourd'hui l'[optimiseur](../optimizer/) le plus utilisé. Il maintient à la fois le **moment d'ordre un** du gradient (la quantité de mouvement, c'est-à-dire la direction) et son **moment d'ordre deux** (l'historique de l'amplitude du gradient), ce qui lui permet d'**adapter le pas pour chaque paramètre** — l'entraînement est à la fois rapide et stable, au point qu'Adam est devenu le choix par défaut en [apprentissage profond](../dl/).

## Intuition

Reprenons l'image de la « descente de montagne les yeux bandés » de la page sur les [optimiseurs](../optimizer/) :

- **La quantité de mouvement (momentum)** fait de vous une bille qui dévale la pente et franchit les petits creux grâce à son inertie — c'est le premier ingrédient d'Adam.
- **Le pas adaptatif** : dans les directions durablement escarpées, le pas diminue automatiquement (pour ne pas aller trop loin) ; dans les directions plates ou rarement mises à jour, il s'agrandit (pour ne pas traîner) — c'est le second ingrédient d'Adam.

Adam **réunit les deux** : il retient la direction moyenne du gradient ainsi que l'« intensité » moyenne du gradient de chaque paramètre, puis utilise la seconde pour normaliser la première. Résultat : sans presque rien régler, il fonctionne de manière fiable sur toutes sortes de réseaux.

## Formulation mathématique : la mise à jour complète

Notons $g_t$ le gradient à l'étape $t$ (calculé par [rétropropagation](../backpropagation/)). Adam maintient deux moyennes mobiles :

**Moment d'ordre un (momentum)** :
$$
m_t = \beta_1 m_{t-1} + (1-\beta_1)\, g_t
$$

**Moment d'ordre deux (carré du gradient)** :
$$
v_t = \beta_2 v_{t-1} + (1-\beta_2)\, g_t^2
$$

Comme $m_0 = v_0 = 0$, ces deux estimations sont **biaisées vers 0** au début ; on effectue donc une **correction du biais** :
$$
\hat{m}_t = \frac{m_t}{1-\beta_1^{\,t}},\qquad
\hat{v}_t = \frac{v_t}{1-\beta_2^{\,t}}
$$

**Mise à jour finale des paramètres** :
$$
\theta_{t+1} = \theta_t - \eta\,\frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

Explication symbole par symbole :

- $g_t$ : le gradient courant ; $g_t^2$ est le carré **élément par élément**.
- $m_t$ : moyenne mobile exponentielle du gradient (**direction / momentum**).
- $v_t$ : moyenne mobile exponentielle du carré du gradient (**l'amplitude du gradient de chaque paramètre**).
- $\beta_1$ : taux de décroissance du momentum, **0,9 par défaut**.
- $\beta_2$ : taux de décroissance du moment d'ordre deux, **0,999 par défaut**.
- $\beta_1^{\,t}, \beta_2^{\,t}$ : la **puissance $t$-ième** de $\beta$ (pour la correction du biais) ; elles tendent vers 0 quand $t$ croît, et la correction s'efface progressivement.
- $\hat m_t, \hat v_t$ : les estimations après correction du biais.
- $\eta$ : le [taux d'apprentissage](../learning-rate/), **0,001 par défaut**.
- $\epsilon$ : petite constante évitant la division par zéro, **$10^{-8}$ par défaut**.

Intuition : $\dfrac{\hat m_t}{\sqrt{\hat v_t}}$ **normalise automatiquement** le pas effectif de chaque paramètre — dans une direction où le gradient est durablement grand, le dénominateur est grand et le pas se réduit ; dans le cas inverse, il s'agrandit.

{% include fviz/optimizer.html %}

## Un exemple concret

Pour un seul paramètre, première étape : $g_1 = 0.1$, $\beta_1=0.9,\beta_2=0.999,\eta=0.001,\epsilon=10^{-8}$.

$$
m_1 = 0.9\times0 + 0.1\times0.1 = 0.01
$$
$$
v_1 = 0.999\times0 + 0.001\times0.01 = 0.00001
$$

Correction du biais ($t=1$) :
$$
\hat m_1 = \frac{0.01}{1-0.9} = 0.1,\qquad
\hat v_1 = \frac{0.00001}{1-0.999} = 0.01
$$

Mise à jour :
$$
\Delta\theta = -\,0.001\times\frac{0.1}{\sqrt{0.01}+10^{-8}}
= -0.001\times\frac{0.1}{0.1} = -0.001
$$

Remarque : après correction du biais, le pas effectif de la première étape est à peu près égal au taux d'apprentissage $\eta=0.001$ — c'est exactement le but de la correction ; sans elle, la première étape serait faussée par des valeurs de $m$ et $v$ trop petites.

```python
import torch
theta = torch.tensor([1.0], requires_grad=True)
opt = torch.optim.Adam([theta], lr=1e-3, betas=(0.9, 0.999), eps=1e-8)
for _ in range(3):
    opt.zero_grad()
    loss = (theta - 0.0)**2          # objectif : ramener theta vers 0
    loss.backward()
    opt.step()
    print(round(theta.item(), 6))
```

## Pourquoi c'est important / où l'utiliser

- **Optimiseur de premier choix par défaut** : peu sensible au taux d'apprentissage, convergence rapide, presque prêt à l'emploi. Pour un débutant, commencer l'entraînement de n'importe quel réseau avec Adam et `lr=1e-3` n'est presque jamais une erreur.
- Il se comporte de manière robuste sur presque toutes les architectures : [Transformer](../transformer/), [RNN](../rnn/)/[LSTM](../lstm/), [CNN](../cnn/), etc.
- Sa variante courante **AdamW** découple la décroissance des poids (weight decay) de la mise à jour par le gradient, ce qui améliore la régularisation ; c'est aujourd'hui la norme pour l'entraînement des grands modèles.

## Intérêt pour la prévision de séries temporelles

Lors de l'entraînement de modèles de prévision multi-échelles comme [Kernel U-Net (KUN)](../../kun/), une longue fenêtre d'historique fait varier énormément l'échelle des gradients d'un paramètre à l'autre ; le **pas adaptatif par paramètre** d'Adam aplanit justement ces écarts automatiquement, ce qui évite de régler à la main le pas de chaque couche. En pratique, `Adam(lr=1e-3 ou 1e-4)` est un point de départ robuste et courant pour entraîner KUN ; si la loss oscille, diminuez d'abord le [taux d'apprentissage](../learning-rate/) plutôt que de changer d'optimiseur.

## Résumé

- Adam = **momentum (moment d'ordre un) + pas adaptatif (moment d'ordre deux) + correction du biais**.
- Formule clé : $\theta_{t+1} = \theta_t - \eta\,\dfrac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}$.
- Hyperparamètres par défaut : $\beta_1=0.9,\ \beta_2=0.999,\ \epsilon=10^{-8}$ ; le taux d'apprentissage reste à régler soi-même.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
