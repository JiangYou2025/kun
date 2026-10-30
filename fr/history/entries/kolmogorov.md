---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1933 · Mathématiques"
permalink: /fr/history/e/kolmogorov/
title: "Les axiomes des probabilités (Kolmogorov, 1933)"
lead: "Qu'est-ce au juste qu'une probabilité ? Pendant trois siècles, ce fut une « intuition de joueur ». En 1933, Kolmogorov la fixe définitivement par trois axiomes de théorie de la mesure, et « la moyenne temporelle égale la moyenne d'ensemble » devient enfin un théorème démontrable."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

De Pascal et Fermat à Laplace, la théorie des probabilités avait accumulé une foule de résultats, mais il lui manquait toujours un fondement logique rigoureux — le sixième problème de Hilbert, en 1900, rangeait même « l'axiomatisation des probabilités » parmi les questions ouvertes. Au début du XXᵉ siècle, la théorie de la mesure et de l'intégration de Lebesgue arrive à maturité et offre aux probabilités un support possible. En 1933, Andrey Kolmogorov publie les *Fondements de la théorie des probabilités* (*Grundbegriffe der Wahrscheinlichkeitsrechnung*), qui achève d'un seul coup l'axiomatisation par la théorie de la mesure et établit officiellement les probabilités comme une branche des mathématiques modernes.

### Problème

Avant Kolmogorov, « variable aléatoire », « probabilité conditionnelle » ou « limite d'une infinité d'épreuves » n'avaient pas de définition unifiée, et bien des affirmations sur l'infini et sur les processus aléatoires continus ne pouvaient être démontrées rigoureusement. En particulier, une question essentielle pour les séries temporelles : **nous ne pouvons observer qu'une seule série temporelle (une seule réalisation) ; de quel droit utiliser sa moyenne temporelle pour estimer l'espérance véritable (la moyenne d'ensemble) de tout le processus aléatoire ?** Sans probabilités axiomatisées, la légitimité de cette inférence restait en suspens.

### Les autres courants de l'époque (et leurs limites)

- **Intuition fréquentiste (le « collectif » de von Mises)** : définit la probabilité comme la limite de la fréquence sur une infinité d'épreuves. L'idée est simple, mais la « suite aléatoire » elle-même est difficile à définir sans contradiction, ce qui en fait un fondement axiomatique peu net.
- **Définition classique par l'équiprobabilité** : probabilité = nombre de cas favorables / nombre total de cas. Elle ne vaut que pour des situations finies et symétriques, et échoue immédiatement face aux lois continues et aux processus aléatoires.
- Aucune des deux ne peut porter une théorie des processus aléatoires **en temps continu et de dimension infinie**, qui est précisément ce dont ont besoin les séries temporelles et les processus de diffusion.

### Méthode

Kolmogorov définit la probabilité comme une **mesure** sur un espace probabilisé $$(\Omega,\mathcal F,\mathbb P)$$, satisfaisant trois axiomes : la positivité, la normalisation $$\mathbb P(\Omega)=1$$ et l'additivité dénombrable

$$ \mathbb P\Big(\bigcup_{i=1}^{\infty} A_i\Big)=\sum_{i=1}^{\infty}\mathbb P(A_i)\quad(\text{si les }A_i\text{ sont deux à deux disjoints}) $$

Une variable aléatoire est une fonction mesurable, l'espérance est une intégrale, et l'espérance conditionnelle est définie rigoureusement par le théorème de Radon–Nikodym. Son **théorème de cohérence (d'extension)** garantit que, dès lors que les lois de dimension finie sont mutuellement cohérentes, il existe un processus aléatoire défini sur la trajectoire entière : les processus en temps continu existent donc légitimement. Pour les processus de Markov, il écrit les **équations progressive et rétrograde** de l'évolution de la densité de probabilité (équations de Kolmogorov, qui correspondent à l'équation de Fokker–Planck en physique) :

$$ \frac{\partial p}{\partial t}=-\frac{\partial}{\partial x}\big[\mu(x)p\big]+\frac12\frac{\partial^2}{\partial x^2}\big[\sigma^2(x)p\big] $$

Dans ce cadre, le **théorème ergodique** peut être énoncé et démontré rigoureusement : pour un processus stationnaire ergodique,

$$ \frac1T\int_0^T f(X_t)\,dt \;\xrightarrow{\;T\to\infty\;}\; \mathbb E[f(X_0)] $$

autrement dit, **la moyenne temporelle converge vers la moyenne d'ensemble**.

### Résultats

Les probabilités acquièrent dès lors un statut aussi rigoureux que l'analyse et l'algèbre. Le bénéfice le plus direct : le théorème ergodique fournit la preuve de légitimité de « l'inférence statistique à partir d'une seule trajectoire » ; sans lui, l'estimation de la moyenne et de l'autocovariance d'une série temporelle ne tiendrait pas logiquement. Les équations progressive et rétrograde, elles, mettent en correspondance exacte la dynamique stochastique de [Langevin / OU](../langevin/) et des équations aux dérivées partielles déterministes.

### Portée et perspectives

L'axiomatisation de Kolmogorov est le socle commun de toute la théorie ultérieure des processus stochastiques : la théorie des martingales de [Lévy](../levy/) et Doob, l'intégrale stochastique d'Itô, la [théorie spectrale de Wiener–Khinchin](../wiener-khinchin/), et jusqu'à la théorie de la généralisation de l'apprentissage statistique moderne reposent sur elle. Chaque fois que nous supposons que « les données sont des échantillons indépendants d'une certaine loi » ou que « la stationnarité rend l'estimation convergente », ce sont ces axiomes de 1933 qui, en silence, s'en portent garants. Ils ont fait de « l'inférence d'un monde aléatoire infini à partir d'observations finies » une science rigoureuse.
