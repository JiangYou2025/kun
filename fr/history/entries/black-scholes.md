---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1973 · Mathématiques"
permalink: /fr/history/e/black-scholes/
title: "La formule de valorisation des options (Black · Scholes · Merton, 1973)"
lead: "Répliquez une option avec un portefeuille de couverture ajusté en continu, et son prix ne dépend plus de l'aversion au risque. Black, Scholes et Merton tirent du calcul d'Itô une EDP qui fait entrer la valorisation des produits dérivés dans une nouvelle ère."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

Les options — le droit d'acheter ou de vendre un sous-jacent à un prix convenu dans le futur — s'échangeaient depuis longtemps, mais la question « combien valent-elles vraiment ? » est restée longtemps sans réponse convaincante. Les tentatives antérieures devaient souvent supposer les préférences des investisseurs face au risque ou leurs anticipations sur les rendements futurs, et les avis divergeaient. À cette époque, le [calcul d'Itô](../ito/) offrait déjà des outils rigoureux pour les processus aléatoires en temps continu, et le mouvement brownien géométrique servait à décrire les trajectoires des cours : tout était en place, il ne manquait que le dernier pas.

### Problème

La difficulté centrale est l'**aversion au risque** : le gain d'une option dépend du cours futur, incertain, de l'action ; il semble donc qu'il faille savoir quelle compensation le marché exige pour porter ce risque avant de pouvoir fixer un prix. Or les investisseurs n'ont pas tous les mêmes préférences — le prix varierait-il alors selon la personne ? **Peut-on donner un prix d'option objectif, indépendant des préférences subjectives de quiconque ?**

### Autres courants de l'époque (et leurs limites)

- **Valorisation par l'utilité / l'équilibre** : déduire le prix des fonctions d'utilité des investisseurs et de l'équilibre de marché. Il faut fixer des paramètres de préférence difficiles à observer, et la conclusion n'est pas unique.
- **Actualisation du gain espéré** : actualiser le gain futur espéré de l'option à un certain taux. Mais la question « quel taux d'actualisation utiliser ? » réintroduit à elle seule le problème de la prime de risque.
- **Ajustement purement statistique sur les prix historiques des options** : très empirique, sans fondement théorique d'absence d'arbitrage, difficile à extrapoler à de nouveaux contrats.

### Méthode

L'idée clé est la **réplication par couverture dynamique**. Supposons que le cours suive un mouvement brownien géométrique $$dS=\mu S\,dt+\sigma S\,dW$$ ; on développe le prix de l'option $$V(S,t)$$ par le **lemme d'Itô** :

$$ dV=\frac{\partial V}{\partial t}\,dt+\frac{\partial V}{\partial S}\,dS+\frac12\,\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\,dt $$

On construit un portefeuille qui détient l'option et vend à découvert $$\partial V/\partial S$$ actions : le terme aléatoire $$dW$$ s'y annule exactement, et le portefeuille devient instantanément **sans risque**. L'absence d'arbitrage impose qu'il ne rapporte que le taux sans risque $$r$$, d'où l'**équation aux dérivées partielles de Black–Scholes** :

$$ \frac{\partial V}{\partial t}+\frac12\,\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV=0 $$

Notons que l'équation **ne contient pas $$\mu$$** — la dérive réelle a disparu, et le prix ne dépend pas des préférences face au risque. Pour un call européen, on obtient une formule fermée ($$N(\cdot)$$ est la fonction de répartition de la loi normale standard) :

$$ C=S_0\,N(d_1)-K e^{-rT}N(d_2),\qquad d_{1,2}=\frac{\ln(S_0/K)+(r\pm\tfrac12\sigma^2)T}{\sigma\sqrt{T}} $$

### Résultats

Une formule qui ne requiert que cinq grandeurs, $$S_0,K,r,T,\sigma$$, et dont le seul paramètre inconnu est la volatilité $$\sigma$$, a fait passer la valorisation des produits dérivés de l'art divinatoire à l'ingénierie calculable. Elle a directement alimenté l'essor explosif des marchés d'options et constitue un résultat fondateur de l'ingénierie financière ; Scholes et Merton ont reçu pour cela le prix Nobel d'économie 1997.

### Portée et perspectives

Pour les séries temporelles, Black–Scholes a placé la **modélisation par processus aléatoires** au cœur de la pratique financière, tout en exposant les points faibles de ses hypothèses : volatilité $$\sigma$$ constante et rendements gaussiens. Le marché a voté contre avec le « sourire de volatilité ». Les efforts pour le corriger forment la suite de l'histoire : décrire la volatilité variable dans le temps avec [ARCH/GARCH](../arch/), des trajectoires de volatilité plus réalistes avec la volatilité stochastique et la [volatilité rugueuse](../rough-volatility/), tandis que le calcul efficace des sensibilités (les Grecques) a suscité les applications du [calcul de Malliavin](../malliavin/). Une seule EDP a ouvert toute l'ère de la finance quantitative.
