---
updated: "2026-06-11"
layout: history
lang: fr
era: "Récit de la préhistoire 11 · Méthode"
permalink: /fr/prehistory/jevons-sunspots/
title: "Jevons et la théorie des taches solaires (Jevons' Sunspot Theory)"
lead: "Dans les années 1870, un économiste de tout premier plan en était convaincu : les crises commerciales reviennent elles aussi tous les 11 ans environ, et ce sont les taches solaires qui tirent les ficelles. C'est l'exemple le plus célèbre de la préhistoire d'un « cycle vu là où il n'existe pas »."
math: false
prev: /prehistory/snow-cholera/
next: /prehistory/kelvin-tides/
---

> Ceci est l'un des récits de la [préhistoire et des applications contemporaines](../).

### Une coïncidence séduisante

William Stanley Jevons était l'un des meilleurs économistes de son temps. Il remarqua une coïncidence séduisante : les crises commerciales britanniques semblaient survenir à peu près tous les dix ans, et [les taches solaires suivent elles aussi un cycle d'environ 11 ans](../sunspot-cycle/). Deux cycles si proches, était-ce un hasard ? Il proposa hardiment une chaîne causale : taches solaires → influence sur le climat et la météo → effet sur les récoltes → variation du prix des céréales → déclenchement des cycles d'affaires et des crises. Une hypothèse grandiose, qui reliait d'un seul fil l'astronomie, la météorologie, l'agriculture et l'économie.

### La difficulté : quelques années de crise seulement

La difficulté tenait précisément au manque de données. Les années pouvant passer pour des « crises commerciales » se comptaient sur les doigts de la main. Décider, à partir de ces quelques points, s'il s'agissait d'un **cycle réel** et non d'une pure coïncidence relevait statistiquement de la mission impossible. Pire encore : lorsque les deux cycles ne coïncidaient pas, Jevons **ajustait** à plusieurs reprises la durée du cycle solaire qu'il retenait (tantôt 10,45 ans, tantôt une autre valeur), afin que les années de crise tombent au « bon » endroit.

### La solution (en réalité, une leçon) : un cycle sur mesure

Tout le problème est là : quand on s'autorise à retoucher la période et qu'on ne dispose que d'une poignée de points, on parvient **toujours** à faire « coller » une courbe. L'hypothèse de Jevons ne résiste pas à l'examen — échantillon trop petit, période ajustée par complaisance, chaque maillon de la chaîne causale fragile. La postérité en a fait un contre-exemple classique : sur une série courte, on « voit » très facilement des cycles qui n'existent pas, et l'on invente pour ce pseudo-cycle une belle histoire causale. Cette tentation de la **corrélation fallacieuse / du pseudo-cycle** reste aujourd'hui l'un des pièges les plus courants de l'analyse des séries temporelles.

### Ce que cela signifie pour les séries temporelles aujourd'hui

L'échec de Jevons fait ressortir un besoin pressant : disposer d'un **test objectif** qui dise si un « cycle » repéré dans une série est un vrai signal ou une simple fluctuation apparue par hasard dans le bruit. C'est précisément cette question qui, en 1898, a donné naissance au [périodogramme de Schuster](../) — le premier outil permettant de tester si une « périodicité cachée » est significative, et qui mène tout droit à l'analyse spectrale du XXe siècle. En ajoutant à l'ensemble des récits de la préhistoire la dimension de « ce qui était faux », la leçon est limpide : **aussi convaincant que paraisse un rythme, il faut d'abord se demander s'il résiste à un test**. C'est aussi la première leçon dont l'analyse des séries en [économie et finance](../../applications/finance/) doit toujours se souvenir.
