---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 6 · Météo et climat"
permalink: /fr/applications/weather/
title: "Météorologie et climat"
lead: "La prévision météorologique est le plus ancien et le plus vaste chantier d'ingénierie des séries temporelles de l'humanité : il faut prévoir l'avenir sur tout un champ spatio-temporel de grande dimension, tout en acceptant la limite stricte imposée par le chaos."
math: false
prev: /applications/health/
next: /applications/industry/
---

> Ceci est le scénario 6 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : champs maillés en trois dimensions de température / pression / humidité / vent, observations satellitaires et radar, jeux de données de réanalyse.
- **Tâches** : prévision numérique du temps, prévision immédiate (nowcasting), prévision saisonnière, projections climatiques, alerte aux événements extrêmes.

## Ce qui rend ce domaine particulier

- **Champs spatio-temporels de grande dimension** : l'objet de la prévision n'est pas une courbe, mais l'évolution dans le temps de toute une grille couvrant la Terre, de dimension gigantesque et contrainte par les lois de la physique.
- **Limite de prévisibilité due au chaos** : Lorenz l'a montré depuis longtemps, l'atmosphère est extrêmement sensible aux conditions initiales, et au-delà d'environ deux semaines la prévision déterministe perd l'essentiel de sa valeur.
- **Assimilation de données** : il faut intégrer en continu d'énormes volumes d'observations en temps réel dans l'état du modèle pour contenir la croissance des erreurs.

## Méthodes courantes

- L'outil traditionnel est la **prévision numérique du temps (PNT)** : résoudre sur supercalculateur les équations aux dérivées partielles du mouvement atmosphérique, avec un filtre de Kalman d'ensemble (EnKF) pour l'assimilation de données (voir le [prologue](../../history/foundations/) de l'histoire).
- La nouvelle vague guidée par les données : FourCastNet, GraphCast, les opérateurs neuronaux de Fourier (FNO), etc., apprennent directement par apprentissage profond l'application d'un champ à un autre, avec des gains de vitesse de plusieurs ordres de grandeur ([prologue](../../history/foundations/), [Frontières 2026 · Spatio-temporel (page KUN)](../../kun/)).

## Un cas emblématique : GraphCast

En 2023, GraphCast de DeepMind a utilisé un réseau de neurones sur graphes pour la prévision météorologique mondiale à moyen terme, surpassant les modèles numériques traditionnels sur la plupart des indicateurs, avec une inférence de l'ordre de la minute (là où un modèle traditionnel tourne des heures sur un supercalculateur). C'est une étape marquante de la prévision météorologique guidée par les données — mais elle reste soumise à la même limite chaotique : aussi rapide soit-elle, elle ne peut produire de prévision déterministe au-delà de deux semaines.

---

**Termes clés (Key terms)** : prévision numérique du temps (PNT), assimilation de données, EnKF, chaos / limite de prévisibilité, opérateur neuronal (FNO), GraphCast.
