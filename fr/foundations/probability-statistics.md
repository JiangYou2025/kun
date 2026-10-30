---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/probability-statistics/
title: "Probabilités et statistiques"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

Les probabilités décrivent mathématiquement **l'incertitude** (on connaît la loi, on anticipe les résultats) ; les statistiques font le chemin inverse et **infèrent la loi à partir des données** (on connaît les résultats, on remonte au mécanisme). Prévoir, c'est fondamentalement composer avec l'incertitude : ces deux disciplines sont la langue de ce métier.

## Intuition

Probabilités et statistiques sont les deux faces d'une même pièce :

- **Probabilités (déduction)** : sachant que la pièce est équilibrée, on demande « quelle est la probabilité d'obtenir 7 piles sur 10 lancers ? » — on va du modèle aux données.
- **Statistiques (induction)** : on observe seulement 7 piles et 3 faces, et l'on demande à l'inverse « la pièce est-elle équilibrée, que vaut à peu près $p$ ? » — on va des données au modèle.

L'[apprentissage automatique](../ml/) utilise les deux : on **suppose** que les données sont engendrées par un certain modèle probabiliste (probabilités), on **estime** ensuite les paramètres du modèle à partir des données observées (statistiques), et l'on finit par porter, avec le modèle, un jugement assorti d'incertitude sur de nouvelles situations.

## Formulation mathématique

**Axiomes des probabilités** : $0\le P(A)\le 1$, $P(\Omega)=1$, et les probabilités d'événements incompatibles s'additionnent.

**Probabilité conditionnelle et indépendance** :

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad A\perp B\iff P(A\cap B)=P(A)P(B)
$$

Espérance et variance d'une [variable aléatoire](../random-variable/) (qui décrivent son « centre » et sa « dispersion ») :

$$
\mathbb{E}[X]=\sum_i x_i\,p_i,\qquad
\operatorname{Var}(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]
$$

**Lois usuelles** : Bernoulli, binomiale, Poisson (discrètes) ; normale $\mathcal{N}(\mu,\sigma^2)$, uniforme, exponentielle (continues). La loi normale est omniprésente grâce au **théorème central limite** (la somme d'un grand nombre de facteurs indépendants tend vers une loi normale).

**Inférence statistique** : on estime la moyenne de la population par la moyenne empirique $\bar x$, et l'on quantifie « à quel point on est sûr » avec des intervalles de confiance et des tests d'hypothèses.

{% include fviz/clt.html %}

## Un exemple concret

On lance un dé équilibré à six faces ; $X$ est le nombre de points obtenu.

$$
\mathbb{E}[X]=\frac{1+2+3+4+5+6}{6}=3.5
$$
$$
\operatorname{Var}(X)=\frac{1}{6}\sum_{k=1}^{6}(k-3.5)^2\approx 2.92
$$

L'espérance 3.5 est la moyenne à long terme (même si aucun lancer ne peut donner 3.5) ; la variance mesure l'ampleur des fluctuations.

```python
import numpy as np
rolls = np.random.randint(1, 7, size=100000)
print(round(rolls.mean(), 3))   # ≈ 3.5   loi des grands nombres : la moyenne empirique converge vers l'espérance
print(round(rolls.var(),  3))   # ≈ 2.92
```

C'est précisément la **loi des grands nombres** : plus l'échantillon est grand, plus la moyenne empirique se rapproche de la véritable espérance.

## Pourquoi c'est important / où on l'utilise

- **Cadre de modélisation** : le [maximum de vraisemblance](../maximum-likelihood/) et l'[inférence bayésienne](../bayes-theorem/) reposent sur les probabilités.
- **[Fonctions de perte](../loss-function/)** : l'[entropie croisée](../cross-entropy/) et la log-vraisemblance négative viennent du point de vue probabiliste.
- **Évaluation et [généralisation](../generalization/)** : séparation entraînement / test, [validation croisée](../cross-validation/), intervalles de confiance, tests A/B relèvent tous des méthodes statistiques.

## Intérêt pour la prévision de séries temporelles

- Une série temporelle peut être vue comme une suite de [variables aléatoires](../random-variable/) qui évolue dans le temps ; stationnarité, autocorrélation et loi du bruit s'expriment toutes dans le langage des probabilités.
- La **prévision probabiliste** ne donne pas seulement une estimation ponctuelle mais aussi une loi ou un intervalle — elle répond à « quelle est la probabilité que la valeur future tombe dans telle plage ? », ce qui est crucial pour les décisions face au risque.
- Pour évaluer les prévisions de KUN (Kernel U-Net), il faut des indicateurs statistiques (RMSE, MAE, taux de couverture) accompagnés d'une quantification de l'incertitude pour juger si le modèle est vraiment fiable.

## En résumé

- Probabilités : du modèle vers les données ; statistiques : des données vers le modèle — la prévision utilise les deux.
- Espérance, variance, probabilité conditionnelle et lois usuelles sont les outils de base.
- Ils sous-tendent le maximum de vraisemblance, l'approche bayésienne, l'entropie croisée et la quantification de l'incertitude des prévisions.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
