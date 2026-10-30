---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/unsupervised-learning/
title: "Apprentissage non supervisé"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

L'**apprentissage non supervisé (unsupervised learning)** désigne la situation où les données d'entraînement **n'ont aucune étiquette** : il n'y a pas de « bonne réponse » à laquelle se référer, et le but du modèle est de **découvrir par lui-même la structure et les régularités cachées** dans les données.

## Intuition

Si l'[apprentissage supervisé](../supervised-learning/) ressemble à « faire des exercices corrigés par un professeur, avec le corrigé sous les yeux », l'apprentissage non supervisé, c'est **sans professeur** : vous avez devant vous une montagne de données, personne ne vous dit ce qui est juste ni à quelle catégorie appartient chaque élément, et vous devez observer, généraliser et trouver vous-même la logique.

Un exemple de la vie quotidienne : vous videz sur la table un panier de fruits sans étiquette, et personne ne vous dit comment ils s'appellent. Pourtant, vous les **répartissez naturellement en plusieurs tas** selon « la taille, la couleur, la forme » — les rouges et ronds d'un côté, les jaunes et allongés de l'autre. Vous ne connaissez pas le « vrai nom » de chaque tas, mais vous avez découvert la **structure d'organisation** propre aux données. C'est exactement ce que fait l'apprentissage non supervisé.

Faute d'étiquettes, le but de l'apprentissage non supervisé n'est pas de « prédire juste », mais de « **révéler les motifs intrinsèques des données** ».

## Les principales tâches

L'apprentissage non supervisé comprend quelques tâches typiques :

- **Partitionnement (clustering)** : regrouper automatiquement les échantillons similaires. L'[algorithme](../algorithms/) emblématique est **K-means**. Voir [Partitionnement](../clustering/).
- **Réduction de dimension (dimensionality reduction)** : compresser des données de grande dimension en basse dimension en conservant le plus d'information possible, pour faciliter la visualisation et la modélisation ultérieure. La méthode emblématique est l'analyse en composantes principales, voir [ACP (analyse en composantes principales)](../pca/).
- **Détection d'anomalies (anomaly detection)** : repérer les « points aberrants » nettement différents de la majorité des échantillons, comme une fraude à la carte bancaire ou une panne d'équipement.
- **Estimation de densité (density estimation)** : estimer la distribution des données dans l'espace, pour comprendre « où les données apparaissent habituellement ».

## Principe (intuition mathématique)

Les objectifs d'[optimisation](../optimization/) diffèrent selon les tâches, mais tous tournent autour de la « mesure de la similarité / de l'information » :

**Partitionnement** : répartir $n$ échantillons en $K$ groupes de sorte que la **distance intra-groupe soit aussi petite que possible** (les échantillons d'un même groupe se ressemblent). K-means minimise la somme des carrés des distances de chaque échantillon au centre $\mu_k$ de son groupe :

$$
\min_{\{\mu_k\}}\ \sum_{k=1}^{K}\ \sum_{x \in C_k} \lVert x - \mu_k \rVert^2
$$

où $C_k$ est le $k$-ième groupe et $\mu_k$ son centre.

**Réduction de dimension (ACP)** : chercher un nouveau jeu de directions de coordonnées tel que la **variance des données projetées soit maximale** — plus la variance est grande, plus on conserve d'information. Cela revient à trouver les vecteurs propres associés aux plus grandes valeurs propres de la matrice de covariance. L'intuition : garder les quelques directions où les données « s'étalent le plus », et jeter celles où elles ne varient presque pas.

Remarquez : dans aucun de ces deux objectifs **n'apparaît l'étiquette $y$**, seulement les données $x$ elles-mêmes — c'est la marque même du « non supervisé ».

## Un exemple concret

Faisons un partitionnement K-means avec `scikit-learn`. Notez qu'on ne fournit que `X`, **sans aucune étiquette** :

```python
from sklearn.cluster import KMeans
import numpy as np

# Seulement l'entrée X, pas de y ! Chaque ligne contient les deux variables d'un échantillon
X = np.array([
    [1, 2], [1.5, 1.8], [1, 0.6],     # semble former un groupe
    [8, 8], [9, 11], [8.5, 9],        # semble former un autre groupe
])

model = KMeans(n_clusters=2, n_init=10, random_state=0)
labels = model.fit_predict(X)   # répartit automatiquement les échantillons en 2 groupes

print(labels)            # par exemple [0 0 0 1 1 1]
print(model.cluster_centers_)   # les centres des deux groupes
```

Le modèle ignore quel est le « bon regroupement » ; il trouve simplement par lui-même, à partir des distances entre échantillons, deux centres de concentration. Avec l'ACP, c'est pareil : `from sklearn.decomposition import PCA`, puis `PCA(n_components=2).fit_transform(X)` suffit pour ramener des données de grande dimension à 2 dimensions, là encore sans aucune étiquette.

## Pourquoi c'est important (où l'utiliser)

Dans le monde réel, **les données étiquetées coûtent souvent cher** — il faut les annoter à la main, ce qui prend du temps et de l'argent ; **les données non étiquetées, elles, sont massives et faciles à obtenir**. L'apprentissage non supervisé permet d'extraire directement de la valeur de ces données brutes :

- Le **partitionnement** pour segmenter une clientèle, classer des documents, regrouper des images.
- La **réduction de dimension** pour compresser, débruiter et explorer visuellement les données.
- La **détection d'anomalies** pour découvrir fraudes, intrusions et pannes.

C'est souvent la **première étape** d'un processus de modélisation : comprendre d'abord la structure des données de façon non supervisée, puis décider du traitement à suivre. La différence fondamentale avec l'[apprentissage supervisé](../supervised-learning/) (avec étiquettes, qui apprend une correspondance) tient en une question : **y a-t-il une bonne réponse ?**

## Intérêt pour la prévision de séries temporelles

Si la prévision est en elle-même une tâche d'[apprentissage supervisé](../supervised-learning/), l'apprentissage non supervisé est en séries temporelles un « outil d'appoint » très puissant :

- **Partitionner des séries / segments similaires** : quand on dispose de centaines ou de milliers de séries (par exemple les ventes de nombreux magasins), on peut d'abord les **partitionner** pour regrouper celles qui se comportent de façon similaire, puis modéliser chaque groupe séparément — souvent plus précis qu'« un modèle unique pour tout ».
- **Réduire la dimension d'un grand nombre de séries liées** : quand les variables sont extrêmement nombreuses, l'[ACP](../pca/) compresse de nombreuses séries corrélées en quelques **composantes principales**, ce qui réduit à la fois le bruit et le coût de calcul.
- **Détection d'anomalies** : repérer dans les séries les ruptures, les pannes de capteurs ou les événements anormaux, pour éviter qu'ils ne contaminent les données d'entraînement ou n'induisent la prévision en erreur.
- **Utiliser les étiquettes de groupe / composantes de l'ACP comme variables** : ajouter au tableau de prévision supervisé « la catégorie à laquelle appartient la série » ou « les premières composantes principales » comme variables supplémentaires améliore souvent nettement la prévision.
- **Identification de régimes (regime detection)** : identifier les différents « segments d'état » — phases haussières / baissières d'un marché, fonctionnement normal / anormal d'un équipement — pour que le modèle de prévision adopte une stratégie adaptée à chaque régime.

En une phrase : **l'apprentissage non supervisé vous aide à « comprendre » la structure des données, et l'apprentissage supervisé s'en sert ensuite pour « produire » la prévision.** Les deux sont souvent utilisés de concert.

## Résumé

- **Apprentissage non supervisé** = des données **sans étiquettes** ; le but est de découvrir une structure cachée, pas de prédire une bonne réponse.
- Tâches principales : **partitionnement** (regroupement), **réduction de dimension** (compression, par exemple l'ACP), **détection d'anomalies**, **estimation de densité**.
- Intuition du principe : le partitionnement **minimise la distance intra-groupe**, l'ACP **maximise la variance projetée** ; aucun de ces objectifs ne contient l'étiquette $y$.
- Intérêt : les données non étiquetées sont massives et faciles à obtenir ; on peut en extraire directement la structure, segmenter, débruiter, repérer les anomalies.
- En séries temporelles, il sert souvent d'**appoint** : partitionnement de séries, réduction de dimension, détection d'anomalies, variables supplémentaires, identification de régimes — en tandem avec l'[apprentissage supervisé](../supervised-learning/).

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
