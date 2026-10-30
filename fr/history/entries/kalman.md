---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1960 · Contrôle / communications"
permalink: /fr/history/e/kalman/
title: "Le filtre de Kalman et l'espace d'états (Kálmán, 1960)"
lead: "À partir d'observations bruitées, comment extraire en temps réel l'état véritable d'un système ? Kálmán propose une récurrence en deux temps, prédiction puis mise à jour, qui a permis à Apollo de retrouver le chemin du retour."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 4 · Filtre de Kalman](../../04/).

### Contexte

En 1960, Rudolf E. Kálmán publie « A New Approach to Linear Filtering and Prediction Problems ». L'aérospatiale et le guidage ont alors un besoin pressant d'estimer **en temps réel** la position et la vitesse d'un engin à partir de capteurs bruités. La génération précédente, le filtrage de Wiener–Kolmogorov, donnait une solution optimale dans le domaine fréquentiel, mais elle exigeait la stationnarité, nécessitait tout l'historique et se prêtait mal à une exécution récursive sur un calculateur embarqué. L'époque réclamait une méthode d'estimation capable de calculer au fil de l'eau avec un minimum de ressources.

### Problème

L'état véritable (position, vitesse) est invisible ; on ne dispose que d'observations indirectes polluées par du bruit (radar, gyroscope). **Comment, à chaque instant, fusionner de manière optimale la « prédiction a priori tirée de la dynamique du système » et « l'observation bruitée qui vient d'arriver », afin d'estimer l'état caché de façon récursive et en temps réel, tout en quantifiant l'incertitude de l'estimation ?**

### Les autres courants de l'époque (et leurs limites)

- **Filtrage de Wiener–Kolmogorov** : optimal en théorie, mais limité aux processus stationnaires, fondé sur le spectre et sur tout l'historique, non récursif, inadapté aux systèmes en ligne et variables dans le temps.
- **Moindres carrés récursifs (RLS)** : met à jour des paramètres en ligne, mais ne modélise pas explicitement la dynamique « évolution de l'état dans le temps + bruit de processus ».
- **Méthodes de type [lissage exponentiel](../holt/)** : récurrences efficaces, mais les coefficients de lissage sont fixés empiriquement, sans gain optimal déduit des statistiques du bruit, et sans covariance en sortie.

### Méthode

Kálmán décrit le système par un **espace d'états** : l'état caché $$x_t$$ évolue linéairement, l'observation $$z_t$$ est une application linéaire de l'état, et chacun porte un bruit gaussien :

$$ x_t = F x_{t-1} + w_t,\qquad z_t = H x_t + v_t,\quad w_t\sim\mathcal{N}(0,Q),\ v_t\sim\mathcal{N}(0,R) $$

L'estimation procède par une récurrence en deux temps. **Prédiction** (extrapolation de l'état et de la covariance selon la dynamique) :

$$ \hat{x}_{t}^{-}=F\hat{x}_{t-1},\qquad P_t^{-}=F P_{t-1}F^{\top}+Q $$

**Mise à jour** (correction par la nouvelle observation $$z_t$$), dont le cœur est le **gain de Kalman** $$K_t$$ :

$$ K_t = P_t^{-}H^{\top}\big(H P_t^{-}H^{\top}+R\big)^{-1},\qquad \hat{x}_t=\hat{x}_t^{-}+K_t\big(z_t-H\hat{x}_t^{-}\big) $$

puis mise à jour de la covariance $$P_t=(I-K_tH)P_t^{-}$$. Le gain $$K_t$$ est la clé : lorsque le bruit d'observation $$R$$ est faible (observation fiable), $$K_t$$ est grand et l'on se fie davantage aux nouvelles données ; lorsque l'incertitude de prédiction $$P_t^{-}$$ est faible, $$K_t$$ est petit et l'on se fie davantage à la prédiction du modèle. Le terme entre parenthèses $$z_t-H\hat{x}_t^{-}$$ est l'**innovation** — l'écart entre observation et prédiction. Sous les hypothèses linéaires et gaussiennes, c'est l'estimateur optimal au sens de l'**erreur quadratique moyenne minimale**.

### Résultats

Le filtre de Kalman a aussitôt servi à la navigation d'Apollo, au guidage inertiel et au pistage radar, et il s'est rapidement répandu dans le traitement du signal et l'automatique. Il ne conserve que l'état courant et sa covariance, pour un coût constant à chaque pas, tout en fournissant à la fois **une estimation ponctuelle et son incertitude** — un outil extrêmement pratique pour l'ingénieur. Pour les systèmes non linéaires sont apparus successivement le filtre de Kalman étendu (EKF) et le filtre de Kalman sans parfum (UKF).

### Portée et perspectives

Le filtre de Kalman a établi la récurrence « prédiction-mise à jour » comme paradigme général de l'estimation séquentielle, et le modèle espace d'états est devenu un cadre unificateur pour les séries temporelles — le [lissage exponentiel](../holt-winters/), les séries temporelles structurelles et l'ARIMA peuvent tous s'écrire en espace d'états, puis être estimés et évalués en vraisemblance par filtre de Kalman. Il est le miroir de la [programmation dynamique de Bellman](../bellman-dp/) (l'un pour l'estimation optimale, l'autre pour le contrôle optimal, réunis dans le LQG), et s'inscrit dans la lignée de l'idée d'« innovation » des [martingales de Doob](../doob-martingale/). Des engins spatiaux au SLAM, à la fusion de capteurs et au filtrage probabiliste d'aujourd'hui, le chemin du retour est toujours pavé de ces deux étapes.
