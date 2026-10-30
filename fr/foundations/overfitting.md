---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/overfitting/
title: "Surapprentissage"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

Le **surapprentissage** (overfitting) désigne un modèle excellent sur les données d'entraînement mais qui a pris le **bruit et les coïncidences fortuites** de ces données pour de vraies régularités, si bien qu'il se révèle mauvais sur des données nouvelles. C'est le mode d'échec le plus courant en [apprentissage automatique](../ml/) ; son pendant est le **sous-apprentissage** (le modèle, trop simple, n'apprend même pas bien les données d'entraînement).

## Intuition

Imaginez un élève qui prépare un examen :

- **L'élève en sous-apprentissage** : il n'a presque pas révisé et ne sait faire ni les exercices de base ni ceux de l'examen.
- **L'élève en surapprentissage** : il a appris par cœur, mot pour mot, les **réponses** des annales — il suffit qu'on change un nombre dans l'énoncé pour qu'il soit perdu. Il a retenu des réponses précises, pas une méthode de résolution.
- **L'élève qui [généralise](../generalization/) bien** : il a compris la méthode sous-jacente et réussit aussi les nouveaux exercices.

Le surapprentissage, c'est au fond du « par cœur » : le modèle a assez de capacité pour prendre le raccourci consistant à **mémoriser chaque exemple d'entraînement**, plutôt que de **dégager des régularités généralisables**.

## Comment le reconnaître

Le signal le plus fiable est **l'écart (gap) entre l'erreur d'entraînement et l'erreur de validation** :

$$
\text{écart de généralisation} = \text{erreur de validation} - \text{erreur d'entraînement}
$$

- Erreur d'entraînement faible, erreur de validation faible elle aussi et proche → bon ajustement.
- Erreur d'entraînement **très faible**, erreur de validation **nettement plus élevée** → **surapprentissage**, l'écart est grand.
- Erreurs d'entraînement et de validation **toutes deux élevées** → sous-apprentissage.

Lors de l'entraînement d'un [réseau de neurones](../neural-network/), tracez une **courbe d'apprentissage** (époques en abscisse, perte en ordonnée) : si la [perte](../loss-function/) d'entraînement continue de baisser alors que la perte de validation commence à **remonter**, ce point d'inflexion marque le début du surapprentissage — c'est aussi là que l'[arrêt précoce](../regularization/) doit intervenir.

## Pourquoi cela se produit

Du point de vue du [compromis biais–variance](../bias-variance/), surapprentissage = **variance élevée**. Causes fréquentes :

- **Capacité du modèle trop grande par rapport aux données** : plus de paramètres que d'exemples (polynômes de degré élevé, arbres très profonds, réseaux énormes).
- **Données d'entraînement trop peu nombreuses ou trop bruitées** : faute d'exemples, le modèle ne peut que coller à quelques points isolés.
- **Fuites ou redondances dans les variables** : le modèle s'accroche à une variable corrélée par hasard, sans lien causal.
- **Entraînement trop long** : à force d'itérations, le modèle glisse de l'apprentissage des régularités vers la mémorisation des exemples.

## Un exemple concret

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(1)
X = rng.uniform(0, 1, (120, 1))
y = (np.sin(6 * X).ravel() + rng.normal(0, 0.15, 120))
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=0)

for depth in [2, 5, None]:   # None = profondeur illimitée, divisions arbitraires
    m = DecisionTreeRegressor(max_depth=depth, random_state=0).fit(Xtr, ytr)
    tr = np.mean((m.predict(Xtr) - ytr) ** 2)
    te = np.mean((m.predict(Xte) - yte) ** 2)
    print(f"max_depth={str(depth):>4}  MSE entraînement={tr:.3f}  MSE test={te:.3f}")
```

L'arbre de profondeur illimitée a une MSE d'entraînement proche de 0 (il peut attribuer une feuille à chaque exemple), mais sa MSE de test est la plus élevée — c'est le phénomène de surapprentissage tel qu'on le décrit dans les manuels.

## Comment le combattre

- **Plus de données / augmentation de données** : le remède le plus fondamental.
- **[Régularisation](../regularization/)** : pénalités $\ell_1$ / $\ell_2$, [Dropout](../dropout/), élagage des arbres, limitation de `max_depth`.
- **Arrêt précoce** : interrompre l'entraînement quand la perte de validation commence à remonter.
- **Réduire la complexité du modèle** : moins de variables, un modèle moins profond.
- **Choisir les hyperparamètres par [validation croisée](../cross-validation/)** : sélectionner le modèle sur un ensemble de validation, pas sur l'ensemble d'entraînement.
- **[Méthodes d'ensemble](../ensemble-gbdt/)** : le bagging et les forêts aléatoires font baisser la variance en moyennant.

## Intérêt pour la prévision de séries temporelles

Dans les séries temporelles, le surapprentissage est particulièrement insidieux, car les points de données **ne sont pas indépendants** :

- **Fuite du futur (look-ahead bias)** : utiliser une information qui n'est pas encore disponible au moment de la prévision (par exemple des statistiques calculées sur le futur, ou un ensemble de validation tiré après mélange aléatoire) gonfle artificiellement le score de validation — c'est une forme de « surapprentissage par tricherie ». Découpez toujours dans l'ordre chronologique avec une [validation croisée pour séries temporelles](../cross-validation/).
- **Trop de variables retardées** : en entassant des dizaines voire des centaines de retards et de statistiques glissantes, on permet au modèle de mémoriser les fluctuations fortuites du passé. Privilégiez un petit nombre de variables ayant un sens métier, plus une régularisation.
- **Surapprentissage d'une seule période historique** : les événements exceptionnels d'une période (pandémie, promotions) sont pris pour la norme. Valider sur **plusieurs périodes** avec des fenêtres glissantes est plus robuste.

## En résumé

- Surapprentissage = bon à l'entraînement, mauvais au test ; il correspond à une **variance élevée**, à du par cœur.
- On le diagnostique avec **l'écart entre erreurs d'entraînement et de validation** et avec les **courbes d'apprentissage**.
- Arsenal : plus de données, régularisation, arrêt précoce, réduction de la complexité, validation croisée, méthodes d'ensemble.
- En prévision, le plus dangereux est la **fuite du futur** — le découpage chronologique est le minimum non négociable.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
