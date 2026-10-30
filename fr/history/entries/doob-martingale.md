---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1953 · Mathématiques"
permalink: /fr/history/e/doob-martingale/
title: "La théorie des martingales (Doob, 1953)"
lead: "« Dans un jeu équitable, la fortune espérée à l'instant suivant est égale à la fortune présente. » Doob a forgé cette intuition naïve en ossature des processus stochastiques modernes, et en cœur mathématique de la finance sans arbitrage."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

Le mot « martingale » vient d'une vieille stratégie de jeu consistant à « doubler la mise après chaque perte ». Lévy et Ville lui donnèrent une définition probabiliste dans les années 1930, mais c'est Joseph L. Doob qui, avec son grand ouvrage *Stochastic Processes* (1953), en fit un édifice théorique complet. Les probabilités fondées sur la théorie de la mesure (l'axiomatisation de Kolmogorov) étaient alors mûres, et l'on avait besoin d'un langage pour décrire précisément la dynamique de « l'information qui s'accumule au fil du temps » — la martingale vint combler exactement ce manque.

### Problème

Comment exprimer de façon mathématiquement rigoureuse le « jeu équitable » et le « flux d'information » ? Intuitivement, dans un pari équitable, la meilleure prévision de votre fortune future est votre fortune présente ; mais pour rendre cette phrase démontrable et exploitable — prouver qu'aucun système de jeu ne gagne à coup sûr, établir convergences et inégalités —, il faut d'abord définir précisément « l'espérance conditionnelle sachant l'information disponible » et contraindre son évolution dans le temps. **Comment faire des « fluctuations équitables imprévisibles » un objet calculable, susceptible de théorèmes ?**

### Autres courants de l'époque (et leurs limites)

- **Processus à accroissements indépendants (marche aléatoire, mouvement brownien)** : structure claire, mais l'exigence d'accroissements mutuellement indépendants est trop forte ; bien des processus équitables ne sont pas indépendants, tout en restant « imprévisibles quant à la direction du pas suivant ».
- **Théorie spectrale des processus stationnaires ([Wold](../wold/), Wiener)** : excellente pour les moments d'ordre deux et l'analyse fréquentielle, centrée sur la structure de corrélation, mais elle ne décrit pas directement la dynamique de « l'espérance conditionnelle mise à jour par l'information », ni les temps d'arrêt.
- **Théorèmes limites classiques (loi des grands nombres, théorème central limite)** : conçus pour des sommes indépendantes, ils traitent mal les situations séquentielles avec dépendance et arrêt à un instant aléatoire.

### Méthode

Étant donnée une suite croissante de tribus d'information (une **filtration**) $$\mathcal{F}_0\subseteq\mathcal{F}_1\subseteq\cdots$$, un processus $$\{X_t\}$$ est une **martingale** s'il est adapté à la filtration et si

$$ \mathbb{E}\!\left[X_{t+1}\mid \mathcal{F}_t\right] = X_t $$

c'est-à-dire : en utilisant toute l'information disponible jusqu'à $$t$$ pour prévoir l'instant suivant, la meilleure estimation est la valeur actuelle — c'est la formulation précise de « l'équité » (avec $$\ge$$ on parle de sous-martingale, avec $$\le$$ de sur-martingale). Doob bâtit sur cette base trois piliers : la **décomposition de Doob** — toute sous-martingale se décompose de manière unique en une martingale et un processus croissant prévisible

$$ X_t = M_t + A_t,\qquad M\ \text{martingale},\ A\ \text{prévisible et croissant} $$

ce qui sépare proprement la « tendance prévisible » $$A_t$$ de la « fluctuation équitable imprévisible » $$M_t$$ ; le **théorème d'arrêt optimal** — sous des conditions appropriées, $$\mathbb{E}[X_\tau]=\mathbb{E}[X_0]$$, ce qui affirme qu'aucune stratégie d'arrêt fondée sur l'information disponible ne peut modifier l'espérance d'un jeu équitable (aucun système de jeu ne gagne à coup sûr) ; et enfin l'**inégalité maximale de Doob** et le **théorème de convergence des martingales**, qui garantit qu'une martingale bornée converge presque sûrement.

### Résultats

La martingale devint rapidement un outil universel des processus stochastiques : elle unifia les démonstrations de la loi des grands nombres, servit de fondement à l'intégrale stochastique d'Itô et aux équations différentielles stochastiques, et rendit maîtrisable l'analyse de « l'arrêt à un instant aléatoire ». En statistique, elle réunit tests séquentiels, rapports de vraisemblance et analyse des temps d'arrêt dans un même cadre.

### Portée et perspectives

La martingale est le cœur mathématique de la finance moderne : l'**hypothèse des marchés efficients** dit que les prix reflètent déjà toute l'information et que leurs variations futures sont imprévisibles — c'est exactement $$\mathbb{E}[X_{t+1}\mid\mathcal{F}_t]=X_t$$ ; l'**absence d'arbitrage** équivaut à l'existence d'une « mesure martingale équivalente » sous laquelle les prix actualisés sont des martingales, d'où découle la valorisation des options de Black–Scholes. Vue sous cet angle, la marche aléatoire de [Bachelier](../bachelier/) en 1900 en était l'embryon, et le « regret » et l'analyse des temps d'arrêt du [bandit de Robbins](../robbins-bandit/) en sont de proches voisins. Une seule phrase — « l'espérance de l'instant suivant est égale à l'instant présent » — a porté un demi-siècle de mathématiques, des théorèmes limites de probabilité jusqu'à la valorisation des produits dérivés.
