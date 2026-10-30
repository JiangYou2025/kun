---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 7 · Industrie et IoT"
permalink: /fr/applications/industry/
title: "Industrie et Internet des objets"
lead: "Avant de tomber en panne, une machine laisse souvent des indices dans ses capteurs. L'objectif des séries temporelles industrielles est d'entendre, au milieu de montagnes de signaux de vibration, de température et de courant, les pas de la panne qui approche."
math: false
prev: /applications/weather/
next: /applications/signal/
---

> Ceci est le scénario 7 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : flux multicapteurs des équipements (vibration / température / courant / pression), enregistrements SCADA, données de contrôle qualité.
- **Tâches** : maintenance prédictive et durée de vie résiduelle (RUL), détection d'anomalies et de pannes, maîtrise statistique des procédés (MSP), capteurs logiciels.

## Ce qui rend ce domaine particulier

- **Multivarié et haute fréquence** : des dizaines, voire des centaines de capteurs échantillonnés simultanément, avec dérive des capteurs et bruit.
- **Rareté des étiquettes de panne** : les équipements tombent rarement en panne, les exemples positifs sont très peu nombreux, et la plupart des tâches doivent passer par la **détection d'anomalies non supervisée**.
- **Temps réel en périphérie** : il faut souvent exécuter les modèles sur l'équipement lui-même, avec une faible latence.

## Méthodes courantes

- Les cartes de contrôle de la **maîtrise statistique des procédés (MSP)** comme référence la plus simple.
- Modèles à espace d'états / filtre de Kalman pour le lissage et la surveillance en ligne (histoire [4](../../history/04/)).
- Anomalies non supervisées : une alerte se déclenche dès que l'**erreur de reconstruction** d'un autoencodeur ou le **résidu** d'un modèle de prévision dépasse un seuil.
- La prévision de la RUL fait régresser les séries multicapteurs vers la durée de vie résiduelle, souvent avec des LSTM / TCN (cours [9](../../course/09/)).

## Un cas emblématique : la durée de vie résiduelle (RUL)

Le jeu de données C-MAPSS de la NASA, sur des turboréacteurs à double flux, est la référence standard de la maintenance prédictive : en entrée, des séries multicapteurs de dégradation ; en sortie, « combien de cycles reste-t-il ». Il réunit les deux grandes difficultés du contexte industriel — modéliser une dégradation multivariée, et fournir malgré tout des prévisions fiables alors que les exemples de pannes sont rares.

---

**Termes clés (Key terms)** : maintenance prédictive, durée de vie résiduelle (RUL), détection d'anomalies, cartes de contrôle MSP, capteur logiciel, dérive des capteurs.
