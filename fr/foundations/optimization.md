---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/optimization/
title: "Optimisation"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

Optimiser, c'est chercher, sous d'éventuelles contraintes, le jeu de variables qui rend une **fonction objectif** optimale (maximale ou minimale). Entraîner un modèle revient, au fond, à résoudre un problème d'optimisation — faire descendre la « perte » aussi bas que possible.

## Intuition

Les trois ingrédients de l'optimisation se comprennent avec l'analogie de « trouver le logement le moins cher » :

- **La fonction objectif** : ce que vous voulez minimiser (le prix) ;
- **Les variables de décision** : ce que vous pouvez ajuster (le quartier, la surface, l'étage) ;
- **Les contraintes** : les limites à respecter (le budget, le temps de trajet, le nombre de pièces).

Optimiser, c'est choisir, parmi toutes les solutions qui respectent les contraintes, celle qui rend l'objectif optimal. En apprentissage automatique, la fonction objectif est la **perte**, les variables de décision sont les **paramètres du modèle**, et les contraintes peuvent être un terme de régularisation ou des bornes sur les paramètres.

## Formulation mathématique

Forme générale :

$$
\min_{\theta}\ f(\theta)\quad
\text{s.t.}\quad g_i(\theta)\le 0,\quad h_j(\theta)=0
$$

- $f(\theta)$ — l'objectif / la [fonction de perte](../loss-function/) ;
- $\theta$ — les variables de décision (paramètres du modèle) ;
- $g_i\le 0$ — contraintes d'inégalité ; $h_j=0$ — contraintes d'égalité ;
- sans contrainte, il ne reste que $\min_\theta f(\theta)$, ce qui est précisément le cas de la plupart des problèmes d'apprentissage profond.

Condition nécessaire d'optimalité (sans contrainte, fonction dérivable) : **le [gradient](../gradient/) est nul**

$$
\nabla f(\theta^\*)=0
$$

Mais un point de gradient nul peut être un minimum, un maximum ou un point selle ; il faut une information du second ordre (la matrice hessienne) pour trancher.

## Un exemple concret

Minimisons $f(\theta)=\theta^2-4\theta+5$. En annulant la dérivée :

$$
f'(\theta)=2\theta-4=0\ \Rightarrow\ \theta^\*=2,\quad f(2)=1
$$

La dérivée seconde $f''=2>0$ confirme qu'il s'agit d'un minimum. Ce problème est [convexe](../convex-optimization/), donc $\theta^\*=2$ est aussi l'optimum global.

```python
import numpy as np
theta = 0.0          # on s'en approche par descente de gradient, sans résolution analytique
for _ in range(50):
    theta -= 0.1 * (2*theta - 4)
print(round(theta, 4))   # ≈ 2.0
```

Quand la fonction est trop complexe pour être résolue analytiquement (c'est le cas des réseaux de neurones), on recourt à des méthodes **itératives** comme la [descente de gradient](../gradient-descent/), qui s'approchent de la solution pas à pas.

## Pourquoi c'est important / où on l'utilise

- **Entraîner = optimiser** : presque tout « apprentissage » peut s'écrire comme « minimiser une certaine perte ».
- **Familles de méthodes** : solution analytique (moindres carrés), méthodes du premier ordre ([descente de gradient](../gradient-descent/), SGD, [Adam](../adam/)), méthodes du second ordre (méthode de Newton), optimisation sous contraintes (multiplicateurs de Lagrange, conditions KKT).
- **Convexe ou non convexe** : l'[optimisation convexe](../convex-optimization/) garantit un optimum global ; l'apprentissage profond est non convexe, on ne peut y viser qu'une solution « suffisamment bonne », d'où le besoin de nombreuses astuces d'ingénierie.

## Intérêt pour la prévision de séries temporelles

- Ajuster un ARIMA ou entraîner KUN (Kernel U-Net), c'est résoudre un problème d'optimisation : minimiser une perte de prévision (MSE, MAE, etc.).
- L'idée d'optimisation sous contraintes apparaît dans les modèles de prévision régularisés ou soumis à des contraintes de monotonie / de non-négativité.
- La recherche d'hyperparamètres ([taux d'apprentissage](../learning-rate/), longueur de fenêtre, profondeur du réseau) est elle-même un problème d'**optimisation externe**, souvent résolu par recherche sur grille ou optimisation [bayésienne](../bayes-theorem/).

## En résumé

- Optimisation = rendre une fonction objectif optimale sous contraintes ; ses trois ingrédients sont l'objectif, les variables et les contraintes.
- Sans contrainte, la condition nécessaire d'optimalité est un gradient nul.
- Les problèmes convexes sont confortables ; les problèmes non convexes (l'apprentissage profond) reposent sur des méthodes itératives et des astuces : « entraîner un modèle », c'est « résoudre un problème d'optimisation ».

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
