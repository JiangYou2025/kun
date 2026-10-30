---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 3 · Distribution et logistique"
permalink: /fr/applications/retail/
title: "Commerce de détail et chaîne logistique"
lead: "Des millions de SKU, une courbe par magasin et par jour — la difficulté de la prévision dans la distribution ne tient pas à la complexité d'une série isolée, mais à leur nombre gigantesque, à leur caractère clairsemé et intermittent, et aux perturbations répétées des promotions et des jours fériés."
math: false
prev: /applications/energy/
next: /applications/transport/
---

> Ceci est le scénario 3 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : ventes journalières ou hebdomadaires par SKU × magasin, prix, indicateurs de promotion, stocks, météo et calendrier des jours fériés.
- **Tâches** : prévision de la demande, réapprovisionnement et stock de sécurité, tarification dynamique, démarrage à froid des nouveaux produits.

## Ce qui rend ce domaine particulier

- **Des séries en masse** : des millions de combinaisons SKU × magasin ; modéliser chaque série séparément est irréaliste, il faut un **modèle global** (un seul modèle pour toutes les séries).
- **Demande intermittente** : beaucoup de séries sont truffées de zéros (nombre d'articles ne se vendent tout simplement pas certains jours), ce qui met en échec les modèles ordinaires.
- **Fortes perturbations exogènes** : promotions, baisses de prix, jours fériés et élasticité-prix expliquent souvent mieux les ventes que la tendance historique.
- **Une évaluation orientée métier** : ce qui compte, ce sont le taux de rupture, la rotation des stocks et la perte par quantiles pondérée, plutôt que la seule MAE.

## Méthodes courantes

- Méthodes dédiées à la demande intermittente : **Croston / SBA**.
- Modèle probabiliste profond global **DeepAR** (histoire [9](../../history/09/)), qui apprend d'un coup les points communs de dizaines de millions de séries.
- GBDT + riches variables de calendrier et de promotion (cours [13](../../course/13/)).
- La **prévision par quantiles** sert directement aux décisions de stock de sécurité ([14](../../course/14/)).

## Un cas emblématique : la compétition M5

La compétition M5 de 2020 (ventes hiérarchiques de Walmart) a pratiquement défini le paradigme actuel de la prévision dans la distribution : la solution gagnante reposait sur **LightGBM + une ingénierie de variables poussée**, tandis que la piste probabiliste était dominée par les réseaux de neurones globaux. Elle a aussi mis sur le devant de la scène l'« **évaluation par quantiles** » — car une décision de réapprovisionnement requiert, par nature, un certain quantile de la distribution, et non sa moyenne.

---

**Termes clés (Key terms)** : demande intermittente, Croston, modèle global, DeepAR, variables de promotion / calendrier, perte par quantiles, stock de sécurité.
