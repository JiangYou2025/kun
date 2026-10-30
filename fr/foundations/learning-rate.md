---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/learning-rate/
title: "Le taux d'apprentissage"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)

Le **taux d'apprentissage (learning rate, $\eta$)** est la **taille du pas** que fait la [descente de gradient](../gradient-descent/) à chaque itération. Il détermine « jusqu'où l'on avance d'un coup dans la direction du gradient ». Trop grand, l'entraînement oscille, voire diverge ; trop petit, il avance comme un escargot — c'est **l'hyperparamètre le plus crucial de l'apprentissage profond, celui qu'il faut régler en priorité**.

## Intuition

Reprenons l'image de la « descente de montagne les yeux bandés ». La [rétropropagation](../backpropagation/) vous indique la pente descendante la plus raide sous vos pieds ; le taux d'apprentissage décide de **la longueur de chacun de vos pas** :

- **Pas trop grands** : vous risquez d'enjamber le fond de la vallée d'un seul pas, d'atterrir sur le versant opposé, puis de revenir… vous **oscillez** d'un côté à l'autre, et vous pouvez même monter de plus en plus haut (**divergence**).
- **Pas trop petits** : la direction est bonne, mais vous avancez très lentement ; l'entraînement prend une éternité, et vous risquez de rester coincé dans un petit creux.
- **Pas bien dosés** : vous atteignez le fond de la vallée de façon stable et assez rapide.

Le taux d'apprentissage n'obéit donc ni à « plus c'est grand, plus c'est rapide », ni à « plus c'est petit, mieux c'est » : il faut trouver la **zone optimale**.

## Principe : comment il intervient dans la règle de mise à jour

Forme générale de la mise à jour des paramètres :

$$
\theta_{t+1} = \theta_t - \eta\, g_t
$$

- $\theta_t$ : les paramètres courants ; $g_t$ : le gradient calculé par la [rétropropagation](../backpropagation/) ; $\eta$ : le taux d'apprentissage.
- $\eta$ **met directement à l'échelle** le déplacement à chaque pas. Doubler $\eta$, c'est doubler le pas.

Un exemple simple montre son effet sur la convergence. Pour minimiser $\mathcal{L}=\theta^2$ (gradient $g=2\theta$), la mise à jour devient $\theta_{t+1} = \theta_t(1 - 2\eta)$ :

- $\eta=0.1$ : facteur $0.8$, **convergence régulière** vers 0.
- $\eta=0.5$ : facteur $0$, **convergence en un seul pas** (idéal, mais les surfaces réelles ne sont jamais aussi accommodantes).
- $\eta=1.0$ : facteur $-1$, **oscillation perpétuelle** entre $+1$ et $-1$.
- $\eta=1.5$ : facteur $-2$, $|\theta|$ ne cesse de croître : **divergence** !

{% include fviz/optimizer.html %}

## Planification du taux d'apprentissage (schedule)

Un taux d'apprentissage fixe est rarement optimal. La pratique courante consiste à **commencer grand, puis diminuer** :

- **Warmup (échauffement)** : en début d'entraînement, on fait croître $\eta$ linéairement depuis une très petite valeur jusqu'à la valeur cible, pour éviter d'être projeté au loin dès le départ par des gradients énormes.
- **Décroissance (decay)** : en fin d'entraînement, on réduit progressivement $\eta$ pour que les paramètres puissent **s'ajuster finement** près du fond de la vallée. Les variantes courantes sont la step decay et le recuit cosinus (cosine annealing).

Une courbe typique : montée pendant le warmup, puis lente descente le long d'une courbe cosinus.

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
# Recuit cosinus : lr descend de 1e-3 jusqu'à presque 0 le long d'une courbe cosinus
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=100)
for epoch in range(100):
    train_one_epoch(...)
    opt.step()
    sched.step()                 # met à jour le taux d'apprentissage à chaque epoch
    print(sched.get_last_lr())
```

{% include fviz/lr-schedule.html %}

## Comment choisir le taux d'apprentissage

- Points de départ courants : **$10^{-3}$ pour Adam**, $10^{-1}\sim10^{-2}$ pour SGD.
- **Balayer par ordres de grandeur (facteur 10)** : essayez $10^{-2}, 10^{-3}, 10^{-4}$ et retenez celui pour lequel la perte baisse le plus vite sans osciller.
- Diagnostiquer à partir de la courbe de perte : **fortes oscillations / apparition de NaN → réduire** ; **baisse très lente et plate → augmenter**.

## Signification pour la prévision de séries temporelles

Lorsqu'on entraîne un modèle comme [Kernel U-Net (KUN)](../../kun/) sur des **fenêtres d'historique longues**, le taux d'apprentissage est particulièrement sensible : plus la séquence est longue, plus l'échelle des gradients fluctue, et un taux trop élevé déclenche plus facilement une [explosion du gradient](../vanishing-exploding-gradient/) qui fait passer la perte à NaN. En pratique, on combine souvent [Adam](../adam/), un taux d'apprentissage modéré, un warmup et une décroissance cosinus, et, en cas d'explosion du gradient, on commence par **réduire le taux d'apprentissage**. C'est le premier réflexe pour stabiliser l'entraînement de KUN.

## En résumé

- Le taux d'apprentissage $\eta$ = la **taille du pas** de la descente de gradient, qui apparaît dans $\theta_{t+1}=\theta_t-\eta g_t$.
- **Trop grand, il oscille ou diverge ; trop petit, il est trop lent** : il faut trouver la zone optimale.
- En pratique : partir des ordres de grandeur et combiner avec une planification **warmup + décroissance** ; c'est l'hyperparamètre à régler en priorité.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)
