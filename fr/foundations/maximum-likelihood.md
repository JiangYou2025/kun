---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/maximum-likelihood/
title: "Maximum de vraisemblance"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)

L'estimation par maximum de vraisemblance (MLE) est une méthode pour **trouver des paramètres** : parmi tous les paramètres possibles, on retient celui qui rend la plus probable l'apparition des « **données réellement observées** ». L'objectif d'entraînement de nombreux modèles est, au fond, un maximum de vraisemblance.

## Intuition

Vous trouvez une pièce, la lancez 10 fois et obtenez 7 piles et 3 faces. Question : quelle est à peu près la probabilité $p$ de tomber sur pile ?

L'intuition répond 0,7. Le maximum de vraisemblance transforme cette intuition en principe : **on choisit le $p$ qui rend l'événement « 7 piles, 3 faces » le plus probable**.

- Si $p=0.1$, obtenir 7 piles est presque impossible ;
- si $p=0.7$, obtenir 7 piles est tout à fait naturel ;
- 0,7 est donc le paramètre qui « explique le mieux les données ».

Le maximum de vraisemblance consiste à « **faire en sorte que le modèle soit le moins surpris possible par les données déjà observées** ».

## Formulation mathématique

Soit des données $x_1,\dots,x_n$ indépendantes et identiquement distribuées, et un modèle de paramètre $\theta$. La **fonction de vraisemblance** est la probabilité jointe d'observer ces données sous ce paramètre :

$$
L(\theta)=\prod_{i=1}^{n} p(x_i\mid\theta)
$$

Un produit est peu commode ; en passant au logarithme, il devient une somme (le logarithme est monotone et ne déplace pas le maximum), d'où la **log-vraisemblance** :

$$
\ell(\theta)=\sum_{i=1}^{n}\log p(x_i\mid\theta)
$$

L'estimateur du maximum de vraisemblance :

$$
\hat\theta_{\text{MLE}}=\arg\max_\theta\ \ell(\theta)
$$

En pratique, on **minimise** de façon équivalente la **log-vraisemblance négative** (NLL), ce qui rejoint les [fonctions de perte](../loss-function/) et la [descente de gradient](../gradient-descent/) :

$$
\hat\theta=\arg\min_\theta\ \Big(-\sum_i\log p(x_i\mid\theta)\Big)
$$

## Un exemple concret

Revenons aux 7 piles et 3 faces. La vraisemblance vaut $L(p)=p^7(1-p)^3$ ; en prenant le logarithme :

$$
\ell(p)=7\log p+3\log(1-p)
$$

On dérive et on annule :

$$
\ell'(p)=\frac{7}{p}-\frac{3}{1-p}=0\ \Rightarrow\ 7(1-p)=3p\ \Rightarrow\ p=0.7
$$

On retrouve bien 0,7, conformément à l'intuition.

```python
import numpy as np
ps = np.linspace(0.01, 0.99, 99)
ll = 7*np.log(ps) + 3*np.log(1-ps)
print(round(ps[np.argmax(ll)], 2))   # 0.7
```

## Pourquoi c'est important / où on l'utilise

- **Un principe d'entraînement unificateur** : le MLE de la régression linéaire (sous hypothèse de bruit gaussien) donne exactement les **moindres carrés** ; le MLE en classification donne exactement la perte d'[entropie croisée](../cross-entropy/).
- Il est complémentaire de l'approche [bayésienne](../bayes-theorem/) : le MLE ne considère que la vraisemblance $p(\text{données}\mid\theta)$, tandis que l'approche bayésienne la multiplie en plus par un a priori $p(\theta)$ (ajouter un terme de régularisation revient à ajouter un a priori, c'est l'estimation MAP).
- Avec de grands échantillons, le MLE possède de bonnes propriétés statistiques (convergence, efficacité asymptotique).

## Intérêt pour la prévision de séries temporelles

- Les paramètres des modèles classiques (AR, ARIMA, GARCH) sont le plus souvent ajustés par maximum de vraisemblance.
- En prévision probabiliste, l'objectif d'entraînement s'écrit souvent « maximiser la log-vraisemblance des observations futures » — par exemple, faire en sorte que la loi gaussienne produite par le modèle colle au plus près des valeurs réelles.
- KUN (Kernel U-Net) utilise la MSE pour la prévision ponctuelle, ce qui correspond précisément au « maximum de vraisemblance sous bruit gaussien » ; pour une prévision probabiliste, la perte s'écrit directement comme une log-vraisemblance négative.

## Erreurs fréquentes

- La vraisemblance **n'est pas** une probabilité sur les paramètres : $L(\theta)$ décrit « la probabilité des données en fonction de $\theta$ », et son intégrale en $\theta$ ne vaut pas 1.
- Sur de petits échantillons, le MLE peut [**surapprendre**](../overfitting/) (par exemple sous-estimer la variance) ; ajouter un a priori / une régularisation (MAP) est alors plus robuste.
- Pensez à utiliser la **log**-vraisemblance : un produit risque le dépassement inférieur (underflow), une somme est plus stable et plus facile à dériver.

[← Fondements mathématiques](../math/) · [Vue d'ensemble du cours de base](../)
