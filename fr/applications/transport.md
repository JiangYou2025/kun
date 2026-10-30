---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 4 · Transports"
permalink: /fr/applications/transport/
title: "Transports et mobilité"
lead: "La congestion d'une route se propage le long du réseau vers l'aval — dès le départ, la prévision du trafic n'est pas une affaire de courbe isolée, mais celle d'un graphe entier qui évolue dans le temps."
math: false
prev: /applications/retail/
next: /applications/health/
---

> Ceci est le scénario 4 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : vitesses et débits mesurés par les capteurs du réseau routier (boucles inductives, caméras), demande de déplacements, trajectoires de véhicules et de piétons, commandes de VTC.
- **Tâches** : prévision à court terme de l'état du trafic, estimation de l'heure d'arrivée (ETA), prédiction de trajectoires, prévision de la demande origine-destination (OD).

## Ce qui rend ce domaine particulier

- **Couplage spatio-temporel** : la congestion en amont se transmet à l'aval, et les tronçons voisins sont fortement corrélés — c'est par nature un problème de **structure de graphe**.
- **Forte périodicité + chocs ponctuels** : les rythmes de déplacement quotidiens et hebdomadaires sont stables, mais accidents, intempéries et grands événements les bouleversent soudainement.
- **Temps réel** : la navigation et la régulation exigent des mises à jour à la seconde.

## Méthodes courantes

- **Réseaux de neurones sur graphes spatio-temporels (STGNN)** : DCRNN, Graph WaveNet, etc., qui représentent le réseau routier comme un graphe et modélisent simultanément la topologie spatiale et l'évolution temporelle.
- Référence classique : un ARIMA saisonnier par tronçon (cours [8](../../course/08/)) comme point de comparaison.
- Prédiction de trajectoires : le plus souvent par modèles de séquences / Transformer ([10](../../course/10/)).
- Pour un panorama de la prévision spatio-temporelle, voir [Questions ouvertes en séries temporelles 2026 · Prévision spatio-temporelle](../../kun/).

## Un cas emblématique : l'ETA en navigation

Les applications cartographiques modernes représentent tout le réseau routier sous forme de graphe et utilisent des **réseaux de neurones sur graphes** pour combiner les conditions de circulation en temps réel et prédire l'heure d'arrivée (les travaux menés en 2020 par DeepMind et Google Maps ont nettement réduit l'erreur d'ETA). Les transports sont ainsi devenus l'un des terrains où la « prévision spatio-temporelle » est la plus mature — structure spatiale et dynamique temporelle doivent être modélisées ensemble, l'une ne va pas sans l'autre.

---

**Termes clés (Key terms)** : prévision spatio-temporelle, graphe du réseau routier, STGNN, DCRNN, ETA, prédiction de trajectoires, matrice OD.
