---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1983 · Physique"
permalink: /fr/history/e/correlation-dimension/
title: "La dimension de corrélation (Grassberger · Procaccia, 1983)"
lead: "Un signal relève-t-il d'un chaos de faible dimension ou d'un bruit de grande dimension ? Comptez « combien de paires de points sont proches l'une de l'autre » dans l'espace des phases, et la dimension fractale émerge d'une loi d'échelle."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

Le [plongement par retards de Takens](../takens/) permet de reconstruire l'espace des phases à partir d'une série scalaire et de « dessiner » l'attracteur du [chaos](../lorenz-chaos/). Mais la reconstruction soulève aussitôt une question de discrimination plus aiguë : cet écheveau de trajectoires est-il un **chaos déterministe de faible dimension**, gouverné par quelques degrés de liberté, ou un **bruit aléatoire** fondamentalement **de grande dimension** ? Les deux peuvent paraître « désordonnés » à l'écran, et l'œil ne sait pas les distinguer. Il faut un indicateur quantitatif — la **dimension** de l'attracteur — pour dire combien de degrés de liberté effectifs il « occupe ». La géométrie fractale de [Mandelbrot](../mandelbrot/) fournissait le langage des « dimensions non entières », mais calculer cette dimension de façon fiable à partir de données expérimentales finies et bruitées restait un problème difficile.

### Problème

La dimension de comptage de boîtes (*box-counting dimension*) théorique exige de découper l'espace en petites cellules et de les compter ; dans un espace des phases de grande dimension, la quantité de données nécessaire explose exponentiellement avec la dimension, ce qui la rend presque inapplicable aux données expérimentales. **Peut-on concevoir un algorithme qui estime directement et robustement la dimension fractale à partir d'un nombre fini de points échantillonnés ?**

### Autres courants de l'époque (et leurs limites)

- **Dimension de comptage de boîtes** : définition claire, mais en grande dimension il faut un nombre astronomique de points, elle est sensible au bruit et converge difficilement sur des données expérimentales.
- **Inspection visuelle de l'attracteur / analyse spectrale** : juger à l'œil ou par le spectre de Fourier. Le spectre d'un chaos est large bande, de forme semblable à celui d'un bruit, et ne permet pas de distinguer quantitativement les dimensions.
- **Estimation des exposants de Lyapunov** : permet de dire s'il y a sensibilité aux conditions initiales, mais les algorithmes de l'époque étaient fragiles face au bruit et ne donnaient pas directement de dimension géométrique.

### Méthode

Grassberger et Procaccia proposent d'estimer la dimension par l'**intégrale de corrélation** (*correlation integral*). Dans l'espace des phases reconstruit de dimension $$m$$, on prend $$N$$ points $$\{\mathbf{y}_i\}$$ et l'on définit la proportion de paires de points distants de moins de $$r$$ :

$$ C(r) = \lim_{N\to\infty}\frac{2}{N(N-1)}\sum_{i<j}\Theta\big(r-\|\mathbf{y}_i-\mathbf{y}_j\|\big) $$

où $$\Theta$$ est la fonction échelon de Heaviside (1 si la distance est inférieure à $$r$$, 0 sinon). Pour un attracteur fractal, l'intégrale de corrélation suit, pour $$r$$ petit, une loi de puissance :

$$ C(r)\sim r^{D_2}\quad\Longrightarrow\quad D_2 = \lim_{r\to 0}\frac{\log C(r)}{\log r} $$

$$D_2$$ est la **dimension de corrélation**. En pratique, on trace $$\log C(r)$$ en fonction de $$\log r$$ et l'on prend la pente de la partie droite dans la zone d'échelle intermédiaire pour obtenir $$D_2$$. La clé de la discrimination : quand la dimension de plongement $$m$$ augmente, le $$D_2$$ d'un **chaos de faible dimension** converge vers une valeur finie (saturation des degrés de liberté), tandis que celui d'un **bruit aléatoire** croît indéfiniment avec $$m$$ sans saturer — c'est précisément l'empreinte qui permet de les distinguer.

### Résultats

L'algorithme de la dimension de corrélation, peu coûteux en calcul et bien moins gourmand en données que le comptage de boîtes, est vite devenu un outil standard de l'analyse non linéaire des séries temporelles ; il a été largement appliqué à la turbulence des fluides, aux lasers, aux électrocardiogrammes, aux électroencéphalogrammes et à bien d'autres signaux, pour juger s'ils cachent une structure déterministe de faible dimension. Avec les exposants de Lyapunov et le choix des paramètres de plongement, il forme la boîte à outils du chaos expérimental.

### Portée et perspectives

L'algorithme de Grassberger–Procaccia a fait passer la dimension fractale du statut de concept purement mathématique à celui de **grandeur physique mesurable à partir des données**, et a rendu empiriquement abordable la question « combien de degrés de liberté effectifs ce signal possède-t-il ? ». On a aussi reconnu plus tard ses limites : des données finies, le bruit et les corrélations à longue portée peuvent produire de fausses apparences de faible dimension, ce qui impose une interprétation prudente. Mais l'idée qu'il a établie — **remonter à la géométrie à partir des données par des lois d'échelle** — a eu une influence durable, et se prolonge dans les travaux modernes qui utilisent les méthodes d'espace des phases pour la prévision non linéaire, la mesure de complexité, et même la distinction entre déterminisme et aléa.
