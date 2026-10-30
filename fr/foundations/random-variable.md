---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/random-variable/
title: "Variable aléatoire"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

Une variable aléatoire est une variable qui associe un **nombre** à un « résultat aléatoire » ; la façon dont ses valeurs se répartissent est décrite par une **loi de probabilité**. Une série temporelle peut être vue comme une suite de variables aléatoires qui évoluent dans le temps.

## Intuition

Le « résultat » d'un lancer de dé est au départ un événement abstrait, mais nous voulons calculer avec des nombres. La variable aléatoire sert de pont : elle **colle une étiquette numérique** sur chaque résultat possible, ce qui permet de parler de moyenne, de fluctuations et de loi de probabilité.

- Lancer de dé → la variable aléatoire $X$ prend les valeurs 1\~6 ;
- Pile ou face → on pose pile = 1, face = 0 ;
- La température de demain → une variable aléatoire continue.

Attention : une variable aléatoire n'est pas un nombre fixé, mais plutôt « une machine à probabilités dont le tirage n'a pas encore eu lieu » ; elle décrit **toutes les valeurs possibles et leurs probabilités**.

## Formulation mathématique

Une **variable aléatoire discrète** est décrite par sa **fonction de masse (PMF)** :

$$
p(x)=P(X=x),\qquad \sum_x p(x)=1
$$

Une **variable aléatoire continue** est décrite par sa **densité de probabilité (PDF)** ; les probabilités s'obtiennent par intégration :

$$
P(a\le X\le b)=\int_a^b f(x)\,dx,\qquad \int_{-\infty}^{\infty} f(x)\,dx=1
$$

Deux nombres clés caractérisent une variable aléatoire :

$$
\text{espérance (centre)}\quad \mu=\mathbb{E}[X]=\sum_x x\,p(x)\ \text{ou}\ \int x f(x)\,dx
$$
$$
\text{variance (dispersion)}\quad \sigma^2=\operatorname{Var}(X)=\mathbb{E}[(X-\mu)^2]
$$

Entre plusieurs variables aléatoires, la dépendance se décrit par la **loi jointe** et la **covariance** $\operatorname{Cov}(X,Y)$.

## Un exemple concret

Variable aléatoire de Bernoulli : un lancer unique, avec une probabilité de pile $p=0.3$ ; on pose $X=1$ pour pile et $X=0$ pour face.

$$
\mathbb{E}[X]=1\cdot 0.3+0\cdot 0.7=0.3
$$
$$
\operatorname{Var}(X)=p(1-p)=0.3\times 0.7=0.21
$$

```python
import numpy as np
X = (np.random.rand(100000) < 0.3).astype(int)  # Bernoulli(0.3)
print(round(X.mean(), 3))  # ≈ 0.300  ← espérance
print(round(X.var(),  3))  # ≈ 0.210  ← variance
```

## Pourquoi c'est important / où on l'utilise

- **L'atome de toute modélisation** : données, paramètres, bruit et prévisions sont tous modélisés comme des variables aléatoires.
- **[Perte](../loss-function/) et inférence** : le [maximum de vraisemblance](../maximum-likelihood/) et l'approche [bayésienne](../bayes-theorem/) manipulent des lois de variables aléatoires.
- **Modèles génératifs** : on considère les données comme tirées d'une certaine variable aléatoire et l'on apprend sa loi (VAE, modèles de diffusion, etc.).

## Intérêt pour la prévision de séries temporelles

- Une série temporelle $\{X_1,X_2,\dots,X_t\}$ est une suite de variables aléatoires ; prévoir, c'est estimer la loi de $X_{t+1}$ (ou son espérance).
- La **stationnarité** signifie que les propriétés statistiques de ces variables (moyenne, variance, autocorrélation) ne changent pas dans le temps — c'est une hypothèse de nombreuses méthodes classiques.
- En prévision ponctuelle, KUN (Kernel U-Net) fournit l'espérance conditionnelle $\mathbb{E}[X_{t+1}\mid \text{passé}]$ ; en prévision probabiliste, il produit directement les paramètres de la loi de $X_{t+1}$ (par exemple sa moyenne et sa variance).

## En résumé

- Variable aléatoire = associer un nombre à un résultat aléatoire ; sa loi (PMF / PDF) décrit la répartition de ses valeurs.
- L'espérance décrit le centre, la variance les fluctuations.
- Une série temporelle est une suite de variables aléatoires ; prévoir, c'est inférer la loi ou l'espérance des variables futures.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
