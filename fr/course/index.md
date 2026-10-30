---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/course/
title: "Introduction aux séries temporelles · Sommaire du cours"
lead: "Un cours d'introduction à l'analyse et à la prévision des séries temporelles, en 17 leçons. Cette page ne présente que la structure et les titres ; le contenu est complété leçon par leçon. La mise en forme s'inspire des notes de cours de tsamardzic/nlp_intro."
---

## Présentation du cours

Ce cours vous fait découvrir les **séries temporelles (time series)** en partant de zéro : ce qu'elles sont, comment les analyser, comment faire de la **prévision (forecasting)**, jusqu'aux modèles modernes d'apprentissage profond, dont le **Kernel U-Net (KUN)** de ce dépôt.

> Site associé (chinois / anglais / français) : [Séries temporelles](../time-series/) · [Comment prévoir](../forecasting/) · [Utiliser KUN](../kun/)
>
> Envie de connaître l'origine des méthodes ? Voir l'[histoire des séries temporelles](../history/).
>
> Besoin de consolider vos bases en mathématiques ou en apprentissage automatique ? Voir le [cours de fondamentaux](../foundations/), indépendant : mathématiques / informatique / apprentissage automatique / apprentissage profond.

## Sommaire

| # | Leçon | Thème |
|---|------|------|
| 1 | [Introduction : séries temporelles et tâches de prévision](01/) | Introduction |
| 2 | [Données : jeux de données et préparation des données](02/) | Data & preparation |
| 3 | [Modèles linéaires : ajustement et prévision](03/) | Linear models |
| 4 | [Visualisation : analyser les résultats et tracer des graphiques](04/) | Visualization & analysis |
| 5 | [Composantes et décomposition](05/) | Components & decomposition |
| 6 | [Stationnarité, différenciation et transformations](06/) | Stationarity & transforms |
| 7 | [Autocorrélation : ACF et PACF](07/) | Autocorrelation |
| 8 | [Modèles classiques : AR / MA / ARIMA / SARIMA](08/) | Classical models |
| 9 | [Modèles d'apprentissage profond : RNN / LSTM / GRU et TCN](09/) | Deep learning models |
| 10 | [Transformer et séries temporelles](10/) | Transformers |
| 11 | [Kernel U-Net](11/) | Kernel U-Net |
| 12 | [Données particulières et transformations : transformation log (données financières / sociales) et lissage exponentiel](12/) | Special data & transforms |
| 13 | [Tâches et choix du modèle : quel modèle pour quelle tâche](13/) | Tasks & model selection |
| 14 | [Prévision probabiliste](14/) | Probabilistic forecasting |
| 15 | [Prévision multivariée](15/) | Multivariate forecasting |
| 16 | [Systèmes dynamiques](16/) | Dynamical systems |
| 17 | [Flow matching et diffusion](17/) | Flow matching & diffusion |

## Thème complémentaire

- [**Types d'ondes et prévision**](wave-types/) — un canevas interactif pour découvrir six formes d'onde de base : tendance, cycle, amortissement, onde carrée, onde composite et bruit, ainsi que la difficulté de prévision de chacune. À lire avec les leçons 4 et 5.

## Études de cas pratiques

Les études de cas Jupyter exécutables qui accompagnent le cours (données synthétiques, prêtes à lancer après un simple clonage) se trouvent dans le dossier [`notebooks/`](https://github.com/JiangYou2025/kun/tree/main/notebooks) du dépôt :

1. [Exploration et décomposition](https://github.com/JiangYou2025/kun/blob/main/notebooks/01_explore_and_decompose.ipynb) — leçons 4 et 5
2. [Références de prévision et évaluation](https://github.com/JiangYou2025/kun/blob/main/notebooks/02_forecasting_baselines.ipynb) — leçons 3 et 4
3. [Prévision par réseau de neurones à fenêtre glissante (l'idée de KUN)](https://github.com/JiangYou2025/kun/blob/main/notebooks/03_kun_style_window_forecast.ipynb) — leçons 9 et 11

## Mode d'emploi

- Lisez dans l'ordre : chaque leçon s'appuie sur la précédente.
- Chaque leçon ne liste d'abord que **le titre et le plan des sections**, pour construire une carte d'ensemble avant de compléter les détails.
- La leçon 11 aboutit à **KUN** et renvoie au tutoriel pratique [Utiliser KUN](../kun/).
