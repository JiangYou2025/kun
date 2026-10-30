---
updated: "2026-06-03"
layout: history
lang: fr
era: "Paradoxes du temps 1 · Philosophie"
permalink: /fr/paradoxes/zeno-arrow/
title: "La flèche de Zénon"
lead: "Une flèche en vol occupe, à chaque « instant », une position déterminée — puisqu'elle est immobile à chaque instant, comment un vol composé d'une infinité d'instants immobiles pourrait-il être un « mouvement » ?"
math: true
prev: /paradoxes/
next: /paradoxes/achilles-tortoise/
---

> Ceci est l'un des [paradoxes du temps](../).

À Élée, au V<sup>e</sup> siècle avant notre ère, Zénon prend la défense de son maître Parménide. Celui-ci soutenait que l'« être » véritable est un, immuable et immobile, et que le mouvement et le changement que nous percevons ne sont qu'illusion. La tâche de Zénon était de raisonner par l'absurde : il conçut une série de paradoxes destinés à faire se contredire le sens commun selon lequel « le mouvement existe réellement ».

La difficulté consiste à découper le temps en miettes : si le temps est fait de « maintenant » sans durée, alors, à chaque « maintenant », la flèche occupe une position fixe et ne parcourt aucune distance — elle est donc immobile. Mais comment une infinité d'« immobilités » additionnées pourrait-elle devenir un « vol » ?

Les contemporains ne purent répliquer que sur le plan des concepts. Aristote objecta que le temps n'est pas une enfilade de « maintenant » indivisibles, et que traiter le continu comme un empilement de points est en soi une erreur — mais il ne disposait d'aucun outil capable de traiter avec précision l'« infini » et l'« instantané », et le débat resta en suspens pendant près de deux mille ans.

La vraie réponse est venue du calcul infinitésimal. Newton et Leibniz au XVII<sup>e</sup> siècle, puis la rigueur apportée aux limites par Cauchy et Weierstrass au XIX<sup>e</sup>, ont donné de la « vitesse instantanée » une définition nette : ce n'est pas la distance parcourue pendant un instant (qui est évidemment nulle), mais le **taux de variation** de la position par rapport au temps

$$v(t)=\lim_{\Delta t\to 0}\frac{x(t+\Delta t)-x(t)}{\Delta t}=\frac{dx}{dt}.$$

Le mouvement ne se cache pas dans un instant isolé, mais dans la **tendance limite** autour de cet instant. Une question longtemps tenue pour un sophisme a fini par faire naître le langage le plus puissant dont l'humanité dispose pour décrire le changement — à l'origine de toutes les équations différentielles et, plus tard, de la modélisation des « taux de variation » dans les séries temporelles.
