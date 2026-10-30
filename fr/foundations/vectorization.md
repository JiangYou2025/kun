---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/vectorization/
title: "Vectorisation"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

La **vectorisation (vectorization)** consiste à remplacer les boucles explicites élément par élément par des **opérations sur des tableaux entiers**, en confiant le calcul en une seule fois à des routines rapides écrites en C/Fortran. C'est une compétence de base pour accélérer le calcul scientifique, et la condition pour bien utiliser [NumPy](../numpy/), [Pandas](../pandas/) et le [GPU](../gpu/).

## Intuition

Supposons qu'il faille ajouter un à chacun de dix mille nombres.

- **L'approche par boucle** : écrire un `for`, prendre les nombres un par un, ajouter un, les remettre en place. À chaque itération, l'interpréteur Python fait tout un travail supplémentaire (vérification de types, encapsulation d'objets) — c'est comme **demander à une personne de porter dix mille briques une à une**.
- **L'approche vectorisée** : écrire directement `a + 1`, pour dire au niveau inférieur « ajoute un à tout le tableau ». Le code C sous-jacent traite le bloc en mémoire contiguë et peut même utiliser les instructions SIMD du processeur pour calculer plusieurs valeurs à la fois — comme **un tapis roulant qui transporte une rangée entière de briques d'un coup**.

Résultat : la vectorisation est souvent **des dizaines, voire des centaines de fois** plus rapide qu'une boucle en Python pur, et le code est plus court, plus proche de l'expression mathématique. **En une phrase : ne laissez pas Python compter un par un, laissez le tableau parler d'un seul bloc.**

## Points essentiels

- **Opérations globales** : `a + b`, `a * 2`, `np.exp(a)` s'appliquent directement à tout le tableau.
- **Diffusion (broadcasting)** : des tableaux de formes différentes mais compatibles s'alignent automatiquement, sans extension explicite.
- **Indexation booléenne au lieu de boucles avec if** : `a[a < 0] = 0` réalise en une ligne « mettre les nombres négatifs à zéro ».
- **Agréger avec axis** : `a.sum(axis=0)`, `a.mean(axis=1)` remplacent les sommes par boucles imbriquées.
- **Éviter les `for` Python sur des tableaux** : c'est un anti-motif, et presque toujours réécrivable sous forme vectorisée.

Pourquoi est-ce plus rapide ? Parce que la vectorisation fait descendre la boucle de la **lente couche interprétée de Python** vers la **rapide couche compilée**, en tirant au passage parti de la mémoire contiguë et des instructions parallèles.

## Un exemple

La même tâche, boucle contre vectorisation — la différence saute aux yeux :

```python
import numpy as np

a = np.random.randn(1_000_000)

# Lent : boucle en Python pur, qui ramène les négatifs à 0 (ReLU)
def relu_loop(x):
    out = np.empty_like(x)
    for i in range(len(x)):
        out[i] = x[i] if x[i] > 0 else 0.0
    return out

# Rapide : vectorisé, en une ligne
def relu_vec(x):
    return np.maximum(x, 0)

# Les deux donnent le même résultat, mais relu_vec est généralement des dizaines de fois plus rapide
np.testing.assert_allclose(relu_loop(a), relu_vec(a))
```

Voyons un autre cas fréquent — la distance euclidienne de chaque échantillon au point central :

```python
X = np.random.randn(1000, 3)     # 1000 points en trois dimensions
c = X.mean(axis=0)               # le centre, de forme (3,)

# Vectorisé : soustraction par diffusion + somme des carrés par ligne + racine carrée
dist = np.sqrt(((X - c) ** 2).sum(axis=1))   # forme (1000,)
```

Pas une seule boucle explicite, et pourtant les distances des mille points sont calculées — `X - c` s'aligne automatiquement par diffusion, et `sum(axis=1)` somme le long de l'axe des variables.

## Intérêt pour la prévision de séries temporelles

La vectorisation est omniprésente dans une chaîne de traitement de séries temporelles, et décide directement si l'on peut traiter de gros volumes de données :

- **Découper des fenêtres glissantes** : `np.lib.stride_tricks.sliding_window_view` génère d'un coup toutes les fenêtres « des L derniers pas », sans copie, bien plus vite que de découper en boucle une fenêtre après l'autre.
- **Normalisation / différenciation par lots** : soustraire la moyenne et diviser par l'écart-type, ou calculer la différence première, sur une série entière ou tout un [batch](../batch/) — ce ne sont que des opérations sur tableaux.
- **Nourrir le [GPU](../gpu/)** : pour entraîner **KUN / Kernel U-Net**, les fenêtres d'un batch sont empilées en un tenseur, et les convolutions et sous-échantillonnages sont calculés en parallèle sur tout le lot — seul un code vectorisé empêche les milliers de cœurs du GPU de tourner à vide.

On peut le dire : **sans maîtriser la vectorisation, on ne tire pas parti de toute la [pile de calcul scientifique](../scientific-computing/), et on n'arrive pas à nourrir le GPU.**

## Idées reçues fréquentes

- **Croire que vectoriser, c'est seulement « écrire plus court »** : sa vraie valeur est de faire descendre le calcul vers la couche compilée et le matériel parallèle — c'est une **accélération qualitative**.
- **Vectoriser aveuglément au point de saturer la mémoire** : la vectorisation crée souvent d'un coup de gros tableaux intermédiaires ; sur des séquences très longues, il faut arbitrer avec la mémoire et, si nécessaire, traiter par blocs.
- **Forcer la vectorisation sur une logique fortement dépendante** : un calcul où chaque étape dépend de la précédente, comme la [programmation dynamique](../dynamic-programming/), se vectorise difficilement en entier ; envisagez une bibliothèque spécialisée ou Numba.
- **Oublier les règles de diffusion** : les dimensions s'alignent de droite à gauche ; une erreur provoque une erreur de forme ou un résultat inattendu.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
