---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 1950 · Informatique"
permalink: /fr/history/e/brown-ses/
title: "Le lissage exponentiel simple (Brown, années 1950)"
lead: "Le pistage radar comme le réapprovisionnement d'un entrepôt exigent de « calculer en marchant ». Avec une formule récursive qui n'occupe qu'un seul nombre, Brown comprime tout l'historique, pondéré par une décroissance exponentielle, en la meilleure estimation du présent."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 3 · Lissage exponentiel](../../03/).

### Contexte

Pendant et après la Seconde Guerre mondiale, Robert G. Brown travaille pour la marine américaine sur la conduite de tir et la défense antiaérienne, puis se tourne après la guerre vers la recherche opérationnelle, où il prévoit la demande d'un grand nombre d'articles en stock. Ces deux contextes partagent une même contrainte d'ingénierie : les données **arrivent une à une**, et les ressources de calcul et de stockage sont extrêmement limitées — le radar doit pister en temps réel, et un système de stocks doit gérer simultanément des milliers de pièces. Rappeler tout l'historique pour réajuster une courbe était impossible, faute de puissance de calcul comme de mémoire.

### Problème

Les méthodes classiques (moyenne mobile, ajustement par moindres carrés) doivent conserver une fenêtre, voire tout l'historique, et **traitent tous les échantillons passés sur un pied d'égalité**. Or, en réalité, plus une observation est récente, mieux elle représente le niveau réel actuel. **Peut-on concevoir une prévision qui ne conserve qu'« un seul nombre », se met à jour en O(1) à chaque nouvelle observation, et laisse automatiquement s'estomper l'influence des données anciennes ?**

### Autres courants de l'époque (et leurs limites)

- **Moyenne mobile simple** : moyenne à poids égaux des $$k$$ dernières périodes. Il faut garder $$k$$ valeurs en mémoire, et les poids sont tronqués « en falaise » — une donnée qui vient de sortir de la fenêtre tombe brusquement à zéro, ce qui rend la méthode lente à réagir et peu lisse.
- **Moindres carrés globaux / ajustement par régression** : précis, mais il faut conserver tout l'historique et tout recalculer par lots ; impossible en ligne, inadapté à un très grand nombre d'articles.
- **Méthode naïve (prendre la valeur précédente comme prévision)** : d'une simplicité extrême, mais sans aucune résistance au bruit : la moindre fluctuation ponctuelle se répercute directement sur la prévision.

### Méthode

Brown propose le **lissage exponentiel simple (SES)** : on maintient un « niveau » $$\ell_t$$ qui, à chaque période, se rapproche de la nouvelle observation dans une proportion fixe :

$$ \ell_t = \alpha\, x_t + (1-\alpha)\,\ell_{t-1},\qquad 0<\alpha<1 $$

où $$x_t$$ est l'observation courante et $$\alpha$$ le coefficient de lissage. La prévision à $$h$$ pas est simplement $$\hat{x}_{t+h}=\ell_t$$ (extrapolation plate). En déroulant la récurrence, on voit qu'il s'agit au fond d'une **moyenne à pondération exponentielle** :

$$ \ell_t = \alpha\sum_{j=0}^{t-1}(1-\alpha)^{j}\,x_{t-j} + (1-\alpha)^{t}\ell_0 $$

Le poids des observations anciennes décroît géométriquement selon $$(1-\alpha)^{j}$$ : il ne s'annule jamais, mais diminue rapidement. Plus $$\alpha$$ est grand, plus la méthode est réactive et colle aux nouvelles données ; plus il est petit, plus elle est lisse et résistante au bruit. Tout le calcul ne demande de conserver qu'un seul nombre, $$\ell_{t-1}$$, avec un coût de mise à jour constant en O(1).

### Résultats

Le SES s'est rapidement répandu dans la prévision des stocks et de la demande : mise en œuvre minimale, mémoire minimale, et comportement robuste sur les séries stationnaires sans tendance. Il a transformé la « pondération de l'historique » d'un problème d'ajustement par lots en une récurrence en ligne qui peut tourner indéfiniment. On a démontré plus tard que le SES est exactement la prévision optimale d'un **ARIMA(0,1,1)**, ce qui a donné à cette formule toute simple un solide fondement statistique.

### Portée et perspectives

Le SES a établi l'idée centrale de la famille du lissage exponentiel — **porter l'historique dans un état récursif et oublier le passé par des poids exponentiels**. Il a donné naissance à la [méthode de tendance linéaire de Holt](../holt/), capable de traiter la tendance, puis à [Holt–Winters](../holt-winters/), avec saisonnalité ; et sa posture en ligne, « maintenir un état, prévoir puis mettre à jour », fait écho au [filtre de Kalman](../kalman/) né à la même époque. Aujourd'hui, la surveillance par EWMA dans les systèmes de flux, le momentum et Adam en optimisation par gradient ne sont, au fond, rien d'autre que cette ligne de récurrence de Brown.
