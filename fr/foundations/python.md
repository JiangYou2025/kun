---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/python/
title: "Python"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

**Python** est le principal langage de programmation de la science des données et de l'[apprentissage automatique](../ml/). Sa syntaxe est concise, il s'apprend vite et il dispose d'un écosystème extrêmement riche : [NumPy](../numpy/), [Pandas](../pandas/), PyTorch, etc. Tous les exemples pratiques de ce cours sont en Python.

## Intuition

Si la [programmation](../programming/) consiste à « écrire une idée sous forme d'instructions », Python est un langage d'instructions **particulièrement proche de la langue naturelle**. Il a été délibérément conçu pour être simple :

```python
for name in ["Alice", "Bob"]:
    print(f"Bonjour, {name}")
```

On peut presque le lire mot à mot : « pour chaque nom de la liste, afficher une salutation ». Pas de points-virgules, pas d'accolades : l'indentation délimite les blocs de code. **C'est parce que la barrière d'entrée est basse que les chercheurs peuvent consacrer leur énergie à leurs « idées » plutôt qu'à « se battre avec le langage »** — c'est aussi ce qui en a fait le standard de fait du calcul scientifique.

Python a toutefois un prix : c'est un langage **interprété**, et les boucles en Python pur élément par élément sont lentes — c'est précisément ce que la [vectorisation](../vectorization/) de [NumPy](../numpy/) vient compenser.

## Points essentiels

Quelques-unes des fonctionnalités les plus utilisées du langage :

- **Typage dynamique** : pas besoin de déclarer le type d'une variable ; après `x = 3`, on peut encore écrire `x = "abc"`.
- **Structures de données de base** : liste `list`, dictionnaire `dict`, ensemble `set`, tuple `tuple` (voir les [structures de données](../data-structures/)).
- **Listes en compréhension** : générer une liste en une ligne, `[x**2 for x in range(5)]` → `[0,1,4,9,16]`.
- **Fonctions et paramètres par défaut** : `def f(x, lr=0.01): ...`.
- **Une bibliothèque standard riche et un vaste écosystème tiers** : un `import` et c'est prêt.
- **Gestion des paquets et des environnements** : installer des paquets avec `pip`, isoler les environnements avec `venv` / `conda` (cela relève des [bonnes pratiques d'ingénierie](../engineering-practice/)).

## Un exemple

Une petite démonstration de quelques tournures typiques de Python :

```python
# Liste en compréhension + condition
evens = [x for x in range(10) if x % 2 == 0]   # [0,2,4,6,8]

# Dictionnaire : retrouver une caractéristique à partir d'une date
holiday = {"2026-01-01": "Jour de l'an", "2026-05-01": "Fête du Travail"}
print(holiday.get("2026-01-01", "Jour ouvré"))      # Jour de l'an
print(holiday.get("2026-03-15", "Jour ouvré"))      # Jour ouvré (valeur par défaut)

# Déballage de tuple : une fonction qui renvoie plusieurs valeurs
def min_max(xs):
    return min(xs), max(xs)

lo, hi = min_max([3, 7, 1, 9])
print(lo, hi)                                     # 1 9

# Formatage avec les f-strings
mae = 0.12345
print(f"MAE de test = {mae:.3f}")                 # MAE de test = 0.123
```

Ces tournures sont concises mais très expressives : ce sont des outils de tous les jours pour manipuler des données.

## Intérêt pour la prévision de séries temporelles

Python porte ce cours de bout en bout, des données jusqu'au modèle :

- **Traitement des données** : [Pandas](../pandas/) lit, aligne et rééchantillonne les séries temporelles.
- **Calcul numérique** : [NumPy](../numpy/) réalise les opérations [vectorisées](../vectorization/) comme le découpage en fenêtres, la normalisation ou la FFT.
- **Modélisation et entraînement** : PyTorch construit et entraîne **KUN / Kernel U-Net**, accéléré sur [GPU](../gpu/).
- **Visualisation et restitution** : Matplotlib trace les courbes de prévision et la distribution des erreurs.

Toute la [pile de calcul scientifique](../scientific-computing/) repose sur Python — **bien maîtriser Python, c'est obtenir la clé qui ouvre la pratique de la prévision de séries temporelles.**

## Erreurs fréquentes

- **Croire que Python est trop lent pour le calcul scientifique** : les boucles en Python pur sont effectivement lentes, mais en déléguant le calcul à la couche C via [NumPy](../numpy/), la vitesse est largement suffisante.
- **Mauvaise indentation** : Python délimite les blocs par l'indentation ; mélanger espaces et tabulations provoque directement une erreur.
- **Le piège des paramètres par défaut mutables** : dans `def f(x, cache=[])`, la liste `[]` n'est créée qu'une seule fois et partagée entre les appels ; utilisez plutôt `None` et initialisez à l'intérieur de la fonction.
- **Ne pas isoler les environnements** : si tous les projets partagent les mêmes paquets, les conflits de versions finissent toujours par arriver ; prenez l'habitude d'utiliser `venv` / `conda`.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
