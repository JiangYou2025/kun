---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/attention/
title: "Attention"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

L'**attention** est un mécanisme qui permet à un modèle, lorsqu'il traite une position d'une séquence, de **pondérer les autres positions selon leur pertinence** puis d'agréger leurs informations. Elle lui permet de « sauter par-dessus la distance » pour se concentrer directement sur ce qui compte vraiment ; c'est le cœur du [Transformer](../transformer/).

## Intuition

En lisant la phrase « Le latte de ce café est excellent, **il** mérite qu'on y revienne », vous rattachez automatiquement « il » à « café ». Cette capacité à « revenir sur le contenu pertinent quand on en a besoin », c'est l'attention.

On peut comparer le mécanisme à la **consultation d'un dictionnaire** :

- Vous avez en main une **requête (Query)** : « Que veux-je savoir ? »
- Chaque entrée du dictionnaire possède une **clé (Key)** : « À quelle question puis-je répondre ? »
- ainsi qu'une **valeur (Value)** associée : « Le contenu que je porte réellement. »

L'attention compare d'abord la Query à chaque Key pour obtenir un ensemble de poids indiquant « quelle attention lui accorder », puis calcule avec ces poids une moyenne pondérée de toutes les Values. **Les positions pertinentes reçoivent un poids élevé, les autres un poids faible.**

## Formulation mathématique

La forme la plus courante est l'**attention par produit scalaire mis à l'échelle (Scaled Dot-Product Attention)** :

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left( \frac{Q K^{\top}}{\sqrt{d_k}} \right) V
$$

- $Q \in \mathbb{R}^{L \times d_k}$ : la matrice des requêtes, dont chaque ligne est le vecteur requête d'une position ; $L$ est la longueur de la séquence ;
- $K \in \mathbb{R}^{L \times d_k}$ : la matrice des clés ;
- $V \in \mathbb{R}^{L \times d_v}$ : la matrice des valeurs ;
- $Q K^{\top} \in \mathbb{R}^{L \times L}$ : la matrice de similarité, produit scalaire de chaque requête avec chaque clé ;
- $\sqrt{d_k}$ : le facteur d'échelle, qui empêche des produits scalaires trop grands de pousser la softmax dans sa zone de saturation où le [gradient](../gradient/) est minuscule ;
- $\mathrm{softmax}$ : normalise chaque ligne en poids dont la somme vaut 1 ;
- la multiplication finale par $V$ : somme pondérée de toutes les valeurs.

$Q, K, V$ sont généralement obtenues par transformation linéaire d'une même entrée $X$ ($Q = XW_Q$, etc.) ; lorsque les trois proviennent de la même séquence, on parle d'**auto-attention (Self-Attention)**.

L'**attention multi-têtes** effectue en parallèle $h$ exemplaires du calcul ci-dessus (chacun s'intéressant à un aspect différent), puis les concatène : le modèle capte ainsi simultanément plusieurs types de dépendances, comme les « relations syntaxiques » ou les « corrélations numériques ».

{% include fviz/attention-heat.html %}

## Un exemple concret

Supposons une séquence de seulement 3 positions, et que les produits scalaires d'une requête avec les trois clés (après division par $\sqrt{d_k}$) valent $[2.0,\ 0.0,\ 1.0]$. La softmax donne :

$$
\frac{[e^{2}, e^{0}, e^{1}]}{e^{2}+e^{0}+e^{1}} = \frac{[7.39,\ 1.00,\ 2.72]}{11.11} \approx [0.66,\ 0.09,\ 0.25]
$$

La sortie vaut donc $\approx 0.66\,V_1 + 0.09\,V_2 + 0.25\,V_3$ : la position 1 est la plus pertinente (poids 0,66) et domine le résultat. Voilà concrètement ce qu'est une « agrégation pondérée par la pertinence ».

## Pourquoi c'est important / où l'utiliser

- **Accès direct aux dépendances à longue portée** : contrairement au [RNN](../rnn/), qui doit transmettre l'information pas à pas, l'attention **relie directement en une étape** deux positions quelconques ; les relations lointaines ne s'affaiblissent plus avec la distance.
- **Entièrement parallèle** : tout le produit $QK^\top$ se calcule en une seule multiplication matricielle, ce qui rend l'entraînement bien plus rapide qu'avec une structure récurrente.
- **Interprétable** : visualiser les poids d'attention montre « où regarde » le modèle.
- C'est le composant de base du [Transformer](../transformer/) et de presque tous les grands modèles de langage.

## Intérêt pour la prévision de séries temporelles

L'attention permet à un modèle de prévision d'**aligner directement des instants très éloignés** — par exemple relier « ce matin » à « la même plage horaire la semaine dernière » pour capter une périodicité ; c'est son atout pour la prévision de longues séries.

Mais elle a un coût incontournable : la matrice de similarité $QK^\top$ est de taille $L \times L$, **le calcul et la mémoire sont tous deux en $O(L^2)$**. Quand la fenêtre d'historique atteint plusieurs milliers de pas, ce coût quadratique devient très élevé.

C'est justement l'un des points de départ de **Kernel U-Net (KUN)**, le modèle mis en avant sur ce site : plutôt que d'appliquer une coûteuse attention en $O(L^2)$ sur toute la longueur de la séquence, KUN recourt à un **sous-échantillonnage multi-échelle** de type [U-Net](../u-net/) pour capter la structure à longue portée sur des séquences grossières plus courtes, à moindre coût. **L'attention n'est pas rejetée pour autant** — elle peut parfaitement être intégrée comme composant à une échelle donnée ; ce que KUN change, c'est « à quelle granularité et pour quel coût » on modélise les dépendances à longue portée.

## Résumé

- Attention = agrégation pondérée des **Values** selon la **similarité Query–Key** : on regarde davantage ce qui est pertinent.
- L'auto-attention **relie directement en une étape** deux points quelconques de la séquence, capte les dépendances à longue portée et se parallélise.
- Son coût en $O(L^2)$ est élevé sur les longues séries — c'est ce qui motive KUN à lui substituer le multi-échelle.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
