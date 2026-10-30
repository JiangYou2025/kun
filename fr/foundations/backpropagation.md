---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/backpropagation/
title: "Rétropropagation"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **rétropropagation (backpropagation)** est l'algorithme qui calcule efficacement le [gradient](../gradient/) de la [fonction de perte](../loss-function/) par rapport à **chacun des poids** du réseau. Il s'agit au fond d'une application systématique de la **[règle de dérivation en chaîne](../chain-rule/)** à un réseau multicouche : l'erreur repart de la couche de sortie et remonte couche par couche, en indiquant au passage à chaque paramètre « dans quelle direction et de combien il doit être ajusté ».

## Intuition

Une fois la prédiction obtenue par [propagation avant](../forward-propagation/), on dispose d'une erreur (la perte). Mais le réseau compte des milliers, voire des millions de poids : **qui est fautif, et dans quelle mesure ?**

Imaginez une chaîne de production qui a sorti une pièce défectueuse. On remonte les responsabilités depuis le produit fini : on regarde d'abord la contribution de la dernière opération à l'erreur, puis comment celle-ci a été influencée par l'opération précédente… et l'on répartit ainsi la « responsabilité » au prorata jusqu'à chaque poste. La rétropropagation est ce **système automatique d'attribution des responsabilités** : elle calcule pour chaque poids un gradient qui indique « comment varie la perte si ce poids augmente légèrement ».

L'idée clé : **dériver séparément par rapport à chaque poids serait beaucoup trop lent** (il y a des millions de paramètres). La rétropropagation **réutilise astucieusement les résultats intermédiaires** et obtient tous les gradients en un seul balayage de l'arrière vers l'avant, pour un coût à peine supérieur à une propagation avant supplémentaire.

## Règle de dérivation en chaîne : la dérivation à travers les couches

Notons $\mathcal{L}$ la perte. Nous cherchons $\dfrac{\partial \mathcal{L}}{\partial W^{(l)}}$ et $\dfrac{\partial \mathcal{L}}{\partial b^{(l)}}$. Rappelons les formules de la propagation avant : $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$.

Définissons pour chaque couche le **terme d'erreur (error)** $\delta^{(l)} = \dfrac{\partial \mathcal{L}}{\partial z^{(l)}}$, qui mesure « l'influence sur la perte d'une variation de la valeur pré-activation de cette couche ».

**Couche de sortie** (couche $L$) :

$$
\delta^{(L)} = \frac{\partial \mathcal{L}}{\partial a^{(L)}} \odot \sigma'\big(z^{(L)}\big)
$$

**Récurrence vers les couches précédentes** (c'est la relation de récurrence au cœur de la rétropropagation) :

$$
\delta^{(l)} = \big( W^{(l+1)\top}\, \delta^{(l+1)} \big) \odot \sigma'\big(z^{(l)}\big)
$$

Une fois les $\delta^{(l)}$ connus pour chaque couche, les gradients sont simples :

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}} = \delta^{(l)}\, a^{(l-1)\top},
\qquad
\frac{\partial \mathcal{L}}{\partial b^{(l)}} = \delta^{(l)}
$$

Explication des symboles :

- $\delta^{(l)}$ : le signal d'erreur de la couche $l$ (de même dimension que le nombre de [neurones](../neuron/) de cette couche).
- $W^{(l+1)\top}$ : la **transposée** de la matrice de poids de la couche suivante — elle « ramène » l'erreur de la couche $l+1$ vers la couche $l$.
- $\odot$ : le **produit élément par élément** (produit de Hadamard).
- $\sigma'(z^{(l)})$ : la **dérivée** de la [fonction d'activation](../activation-function/) dans cette couche ; elle détermine si le signal peut remonter sans entrave.
- $a^{(l-1)}$ : les activations de la couche précédente, conservées lors de la propagation avant.

Remarquez le produit répété des termes $\sigma'(z^{(l)})$ — c'est précisément la source de la [disparition / explosion du gradient](../vanishing-exploding-gradient/) : plus il y a de couches, plus le nombre de dérivées multipliées entre elles est grand.

## Un exemple concret

Considérons la chaîne la plus simple à deux couches : $z_1 = w_1 x$, $a_1 = \sigma(z_1)$, $z_2 = w_2 a_1$, $\hat y = z_2$, avec la perte $\mathcal{L} = \tfrac12 (\hat y - y)^2$. Prenons pour $\sigma$ la sigmoïde.

Calculons de l'arrière vers l'avant :

$$
\frac{\partial \mathcal{L}}{\partial \hat y} = \hat y - y
\;\Rightarrow\;
\delta_2 = \hat y - y
$$

$$
\frac{\partial \mathcal{L}}{\partial w_2} = \delta_2 \cdot a_1
$$

Remontons d'une couche :

$$
\delta_1 = (w_2 \cdot \delta_2)\cdot \sigma'(z_1),
\qquad
\frac{\partial \mathcal{L}}{\partial w_1} = \delta_1 \cdot x
$$

Avec des nombres : $x=1,\, w_1=0.5,\, w_2=2,\, y=1$. Passage avant : $z_1=0.5$, $a_1=\sigma(0.5)\approx0.622$, $\hat y = 2\times0.622=1.244$.

Passage arrière : $\delta_2 = 1.244-1 = 0.244$ ; $\partial\mathcal{L}/\partial w_2 = 0.244\times0.622 \approx 0.152$.
Dérivée de la sigmoïde : $\sigma'(z_1)=a_1(1-a_1)=0.622\times0.378\approx0.235$.
$\delta_1 = 2\times0.244\times0.235 \approx 0.115$ ; $\partial\mathcal{L}/\partial w_1 = 0.115\times1 = 0.115$.

```python
import numpy as np
sig = lambda z: 1/(1+np.exp(-z))
x, w1, w2, y = 1.0, 0.5, 2.0, 1.0
z1 = w1*x; a1 = sig(z1); yhat = w2*a1          # passage avant
d2 = yhat - y                                   # erreur de sortie
gw2 = d2*a1
d1 = w2*d2*(a1*(1-a1))                           # remontée d'une couche
gw1 = d1*x
print(round(gw1,3), round(gw2,3))               # 0.115 0.152
```

## Pourquoi c'est important / où l'utiliser

- **Sans rétropropagation, pas d'apprentissage profond moderne.** C'est elle qui rend l'entraînement de réseaux à des millions de paramètres faisable en pratique.
- Les gradients qu'elle produit sont transmis à un [optimiseur](../optimizer/) (comme [Adam](../adam/)), qui met à jour les poids selon le [taux d'apprentissage](../learning-rate/) : $W \leftarrow W - \eta\, \partial\mathcal{L}/\partial W$.
- En pratique, vous n'avez presque jamais à l'écrire vous-même — les frameworks de [différentiation automatique](../autodiff/) s'en chargent. Mais comprendre sa récurrence est indispensable pour diagnostiquer un entraînement qui ne converge pas, une explosion du gradient, etc.

## Idées reçues

- **« Rétropropagation = [descente de gradient](../gradient-descent/) »** — non. La rétropropagation se contente de **calculer les gradients** ; la manière de s'en servir pour mettre à jour les paramètres relève de l'[optimiseur](../optimizer/).
- **« Elle apprend les paramètres »** — elle ne met pas à jour les paramètres, elle fournit seulement l'information de direction.
- **« Elle n'a rien à voir avec la propagation avant »** — c'est tout le contraire : elle **dépend fortement** des valeurs intermédiaires $a^{(l)}, z^{(l)}$ conservées lors de la propagation avant.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
