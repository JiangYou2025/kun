---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/evaluation-metrics/
title: "Métriques d'évaluation"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

Les **métriques d'évaluation (evaluation metrics)** sont les **critères quantitatifs** qui mesurent la qualité d'un modèle. Une métrique doit **correspondre à l'objectif métier**, et elle doit être rapportée sur un **jeu de test** que le modèle n'a jamais vu.

## Intuition

**Une métrique est la « règle graduée » avec laquelle vous notez — choisissez la mauvaise règle, et vous jugerez mal même le meilleur des modèles.**

Un même modèle peut conduire à des conclusions opposées selon la métrique utilisée. Prenons un modèle de prévision des ventes : son erreur moyenne semble faible, mais il se trompe lourdement sur quelques jours de grosse promotion ; si ce que votre activité redoute le plus, c'est une « erreur d'approvisionnement pendant les promotions », alors ce beau score d'« erreur moyenne faible » ne vaut rien.

Apprendre les métriques d'évaluation, ce n'est donc pas seulement retenir des formules, c'est comprendre **ce que mesure chaque règle, à quoi elle est sensible, et quand elle peut tromper**, puis **choisir la bonne règle selon l'objectif métier**.

## Métriques de régression

Une tâche de régression prédit une **valeur continue** (température, ventes, cours de bourse…). Notons $y_i$ la valeur réelle, $\hat y_i$ la prédiction et $n$ le nombre d'échantillons.

**Erreur absolue moyenne MAE (Mean Absolute Error)**

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}\left|y_i-\hat y_i\right|$$

La taille moyenne de l'erreur en valeur absolue, dans la même unité que $y$ : intuitive et **peu sensible aux valeurs aberrantes**.

**Erreur quadratique moyenne MSE (Mean Squared Error)**

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2$$

On élève au carré avant de moyenner, ce qui **pénalise fortement les grandes erreurs** ; mais l'unité est le carré de celle de $y$, ce qui complique l'interprétation.

**Racine de l'erreur quadratique moyenne RMSE (Root Mean Squared Error)**

$$\text{RMSE} = \sqrt{\text{MSE}}$$

Après la racine, **l'unité est la même que celle de $y$** : on conserve la « forte pénalisation des grandes erreurs » tout en facilitant l'interprétation. C'est l'une des métriques de régression les plus utilisées.

**Coefficient de détermination $R^2$**

$$R^2 = 1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}$$

Il indique dans quelle mesure le modèle fait mieux que « prédire simplement la moyenne ». $R^2=1$ est parfait, $R^2=0$ équivaut à deviner la moyenne, et il **peut être négatif** (pire que la moyenne).

**Erreur absolue moyenne en pourcentage MAPE**

$$\text{MAPE} = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i-\hat y_i}{y_i}\right|$$

Elle exprime l'erreur **en pourcentage**, ce qui permet de comparer des séries d'ordres de grandeur différents ; mais lorsque $y_i$ est proche de 0, le dénominateur minuscule fait **exploser** la valeur — c'est son point faible fatal.

La **MAPE symétrique (sMAPE)** remplace le dénominateur par la demi-somme de la valeur réelle et de la prédiction, ce qui atténue le problème de la division par de petites valeurs :

$$\text{sMAPE} = \frac{1}{n}\sum_{i=1}^{n}\frac{|y_i-\hat y_i|}{(|y_i|+|\hat y_i|)/2}$$

L'**erreur absolue moyenne normalisée MASE (Mean Absolute Scaled Error)** divise l'erreur par celle d'une **référence naïve** (par exemple « prédire avec la valeur de l'instant précédent ») et donne un score relatif sans dimension : $\text{MASE}<1$ signifie que le modèle fait mieux que la référence naïve, $>1$ qu'il fait moins bien. Elle est robuste aux valeurs nulles et particulièrement courante en séries temporelles.

## Métriques de classification

Une tâche de classification prédit une **classe** (« oui / non », « fraude / normal »…).

**L'exactitude (accuracy)** = la proportion de prédictions correctes. Simple, mais extrêmement trompeuse en cas de **déséquilibre des classes** : si 99 % des échantillons sont « normaux », un modèle inutile qui « prédit toujours normal » atteint 99 % d'exactitude, sans détecter une seule fraude.

Les métriques fondées sur la **matrice de confusion** (vrais positifs TP, faux positifs FP, vrais négatifs TN, faux négatifs FN) sont plus fiables :

$$\text{precision (précision)} = \frac{TP}{TP+FP},\qquad \text{recall (rappel)} = \frac{TP}{TP+FN}$$

- **Précision** : parmi ce que vous déclarez « positif », combien le sont vraiment ? (on veut « éviter les fausses alertes »)
- **Rappel** : parmi tous les vrais positifs, combien en avez-vous détecté ? (on veut « ne rien laisser passer »)

Les deux évoluent généralement en sens inverse ; on les combine avec le **score F1** (la **moyenne harmonique** de la précision et du rappel) :

$$F_1 = \frac{2\cdot\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}}$$

**Courbe ROC / AUC** : en faisant varier le seuil de décision, on trace la courbe « taux de vrais positifs contre taux de faux positifs » ; l'aire sous la courbe, l'**AUC**, mesure la capacité globale du modèle à ordonner les exemples : $0.5$ équivaut au hasard, $1.0$ est parfait.

## Fonction de perte contre métrique d'évaluation

Ces deux notions se ressemblent beaucoup, mais leurs rôles diffèrent :

- La **[fonction de perte](../loss-function/)** est ce que l'on **optimise** (minimise) pendant l'entraînement ; elle doit être **différentiable** pour que la [descente de gradient](../gradient-descent/) fonctionne (par exemple MSE, [entropie croisée](../cross-entropy/)).
- La **métrique d'évaluation** est le score **rapporté** aux humains après l'entraînement ; elle **n'a pas besoin d'être différentiable** et se choisit au plus près du métier (par exemple MAE, F1, AUC, MASE).

Exemple : en classification, on entraîne avec l'**entropie croisée** comme perte (différentiable, facile à optimiser), mais on rapporte souvent le **F1 / l'AUC** (non différentiables, mais plus représentatifs de « a-t-on détecté la fraude »). En une phrase : **la fonction de perte est « destinée à l'optimiseur pendant l'entraînement », la métrique d'évaluation est « destinée aux humains après l'entraînement ».**

## Un exemple concret

```python
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             r2_score, f1_score, classification_report)
import numpy as np

# Régression
y_true = [3.0, 5.0, 2.5, 7.0]
y_pred = [2.8, 4.5, 3.0, 6.0]
print("MAE :", mean_absolute_error(y_true, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
print("R2  :", r2_score(y_true, y_pred))

# Classification
yc_true = [0, 1, 1, 0, 1]
yc_pred = [0, 1, 0, 0, 1]
print("F1  :", f1_score(yc_true, yc_pred))
print(classification_report(yc_true, yc_pred))   # précision / rappel / F1 d'un seul coup d'œil
```

## Pourquoi c'est important : coller à l'objectif métier

Multiplier les métriques n'est pas un but ; il faut **viser ce qui compte vraiment pour vous** :

- En dépistage médical, on redoute avant tout **le cas manqué** → on regarde d'abord le **rappel**.
- En filtrage anti-spam, on redoute avant tout **de bloquer un e-mail légitime** → on regarde d'abord la **précision**.
- En prévision de stocks, les grandes erreurs coûtent cher → on utilise la **RMSE**, qui **pénalise fortement les grandes erreurs**.
- Pour expliquer à sa direction « de combien d'unités on se trompe en moyenne » → on utilise la **MAE**, dont l'unité est intuitive.

Choisir la mauvaise métrique, c'est optimiser un objectif « joli sur le papier mais inutile ».

## Intérêt pour la prévision de séries temporelles

- Pour la **prévision de valeurs numériques**, on utilise généralement la **RMSE / MAE** : la RMSE est plus sensible aux grosses erreurs occasionnelles, la MAE est plus robuste et plus facile à interpréter.
- **Prudence avec la MAPE** : dès qu'une série contient des **valeurs nulles ou très petites**, la MAPE est amplifiée jusqu'à devenir absurde. On lui préfère alors la **sMAPE** ou la **MASE**, plus stables.
- **Privilégier la MASE** : elle compare l'erreur du modèle à celle de la **prévision naïve (prendre la valeur de la période précédente comme prévision)** et répond naturellement à la question la plus importante : « de combien mon modèle fait-il mieux que “ne rien faire” ? »
- **Évaluer impérativement dans l'ordre chronologique, hors échantillon (sur le futur)** : entraîner sur le passé et noter sur une période future jamais vue ; sinon le score n'a aucun sens (voir la validation progressive dans [validation croisée](../cross-validation/)).
- **Suivre l'erreur par horizon (per-horizon)** : la prévision du pas suivant est généralement précise, mais l'erreur **augmente avec l'horizon de prévision**. Rapporter **séparément** l'erreur de chaque horizon est plus informatif qu'une seule moyenne globale.
- **Toujours comparer à une référence naïve** : avant tout modèle sophistiqué, vérifiez qu'il bat réellement la référence naïve « prédire aujourd'hui avec la valeur d'hier » ; sinon, sa complexité ne vaut rien.

## En résumé

- Une métrique d'évaluation = la règle qui juge la qualité d'un modèle ; **une mauvaise règle conduit à de mauvais jugements** ; elle doit correspondre à l'objectif métier et être rapportée sur le **jeu de test**.
- Régression : MAE (robuste), MSE / RMSE (pénalisent fortement les grandes erreurs, RMSE dans la même unité), $R^2$, MAPE (craint les zéros), sMAPE / MASE (plus stables, comparables).
- Classification : exactitude (trompeuse en cas de déséquilibre), précision, rappel, F1, matrice de confusion, ROC / AUC.
- La **fonction de perte** est optimisée (différentiable), la **métrique d'évaluation** est rapportée (pas forcément différentiable) — ne les confondez pas.
- Séries temporelles : évaluer dans l'ordre chronologique sur le futur, suivre l'erreur par horizon, se méfier de la MAPE, privilégier la MASE, et **toujours comparer à la référence naïve**.

Notions liées : [fonction de perte](../loss-function/) · [chaîne d'entraînement](../training-pipeline/) · [surapprentissage](../overfitting/) · [généralisation](../generalization/)

---

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
