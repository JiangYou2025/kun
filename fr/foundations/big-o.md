---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/big-o/
title: "La complexité Big-O"
no_comments: true
math: true
---

> Extrait de [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours de base](../)

La **notation Big-O (grand O)** décrit, lorsque la taille d'entrée $n$ augmente, **comment évoluent** approximativement le temps ou la mémoire nécessaires à un [algorithme](../algorithms/). C'est l'étalon standard pour juger si un algorithme « passe à l'échelle ».

## Intuition

Big-O ne s'intéresse pas au « nombre de millisecondes d'exécution », mais à la question : « **si les données doublent, par combien le coût est-il multiplié ?** » Elle ignore délibérément les constantes et les termes d'ordre inférieur pour ne regarder que la « forme » de la croissance.

Prenons une analogie : transmettre un avis à un groupe de personnes.

- Publier une annonce dans le groupe de discussion — une seule étape, quel que soit le nombre de personnes. C'est $O(1)$, le **temps constant**.
- Appeler chacun au téléphone — deux fois plus de personnes, deux fois plus d'appels. C'est $O(n)$, **linéaire**.
- Demander à chacun de serrer la main de tous les autres — deux fois plus de personnes, quatre fois plus de poignées de main. C'est $O(n^2)$, **quadratique**.

$$O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(2^n)$$

Plus on est à gauche, mieux c'est. Attention à la croissance **exponentielle** comme $O(2^n)$ : dès $n=50$, on atteint des nombres astronomiques, et le calcul devient en pratique « impossible à exécuter ».

{% include fviz/big-o.html %}

## Points essentiels

Comment lire la complexité d'un morceau de code ? Regardez l'imbrication des boucles :

- Pas de boucle, seulement quelques affectations → $O(1)$.
- Une boucle qui parcourt les données une fois → $O(n)$.
- Deux boucles imbriquées qui s'exécutent chacune $n$ fois → $O(n^2)$.
- La taille du problème est divisée par deux à chaque étape → un $\log n$ apparaît.
- Diviser pour régner + un parcours complet à chaque niveau (comme le tri fusion) → $O(n\log n)$.

Deux règles de simplification :

- **Supprimer les coefficients constants** : $O(3n)$ s'écrit $O(n)$.
- **Ne garder que le terme d'ordre le plus élevé** : $O(n^2 + n)$ s'écrit $O(n^2)$.

Par défaut, Big-O décrit une borne supérieure de la croissance dans le **pire cas**.

## Un exemple

Les trois fonctions ci-dessous ont chacune une complexité différente :

```python
def first(arr):              # O(1) : ne regarde que le premier élément
    return arr[0]

def total(arr):             # O(n) : un seul parcours
    s = 0
    for x in arr:
        s += x
    return s

def all_pairs(arr):         # O(n^2) : compare chaque paire
    dups = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                dups.append((i, j))
    return dups
```

Effet approximatif lorsque les données passent de 1 000 à 1 million d'éléments (×1 000) :

| Complexité | Données ×1000, temps environ ×… |
|---|---|
| $O(1)$ | ×1 (quasiment inchangé) |
| $O(n)$ | ×1000 |
| $O(n\log n)$ | un peu plus de ×1000 |
| $O(n^2)$ | **×1 million** |

`all_pairs` termine instantanément sur 1 000 éléments, mais peut tourner pendant des heures sur 1 million — **voilà pourquoi la complexité compte davantage que la vitesse de la machine**.

## Signification pour la prévision de séries temporelles

Pour la prévision de longues séries, la complexité détermine directement la faisabilité :

- L'[auto-attention](../attention/) naïve (du [Transformer](../transformer/)) coûte $O(n^2)$ pour une séquence de longueur $n$ ; dès que la séquence s'allonge, la mémoire GPU et le temps de calcul explosent — c'est précisément le problème que cherchent à résoudre les diverses « attentions efficaces ».
- La **FFT** fait passer l'analyse spectrale de $O(n^2)$ à $O(n\log n)$, ce qui rend possible l'analyse des périodicités sur de longues séries.
- **KUN / Kernel U-Net** raccourcit la séquence par sous-échantillonnage couche après couche, évitant ainsi des opérations coûteuses sur la longueur d'origine ; il s'agit au fond d'échanger de la structure contre une complexité plus faible.

Quand le volume de données passe de quelques milliers de pas de temps à plus d'un million, **la différence entre $O(n^2)$ et $O(n\log n)$, c'est la différence entre « impossible à exécuter » et « un résultat en quelques secondes ».**

## Idées reçues fréquentes

- **Prendre Big-O pour un nombre exact de secondes** : elle ne décrit qu'une tendance de croissance, ce n'est pas un chronomètre. Sur de petites données, un algorithme en $O(n^2)$ peut même être plus rapide qu'un algorithme en $O(n\log n)$ (constante plus petite).
- **Négliger la complexité en espace** : la mémoire se mesure aussi en Big-O, et il faut faire le compte avec soin, surtout quand on échange de la mémoire cache contre de la vitesse.
- **Croire que le terme d'ordre le plus élevé domine toujours** : ce n'est vrai que pour $n$ suffisamment grand ; pour un petit $n$, les termes constants peuvent compter davantage.
- **Confondre « pire cas » et « cas moyen »** : la recherche dichotomique est en $O(\log n)$ dans le pire cas, mais elle suppose d'abord que « les données sont triées ».

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours de base](../)
