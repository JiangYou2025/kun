---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/linear-model/
title: "Les modèles linéaires"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)

Un **modèle linéaire** prédit à l'aide d'une **combinaison linéaire** des variables d'entrée (une somme pondérée à laquelle on ajoute un biais). Simple, interprétable et rapide à entraîner, c'est le **modèle de référence (baseline)** à essayer en premier dans presque toutes les tâches d'[apprentissage automatique](../ml/).

## Intuition

Imaginez que vous vouliez prédire le prix d'un logement à partir de sa surface. L'idée la plus naïve : **un certain prix par mètre carré, plus un prix de base**. Sous forme d'équation :

$$\text{prix} \approx w \times \text{surface} + b$$

Ici, $w$ (la pente) vous dit « de combien le prix augmente pour chaque mètre carré supplémentaire », et $b$ (l'ordonnée à l'origine) est le « prix de base » pour une surface nulle. Lorsque vous avez plusieurs variables (surface, étage, distance au métro…), vous attribuez un poids à chacune et vous additionnez le tout — c'est là tout le secret du modèle linéaire : **ajuster les données par une droite (ou, en dimension supérieure, par un hyperplan)**.

« Linéaire » ne signifie pas que le monde est linéaire, mais que **le modèle est linéaire par rapport aux paramètres $w$**. C'est précisément grâce à cette structure si simple que l'on voit clairement quel rôle joue chaque variable ; cette **interprétabilité** est quelque chose que bien des modèles complexes ne peuvent offrir.

## Formulation mathématique : la régression linéaire

Pour un échantillon à $d$ variables $x = (x_1, x_2, \dots, x_d)$, la prédiction de la régression linéaire est

$$\hat{y} = w^\top x + b = \sum_{j=1}^{d} w_j x_j + b$$

- **Poids / coefficients** $w_j$ : la « contribution » de la $j$-ième variable à la prédiction. $w_j > 0$ signifie que plus la variable est grande, plus la prédiction est grande ; $w_j < 0$, l'inverse ; $w_j \approx 0$, que la variable n'apporte pratiquement rien.
- **Ordonnée à l'origine (intercept)** $b$ : la prédiction de référence lorsque toutes les variables valent 0.

Comment trouver les « meilleurs » $w$ et $b$ ? On cherche à rendre l'écart entre les prédictions $\hat{y}_i$ et les vraies valeurs $y_i$ le plus petit possible, en prenant comme [perte](../loss-function/) l'**erreur quadratique moyenne (MSE)** :

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}\left(y_i - \hat{y}_i\right)^2$$

La méthode qui minimise cette erreur s'appelle la **méthode des moindres carrés (least squares)**. Chose remarquable, elle admet une **solution analytique (closed-form solution)** — pas besoin d'itérer, on l'obtient en une seule étape :

$$w = (X^\top X)^{-1} X^\top y$$

où $X$ est la matrice des variables, obtenue en empilant tous les échantillons en lignes. La régression linéaire s'entraîne donc extrêmement vite, ce qui explique en bonne partie qu'elle serve de référence « à essayer d'emblée ».

## Formulation mathématique : la régression logistique (classification)

S'il s'agit de **classification** (par exemple « pleuvra-t-il demain ? »), produire directement un nombre réel ne convient plus : on veut une **probabilité**. On applique donc à la sortie de la partie linéaire une **fonction sigmoïde**, qui la comprime dans l'intervalle $(0,1)$ :

$$p = \sigma(w^\top x + b), \qquad \sigma(z) = \frac{1}{1 + e^{-z}}$$

Le graphe de $\sigma(z)$ est une « courbe en S » lisse : elle tend vers 1 quand $z$ est grand, vers 0 quand $z$ est petit, et vaut exactement 0,5 en $z=0$. Si $p > 0.5$, on prédit la classe positive, sinon la classe négative.

La régression logistique n'utilise pas la MSE, mais la perte d'**[entropie croisée](../cross-entropy/) (cross-entropy)** :

$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^{n}\Big[y_i \log p_i + (1-y_i)\log(1-p_i)\Big]$$

Elle mesure « à quel point la distribution de probabilité prédite s'écarte des vraies étiquettes » ; la perte est minimale lorsque le modèle attribue une forte probabilité à la classe positive et une faible probabilité à la classe négative.

## Un exemple concret (sklearn)

```python
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler

# ---- Régression linéaire : prédire le prix à partir de la surface ----
X = np.array([[50], [60], [80], [100], [120]])   # surface
y = np.array([150, 180, 240, 300, 360])          # prix (en dizaines de milliers)

reg = LinearRegression().fit(X, y)
print("pente w =", reg.coef_, "ordonnée à l'origine b =", reg.intercept_)
print("prédiction pour 90 m² :", reg.predict([[90]]))

# ---- Régression logistique : classification binaire, penser à standardiser d'abord ----
Xc = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 4.0], [4.0, 3.0]])
yc = np.array([0, 0, 1, 1])

scaler = StandardScaler()
Xc_scaled = scaler.fit_transform(Xc)             # les coefficients ne sont comparables qu'après mise à l'échelle
clf = LogisticRegression().fit(Xc_scaled, yc)
print("probabilités prédites :", clf.predict_proba(scaler.transform([[2.5, 2.5]])))
```

Notez qu'on a volontairement effectué une **mise à l'échelle des variables (feature scaling)** : lorsque les ordres de grandeur des variables diffèrent fortement (par exemple une « surface » de quelques dizaines et un « nombre de pièces » à un chiffre), ne pas les mettre à l'échelle rend les coefficients incomparables et ralentit ou fausse l'optimisation. La **standardisation (StandardScaler)** est un prétraitement quasi systématique pour les modèles linéaires.

## Pourquoi c'est important (où l'utilise-t-on)

- **Une référence solide** : avant de vous lancer dans un modèle complexe, faites d'abord tourner un modèle linéaire. S'il suffit déjà, inutile de vous compliquer la vie ; sinon, il vous fournit au moins une ligne de référence « à dépasser ».
- **Rapide** : solution analytique ou simple [descente de gradient](../gradient-descent/), entraînement en quelques secondes, idéal pour expérimenter vite.
- **Interprétable** : un coup d'œil aux coefficients suffit pour savoir quelles variables comptent et dans quel sens, ce qui facilite les explications et le diagnostic des problèmes de données.
- Lorsque les variables sont nombreuses et que le risque de [surapprentissage](../overfitting/) est élevé, il se combine naturellement avec la [régularisation](../regularization/) pour donner **Ridge (L2)** et **Lasso (L1)**, qui rétrécissent automatiquement, voire éliminent, les variables inutiles.

## Signification pour la prévision de séries temporelles

En prévision de séries temporelles, la puissance des modèles linéaires est souvent sous-estimée. L'astuce centrale consiste à construire des **variables retardées (lag features)** : on prend les valeurs des périodes précédentes $y_{t-1}, y_{t-2}, \dots, y_{t-p}$ comme variables d'entrée pour prédire la valeur courante $y_t$. La régression linéaire devient alors

$$\hat{y}_t = w_1 y_{t-1} + w_2 y_{t-2} + \dots + w_p y_{t-p} + b$$

**C'est exactement un modèle AR (autorégressif linéaire)** ! Autrement dit, l'autorégression des séries temporelles classiques n'est rien d'autre qu'une « régression linéaire sur des variables retardées ». Cela apporte trois avantages :

- c'est une **référence de prévision extrêmement solide**, que bien des modèles profonds sophistiqués ne battent pas toujours de façon fiable ;
- **les coefficients indiquent directement quels retards comptent** — par exemple, un $w_1$ élevé traduit une forte dépendance à la période précédente, et un $w_7$ élevé suggère une périodicité hebdomadaire ;
- lorsque l'ordre $p$ est grand et les variables nombreuses, la combinaison avec la [régularisation](../regularization/) (Lasso sélectionne automatiquement les quelques retards clés) prévient efficacement le surapprentissage.

Si l'hypothèse linéaire ne suffit pas, on peut alors envisager des [familles de modèles](../model-families/) plus souples, comme les [arbres de décision](../decision-tree/), l'[apprentissage ensembliste / GBDT](../ensemble-gbdt/) ou les méthodes à noyau.

## En résumé

- **Modèle linéaire = somme pondérée des variables + biais** : $\hat{y} = w^\top x + b$, la structure la plus simple et la plus interprétable.
- La **régression linéaire** s'ajuste par MSE / moindres carrés et admet la solution analytique $w=(X^\top X)^{-1}X^\top y$ ; la **régression logistique** produit une probabilité via la sigmoïde et s'entraîne par entropie croisée, pour la classification.
- Les coefficients $w_j$ reflètent directement l'importance et le sens de chaque variable ; pensez toujours à **mettre les variables à l'échelle** pour que les coefficients soient comparables.
- Avec beaucoup de variables, combinez-le avec la [régularisation](../regularization/) → Ridge / Lasso.
- En séries temporelles, **régression linéaire sur variables retardées ≈ autorégression linéaire (AR)** : une référence à la fois rapide et solide, dont les coefficients révèlent en outre les retards les plus importants.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)
