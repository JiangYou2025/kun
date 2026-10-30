---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/cnn/
title: "CNN (réseaux de neurones convolutifs)"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)

Un **CNN (Convolutional Neural Network, réseau de neurones convolutif)** fait glisser de petits **noyaux de convolution** sur les données pour en extraire des **motifs locaux invariants par translation**. Il s'est d'abord illustré sur les images, mais il s'applique tout aussi bien aux séries temporelles — il suffit de remplacer la convolution bidimensionnelle par une **convolution unidimensionnelle** le long de l'axe du temps.

## Intuition

Imaginez que vous balayiez une série temporelle de gauche à droite avec une petite loupe (le noyau de convolution, de largeur 3 par exemple). À chaque position, la loupe répond à une question : « ce petit segment contient-il la forme qui m'intéresse ? » — par exemple un front montant, un pic ou une marche.

Le point essentiel : **la même loupe utilise les mêmes paramètres à toutes les positions**. Cela apporte deux avantages :

- **Invariance par translation** : que le pic apparaisse au début ou à la fin de la série, le même noyau saura le reconnaître ;
- **Partage des paramètres** : contrairement au [MLP](../mlp/), qui attribue un jeu de poids indépendant à chaque position, le CNN n'utilise qu'un seul jeu de paramètres de noyau pour toute la série ; il a donc beaucoup moins de paramètres et est moins sujet au [surapprentissage](../overfitting/).

## Principe

Convolution unidimensionnelle : un noyau $\mathbf{w}$ de longueur $k$ glisse sur l'entrée $\mathbf{x}$ ; la $t$-ième valeur de sortie vaut :

$$
y_t = \sum_{i=0}^{k-1} w_i \, x_{t+i} + b
$$

- $x_{t+i}$ : la valeur de l'entrée à l'instant $t+i$ ;
- $w_i$ : le $i$-ième poids du noyau, un paramètre à apprendre ;
- $k$ : la taille du noyau (kernel size), c'est-à-dire la largeur de la fenêtre locale examinée à chaque fois ;
- $b$ : le biais ;
- $y_t$ : la sortie à cette position, appelée un point de la « carte de caractéristiques » (feature map).

Une couche de convolution est généralement suivie d'une [fonction d'activation](../activation-function/) non linéaire, puis d'un **pooling (regroupement)** qui sous-échantillonne — par exemple le max-pooling, qui prend le maximum dans chaque petite fenêtre :

$$
p_t = \max\left(y_{2t},\, y_{2t+1}\right)
$$

Après sous-échantillonnage, la série est plus courte (ici sa longueur est divisée par deux), mais la « portée de vue » de chaque point (le **champ récepteur**) s'élargit. **L'empilement de plusieurs couches de convolution + sous-échantillonnage permet au réseau de passer progressivement des détails locaux à des motifs d'échelle plus grande** — c'est précisément la source de l'idée multi-échelle de U-Net et de KUN, que nous verrons plus loin.

Quelques réglages courants :

- **stride (pas)** : de combien de positions le noyau avance à chaque fois ; un pas > 1 permet aussi de sous-échantillonner ;
- **padding (remplissage)** : on ajoute des zéros aux deux extrémités pour que la sortie ait la même longueur que l'entrée ;
- **dilation (dilatation)** : on laisse des espaces entre les points échantillonnés par le noyau, ce qui élargit le champ récepteur sans ajouter de paramètres (les convolutions causales dilatées, comme dans WaveNet/TCN, sont courantes pour les séries temporelles).

{% include fviz/conv1d.html %}

## Un exemple concret

Convoluons l'entrée $\mathbf{x} = [3, 3, 5, 5, 5]$ avec un noyau de longueur 3, $\mathbf{w} = [1, 0, -1]$ (un simple « détecteur de contours »), sans padding, avec un stride de 1 et $b=0$ :

- $y_0 = 1\cdot3 + 0\cdot3 + (-1)\cdot5 = -2$
- $y_1 = 1\cdot3 + 0\cdot5 + (-1)\cdot5 = -2$
- $y_2 = 1\cdot5 + 0\cdot5 + (-1)\cdot5 = 0$

La sortie $[-2, -2, 0]$ donne une réponse non nulle au niveau du « saut » de 3 à 5, et 0 sur la partie plate. C'est cela, un noyau de convolution qui « détecte des variations locales ».

Version PyTorch :

```python
import torch.nn as nn

conv = nn.Conv1d(in_channels=1, out_channels=16,
                 kernel_size=3, padding=1)   # 16 noyaux, sortie de même longueur
# Forme de l'entrée : (lot, canaux=1, longueur temporelle)
```

## Pourquoi c'est important / où l'utilise-t-on

- **Efficace** : peu de paramètres, calcul parallélisable, entraînement rapide.
- **Spécialiste des caractéristiques locales** : excelle à capter les motifs « de forme » — ondes périodiques, ruptures brusques, segments saisonniers.
- **Pierre angulaire du multi-échelle** : le sous-échantillonnage couche après couche forme une pyramide de caractéristiques allant du fin au grossier, base structurelle du [U-Net](../u-net/) de segmentation d'images et de nombreux modèles de séries temporelles.

## Signification pour la prévision de séries temporelles

La **convolution unidimensionnelle + sous-échantillonnage** le long de l'axe du temps est précisément l'ancêtre conceptuel du modèle phare de ce site, **Kernel U-Net (KUN)**. Le CNN nous livre une intuition centrale :

> **Regarder une série à différentes résolutions temporelles permet de saisir à la fois les détails à court terme et les tendances à long terme.**

Les convolutions des couches basses voient les fluctuations « à la minute » ; après quelques sous-échantillonnages, on voit les tendances « à l'heure, au jour ». KUN hérite de cette approche **multi-échelle (multi-résolution)** : il sous-échantillonne l'axe du temps niveau par niveau pour obtenir plusieurs vues allant du fin au grossier, mais **remplace les lourds blocs de convolution par des « noyaux » apprenables plus légers**, afin de concilier informations à courte et à longue portée avec moins de calcul. Comprendre la convolution 1D et le sous-échantillonnage est donc la première étape pour comprendre KUN.

## En résumé

- Le CNN fait glisser des **noyaux de convolution partagés** pour extraire des motifs **locaux et invariants par translation**.
- **Sous-échantillonnage + couches multiples** agrandissent le champ récepteur niveau par niveau et forment des caractéristiques multi-échelles allant du fin au grossier.
- La convolution unidimensionnelle convient naturellement aux séries temporelles ; elle est la source conceptuelle de la structure multi-échelle de [U-Net](../u-net/) et de Kernel U-Net.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)
