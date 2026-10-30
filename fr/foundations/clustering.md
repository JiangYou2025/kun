---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/clustering/
title: "Le clustering"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)

Le **clustering (partitionnement, ou classification non supervisée)** est une méthode d'**[apprentissage non supervisé](../unsupervised-learning/)** : sans aucune étiquette, il regroupe automatiquement les échantillons semblables dans un même groupe (cluster), de sorte que « les éléments d'un même groupe soient aussi semblables que possible, et les groupes aussi différents que possible les uns des autres ».

## Intuition

Imaginez que vous disposiez d'une masse de relevés de ventes de supermarchés, sans que personne ne vous dise quels magasins sont des « grands magasins de centre-ville », des « petites surfaces de banlieue » ou des magasins « à pics de fréquentation les jours fériés ». Le clustering consiste à **laisser les données parler d'elles-mêmes** : selon la « distance » entre les échantillons dans l'espace des variables, on regroupe les points proches les uns des autres.

Le mot-clé ici est la **similarité**, généralement mesurée par une **distance**. Plus deux échantillons sont proches, plus ils ont de chances d'appartenir au même cluster. La plus utilisée est la **distance euclidienne** :

$$d(x, y) = \sqrt{\sum_{i=1}^{p}(x_i - y_i)^2}$$

où $x, y$ sont deux échantillons (chacun décrit par $p$ variables). Contrairement à l'**[apprentissage supervisé](../supervised-learning/)** (où il existe une réponse de référence), le clustering n'a pas de « bon regroupement » : la qualité du résultat se juge à la fois au regard du sens métier et d'indicateurs.

## Principe : l'[algorithme](../algorithms/) K-means

L'algorithme de clustering le plus classique et le plus utilisé est **K-means (k-moyennes)**. Vous devez d'abord fixer le nombre de clusters $k$, puis l'algorithme itère :

1. **Initialisation aléatoire** de $k$ centres (centroïdes, centroid) ; on peut tirer au hasard $k$ échantillons comme points de départ ;
2. **Affectation** : chaque point est affecté au cluster représenté par le **centre le plus proche** ;
3. **Mise à jour** : le centre de chaque cluster est recalculé comme la **moyenne de tous les points du cluster** ;
4. **Répéter** les étapes 2 et 3 jusqu'à ce que les centres ne bougent plus sensiblement (**convergence**).

Intuitivement, c'est un va-et-vient « affectation–mise à jour » : les points suivent le centre le plus proche, les centres sont tirés vers la position moyenne de leurs points, jusqu'à atteindre un état stable.

### Que minimise-t-il ?

K-means minimise en réalité la **somme des carrés intra-cluster (within-cluster sum of squares, WCSS)**, aussi appelée **inertie (inertia)** :

$$J = \sum_{j=1}^{k}\sum_{x\in C_j}\|x-\mu_j\|^2$$

Explication symbole par symbole :

- $k$ : le nombre total de clusters (que vous fixez) ;
- $C_j$ : l'ensemble des échantillons du $j$-ième cluster ;
- $x$ : un échantillon (vecteur) appartenant au cluster $C_j$ ;
- $\mu_j$ : le centre du $j$-ième cluster, égal à la moyenne de tous les $x$ de ce cluster ;
- $\|x-\mu_j\|^2$ : le **carré de la distance euclidienne** entre l'échantillon et le centre auquel il appartient ;
- double somme : on additionne d'abord, dans chaque cluster, les distances au carré de tous les points au centre, puis on fait la somme sur tous les clusters.

Plus $J$ est petit, plus les points de chaque cluster sont serrés autour de leur centre, et plus les clusters sont « compacts ». L'étape d'« affectation » fait choisir à chaque point le centre le plus proche, l'étape de « mise à jour » place le centre sur la moyenne — ces deux étapes font toutes deux décroître $J$, donc l'algorithme converge forcément (mais éventuellement vers un **optimum local** ; c'est pourquoi on le lance souvent plusieurs fois avec des initialisations différentes pour garder le meilleur résultat, ce que sklearn fait par défaut).

## Comment choisir k

C'est à vous de fixer $k$ ; comment le choisir raisonnablement ? Deux outils courants :

- **Méthode du coude (elbow method)** : tracez la courbe de $J$ (l'inertie) en fonction de $k$. Plus $k$ est grand, plus $J$ est petit, mais la baisse ralentit de plus en plus ; le $k$ où la courbe présente un « coude » net est souvent le meilleur compromis.
- **Coefficient de silhouette (silhouette coefficient)** : pour chaque échantillon, on calcule $s = \dfrac{b - a}{\max(a, b)}$, où $a$ est sa distance moyenne aux autres points du **même cluster** et $b$ sa distance moyenne au **cluster voisin le plus proche**. Plus $s$ est proche de 1, meilleur est le partitionnement ; proche de 0, l'échantillon est à la frontière ; négatif, il est peut-être mal classé. On retient le $k$ qui maximise le coefficient de silhouette moyen sur tous les échantillons.

## Un exemple concret

Exécutons K-means avec scikit-learn (attention : **standardiser d'abord**) :

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([[1.0, 2.0], [1.2, 1.8], [5.0, 8.0],
              [5.2, 8.1], [9.0, 1.0], [8.7, 1.2]])

# 1) Standardisation : chaque variable a une moyenne de 0 et une variance de 1,
#    pour éviter que les variables de grande amplitude ne dominent la distance
X_scaled = StandardScaler().fit_transform(X)

# 2) Entraîner KMeans ; n_init=10 signifie 10 initialisations différentes, on garde la meilleure
km = KMeans(n_clusters=3, n_init=10, random_state=0)
labels = km.fit_predict(X_scaled)

print("Étiquette de cluster de chaque échantillon :", labels)        # par ex. [0 0 1 1 2 2]
print("Centres des clusters :", km.cluster_centers_)
print("Somme des carrés intra-cluster (inertia) :", km.inertia_)
print("Coefficient de silhouette :", silhouette_score(X_scaled, labels))
```

`fit_predict` renvoie le cluster auquel appartient chaque échantillon ; `inertia_` est le $J$ ci-dessus ; `silhouette_score` vous aide à évaluer si ce choix de $k$ est bon.

## Limites et autres méthodes

K-means est simple et efficace, mais il faut garder ses hypothèses en tête :

- **Il suppose des clusters « sphériques » et de tailles comparables** : pour des clusters allongés, annulaires ou de densités très différentes, K-means partitionne très mal ;
- **Il est sensible à l'initialisation** : il peut se retrouver piégé dans un optimum local (ce que l'on atténue avec l'initialisation `k-means++` et plusieurs `n_init`) ;
- **Il est sensible à l'échelle** : la distance est dominée par les variables de grande valeur numérique, il **faut donc standardiser les variables au préalable** ;
- **Il faut fixer $k$ à l'avance**, et il est assez sensible aux valeurs aberrantes.

Alternatives :

- **Classification hiérarchique (hierarchical clustering)** : pas besoin de fixer $k$ à l'avance ; par fusions (ou divisions) successives, on obtient un arbre, le « dendrogramme (dendrogram) », que l'on peut « couper » à n'importe quelle hauteur pour obtenir le nombre de clusters voulu ; adaptée lorsqu'on veut observer une structure imbriquée.
- **DBSCAN** : un clustering fondé sur la **densité**, capable de découvrir des clusters de forme arbitraire et de marquer automatiquement les points des zones peu denses comme du **bruit / des valeurs aberrantes** ; il ne nécessite pas de fixer $k$, mais il faut bien régler des paramètres comme le rayon de voisinage.

## Signification pour la prévision de séries temporelles

Le clustering est très utile en prévision de séries temporelles :

- **Partager un modèle entre séries similaires** : on regroupe en quelques classes les magasins, capteurs ou utilisateurs au comportement semblable, et l'on entraîne un modèle par classe (au lieu d'un modèle pour chacune de milliers de séries), ce qui économise du calcul et rend les modèles plus robustes ;
- **Identifier des états / régimes (regime)** : en regroupant des périodes selon leurs caractéristiques, on distingue des **régimes** tels que « période stable / période de forte volatilité / période de promotion », ce qui facilite une modélisation par segments ;
- **Comme variable explicative** : on fournit l'**identifiant de cluster** comme variable catégorielle au modèle de prévision en aval, pour qu'il sache « à quelle catégorie appartient cette série ».

Quelques rappels : **standardisez toujours** avant le clustering ; pour des formes d'onde brutes de séries temporelles, la distance euclidienne ordinaire n'est pas forcément adaptée — envisagez une distance d'alignement comme la **déformation temporelle dynamique (DTW)**, ou extrayez d'abord des caractéristiques statistiques (moyenne, volatilité, tendance, intensité de la périodicité) avant de partitionner.

## En résumé

- Le **clustering** regroupe sans supervision les échantillons similaires, en mesurant leur proximité par une **distance / similarité**.
- **K-means** itère « affectation au centre le plus proche – mise à jour par la moyenne du cluster » pour minimiser la **somme des carrés intra-cluster** $J=\sum_j\sum_{x\in C_j}\|x-\mu_j\|^2$.
- Pour choisir $k$, on utilise couramment la **méthode du coude** et le **coefficient de silhouette** ; **standardisez toujours** les variables au préalable.
- K-means suppose des clusters sphériques et il est sensible à l'initialisation et à l'échelle ; la **classification hiérarchique** et **DBSCAN** sont des alternatives courantes.
- En prévision de séries temporelles, il sert à **regrouper les séries similaires pour partager un modèle**, à **identifier des régimes** et à **fournir une variable explicative** — pensez à standardiser et à choisir la bonne distance.

Pour aller plus loin : [Apprentissage non supervisé](../unsupervised-learning/) · [ACP (analyse en composantes principales)](../pca/) · [Modèles linéaires](../linear-model/)

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)
