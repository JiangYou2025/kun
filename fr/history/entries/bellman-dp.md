---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1957 · Contrôle / communications"
permalink: /fr/history/e/bellman-dp/
title: "Programmation dynamique et équation de Bellman (Bellman, 1957)"
lead: "Dans une décision en plusieurs étapes, le nombre de chemins possibles explose : comment calculer ? La réponse de Bellman : tout segment d'un chemin optimal est lui-même optimal — et un problème gigantesque se découpe alors en une suite de petits problèmes."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1950, Richard Bellman étudie à la RAND Corporation les décisions en plusieurs étapes — interception de missiles, ordonnancement des stocks, allocation de ressources : autant de problèmes séquentiels où « le choix fait maintenant modifie la situation future, dans laquelle il faudra encore décider ». Il systématise cette méthode dans sa monographie *Dynamic Programming* (1957) ; le nom « dynamic programming » a été choisi, selon ses propres souvenirs, en partie pour paraître inoffensif lors des examens budgétaires de l'armée.

### Problème

La difficulté de la décision séquentielle est l'**explosion combinatoire** : si chaque étape offre plusieurs options et qu'il y a $$T$$ étapes, le nombre de chemins de stratégie possibles croît exponentiellement avec $$T$$, et les énumérer un à un est impossible. De plus, les étapes sont couplées — le choix présent change les états atteignables ensuite, si bien qu'on ne peut pas procéder de façon gloutonne, étape par étape, isolément. **Comment obtenir la solution optimale d'une séquence entière de décisions sans énumérer tous les chemins ?**

### Autres courants de l'époque (et leurs limites)

- **Énumération exhaustive / recherche par force brute** : garantit l'optimum, mais le nombre de chemins explose exponentiellement et devient incalculable dès que la taille augmente un peu.
- **Optimisation statique (calcul des variations, programmation linéaire résolue d'un bloc)** : excellente pour l'optimisation sous contraintes en une fois, mais peine à exprimer naturellement la structure de rétroaction multi-étapes où « l'état évolue avec les décisions, puis l'on décide à nouveau ».
- **Glouton pas à pas (myope)** : ne vise à chaque étape que l'optimum immédiat, ignore l'effet sur l'avenir et tombe souvent dans un sous-optimum global.

### Méthode

Le cœur de l'approche de Bellman est le **principe d'optimalité** : une stratégie optimale a la propriété que, quels que soient l'état initial et la première décision, les décisions restantes doivent elles aussi être optimales vis-à-vis du nouvel état produit par la première. On découpe ainsi récursivement « l'optimum de long terme » en « l'étape présente + l'optimum du sous-problème restant ». Pour un **processus de décision markovien (MDP)** à horizon infini actualisé, la fonction de valeur optimale $$V(s)$$ satisfait l'**équation d'optimalité de Bellman** :

$$ V(s) = \max_{a}\Big[\, r(s,a) + \gamma \sum_{s'} P(s'\mid s,a)\,V(s') \,\Big] $$

où $$s$$ est l'état, $$a$$ l'action, $$r(s,a)$$ la récompense immédiate, $$P(s'\mid s,a)$$ la probabilité de transition d'état et $$\gamma\in[0,1)$$ le facteur d'actualisation. $$V(s)$$ est la récompense cumulée espérée que l'on peut obtenir en partant de l'état $$s$$ et en suivant la stratégie optimale. Cette équation transforme l'optimisation globale en un **problème de point fixe**, résoluble par itération sur les valeurs ou itération sur les politiques — avec un coût de calcul qui croît avec le nombre d'états (et non de chemins).

### Résultats

La programmation dynamique est aussitôt devenue un outil universel de la recherche opérationnelle, de l'automatique et de l'économie : plus courts chemins, sac à dos, stocks, commande optimale, allocation de ressources, tout y passe. Elle forme avec la **commande optimale** de la même époque (dont l'équivalent en temps continu est l'équation aux dérivées partielles de Hamilton–Jacobi–Bellman) les deux faces d'une même médaille, et fournit un langage mathématique unifié pour la décision séquentielle avec état.

### Portée et perspectives

L'équation de Bellman est le socle théorique de l'**apprentissage par renforcement** : Q-learning, différences temporelles, et jusqu'aux réseaux de valeur de l'apprentissage par renforcement profond, tous cherchent à résoudre ou approcher cette équation par échantillonnage et approximation de fonctions. Elle partage une même origine, complémentaire, avec les [bandits manchots de Robbins](../robbins-bandit/) (le cas particulier sans état) et avec la vision en espace d'états du [filtre de Kalman](../kalman/) — l'une s'occupe de « décider de façon optimale », l'autre d'« estimer de façon optimale ». Lorsqu'un agent moderne planifie sa récompense de long terme dans un environnement incertain, c'est toujours ce découpage récursif de Bellman qu'il opère.
