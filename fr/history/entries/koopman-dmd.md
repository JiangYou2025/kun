---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2005–10 · Physique"
permalink: /fr/history/e/koopman-dmd/
title: "L'opérateur de Koopman et la DMD (Mezić · Schmid, 2005–10)"
lead: "Une dynamique non linéaire peut-elle « devenir linéaire » ? Le prix à payer est de monter en dimension infinie : on fait agir l'opérateur sur les fonctions d'observation, puis la DMD extrait des données ses modes cohérents et ses fréquences."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

La difficulté des systèmes dynamiques non linéaires tient à l'absence de principe de superposition : spectres, modes, fréquences — les armes du monde linéaire — semblent inutilisables. Pourtant, dès 1931, **Koopman** avait montré que tout système dynamique (même fortement non linéaire) correspond à un opérateur **linéaire** agissant sur l'**espace des fonctions d'observation** — au prix d'un espace généralement **de dimension infinie**. Cette idée sommeille pendant des décennies, jusqu'à sa renaissance en 2004–2005, lorsque Mezić et d'autres la relient à l'analyse spectrale et aux méthodes fondées sur les données ; en 2008–2010, Schmid propose la **décomposition en modes dynamiques (DMD)**, un algorithme pratique pour extraire des modes cohérents à partir d'instantanés d'écoulements de grande dimension. Les deux courants convergent rapidement et deviennent un outil de choix pour analyser des séries spatio-temporelles de grande dimension en mécanique des fluides, en climatologie, en neurosciences, etc.

### Problème

Expériences et simulations produisent des masses de séries de grande dimension (par exemple des millions de degrés de liberté par image d'écoulement), souvent dominées par un petit nombre de **structures cohérentes**. Comment extraire des données, **sans recourir aux équations gouvernantes**, les **modes spatiaux, les taux de croissance ou de décroissance et les fréquences d'oscillation** de ces structures ? La [PCA/EOF](../../../foundations/pca/) classique ne fait que classer par énergie, sans signification dynamique ; l'analyse de Fourier suppose stationnarité et périodicité globale. Il faut une décomposition qui **lie modes spatiaux et fréquences temporelles**.

### Les autres courants de l'époque (et leurs limites)

- **POD/PCA (décomposition orthogonale aux valeurs propres)** : fournit la base de faible dimension optimale au sens de l'énergie (variance), mais ses modes mélangent plusieurs fréquences et ne portent aucune information dynamique (taux de croissance, fréquence).
- **Spectre de Fourier global** : donne les fréquences, mais ses modes sont des sinusoïdes sur tout le champ, incapables de décrire des structures cohérentes locales, et la stationnarité est requise.
- **Analyse aux valeurs propres fondée sur les équations** : exacte, mais elle exige des équations gouvernantes connues et linéarisables ; impuissante face à des données pures ou à des systèmes inconnus.

### Méthode

Soit un état $$ x \in \mathbb{R}^n $$ évoluant selon $$ x_{t+1} = F(x_t) $$ (où $$ F $$ peut être non linéaire). L'**opérateur de Koopman** $$ \mathcal{K} $$ agit sur les fonctions d'observation $$ g $$ de sorte que leur évolution le long des trajectoires devient **linéaire** :

$$ (\mathcal{K} g)(x) = g\big(F(x)\big) $$

Bien que $$ \mathcal{K} $$ soit linéaire, il est de dimension infinie ; ses valeurs propres, fonctions propres et modes décrivent la dynamique globale du système. La **DMD** en est une approximation de dimension finie fondée sur les données : on rassemble les matrices d'instantanés $$ X=[x_1,\dots,x_{m-1}] $$ et $$ X'=[x_2,\dots,x_m] $$, puis on cherche le meilleur opérateur linéaire $$ A $$ tel que

$$ X' \approx A\,X,\qquad A = X'\,X^{+} $$

($$ X^{+} $$ est la pseudo-inverse ; en pratique, on résout après réduction de dimension par SVD). On décompose ensuite $$ A $$ en éléments propres $$ A\phi_j=\lambda_j\phi_j $$ : chaque **mode DMD** $$ \phi_j $$ est une structure spatiale, et sa valeur propre $$ \lambda_j $$ fournit à la fois le **taux de croissance** et la **fréquence d'oscillation** — $$ |\lambda_j| $$ détermine la décroissance ou la croissance, $$ \arg\lambda_j $$ la fréquence. La série est alors reconstruite comme

$$ x_t \approx \sum_j \phi_j\, \lambda_j^{\,t}\, b_j $$

Les données spatio-temporelles de grande dimension se décomposent ainsi en une superposition « mode spatial × évolution temporelle exponentielle complexe » — exactement l'analyse modale du monde linéaire, mais appliquée aux données d'un système non linéaire.

### Résultats

La DMD permet d'extraire automatiquement les **modes cohérents dominants et leurs fréquences** de séries de grande dimension issues de la turbulence, de la combustion, du climat ou de l'EEG, sans équations gouvernantes. Elle a engendré toute une famille d'extensions : Extended DMD, Hankel-DMD (pour les observations courtes), DMDc avec contrôle, ainsi que des versions profondes où un réseau de neurones apprend des sous-espaces invariants de Koopman. En ingénierie, elle remplit à la fois trois fonctions : réduction de dimension, analyse spectrale et prévision à court terme.

### Portée et perspectives

Le caractère révolutionnaire de Koopman–DMD tient à l'**échange de la dimension contre la linéarité** : au lieu d'affronter de front la non-linéarité dans l'espace d'états d'origine, on profite de tous les outils spectraux des opérateurs linéaires dans l'espace de grande (voire infinie) dimension des fonctions d'observation. Cela fait écho à l'esprit des [réseaux à état d'écho](../echo-state-network/) (« déploiement aléatoire en grande dimension + lecture linéaire ») et des méthodes à noyaux. C'est aujourd'hui l'un des paradigmes centraux des systèmes dynamiques fondés sur les données, de la modélisation interprétable des séries temporelles et de l'analyse des systèmes chaotiques ([Lorenz](../lorenz-chaos/)), et cela continue d'éclairer la question fondamentale : « comment trouver un bon système de coordonnées pour un système non linéaire ? »
