---
updated: "2026-06-03"
layout: history
lang: fr
era: "Paradoxes du temps 6 · Physique · Thermodynamique"
permalink: /fr/paradoxes/maxwell-demon/
title: "Le démon de Maxwell"
lead: "Imaginez un petit démon posté près d'une trappe dans une cloison, qui ne laisse passer les molécules rapides que d'un côté et les lentes que de l'autre. Il ne fournit aucun travail, et pourtant un côté se réchauffe, l'autre se refroidit : il crée une différence de température à partir de rien — n'est-ce pas là une violation du second principe ?"
math: true
prev: /paradoxes/loschmidt/
next: /paradoxes/boltzmann-brain/
---

> Ceci est l'un des [paradoxes du temps](../).

Maxwell proposa cette expérience de pensée en 1867, dans le but de montrer que le second principe est statistique et non absolu. Mais le « démon » devint vite une véritable menace : il semblait capable de faire diminuer spontanément l'entropie.

La difficulté : le démon ne fait que « trier », ce qui ne semble rien coûter en énergie ; pourquoi ne pourrait-il pas obtenir gratuitement une différence de température (et, de là, faire tourner un mouvement perpétuel) ?

Des générations se sont succédé pour lui répondre. En 1929, Szilárd le simplifia en un moteur à une seule molécule et souligna que le démon doit **mesurer** l'état de la molécule, soupçonnant que le coût se cachait dans la mesure ; plus tard, Brillouin estima que c'est la mesure qui consomme de l'énergie. Mais la vraie réponse est plus subtile.

La réponse définitive est venue de la théorie de l'information et de la physique du calcul. En 1961, **Landauer** montra que la mesure peut en principe ne rien coûter, mais que la mémoire du démon est finie : tôt ou tard, il doit **effacer** ses enregistrements pour faire de la place, et l'effacement d'un bit d'information dissipe nécessairement au moins

$$E\ge k_B T\ln 2$$

d'énergie, en rejetant l'entropie correspondante dans l'environnement. En 1982, Bennett compléta l'argument : l'entropie que le démon fait diminuer est exactement compensée par celle produite lorsqu'il vide sa mémoire, et le second principe sort indemne.

**Le démon de Maxwell a fait entrer l'« information » dans la physique** — l'information n'est pas un symbole abstrait, et l'effacer coûte une énergie bien réelle. La limite de Landauer est aujourd'hui le plancher énergétique de tout calcul ; elle relie pour toujours le « bit » et le « joule ».
