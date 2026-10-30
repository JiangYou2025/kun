---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1949 · Mathématiques"
permalink: /fr/history/e/feynman-kac/
title: "Résoudre une EDP par des chemins aléatoires (Kac · Feynman, 1949)"
lead: "La solution d'une équation aux dérivées partielles parabolique égale la moyenne prise sur une infinité de chemins aléatoires — la formule de Feynman–Kac soude l'EDP déterministe à l'espérance d'un processus stochastique."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

En 1948, Feynman proposa la formulation par **intégrale de chemins** de la mécanique quantique : l'évolution d'une particule est une somme sur tous les chemins possibles. Après avoir assisté à son exposé, Mark Kac comprit qu'appliquer cette idée de « somme sur les chemins » à l'équation de diffusion **réelle** (et non à l'équation de Schrödinger en temps imaginaire) était rigoureusement faisable — car c'est précisément la [mesure de Wiener](../ito/) qui y apparaît. En 1949, Kac établit le résultat rigoureux aujourd'hui appelé **formule de Feynman–Kac**, exprimant pour la première fois la solution d'une EDP parabolique comme l'espérance d'un processus stochastique.

### Problème

Les **EDP paraboliques** comme l'équation de la chaleur ou de diffusion se résolvent d'ordinaire par des moyens analytiques (séparation des variables, fonctions de Green), qui deviennent extrêmement difficiles dès que la dimension augmente. **Peut-on changer de point de vue : au lieu de résoudre directement l'équation, « échantillonner » la solution à l'aide d'une population de particules en marche aléatoire ?** Et, inversement, quelle est la relation exacte entre EDP et processus stochastiques ?

### Autres courants de l'époque (et leurs limites)

- **Méthodes purement analytiques (fonctions de Green, développements en fonctions propres)** : élégantes en basse dimension et sur des frontières régulières, mais confrontées à la malédiction de la dimension dès que la dimension est élevée, les coefficients variables ou les frontières complexes ; les solutions en forme close sont alors introuvables.
- **Différences finies numériques déterministes** : on discrétise l'EDP sur une grille. Le nombre de points de grille croît exponentiellement avec la dimension, rendant le calcul infaisable en grande dimension.
- **Intégrale de chemins formelle** : la somme de Feynman est d'une puissance considérable en physique, mais sa mesure n'est pas rigoureuse en temps imaginaire (ce n'est pas une véritable mesure). **La correction décisive de Kac** fut de passer à la diffusion réelle, faisant de la « somme » sur les chemins une véritable espérance par rapport à la mesure de Wiener, et donc de la rendre rigoureuse.

### Méthode

Considérons l'EDP parabolique avec terme de potentiel $$V$$ et terme source
$$ \frac{\partial u}{\partial t}=\tfrac12\sigma^2\,\frac{\partial^2 u}{\partial x^2}+\mu\,\frac{\partial u}{\partial x}-V(x)\,u,\qquad u(0,x)=f(x) $$
La formule de Feynman–Kac affirme que sa solution peut s'écrire comme l'**espérance** d'un processus de diffusion $$X_s$$ (vérifiant $$dX_s=\mu\,ds+\sigma\,dW_s$$, $$X_0=x$$) :

$$ u(t,x)=\mathbb{E}\Big[\,f(X_t)\,\exp\!\Big(-\!\int_0^t V(X_s)\,ds\Big)\,\Big|\,X_0=x\Big] $$

L'intuition : on lâche depuis $$x$$ une infinité de trajectoires aléatoires ; chacune, portant le poids $$\exp(-\!\int V)$$, va jusqu'à son point d'arrivée où l'on prend la valeur de $$f$$ ; la moyenne sur tous les chemins donne la solution en ce point. Le moteur de la démonstration est précisément le [lemme d'Itô](../ito/) — en différentiant $$u(t-s,X_s)\exp(-\!\int_0^s V)$$, l'EDP fait exactement s'annuler le terme de dérive, laissant une **martingale** dont l'espérance donne la formule.

### Résultats

La résolution des EDP gagnait ainsi une voie « Monte-Carlo » : on estime l'espérance par simulation aléatoire, et le coût de calcul n'explose plus exponentiellement avec la dimension — les problèmes de grande dimension s'ouvrent soudain. Plus profondément, la formule révèle que le générateur d'un processus de diffusion et l'opérateur parabolique sont une seule et même chose, reliant de façon permanente la théorie des probabilités et les équations aux dérivées partielles.

### Portée et perspectives

Feynman–Kac est le moteur théorique de la finance en temps continu. L'EDP de valorisation de [Black–Scholes](../black-scholes/) (1973) a une solution qui s'écrit directement comme « l'espérance du gain actualisé sous la mesure risque-neutre » — c'est l'incarnation financière de Feynman–Kac, et le fondement de la valorisation par Monte-Carlo. En faisant de « résoudre une équation » et de « moyenner sur des chemins aléatoires » une seule et même opération, elle irrigue encore aujourd'hui la valorisation des produits dérivés, le contrôle stochastique, la simulation d'événements rares, et jusqu'aux méthodes de résolution par échantillonnage en physique et en apprentissage automatique.
