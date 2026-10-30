---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/dynamic-programming/
title: "Programmation dynamique"
no_comments: true
math: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

La **programmation dynamique (Dynamic Programming, DP)** est un paradigme [algorithmique](../algorithms/) : on décompose un grand problème en de nombreux petits problèmes **qui se chevauchent**, et l'on **mémorise** la réponse de chacun pour éviter de la recalculer encore et encore.

## Intuition

L'exemple classique est la suite de Fibonacci $F(n) = F(n-1) + F(n-2)$.

Que se passe-t-il avec une récursion directe ? Pour calculer $F(5)$, il faut $F(4)$ et $F(3)$ ; pour calculer $F(4)$, il faut à nouveau $F(3)$ et $F(2)$… **$F(3)$ est calculé plusieurs fois**, les répétitions s'aggravent à mesure qu'on descend, et le temps total devient exponentiel, en $O(2^n)$.

L'idée de la programmation dynamique : **calculer $F(3)$ une seule fois, le noter, et le lire dans la table la fois suivante.** Chaque sous-problème n'est alors calculé qu'une fois, et la complexité tombe immédiatement à $O(n)$.

Pour qu'un problème se prête à la DP, il doit en général satisfaire deux conditions :

- **Sous-problèmes qui se chevauchent** : les mêmes petits problèmes reviennent de façon répétée (sinon la mise en cache ne sert à rien).
- **Sous-structure optimale** : la solution optimale du grand problème peut se construire à partir des solutions optimales des petits.

## Points essentiels

La DP s'implémente selon deux styles équivalents :

- **Descendant + mémoïsation (memoization)** : on écrit la récursion habituelle, mais on met en cache les résultats déjà calculés pour les renvoyer directement la fois suivante.
- **Ascendant + tabulation (tabulation)** : on part des plus petits sous-problèmes et l'on remplit une table (un tableau) pas à pas jusqu'à l'objectif.

Concevoir une DP en trois étapes :

1. **Définir l'état** : quelles variables décrivent un sous-problème (par exemple « la solution optimale pour les i premiers éléments »).
2. **Écrire l'équation de transition** : comment déduire un grand état des petits.
3. **Fixer les cas de base** : quelle est la réponse des plus petits sous-problèmes.

## Un exemple

Comparons la récursion naïve et la version avec cache :

```python
# Récursion naïve : exponentielle en O(2^n), d'une lenteur absurde dès n=40
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# DP ascendante : O(n) en temps, O(1) en espace
def fib_dp(n):
    if n < 2:
        return n
    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur   # on ne garde que les deux derniers états
    return cur

print(fib_dp(50))      # 12586269025, résultat instantané
```

[Python](../python/) propose même un décorateur intégré qui ajoute la mémoïsation en une ligne :

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
# avec le cache, la récursion exponentielle devient immédiatement O(n)
```

## Intérêt pour la prévision de séries temporelles

La programmation dynamique est le moteur de nombreux algorithmes classiques sur les séries temporelles :

- **DTW (déformation temporelle dynamique)** : mesure la similarité de deux séries « désynchronisées », l'une plus rapide que l'autre. Elle utilise une table DP à deux dimensions où chaque case $D[i][j]$ représente la distance cumulée minimale de l'alignement des préfixes des deux séries, avec l'équation de transition :

  $$D[i][j] = d(a_i, b_j) + \min\big(D[i-1][j],\ D[i][j-1],\ D[i-1][j-1]\big)$$

- **Algorithme de Viterbi** : trouve la suite d'états la plus probable dans un modèle de Markov caché, en cherchant efficacement l'optimum dans un espace de chemins de taille exponentielle grâce à la DP.
- **Détection de ruptures, segmentation optimale** : découper une série en segments de façon à minimiser l'erreur totale se résout aussi souvent par DP.

Face à de longues séries, c'est précisément le principe « calculer une fois, mémoriser » de la DP qui permet à ces algorithmes de ramener une recherche exhaustive exponentielle à un temps polynomial.

## Pièges courants

- **Croire que la DP, c'est la récursion** : la récursion n'est qu'une façon d'écrire ; l'âme de la DP est la **mise en cache des réponses des sous-problèmes**. Sans sous-problèmes qui se chevauchent, le cache est inutile.
- **Un état mal défini** : si l'état est mal défini, l'équation de transition sera forcément fausse. Réfléchissez d'abord à « ce qui décrit un sous-problème ».
- **Oublier les cas de base** : si les valeurs initiales des plus petits sous-problèmes manquent ou sont fausses, toute la table s'effondre.
- **Ne pas optimiser l'espace** : beaucoup de DP ne dépendent que des un ou deux derniers états (comme Fibonacci), ce qui permet de passer de $O(n)$ à $O(1)$ en espace.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
