---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/activation-function/
title: "Fonction d'activation"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Une **fonction d'activation** est une **fonction non linéaire** appliquée après la somme pondérée de chaque [neurone](../neuron/). C'est elle qui donne à un [réseau de neurones](../neural-network/) la capacité d'« exprimer des relations complexes » — **sans elle, un réseau, aussi profond soit-il, n'équivaut qu'à une seule transformation linéaire**.

## Pourquoi la non-linéarité est indispensable

Rappelons la [propagation avant](../forward-propagation/) : chaque couche calcule $z = Wa + b$. Sans fonction d'activation, empilons plusieurs couches :

$$
W_2(W_1 x + b_1) + b_2 = (W_2 W_1)\,x + (W_2 b_1 + b_2)
$$

Quel que soit le nombre de couches, le résultat **reste une fonction linéaire de $x$** ! La profondeur ne sert à rien. La fonction d'activation $\sigma$ introduit à chaque couche un « pli », ce qui permet au réseau d'approcher **des relations non linéaires arbitrairement complexes** (c'est l'intuition du théorème d'approximation universelle).

## Trois fonctions d'activation classiques

**Sigmoïde** : comprime l'entrée dans $(0,1)$.

$$
\sigma(x) = \frac{1}{1+e^{-x}},\qquad
\sigma'(x) = \sigma(x)\big(1-\sigma(x)\big)
$$

Sa dérivée atteint son maximum en $x=0$, où elle ne vaut que $0.25$, et tend vers 0 aux deux extrémités. Autrement dit, le signal d'erreur est multiplié par un facteur $\le0.25$ à chaque couche sigmoïde traversée — dans un réseau profond, ce produit tend rapidement vers 0 et provoque la [disparition du gradient](../vanishing-exploding-gradient/). Aujourd'hui, on l'utilise surtout dans la couche de sortie pour la classification binaire, rarement dans les couches cachées.

**Tanh** : comprime l'entrée dans $(-1,1)$ ; c'est la version « centrée en zéro » de la sigmoïde.

$$
\tanh(x) = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}},\qquad
\tanh'(x) = 1 - \tanh^2(x)
$$

Le fait d'être centrée en zéro (sorties positives et négatives) rend l'entraînement un peu meilleur qu'avec la sigmoïde, et sa dérivée atteint au maximum 1 (en $x=0$). Mais elle sature toujours aux deux extrémités, et le gradient disparaît encore dans les réseaux profonds. On la rencontre souvent dans les [RNN](../rnn/)/[LSTM](../lstm/).

**ReLU** : l'activation la plus utilisée dans les couches cachées, simple et efficace.

$$
\mathrm{ReLU}(x) = \max(0, x),\qquad
\mathrm{ReLU}'(x) = \begin{cases}1 & x>0\\ 0 & x<0\end{cases}
$$

**Pourquoi ReLU atténue la disparition du gradient** : sur la partie positive, la dérivée **vaut constamment 1**, si bien que le signal d'erreur n'est pas réduit couche après couche lors de la rétropropagation — un produit de 1 reste 1. Cela permet d'entraîner des réseaux très profonds. Le prix à payer : la dérivée est nulle sur la partie négative, et un neurone peut « mourir » (sortir 0 pour toujours). La variante **Leaky ReLU** (une petite pente $0.01x$ lorsque $x<0$) atténue ce problème.

{% include fviz/activation.html %}

## Un exemple concret

Supposons qu'un neurone ait une somme pondérée $z = -0.5$. Comparons la sortie des trois activations et « la part du gradient qui peut revenir » (c'est-à-dire la dérivée) :

| Activation | Sortie | Dérivée (facteur de gradient en ce point) |
|---|---|---|
| Sigmoïde | $\sigma(-0.5)\approx0.378$ | $0.378(1-0.378)\approx0.235$ |
| Tanh | $\tanh(-0.5)\approx-0.462$ | $1-0.462^2\approx0.787$ |
| ReLU | $\max(0,-0.5)=0$ | $0$ (partie négative) |

Imaginons 10 couches toutes en sigmoïde : le facteur de gradient vaut environ $0.235^{10}\approx 5\times10^{-7}$ — **il a pratiquement disparu**. C'est précisément pour cette raison que les réseaux profonds ont abandonné la sigmoïde au profit de ReLU.

```python
import numpy as np
sigmoid = lambda x: 1/(1+np.exp(-x))
tanh    = np.tanh
relu    = lambda x: np.maximum(0, x)
z = -0.5
print(sigmoid(z), tanh(z), relu(z))   # 0.378  -0.462  0.0
```

## Comment choisir

- **Couches cachées : ReLU par défaut** (ou GELU, Leaky ReLU) — rapide, stable, résistante à la disparition du gradient.
- **Couche de sortie en classification binaire : sigmoïde** (pour produire une probabilité) ; softmax en classification multiclasse.
- **Couche de sortie en régression : généralement aucune activation** (on sort directement un réel) — c'est en général le cas pour la couche de sortie en prévision de séries temporelles.
- À l'intérieur des [RNN](../rnn/)/[LSTM](../lstm/), on combine souvent tanh et sigmoïde pour réaliser les portes.

## Idées reçues

- **« Il faut aussi mettre une ReLU en sortie »** — pas pour prédire un réel, sinon le modèle ne pourra jamais produire de valeur négative.
- **« Plus la fonction d'activation est complexe, mieux c'est »** — ReLU est d'une grande simplicité et pourtant la plus utilisée ; complexité n'est pas efficacité.
- **« La sigmoïde convient aux couches cachées profondes »** — c'est tout le contraire : elle provoque la [disparition du gradient](../vanishing-exploding-gradient/).

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
