---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/pca/
title: "ACP (analyse en composantes principales)"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

**L'ACP (analyse en composantes principales, Principal Component Analysis ou PCA)** est la méthode de **réduction de dimension linéaire** la plus utilisée : elle trouve les **directions de plus grande variance** des données et projette les données de grande dimension sur quelques-unes de ces directions, afin de conserver le plus d'information possible avec moins de dimensions.

## Intuition

Imaginez un nuage de points dispersé dans un plan, globalement « étiré » selon une direction oblique. Si l'on **fait tourner les axes** pour que le nouveau premier axe s'aligne exactement sur la direction la plus « longue » du nuage, et le second, perpendiculaire, sur la deuxième direction la plus longue, on constate que l'essentiel de la « dispersion » se lit sur le premier axe, tandis que le second ne varie presque pas.

En ne gardant alors que la coordonnée sur le premier axe, on comprime des données à deux dimensions en une seule, presque sans perte d'information. C'est l'idée centrale de l'ACP — **tourner le repère vers les directions où les données sont le plus dispersées, puis abandonner celles qui ne varient presque pas**. Ces nouvelles directions s'appellent les **composantes principales (principal components)** ; elles sont **orthogonales** entre elles et classées par « variance expliquée » décroissante.

Pourquoi mesurer l'information par la **variance** ? Parce qu'une grande variance signifie que les exemples se distinguent bien dans cette direction et portent beaucoup de différences ; dans une direction de variance proche de 0, tous les exemples se ressemblent, et la garder ne sert à rien.

{% include fviz/pca-2d.html %}

## Principe et formulation mathématique

Voici la démarche standard de l'ACP. Soit une matrice de données $X$ à $n$ lignes (exemples) et $p$ colonnes (variables).

1. **Centrage / standardisation** : on soustrait d'abord à chaque variable sa moyenne (centrage). Si les variables ont des unités différentes, on divise aussi par l'écart-type (standardisation). **Cette étape est indispensable**, sinon le résultat sera biaisé par les variables aux grandes valeurs.

2. **Calcul de la matrice de covariance** (sur $X$ centrée) :

$$\Sigma = \frac{1}{n} X^\top X$$

où $X^\top$ est la transposée de $X$ ; $\Sigma$ est une matrice symétrique $p\times p$ dont la diagonale contient les variances des variables et les termes hors diagonale les covariances entre paires de variables.

3. **Décomposition en éléments propres** : on calcule les **vecteurs propres** et les **valeurs propres** de $\Sigma$ :

$$\Sigma\, v_i = \lambda_i\, v_i$$

- Les **vecteurs propres** $v_i$ sont les directions des **composantes principales** (orthogonales entre elles, elles forment les nouveaux axes) ;
- Les **valeurs propres** $\lambda_i$ mesurent la **variance** des données dans la direction $v_i$, c'est-à-dire « la part de variance expliquée » par cette composante.

En triant les valeurs propres par ordre décroissant $\lambda_1 \ge \lambda_2 \ge \cdots$, les vecteurs propres correspondants sont la première, la deuxième… composante principale.

4. **Projection et réduction** : on forme la matrice $W=[v_1, \dots, v_m]$ des $m$ premières composantes principales et on y projette les données :

$$Z = X W$$

$Z$ est la représentation de dimension réduite, de taille $n\times m$ ($m < p$).

### Combien de composantes garder

On utilise le **ratio de variance expliquée cumulée (cumulative explained variance ratio)** : le ratio de variance expliquée de la $i$-ième composante vaut $\dfrac{\lambda_i}{\sum_j \lambda_j}$. On les cumule du plus grand au plus petit et l'on regarde combien de composantes il faut garder pour atteindre, par exemple, **90 % ou 95 %** de la variance totale : c'est ce nombre qu'on retient.

### Lien avec la [SVD](../svd/)

En pratique, on calcule rarement une vraie décomposition en éléments propres : on applique directement une **décomposition en valeurs singulières (SVD)** à $X$ centrée, $X = U S V^\top$. Les colonnes de $V$ sont les directions des composantes principales, et les carrés des valeurs singulières $S^2$ sont proportionnels aux valeurs propres $\lambda$. La SVD est numériquement plus stable ; c'est elle qu'utilise en interne la classe `PCA` de sklearn.

## Un exemple concret

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Supposons que X ait de nombreuses colonnes, fortement corrélées entre elles
X = np.random.RandomState(0).randn(200, 8)
X[:, 1] = X[:, 0] * 0.9 + 0.1 * X[:, 1]   # corrélation créée artificiellement

# 1) Il faut d'abord standardiser / centrer
X_scaled = StandardScaler().fit_transform(X)

# 2) Ajuster l'ACP
pca = PCA(n_components=4)
Z = pca.fit_transform(X_scaled)            # Z : données réduites (200, 4)

print("Ratio de variance expliquée par composante :", pca.explained_variance_ratio_)
print("Ratio de variance expliquée cumulé :", np.cumsum(pca.explained_variance_ratio_))
# par exemple [0.31 0.18 0.14 0.12] -> cumulé [0.31 0.49 0.63 0.75]
```

`explained_variance_ratio_` indique la proportion de variance totale conservée par chaque composante, et `cumsum` aide à décider combien de composantes suffisent.

## Pourquoi c'est important (où on l'utilise)

L'ACP a de très nombreux usages :

- **Visualisation** : ramener des données de plusieurs dizaines de dimensions à 2 ou 3 dimensions et les afficher en nuage de points pour observer directement les [groupes (clustering)](../clustering/) et les valeurs aberrantes ;
- **Décorrélation** : les composantes principales étant orthogonales, elles éliminent naturellement les corrélations linéaires entre variables ;
- **Compression** : approcher les données d'origine avec quelques composantes, ce qui économise stockage et calcul ;
- **Débruitage** : les directions de très faible variance sont souvent du bruit ; les abandonner rend le signal plus propre ;
- **Variables pour les modèles en aval** : fournir les composantes réduites à un modèle de régression, de classification ou de prévision réduit la dimension, accélère l'entraînement et atténue le [surapprentissage](../overfitting/).

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, l'ACP convient particulièrement aux situations où « il y a trop de variables et elles sont corrélées entre elles » :

- **Compresser les variables retardées** : quand on construit un grand nombre de **variables retardées** (lag features), elles sont souvent fortement corrélées ; l'ACP peut les condenser en quelques composantes et éviter la **multicolinéarité** ;
- **Réduction de dimension multi-séries / modèles à facteurs** : des centaines ou des milliers de séries corrélées (actions d'un même secteur, capteurs d'une même région) peuvent être résumées par l'ACP en quelques **facteurs communs (factor models)** qui capturent leurs moteurs partagés ;
- **Débruitage et accélération** : supprimer les directions de faible variance réduit le bruit et accélère nettement l'entraînement des modèles en aval.

**Mise en garde importante — éviter la fuite du futur** : l'ACP « apprend » les directions des composantes principales ; il faut donc **l'ajuster (`fit`) uniquement sur l'ensemble d'entraînement**, puis appliquer la même transformation (`transform`) aux ensembles de validation et de test. Il faut **découper les données dans l'ordre chronologique** et **ne jamais ajuster l'ACP sur toute la série (futur compris)** : sinon l'information future s'infiltre dans le passé, l'évaluation est artificiellement gonflée et le modèle s'effondre dès sa mise en production. De même, la moyenne et la variance de la standardisation ne doivent être calculées que sur l'ensemble d'entraînement.

## En résumé

- **L'ACP** fait tourner les axes pour trouver les **directions orthogonales de plus grande variance (les composantes principales)** et réalise ainsi une **réduction de dimension linéaire**.
- Démarche : **centrage / standardisation → matrice de covariance $\Sigma=\frac1n X^\top X$ → décomposition en éléments propres**, qui donne les composantes principales (vecteurs propres) et la variance expliquée (valeurs propres) ; en pratique, on passe souvent par la **SVD**.
- Le **ratio de variance expliquée cumulée** décide du nombre de composantes à garder (par exemple pour atteindre 90 % à 95 %).
- **Il faut d'abord standardiser / centrer**, sinon les variables aux grandes unités dominent.
- En prévision, l'ACP permet de **compresser des variables retardées corrélées, d'extraire des facteurs communs, de débruiter et d'accélérer, et d'atténuer la multicolinéarité** ; veillez à **ne l'ajuster que sur l'ensemble d'entraînement et à découper chronologiquement, pour éviter la fuite du futur**.

Pour aller plus loin : [clustering](../clustering/) · [apprentissage non supervisé](../unsupervised-learning/) · [modèles linéaires](../linear-model/)

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
