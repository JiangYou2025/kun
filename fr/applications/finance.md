---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 1 · Finance"
permalink: /fr/applications/finance/
title: "Finance et économie"
lead: "Les marchés sont le champ de bataille le plus séduisant et le plus impitoyable des séries temporelles : données massives, retour immédiat, argent bien réel — mais aussi un rapport signal sur bruit infime et des queues de distribution redoutables."
math: false
next: /applications/energy/
---

> Ceci est le scénario 1 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : cours et rendements des actions, taux de change, taux d'intérêt, cryptomonnaies, volumes échangés, volatilité, ainsi que des séries macroéconomiques comme le PIB, l'IPC ou le taux de chômage.
- **Tâches** : prévision de la direction ou de la valeur des rendements, **prévision de la volatilité**, mesure du risque (VaR / ES), trading de paires et cointégration, tenue de marché à haute fréquence, détection de fraudes et d'anomalies.

## Pourquoi c'est particulièrement difficile

- **Rapport signal sur bruit infime** : on est proche de l'« hypothèse d'efficience des marchés » — la part prévisible est minime, et un modèle prend très facilement le bruit pour du signal et surapprend.
- **Non-stationnarité et ruptures structurelles** : crises, politiques économiques et changements institutionnels peuvent invalider du jour au lendemain les régularités passées.
- **Queues épaisses et regroupement de la volatilité** : les mouvements extrêmes sont bien plus fréquents que ne le prédit la loi normale, et « les fortes fluctuations arrivent en grappes ».
- **Pièges du backtest** : biais d'anticipation, biais du survivant, surapprentissage de l'historique — brillant hors ligne, perdant en production.

## Méthodes courantes

- Les rendements eux-mêmes étant presque un bruit blanc, on concentre les efforts sur la **volatilité** : ARCH / GARCH (histoire [6](../../history/06/)).
- **Cointégration + modèle à correction d'erreur** : la base du trading de paires ([6](../../history/06/)).
- Références classiques : ARIMA (cours [8](../../course/08/)), lissage exponentiel ([12](../../course/12/)).
- Apprentissage automatique et apprentissage profond pour la prévision à partir de variables explicatives ([13](../../course/13/), [9](../../course/09/)), mais **le backtest doit impérativement respecter l'ordre chronologique** ([2](../../course/02/)), faute de quoi les fuites de données fabriquent des gains fictifs.

## Un cas emblématique : le regroupement de la volatilité

En 2003, Engle a reçu le prix Nobel d'économie pour le modèle ARCH. La direction des rendements est presque imprévisible, mais « si la volatilité est forte aujourd'hui, elle le sera probablement demain » est une régularité remarquablement robuste. C'est précisément en s'appuyant sur elle que **la gestion des risques et l'évaluation des options** sont devenues les applications les plus réussies des séries temporelles en finance — ce que l'on prévoit, ce n'est pas la hausse ou la baisse, mais l'incertitude elle-même.

---

**Termes clés (Key terms)** : rendement, volatilité, GARCH, VaR / ES, cointégration, hypothèse d'efficience des marchés, queues épaisses, biais de backtest.
