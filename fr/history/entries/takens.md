---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1981 · Physique"
permalink: /fr/history/e/takens/
title: "Le théorème de plongement par retards (Takens, 1981)"
lead: "Vous n'avez mesuré qu'une seule variable du système, mais vous voulez retrouver toute sa dynamique ? En assemblant les « quelques pas passés » de cette unique série scalaire en coordonnées, on reconstruit un espace des phases équivalent à celui du système d'origine."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

[Le chaos de Lorenz](../lorenz-chaos/) a révélé que de simples systèmes non linéaires déterministes peuvent produire des comportements complexes d'apparence aléatoire, dont l'évolution à long terme est gouvernée par un **attracteur étrange** de faible dimension. Le langage naturel pour étudier ces systèmes est l'**espace des phases** — l'espace géométrique engendré par toutes les variables d'état, l'attracteur étant l'objet géométrique où s'enroulent les trajectoires. Mais en expérience, on ne peut souvent mesurer qu'**une seule** observable du système (la lecture au cours du temps d'une température ou d'une tension), sans accès au vecteur d'état complet. L'observation d'une seule variable serait-elle donc impuissante à atteindre la dynamique multidimensionnelle sous-jacente ?

### Problème

Soit une série temporelle scalaire $$x_t$$, ombre projetée, par une certaine fonction d'observation, d'un système dynamique inconnu de dimension élevée (ou faible). **Peut-on, à partir de cette seule série, reconstruire un espace des phases et un attracteur topologiquement équivalents à ceux du système d'origine ?** Intuitivement, de l'information semble perdue — le multidimensionnel a été écrasé en une dimension.

### Les autres courants de l'époque (et leurs limites)

- **Analyse harmonique / spectrale** : caractériser la série par son spectre de Fourier. Efficace pour les oscillations linéaires, mais le spectre d'un signal chaotique est continu et à large bande ; le domaine fréquentiel ne laisse voir aucune structure déterministe et fait prendre le chaos pour du bruit.
- **Mesure directe par plusieurs sondes** : mesurer simultanément plusieurs variables pour construire le vecteur d'état. Souvent physiquement irréalisable, et l'on ne sait pas lesquelles mesurer, ni combien suffisent.
- **Modélisation ARMA statistique** : elle suppose un mécanisme stochastique linéaire et ne peut saisir la géométrie d'un attracteur non linéaire déterministe.

### Méthode

Takens démontre le théorème de plongement par retards (*delay embedding theorem*). On construit des vecteurs à partir des **coordonnées retardées** de la série à une variable :

$$ \mathbf{y}_t = \big(x_t,\; x_{t-\tau},\; x_{t-2\tau},\; \dots,\; x_{t-(m-1)\tau}\big) $$

où $$\tau$$ est le délai et $$m$$ la dimension de plongement. Le théorème affirme que, pour un système dynamique lisse et une fonction d'observation générique (« générique » au sens mathématique), dès que la dimension de plongement est assez grande — c'est-à-dire

$$ m > 2d $$

($$d$$ étant la dimension de l'attracteur d'origine) — l'application en coordonnées retardées est un **plongement** : la trajectoire reconstruite $$\{\mathbf{y}_t\}$$ est **difféomorphe** à l'attracteur du système d'origine. Cela signifie que les invariants géométriques et dynamiques — dimension, exposants de Lyapunov, structure fractale — sont préservés. Intuitivement, « la valeur actuelle d'une variable plus quelques-unes de ses valeurs passées » contient déjà, implicitement, l'information sur les autres variables : le couplage non linéaire permet à l'histoire de remplacer les composantes d'état non observées.

### Résultats

Le plongement par retards a transformé la reconstruction abstraite de l'espace des phases en algorithme opérationnel : à partir d'un seul signal expérimental, on peut tracer l'attracteur, estimer sa dimension et ses indicateurs de chaos. Il a donné naissance à toute une panoplie d'outils d'analyse non linéaire des séries temporelles, dont la [dimension de corrélation de Grassberger–Procaccia](../correlation-dimension/) est la méthode emblématique pour calculer une dimension fractale dans l'espace des phases reconstruit.

### Portée et perspectives

Le théorème de Takens est le fondement théorique permettant de « voir une dynamique multidimensionnelle à partir d'une observation unidimensionnelle » ; il a fait descendre la théorie du chaos jusqu'aux données réelles — électrocardiogrammes, électroencéphalogrammes, turbulence, lasers, climat ont tous été analysés grâce à lui. L'idée de construction par coordonnées retardées reste vivace : la prévision non linéaire par vecteurs de retards, la reconstruction de dynamiques par calcul par réservoir (*reservoir computing*), jusqu'aux modèles profonds de séries temporelles qui prennent une fenêtre glissante en entrée, reposent au fond sur ce pas de Takens — **reconstruire, à partir du passé, l'état dans lequel on se trouve à présent**.
