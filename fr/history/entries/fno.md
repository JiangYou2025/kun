---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2020 · Physique"
permalink: /fr/history/e/fno/
title: "L'opérateur neuronal de Fourier (Li et al., 2020)"
lead: "Une convolution ne voit que son voisinage local. En la transposant dans le domaine fréquentiel pour en faire une opération globale, on peut apprendre des opérateurs de résolution d'EDP indépendants de la résolution de la grille."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans la foulée des [PINN et DeepONet](../pinn-deeponet/), « apprendre l'opérateur solution d'une EDP avec un réseau de neurones » devint un objectif en vogue : on voulait entraîner un modèle qui associe une fonction d'entrée (conditions initiales, champ de paramètres) à la fonction solution en sortie, et qui donne instantanément la solution pour une nouvelle entrée, en évitant le coût des méthodes numériques classiques qui recalculent tout à chaque fois. La difficulté : le champ réceptif d'un réseau convolutif ordinaire est local, alors que la solution d'une EDP est souvent déterminée par des **interactions globales**.

### Problème

Un apprenant d'opérateurs idéal doit satisfaire deux conditions : la **globalité** — une seule opération doit permettre aux informations éloignées de s'influencer mutuellement ; l'**indépendance vis-à-vis de la discrétisation (discretization-invariant)** — entraîné sur une grille grossière, il doit rester valable en inférence sur une grille fine, car il apprend un opérateur continu et non une application discrète sur une grille fixe. Un CNN ordinaire ne satisfait ni l'une ni l'autre : son champ réceptif est local, et changer de résolution impose de le réentraîner. **Comment construire un opérateur apprenable à la fois global et indépendant de la grille ?**

### Autres courants de l'époque (et leurs limites)

- **Modèles de substitution CNN** : traitent la solution de l'EDP comme une régression d'image ; champ réceptif local et **liés à une résolution fixe**, ils échouent dès qu'on change de grille.
- **Opérateurs à réseaux de neurones sur graphes** : gèrent les maillages irréguliers, mais l'information globale doit s'accumuler par de multiples étapes de passage de messages, et les interactions lointaines coûtent cher.
- **DeepONet** : a inauguré l'apprentissage d'opérateurs, mais sa structure branche–tronc est moins directe que les méthodes fréquentielles pour généraliser entre résolutions et exprimer des noyaux globaux.

### Méthode

Le cœur du FNO est la **couche de Fourier** : elle pousse le théorème de convolution jusqu'au bout — une convolution dans le domaine spatial équivaut à une multiplication point par point dans le domaine fréquentiel. Chaque couche applique une transformée de Fourier aux caractéristiques $$v$$, multiplie les modes basse fréquence par des poids apprenables $$R$$, puis applique la transformée inverse, ce qui donne une opération d'intégrale à noyau **globale** :

$$ (\mathcal{K}v)(x)=\mathcal{F}^{-1}\big(R\cdot \mathcal{F}(v)\big)(x) $$

En pratique, on ne conserve que les premiers modes basse fréquence $$R\in\mathbb{C}^{k_{\max}\times d\times d}$$, combinés à une branche de transformation linéaire point par point $$Wv$$ et à une non-linéarité $$\sigma$$ pour former une couche :

$$ v_{t+1}(x)=\sigma\Big(Wv_t(x)+\mathcal{F}^{-1}\big(R\cdot\mathcal{F}(v_t)\big)(x)\Big) $$

Comme les poids agissent sur les **modes fréquentiels** et non sur les points de la grille, un même jeu de paramètres s'applique à n'importe quelle résolution — c'est l'origine de l'indépendance vis-à-vis de la résolution ; le calcul par FFT rend chaque couche efficace.

### Résultats

Sur des EDP paramétrées comme Burgers, l'écoulement de Darcy ou Navier–Stokes, le FNO surpasse en précision les opérateurs neuronaux antérieurs, et son inférence est **plusieurs ordres de grandeur plus rapide** que les solveurs numériques classiques. Il peut être entraîné sur des données basse résolution et transféré sans réentraînement à une inférence haute résolution (zero-shot super-resolution), réduisant considérablement les coûts en données et en calcul.

### Portée et perspectives

Le FNO injecte l'[analyse de Fourier](../fourier/) classique et la pensée fréquentielle dans l'apprentissage profond d'opérateurs, offrant un paradigme global, efficace et indépendant de la résolution. Il a directement stimulé le calcul scientifique piloté par les données, en particulier la prévision spatio-temporelle à grande échelle — appliquer des opérateurs fréquentiels indépendants de la résolution au système Terre a donné naissance aux [modèles météorologiques neuronaux comme FourCastNet](../neural-weather/). Sur le thème fondateur des séries temporelles, « apprendre comment une dynamique évolue dans l'espace et le temps », le FNO fournit un outil puissant venu de la physique.
