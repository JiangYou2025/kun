---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1990 · Physique"
permalink: /fr/history/e/nonlinear-prediction/
title: "La prévision non linéaire pour distinguer le chaos (Sugihara · May, 1990)"
lead: "Une courbe d'apparence aléatoire relève-t-elle d'un chaos de faible dimension ou d'un pur bruit ? La réponse se cache dans « la vitesse à laquelle la prévision se dégrade avec le temps »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1980, la théorie du chaos a fait prendre conscience aux physiciens et aux écologues qu'un système non linéaire de faible dimension, parfaitement déterministe, peut produire des trajectoires sans aucune régularité apparente, ressemblant à s'y méprendre à du bruit. Le [théorème de plongement de Takens (1981)](../takens/) garantit en outre qu'on peut reconstruire la géométrie de l'espace des phases d'un système à partir des seules coordonnées retardées d'une variable unique. Une question séduisante surgit alors : les séquences irrégulières de la nature — fluctuations des effectifs d'espèces, épidémies, température de surface de la mer — sont-elles pilotées par un bruit aléatoire, ou s'agit-il d'un chaos déterministe de faible dimension déguisé ?

### Problème

Les outils traditionnels (spectre de puissance, autocorrélation) ne permettent pratiquement pas de distinguer « chaos de faible dimension » et « bruit aléatoire de grande dimension » : tous deux donnent un spectre large et continu. **Existe-t-il un critère opérationnel pour distinguer le chaos déterministe du bruit pur ?** L'intuition de Sugihara et May est que les deux diffèrent fondamentalement par leur « prévisibilité » : bien que sensible aux conditions initiales, le chaos reste prévisible à court terme, et la précision de la prévision **décroît systématiquement** avec l'horizon ; le bruit pur, lui, est imprévisible à tout horizon.

### Les autres courants de l'époque (et leurs limites)

- **L'estimation de la dimension / des exposants de Lyapunov (Grassberger–Procaccia, etc.)** : elle caractérise la complexité de l'attracteur, mais est très sensible à la quantité de données et au bruit ; sur des séquences réelles courtes et bruitées, elle donne souvent des résultats peu fiables, voire de fausses structures de faible dimension.
- **La modélisation stochastique linéaire (école ARMA)** : elle suppose par défaut que la séquence est engendrée par un système linéaire plus du bruit ; face à une véritable structure déterministe non linéaire, elle est systématiquement mal ajustée et ne peut répondre à la question « est-ce du chaos ? ».
- **L'analyse spectrale** : un spectre à large bande peut provenir aussi bien du chaos que du bruit ; elle n'a en soi aucun pouvoir discriminant.

### Méthode

Le cœur de la méthode est la **prévision locale (simplex) par plus proches voisins dans l'espace des phases**. On plonge d'abord la séquence dans un espace des phases de dimension $$E$$ par coordonnées retardées :

$$ \mathbf{x}_t=\big(x_t,\,x_{t-\tau},\,x_{t-2\tau},\,\dots,\,x_{t-(E-1)\tau}\big) $$

Pour prédire la valeur de $$\mathbf{x}_t$$ dans $$T_p$$ pas, on cherche dans la trajectoire passée ses quelques plus proches voisins, et l'on extrapole en pondérant ce que chacun de ces voisins est devenu $$T_p$$ pas plus tard :

$$ \hat{x}_{t+T_p}=\sum_{i}w_i\,x_{n_i+T_p},\qquad w_i\propto \exp\!\big(-\lVert \mathbf{x}_t-\mathbf{x}_{n_i}\rVert\big) $$

Le critère décisif est la **courbe de décroissance de la qualité de prévision en fonction de l'horizon $$T_p$$** : on mesure la précision par le coefficient de corrélation $$\rho(T_p)$$ entre valeurs prédites et valeurs réelles.

- Si la séquence est un **chaos de faible dimension** : $$\rho$$ est élevé aux petits horizons et **diminue continûment** quand $$T_p$$ augmente — c'est l'empreinte du déterminisme combiné à la sensibilité aux conditions initiales.
- Si la séquence est un **bruit pur (non corrélé)** : $$\rho(T_p)$$ est faible et à peu près plat à tous les horizons, sans décroissance du type « bon d'abord, mauvais ensuite ».

### Résultats

Appliquée à des données épidémiques comme la rougeole ou la grippe, ainsi qu'à des séries de température de surface de la mer, la méthode a permis d'établir que des fluctuations « d'apparence aléatoire » étaient le produit d'une dynamique non linéaire de faible dimension, et a fourni de meilleures prévisions à court terme que les modèles linéaires. Elle a transformé la théorie abstraite du chaos en un outil directement applicable à des séquences réelles, finies et bruitées.

### Portée et perspectives

Cette idée — « distinguer chaos et bruit par la décroissance de la prévision » — a véritablement relié la géométrie des systèmes dynamiques à la prévision des séries temporelles. Elle a directement donné naissance au **convergent cross mapping (CCM)** de Sugihara et ses collègues, une méthode non linéaire de détection de la causalité qui infère le sens causal entre variables à partir des séries observées. Des plus proches voisins dans l'espace des phases à la modélisation dynamique empirique (EDM), ce fil reste aujourd'hui un paradigme actif en écologie et en neurosciences pour traiter la causalité non linéaire et la prévisibilité.
