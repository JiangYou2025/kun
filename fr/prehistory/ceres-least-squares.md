---
updated: "2026-06-11"
layout: history
lang: fr
era: "Histoire de la préhistoire 9 · Méthode"
permalink: /fr/prehistory/ceres-least-squares/
title: "Cérès et les moindres carrés"
lead: "Le 1ᵉʳ janvier 1801, un astronome découvre un nouvel astre, « Cérès » ; au bout de seulement 40 jours d'observation, il se perd dans l'éclat du Soleil. Dans l'immensité du ciel étoilé, où va-t-il réapparaître ?"
math: true
prev: /prehistory/playfair-chart/
next: /prehistory/snow-cholera/
---

> Ceci est l'une des petites histoires de la page [Préhistoire et applications contemporaines](../).

### Découvert le jour de l'An, aussitôt perdu

Le 1ᵉʳ janvier 1801, à l'observatoire de Palerme, l'astronome italien Giuseppe Piazzi découvre une étoile faible qui se déplace lentement. Elle se trouve entre Mars et Jupiter — précisément là où les astronomes de l'époque cherchaient désespérément une planète qui « devait » exister mais qu'on n'avait jamais trouvée. Cet astre, qui sera baptisé **Cérès**, devient instantanément le centre d'attention de toute l'Europe.

Mais avant même qu'on ait pu bien l'observer, les ennuis commencent : Piazzi ne le suit qu'environ **41 jours** avant que Cérès ne passe trop près du Soleil et ne disparaisse dans l'éclat de l'aube et du crépuscule. Il n'a décrit dans le ciel qu'un arc d'environ 3 degrés. Lorsqu'il réapparaîtra, quelques mois plus tard, de l'autre côté du Soleil, personne ne saura où regarder. Une planète toute neuve risque d'être perdue à jamais.

### La difficulté : trop peu d'observations, une extrapolation trop risquée

La difficulté était la suivante : on ne disposait que d'une courte série de positions bruitées, alors que déterminer une orbite exige de fixer six paramètres orbitaux. Avec si peu de points, entachés d'erreurs, une telle extrapolation était extrêmement risquée : qu'un paramètre soit légèrement faussé, et la position prédite pouvait être à des lieues de la bonne — on aurait alors balayé en vain une mauvaise région du ciel avec le télescope, sans jamais retrouver l'astre.

### La solution : minimiser la somme des carrés des erreurs

Carl Friedrich Gauss, âgé de **24 ans** à peine, donna une réponse élégante. Son idée : ne pas exiger que l'orbite passe par chaque point observé (c'est impossible, et ce ne serait pas souhaitable, puisque chaque point est bruité), mais choisir le jeu de paramètres orbitaux $\theta$ qui minimise la somme des carrés des écarts entre positions prédites et **l'ensemble** des observations :

$$\hat\theta=\arg\min_{\theta}\sum_i\big(y_i-f(x_i;\theta)\big)^2.$$

Ce sont les **moindres carrés**. Toutes les observations « votent » ensemble pour le résultat, les erreurs aléatoires se compensent d'elles-mêmes, et l'on obtient l'orbite la plus robuste. Gauss calcula ainsi où Cérès devait réapparaître et envoya sa prédiction aux astronomes. Fin décembre 1801, von Zach et Olbers retrouvèrent effectivement, tout près de la position annoncée par Gauss, ce petit astre qu'on avait bien failli perdre. (À la même époque, le Français Legendre proposa indépendamment les moindres carrés et fut le premier à les publier officiellement, en 1805 ; Gauss affirma les avoir utilisés bien avant, d'où une célèbre querelle de priorité.)

### Ce qu'ils signifient pour les séries temporelles d'aujourd'hui

Les moindres carrés sont devenus dès lors l'outil universel pour **ajuster un modèle à une série bruitée, puis prédire**. Ils sont l'ancêtre commun de la régression linéaire, du [filtre de Kalman](../../history/04/) et de toutes les « minimisations d'une fonction de perte » de l'apprentissage automatique moderne — quelle que soit la complexité du modèle, l'idée de « régler les paramètres pour minimiser l'erreur totale entre prédictions et données » part d'ici. Un astéroïde qu'on a failli perdre a donné naissance au paradigme fondamental de l'ajustement de données.
