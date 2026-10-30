---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1963 · Physique"
permalink: /fr/history/e/lorenz-chaos/
title: "Chaos déterministe et effet papillon (Lorenz, 1963)"
lead: "Trois équations simples suffisent à rendre la météo à long terme à jamais imprévisible avec précision. Lorenz découvre qu'un système déterministe peut être extrêmement sensible aux conditions initiales — l'effet papillon fixe une limite fondamentale à la prévisibilité."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Au début des années 1960, les météorologues croyaient généralement que, pourvu que les équations soient assez précises, les observations initiales assez denses et la puissance de calcul suffisante, le temps pourrait être prévu indéfiniment. C'était le prolongement du déterminisme laplacien : des équations déterminées donnent un avenir déterminé. Lorenz résout numériquement, sur l'un des premiers ordinateurs, un modèle très simplifié de convection atmosphérique, pour voir jusqu'où peut aller une prévision à long terme.

### Problème

Un hasard : il tronque une valeur intermédiaire à trois décimales et relance le calcul, en s'attendant à un résultat presque identique ; mais très vite, la trajectoire **diverge complètement** de l'originale. Le système est purement déterministe, sans aucun terme aléatoire, et pourtant il amplifie violemment une infime différence initiale. **Pourquoi un système déterministe devient-il, en pratique, imprévisible à long terme ?** La question frappe au cœur de la prévisibilité déterministe.

### Les autres courants de l'époque (et leurs limites)

- **Le déterminisme laplacien** : équations déterminées + conditions initiales exactes = un avenir entièrement calculable. Sa limite : il ignore la sensibilité exponentielle aux conditions initiales, alors qu'en pratique celles-ci ne sont jamais connues qu'approximativement.
- **L'intuition de la stabilité linéaire** : une petite perturbation n'aurait que de petites conséquences. C'est faux pour les systèmes non linéaires — l'erreur croît exponentiellement.
- **Attribuer l'imprévisibilité au bruit aléatoire** : croire que seul le hasard engendre l'incertitude. Lorenz montre que le déterminisme suffit à lui seul à produire l'imprévisibilité.

### Méthode

Le système de Lorenz ne compte que trois variables et trois équations différentielles ordinaires non linéaires :

$$ \dot{x}=\sigma(y-x),\qquad \dot{y}=x(\rho-z)-y,\qquad \dot{z}=xy-\beta z $$

Pour les paramètres classiques $$\sigma=10,\ \rho=28,\ \beta=8/3$$, la trajectoire ne converge ni vers un point fixe ni vers un cycle : elle s'enroule sur un **attracteur étrange** (l'attracteur de Lorenz) qui ne se recoupe jamais. Le mécanisme central est la dépendance sensible aux conditions initiales : deux trajectoires séparées initialement de $$|\delta_0|$$ s'écartent approximativement de manière exponentielle

$$ |\delta(t)|\approx |\delta_0|\,e^{\lambda t} $$

où $$\lambda>0$$ est le plus grand **exposant de Lyapunov**. Il donne directement l'échelle de temps de la prévisibilité : il faut environ $$1/\lambda$$ pour que l'erreur atteigne l'ordre de grandeur du système lui-même ; au-delà de cet horizon, aucune précision initiale ne suffit. C'est l'**effet papillon**.

### Résultats

Lorenz a montré que « déterministe mais imprévisible à long terme » n'est pas une contradiction, mais la situation normale des systèmes non linéaires. Ses trois équations sont devenues l'exemple emblématique de la théorie du chaos ; attracteurs étranges et exposants de Lyapunov positifs sont devenus des outils pour diagnostiquer le chaos, et l'on dispose désormais d'une explication quantitative de la limite intrinsèque des prévisions météorologiques.

### Portée et perspectives

Pour les séries temporelles, le chaos pose une dichotomie fondamentale : une suite d'apparence aléatoire provient-elle d'un processus stochastique de grande dimension, ou d'un chaos déterministe de faible dimension ? Y répondre exige de reconstruire l'espace des phases — c'est précisément le point de départ du [théorème de plongement de Takens](../takens/) (1981), qui montre que l'on peut reconstruire la géométrie de l'attracteur à partir d'une série d'observations univariée. L'exposant de Lyapunov, lui, fournit une borne supérieure de principe à la question « combien de temps cette série reste-t-elle prévisible ? ». Lorenz nous a fait comprendre que la limite de la prévision ne tient parfois ni aux données ni à la puissance de calcul : elle est inscrite dans la dynamique elle-même.
