---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/gradient/
title: "Le gradient"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

Le gradient d'une fonction de plusieurs variables est le **vecteur formé de ses dérivées partielles** par rapport à chacune des variables. Il pointe dans la direction où la fonction **croît le plus vite**, et sa longueur indique à quel point cette montée est raide. En [optimisation](../optimization/), on avance dans la direction opposée pour faire décroître la fonction.

## Intuition

Pour une fonction d'une seule variable, la « dérivée » est un nombre (la pente). Mais un modèle compte des milliers, voire des millions de paramètres : la fonction est **multivariée** — la « pente » n'est alors plus un nombre, mais un **vecteur**, qui vous indique « dans quelle direction aller pour monter le plus vite ».

Debout sur une montagne, le gradient est comme une flèche : elle **pointe vers la montée la plus raide**, et **plus elle est longue, plus la pente est forte**. Pour descendre, on marche dans le sens opposé à la flèche. Une fois au fond de la vallée (un minimum), plus aucune direction ne monte et la longueur de la flèche devient 0 — c'est ce qu'on appelle un « gradient nul ».

{% include fviz/gradient-field.html %}

## Formulation mathématique

Pour $f(x_1,x_2,\dots,x_n)$, le gradient est le vecteur formé de ses **dérivées partielles** :

$$
\nabla f=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\dots,\frac{\partial f}{\partial x_n}\right)
$$

- $\dfrac{\partial f}{\partial x_i}$ — **dérivée partielle** : le taux de variation de la fonction lorsque seul $x_i$ varie, les autres variables restant fixes ;
- $\nabla$ (nabla) — l'opérateur gradient ;
- la **direction** du gradient est celle où la fonction croît le plus vite, et sa **norme** $\lVert\nabla f\rVert$ est le taux de variation maximal dans cette direction.

Une propriété clé : le gradient est **perpendiculaire aux lignes de niveau** (ou surfaces de niveau). En effet, le long d'une ligne de niveau la valeur de la fonction ne change pas, alors que le gradient pointe vers la variation la plus rapide : les deux sont naturellement orthogonaux.

## Un exemple concret

Soit $f(x,y)=x^2+3y^2$. On dérive partiellement par rapport à $x$ puis à $y$ :

$$
\frac{\partial f}{\partial x}=2x,\qquad \frac{\partial f}{\partial y}=6y
$$

$$
\nabla f=(2x,\ 6y)
$$

Au point $(1,1)$, $\nabla f=(2,6)$ : en ce point, la pente est bien plus forte selon $y$ que selon $x$ (car le coefficient de $y$ est plus grand). Pour descendre, on se dirige vers $(-2,-6)$. À l'optimum $(0,0)$, le gradient vaut $(0,0)$.

```python
import numpy as np
def grad(x, y):
    return np.array([2*x, 6*y])
print(grad(1, 1))   # [2 6]  direction de montée la plus rapide
print(grad(0, 0))   # [0 0]  optimum : gradient nul
```

## Pourquoi c'est important / où l'utilise-t-on

- **Le volant de l'optimisation** : la [descente de gradient](../gradient-descent/) utilise $-\nabla L$ pour décider où aller à chaque pas.
- **[Rétropropagation](../backpropagation/)** : elle s'appuie sur la [règle de dérivation en chaîne](../chain-rule/) pour calculer efficacement le gradient de la [perte](../loss-function/) par rapport à chaque paramètre.
- **Intuition géométrique** : le gradient est perpendiculaire aux lignes de niveau, ce qui explique pourquoi, dans une vallée longue et étroite, la descente de gradient oscille « en zigzag ».

## Signification pour la prévision de séries temporelles

- Lors de l'entraînement de KUN (Kernel U-Net), le framework calcule automatiquement le gradient de la perte par rapport à chaque poids, puis le transmet à l'[optimiseur](../optimizer/) pour la mise à jour — le gradient est l'instruction précise qui dit « comment le modèle doit s'améliorer ».
- Dans les réseaux profonds traitant de longues séquences, le gradient peut **s'évanouir ou exploser** pendant la rétropropagation (produit de nombreuses dérivées) ; les connexions résiduelles, la normalisation et l'écrêtage de gradient servent tous à le faire circuler sainement.

## Erreurs fréquentes

- Le gradient est un **vecteur**, avec une direction et une norme : ne le confondez pas avec la dérivée (scalaire) d'une fonction d'une variable.
- Le gradient pointe vers la **montée** la plus rapide ; pour descendre, il faut prendre le gradient **négatif**.
- Un gradient nul signale seulement un « point stationnaire » : ce peut être un minimum, un maximum ou un point selle, et il faut recourir à l'information du second ordre pour trancher.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
