---
updated: "2026-06-03"
layout: history
lang: fr
era: "Paradoxes du temps 2 · Philosophie"
permalink: /fr/paradoxes/achilles-tortoise/
title: "Achille et la tortue"
lead: "On laisse un peu d'avance à la tortue, et Achille aux pieds légers se lance à sa poursuite. Quand il atteint le point de départ de la tortue, celle-ci a déjà avancé un peu ; quand il arrive à ce nouveau point, elle a encore avancé d'un peu moins… Il semble devoir toujours rejoindre d'abord l'endroit où elle était « à l'instant », et ne jamais la rattraper. Pourtant, dans la réalité, il la dépasse en une enjambée — où est l'erreur ?"
math: true
prev: /paradoxes/zeno-arrow/
next: /paradoxes/twin/
---

> Ceci est l'un des [paradoxes du temps](../).

C'est le plus célèbre de la même série de Zénon, et il sert le même argument : « le mouvement est une illusion ». Sa force tient à ce que chaque étape du raisonnement paraît inattaquable : la poursuite est découpée en une infinité de petites phases consistant à « atteindre d'abord l'ancienne position ».

La difficulté n'est pas physique, elle tient à l'**infini** : pour rattraper la tortue, il faudrait apparemment accomplir une infinité d'étapes, et « une infinité d'étapes » signifie intuitivement « ne jamais finir ».

Les Anciens se sont arrêtés là. Aristote a fait remarquer que ces étapes en nombre infini se déroulent dans un laps de temps fini et ne demandent donc pas réellement un temps infini — mais, comme pour la flèche, il lui manquait l'arithmétique permettant d'« additionner une infinité de quantités de plus en plus petites » et d'obtenir un résultat fini.

La réponse est venue de la **convergence des séries infinies**. Supposons qu'Achille aille 10 fois plus vite que la tortue et qu'elle parte avec une avance $d$ : les durées de chaque étape forment une suite géométrique, dont la somme vaut

$$T=\frac{d/v}{\,1-1/10\,}=\frac{10}{9}\cdot\frac{d}{v}<\infty.$$

La somme des durées d'une infinité d'étapes est **finie**. Zénon a découpé une durée finie en une infinité de tranches, puis a glissé subrepticement de « une infinité de tranches » à « un temps infini ».

Dissiper ce paradoxe, c'est apprendre une chose profonde : **une somme d'une infinité de quantités peut parfaitement être un nombre fini.** C'est là le fondement des séries, des intégrales et de toute modélisation en temps continu.
