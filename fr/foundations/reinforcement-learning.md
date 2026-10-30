---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/reinforcement-learning/
title: "Apprentissage par renforcement"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

L'**apprentissage par renforcement** (*Reinforcement Learning*, RL) est le troisième grand paradigme de l'[apprentissage automatique](../ml/) : un **agent** interagit en permanence avec un **environnement** et ajuste son comportement en fonction des **récompenses** (*reward*) qu'il reçoit, dans le but d'apprendre une **politique** (*policy*) qui **maximise la récompense cumulée à long terme**.

## Intuition

Imaginez que vous **dressez un chiot**. Vous ne lui donnez pas de mode d'emploi ; au lieu de cela, quand il fait le bon geste (s'asseoir), il reçoit une friandise, et quand il se trompe, il n'a rien. Avec le temps, le chiot « comprend » de lui-même que « s'asseoir → friandise », et s'assoit de plus en plus volontiers.

L'apprentissage par renforcement, c'est exactement cet **apprentissage par essais et erreurs** (*trial and error*) :

- personne ne dit à l'agent « quelle est la bonne réponse » (c'est la différence fondamentale avec l'apprentissage supervisé) ;
- il ne peut avancer qu'à tâtons, en **essayant des actions, en observant leurs conséquences et en collectant des récompenses** ;
- et la récompense est souvent **différée** : on ne voit pas à cette étape si le choix était bon ou mauvais, il faut attendre plusieurs étapes pour le savoir.

C'est précisément ce qui rend l'apprentissage par renforcement à la fois fascinant et difficile : il doit extraire, d'un **retour d'information différé et rare**, la sagesse d'une longue suite de décisions.

## Principe : le cadre de l'apprentissage par renforcement

L'apprentissage par renforcement modélise le problème comme une boucle entre l'agent et l'environnement :

1. l'agent observe l'**état** (*state*) courant $s$ ;
2. il choisit une **action** $a$ selon sa **politique** (*policy*) $\pi(a\mid s)$ ;
3. l'environnement renvoie une **récompense** (*reward*) $r$ et un nouvel état $s'$ ;
4. on revient à l'étape 1, et ainsi de suite.

$$ s_0 \xrightarrow{a_0} (r_1, s_1) \xrightarrow{a_1} (r_2, s_2) \xrightarrow{a_2} \cdots $$

Le **but** n'est pas de maximiser le $r$ immédiat, mais la **récompense cumulée actualisée** à partir de maintenant, appelée **retour** (*return*) :

$$ G_t = \sum_{k\ge 0} \gamma^k\, r_{t+k} = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots $$

Ici $\gamma\in[0,1]$ est le **facteur d'actualisation** (*discount factor*) : plus $\gamma$ est proche de 1, plus l'agent est « prévoyant » et accorde de l'importance à l'avenir ; plus il est proche de 0, plus l'agent est « myope » et ne s'intéresse qu'à l'immédiat.

Pour mesurer « à quel point il est bon de se trouver dans un état donné », on introduit la **fonction de valeur** (*value function*) :

$$ V^\pi(s) = \mathbb{E}_\pi[\,G_t \mid s_t = s\,] $$

Elle indique le retour moyen obtenu en partant de l'état $s$ et en agissant selon la politique $\pi$. Plus fine encore, la **fonction de valeur d'action** $Q^\pi(s,a)$ donne le retour espéré lorsqu'on « effectue d'abord l'action $a$ dans l'état $s$, puis qu'on suit $\pi$ ». Au cœur de nombreux [algorithmes](../algorithms/), il s'agit d'**estimer $Q$, puis de choisir à chaque étape l'action dont le $Q$ est maximal**.

Tout ce cadre mathématique porte un nom : le **processus de décision markovien** (*Markov Decision Process*, MDP) — « markovien » signifiant que « l'avenir ne dépend que de l'état présent, et non de la manière dont on y est arrivé ».

## Un exemple concret : sortir d'un labyrinthe

Imaginons un robot qui cherche la sortie d'un labyrinthe :

- **État** $s$ : la case où se trouve actuellement le robot ;
- **Action** $a$ : haut, bas, gauche, droite ;
- **Récompense** $r$ : $-1$ s'il heurte un mur, $-0.1$ pour chaque pas (pour encourager les raccourcis), $+10$ en atteignant la sortie ;
- **Politique** $\pi$ : la direction à prendre dans chaque case.

Au début, le robot se cogne au hasard ; mais dès qu'il a atteint une fois la sortie et touché le $+10$, ce « bénéfice » se **propage case par case vers l'arrière** à travers la fonction de valeur, si bien que les cases proches de la sortie acquièrent peu à peu une valeur élevée. Après de nombreux épisodes, le robot a appris un itinéraire presque optimal. C'est ce que font des algorithmes comme le **Q-learning**.

## Exploration et exploitation

L'apprentissage par renforcement se heurte à un dilemme incontournable, le **compromis exploration–exploitation** (*exploration vs exploitation*) :

- **Exploitation** : choisir l'action actuellement connue comme la meilleure, pour empocher une récompense sûre ;
- **Exploration** : essayer des actions encore jamais tentées, qui permettront peut-être de découvrir un meilleur chemin.

Exploiter sans explorer, c'est risquer de rester coincé dans une solution sous-optimale ; explorer sans exploiter, c'est ne jamais apprendre de politique stable. Une approche courante est l'**ε-glouton** (*ε-greedy*) : explorer au hasard avec une petite probabilité $\varepsilon$, et exploiter la meilleure action le reste du temps.

## Comparaison avec les autres paradigmes

L'apprentissage par renforcement diffère profondément des deux paradigmes que vous avez déjà vus :

- Par rapport à l'[apprentissage supervisé](../supervised-learning/) : l'apprentissage supervisé dispose d'**étiquettes** toutes prêtes (chaque entrée a sa réponse de référence) ; le RL **n'a pas d'étiquettes**, seulement des **récompenses différées**, et ses propres actions influencent en outre les données qu'il verra ensuite.
- Par rapport à l'[apprentissage non supervisé](../unsupervised-learning/) : l'apprentissage non supervisé cherche des **structures** dans des données sans étiquettes ([partitionnement](../clustering/), réduction de dimension), tandis que le RL apprend **comment agir**, guidé par un **signal de récompense**.

Algorithmes et jalons courants : le **Q-learning** tabulaire, le **gradient de politique** (*policy gradient*) qui optimise directement la politique, **DQN** qui approxime $Q$ par un [réseau de neurones](../neural-network/), et **AlphaGo**, qui a battu des champions humains de go — tous sont issus des idées de l'apprentissage par renforcement.

## Intérêt pour la prévision de séries temporelles

Il faut le dire franchement : **pour la tâche consistant « simplement à prédire des valeurs futures », l'apprentissage par renforcement est peu utilisé** — la prévision relève par nature de l'**apprentissage supervisé** (les données historiques servent d'entrée, les valeurs futures réelles d'étiquettes).

L'apprentissage par renforcement entre vraiment en scène dans les problèmes en aval où il s'agit de **prendre une suite de décisions fondées sur des prévisions**, problèmes qui ont naturellement la structure « les actions influencent l'avenir, les récompenses arrivent en différé » :

- **Trading / gestion de portefeuille** : décider des achats, des ventes et des positions à partir de prévisions de marché ; le gain ou la perte constitue la récompense ;
- **Stocks / réapprovisionnement** : après avoir prévu la demande, décider de la quantité à commander ; ruptures et surstocks sont tous deux des coûts ;
- **Tarification dynamique** : ajuster les prix en temps réel à partir des prévisions de demande ; le chiffre d'affaires est la récompense ;
- **Ordonnancement des ressources** : allouer puissance de calcul ou électricité en fonction des prévisions de charge.

Dans ces scénarios, la « prévision » est la **perception** en amont, et l'apprentissage par renforcement se charge de l'**action** en aval. Deux points méritent cependant attention : le RL a généralement besoin d'un **simulateur / environnement** pour multiplier les essais et erreurs (tâtonner dans le monde réel coûte trop cher), et il est **très gourmand en données**.

En une phrase : **pour prévoir, on utilise l'apprentissage supervisé ; c'est pour agir sur les résultats de la prévision qu'on envisage l'apprentissage par renforcement**.

## En résumé

- Apprentissage par renforcement = un agent apprend une **politique** par **interaction par essais et erreurs** avec un environnement, en maximisant la **récompense cumulée à long terme**.
- Éléments clés : état $s$, action $a$, récompense $r$, politique $\pi(a\mid s)$, retour $G_t=\sum_k \gamma^k r_{t+k}$, fonctions de valeur $V^\pi/Q^\pi$.
- Son ossature mathématique est le **processus de décision markovien (MDP)** ; sa difficulté centrale est le **compromis exploration–exploitation**.
- Différence essentielle avec l'apprentissage supervisé : **pas d'étiquettes, seulement des récompenses différées**, et les actions modifient les données futures.
- Dans les séries temporelles : **la prévision relève de l'apprentissage supervisé, tandis que les problèmes de décision qui « agissent sur les prévisions » — trading, réapprovisionnement, tarification — sont le terrain du RL**.

Pour aller plus loin : [Apprentissage supervisé](../supervised-learning/) · [Apprentissage non supervisé](../unsupervised-learning/) · [Modèles linéaires](../linear-model/) · [Arbres de décision](../decision-tree/) · [Apprentissage ensembliste / GBDT](../ensemble-gbdt/) · [SVM](../svm/)

---

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
