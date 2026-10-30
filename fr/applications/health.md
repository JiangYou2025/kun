---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 5 · Santé"
permalink: /fr/applications/health/
title: "Santé et physiologie"
lead: "Battements cardiaques, ondes cérébrales, glycémie, courbes épidémiques — en médecine, chaque prévision peut être une question de vie ou de mort ; les exigences d'interprétabilité, de calibration et d'« anticipation » y sont donc plus sévères qu'ailleurs."
math: false
prev: /applications/transport/
next: /applications/weather/
---

> Ceci est le scénario 5 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : signes vitaux en réanimation (fréquence cardiaque / pression artérielle / saturation en oxygène), ECG / EEG, objets connectés portables, dossiers médicaux électroniques (DME), courbes épidémiques.
- **Tâches** : alerte précoce (par exemple pour le sepsis), détection et classification des arythmies, prévision de la glycémie, prévision de la propagation des épidémies.

## Ce qui rend ce domaine particulier

- **Enjeux vitaux** : les fausses alertes engendrent une lassitude face aux alarmes, les alertes manquées peuvent être fatales ; les prévisions doivent être **interprétables et calibrées**.
- **Irrégularités et données manquantes** : examens à des moments variables, appareils qui décrochent, intervalles d'échantillonnage inégaux et modalités hétérogènes.
- **Déséquilibre extrême** : les événements véritablement critiques sont rares, et les exemples positifs et négatifs sont en proportions très inégales.

## Méthodes courantes

- Détection et classification par modèles de séquences : LSTM / TCN (cours [9](../../course/09/)), Transformer ([10](../../course/10/)).
- Temps irrégulier : attention tenant compte des intervalles de temps, modèles en temps continu de type Neural ODE.
- Épidémies : **hybridation** de modèles mécanistes (SIR / SEIR) et de modèles guidés par les données, pour concilier interprétabilité et qualité d'ajustement.
- Produire des **intervalles probabilistes** plutôt qu'une valeur ponctuelle, afin de faciliter l'arbitrage clinique ([14](../../course/14/)).

## Un cas emblématique : l'alerte précoce du sepsis

Prédire, plusieurs heures à l'avance et à partir des signes vitaux en continu, la survenue d'un sepsis est une tâche emblématique des séries temporelles cliniques (par exemple le challenge PhysioNet / CinC 2019). Elle réunit « classification + alerte » et « fort déséquilibre + exigence élevée d'interprétabilité » — chaque heure gagnée influe directement sur le taux de survie.

---

**Termes clés (Key terms)** : alerte précoce, échantillonnage irrégulier, déséquilibre des classes, ECG / EEG, SIR / SEIR, calibration probabiliste.
