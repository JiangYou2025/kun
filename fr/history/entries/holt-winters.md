---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1960 · Contrôle / communications"
permalink: /fr/history/e/holt-winters/
title: "Le lissage saisonnier de Holt–Winters (Winters, 1960)"
lead: "Chaque année, les ventes bondissent à Noël. Winters ajoute au « niveau + tendance » une récurrence saisonnière, et le lissage exponentiel apprend à fêter les fêtes."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 4 · Filtre de Kalman](../../04/).

### Contexte

En 1960, Peter R. Winters publie « Forecasting Sales by Exponentially Weighted Moving Averages », qui pousse un cran plus loin la méthode de tendance linéaire de son collègue [Holt](../holt/). L'une des structures les plus tenaces de la demande commerciale est la **saisonnalité** : le commerce de détail grimpe en fin d'année, la consommation d'énergie suit le chaud et le froid, la fréquentation suit un cycle hebdomadaire. Les générations précédentes de lissage exponentiel savaient suivre le niveau et la tendance, mais restaient démunies face à ces fluctuations périodiques.

### Problème

Le [SES](../brown-ses/) suit le niveau et [Holt](../holt/) y ajoute la tendance, mais tous deux supposent que la série ne présente pas de hausses et de baisses récurrentes de période fixe. Face à des ventes saisonnières, ils traitent les fluctuations régulières de chaque année comme du bruit et corrigent sans cesse dans un sens puis dans l'autre : la prévision ne sait ni monter en haute saison ni descendre en basse saison. **Peut-on, tout en conservant la récurrence en ligne du lissage exponentiel, apprendre explicitement et extrapoler un motif saisonnier de longueur $$m$$ ?**

### Les autres courants de l'époque (et leurs limites)

- **[Méthode de tendance linéaire de Holt](../holt/)** : suit niveau et tendance, mais sans terme saisonnier, d'où un biais systématique sur les séries périodiques.
- **Régression sur indicatrices saisonnières / régression harmonique** : exprime la saisonnalité, mais suppose en général une forme saisonnière fixe et exige un ajustement par lots ; il est difficile de laisser le motif saisonnier évoluer lentement dans le temps.
- **Désaisonnaliser puis prévoir (par exemple X-11)** : traitement en deux temps, procédure lourde, et l'ajustement n'est pas aligné sur l'objectif de prévision.

### Méthode

En plus du niveau $$\ell_t$$ et de la tendance $$b_t$$ de Holt, Winters ajoute un ensemble de **facteurs saisonniers** $$s_t$$ (période $$m$$) : trois récurrences au total, avec trois coefficients de lissage $$\alpha,\beta,\gamma$$. Dans la **forme additive** (amplitude saisonnière à peu près constante) :

$$ \ell_t = \alpha\,(x_t-s_{t-m}) + (1-\alpha)(\ell_{t-1}+b_{t-1}) $$

$$ b_t = \beta\,(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1},\qquad s_t = \gamma\,(x_t-\ell_t) + (1-\gamma)\,s_{t-m} $$

La prévision additionne les trois composantes et les extrapole : $$\hat{x}_{t+h}=\ell_t+h\,b_t+s_{t-m+((h-1)\bmod m)+1}$$. Lorsque l'amplitude saisonnière croît proportionnellement au niveau, on passe à la **forme multiplicative** — la mise à jour du niveau utilise $$x_t/s_{t-m}$$, celle de la saison $$x_t/\ell_t$$, et la prévision se compose par multiplication : $$\hat{x}_{t+h}=(\ell_t+h\,b_t)\,s_{t-m+\dots}$$. Chaque facteur saisonnier est mis à jour une fois toutes les $$m$$ périodes, ce qui permet au motif saisonnier de s'adapter lentement aux données.

### Résultats

Holt–Winters est devenu la référence classique pour les séries avec tendance et saisonnalité : simple à mettre en œuvre, efficace en ligne, interprétable (niveau, tendance et saison se lisent d'un coup d'œil), il reste utilisé aujourd'hui dans la prévision du commerce de détail, de l'énergie et des opérations. Il complète la famille du lissage exponentiel en un trio « niveau-tendance-saison ».

### Portée et perspectives

Holt–Winters marque la maturité du lissage exponentiel ; il a ensuite été intégré au **cadre espace d'états ETS (erreur-tendance-saison)** unifié — chaque variante correspond à un modèle espace d'états, dont on peut estimer la vraisemblance et les intervalles de prévision par [filtre de Kalman](../kalman/), en écho direct au thème de ce chapitre. De l'ETS au TBATS à saisonnalités multiples, jusqu'aux références par défaut des outils de prévision modernes, l'idée de « lisser composante par composante, chacune avec sa propre récurrence » reste l'étalon qui permet de juger si un modèle complexe est réellement utile.
