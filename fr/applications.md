---
updated: "2026-06-11"
layout: history
lang: fr
permalink: /fr/applications/
title: "Applications des séries temporelles"
lead: "Théories et modèles doivent finir par se confronter au terrain. Ce dossier procède domaine par domaine ; pour chaque scénario, il explique à quoi y ressemblent les séries temporelles, ce qu'il faut prévoir ou détecter, où se situent les difficultés et quelles méthodes on y emploie — avec, à chaque étape, des liens vers les chapitres correspondants du cours et de l'histoire."
---

> L'un des dossiers thématiques, aux côtés de l'[histoire](../history/), de la [préhistoire et des applications contemporaines](../prehistory/), de la [nature du temps](../nature-of-time/) et des [paradoxes du temps](../paradoxes/). À voir aussi : [cours d'introduction](../course/) · [Utiliser KUN](../kun/).

## Pourquoi une présentation par scénario

L'[histoire](../history/) raconte comment les méthodes ont évolué, le [cours](../course/) explique comment s'en servir ; cette page adopte un autre angle — **partir du domaine d'application**. Derrière la même formule, « prévoir la suite d'une série », la finance cherche le risque et les queues de distribution, l'électricité les pics et la planification de la production, la médecine l'alerte précoce, la météorologie des champs spatio-temporels. La forme des données, les critères d'évaluation et le coût acceptable d'une erreur diffèrent d'un domaine à l'autre, et le choix des modèles change en conséquence.

Au fil de cette lecture, vous verrez sans cesse le même ensemble de méthodes (ARIMA, lissage exponentiel, GBDT, LSTM, Transformer, modèles à espace d'états) retaillé pour chaque scénario — c'est précisément ainsi que l'on fait correspondre les outils aux problèmes.

## Dix scénarios

| # | Scénario | Tâches typiques | La difficulté en une phrase |
|---|------|---------|-----------|
| 1 | [Finance et économie](finance/) | Rendements, volatilité, risque | Rapport signal sur bruit infime, queues de distribution redoutables |
| 2 | [Énergie et électricité](energy/) | Prévision de charge, production renouvelable | Forte saisonnalité + couplage avec la météo + exigence de pilotabilité |
| 3 | [Commerce de détail et chaîne logistique](retail/) | Prévision de la demande, réapprovisionnement et prix | Multitude de séries intermittentes + promotions et jours fériés |
| 4 | [Transports et mobilité](transport/) | Trafic, ETA, trajectoires | Structure de réseau aux couplages spatio-temporels |
| 5 | [Santé et médecine](health/) | Signes vitaux, épidémies | Enjeux vitaux, échantillonnage irrégulier, besoin d'interprétabilité |
| 6 | [Météorologie et climat](weather/) | Prévision du temps, projections climatiques | Champs spatio-temporels de grande dimension, limite imposée par le chaos |
| 7 | [Industrie et IoT](industry/) | Maintenance prédictive, surveillance des procédés | Capteurs multiples + rareté des étiquettes de panne |
| 8 | [Télécommunications et signal](signal/) | Parole, canal, pistage radar | Fréquence d'échantillonnage élevée, temps réel strict, bruit |
| 9 | [Astronomie et géophysique](geophysics/) | Taches solaires, marées, séismes | Durées très longues, événements majeurs rares |
| 10 | [Langage naturel et séquences](language/) | Modèles de langage, modélisation de séquences | Symboles discrets, dépendances à très longue portée |

> Chaque scénario occupe une page ; nous vous conseillons de les lire dans l'ordre, mais vous pouvez aussi aller directement au domaine qui vous intéresse.
