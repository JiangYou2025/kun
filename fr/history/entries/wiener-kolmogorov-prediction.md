---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 1940 · Contrôle / communications"
permalink: /fr/history/e/wiener-kolmogorov-prediction/
title: "La prédiction optimale comme projection orthogonale (Wiener · Kolmogorov, années 1940)"
lead: "La meilleure façon linéaire de prédire l'avenir est de le projeter perpendiculairement sur « l'espace engendré par le passé » — une proposition géométrique qui unifie filtrage, lissage et prévision."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 2 · Fondements théoriques](../../02/).

### Contexte

En 1938, la [décomposition de Wold](../wold/) a révélé la structure des processus stationnaires, mais sans donner de réponse opérationnelle à la question « comment prédire au mieux l'avenir à partir du passé ». Dans les années 1940, Andreï Kolmogorov (en temps discret) et Norbert Wiener (en temps continu, étudiant le filtrage pour la conduite de tir antiaérienne pendant la guerre) résolvent presque simultanément et indépendamment le problème de la **prédiction linéaire optimale** des processus stationnaires. C'est la première fois que la géométrie de la théorie des probabilités (l'espace de Hilbert) et les besoins de filtrage de l'ingénieur s'ajustent parfaitement.

### Problème

Étant donné tout (ou partie) du passé d'un processus stationnaire $$\{X_t\}$$, il s'agit de prédire $$X_{t+h}$$ (prévision), ou de retrouver le signal vrai à partir d'observations bruitées (filtrage). **Parmi toutes les « combinaisons linéaires du passé », laquelle minimise l'erreur quadratique moyenne ?** Cette prédiction optimale a-t-elle une structure explicite calculable ?

### Les autres courants de l'époque (et leurs limites)

- **Extrapolation de courbes par moindres carrés** : ajuster un polynôme ou une sinusoïde à l'historique puis extrapoler. Cela suppose une forme fonctionnelle déterministe et ignore la structure de corrélation aléatoire du processus ; pour des séries aléatoires stationnaires, ce n'est ni optimal ni robuste.
- **Formules ad hoc récursives point par point** : des lisseurs conçus empiriquement par les ingénieurs (comme le lissage exponentiel simple). Efficaces, mais sans preuve d'optimalité, ils ne disent ni selon quel critère ils sont les meilleurs, ni quelle est l'ampleur de l'erreur.
- **Intuition purement fréquentielle** : choisir des bandes en regardant seulement le spectre de puissance. Cela capte une partie de l'information, mais sans intégrer la contrainte clé de la « causalité (on ne peut utiliser que le passé) » — or cette contrainte causale est précisément la difficulté centrale de la méthode de Wiener–Hopf.

### Méthode

L'idée maîtresse est géométrique. On considère l'ensemble des variables aléatoires de moyenne nulle et de variance finie comme un **espace de Hilbert**, muni du produit scalaire $$\langle X,Y\rangle=\mathbb{E}[XY]$$. Soit $$\mathcal{H}_t=\overline{\mathrm{span}}\{X_s:s\le t\}$$ le sous-espace fermé engendré par « le passé jusqu'à $$t$$ ». Alors la prédiction linéaire optimale $$\hat X_{t+h}$$, qui minimise l'erreur quadratique moyenne $$\mathbb{E}[(X_{t+h}-\hat X)^2]$$, est la **projection orthogonale** de $$X_{t+h}$$ sur $$\mathcal{H}_t$$ :

$$ \hat X_{t+h}=P_{\mathcal{H}_t}X_{t+h},\qquad \mathbb{E}\big[(X_{t+h}-\hat X_{t+h})\,X_s\big]=0\ \ \forall\,s\le t $$

La seconde relation est le **principe d'orthogonalité** : l'erreur de prédiction est décorrélée de toute l'information passée utilisée. Pour un processus (conjointement) gaussien, orthogonalité signifie indépendance, et la projection orthogonale coïncide exactement avec l'espérance conditionnelle $$\mathbb{E}[X_{t+h}\mid \mathcal{H}_t]$$ ; la solution linéaire optimale est donc aussi l'optimum global. Grâce à la représentation MA(∞) de la [décomposition de Wold](../wold/), la prédiction s'écrit comme une troncature sur les innovations ; et dans le domaine fréquentiel, la recherche du filtre optimal **causal** à partir d'un spectre bruité se ramène à la factorisation spectrale de l'**équation de Wiener–Hopf** (voir la [cybernétique de Wiener](../wiener-cybernetics/)).

### Résultats

La prédiction passe de « formules trouvées par tâtonnement » à « la solution unique obtenue par projection », assortie d'une variance d'erreur calculable. Un même cadre unifie trois tâches : la prévision ($$h>0$$), le filtrage (débruitage, $$h=0$$) et le lissage (en utilisant aussi bien le futur que le passé). La suite des innovations $$\varepsilon_t=X_t-P_{\mathcal{H}_{t-1}}X_t$$ devient la base naturelle du calcul récursif, et l'orthogonalité permet des mises à jour pas à pas sans recalculer tout l'historique.

### Portée et perspectives

« Estimation optimale = projection orthogonale = espérance conditionnelle » est devenu la colonne vertébrale de toute la théorie de l'estimation. Mais la théorie de Wiener–Kolmogorov exige un processus stationnaire, et souvent un passé infini et une décomposition fréquentielle ; sa mise en œuvre est lourde. C'est précisément pour traiter « le non-stationnaire, les données finies, la récurrence en temps réel » qu'en 1960 [Kalman](../kalman/) transpose cette même idée de projection dans l'**espace d'états**, obtenant le filtre de Kalman, récursif à chaque instant. De la conduite de tir de guerre au GPS, au SLAM et à la prévision de séquences d'aujourd'hui, l'ossature reste ce même pas : projeter perpendiculairement l'avenir sur le passé.
