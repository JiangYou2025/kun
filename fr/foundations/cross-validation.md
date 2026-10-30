---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/cross-validation/
title: "Validation croisée"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

La **validation croisée (Cross-Validation, CV)** consiste à **découper les données plusieurs fois** et à faire jouer à tour de rôle le rôle d'ensemble de validation à des parties différentes, afin d'**évaluer les modèles, de choisir entre eux et de régler les hyperparamètres de façon plus robuste**. Pour les séries temporelles, le découpage doit **respecter strictement l'ordre chronologique** : on ne mélange jamais les données au hasard.

## Intuition

Supposons que vous ne fassiez qu'un seul découpage « entraînement / test » : 80 % pour l'entraînement, 20 % pour le test, et vous obtenez un score. Le problème, c'est que **ce score contient une part de chance**.

Si ces 20 % se trouvent être « faciles », le score sera trop élevé ; s'ils sont « difficiles », il sera trop bas. Changez la graine aléatoire et le score peut passer de 0,90 à 0,83. Si vous comparez deux modèles ou réglez un hyperparamètre à partir d'un score unique aussi **instable**, vous risquez fort de vous tromper — la différence observée n'est peut-être que du bruit.

**L'idée centrale de la validation croisée** : plutôt que de découper une seule fois et de s'en remettre à la chance, **on découpe de nombreuses fois, de sorte que chaque partie des données serve une fois d'ensemble de validation**, puis on fait la **moyenne** des scores obtenus. La moyenne dilue la part de chance, et l'estimation devient plus stable et plus fiable.

Une analogie : pour juger le niveau d'un élève, un seul examen peut être trompeur ; cinq examens dont on fait la moyenne donnent une image bien plus proche de son niveau réel.

## Validation croisée à K plis (k-fold)

La méthode la plus courante est la **validation croisée à K plis**, qui procède ainsi :

1. Répartir les données au hasard (attention : pas au hasard pour les séries temporelles, voir plus bas) en $k$ parts égales, chacune appelée un **pli (fold)**. On prend couramment $k=5$ ou $k=10$.
2. Tour 1 : le pli 1 sert d'ensemble de validation, les $k-1$ autres plis d'ensemble d'entraînement ; on entraîne, on évalue, et on obtient $\text{score}_1$.
3. Tour 2 : le pli 2 sert d'ensemble de validation, les autres d'ensemble d'entraînement ; on obtient $\text{score}_2$.
4. … et ainsi de suite jusqu'au pli $k$, qui donne $\text{score}_k$.
5. On fait la **moyenne** des $k$ scores, qui constitue le score de validation croisée du modèle :

$$\text{CV score} = \frac{1}{k}\sum_{i=1}^{k}\text{score}_i$$

Ainsi, chaque échantillon **sert exactement une fois de donnée de validation** et participe aussi à l'entraînement : les données sont bien exploitées et l'estimation est plus stable. Outre la moyenne, on regarde aussi l'**écart-type** des $k$ scores — il indique si les performances du modèle sont stables ou non.

La **LOOCV (validation croisée leave-one-out)** est le cas extrême de la validation à K plis : on pose $k=n$ (le nombre total d'échantillons) et l'on ne garde à chaque fois qu'**un seul** échantillon pour la validation, tout le reste servant à l'entraînement. Elle utilise presque toutes les données pour l'entraînement et son estimation est peu biaisée, mais elle exige $n$ entraînements, un coût de calcul énorme, et sa variance est plutôt élevée ; on la réserve donc généralement aux petits jeux de données.

## La CV sert à choisir un modèle et à régler les hyperparamètres, pas à donner la note finale

C'est le point que les débutants confondent le plus souvent : **la validation croisée est un outil de « sélection de modèle » et de « réglage des hyperparamètres », pas un outil qui fournit la note finale non biaisée.**

Pourquoi ? Parce qu'en utilisant le score de CV pour **choisir à répétition** les meilleurs hyperparamètres, vous « flattez » en réalité ces plis de validation — la configuration retenue est, dans une certaine mesure, en [surapprentissage](../overfitting/) sur les données de validation. Le score de CV est donc **légèrement optimiste**.

La bonne procédure découpe les données en trois blocs :

- **Ensemble d'entraînement** : pour ajuster les paramètres du modèle.
- **Ensemble de validation (produit par la rotation de la CV à l'intérieur des données d'entraînement)** : pour régler les hyperparamètres et choisir le modèle.
- **Ensemble de test (mis de côté et jamais touché pendant tout le processus)** : utilisé **une seule fois**, à la toute fin, comme estimation non biaisée de la véritable capacité de généralisation.

En une phrase : **la CV vous aide à « choisir », l'ensemble de test mis de côté vous aide à « rendre compte du résultat »**. C'est aussi le principe clé du découpage des données dans le [pipeline d'entraînement](../training-pipeline/), et il conditionne directement la fiabilité de l'évaluation de la [généralisation](../generalization/) du modèle.

## Un exemple concret

Pour des données ordinaires (qui ne sont pas des séries temporelles), `cross_val_score` de sklearn règle l'affaire en une ligne :

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(scores)            # 5 scores, par exemple [0.91 0.88 0.90 0.87 0.92]
print(scores.mean())     # moyenne : 0.896  ← c'est le score de CV
print(scores.std())      # écart-type : plus il est petit, plus c'est stable
```

Pour les **séries temporelles**, il faut en revanche utiliser `TimeSeriesSplit`, qui garantit que l'ensemble d'entraînement précède toujours l'ensemble de validation :

```python
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

tscv = TimeSeriesSplit(n_splits=5)          # découpage vers l'avant, dans l'ordre chronologique
scores = cross_val_score(model, X, y, cv=tscv, scoring="neg_mean_absolute_error")
print(-scores.mean())                        # MAE moyenne
```

Attention : les plis produits par `TimeSeriesSplit` **ne sont pas** des blocs aléatoires de même taille et sans recouvrement, mais une structure glissante où « l'ensemble d'entraînement s'allonge et l'ensemble de validation est toujours dans le futur ».

## Intérêt pour la prévision de séries temporelles

C'est la partie **la plus importante** de cette section. Les séries temporelles ont une « direction du temps » : le futur ne peut pas servir à prédire le passé, et la validation croisée exige donc un traitement particulier.

**Pourquoi la validation à K plis ordinaire échoue-t-elle ?** Elle commence par **mélanger** les données avant de former les plis. L'ensemble d'entraînement d'un pli peut alors contenir des données **postérieures** aux échantillons de validation. Le modèle a en quelque sorte « jeté un œil au futur » avant de prédire le passé : c'est la **fuite d'information du futur (look-ahead leakage / data leakage)**. Résultat : le score de validation croisée est **gonflé** de façon absurde, mais dès la mise en production, face à un futur réellement inconnu, le modèle s'effondre.

**La bonne méthode : la validation glissante / vers l'avant (walk-forward / rolling-origin).** On s'assure toujours que **le temps de l'ensemble d'entraînement < le temps de l'ensemble de validation**. On découpe l'axe du temps, du plus ancien au plus récent, en plusieurs segments et l'on avance pas à pas :

```
Tour 1  entraînement[1..100]   validation[101..120]
Tour 2  entraînement[1..120]   validation[121..140]
Tour 3  entraînement[1..140]   validation[141..160]
...
```

C'est exactement la logique de `TimeSeriesSplit` : chaque tour simule la situation réelle où l'on « se tient à un instant donné et prédit le futur à partir du passé ».

**Fenêtre croissante ou fenêtre glissante** : deux variantes courantes.

- **Fenêtre croissante (expanding window)** : l'ensemble d'entraînement **s'allonge** sans cesse et intègre tout l'historique (comme ci-dessus). Adaptée lorsque les régularités des données sont stables et que l'on veut exploiter le plus d'historique possible.
- **Fenêtre glissante (sliding window)** : l'ensemble d'entraînement a une **longueur fixe** et se déplace en bloc avec le temps (on abandonne les données les plus anciennes, on ajoute les plus récentes). Adaptée lorsque les régularités **dérivent** et que les données récentes sont plus représentatives.

**gap / embargo (intervalle / zone tampon)** : lorsque les variables explicatives contiennent des informations « à cheval sur plusieurs pas », comme des moyennes mobiles ou des retards, la fin de l'ensemble d'entraînement et le début de l'ensemble de validation peuvent **se chevaucher dans le temps** et provoquer une fuite. La solution consiste à **laisser un petit intervalle vide** (gap / embargo) entre l'entraînement et la validation, pour que des échantillons voisins ne « déteignent » pas l'un sur l'autre.

## Pièges courants

- **Appliquer une validation à K plis mélangée au hasard à une série temporelle** : cela provoque directement une fuite du futur, un score gonflé et un effondrement dès la mise en production. Les séries temporelles se découpent toujours dans l'ordre chronologique.
- **Faire le `fit` de la mise à l'échelle sur l'ensemble des données** : calculer moyenne et écart-type (ou normaliser) sur toutes les données avant le découpage revient à faire fuiter l'information des ensembles de validation et de test vers l'entraînement. La bonne pratique consiste à **faire le `fit` uniquement sur le pli d'entraînement**, puis à appliquer `transform` au pli de validation — en le plaçant dans un `Pipeline`, c'est géré automatiquement par la CV.
- **Régler les hyperparamètres sur l'ensemble de test** : dès que l'ensemble de test a été « vu » et utilisé pour choisir des paramètres, il n'est plus non biaisé et le résultat devient trop optimiste. L'ensemble de test ne sert qu'une fois, tout à la fin.
- **Ignorer la variance des scores entre plis** : ne regarder que la moyenne sans l'écart-type peut masquer le fait que le modèle est très instable sur certaines périodes.

## Résumé

- Validation croisée = découper plusieurs fois, valider à tour de rôle, faire la moyenne : on obtient une évaluation **plus robuste** qu'avec un découpage unique.
- K plis : on divise en $k$ parts, on en garde une pour la validation à tour de rôle et on moyenne les scores $\frac1k\sum_i\text{score}_i$ ; la LOOCV en est la version extrême avec $k=n$.
- La CV sert à **choisir un modèle / régler les hyperparamètres** ; la note finale non biaisée repose sur un **ensemble de test mis de côté**.
- Les séries temporelles **ne doivent jamais être mélangées au hasard** — il faut une validation **vers l'avant / glissante** comme `TimeSeriesSplit`, garantir que le temps d'entraînement < le temps de validation et ajouter si nécessaire un gap/embargo.

Notions liées : [fonction de perte](../loss-function/) · [pipeline d'entraînement](../training-pipeline/) · [surapprentissage](../overfitting/) · [généralisation](../generalization/)

---

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
