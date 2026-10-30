---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/batch/
title: "Batch (lot)"
no_comments: true
math: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

Un **batch (lot)** est le petit groupe d'exemples que l'on fournit d'un coup au modèle lors de l'entraînement d'un [réseau de neurones](../neural-network/). Le modèle calcule le [gradient](../gradient/) sur ce lot, met à jour ses paramètres une fois, puis passe au lot suivant, et ainsi de suite.

## Intuition

Supposons que vous deviez ajuster votre manière de résoudre des problèmes à partir de 10 000 exercices. Trois rythmes sont possibles :

- **Corriger après chaque exercice** : dès qu'un exercice est terminé, on réfléchit et on s'ajuste. Réaction rapide, mais un exercice isolé est très aléatoire, et la méthode risque d'osciller d'un côté à l'autre. Cela correspond à **batch size = 1** ([descente de gradient](../gradient-descent/) stochastique, SGD).
- **Tout faire, puis corriger** : on fait les 10 000 exercices, on fait le bilan global des erreurs et on s'ajuste en une seule fois. La direction est la plus juste, mais c'est trop lent, trop gourmand en mémoire, et l'on ne s'ajuste qu'une fois par tour. Cela correspond au **full batch**.
- **Corriger tous les 32 exercices** : on réfléchit et on s'ajuste une fois tous les 32 exercices. On bénéficie d'une certaine stabilité statistique tout en mettant à jour fréquemment. C'est le **mini-batch**, le compromis utilisé presque toujours en pratique.

**Le batch est par essence un compromis entre « efficacité » et « stabilité ».**

## Points essentiels

- **batch size** : le nombre d'exemples dans un lot. Valeurs courantes : 16, 32, 64, 128, 256 ; on prend souvent une puissance de 2 pour s'accorder à l'alignement mémoire du [GPU](../gpu/).
- **iteration (itération)** : traiter un batch et mettre à jour les paramètres une fois constitue une itération.
- **epoch (époque)** : parcourir une fois l'ensemble d'entraînement en entier constitue une epoch.
  - Relation : `nombre d'itérations par epoch = nombre total d'exemples / batch size` (arrondi à l'entier supérieur).

Effet de la batch size :

- **Plus elle est grande** : l'estimation du gradient est plus lisse et plus stable, le parallélisme du GPU est mieux exploité, mais la mémoire consommée augmente, et la [généralisation](../generalization/) est parfois un peu moins bonne.
- **Plus elle est petite** : les mises à jour sont plus fréquentes et la mémoire occupée est faible, mais le gradient est bruité et l'entraînement instable.

{% include fviz/batch-size.html %}

## Un exemple

PyTorch découpe automatiquement les données en lots avec `DataLoader` :

```python
import torch
from torch.utils.data import TensorDataset, DataLoader

# supposons 1000 exemples, chacun avec 7 caractéristiques
X = torch.randn(1000, 7)
y = torch.randn(1000, 1)

loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

for epoch in range(3):
    for xb, yb in loader:        # on prend un batch à chaque fois
        # xb.shape == (32, 7) ; le dernier lot peut en contenir moins de 32
        pred = model(xb)         # une propagation avant : tout le lot calculé ensemble
        loss = loss_fn(pred, yb)
        loss.backward()          # gradient calculé sur ce lot
        optimizer.step()         # une mise à jour des paramètres
        optimizer.zero_grad()
```

1000 / 32 ≈ 32 itérations font une epoch. Notez que la première dimension de `xb` est la dimension du batch — tout le lot est **empilé dans un seul tenseur** et calculé d'un coup ; c'est exactement là que le [GPU](../gpu/) et la [vectorisation](../vectorization/) montrent leur puissance.

## Intérêt pour la prévision de séries temporelles

Lors de l'entraînement de modèles de prévision comme **KUN / Kernel U-Net** :

- Chaque exemple est généralement une **fenêtre glissante** : on utilise les `L` pas passés pour prédire les `H` pas futurs. Un batch est alors un tenseur de forme `(batch_size, L, nombre de caractéristiques)`.
- La dimension du batch permet de **calculer de nombreuses fenêtres en parallèle**, d'exploiter pleinement le GPU et de réduire fortement le temps d'entraînement.
- Attention avec les données temporelles : `shuffle=True` mélange l'ordre **entre les exemples (fenêtres)**, mais pas l'ordre temporel **à l'intérieur** d'une fenêtre — cet ordre interne ne doit jamais être modifié, sous peine de détruire la structure temporelle.

## Idées reçues

- **Confondre batch size et capacité du modèle** : la batch size n'influe que sur la dynamique de l'entraînement, pas sur la complexité de ce que le modèle peut apprendre.
- **Croire qu'un batch plus grand est toujours meilleur** : un grand batch fait gagner du temps, mais la mémoire peut saturer, et il faut parfois augmenter le [taux d'apprentissage](../learning-rate/) en conséquence.
- **Mélanger n'importe comment des données temporelles** : on peut mélanger l'ordre des fenêtres, mais jamais les pas de temps à l'intérieur d'une fenêtre, et il faut aussi éviter que les fenêtres d'entraînement « voient en douce » les données futures de l'ensemble de validation.
- **Oublier que le dernier lot est incomplet** : avec 1000 exemples et batch=32, le dernier lot ne contient que 8 exemples ; le code doit le gérer correctement.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
