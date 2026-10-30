---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/entropy/
title: "Entropie"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

L'entropie mesure l'**incertitude** d'une [variable aléatoire](../random-variable/) : plus le résultat est difficile à deviner, plus l'entropie est élevée ; plus il est certain, plus elle est faible. C'est la pierre angulaire de la [théorie de l'information](../information-theory/), et elle quantifie aussi « la quantité minimale d'information nécessaire pour décrire une chose ».

## Intuition

Voyez l'entropie comme « **le nombre moyen de questions fermées (oui / non) à poser pour deviner la réponse** ».

- Une **pièce équilibrée**, pile ou face à 50 % chacun : il faut au minimum 1 question (« Est-ce face ? »), entropie = 1 bit.
- Une **pièce truquée** qui tombe sur face 99 % du temps : on connaît presque la réponse sans rien demander, entropie proche de 0.
- Un **dé équilibré à 16 faces**, chaque face ayant la même chance : c'est le plus difficile à deviner, entropie = 4 bits.

La règle : **plus c'est uniforme et plus il y a de possibilités → plus c'est incertain → plus l'entropie est élevée** ; plus c'est concentré sur un résultat → plus c'est certain → plus l'entropie est faible. L'entropie atteint son maximum pour la distribution uniforme.

## Formulation mathématique

L'entropie de Shannon d'une variable aléatoire discrète $X$ :

$$
H(X)=-\sum_i p_i \log p_i
$$

- $p_i$ — la probabilité de l'événement $i$ ;
- par convention, $0\log 0 = 0$ ;
- avec un $\log$ en base 2, l'unité est le **bit** ; en base $e$, c'est le **nat**.

Pourquoi $-\log p$ ? Parce que la « quantité d'information » portée par un événement est définie comme $-\log p_i$ : **plus un événement est rare, plus sa survenue apporte d'information** (« le soleil s'est levé ce matin » n'apprend presque rien ; « il a neigé aujourd'hui (dans le désert) » apporte énormément d'information). L'entropie est la **moyenne** de cette quantité d'information pondérée par les probabilités, c'est-à-dire l'espérance $\mathbb{E}[-\log p]$.

## Un exemple concret

Comparons l'entropie de deux pièces (en base 2) :

Pièce équilibrée $p=[0.5,0.5]$ :

$$
H=-(0.5\log_2 0.5+0.5\log_2 0.5)=-(0.5\cdot(-1)+0.5\cdot(-1))=1\ \text{bit}
$$

Pièce biaisée $p=[0.9,0.1]$ :

$$
H=-(0.9\log_2 0.9+0.1\log_2 0.1)\approx 0.469\ \text{bit}
$$

La seconde est plus prévisible, son entropie est plus faible.

```python
import numpy as np
def entropy(p):
    p = np.array(p)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))
print(round(entropy([0.5, 0.5]), 3))   # 1.0
print(round(entropy([0.9, 0.1]), 3))   # 0.469
```

## Pourquoi c'est important / où l'utilise-t-on

- **[Arbres de décision](../decision-tree/)** : le « gain d'information » (la baisse d'entropie avant / après une division) sert à choisir la variable la plus discriminante.
- **[Fonctions de perte](../loss-function/)** : l'[entropie croisée](../cross-entropy/) et la [divergence KL](../kl-divergence/) reposent toutes deux sur l'entropie.
- **Théorie de la compression** : l'entropie fixe la borne inférieure théorique de la compression sans perte — la longueur moyenne de codage ne peut pas être inférieure à l'entropie.

## Intérêt pour la prévision de séries temporelles

- L'entropie mesure directement la **difficulté de prévision** : pour une série à forte entropie (proche d'une marche aléatoire, très bruitée), la prévisibilité a une limite théorique, aussi puissant que soit le modèle.
- Pour évaluer « combien d'information » contient une variable ou une fenêtre d'historique, l'entropie fournit un outil quantitatif.
- Si l'entraînement de KUN (Kernel U-Net) fait intervenir des sorties probabilistes ou de classification, la borne inférieure de sa perte (l'entropie croisée) est précisément l'entropie de la vraie distribution — on ne peut jamais faire descendre la perte en dessous de l'incertitude propre aux données.

## En résumé

- Entropie = incertitude moyenne = quantité moyenne d'information $\mathbb{E}[-\log p]$.
- La distribution uniforme a l'entropie maximale ; un événement certain a une entropie nulle.
- Elle est la source commune de l'entropie croisée, de la divergence KL, du gain d'information et de la limite de compression, ainsi que l'étalon théorique de la difficulté de prévision.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
