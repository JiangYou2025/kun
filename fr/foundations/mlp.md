---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/mlp/
title: "MLP (perceptron multicouche)"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)

Le **MLP (Multi-Layer Perceptron, perceptron multicouche)** est le [réseau de neurones](../neural-network/) le plus élémentaire : un empilement de couches entièrement connectées (fully-connected), où chaque [neurone](../neuron/) d'une couche est relié à chaque neurone de la couche suivante, avec des [fonctions d'activation](../activation-function/) intercalées. C'est la « brique » de presque toutes les [architectures](../architectures/) modernes.

## Intuition

« Entièrement connecté » signifie : **pas de tri préalable**. Chaque neurone voit toute l'information de la couche précédente et décide lui-même de ce qui compte et de ce qu'il ignore (grâce aux poids appris).

Cela contraste avec le [CNN](../cnn/), qui « ne regarde qu'une fenêtre locale », et avec l'[attention](../attention/), qui « sélectionne l'essentiel selon la pertinence ». Le MLP ne présuppose aucune structure : c'est la forme la plus simple et la plus générale. Avec suffisamment de neurones, il peut en théorie approcher n'importe quelle fonction continue (**théorème d'approximation universelle**). Le prix à payer : beaucoup de paramètres, et aucune exploitation de la structure propre aux données (comme l'ordre temporel ou le voisinage des pixels).

{% include fviz/relu-approx.html %}

## Formulation mathématique

Un MLP à $L$ couches consiste à imbriquer de façon répétée « transformation linéaire + activation ». Soit l'entrée $\mathbf{x}$ ; on pose $\mathbf{h}^{(0)} = \mathbf{x}$, et la couche $l$ s'écrit :

$$
\mathbf{h}^{(l)} = \sigma\!\left( \mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)} \right), \quad l = 1, \dots, L
$$

- $\mathbf{h}^{(l-1)} \in \mathbb{R}^{d_{l-1}}$ : sortie de la couche $l-1$ (de dimension $d_{l-1}$) ;
- $\mathbf{W}^{(l)} \in \mathbb{R}^{d_l \times d_{l-1}}$ : matrice de poids, qui envoie l'espace de dimension $d_{l-1}$ vers celui de dimension $d_l$ ;
- $\mathbf{b}^{(l)} \in \mathbb{R}^{d_l}$ : vecteur de biais ;
- $\sigma$ : fonction d'activation, appliquée élément par élément (dans les couches cachées, on utilise souvent ReLU $\sigma(z)=\max(0,z)$) ;
- la couche de sortie n'a généralement **pas d'activation** (tâches de régression) : directement $\hat{\mathbf{y}} = \mathbf{W}^{(L)}\mathbf{h}^{(L-1)} + \mathbf{b}^{(L)}$.

**Nombre de paramètres** : la couche $l$ compte $d_l \times d_{l-1} + d_l$ paramètres. C'est aussi le point faible du MLP — dès que la dimension augmente, la matrice de poids explose.

## Un exemple concret

Calculons à la main un MLP minuscule : entrée de dimension 2, couche cachée de 2 neurones (ReLU), sortie de dimension 1.

Soit $\mathbf{x} = \begin{bmatrix}1\cr 2\end{bmatrix}$,

$$
\mathbf{W}^{(1)} = \begin{bmatrix}1 & 0\\-1 & 1\end{bmatrix},\quad
\mathbf{b}^{(1)} = \begin{bmatrix}0\\0\end{bmatrix}
$$

Partie linéaire de la couche 1 : $\mathbf{W}^{(1)}\mathbf{x} = \begin{bmatrix}1\cdot1 + 0\cdot2\cr  -1\cdot1 + 1\cdot2\end{bmatrix} = \begin{bmatrix}1\cr 1\end{bmatrix}$.

Après ReLU : $\mathbf{h}^{(1)} = \begin{bmatrix}\max(0,1)\cr\max(0,1)\end{bmatrix} = \begin{bmatrix}1\cr 1\end{bmatrix}$.

Couche de sortie $\mathbf{W}^{(2)} = \begin{bmatrix}2 & 3\end{bmatrix}$, $b^{(2)}=1$ :

$$
\hat{y} = 2\cdot1 + 3\cdot1 + 1 = 6
$$

Version en code :

```python
import torch.nn as nn

mlp = nn.Sequential(
    nn.Linear(2, 2),
    nn.ReLU(),
    nn.Linear(2, 1),
)
```

## Pourquoi c'est important / où on l'utilise

- **Approximateur universel** : en théorie, il peut ajuster n'importe quelle relation entrée–sortie, aussi complexe soit-elle.
- **Composant universel** : le « réseau à propagation avant » (feed-forward) de chaque bloc d'un [Transformer](../transformer/) est un MLP ; la tête de prédiction finale d'un CNN ou d'un U-Net est aussi souvent un MLP. Le maîtriser, c'est comprendre une partie d'innombrables modèles.
- **Référence solide** : en prévision de séries temporelles, aplatir tout l'historique et le donner à un MLP (à la manière de DLinear ou N-BEATS) se révèle souvent étonnamment performant ; c'est un point de comparaison indispensable.

## Intérêt pour la prévision de séries temporelles

L'approche de prévision la plus simple : traiter la fenêtre d'historique de longueur $L$ comme un vecteur de dimension $L$ et la projeter directement par un MLP vers un futur de dimension $H$ :

```python
forecaster = nn.Sequential(
    nn.Linear(96, 256), nn.ReLU(),
    nn.Linear(256, 24),     # 96 pas d'historique -> 24 pas de prévision
)
```

Cette approche « aplatir + entièrement connecté » est simple et efficace, mais elle a deux limites : elle **ignore la structure séquentielle du temps** (mélanger l'ordre des entrées ne change pas le résultat), et plus la fenêtre est longue, plus il y a de paramètres. Le **Kernel U-Net (KUN)**, mis en avant sur ce site, atténue précisément ces deux points par une approche [multi-échelle](../u-net/) — il traite les données avec des « noyaux » légers à différentes résolutions temporelles, et la transformation à l'intérieur de chaque noyau reste, au fond, un petit MLP. Le MLP est donc à la fois une référence et une pièce interne d'architectures plus avancées.

## Erreurs fréquentes

- **« Un MLP fonctionne aussi sans activation »** : faux. Sans activation, plusieurs couches s'effondrent en une seule couche linéaire ; la profondeur ne sert alors à rien.
- **« Plus il y a de couches, mieux c'est »** : un MLP pur trop profond se heurte facilement à l'[évanouissement / l'explosion du gradient](../vanishing-exploding-gradient/) et au [surapprentissage](../overfitting/) ; il a souvent besoin d'aides comme le [Dropout](../dropout/) ou la [BatchNorm](../batchnorm/).
- **« Le MLP comprend l'ordre temporel »** : non. Il traite l'entrée comme un vecteur sans ordre ; la structure temporelle doit être introduite par un CNN, un RNN, l'attention ou une conception explicite.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)
