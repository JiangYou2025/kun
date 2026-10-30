---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2015–16 · Informatique"
permalink: /fr/history/e/deep-rl/
title: "L'apprentissage par renforcement profond (DQN · AlphaGo, 2015–16)"
lead: "Quand les entrées perceptives sont de trop grande dimension pour concevoir des caractéristiques à la main, peut-on laisser un réseau profond approcher directement la valeur et la politique ? DQN et AlphaGo ont répondu par l'affirmative."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

L'apprentissage par renforcement (RL) étudie la **décision séquentielle** : à chaque instant, un agent observe un état, choisit une action et reçoit une récompense, avec pour objectif de maximiser le gain de long terme. C'est par nature un problème de séries temporelles — les actions influencent la distribution des états futurs, et les récompenses s'étendent sur de très longues durées. Le cadre classique est le **processus de décision markovien (MDP)**, associé à des méthodes de différences temporelles comme le **Q-learning** de Watkins (1989). Mais pendant des décennies, ces méthodes sont surtout restées cantonnées à des problèmes jouets à états de faible dimension et énumérables.

### Problème

Dans les tâches réelles, l'état est souvent une perception brute de grande dimension : une image de jeu compte des dizaines de milliers de pixels, et le go compte environ $$10^{170}$$ positions. Un Q-learning tabulaire ne peut ni stocker ni généraliser un espace d'états aussi immense, et concevoir des caractéristiques à la main est laborieux et fragile. **Peut-on laisser un approximateur de fonctions apprendre la fonction de valeur ou la politique directement à partir des entrées brutes ?** Les premières tentatives de RL avec des réseaux de neurones divergeaient souvent — la cible bouge, les données sont fortement corrélées, et l'entraînement est extrêmement instable.

### Autres courants de l'époque (et leurs limites)

- **Approximation linéaire + caractéristiques manuelles** : bonnes propriétés de convergence théorique, mais un pouvoir d'expression limité par les caractéristiques conçues à la main, qui gère mal les entrées au niveau du pixel.
- **Planification par modèle (recherche arborescente Monte-Carlo, MCTS)** : utilisée seule au go, elle manque d'une bonne évaluation des positions ; la profondeur de recherche est limitée et le niveau de jeu reste amateur.
- **Premières formes du gradient de politique** : forte variance, faible efficacité en échantillons, entraînement difficile à stabiliser sur des tâches perceptives de grande dimension.

### Méthode

**DQN** approche la valeur d'action $$Q(s,a;\theta)$$ avec un réseau convolutif et introduit deux techniques de stabilisation : le **rejeu d'expérience** (qui casse la corrélation entre échantillons) et le **réseau cible** (une copie figée des paramètres $$\theta^-$$ fournissant une cible stable). Il minimise l'erreur de différence temporelle :

$$ L(\theta)=\mathbb{E}\Big[\big(r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta)\big)^2\Big] $$

où $$\gamma$$ est le facteur d'actualisation et $$r+\gamma\max_{a'}Q(\cdot;\theta^-)$$ la cible de retour obtenue par amorçage (*bootstrapping*). **AlphaGo**, lui, intègre les réseaux profonds dans la recherche : un réseau de politique $$p(a\mid s)$$ réduit la largeur de la recherche, un réseau de valeur $$v(s)$$ en réduit la profondeur, et le MCTS combine les deux en maintenant pour chaque arête

$$ Q(s,a)+u(s,a),\qquad u(s,a)\propto \frac{P(s,a)}{1+N(s,a)} $$

ce qui équilibre exploitation ($$Q$$ élevé) et exploration (a priori $$P$$ élevé, nombre de visites $$N$$ faible).

### Résultats

Sur 49 jeux Atari, DQN atteint, voire dépasse, le niveau humain avec **un même réseau et un même jeu d'hyperparamètres**, à partir des seuls pixels de l'écran et du score. En 2016, AlphaGo bat Lee Sedol 4 à 1 : c'est le premier programme à vaincre un joueur professionnel de tout premier plan au go complet sur 19×19. L'année suivante, AlphaGo Zero va plus loin : par le seul jeu contre lui-même, sans parties humaines, il surpasse toutes les versions précédentes.

### Portée et perspectives

L'apprentissage par renforcement profond a montré que **les réseaux profonds peuvent servir d'approximateurs de valeur et de politique dans la décision séquentielle**, faisant passer le RL des tables de faible dimension à la perception brute de grande dimension. Il partage le même noyau que les séries temporelles — utiliser l'historique pour prévoir et optimiser l'avenir. Ce fil mène à l'optimisation de politique, aux modèles du monde, et au paradigme qui combine grands modèles ([modèles de fondation](../foundation-models/)) et alignement par RL. Quand on apprend à un agent à « décider en regardant l'écran », l'ossature reste ce pas : la différence temporelle du Q-learning plus l'approximation profonde.
