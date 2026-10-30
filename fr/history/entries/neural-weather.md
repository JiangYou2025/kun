---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2022–23 · Physique"
permalink: /fr/history/e/neural-weather/
title: "La prévision météorologique neuronale : FourCastNet et GraphCast (2022–23)"
lead: "Depuis des décennies, la prévision météorologique repose sur des supercalculateurs qui résolvent laborieusement les équations de l'atmosphère. Si l'on entraîne plutôt un réseau de prévision spatio-temporelle sur des données de réanalyse, on peut aller des dizaines de milliers de fois plus vite, avec une meilleure précision."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Le pilier de la prévision météorologique moderne est la **prévision numérique du temps (PNT)** : on intègre dans le temps, sur une grille, les équations de la dynamique des fluides et de la thermodynamique de l'atmosphère, et chaque exécution consomme une puissance de calcul considérable sur de grands supercalculateurs. Parallèlement, des décennies d'observations ont été assimilées en **jeux de données de réanalyse** de haute qualité (comme ERA5), qui fournissent un état global de l'atmosphère sur le long terme, dense et régulier — exactement le matériau d'entraînement dont rêvent les modèles pilotés par les données.

### Problème

Précise, la PNT est néanmoins **coûteuse et lente** : la production de grandes prévisions d'ensemble et les mises à jour fréquentes sont limitées par la puissance de calcul. Une question aiguë en découle : **peut-on, par apprentissage profond, apprendre directement à partir des données de réanalyse l'application « état présent → état futur »**, tout en maintenant voire en dépassant la précision de la PNT, et ramener le coût d'une prévision de plusieurs heures de supercalculateur à quelques secondes sur un GPU ordinaire ?

### Les autres courants de l'époque (et leurs limites)

- **Les modèles numériques traditionnels (PNT)** : physiquement rigoureux et interprétables, mais extrêmement coûteux en calcul, ce qui limite les ensembles et la haute résolution.
- **Les premières corrections par apprentissage automatique** : elles se contentent d'un post-traitement des biais sur les sorties de la PNT, sans remplacer la prévision elle-même ; le gain est limité.
- **Les modèles purement pilotés par les données à petite échelle** : faute de structure physique globale cohérente et de stabilité à long terme, l'erreur explose après plusieurs pas de déroulement autorégressif.

### Méthode

Ces modèles traitent la prévision comme une **prévision spatio-temporelle autorégressive** : on apprend un opérateur $$G_\theta$$ qui fait avancer d'un pas de temps le champ d'état global de l'atmosphère $$X_t$$ à un instant donné (un tenseur de grande dimension empilant vent, température, humidité, etc. sur plusieurs niveaux de pression), puis on réinjecte la sortie dans le modèle pour dérouler une prévision à longue échéance :

$$ \widehat{X}_{t+\Delta t}=G_\theta(X_t),\qquad \widehat{X}_{t+k\Delta t}=G_\theta^{\,k}(X_t) $$

**FourCastNet** modélise des champs sphériques à haute résolution avec un opérateur neuronal de Fourier adaptatif (héritier de la convolution globale dans le domaine fréquentiel du [FNO](../fno/)) ; **GraphCast** discrétise la Terre en un graphe multi-échelle, fait circuler l'information entre les nœuds par un réseau de neurones sur graphes, et s'entraîne avec une perte sur plusieurs pas de déroulement pour limiter l'accumulation des erreurs :

$$ \mathcal{L}=\sum_{k=1}^{K} w_k\,\big\|\,G_\theta^{\,k}(X_t)-X_{t+k\Delta t}\,\big\|^2 $$

Tous deux sont entraînés de bout en bout sur ERA5 ; ils apprennent les lois d'évolution de l'atmosphère contenues dans les données, au lieu de résoudre explicitement les équations.

### Résultats

Sur un grand nombre de variables météorologiques clés et d'échéances de plusieurs jours, GraphCast **surpasse les modèles numériques opérationnels de l'époque**, alors qu'une prévision à 10 jours ne demande qu'environ une minute sur une seule machine — plusieurs ordres de grandeur plus vite que les modèles traditionnels ; FourCastNet produit lui aussi des prévisions globales à haute résolution pour un coût très faible, rendant les grandes prévisions d'ensemble bon marché et réalisables.

### Portée et perspectives

Les modèles météorologiques neuronaux démontrent que **la prévision spatio-temporelle pilotée par les données peut égaler, voire dépasser, les solveurs fondés sur les premiers principes sur un problème de physique aussi ardu que le système Terre**, en étant bien plus rapide et bien moins coûteuse. Ils portent la prévision des séries temporelles à l'échelle planétaire et, avec le [FNO](../fno/) et les [PINN/DeepONet](../pinn-deeponet/), dessinent les contours de l'« IA pour la science » ; ils s'orientent désormais vers la prévision de dynamiques spatio-temporelles plus vastes — climat, océans, séismes —, et jusqu'aux modèles de fondation du système Terre ([../foundation-models/](../foundation-models/)).
