---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/neuron/
title: "Le neurone"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)

**Le neurone (neuron) est la plus petite unité de calcul d'un [réseau de neurones](../neural-network/)** : il fait la somme pondérée de plusieurs entrées, y ajoute un biais, puis passe le résultat dans une [fonction d'activation](../activation-function/) pour produire un nombre. Tous les modèles profonds ne sont, en fin de compte, que des empilements de milliers de ces petites unités.

## Intuition

Vous pouvez vous représenter un neurone comme un **petit juge qui attribue une note**. Devant lui se trouvent quelques caractéristiques (par exemple le cours d'ouverture d'une action aujourd'hui, son volume d'échanges, son cours de clôture d'hier). Pour chacune, il a un poids qui dit « à quel point j'y accorde de l'importance » ; il additionne le tout selon ces poids pour obtenir une note globale. Si la note est assez élevée (au-delà d'un certain seuil), il « s'excite » et produit une valeur plutôt grande ; sinon, il reste silencieux.

- **Poids $w_i$** : exprime « à quel point cette entrée compte pour moi ». Un poids positif signifie que plus l'entrée est grande, plus le neurone tend à s'activer ; un poids négatif, l'inverse.
- **Biais $b$** : c'est en quelque sorte la « ligne de base » ou le « tempérament » du juge. Un biais élevé signifie qu'il s'excite facilement ; un biais très négatif, qu'il est difficile à activer.
- **Fonction d'activation** : décide « comment la note globale devient une sortie » et introduit la **non-linéarité**, essentielle.

Un neurone seul est très limité et ne sait faire qu'une chose simple ; mais en reliant de nombreux neurones en réseau, on peut approcher des fonctions extrêmement complexes.

## Formulation mathématique

Le calcul d'un neurone se fait en deux étapes. D'abord une **somme pondérée linéaire** (appelée aussi pré-activation, notée $z$) :

$$ z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^\top \mathbf{x} + b $$

où :

- $\mathbf{x} = (x_1, \dots, x_n)$ est le vecteur d'entrée et $n$ le nombre de caractéristiques d'entrée ;
- $\mathbf{w} = (w_1, \dots, w_n)$ est le vecteur de poids, les paramètres que le neurone doit **apprendre** ;
- $b$ est le biais, lui aussi un paramètre à apprendre ;
- $\mathbf{w}^\top \mathbf{x}$ est le produit scalaire, soit $w_1x_1 + w_2x_2 + \dots + w_nx_n$.

Ensuite, on applique une fonction d'activation $\sigma$ pour obtenir la **sortie $a$** (activation) :

$$ a = \sigma(z) = \sigma(\mathbf{w}^\top \mathbf{x} + b) $$

Sans $\sigma$ (c'est-à-dire si $\sigma$ est l'identité), quel que soit le nombre de couches empilées, le réseau entier n'est qu'une composition de transformations linéaires, donc encore une fonction linéaire — voilà pourquoi la [fonction d'activation](../activation-function/) est indispensable.

## Un exemple concret

Supposons un neurone à deux entrées $x_1, x_2$, de poids $\mathbf{w} = (0.5,\ -1.2)$, de biais $b = 0.3$, avec ReLU comme fonction d'activation ($\mathrm{ReLU}(z)=\max(0,z)$).

Pour l'entrée $\mathbf{x} = (4,\ 1)$ :

$$ z = 0.5 \times 4 + (-1.2)\times 1 + 0.3 = 2.0 - 1.2 + 0.3 = 1.1 $$
$$ a = \mathrm{ReLU}(1.1) = 1.1 $$

Avec une autre entrée $\mathbf{x} = (1,\ 3)$ :

$$ z = 0.5\times 1 + (-1.2)\times 3 + 0.3 = 0.5 - 3.6 + 0.3 = -2.8 $$
$$ a = \mathrm{ReLU}(-2.8) = 0 $$

On voit que la seconde entrée rend le neurone « silencieux ». En code :

```python
import numpy as np

w = np.array([0.5, -1.2])
b = 0.3

def neuron(x):
    z = w @ x + b          # somme pondérée
    return max(0.0, z)     # activation ReLU

print(neuron(np.array([4, 1])))  # 1.1
print(neuron(np.array([1, 3])))  # 0.0
```

## Pourquoi c'est important / où on l'utilise

Le neurone est l'**atome** qui permet de comprendre toutes les structures de l'[apprentissage profond](../dl/) :

- En plaçant côte à côte plusieurs neurones dans une couche, on obtient une **couche entièrement connectée** ; en empilant plusieurs couches entièrement connectées, on obtient un [MLP](../mlp/).
- Dans un [CNN](../cnn/), les neurones partagent leurs poids et ne regardent qu'une entrée locale : ils deviennent des noyaux de convolution.
- Dans un [RNN](../rnn/), les neurones reçoivent en plus l'état caché de l'instant précédent.

Une fois cette étape « somme pondérée + activation » comprise, vous pouvez comprendre la [propagation avant](../forward-propagation/) (qui répète cette étape à travers le réseau) et la [rétropropagation](../backpropagation/) (qui calcule en sens inverse le gradient de chaque $w_i, b$).

## Intérêt pour la prévision de séries temporelles

En prévision, les « entrées » d'un neurone sont souvent **les valeurs d'une fenêtre d'historique** ou des caractéristiques qui en sont tirées. Par exemple, pour prédire le futur à partir des 96 derniers instants, chaque neurone effectue une combinaison pondérée de ces 96 nombres (ou de caractéristiques extraites par des couches supérieures). Le modèle phare de ce site, le [Kernel U-Net (KUN)](../u-net/), ne fait pas exception : il utilise à plusieurs échelles cette unité de base « somme pondérée + non-linéarité » pour extraire les motifs temporels, simplement organisées en une structure multi-échelle en forme de U.

## En résumé

- Un neurone = **une somme pondérée $\mathbf{w}^\top\mathbf{x}+b$, suivie d'une fonction d'activation $\sigma$**.
- $\mathbf{w}$ et $b$ sont des paramètres appris, ajustés automatiquement par l'entraînement ([rétropropagation](../backpropagation/) + [optimiseur](../optimizer/)).
- **La non-linéarité apportée par la fonction d'activation** est ce qui permet au réseau d'ajuster des fonctions complexes ; sans elle, aussi profond soit-il, il ne reste qu'un [modèle linéaire](../linear-model/).
- Toutes les architectures complexes ne sont que des « agencements » différents de neurones.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)
