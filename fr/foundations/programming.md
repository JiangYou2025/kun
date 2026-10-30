---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/programming/
title: "Programmation"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

**Programmer**, c'est décomposer une idée en instructions explicites qu'un ordinateur peut exécuter pas à pas. C'est la compétence de base qui permet de « faire tourner » les mathématiques et les modèles et de mener des expériences concrètes. Tous les exemples de ce cours utilisent [Python](../python/).

## Intuition

Programmer ressemble beaucoup à écrire une recette pour un cuisinier **extrêmement obéissant mais totalement dépourvu de bon sens** :

- Impossible d'écrire « faire sauter jusqu'à ce que ce soit à peu près cuit » — il faut préciser « faire sauter 3 minutes à feu moyen ».
- Le cuisinier suit les instructions à la lettre ; mais si vous vous trompez d'une étape (du sucre à la place du sel), il ne corrigera jamais : il préparera fidèlement le mauvais plat.

L'essentiel de la programmation n'est donc pas de retenir une syntaxe, mais de **décomposer une idée floue en étapes précises, sans ambiguïté et ordonnées** — cette « pensée computationnelle » est la vraie compétence ; la syntaxe n'est que l'outil qui l'exprime.

## Points essentiels

Presque tous les programmes sont construits à partir de quelques briques :

- **Variables** : donner un nom à une donnée pour la stocker, `lr = 0.001`.
- **Types de données** : nombres, chaînes de caractères, listes, dictionnaires, etc. (voir [structures de données](../data-structures/)).
- **Structures de contrôle** :
  - conditions `if / else` : suivre des branches différentes selon la situation ;
  - boucles `for / while` : répéter une action.
- **Fonctions** : empaqueter un morceau de logique, lui donner un nom et le réutiliser, pour éviter le code dupliqué.
- **Modules / bibliothèques** : des fonctionnalités écrites par d'autres, prêtes à l'emploi, comme [NumPy](../numpy/) et [Pandas](../pandas/).

Les bonnes habitudes d'écriture — **des noms clairs, des fonctions courtes, une seule tâche par fonction, des messages en cas d'erreur** — relèvent des [bonnes pratiques d'ingénierie](../engineering-practice/).

## Un exemple

Traduire en code l'idée « calculer la moyenne glissante d'une série » :

```python
def moving_average(series, window):
    """Moyenne glissante de series sur une fenêtre de taille window ; renvoie une nouvelle liste"""
    if window <= 0:                      # défensif : vérification des paramètres
        raise ValueError("window doit être strictement positif")
    result = []
    for i in range(len(series)):
        start = max(0, i - window + 1)   # borne gauche de la fenêtre
        chunk = series[start : i + 1]    # valeurs dans la fenêtre
        result.append(sum(chunk) / len(chunk))
    return result

data = [10, 12, 14, 13, 15, 16]
print(moving_average(data, 3))
# [10.0, 11.0, 12.0, 13.0, 14.0, 14.666...]
```

Cet exemple réunit toutes les briques : l'encapsulation dans une **fonction**, la **vérification des paramètres** (if), la **boucle** de parcours, les **variables** pour les résultats intermédiaires. Une fois la [vectorisation](../vectorization/) apprise, vous verrez que [NumPy](../numpy/) / [Pandas](../pandas/) font la même chose en une ligne, et plus vite — mais c'est en comprenant la version avec boucle qu'on saisit ce que la vectorisation fait gagner.

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, la programmation intervient du début à la fin :

- **Prétraitement des données** : lire les fichiers, aligner les dates, combler les valeurs manquantes, découper en fenêtres glissantes — tout cela, c'est du code.
- **Implémenter et modifier les modèles** : pour faire tourner **KUN / Kernel U-Net**, ajuster son architecture ou y ajouter des modules, il faut savoir lire et modifier du code.
- **Lancer des expériences, tracer des courbes, calculer des métriques** : derrière chaque conclusion se trouve un script que l'on peut réexécuter.

Savoir programmer, c'est pouvoir passer de « lire des articles » à « vérifier et améliorer soi-même ». **Si vous ne savez pas exécuter le code, un modèle n'est pour vous qu'une figure.**

## En résumé

- Programmer = décomposer une idée en instructions précises, ordonnées et sans ambiguïté ; l'essentiel est la pensée computationnelle, pas la syntaxe apprise par cœur.
- Les briques : variables, types de données, structures de contrôle (if / boucles), fonctions, bibliothèques.
- Du bon code : des noms clairs, des fonctions courtes, une gestion des erreurs — ce qui mène aux [bonnes pratiques d'ingénierie](../engineering-practice/).
- Ce cours utilise [Python](../python/) ; c'est votre porte d'entrée vers toutes les expériences pratiques.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
