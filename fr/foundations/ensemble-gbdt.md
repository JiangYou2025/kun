---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/ensemble-gbdt/
title: "Apprentissage ensembliste / GBDT"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

L'idée de l'**apprentissage ensembliste (ensemble learning)** est de combiner de nombreux **modèles faibles** pour obtenir un modèle bien plus puissant que chacun d'eux pris isolément. Parmi ces méthodes, le **GBDT (gradient boosting sur arbres de décision)**, ainsi que ses implémentations XGBoost / LightGBM / CatBoost, constitue **la référence la plus solide sur les données tabulaires**, et compte aussi parmi les meilleures méthodes de prévision de séries temporelles.

## Intuition

Une personne seule peut se tromper, mais un groupe qui vote ou fait la moyenne est souvent plus juste que n'importe quel expert isolé — c'est la **sagesse des foules (wisdom of crowds)**. L'apprentissage ensembliste applique ce principe aux modèles : un [arbre de décision](../decision-tree/) seul est faible et instable, mais **en combinant intelligemment de nombreux arbres**, leurs erreurs se compensent et l'ensemble devient à la fois précis et stable.

Tout l'enjeu est dans la « manière de combiner ». Il existe deux grandes écoles, aux logiques radicalement différentes :

- **Bagging (ensachage)** : de nombreux modèles apprennent **en parallèle et indépendamment**, puis on fait la moyenne ou un vote — le but principal est de **réduire la variance**.
- **Boosting (renforcement)** : les modèles apprennent **en série, en relais**, chacun se consacrant à corriger les erreurs des précédents — le but principal est de **réduire le biais**.

## Deux paradigmes : Bagging contre Boosting

**Bagging (en parallèle, réduit la variance)**

Son représentant emblématique est la **forêt aléatoire (random forest)**. Ses deux sources d'aléa en sont l'essence :

1. **Échantillonnage bootstrap** : chaque arbre est entraîné sur un sous-ensemble obtenu par « tirage avec remise » dans le jeu d'entraînement, si bien que chaque arbre voit des données légèrement différentes.
2. **Sous-ensemble aléatoire de variables** : à chaque division, on ne choisit que parmi une partie des variables tirée au hasard, ce qui force les différents arbres à s'intéresser à des angles différents.

On entraîne ainsi des centaines d'arbres **peu corrélés** entre eux ; à la prédiction, on prend le vote majoritaire en classification et la moyenne en régression. Un arbre seul a une variance élevée (il est instable), mais en moyennant beaucoup d'arbres indépendants, **la variance chute fortement** et l'ensemble devient très robuste.

**Boosting (en série, réduit le biais)**

Les modèles ne sont plus indépendants : ils **se passent le relais l'un après l'autre**, chaque nouveau modèle venant combler ce que l'ensemble précédent n'a pas encore bien appris. Le boosting s'attaque directement au **biais** — il façonne progressivement une série de modèles faibles « presque bons » en un modèle fort. Le GBDT appartient à cette école.

(Sur le compromis entre biais et variance, voir le [compromis biais–variance](../bias-variance/) ; sur la place de ces modèles dans l'ensemble du paysage, voir les [familles de modèles](../model-families/).)

## Principe : le gradient boosting (GBDT)

Le **gradient boosting** est l'[algorithme](../algorithms/) de boosting le plus abouti. Son idée centrale est d'une rare élégance : **chaque nouvel arbre ajuste la part de l'erreur que le modèle actuel n'explique pas encore.**

Soit $F_{m-1}(x)$ le modèle d'ensemble actuel. On entraîne un nouvel arbre $h_m(x)$ pour ajuster ses **résidus / son [gradient](../gradient/) négatif**, puis on l'ajoute :

$$F_{m}(x) = F_{m-1}(x) + \eta\, h_m(x)$$

Version intuitive (avec une perte quadratique) : le $m$-ième arbre ajuste les **résidus**

$$r_i = y_i - F_{m-1}(x_i)$$

c'est-à-dire « ce qui manque encore ». Plus généralement, il ajuste le **gradient négatif** de la fonction de perte par rapport à la prédiction courante, d'où le nom de gradient boosting — ce qui lui permet de s'adapter à toutes sortes de fonctions de perte (régression, classification, quantiles, etc.).

Quelques hyperparamètres clés de la formule :

- **[Taux d'apprentissage](../learning-rate/) $\eta$ (learning rate)** : chaque arbre ne fait qu'un petit pas. Un $\eta$ petit → apprentissage plus lent mais plus stable et moins sujet au surapprentissage, généralement associé à davantage d'arbres.
- **Nombre d'arbres $M$ (`n_estimators`)** : combien d'arbres se passent le relais. Trop d'arbres mène au surapprentissage ; on l'associe souvent à l'arrêt précoce.
- **Profondeur des arbres (`max_depth`)** : chaque arbre de base est généralement très peu profond (apprenant faible) ; c'est le nombre qui fait la force.

Notez que $\eta$ et $M$ forment un couple qui se compense : **petit $\eta$ + grand $M$** donne souvent les meilleurs résultats, au prix d'un entraînement plus lent.

## Implémentations et régularisation

Écrire un GBDT à la main est lent ; en pratique, on utilise presque toujours l'une de ces trois bibliothèques hautement optimisées :

- **XGBoost** : classique, robuste, un incontournable des compétitions.
- **LightGBM** : basé sur des histogrammes, avec une croissance feuille par feuille, **rapide et économe en mémoire** — le premier choix pour les gros volumes.
- **CatBoost** : particulièrement bon sur les **variables catégorielles**, et peu exigeant en réglages.

Tous constituent **des références solides sur les données tabulaires** — face à un jeu de données structuré, commencer par un GBDT donne souvent un score difficile à battre.

Le GBDT est extrêmement expressif, donc **lutter contre le surapprentissage** est essentiel (voir [régularisation](../regularization/), [surapprentissage](../overfitting/)). Les leviers courants :

- `learning_rate` ($\eta$) : le diminuer stabilise.
- `n_estimators` ($M$) : combiné à l'**arrêt précoce** pour choisir automatiquement le meilleur nombre d'arbres.
- `max_depth` / `num_leaves` : limitent la complexité de chaque arbre.
- `subsample` / `colsample` : chaque arbre n'utilise qu'une partie des échantillons / variables (on réintroduit ainsi l'aléa du bagging), ce qui accélère et réduit la variance.

## Un exemple concret (sklearn / lightgbm)

```python
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=2000, n_features=20, noise=10, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

gbdt = GradientBoostingRegressor(
    n_estimators=300,     # M : nombre d'arbres
    learning_rate=0.05,   # η : taux d'apprentissage, petits pas prudents
    max_depth=3,          # chaque arbre de base est peu profond
    subsample=0.8,        # chaque arbre utilise au hasard 80 % des échantillons
    random_state=0,
)
gbdt.fit(Xtr, ytr)
print("MSE de test :", mean_squared_error(yte, gbdt.predict(Xte)))
```

Passer à LightGBM est presque identique, mais beaucoup plus rapide sur de gros volumes :

```python
import lightgbm as lgb
model = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=31, subsample=0.8)
model.fit(Xtr, ytr)
```

Essayez de diminuer `learning_rate` et d'augmenter `n_estimators` pour constater qu'« avancer à petits pas est plus stable ».

## Intérêt pour la prévision de séries temporelles (essentiel)

C'est l'un des terrains où le GBDT brille le plus en pratique. Transformer une série temporelle en tableau — en construisant des **variables retardées** ($t-1, t-7, t-28$), des **statistiques glissantes** (moyenne / maximum / écart-type des 7 derniers jours) et des **variables calendaires** (jour de la semaine, mois, jours fériés) — puis la donner à un GBDT est aujourd'hui l'une des recettes de prévision les plus performantes. La solution gagnante de la célèbre **compétition M5 de prévision des ventes** reposait essentiellement sur LightGBM.

Il excelle en particulier à **prévoir simultanément de nombreuses séries liées** (par exemple des milliers de produits / magasins) : on empile toutes les séries dans une grande table et on les apprend ensemble avec un seul GBDT, ce qui permet au modèle de partager les régularités d'une série à l'autre — simple et puissant.

Mais il existe un **avertissement important**, identique à celui des [arbres de décision](../decision-tree/) :

> **Le GBDT ne sait pas non plus extrapoler une tendance.**

Comme sa prédiction se ramène finalement à la moyenne d'une feuille, sa sortie **ne peut pas sortir de la plage vue à l'entraînement**. Face à une série en hausse durable, il va systématiquement **sous-estimer l'avenir**. La parade standard : **retirer d'abord la tendance / différencier, puis utiliser le GBDT** pour modéliser la partie stationnaire restante (ou construire un terme de tendance séparé et laisser le GBDT n'apprendre que la non-linéarité et la saisonnalité des résidus).

Enfin, l'évaluation doit impérativement se faire par **validation croisée pour séries temporelles** (découpage glissant dans l'ordre chronologique, en ne prédisant le futur qu'à partir du passé), **jamais par mélange aléatoire** — sinon on utilise de l'information future pour prédire le passé, ce qui provoque une fuite de données et gonfle artificiellement les résultats. Voir la [validation croisée](../cross-validation/).

## En résumé

- L'**apprentissage ensembliste** combine de nombreux modèles faibles en un modèle fort, grâce à la **sagesse des foules**.
- Deux paradigmes : le **bagging** (en parallèle, réduit la variance, comme la forêt aléatoire : bootstrap + variables aléatoires) contre le **boosting** (en série, réduit le biais).
- Le **GBDT** est le gradient boosting : chaque nouvel arbre ajuste les **résidus / le gradient négatif**, $F_m(x)=F_{m-1}(x)+\eta\,h_m(x)$ ; les clés sont le **taux d'apprentissage $\eta$, le nombre d'arbres $M$ et la profondeur**, et petit $\eta$ + grand $M$ est souvent optimal.
- Les implémentations **XGBoost / LightGBM / CatBoost** sont des **références solides sur données tabulaires** ; on lutte contre le surapprentissage avec `learning_rate` / `n_estimators` / `max_depth` / `subsample` (voir [régularisation](../regularization/), [surapprentissage](../overfitting/)).
- En séries temporelles, c'est une méthode de pointe sur des **variables retardées / glissantes / calendaires** (vainqueur de M5), particulièrement douée pour prévoir de nombreuses séries à la fois.
- **Avertissement crucial : pas d'extrapolation de tendance** — on **retire souvent la tendance / on différencie avant d'appliquer le GBDT**, et on évalue par **validation croisée pour séries temporelles**.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
