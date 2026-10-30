---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/algorithms/
title: "Algorithmes"
no_comments: true
math: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

Un **algorithme** est une suite d'étapes précises et finies qui résout une classe de problèmes. À partir d'une entrée, on exécute ces étapes une à une et l'on obtient forcément, à la fin, la sortie correcte. C'est l'« âme » du programme, tandis que les [structures de données](../data-structures/) en sont le « corps » sur lequel il agit.

## Intuition

Imaginez que vous cherchiez le nom « Zhang Wei » dans un épais annuaire papier.

- **La méthode naïve** : commencer à la première page et tourner les pages une à une jusqu'à le trouver. C'est la **recherche linéaire** ; dans le pire des cas, il faut parcourir tout l'annuaire.
- **La méthode astucieuse** : ouvrir l'annuaire au milieu, regarder si « Zhang » se trouve dans la première ou la seconde moitié, écarter une moitié, puis ouvrir la moitié restante en son milieu… Chaque fois, on élimine la moitié des pages. C'est la **recherche dichotomique** (ou binaire).

Les deux méthodes trouvent la personne, mais leur efficacité n'a rien à voir. Pour un annuaire d'un million de noms, la recherche linéaire demande jusqu'à un million d'étapes dans le pire des cas, la recherche dichotomique environ 20 seulement (car $2^{20} \approx 10^6$). **Voilà la puissance des algorithmes : pour un même problème, un bon algorithme peut être des dizaines de millions de fois plus rapide.**

Un algorithme ne pose pas seulement la question « peut-on résoudre le problème ? », mais surtout « en combien de temps et avec combien de mémoire ? ». L'instrument qui le mesure est la [complexité Big-O](../big-o/).

{% include fviz/binary-search.html %}

## Points essentiels

Un algorithme doit généralement satisfaire plusieurs propriétés :

- **Finitude** : un nombre fini d'étapes ; il doit s'arrêter (pas de boucle infinie).
- **Déterminisme** : chaque étape est claire et sans ambiguïté.
- **Entrées et sorties** : il reçoit des données et renvoie un résultat.
- **Effectivité** : chaque étape peut être réalisée en un temps fini.

Pour concevoir un algorithme, les « recettes » (paradigmes) les plus courantes sont :

- **Force brute** : essayer toutes les possibilités. Simple mais souvent lent.
- **Diviser pour régner** : découper un gros problème en petits, les résoudre séparément puis combiner (par exemple le tri fusion ou la recherche dichotomique).
- **Algorithme glouton** : choisir à chaque étape ce qui semble le meilleur sur le moment, en espérant un optimum global.
- **[Programmation dynamique](../dynamic-programming/)** : décomposer le problème en sous-problèmes qui se chevauchent et mémoriser les résultats intermédiaires pour éviter de les recalculer.

## Un exemple

Comparons en Python la recherche linéaire et la recherche dichotomique :

```python
def linear_search(arr, target):
    """Parcourt du début à la fin, O(n) dans le pire des cas"""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):
    """Exige que arr soit trié ; coupe en deux à chaque fois, O(log n)"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1     # la cible est dans la moitié droite
        else:
            hi = mid - 1     # la cible est dans la moitié gauche
    return -1

data = list(range(1_000_000))   # trié : 0,1,2,...,999999
print(binary_search(data, 987654))   # affiche : 987654
```

Sur un million d'éléments, `binary_search` n'a besoin que d'une vingtaine de comparaisons ; `linear_search` peut en demander un million dans le pire des cas. Notez que la recherche dichotomique a une **condition préalable** : les données doivent être triées — ce qui illustre bien la collaboration entre algorithme et structure de données.

## Intérêt pour la prévision de séries temporelles

L'analyse des séries temporelles regorge d'algorithmes :

- **DTW (Dynamic Time Warping, déformation temporelle dynamique)** utilise la [programmation dynamique](../dynamic-programming/) pour aligner deux séries qui évoluent à des vitesses différentes.
- **La FFT (transformée de Fourier rapide)** ramène le calcul du spectre de $O(n^2)$ à $O(n\log n)$, ce qui rend l'analyse des périodicités praticable sur de longues séries.
- Pour entraîner des modèles comme **KUN / Kernel U-Net**, la manière de découper efficacement une longue série en fenêtres et d'effectuer le sous-échantillonnage par convolution relève, au fond, de la conception d'algorithmes et de structures de données.

Quand le volume de données passe de quelques milliers à plusieurs millions de pas de temps, **une implémentation en $O(n^2)$ peut tout simplement ne plus tourner**, alors que la version en $O(n\log n)$ termine en quelques secondes. Choisir le bon algorithme est souvent plus efficace que d'acheter une machine plus rapide.

## Résumé

- Algorithme = suite d'étapes finies et déterministes pour résoudre un problème ; on le juge à sa [complexité](../big-o/).
- Un même problème admet de nombreux algorithmes, dont l'efficacité peut différer de plusieurs ordres de grandeur.
- Paradigmes courants : force brute, diviser pour régner, glouton, [programmation dynamique](../dynamic-programming/).
- Algorithmes et [structures de données](../data-structures/) sont indissociables — c'est avec la bonne structure que l'algorithme devient rapide.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
