---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/math/
title: "Fondements mathématiques"
lead: "Calcul différentiel et intégral, algèbre linéaire, probabilités et statistiques, optimisation et théorie de l'information — le langage mathématique de la modélisation prédictive. On pose le cadre et les concepts, sans entrer dans les démonstrations."
prev: /foundations/
next: /foundations/cs/
math: true
---

> Ceci est une **carte conceptuelle** : elle indique, pour chaque domaine des mathématiques, « ce qu'il contient et à quoi il sert ». Il suffit d'en acquérir l'intuition ; pour les démonstrations systématiques, reportez-vous à des manuels spécialisés.

## 1. [Calcul différentiel et intégral](../calculus/)

Les mathématiques du « changement », fondement de l'optimisation et de l'entraînement.

- **Limites et continuité** : comprendre l'idée d'« approcher indéfiniment »
- **Dérivées / dérivées partielles** : la sensibilité d'une fonction aux variations d'une variable
- **[Gradient](../gradient/) $\nabla f$** : la direction de plus forte croissance d'une fonction de plusieurs variables — le cœur de l'entraînement des [réseaux de neurones](../neural-network/)
- **[Règle de dérivation en chaîne](../chain-rule/)** : dériver une fonction composée, principe mathématique de la **[rétropropagation](../backpropagation/)**
- **Intégrale** : calculer des aires / des quantités cumulées ; nécessaire pour normaliser une densité de probabilité

{% include fviz/derivative.html %}

## 2. [Algèbre linéaire](../linear-algebra/)

Le « langage » des données et des modèles — tout y est vecteur ou matrice.

- **Scalaires / vecteurs / matrices / tenseurs** : la manière d'organiser les données
- **[Multiplication matricielle](../matrix-multiplication/)** : une transformation linéaire, l'essence de chaque couche d'un réseau de neurones
- **Transposée, inverse, rang** : décrire la structure d'une matrice
- **[Normes](../norm/)** : $\ell_1$ (parcimonie), $\ell_2$ (énergie / erreur) pour mesurer la « taille »
- **Valeurs propres et vecteurs propres** : stabilité, directions principales
- **Décompositions matricielles ([ACP](../pca/) / [SVD](../svd/))** : réduction de dimension et compression

{% include fviz/matrix-transform.html %}

## 3. [Probabilités et statistiques](../probability-statistics/)

Les outils pour raisonner et décider dans l'**incertitude**.

- **[Variables aléatoires](../random-variable/) et lois de probabilité** : discrètes / continues ; loi normale, de Bernoulli, de Poisson
- **Espérance, variance, covariance** : centre, dispersion, co-variation
- **Probabilité conditionnelle et [théorème de Bayes](../bayes-theorem/)** : mettre à jour ses croyances à la lumière de nouvelles données
- **Loi des grands nombres et théorème central limite** : pourquoi la « moyenne » et la « loi normale » sont partout
- **Estimation** : [maximum de vraisemblance](../maximum-likelihood/) (MLE), maximum a posteriori (MAP)
- **Tests d'hypothèses et intervalles de confiance** : juger si une « différence est significative »

{% include fviz/clt.html %}

## 4. [Optimisation](../optimization/)

« Apprendre = minimiser la [perte](../loss-function/) » : l'optimisation est le pont entre les mathématiques et l'apprentissage automatique.

$$\theta^\* = \arg\min_\theta \; \mathcal{L}(\theta)$$

- **[Convexe ou non convexe](../convex-optimization/)** : existe-t-il un unique optimum global ?
- **[Descente de gradient](../gradient-descent/)** : descendre itérativement dans la direction opposée au gradient, $\theta \leftarrow \theta - \eta\,\nabla\mathcal{L}$
- **Descente de gradient stochastique / par mini-lots (SGD)** : estimer le gradient sur un petit lot d'exemples
- **Optimisation sous contraintes et multiplicateurs de Lagrange** : optimiser en respectant des conditions

## 5. [Théorie de l'information](../information-theory/)

Elle mesure la « quantité d'information » et l'« écart entre distributions » ; c'est l'origine des [fonctions de perte](../loss-function/) de l'apprentissage profond.

- **[Entropie](../entropy/) (entropy)** : la mesure de l'incertitude
- **[Entropie croisée](../cross-entropy/) (cross-entropy)** : la perte la plus courante en classification
- **[Divergence KL](../kl-divergence/)** : la « distance » entre deux distributions
- **Information mutuelle** : combien d'information deux variables partagent

{% include fviz/cross-entropy.html %}

---

**Termes clés :** [gradient](../gradient/), [règle de dérivation en chaîne](../chain-rule/), [multiplication matricielle](../matrix-multiplication/), [norme](../norm/), [SVD](../svd/), [variable aléatoire](../random-variable/), [théorème de Bayes](../bayes-theorem/), [maximum de vraisemblance](../maximum-likelihood/), [optimisation convexe](../convex-optimization/), [descente de gradient](../gradient-descent/), [entropie](../entropy/), [entropie croisée](../cross-entropy/), [divergence KL](../kl-divergence/).
