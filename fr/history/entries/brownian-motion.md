---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1905 · Physique"
permalink: /fr/history/e/brownian-motion/
title: "La théorie physique du mouvement brownien (Einstein · Smoluchowski, 1905)"
lead: "Pourquoi les grains de pollen s'agitent-ils sans fin dans l'eau ? Einstein répond : vous voyez de vos propres yeux des molécules invisibles qui les heurtent — un processus aléatoire microscopique, qui laisse une preuve irréfutable : le déplacement quadratique moyen est proportionnel au temps."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

En 1827, le botaniste Brown observe que de fines particules de pollen en suspension dans l'eau s'agitent sans cesse de façon désordonnée ; pendant près de quatre-vingts ans, personne ne sait l'expliquer. Au début du XX<sup>e</sup> siècle, la théorie atomique et moléculaire est encore contestée, et certains physiciens (comme Mach ou Ostwald) doutent même de la réalité des atomes. En 1905 (Einstein) et en 1906 (Smoluchowski), chacun de son côté propose une théorie quantitative du mouvement brownien, qui fait de cette agitation microscopique une preuve testable de l'existence des atomes.

### Problème

Si la particule est heurtée de toutes parts par les molécules d'eau, que la direction de chaque choc est aléatoire et que la force résultante est nulle en moyenne, **pourquoi la particule s'éloigne-t-elle continûment au lieu de rester sur place ?** De plus, son mouvement semble totalement dépourvu d'inertie — quelle relation lie donc déplacement et temps ? Cette relation peut-elle être mesurée expérimentalement et, en retour, permettre de « peser » la taille des molécules ?

### Autres courants de l'époque (et leurs limites)

- **Vision mécanique / trajectoire inertielle** : tenter de suivre la vitesse instantanée et la trajectoire de la particule comme celles d'une boule de billard. Sa limite : les collisions se produisent des milliers de milliards de fois par seconde, la vitesse instantanée est impossible à mesurer, et cette voie est impraticable.
- **Explication purement qualitative par l'agitation thermique** : admet que les chocs moléculaires en sont la cause, mais reste qualitative, sans prédiction quantitative vérifiable — elle ne peut donc pas trancher la question de la vérité de l'atomisme.
- La percée consiste à renoncer à suivre la trajectoire pour étudier plutôt une **statistique du déplacement** (le déplacement quadratique moyen), et à la relier au coefficient de diffusion, mesurable à l'échelle macroscopique.

### Méthode

Le basculement clé d'Einstein consiste à passer de la trajectoire aléatoire à l'**évolution de la densité de probabilité** : la distribution de la position de la particule $$\rho(x,t)$$ satisfait l'**équation de diffusion**

$$ \frac{\partial \rho}{\partial t}=D\,\frac{\partial^2 \rho}{\partial x^2} $$

dont la solution est une gaussienne de variance croissant linéairement avec le temps ; ainsi, **le déplacement quadratique moyen est proportionnel au temps** :

$$ \langle x^2\rangle = 2Dt $$

et le coefficient de diffusion est relié à la température, à la viscosité et à la taille des particules par la **relation d'Einstein** :

$$ D=\frac{k_B T}{6\pi\eta a} $$

où $$k_B$$ est la constante de Boltzmann, $$T$$ la température, $$\eta$$ la viscosité et $$a$$ le rayon de la particule. Le fait que $$\langle x^2\rangle\propto t$$ et non $$\propto t^2$$ est précisément l'empreinte statistique qui distingue « l'accumulation aléatoire sans inertie » du « mouvement uniforme ».

### Résultats

En 1908, Perrin vérifie expérimentalement avec précision $$\langle x^2\rangle = 2Dt$$ et en déduit le nombre d'Avogadro, **mettant un point final au débat sur la réalité des atomes** (Perrin recevra plus tard le prix Nobel). Un processus en apparence purement aléatoire est devenu une balance pour peser les molécules.

### Portée et perspectives

Le squelette mathématique du mouvement brownien — « accroissements indépendants, accroissements gaussiens, variance proportionnelle au temps » — a été construit rigoureusement par Norbert Wiener en 1923 pour devenir le **processus de Wiener** des probabilités, pierre angulaire de presque tous les processus aléatoires en temps continu. Il donne à la marche aléatoire financière proposée cinq ans plus tôt par [Bachelier](../bachelier/) un double fondement physique et mathématique ; il se prolonge vers l'[équation de Langevin](../langevin/), autre description du même phénomène, et vers les équations différentielles stochastiques, vers le [processus d'Ornstein–Uhlenbeck](../ornstein-uhlenbeck/), et, par l'intégrale d'Itô, vers l'analyse stochastique moderne. Quand on parle aujourd'hui de « modèles de diffusion » ou de « processus aléatoires », la source se trouve toujours à la surface de cette eau agitée.
