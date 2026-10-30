---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1976 · Mathématiques"
permalink: /fr/history/e/malliavin/
title: "Dériver par rapport au hasard (Malliavin, 1976)"
lead: "Peut-on dériver par rapport à la trajectoire brownienne elle-même ? Malliavin transporte le calcul des variations dans un espace aléatoire de dimension infinie ; il permet ainsi de décider si la solution d'une équation stochastique admet une densité lisse, et fournit un algorithme élégant pour les sensibilités de couverture."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Le [calcul d'Itô](../ito/) a résolu la question « comment intégrer par rapport à un processus aléatoire », faisant des équations différentielles stochastiques (EDS) $$dX_t=b(X_t)dt+\sigma(X_t)dW_t$$ le langage standard de la modélisation des phénomènes aléatoires à temps continu ; le modèle de [Black–Scholes](../black-scholes/) repose dessus. Mais une question complémentaire restait ouverte : peut-on dériver une quantité aléatoire par rapport à **la source d'aléa qui la pilote (la trajectoire brownienne elle-même)** ? Il fallait pour cela un calcul différentiel sur l'espace des trajectoires, de dimension infinie.

### Problème

Deux besoins concrets l'ont motivé. Le premier est purement théorique : quand la solution $$X_t$$ d'une EDS possède-t-elle une **densité de probabilité lisse** ? La question touche à la régularité des solutions d'équations aux dérivées partielles (Malliavin a d'ailleurs créé cette théorie précisément pour donner une preuve probabiliste du théorème d'hypoellipticité de Hörmander). Le second est appliqué : en finance, comment calculer de façon efficace et stable les **sensibilités (les Grecques)** du prix d'une option par rapport à ses paramètres, en particulier lorsque la fonction de paiement n'est pas lisse et que les différences finies sont très bruitées ? **Il fallait un calcul capable de « dériver par rapport au hasard ».**

### Les autres courants de l'époque (et leurs limites)

- **Le calcul d'Itô** : excellent pour l'intégration stochastique, mais il ne fournit pas en lui-même de « dérivée directionnelle » par rapport à la trajectoire brownienne et répond difficilement à la question de l'existence d'une densité.
- **Les Grecques par différences finies** : simples à mettre en œuvre, mais numériquement très instables pour des paiements discontinus, avec une forte variance et une convergence lente.
- **Les méthodes par EDP (équations aux dérivées partielles) pour les sensibilités** : efficaces en petite dimension, mais elles s'effondrent rapidement quand la dimension augmente (malédiction de la dimension).

### Méthode

Malliavin définit sur l'espace de Wiener un **opérateur de dérivation** $$D$$ : pour une fonctionnelle $$F$$ (par exemple $$F=\int_0^T h_s\,dW_s$$), $$D_t F$$ mesure la sensibilité de $$F$$ à l'accroissement brownien à l'instant $$t$$. Son opérateur adjoint $$\delta$$ (l'intégrale de Skorokhod) vérifie une formule d'intégration par parties :

$$ \mathbb{E}\!\left[\,F\,\delta(u)\,\right]=\mathbb{E}\!\left[\,\langle DF,\,u\rangle_{L^2[0,T]}\,\right] $$

Cette **intégration par parties stochastique** est la source de toute sa puissance. D'une part, si la matrice de covariance de Malliavin $$\gamma_X=\langle DX,DX\rangle$$ est inversible et suffisamment régulière, on peut démontrer que $$X$$ admet une densité lisse — c'est le critère de densité. D'autre part, elle permet de transformer « dériver une fonction de paiement non lisse » en « prendre l'espérance contre un poids lisse » :

$$ \frac{\partial}{\partial\theta}\,\mathbb{E}[\Phi(X_T)]=\mathbb{E}\!\left[\Phi(X_T)\,\pi\right] $$

où le poids $$\pi$$ est donné explicitement par $$\delta$$ : **le gradient porte sur le poids, et non sur la fonction de paiement**, de sorte que l'on peut estimer de manière stable les Grecques par Monte-Carlo même lorsque $$\Phi$$ présente des sauts.

### Résultats

Sur le plan théorique, le calcul de Malliavin fournit un critère simple d'existence et de régularité de la densité des solutions d'EDS, ainsi qu'une preuve probabiliste pour les équations hypoelliptiques de type Hörmander. Sur le plan appliqué, il a donné la méthode des « poids de Malliavin » pour calculer des sensibilités comme le Delta, le Gamma ou le Vega, particulièrement efficace pour les produits dérivés à paiement discontinu ou dépendant de la trajectoire, avec une réduction notable de la variance Monte-Carlo.

### Portée et perspectives

En étendant le calcul des variations à l'analyse stochastique en dimension infinie, il est devenu l'un des piliers de l'analyse stochastique moderne et sert aussi en profondeur la finance quantitative pour la couverture fine et le calcul des risques dans le cadre de [Black–Scholes](../black-scholes/). Cet outil pour « dériver par rapport au hasard » fait écho à des recherches récentes comme la [volatilité rugueuse](../rough-volatility/), modélisée par le mouvement brownien fractionnaire : lorsque les trajectoires de volatilité deviennent plus rugueuses et les paiements plus irréguliers, pouvoir dériver et intégrer par parties sur l'espace des trajectoires est précisément la clé pour analyser ces modèles.
