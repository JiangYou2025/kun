---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 2 · Énergie"
permalink: /fr/applications/energy/
title: "Énergie et électricité"
lead: "L'électricité ne se stocke pas à grande échelle, et l'offre doit égaler la demande en temps réel — ce qui fait de la prévision de la charge électrique l'une des tâches de séries temporelles aux conséquences les plus directes : une petite erreur, et l'on gaspille du combustible ou l'on doit procéder à des délestages."
math: false
prev: /applications/finance/
next: /applications/retail/
---

> Ceci est le scénario 2 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : charge électrique par région ou par bâtiment, production éolienne et photovoltaïque, prix de l'électricité, consommation de gaz, et variables météorologiques comme la température et l'irradiance.
- **Tâches** : prévision de charge à court terme (STLF), prévision de la production renouvelable, prévision des prix de l'électricité, effacement de la demande et optimisation de la répartition de la production.

## Ce qui rend ce domaine particulier

- **Saisonnalités multiples** : trois cycles superposés — journalier (pointes du matin et du soir), hebdomadaire (jours ouvrés / week-end) et annuel (saisons chaude et froide).
- **Fort couplage avec la météo** : la température pilote la charge de climatisation et de chauffage, le vent et l'irradiance pilotent la production renouvelable ; la météo est la première variable exogène.
- **Des conséquences bien concrètes** : les prévisions déterminent directement l'engagement des centrales ; les erreurs ont un coût financier et physique réel, et l'équilibre entre offre et demande doit être assuré à chaque instant.
- **La prévision probabiliste est indispensable** : pour décider du volume de réserve tournante, le réseau a besoin d'une « distribution de la production », et pas seulement d'une valeur ponctuelle.

## Méthodes courantes

- Références à saisonnalités multiples + **Holt-Winters / ETS à saisonnalités multiples** (cours [12](../../course/12/)).
- Régression ou GBDT intégrant des variables météorologiques exogènes ([13](../../course/13/)).
- Apprentissage profond pour les longues séries et les données multivariées, avec sortie directe de prévisions probabilistes ([9](../../course/09/), [14](../../course/14/)).

## Un cas emblématique : la prévision probabiliste de la production renouvelable

La production éolienne et solaire fluctue fortement avec la météo ; ce dont le gestionnaire de réseau a besoin, ce n'est pas « demain à 18 h, production = 42 MW », mais « quelle est la probabilité de passer sous 30 MW ? ». La **prévision par quantiles / probabiliste** ([14](../../course/14/)) est ainsi devenue la norme pour l'intégration au réseau — c'est en quantifiant l'incertitude que l'on peut dimensionner raisonnablement la capacité de réserve.

---

**Termes clés (Key terms)** : prévision de charge (STLF), saisonnalités multiples, variable exogène, prévision probabiliste / par quantiles, effacement de la demande, production renouvelable.
