---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/cs/
title: "Fondements de l'informatique"
lead: "Programmation, structures de données et algorithmes, pile de calcul scientifique et pratiques d'ingénierie — le bagage informatique nécessaire pour faire réellement tourner un modèle. On n'y pose que la charpente et les concepts."
prev: /foundations/math/
next: /foundations/ml/
---

> Ceci est une **carte conceptuelle** : elle recense les compétences informatiques de base à maîtriser pour travailler sur les données et la modélisation ; les approfondir passe par la pratique.

## 1. Bases de la [programmation](../programming/) ([Python](../python/))

La langue commune de la science des données.

- **Types de base et [structures de données](../data-structures/)** : nombres / chaînes / listes / dictionnaires / ensembles
- **Structures de contrôle** : conditions, boucles, fonctions
- **Programmation orientée objet et modules** : classes, paquets, imports
- **Gestion des environnements** : `venv` / `conda`, dépendances et [reproductibilité](../reproducibility/)

## 2. Structures de données et [algorithmes](../algorithms/)

Écrire du code à la fois correct et rapide.

- **Structures de données essentielles** : tableaux, tables de hachage, piles / files, arbres, graphes
- **Analyse de complexité ([Big-O](../big-o/))** : coût en temps et en espace
- **Algorithmes courants** : tri, recherche, récursivité, [programmation dynamique](../dynamic-programming/)
- **Stabilité numérique** : erreurs en virgule flottante, dépassement de capacité et soupassement

## 3. Pile de calcul scientifique

Les outils quotidiens des séries temporelles et de l'apprentissage automatique.

- **[NumPy](../numpy/)** : tableaux à N dimensions et calcul **[vectorisé](../vectorization/)** (plus rapide que les boucles Python de plusieurs ordres de grandeur)
- **[Pandas](../pandas/)** : tableaux / index temporels, rééchantillonnage, alignement
- **Matplotlib** : visualisation
- **Idée clé** : remplacer les boucles explicites par la **vectorisation**

```python
import numpy as np
x = np.arange(1000)
y = x ** 2          # vectorisation : une ligne vaut mieux qu'une boucle for
```

## 4. Notions de systèmes informatiques

Comprendre d'où vient la performance.

- **Mémoire et cache** : l'emplacement des données détermine la vitesse
- **CPU ou [GPU](../gpu/)** : pourquoi le calcul parallèle a rendu l'apprentissage profond possible
- **Parallélisme et traitement par lots** : la motivation matérielle des calculs par [lot (batch)](../batch/)
- **Formats de stockage** : compromis entre CSV / Parquet / binaire

## 5. [Pratiques d'ingénierie](../engineering-practice/)

Rendre le travail reproductible et collaboratif.

- **Gestion de versions ([Git](../git/))** : commits, branches, collaboration
- **Jupyter Notebook** : exploration et présentation interactives
- **Reproductibilité** : fixer les graines aléatoires, consigner les versions des dépendances
- **Débogage et journalisation** : localiser les problèmes plutôt que modifier à l'aveugle

---

**Termes clés :** [Python](../python/), [structures de données](../data-structures/), [complexité Big-O](../big-o/), [programmation dynamique](../dynamic-programming/), [NumPy](../numpy/), [vectorisation](../vectorization/), [Pandas](../pandas/), [parallélisme GPU](../gpu/), [batch](../batch/), [Git](../git/), [reproductibilité](../reproducibility/).
