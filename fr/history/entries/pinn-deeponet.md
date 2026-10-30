---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2019 · Physique"
permalink: /fr/history/e/pinn-deeponet/
title: "Réseaux informés par la physique et opérateurs neuronaux (Raissi · Lu, 2019)"
lead: "Si l'on inscrit l'équation qui gouverne le système dans la fonction de perte elle-même, un réseau de neurones peut-il à la fois ajuster les données et obéir à la physique ? Et, un pas plus loin, peut-il apprendre d'un coup les solutions de toute une famille d'équations ?"
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Une foule de systèmes dynamiques — fluides, conduction thermique, ondes — sont décrits par des **équations aux dérivées partielles (EDP)**. On les résout traditionnellement par des méthodes numériques discrètes comme les différences finies ou les éléments finis : précises, mais le maillage coûte cher, et elles sont particulièrement à la peine face aux **problèmes inverses** (retrouver des paramètres ou des champs inconnus à partir d'observations clairsemées). Parallèlement, les réseaux de neurones excellent à ajuster des données, mais ignorent souvent les contraintes physiques et se dégradent dès qu'ils extrapolent hors des zones couvertes par les données.

### Problème

Deux aspirations de longue date. D'une part, **peut-on faire respecter les lois physiques connues par un modèle piloté par les données**, de sorte qu'il fournisse une solution physiquement plausible même à partir d'observations clairsemées, voire bruitées, et qu'il résolve au passage les paramètres inconnus d'un problème inverse ? D'autre part, un solveur numérique classique **doit tout recalculer pour chaque jeu de paramètres ou de conditions initiales et aux limites** — peut-on entraîner un modèle qui apprenne une fois pour toutes l'application « fonction d'entrée → fonction de sortie », et donne instantanément la solution pour une nouvelle entrée ?

### Autres courants de l'époque (et leurs limites)

- **Solveurs numériques purs (FEM/FDM)** : précis et fiables, mais le maillage est coûteux, chaque nouveau cas de figure exige une nouvelle résolution, et les problèmes inverses demandent des simulations directes répétées.
- **Régression purement pilotée par les données** : souple, mais sans contrainte physique : elle extrapole mal, exige beaucoup de données et inspire peu de confiance physique.
- **Réseaux de neurones classiques approchant une solution unique** : ils peuvent ajuster une courbe solution, mais font du solveur un outil à usage unique, incapable de généraliser à d'autres fonctions d'entrée.

### Méthode

Un **PINN (réseau de neurones informé par la physique)** représente directement la solution par un réseau $$u_\theta(x,t)$$ et, grâce à la différentiation automatique, inscrit le résidu de l'EDP dans la perte. Pour une équation de la forme $$u_t+\mathcal{N}[u]=0$$, on définit le résidu $$r_\theta=\partial_t u_\theta+\mathcal{N}[u_\theta]$$ et l'on minimise conjointement :

$$ \mathcal{L}=\underbrace{\frac{1}{N_d}\sum\big(u_\theta-u_{\text{obs}}\big)^2}_{\text{données/bords}}+\lambda\,\underbrace{\frac{1}{N_r}\sum r_\theta^2}_{\text{résidu physique}} $$

Le terme de résidu physique force le réseau à respecter l'équation même là où il n'y a pas de données ; si l'équation contient des paramètres inconnus, il suffit de les traiter comme des variables entraînables optimisées en même temps pour résoudre le problème inverse. **DeepONet (réseau d'opérateurs profond)** va plus loin et apprend un **opérateur** $$G:u\mapsto G(u)$$. Un « réseau branche » encode les valeurs de la fonction d'entrée $$u$$ en quelques points d'échantillonnage, un « réseau tronc » encode la coordonnée de requête $$y$$, et leur produit scalaire donne la sortie :

$$ G_\theta(u)(y)=\sum_{k=1}^{p} b_k(u)\,t_k(y) $$

Cette architecture s'appuie sur un résultat théorique garantissant l'approximation de tout opérateur non linéaire continu (théorème d'approximation universelle des opérateurs).

### Résultats

Les PINN peuvent résoudre le problème direct à partir de données clairsemées et bruitées tout en identifiant les coefficients inconnus de l'EDP, unifiant « résolution » et « inversion » dans une même optimisation. Une fois entraîné, DeepONet donne presque instantanément la solution complète pour une **nouvelle fonction d'entrée**, bien plus vite qu'une résolution numérique refaite à chaque fois, et montre une forte capacité de généralisation sur de nombreuses classes d'EDP paramétrées.

### Portée et perspectives

Ces deux travaux soudent le « calcul scientifique » et l'« apprentissage profond » : les PINN font obéir le réseau à la physique, DeepONet lui fait apprendre l'« opérateur de résolution » lui-même. Ils partagent le même fond que les séries temporelles — dans les deux cas, on apprend comment une dynamique évolue dans l'espace et le temps. Dans le prolongement de cette voie de l'« apprentissage d'opérateurs » sont rapidement apparus les opérateurs neuronaux de Fourier, qui effectuent une convolution globale dans le domaine fréquentiel ([../fno/](../fno/)), puis la prévision météorologique et climatique pilotée par les données ([../neural-weather/](../neural-weather/)).
