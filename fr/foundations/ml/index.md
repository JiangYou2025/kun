---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/ml/
title: "Fondements de l'apprentissage automatique"
lead: "Apprentissage supervisé / non supervisé, grandes familles de modèles, processus d'entraînement, généralisation et évaluation — les paradigmes de base pour qu'un modèle apprenne à partir des données. On pose le cadre et les concepts."
prev: /foundations/cs/
next: /foundations/dl/
math: true
---

> Ceci est une **carte conceptuelle** : elle indique « ce que fait l'apprentissage automatique, quels outils il emploie et comment juger qu'un modèle a bien appris » ; l'étude approfondie des [algorithmes](../algorithms/) est laissée aux manuels spécialisés.

## 1. Qu'est-ce que l'apprentissage automatique ?

Plutôt que d'écrire explicitement des règles, on **apprend à partir des données** une application $f_\theta: X \to y$.

- **[Apprentissage supervisé](../supervised-learning/)** : avec étiquettes, on apprend la correspondance entrée → sortie (régression / classification)
- **[Apprentissage non supervisé](../unsupervised-learning/)** : sans étiquettes, on cherche une structure ([partitionnement](../clustering/) / réduction de dimension)
- **[Apprentissage par renforcement](../reinforcement-learning/)** : on interagit avec un environnement pour maximiser la récompense cumulée
- La prévision de séries temporelles est généralement modélisée comme un problème d'**apprentissage supervisé** (fenêtre passée → valeurs futures)

## 2. Les grandes [familles de modèles](../model-families/)

- **[Modèles linéaires](../linear-model/)** : régression linéaire / logistique — un point de départ simple et interprétable
- **K plus proches voisins (KNN)** : un vote des « voisins »
- **[Arbres de décision](../decision-tree/)** : des partitions interprétables en if-else
- **Méthodes d'ensemble** : forêts aléatoires, [gradient boosting](../ensemble-gbdt/) (GBDT / XGBoost) — de solides références sur les données tabulaires
- **Machines à vecteurs de support ([SVM](../svm/))** : classification à marge maximale
- **Partitionnement et réduction de dimension** : K-means, [ACP](../pca/)

{% include fviz/kmeans.html %}

## 3. [Processus d'entraînement](../training-pipeline/)

- **[Fonction de perte](../loss-function/)** : MSE / MAE en régression, [entropie croisée](../cross-entropy/) en classification
- **[Optimisation](../optimization/)** : [descente de gradient](../gradient-descent/) ou solution analytique, pour minimiser la perte
- **Découpage des données** : entraînement / validation / test
- **[Validation croisée](../cross-validation/)** : un choix d'hyperparamètres plus robuste (**pour les séries temporelles, il faut découper dans l'ordre chronologique**, sans mélange aléatoire)
- **Réglage des hyperparamètres** : recherche par grille / aléatoire / bayésienne

{% include fviz/ts-split.html %}

## 4. La [généralisation](../generalization/) : le défi central

L'objectif est de bien se comporter sur des données **jamais vues**, et non de mémoriser l'ensemble d'entraînement.

- **Sous-apprentissage** : modèle trop simple, biais élevé
- **[Surapprentissage](../overfitting/)** : modèle trop complexe, qui mémorise le bruit, variance élevée
- **[Compromis biais–variance](../bias-variance/)** : trouver le bon niveau de complexité
- **[Régularisation](../regularization/)** : $\ell_1$ / $\ell_2$, [arrêt précoce](../early-stopping/), élagage — imposer des contraintes au modèle

{% include fviz/polyfit.html %}

## 5. [Métriques d'évaluation](../evaluation-metrics/)

- **Régression** : MSE, RMSE, MAE, MAPE, $R^2$
- **Classification** : exactitude, précision / rappel, F1, ROC-AUC
- **Essentiel** : la métrique doit correspondre à l'objectif métier et être rapportée sur l'**ensemble de test**

---

**Termes clés :** apprentissage [supervisé](../supervised-learning/) / [non supervisé](../unsupervised-learning/) / [par renforcement](../reinforcement-learning/), [modèle linéaire](../linear-model/), [arbre de décision](../decision-tree/), [ensemble (GBDT)](../ensemble-gbdt/), [SVM](../svm/), [partitionnement](../clustering/), [ACP](../pca/), [fonction de perte](../loss-function/), [validation croisée](../cross-validation/), [surapprentissage](../overfitting/), [compromis biais–variance](../bias-variance/), [régularisation](../regularization/), [métriques d'évaluation](../evaluation-metrics/).
