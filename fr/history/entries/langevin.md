---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1908 · Physique"
permalink: /fr/history/e/langevin/
title: "La force aléatoire (Langevin, 1908)"
lead: "Einstein calculait comment se diffuse une loi de probabilité ; Langevin, lui, tient à écrire directement la force subie par la particule — un terme de frottement plus un terme aléatoire, trois lignes d'équation de Newton, d'où naîtront toutes les équations différentielles stochastiques."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

En 1905–1906, [Einstein et Smoluchowski](../brownian-motion/) avaient déjà expliqué le mouvement brownien par l'équation de diffusion, mais leur démarche — « trouver l'évolution de la densité de probabilité » — restait assez abstraite. En 1908, Paul Langevin propose une voie plus intuitive, « infiniment plus simple » selon ses propres mots : appliquer toujours la deuxième loi de Newton et écrire directement l'équation du mouvement d'une seule particule, en décomposant simplement en deux parties la force résultante des chocs moléculaires. Ce point de vue fait entrer l'aléatoire dans l'équation différentielle elle-même.

### Problème

Une particule dans un liquide subit d'innombrables chocs moléculaires. Ces chocs produisent à la fois une **résistance visqueuse systématique** (plus la particule va vite, plus elle est frappée de face, ce qui se manifeste comme un frottement) et des **fluctuations instantanées irrégulières** (le déséquilibre aléatoire des chocs). **Peut-on inscrire ces deux effets dans une même équation du mouvement, qui produise la diffusion tout en conservant la forme de la mécanique newtonienne ?** La difficulté : l'équation contient une force aléatoire discontinue partout, qu'on ne peut pas dériver au sens classique.

### Les autres courants de l'époque (et leurs limites)

- **Mécanique purement déterministe** : on écrit l'équation de Newton avec des forces extérieures régulières. Elle ne peut pas accueillir « des milliers de milliards de chocs aléatoires par seconde » : soit on ignore les fluctuations et l'on n'obtient pas de diffusion, soit on tente de suivre explicitement toutes les molécules, ce qui est impossible à calculer.
- **La démarche purement probabiliste d'Einstein** : ne parle que de l'évolution de la loi $$\rho(x,t)$$ et évite les trajectoires individuelles. Juste et puissante, elle ne dit pas directement « quelle force la particule subit à cet instant » ; l'image physique manque de concret et se généralise mal aux cas avec force extérieure ou dépendance en vitesse.
- Il manquait un pont : unifier **la dynamique d'une trajectoire aléatoire individuelle** et la diffusion macroscopique.

### Méthode

L'idée centrale de Langevin est de décomposer la force des chocs moléculaires en un terme de frottement déterministe et un terme de force aléatoire, ce qui donne l'**équation de Langevin** :

$$ m\,\frac{dv}{dt}=-\gamma\, v + \xi(t) $$

où $$-\gamma v$$ est le frottement visqueux proportionnel à la vitesse (traînée de Stokes $$\gamma=6\pi\eta a$$), et $$\xi(t)$$ une **force aléatoire (bruit blanc)** de moyenne nulle, vérifiant

$$ \langle \xi(t)\rangle=0,\qquad \langle \xi(t)\xi(t')\rangle = 2\gamma k_B T\,\delta(t-t') $$

Cette seconde relation est la **relation de fluctuation-dissipation** : les mêmes chocs moléculaires fournissent à la fois la dissipation (le frottement $$\gamma$$) et les fluctuations (l'intensité de la force aléatoire), et la température $$T$$ les verrouille l'une à l'autre. Langevin retrouve ainsi en quelques lignes d'algèbre $$\langle x^2\rangle = 2Dt$$, en parfait accord avec Einstein.

### Résultats

Pour le même mouvement brownien, Langevin fournit un « langage des forces » bien plus intuitif que l'équation de diffusion, qui se généralise aisément aux cas avec champ de force extérieur et avec inertie. La relation de fluctuation-dissipation est en outre l'un des théorèmes centraux de la physique statistique : elle relie quantitativement la dissipation observable aux fluctuations microscopiques.

### Portée et perspectives

L'équation de Langevin est le prototype physique des **équations différentielles stochastiques (EDS)** : une dérive déterministe plus un forçage par le bruit. Pour rendre mathématiquement rigoureux le terme de bruit blanc, il faudra la théorie de l'intégrale stochastique développée plus tard par Itô et Stratonovich ; dans la limite suramortie, elle donne directement le [processus d'Ornstein–Uhlenbeck](../ornstein-uhlenbeck/), dont la discrétisation est exactement un AR(1), traduisant « frottement + bruit thermique » en « [autorégression](../yule-ar/) ». De la dynamique moléculaire à la modélisation de la volatilité financière, jusqu'à l'échantillonnage « score + bruit » des modèles génératifs de diffusion d'aujourd'hui (l'échantillonnage par dynamique de Langevin), tout cela est l'écho de cette équation de 1908.
