---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/data-structures/
title: "Structures de données"
no_comments: true
math: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

Une **structure de données** est une manière d'organiser et de stocker des données. Avec la bonne structure, les opérations courantes (recherche, insertion, suppression) sont rapides ; avec la mauvaise, le même [algorithme](../algorithms/) peut être plus lent de plusieurs ordres de grandeur.

## Intuition

Les structures de données sont comme des outils de rangement, chacun excellant dans une tâche différente :

- Le **tableau (list)** ressemble à une rangée de casiers numérotés à la suite : connaissant le numéro, on récupère instantanément le contenu ($O(1)$), mais pour en insérer un au milieu, il faut décaler tous les suivants.
- La **table de hachage (dict)** ressemble à un dictionnaire avec index : on annonce la « clé » et l'on tombe aussitôt sur la « valeur » correspondante, en $O(1)$ en moyenne.
- La **pile** ressemble à une pile d'assiettes : on ne peut prendre ou poser que par le dessus (dernier entré, premier sorti).
- La **file** ressemble à une file d'attente au guichet : le premier arrivé est le premier servi (premier entré, premier sorti).
- L'**arbre / le graphe** ressemble à un arbre généalogique ou à un plan de métro : il exprime des hiérarchies et des connexions.

**Il n'existe pas de « meilleure » structure de données, seulement celle qui convient le mieux aux opérations à effectuer.**

## Points essentiels

La complexité d'une même opération varie fortement d'une structure à l'autre :

| Structure | Accès par position | Recherche par valeur | Insertion/suppression | Usage typique |
|---|---|---|---|---|
| Tableau list | $O(1)$ | $O(n)$ | au milieu $O(n)$ | stockage séquentiel, accès aléatoire |
| Table de hachage dict/set | — | $O(1)$ amorti | $O(1)$ amorti | détection de doublons, comptage, table de correspondance |
| Pile/file | — | $O(n)$ | aux extrémités $O(1)$ | annulation, parcours en largeur, tampon |
| Arbre équilibré | — | $O(\log n)$ | $O(\log n)$ | ensembles ordonnés, requêtes par intervalle |

Retenez un compromis fondamental : **échanger de l'espace contre du temps**. Une table de hachage occupe un peu plus de mémoire, en échange d'une recherche quasi instantanée.

## Un exemple

Une même tâche — « trouver les éléments qui apparaissent plusieurs fois » — n'a pas du tout la même complexité selon la structure utilisée :

```python
# Méthode naïve : avec une list, chaque élément est comparé à tous les précédents → O(n^2)
def dups_slow(arr):
    seen, out = [], []
    for x in arr:
        if x in seen:        # "in list" est un parcours linéaire en O(n) !
            out.append(x)
        seen.append(x)
    return out

# Méthode astucieuse : avec un set, la recherche est en O(1) → O(n) au total
def dups_fast(arr):
    seen, out = set(), []
    for x in arr:
        if x in seen:        # "in set" est en O(1) en moyenne
            out.append(x)
        seen.add(x)
    return out
```

La logique est presque identique : on a seulement remplacé `list` par `set`. Sur un million d'éléments, `dups_fast` termine presque instantanément, alors que `dups_slow` peut tourner très longtemps — **changer de structure de données est plus efficace que changer de machine.**

Une autre astuce très fréquente — compter avec un `dict` :

```python
from collections import Counter
counts = Counter(["a", "b", "a", "c", "a"])
print(counts)            # Counter({'a': 3, 'b': 1, 'c': 1})
print(counts["a"])      # 3, obtenu en O(1)
```

## Intérêt pour la prévision de séries temporelles

- **Fenêtres glissantes** : découper une longue série en échantillons « L pas passés → H pas futurs » repose sur un découpage efficace de tableaux ; avec `stride_tricks` de [NumPy](../numpy/), on peut même générer toutes les fenêtres sans aucune copie.
- **Mise en cache des résultats intermédiaires** : la [programmation dynamique](../dynamic-programming/) (DTW, Viterbi, etc.) s'appuie sur des tableaux à deux dimensions pour conserver les réponses des sous-problèmes.
- **Tables de correspondance de variables** : pour associer un horodatage à des variables comme les jours fériés ou le jour de la semaine, un `dict` permet une recherche en $O(1)$.
- Le sous-échantillonnage et les connexions résiduelles de **KUN / Kernel U-Net** consistent essentiellement à indexer et réorganiser efficacement une structure de données : le tenseur (tableau multidimensionnel).

## Résumé

- La structure de données détermine la vitesse des opérations ; elle forme un trio indissociable avec les [algorithmes](../algorithms/) et la [complexité Big-O](../big-o/).
- Le compromis central consiste à **échanger de l'espace contre du temps** : tables de hachage et caches consomment plus de mémoire pour une recherche plus rapide.
- Règle pratique : **recherches fréquentes → `set`/`dict` ; accès séquentiel → `list` ; calcul numérique par lots → tableaux [NumPy](../numpy/).**
- Une petite modification comme remplacer `list` par `set` fait souvent passer de $O(n^2)$ à $O(n)$.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
