---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1980 · Contrôle / Communications"
permalink: /fr/history/e/mpc/
title: "La commande prédictive par modèle (Cutler · Ramaker, 1980)"
lead: "Plutôt que de corriger passivement l'erreur après coup, mieux vaut regarder quelques pas en avant : prédire l'avenir avec un modèle, résoudre une optimisation sous contraintes, n'exécuter que le premier pas — puis recommencer en glissant l'horizon."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1970, le pilier de la commande industrielle est le PID : il ajuste la commande à partir de l'erreur courante, de son intégrale et de sa dérivée. Simple et fiable, il est néanmoins **réactif** par nature — il ne regarde que l'instant présent, ne planifie pas l'avenir et gère mal les contraintes dures du type « l'ouverture de la vanne est bornée » ou « la température ne doit pas dépasser un seuil ». Or les procédés du raffinage ou de la pétrochimie sont souvent multivariables, fortement couplés et soumis à de nombreuses contraintes opératoires ; le réglage boucle par boucle du PID y atteint ses limites. La programmation dynamique de [Bellman](../bellman-dp/) et la théorie de la commande optimale existaient depuis longtemps, mais résoudre directement un problème de commande optimale à horizon infini était hors de portée d'un calcul en ligne.

### Problème

Comment faire en sorte qu'un régulateur **exploite activement des prévisions de l'avenir**, **traite explicitement les contraintes**, tout en restant calculable à chaque période d'échantillonnage ? La commande optimale théorique soit ignore les contraintes, soit est irréalisable en calcul. L'industrie avait besoin d'un compromis à la fois optimal et déployable.

### Les autres courants de l'époque (et leurs limites)

- **Le PID / la rétroaction classique** : réglage simple et robuste, mais aucune anticipation, aucun traitement des contraintes, et une coordination difficile des couplages multivariables.
- **La LQR / la commande optimale ([Kalman](../kalman/), etc.)** : elle fournit un retour d'état élégant, mais sa forme standard n'inclut pas de contraintes d'inégalité et cesse d'être valable dès qu'une contrainte devient active.
- **La programmation dynamique pure** : optimale en théorie, mais la malédiction de la dimension rend irréaliste la résolution en ligne sur tout l'horizon.

### Méthode

Cutler et Ramaker proposent le Dynamic Matrix Control (DMC), qui fonde la commande prédictive par modèle (MPC). L'idée est l'**horizon glissant (receding horizon)** : à chaque instant $$t$$, on utilise un modèle du procédé pour prédire les $$N$$ sorties futures $$\hat{y}_{t+k}$$, puis on résout une optimisation sous contraintes à horizon fini :

$$ \min_{u_t,\dots,u_{t+M-1}} \sum_{k=1}^{N}\big\| \hat{y}_{t+k}-r_{t+k}\big\|_Q^2 + \sum_{k=0}^{M-1}\big\|\Delta u_{t+k}\big\|_R^2 $$

$$ \text{s.t.}\quad u_{\min}\le u_{t+k}\le u_{\max},\quad \Delta u_{\min}\le \Delta u_{t+k}\le \Delta u_{\max},\quad y_{\min}\le \hat{y}_{t+k}\le y_{\max} $$

où $$r$$ est la trajectoire de référence, $$Q,R$$ des pondérations et $$\Delta u$$ l'incrément de commande. Le DMC construit le modèle de prédiction à partir des coefficients de la réponse indicielle, et l'ensemble du problème est un programme quadratique (QP). Le point clé : une fois la séquence optimale de commandes obtenue, **on n'en exécute que le premier pas** $$u_t$$ ; à l'instant suivant, on reçoit une nouvelle mesure, on prédit de nouveau et on résout de nouveau. Cette structure glissante « prédire — optimiser — exécuter le premier pas — rétroagir — prédire de nouveau » combine l'anticipation de la planification optimale et la rétroaction qui compense les erreurs de modèle et les perturbations.

### Résultats

Le DMC a connu un grand succès dans les raffineries de Shell et d'autres entreprises : il permet de fonctionner de façon stable tout près des limites de contraintes (qui correspondent souvent précisément à l'optimum économique), avec des gains notables de capacité et d'efficacité énergétique. La MPC est ensuite devenue la norme de fait de la commande avancée des procédés industriels, et s'est étendue à la chimie, à l'énergie électrique, à l'automobile et jusqu'à la robotique.

### Portée et perspectives

La MPC a mis en œuvre, à l'échelle de l'ingénierie, l'idée de « **décision pilotée par la prévision** » : commander n'est plus corriger passivement les erreurs, mais planifier de façon optimale, sous contraintes, à partir d'une prévision glissante de l'avenir. Le modèle de procédé sur lequel elle s'appuie provient souvent de l'[identification de systèmes](../system-identification/) ; son principe d'horizon glissant fait écho à l'idée d'« utiliser la prévision pour guider l'action présente » de l'apprentissage par renforcement par [différences temporelles / Q-learning](../td-qlearning/). Aujourd'hui, de la conduite autonome à l'ordonnancement des centres de données, partout où l'on « regarde quelques pas, résout une optimisation, avance d'un pas, puis regarde à nouveau », c'est l'esprit de la MPC qui se prolonge.
