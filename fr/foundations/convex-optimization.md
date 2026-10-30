---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/convex-optimization/
title: "L'optimisation convexe"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

L'optimisation convexe étudie les problèmes d'optimisation dont la fonction objectif est « en forme de bol » (une fonction convexe). Sa plus belle propriété : **tout optimum local est nécessairement un optimum global** ; la résolution est donc stable, fiable et assortie de garanties théoriques.

## Intuition

Représentez-vous la fonction objectif comme un relief :

- Une **fonction convexe** est comme un grand bol lisse : où que vous posiez une bille, elle roulera jusqu'au **même point le plus bas**.
- Une **fonction non convexe** est comme une vallée accidentée, parsemée de petits creux (optima locaux) : la bille peut rester coincée dans l'un d'eux, sans pouvoir en sortir ni trouver le véritable fond de la vallée.

Si l'optimisation convexe est si appréciée, c'est parce qu'elle est « sans piège » : inutile de craindre de rester bloqué sur une solution sous-optimale.

## Formulation mathématique

**Ensemble convexe** : le segment reliant deux points quelconques de l'ensemble reste dans l'ensemble.

**Fonction convexe** : son domaine de définition est un ensemble convexe et, pour tous points $x_1,x_2$ et tout $\lambda\in[0,1]$,

$$
f(\lambda x_1+(1-\lambda)x_2)\le \lambda f(x_1)+(1-\lambda)f(x_2)
$$

Intuitivement : **le graphe de la fonction reste toujours sous n'importe laquelle de ses cordes**.

Si $f$ est deux fois dérivable, le critère est plus simple :

- en dimension 1 : $f''(x)\ge 0$ partout ;
- en dimension supérieure : la **matrice hessienne (Hessian)** $\nabla^2 f$ est **semi-définie positive** partout.

Forme standard d'un problème d'optimisation convexe :

$$
\min_{x}\ f(x)\quad \text{s.t.}\quad g_i(x)\le 0,\ h_j(x)=0
$$

où l'objectif $f$ et les contraintes d'inégalité $g_i$ sont des fonctions convexes, et les contraintes d'égalité $h_j$ des fonctions affines (linéaires).

## Un exemple concret

Les moindres carrés $f(x)=(x-2)^2+1$. Sa dérivée seconde $f''(x)=2>0$ est positive partout, la fonction est donc convexe. Annulons la dérivée première :

$$
f'(x)=2(x-2)=0\ \Rightarrow\ x=2
$$

$x=2$ est un optimum local, et c'est aussi, de façon garantie, l'**optimum global**, avec $f(2)=1$.

```python
import numpy as np
xs = np.linspace(-1, 5, 7)
f  = (xs - 2)**2 + 1
print(list(zip(xs, f)))   # forme de bol partout, minimum en x=2
```

En revanche, une fonction comme $f(x)=x^4-3x^2$, qui a deux creux, est non convexe : la [descente de gradient](../gradient-descent/) peut aboutir dans des creux différents selon le point de départ.

## Pourquoi c'est important / où l'utilise-t-on

- Les fonctions objectifs de la **régression linéaire, de la régression ridge, de la régression logistique et des [SVM](../svm/)** sont toutes convexes : elles ont donc un optimum unique et reproductible.
- Après l'ajout d'un [terme de régularisation](../norm/) $\ell_1/\ell_2$ (une fonction convexe), l'ensemble reste convexe — c'est l'une des raisons pour lesquelles la [régularisation](../regularization/) fonctionne si bien.
- La convexité fournit une **garantie de convergence** : convexité + pas adapté, et la descente de gradient converge forcément vers l'optimum global.

## Signification pour la prévision de séries temporelles

- Les modèles classiques (une partie de l'estimation d'ARIMA, l'autorégression linéaire) relèvent de l'optimisation convexe : leurs solutions sont stables et interprétables.
- La [perte](../loss-function/) des modèles profonds comme KUN (Kernel U-Net) est **non convexe**, sans garantie d'optimum global ; en pratique, on s'appuie donc sur une bonne initialisation, [Adam](../adam/), la planification du [taux d'apprentissage](../learning-rate/), la [normalisation par lots](../batchnorm/) et d'autres techniques pour « contourner les mauvaises solutions locales ». Comprendre la différence entre convexe et non convexe vous fait saisir pourquoi l'entraînement des modèles profonds exige autant d'astuces.

## En résumé

- Fonction convexe = en forme de bol : tout optimum local est un optimum global.
- Critère : $f''\ge 0$ / hessienne semi-définie positive.
- L'apprentissage automatique classique pose surtout des problèmes convexes (sereins) ; l'apprentissage profond surtout des problèmes non convexes (qui demandent des astuces).

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
