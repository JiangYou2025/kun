---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/numpy/
title: "NumPy"
no_comments: true
---

> Extrait de [Fondements de l'informatique](../cs/) · [Vue d'ensemble du cours de base](../)

**NumPy** est la pierre angulaire du calcul numérique en [Python](../python/). Il fournit un type de tableau multidimensionnel efficace, `ndarray`, ainsi qu'un ensemble complet de fonctions effectuant des opérations [vectorisées](../vectorization/) sur des tableaux entiers. Presque toutes les bibliothèques de calcul scientifique et d'[apprentissage automatique](../ml/) (Pandas, scikit-learn, PyTorch) reposent sur lui.

## Intuition

La `list` native de Python est flexible, mais lente : chacun de ses éléments est un objet Python indépendant, dispersé quelque part en mémoire, et les opérations doivent être interprétées une à une.

Le `ndarray` de NumPy est différent : il **range de manière compacte des nombres d'un même type dans une mémoire contiguë**, et confie les calculs à des boucles de bas niveau écrites en C, exécutées d'un seul coup. Résultat : **pour un même calcul, NumPy est souvent des dizaines, voire des centaines de fois plus rapide que du Python pur**, avec un code plus court.

En une phrase : **NumPy vous permet d'écrire du code comme on écrit une formule mathématique, en laissant les boucles au bas niveau.**

## Points essentiels

- **ndarray** : un tableau à N dimensions, doté de deux attributs fondamentaux, `shape` (la forme) et `dtype` (le type des éléments).
- **[Vectorisation](../vectorization/)** : `a + b`, `a * 2`, `np.sqrt(a)` s'appliquent directement au tableau entier, sans écrire de boucle.
- **Diffusion (broadcasting)** : des tableaux de formes différentes mais compatibles s'alignent automatiquement pour le calcul, par exemple « soustraire le même vecteur à chaque ligne d'une matrice ».
- **Découpage et indexation** : `a[1:5]`, `a[:, 0]`, `a[a > 0]` (indexation booléenne) sont souples et efficaces, et renvoient le plus souvent des **vues** (sans copier les données).
- **Axes (axis)** : on précise la direction d'une agrégation ; `a.mean(axis=0)` calcule la moyenne par colonne, `axis=1` par ligne.

## Un exemple

Mesurez la puissance de la vectorisation — élever au carré et ajouter 1 à un million de nombres :

```python
import numpy as np

a = np.arange(1_000_000, dtype=float)

# À la manière NumPy : une ligne, boucle C en dessous
b = a ** 2 + 1          # tout le tableau calculé d'un coup

# Équivalent en Python pur : bien plus lent
# b = [x**2 + 1 for x in a]
```

La diffusion rend la « standardisation par colonne » très élégante :

```python
X = np.random.randn(1000, 5)          # 1000 exemples, 5 variables
mean = X.mean(axis=0)                  # forme (5,), moyenne de chaque colonne
std  = X.std(axis=0)                   # forme (5,)
X_norm = (X - mean) / std              # (1000,5) moins / divisé par (5,) automatiquement
print(X_norm.mean(axis=0).round(6))    # moyenne de chaque colonne ≈ 0
print(X_norm.std(axis=0).round(6))     # écart-type de chaque colonne ≈ 1
```

Qu'une matrice `(1000, 5)` et un vecteur `(5,)` puissent être combinés directement, c'est la **diffusion** : le vecteur est automatiquement « recopié » sur chaque ligne — sans être réellement copié, ce qui économise mémoire et temps.

## Intérêt pour la prévision de séries temporelles

NumPy est le moteur de bas niveau du traitement des données temporelles :

- **Fenêtres glissantes** : découper une longue série en exemples d'entraînement « L pas passés → H pas futurs » ; `np.lib.stride_tricks.sliding_window_view` génère toutes les fenêtres sans copie, des ordres de grandeur plus vite qu'une boucle Python.

  ```python
  series = np.arange(10)
  windows = np.lib.stride_tricks.sliding_window_view(series, 3)
  # forme (8, 3) : chaque ligne est une fenêtre de longueur 3, sans copie mémoire supplémentaire
  ```

- **Mathématiques par lots** : différenciation, normalisation, statistiques glissantes, spectre par FFT — tout se fait par opérations sur des tableaux.
- **Un maillon central** : les colonnes de [Pandas](../pandas/) sont, en dessous, des tableaux NumPy ; les tenseurs fournis à **KUN / Kernel U-Net** sont eux aussi convertis depuis des tableaux NumPy. Maîtriser NumPy, c'est ouvrir toute la [pile de calcul scientifique](../scientific-computing/).

## Erreurs fréquentes

- **Écrire encore des boucles Python `for` pour traiter un tableau élément par élément** : c'est renoncer à tous les avantages de NumPy ; utilisez plutôt la [vectorisation](../vectorization/).
- **Confondre vue et copie** : un découpage renvoie généralement une **vue** ; la modifier modifie le tableau d'origine. Pour une copie indépendante, appelez explicitement `.copy()`.
- **Négliger le dtype** : une division ou un dépassement de capacité sur un tableau d'entiers peut donner des résultats inattendus ; utilisez `astype(float)` si nécessaire.
- **Formes incompatibles** : les règles de diffusion alignent les dimensions **de droite à gauche** ; en cas d'erreur, on obtient un `shape mismatch`.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble du cours de base](../)
