---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/optimizer/
title: "Optimiseur"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Un **optimiseur** est l'[algorithme](../algorithms/) qui, à partir des gradients calculés par la [rétropropagation](../backpropagation/), **met effectivement à jour les paramètres du réseau**. Une fois qu'on « sait dans quelle direction aller », il décide **comment faire le pas** : quelle longueur, faut-il tenir compte des directions passées, chaque paramètre a-t-il son propre pas ? Les plus courants sont SGD, Momentum et [Adam](../adam/).

## Intuition

Imaginez l'entraînement comme une **descente de montagne les yeux bandés** à la recherche du point le plus bas (la [perte](../loss-function/) minimale). La rétropropagation vous indique la **direction de plus forte pente descendante** sous vos pieds (le gradient négatif). Mais connaître la direction ne suffit pas, il faut encore décider :

- Quelle longueur de pas ? (c'est le [taux d'apprentissage](../learning-rate/))
- Faut-il, comme une bille qui dévale la pente, **garder de l'inertie** pour franchir les petits creux ? (le momentum)
- Avancer davantage dans les directions plates et moins dans les directions escarpées ? (le pas adaptatif)

Chaque optimiseur est une combinaison différente de ces stratégies. **Optimiseur = règle qui transforme le gradient en mise à jour des paramètres.**

## Principe : du plus simple à l'adaptatif

**La [descente de gradient](../gradient-descent/) la plus simple (SGD)** :

$$
\theta_{t+1} = \theta_t - \eta\, g_t
$$

- $\theta_t$ : les paramètres à l'étape $t$ ; $g_t = \nabla_\theta \mathcal{L}$ est le gradient courant ; $\eta$ est le [taux d'apprentissage](../learning-rate/) (le pas).
- Sens : avancer d'une distance $\eta$ dans la direction du gradient négatif. C'est simple, mais cela oscille facilement d'un bord à l'autre dans les vallées étroites et converge lentement.

**Ajout du momentum** : on accumule une « vitesse » pour donner de l'inertie aux mises à jour :

$$
v_t = \beta v_{t-1} + g_t,\qquad
\theta_{t+1} = \theta_t - \eta\, v_t
$$

- $v_t$ : la vitesse (une moyenne mobile exponentielle des gradients) ; $\beta$ (par exemple 0.9) règle la part d'historique conservée.
- Effet : on **accélère** dans les directions constantes et les oscillations **se compensent** dans les directions qui font des allers-retours ; c'est plus stable et plus rapide.

**Pas adaptatif (par exemple Adam)** : on redimensionne en plus le pas de chaque paramètre — petits pas pour les paramètres dont le gradient reste grand, grands pas pour ceux qui sont rarement mis à jour. C'est ce que fait [Adam](../adam/), qui combine momentum et adaptation par paramètre.

{% include fviz/optimizer.html %}

## Un exemple concret

Minimisons $\mathcal{L}(\theta) = \theta^2$ (optimum $\theta=0$, gradient $g=2\theta$). Partons de $\theta_0 = 1$ avec $\eta=0.1$ et SGD :

$$
\theta_1 = 1 - 0.1\times(2\times1) = 0.8
$$
$$
\theta_2 = 0.8 - 0.1\times(2\times0.8) = 0.64
$$
$$
\theta_3 = 0.64 - 0.1\times(2\times0.64) = 0.512
$$

Chaque pas multiplie par 0.8 : on converge régulièrement vers 0.

```python
import torch
theta = torch.tensor([1.0], requires_grad=True)
opt = torch.optim.SGD([theta], lr=0.1)        # remplacer par torch.optim.Adam pour utiliser Adam
for step in range(3):
    opt.zero_grad()
    loss = theta**2
    loss.backward()                            # la rétropropagation calcule le gradient
    opt.step()                                 # l'optimiseur met à jour les paramètres
    print(round(theta.item(), 3))             # 0.8, 0.64, 0.512
```

Notez la répartition des rôles : `loss.backward()` ([rétropropagation](../backpropagation/) / [différentiation automatique](../autodiff/)) **ne fait que calculer les gradients** ; c'est `opt.step()` (l'optimiseur) **qui met à jour les paramètres**.

## Pourquoi c'est important / où on l'utilise

- L'optimiseur **détermine directement si l'entraînement converge, à quelle vitesse, et avec quelle précision finale**. Pour un même réseau, changer d'optimiseur peut donner des résultats radicalement différents.
- C'est, après le [taux d'apprentissage](../learning-rate/), le réglage d'entraînement le plus important. En pratique, **[Adam](../adam/) est le choix par défaut**, simple et robuste ; certains, pour pousser la généralisation au maximum, passent à SGD+Momentum et le règlent patiemment.

## Intérêt pour la prévision de séries temporelles

Lors de l'entraînement de modèles de prévision comme [Kernel U-Net (KUN)](../../kun/), une longue fenêtre d'historique et une structure multi-échelles rendent la surface de perte plus complexe et les échelles de gradient plus disparates. Le **pas par paramètre d'un optimiseur adaptatif (Adam)** est alors particulièrement utile : il équilibre automatiquement des paramètres d'échelles différentes et, associé à un [taux d'apprentissage](../learning-rate/) raisonnable, fait converger KUN rapidement et de façon stable.

## En résumé

- Optimiseur = **règle qui transforme le gradient en mise à jour des paramètres** ; le gradient est fourni par la rétropropagation.
- Évolution : SGD → + momentum (inertie) → + pas adaptatif (Adam).
- Il forme un duo avec le [taux d'apprentissage](../learning-rate/) : l'optimiseur décide « comment avancer », le taux d'apprentissage « de combien ».

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
