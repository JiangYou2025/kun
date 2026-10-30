---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/vanishing-exploding-gradient/
title: "Disparition / explosion du gradient"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **disparition / explosion du gradient (vanishing / exploding gradient)** désigne le phénomène par lequel, lors de la [rétropropagation](../backpropagation/) dans un réseau profond, le gradient, à force de **produits successifs**, **tend exponentiellement vers 0** (disparition) ou **s'amplifie brutalement** (explosion) : les premières couches n'apprennent plus rien, ou l'entraînement s'effondre purement et simplement. C'est l'obstacle numéro un à l'entraînement des réseaux très profonds / très longs.

## Intuition

La rétropropagation renvoie le signal d'erreur **couche par couche, en le multipliant à chaque fois**. Imaginez un nombre multiplié encore et encore par le même facteur $r$ :

- Si $r=0.5$, après 10 couches il devient $0.5^{10}\approx0.001$ — le signal a presque **disparu** ; les couches proches de l'entrée reçoivent un gradient quasi nul et **n'apprennent plus**.
- Si $r=1.5$, après 10 couches il devient $1.5^{10}\approx58$, et après 30 couches c'est un nombre astronomique — le gradient **explose**, les mises à jour des paramètres sont énormes, la loss devient NaN et l'entraînement **s'effondre**.

Ce n'est que lorsque ce facteur reste stable autour de 1 que le signal peut traverser intact de nombreuses couches. **La profondeur elle-même amplifie le problème** — plus il y a de couches, plus il y a de produits.

## Principe : d'où viennent les produits successifs

Rappelons la relation de récurrence de la rétropropagation :

$$
\delta^{(l)} = \big(W^{(l+1)\top}\,\delta^{(l+1)}\big)\odot \sigma'\big(z^{(l)}\big)
$$

Entre la couche de sortie et la couche $l$, le gradient accumule toute une chaîne de produits de $W$ et de $\sigma'$. Grossièrement, l'ordre de grandeur du gradient à la couche $l$ est proportionnel à

$$
\prod_{k=l}^{L} \big\| W^{(k)} \big\| \cdot \big| \sigma'(z^{(k)}) \big|
$$

Terme par terme :

- $\sigma'(z)$ : la dérivée de la [fonction d'activation](../activation-function/). **La dérivée de la sigmoïde est $\le0.25$** : le produit décroît forcément de façon exponentielle → disparition du gradient.
- $\big\|W^{(k)}\big\|$ : la taille des poids. Si les poids sont en général $>1$, le produit croît exponentiellement → explosion du gradient.
- **Produit supérieur à 1 → explosion ; inférieur à 1 → disparition.** Le point critique consiste à maintenir le facteur effectif de chaque couche aussi proche de 1 que possible.

## Un exemple concret

Un réseau de 10 couches, chacune avec une sigmoïde, et un facteur de gradient d'environ $0.2$ par couche :

$$
0.2^{10} = 1.024\times10^{-7}
$$

La première couche ne reçoit qu'un dix-millionième du gradient de la couche de sortie — **autant dire qu'elle n'apprend pas**. À l'inverse, si les poids portent le facteur à $1.3$ :

$$
1.3^{10} \approx 13.8,\qquad 1.3^{30}\approx 2620
$$

Après 30 couches, le gradient est amplifié plus de mille fois, et une seule mise à jour suffit à envoyer les paramètres à NaN.

{% include fviz/grad-product.html %}

## Comment y remédier

C'est la motivation commune de plusieurs innovations clés de l'[apprentissage profond](../dl/) :

- **Changer de fonction d'activation** : remplacer la sigmoïde / tanh par [ReLU](../activation-function/) (dont la dérivée vaut toujours 1 sur la partie positive) évite à la racine la décroissance due aux produits de dérivées $<1$.
- **Une bonne initialisation des poids** : les initialisations de Xavier / de He stabilisent la variance de chaque couche, de sorte que le facteur initial soit proche de 1.
- **La normalisation** : la [BatchNorm](../batchnorm/) / LayerNorm ramène les entrées de chaque couche à une distribution stable et empêche la dérive numérique.
- **Les connexions résiduelles (ResNet)** : ajouter un « raccourci identité » $y = x + F(x)$ offre au gradient un **chemin direct sans atténuation** jusqu'aux couches superficielles.
- **L'écrêtage du gradient (gradient clipping)** : quand la norme du gradient dépasse un seuil, on la ramène à l'échelle ; c'est le remède d'urgence le plus direct **contre l'explosion**.
- **Les structures à portes** : le [LSTM](../lstm/) utilise des portes et un état de cellule précisément pour que le gradient d'un [RNN](../rnn/) ne disparaisse pas sur de longues séquences.

```python
# Écrêtage du gradient : la ligne habituelle pour éviter l'explosion pendant l'entraînement
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

## Intérêt pour la prévision de séries temporelles

Un modèle séquentiel déplie le réseau le long des **pas de temps** : **plus la fenêtre d'historique est longue, plus le nombre de couches équivalent est grand, et plus les produits de gradients sont nombreux** — c'est pourquoi la disparition / explosion du gradient est particulièrement grave en prévision de longues séquences, et c'est précisément pour cela qu'un [RNN](../rnn/) ordinaire n'apprend pas les dépendances de long terme, et que le [LSTM](../lstm/) a vu le jour.

Le modèle phare de ce site, [Kernel U-Net (KUN)](../../kun/), utilise un **sous-échantillonnage multi-échelles** qui compresse la longue séquence en une représentation plus courte avant de la traiter, ce qui raccourcit d'autant le chemin que doit parcourir le gradient et atténue naturellement ce problème. Pour entraîner KUN sur de longues fenêtres d'historique, il reste conseillé de combiner [Adam](../adam/), un [taux d'apprentissage](../learning-rate/) modéré et l'écrêtage du gradient pour stabiliser l'entraînement.

## Résumé

- Cause profonde : en rétropropagation, le gradient est un **produit successif** ; si le facteur est $<1$, il **disparaît**, s'il est $>1$, il **explose**, et la profondeur / la longueur de la séquence amplifient le phénomène.
- Disparition → les couches superficielles n'apprennent plus ; explosion → la loss devient NaN.
- Combinaison de remèdes : **ReLU + bonne initialisation + normalisation + résiduel + écrêtage du gradient + portes (LSTM)**.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
