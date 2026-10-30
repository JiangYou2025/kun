---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/cross-entropy/
title: "L'entropie croisée"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

L'entropie croisée mesure le coût moyen engendré lorsqu'on « **décrit la distribution réelle à l'aide de la distribution prédite par le modèle** ». C'est la [fonction de perte](../loss-function/) la plus utilisée pour les tâches de classification : plus le modèle est proche de la vérité, plus l'entropie croisée est faible.

## Intuition

L'[entropie](../entropy/) mesure « le nombre moyen de bits nécessaires pour coder de façon optimale la situation réelle ». L'entropie croisée pose une question plus concrète : **si j'utilise un codage « erroné » (fondé sur la prédiction $q$ du modèle) pour décrire les événements qui se produisent réellement (distribution réelle $p$), combien de bits me faudra-t-il en moyenne ?**

Dès que la prédiction $q$ s'écarte de la vérité $p$, vous utilisez des codes plus longs et payez un coût supplémentaire. Plus la prédiction est juste, plus ce coût s'approche de la borne inférieure qu'est l'entropie ; plus elle est aberrante, plus le coût est élevé. « Minimiser l'entropie croisée » équivaut donc à « rapprocher autant que possible la distribution prédite de la distribution réelle ».

## Formulation mathématique

Pour des distributions discrètes, l'entropie croisée entre la distribution réelle $p$ et la distribution prédite $q$ est :

$$
H(p,q)=-\sum_i p_i \log q_i
$$

- $p_i$ — la probabilité réelle de la classe $i$ (en classification, c'est souvent un vecteur one-hot : 1 pour la bonne classe, 0 pour les autres) ;
- $q_i$ — la probabilité de la classe $i$ prédite par le modèle ;
- avec un $\log$ en base 2, l'unité est le bit ; en base $e$ (l'usage courant en apprentissage automatique), l'unité est le nat.

Sa relation avec l'[entropie](../entropy/) et la [divergence de KL](../kl-divergence/) est :

$$
H(p,q)=H(p)+D_{\mathrm{KL}}(p\parallel q)
$$

Comme $H(p)$ (l'entropie de la distribution réelle) est une constante, **minimiser l'entropie croisée = minimiser la divergence de KL = rapprocher $q$ de $p$**.

Lorsque $p$ est one-hot (notons $c$ la bonne classe), la formule se réduit à une forme très simple :

$$
H(p,q)=-\log q_c
$$

C'est la « **log-vraisemblance négative** » : elle ne pénalise que le fait d'attribuer une probabilité trop faible à la bonne réponse.

{% include fviz/cross-entropy.html %}

## Un exemple concret

Classification à trois classes, l'étiquette réelle est la classe 1, en one-hot $p=[1,0,0]$.

- Le modèle A prédit $q=[0.7,0.2,0.1]$ : perte $=-\log 0.7\approx 0.357$.
- Le modèle B prédit $q=[0.3,0.4,0.3]$ : perte $=-\log 0.3\approx 1.204$.

Le modèle A attribue une probabilité plus élevée à la bonne classe, son entropie croisée est plus faible : c'est exactement ce que l'on veut.

```python
import numpy as np
def cross_entropy(p, q):
    q = np.clip(q, 1e-12, 1.0)        # évite log(0)
    return -np.sum(p * np.log(q))
p = np.array([1, 0, 0])
print(round(cross_entropy(p, [0.7, 0.2, 0.1]), 3))  # 0.357
print(round(cross_entropy(p, [0.3, 0.4, 0.3]), 3))  # 1.204
```

## Pourquoi c'est important / où l'utilise-t-on

- **La perte par défaut en classification** : classification d'images, prédiction du mot suivant dans les modèles de langage… presque tout utilise l'entropie croisée (associée à une sortie softmax qui produit des probabilités).
- **Un gradient élégant** : avec la combinaison softmax + entropie croisée, le gradient vaut exactement $q-p$ (prédiction moins réalité), ce qui est simple, stable et facilite l'entraînement.
- Elle équivaut au **maximum de vraisemblance** : minimiser l'entropie croisée, c'est faire une [estimation du maximum de vraisemblance](../maximum-likelihood/).

## Signification pour la prévision de séries temporelles

- Lorsque la prévision est modélisée comme un **problème de classification** (par exemple prédire « hausse / stable / baisse », ou discrétiser les valeurs en intervalles pour une prévision probabiliste), l'entropie croisée est la perte naturelle.
- Les modèles de prévision probabilistes produisent une distribution des valeurs futures ; on utilise l'entropie croisée (ou sa généralisation continue) pour évaluer « à quel point la distribution prédite colle aux valeurs effectivement observées ».
- Même si les tâches de régression comme celles de KUN (Kernel U-Net) utilisent souvent la MSE, comprendre l'entropie croisée vous aide à choisir la bonne perte lorsque vous avez besoin de **sorties probabilistes / de prévisions par quantiles**.

## Idées reçues fréquentes

- **L'entropie croisée n'est pas symétrique** : $H(p,q)\ne H(q,p)$, on ne peut pas intervertir les arguments.
- Pensez à écrêter numériquement $q$ (pour éviter que $\log 0$ ne devienne infini).
- L'entropie croisée est $\ge$ l'entropie $H(p)$, avec égalité si et seulement si $q=p$ — elle n'est jamais plus économe que « connaître la vérité ».

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
