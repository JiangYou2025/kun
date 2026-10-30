---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 10 · Modélisation de séquences"
permalink: /fr/applications/language/
title: "Langage naturel et séquences"
lead: "Textes, musique, code, ADN : autant de séquences de symboles ordonnés — proches cousines des séries temporelles. Cette parenté explique pourquoi les deux domaines n'ont cessé de s'emprunter leurs modèles."
math: false
prev: /applications/geophysics/
---

> Ceci est le scénario 10, le dernier, du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : textes, transcriptions de la parole, musique, code source, séquences d'ADN / de protéines.
- **Tâches** : modélisation du langage (prédire le token suivant), étiquetage de séquences, traduction automatique, génération de séquences.

## Points communs et différences avec les séries temporelles numériques

- **Points communs** : il s'agit fondamentalement de séquences ordonnées, et le cœur du problème est toujours de « prédire l'avenir à partir du passé ».
- **Différences** : les symboles sont **discrets** (et non des valeurs numériques continues), les dépendances peuvent porter sur de très longues distances, et il n'y a pas d'intervalle d'échantillonnage fixe.

## Généalogie des méthodes (très proche de celle des séries temporelles)

- RNN / LSTM (cours [9](../../course/09/), histoire [7](../../history/07/)).
- **Transformer / auto-attention** (cours [10](../../course/10/), histoire [9](../../history/09/)) — la même architecture irrigue aujourd'hui en retour les séries temporelles numériques, donnant naissance à PatchTST et iTransformer.
- C'est grâce à cette perméabilité que Chronos peut **discrétiser les valeurs en tokens** et réutiliser directement l'architecture des modèles de langage pour la prévision (cours [10](../../course/10/)).

## Un cas emblématique : le transfert d'architectures dans les deux sens

Le LSTM et le Transformer, inventés pour le TALN, ont été largement adoptés par les séries temporelles ; à l'inverse, les modèles de fondation pour séries temporelles (comme Chronos) empruntent le paradigme des modèles de langage. Les deux domaines partagent le même tronc de « modélisation de séquences » — et c'est précisément pour cela que ce cours place le langage à côté des séries temporelles : **la séquence vient d'abord, la série temporelle ensuite**.

> Arrivé ici, vous avez parcouru l'ensemble des [dix scénarios](../). Revenez au [sommaire des applications](../), ou poursuivez avec le [cours d'introduction](../../course/) et l'[histoire](../../history/).

---

**Termes clés (Key terms)** : modèle de langage, token, auto-attention, étiquetage de séquences, Chronos, modélisation de séquences.
