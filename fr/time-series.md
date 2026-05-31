---
lang: fr
ref: time-series
permalink: /fr/time-series/
title: "Qu'est-ce qu'une série temporelle ?"
lead: "Avant de prévoir, il faut comprendre ce que l'on observe. Cette page présente le vocabulaire essentiel et la structure cachée dans presque toute série temporelle."
next: forecasting
math: true
---

## La définition en une phrase

Une **série temporelle** est une suite d'observations enregistrées dans l'ordre du temps, généralement à intervalles réguliers :

$$ x_1, x_2, x_3, \dots, x_T $$

Chaque $x_t$ est la valeur mesurée au pas de temps $t$. Ce qui rend une série temporelle particulière — et plus difficile que des données tabulaires ordinaires — c'est que **l'ordre compte** : hier influence aujourd'hui ; on ne peut pas mélanger les lignes.

Les exemples sont partout : température quotidienne, demande horaire d'électricité, cours de clôture d'une action, nombre de patients arrivant à l'hôpital, utilisation du CPU d'un serveur.

## Univariée vs. multivariée

- **Univariée** — une seule variable dans le temps (un capteur, les ventes d'un produit).
- **Multivariée** — plusieurs variables enregistrées ensemble, souvent corrélées (température *et* humidité *et* charge électrique). KUN est conçu pour le cas multivarié.

## Les quatre composantes

La plupart des séries se décomposent en quelques éléments récurrents. Les comprendre indique ce qu'un modèle doit capturer.

| Composante | Description | Exemple |
|---|---|---|
| **Tendance** | Direction à long terme (hausse/baisse) | Une population urbaine qui croît chaque année |
| **Saisonnalité** | Un motif qui se répète sur une période fixe | Plus de ventes de glaces chaque été |
| **Cyclique** | Se répète, mais sans période fixe | Les cycles économiques d'expansion–récession |
| **Bruit / résidu** | La part irrégulière et imprévisible | Une erreur de mesure aléatoire |

Une écriture classique est la **décomposition additive** :

$$ x_t = \text{Tendance}_t + \text{Saisonnalité}_t + \text{Résidu}_t $$

> **Intuition :** prévoir, c'est l'art de bien modéliser la tendance et la saisonnalité, et de *ne pas* essayer de prédire le bruit.

## La stationnarité — la propriété que les modèles adorent

Une série est **stationnaire** si ses propriétés statistiques (moyenne, variance, autocorrélation) ne changent pas dans le temps. Beaucoup de méthodes classiques supposent la stationnarité, car un processus dont les règles bougent sans cesse est presque impossible à extrapoler.

Les données réelles sont généralement **non stationnaires** (tendance, variance changeante). Deux remèdes courants :

- **Différenciation** — modéliser la variation $x_t - x_{t-1}$ plutôt que la valeur brute, ce qui supprime une tendance.
- **Transformations** — par exemple le logarithme pour stabiliser une variance croissante.

Les modèles profonds modernes comme KUN tolèrent mieux la non-stationnarité, mais normaliser les données aide toujours beaucoup.

## L'autocorrélation — le passé prédit l'avenir

Si la prévision est possible, c'est grâce à l'**autocorrélation** : une valeur est corrélée à ses propres valeurs passées. L'**autocorrélation au décalage $k$** mesure à quel point la série ressemble à une copie d'elle-même décalée de $k$ pas. Une forte autocorrélation au décalage 24 sur des données horaires, par exemple, crie « saisonnalité quotidienne ».

## Comment poser le problème pour un modèle

Étant donné une **fenêtre de rétrospection** (aussi appelée *contexte* ou *longueur d'entrée*) des $L$ dernières observations, on veut prédire les $H$ valeurs suivantes (l'**horizon**) :

$$ \underbrace{(x_{t-L+1}, \dots, x_t)}_{\text{entrée}} \;\longrightarrow\; \underbrace{(x_{t+1}, \dots, x_{t+H})}_{\text{prévision}} $$

Ce cadrage par fenêtre glissante transforme une série brute en de nombreux exemples d'entraînement (entrée → cible) — exactement le format attendu par KUN.

## Quelques pièges pratiques

- **Valeurs manquantes et horodatages irréguliers** — combler, interpoler ou rééchantillonner avant l'entraînement.
- **Fuite de données** — ne jamais laisser une information du futur s'infiltrer dans l'entrée (un bug très courant). Toujours découper selon le temps, jamais aléatoirement.
- **Valeurs aberrantes et changements de régime** — un jour férié, une panne de capteur ou une pandémie peuvent briser les motifs appris.

Muni de ce vocabulaire, vous êtes prêt pour la question suivante : *comment produire concrètement une prévision ?*
