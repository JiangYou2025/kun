---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/git/
title: "Git"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

**Git** est un outil de gestion de versions distribué. Il prend une série d'« instantanés » de votre projet, ce qui vous permet de revenir à tout moment à n'importe quelle version antérieure, de voir qui a modifié chaque ligne de code et quand, et de collaborer à plusieurs en toute sécurité. C'est l'infrastructure de base des [bonnes pratiques d'ingénierie](../engineering-practice/) et de la [reproductibilité](../reproducibility/).

## Intuition

Voyez Git comme le « système de sauvegarde d'un jeu vidéo » pour votre code :

- Chaque `commit` revient à **créer une sauvegarde** : il enregistre l'état de tous les fichiers à cet instant, accompagné d'une phrase expliquant « ce que j'ai changé ».
- Envie de tenter une modification audacieuse ? Ouvrez une `branch` (branche), l'équivalent d'une sauvegarde parallèle : si ça tourne mal, vous la jetez sans toucher à la ligne principale.
- Vous avez tout cassé ? `checkout` vous ramène à n'importe quelle sauvegarde précédente.
- En équipe, chacun travaille sur sa propre branche, puis on `merge` (fusionne) le tout — Git se charge d'assembler les modifications de chacun.

Comparé à la copie manuelle datée de `projet_final_v2_vraiment_final.zip`, Git rend l'historique **clair, traçable et sans perte**.

## Points essentiels

Git distingue trois zones clés :

- **Le répertoire de travail** : les fichiers que vous êtes en train de modifier.
- **La zone de préparation (staging)** : avec `git add`, vous choisissez les modifications à inclure dans le prochain commit.
- **Le dépôt (repo)** : avec `git commit`, vous les enregistrez définitivement.

Le cycle de commandes le plus courant :

```bash
git status                 # voir quels fichiers ont changé
git add .                  # placer les modifications dans la zone de préparation
git commit -m "Corrige le dépassement d'indice lors du découpage en fenêtres"   # sauvegarder avec un message
git log --oneline          # consulter l'historique
git push                   # pousser vers le dépôt distant (par exemple GitHub)
```

Branches et collaboration :

```bash
git branch feature-kun     # créer une branche
git checkout feature-kun   # basculer dessus (ou git switch)
git merge feature-kun      # la fusionner dans la branche principale
git pull                   # récupérer les dernières modifications des autres
```

## Un exemple

Un déroulé typique d'« essai-erreur » :

```bash
# Le code est sain sur la branche principale ; je veux essayer une nouvelle fonction de perte
git checkout -b try-new-loss      # créer la branche d'expérience et basculer dessus

# ... modifier le code, lancer les expériences ...
git add train.py
git commit -m "Expérience : passage à la perte de Huber"

# Résultat décevant : on abandonne toute la branche
git checkout main
git branch -D try-new-loss        # la branche principale est intacte

# Si le résultat est bon, on la fusionne
# git checkout main && git merge try-new-loss
```

`git diff` permet aussi de voir précisément quelles lignes ont changé :

```bash
git diff HEAD~1 train.py    # comparer avec le commit précédent
```

## Intérêt pour la prévision de séries temporelles

Dans une recherche comme **KUN / Kernel U-Net**, Git sert directement la crédibilité des résultats :

- **Expériences traçables** : chaque courbe d'expérience correspond à un commit. Six mois plus tard, pour reproduire un meilleur résultat, il suffit d'un `git checkout <le commit de l'époque>` pour retrouver le code exact à l'identique.
- **Comparaisons claires** : « le sous-échantillonnage apporte-t-il vraiment quelque chose ? » On fait de l'A/B avec des branches, et `git diff` montre tout d'un coup d'œil.
- **Collaborer sans se marcher dessus** : plusieurs personnes modifient des modules différents sans interférer, et même les conflits de fusion restent traçables.
- **Au service de la reproductibilité** : en consignant la version du code (le hash du commit) avec la configuration et la graine aléatoire, on obtient une preuve complète de [reproductibilité](../reproducibility/).

Conseil pratique : excluez avec `.gitignore` les gros jeux de données, les poids de modèles, `__pycache__`, etc. — **Git gère le code, pas des gigaoctets de données.**

## En résumé

- Git = gestion de versions + système de collaboration pour le code ; le geste central est `add` → `commit` → `push`.
- Trois zones : répertoire de travail / zone de préparation / dépôt ; les branches permettent d'expérimenter sans risque.
- Chaque commit doit dire clairement « ce qui a changé » : c'est ce qui donne de la valeur à l'historique.
- C'est le socle des [bonnes pratiques d'ingénierie](../engineering-practice/) et de la [reproductibilité](../reproducibility/) — **sans gestion de versions, pas d'expériences crédibles.**

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
