---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1927 · Mathématiques"
permalink: /fr/history/e/slutsky/
title: "Les pseudo-cycles qui émergent des sommes aléatoires (Slutsky, 1927)"
lead: "Additionnez sans relâche, par moyennes mobiles, une suite de bruit pur, et voici que surgissent des fluctuations étonnamment semblables aux cycles économiques. Par ce contre-exemple, Slutsky lance un avertissement : le cycle que vous voyez n'est peut-être qu'un mirage laissé par le filtrage."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 1 · Autorégression](../../01/).

### Contexte

Dans les années 1920, les économistes sont fascinés par le « cycle des affaires » : crises, prospérité et dépressions semblent revenir selon un certain rythme, et beaucoup croient qu'une période bien déterminée s'y cache, qui n'attend que d'être découverte. Dans le traitement statistique, on a l'habitude d'appliquer aux données brutes une **moyenne mobile** pour « lisser » les perturbations de court terme et faire ressortir tendance et cycle. Au même moment, [Yule](../yule-ar/) explique par l'autorégression la quasi-périodicité des taches solaires. Le statisticien ukrainien Slutsky aborde la même énigme par l'autre bout.

### Problème

Un soupçon aigu : ces « cycles » observés et nommés encore et encore sont-ils une propriété du système économique lui-même, ou bien **ont-ils été fabriqués par nos méthodes de traitement** ? Les opérations courantes — lissage, différenciation, moyenne mobile — pourraient-elles engendrer des fluctuations à partir de rien ? Si c'est le cas, une multitude de travaux qui « découvrent des cycles » reposent sur du sable.

### Les autres courants de l'époque (et leurs limites)

- **L'école des cycles déterministes** : elle croit à l'existence de cycles des affaires de durée fixe, que l'on cherche à capturer par des harmoniques ou par le périodogramme. Sa limite : elle traite le traitement des données comme une lentille neutre et ignore que le filtrage lui-même façonne le signal.
- **La vision autorégressive de [Yule](../yule-ar/) (la même année)** : les cycles proviennent d'une structure interne de rappel excitée par le bruit. Profonde, mais elle insiste sur le fait que « le système possède un véritable quasi-cycle » ; elle complète, plutôt qu'elle ne remplace, l'idée de Slutsky selon laquelle « le cycle peut n'être qu'un pur artefact ».
- Ce n'est qu'ensemble qu'elles sont complètes : un cycle peut provenir d'une dynamique réelle comme du filtrage — il faut savoir les distinguer.

### Méthode

Slutsky prend une suite de **nombres aléatoires indépendants et identiquement distribués** (du bruit pur) et se contente d'en faire des sommes pondérées linéaires, obtenant une nouvelle série :

$$ X_t = \sum_{j=0}^{q} b_j\,\varepsilon_{t-j},\qquad \varepsilon_t \sim \mathrm{WN}(0,\sigma^2) $$

C'est précisément la structure que l'on appellera plus tard **MA(q)** (moyenne mobile). La découverte clé : même si l'entrée ne contient aucun cycle, la sortie $$X_t$$ présente des fluctuations lisses et régulières. L'explication se trouve dans le domaine fréquentiel : la sommation équivaut à un **filtre passe-bas**, dont la réponse en fréquence

$$ H(\omega) = \sum_{j=0}^{q} b_j\, e^{-i\omega j} $$

atténue les hautes fréquences et amplifie une certaine bande de fréquences basses et moyennes ; le spectre de puissance plat du bruit blanc est ainsi « façonné » en un spectre présentant un pic, comme s'il existait une période dominante. Slutsky démontre ainsi qu'**un filtrage linéaire peut faire « émerger » un quasi-cycle de l'absence de cycle**, phénomène que la postérité a appelé l'**effet Slutsky–Yule**.

### Résultats

La conclusion est aussi troublante qu'éclairante : les prétraitements courants comme la moyenne mobile ou la différenciation introduisent tous des pseudo-cycles, et nombre de « cycles des affaires » rapportés avec solennité pourraient bien n'être que des artefacts de filtrage. C'est un signal d'alarme pour toute la recherche empirique sur les cycles : avant de proclamer la découverte d'un cycle, il faut exclure la contribution des méthodes de traitement.

### Portée et perspectives

Slutsky et [Yule](../yule-ar/), partis de deux extrémités, ont posé ensemble la vision moderne des processus stochastiques linéaires : une série est le produit d'un bruit blanc façonné par un système linéaire. Les structures MA et AR seront unifiées en 1938 par la [décomposition de Wold](../wold/), puis intégrées au cadre ARMA/ARIMA de [Box–Jenkins](../box-jenkins/). L'héritage le plus durable est une vigilance méthodologique : face à tout « cycle » ou « signal », se demander d'abord — cela vient-il des données elles-mêmes, ou de mon traitement ? Cette prudence a traversé un siècle de pratique de l'analyse spectrale et du filtrage.
