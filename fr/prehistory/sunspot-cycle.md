---
updated: "2026-06-11"
layout: history
lang: fr
era: "Récit de la préhistoire 13 · Observation · Méthode"
permalink: /fr/prehistory/sunspot-cycle/
title: "Le cycle de 11 ans des taches solaires (The Sunspot Cycle)"
lead: "Un astronome amateur, qui cherchait une planète cachée près du Soleil, compta pendant des années, jour après jour, les taches à la surface du Soleil — il ne trouva pas la planète, mais tomba sur un rythme resté caché pendant des millénaires."
math: false
prev: /prehistory/kelvin-tides/
next: /prehistory/
---

> Ceci est l'un des récits de la [préhistoire et des applications contemporaines](../), et aussi le pont qui mène de ces récits au [corps de l'histoire](../../history/).

### Dix-sept ans à compter des taches pour trouver une planète

Au début du XIXe siècle, le pharmacien allemand et astronome amateur Heinrich Schwabe nourrissait une idée fixe : il était convaincu qu'une planète inconnue se cachait à l'intérieur de l'orbite de Mercure (on l'appellera plus tard « Vulcain », Vulcan), et qu'elle projetterait un petit point noir en passant devant le disque solaire. Pour la surprendre, Schwabe installa sa lunette chaque jour de beau temps à partir de 1826, notant quotidiennement le nombre et la position des taches sur le disque du Soleil — et il le fit pendant dix-sept ans.

Vulcain ne se montra jamais (elle n'existait pas). Mais dans ces comptages quotidiens de taches, Schwabe tomba sur quelque chose d'inattendu. Plus tard, l'astronome suisse Rudolf Wolf rassembla, pondéra et normalisa les observations de divers lieux et époques pour constituer une série qui se poursuit encore aujourd'hui, le « **nombre de Wolf** » — devenue l'une des séries temporelles de long terme les plus importantes de l'histoire de l'astronomie.

### La difficulté : bruit ou cycle ?

La difficulté était la suivante : le nombre de taches varie d'un jour à l'autre de façon apparemment désordonnée. N'est-ce qu'une agitation aléatoire à la surface du Soleil, ou un cycle se cache-t-il en dessous ? Une ou deux années d'observations ne permettent pas de le dire ; seule la comparaison de comptages continus suffisamment longs pouvait faire émerger une régularité.

### La solution : découvrir un rythme « pas tout à fait exact »

En accumulant et en comparant des années de comptages continus, Schwabe annonça en **1843** que le nombre de taches solaires monte et redescend selon un cycle d'environ **11 ans**, passant de peu à beaucoup puis à peu. C'était une découverte remarquable. Mais on s'aperçut vite d'un problème : ce cycle n'est **pas « exact »** — tantôt neuf ans, tantôt quatorze ; et la hauteur des maxima varie elle aussi, tantôt forte, tantôt faible. Si l'on tente de l'ajuster par une sinusoïde de fréquence et d'amplitude fixes, on n'y parvient jamais vraiment.

### Ce que cela signifie pour les séries temporelles aujourd'hui

C'est l'exemple type du phénomène **quasi périodique** (quasi-periodic) : un rythme net, mais pas une période stricte, dont la durée comme l'intensité dérivent. Il met complètement en échec les modèles harmoniques déterministes — qui écrivent le signal comme une somme de quelques sinusoïdes fixes.

C'est justement cette énigme — « pourquoi le cycle dérive-t-il ? » — qui a directement suscité la réponse de Yule en 1927 : au lieu de voir le nombre de taches comme une sinusoïde plus du bruit, il le décrivit par un **processus aléatoire** — un autorégressif d'ordre 2, AR(2) —, où le nombre de taches de chaque année est déterminé par les valeurs des deux années précédentes plus un choc aléatoire. Le cycle qui dérive passait ainsi du statut de « défaut d'ajustement gênant » à celui de « conséquence naturelle d'une dynamique aléatoire ». Cette série des taches solaires est précisément l'héroïne du [chapitre 1 de l'histoire](../../history/01/) — c'est ici que la préhistoire passe le relais à l'analyse moderne des séries temporelles.
