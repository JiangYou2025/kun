---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1993 · Contrôle / Communications"
permalink: /fr/history/e/particle-filter/
title: "Le filtre particulaire (Gordon et al., 1993)"
lead: "Quand un système n'est ni linéaire ni gaussien, les formules du filtre de Kalman ne tiennent plus. Alors renonçons à la solution exacte — lâchons une nuée de « particules » pondérées pour approcher la loi a posteriori."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Le [filtre de Kalman (1960)](../kalman/) est une étape majeure de l'estimation d'état, mais son élégance repose sur deux hypothèses fortes : un système linéaire et un bruit gaussien. La loi a posteriori reste alors gaussienne en permanence et deux grandeurs, la moyenne et la covariance, suffisent à la propager exactement. Or le pistage radar, les manœuvres de cibles ou la volatilité financière sont souvent **ni linéaires ni gaussiens**, et la loi a posteriori peut prendre des formes complexes, multimodales ou asymétriques. Le filtre de Kalman étendu (EKF) s'en tire tant bien que mal par linéarisation locale, mais il diverge face à une forte non-linéarité ou à la multimodalité.

### Problème

L'idéal du filtrage bayésien est de maintenir récursivement la loi a posteriori complète $$p(\mathbf{x}_t\mid \mathbf{y}_{1:t})$$, mais les intégrales qu'elle fait intervenir n'ont pas de forme close pour un modèle non linéaire et non gaussien général. **Comment représenter et mettre à jour une loi a posteriori quelconque, de façon approchée et récursive, sans rien supposer de sa forme ?** Il faut pour cela une représentation numérique capable d'exprimer n'importe quelle distribution et de se mettre à jour en ligne au fil des observations.

### Autres courants de l'époque (et leurs limites)

- **Filtre de Kalman étendu (EKF)** : on développe la non-linéarité au premier ordre de Taylor autour de l'estimation courante. Peu coûteux, mais l'erreur de linéarisation est grande en cas de forte non-linéarité, et il ne peut par nature décrire qu'une loi a posteriori gaussienne unimodale : il échoue fatalement face à la multimodalité.
- **Filtres sur grille / à masses ponctuelles** : on pose une grille fixe sur l'espace d'état pour intégrer numériquement. Faisable en basse dimension, mais le nombre de points explose exponentiellement avec la dimension (fléau de la dimension).
- **Filtres à somme de gaussiennes** : on approche la loi a posteriori par un mélange de gaussiennes. Plus souple que l'EKF, mais la gestion du nombre de composantes et de leurs paramètres est complexe, et l'on reste limité par les briques gaussiennes.

### Méthode

Le filtre particulaire (**Monte-Carlo séquentiel / filtre bootstrap**) approche la loi a posteriori par un ensemble d'échantillons pondérés (les particules) :

$$ p(\mathbf{x}_t\mid \mathbf{y}_{1:t})\;\approx\;\sum_{i=1}^{N} w_t^{(i)}\,\delta\big(\mathbf{x}_t-\mathbf{x}_t^{(i)}\big) $$

Chaque pas comporte deux phases. **Prédiction** : chaque particule est propagée par tirage selon le modèle de transition d'état, $$\mathbf{x}_t^{(i)}\sim p(\mathbf{x}_t\mid \mathbf{x}_{t-1}^{(i)})$$. **Mise à jour** : la nouvelle observation sert à repondérer les particules — plus une particule est compatible avec l'observation, plus son poids est grand :

$$ w_t^{(i)}\;\propto\;w_{t-1}^{(i)}\;p\big(\mathbf{y}_t\mid \mathbf{x}_t^{(i)}\big) $$

C'est l'**échantillonnage préférentiel**. Mais au fil du temps apparaît une « dégénérescence des poids » : quelques particules concentrent presque tout le poids, les autres ne servent plus à rien. Le coup décisif de Gordon et ses coauteurs est le **rééchantillonnage (resampling)** : on recopie les particules avec remise selon leurs poids, éliminant les échantillons de faible poids et multipliant ceux de fort poids, pour revenir à un ensemble équipondéré. Le cycle « échantillonnage préférentiel + rééchantillonnage » fait converger automatiquement la nuée de particules vers les régions de forte probabilité a posteriori.

### Résultats

Sur le pistage de cibles non linéaire et non gaussien, le filtre bootstrap surpasse nettement l'EKF et gère de façon robuste les lois a posteriori multimodales et les manœuvres brutales. Comme il suffit de savoir « tirer selon le modèle de transition et calculer la vraisemblance d'une observation », il n'impose presque aucune contrainte sur la forme du modèle : il a été rapidement adopté en radar, en navigation, en localisation robotique (SLAM), en économétrie, etc.

### Portée et perspectives

Le filtre particulaire a apporté la souplesse du Monte-Carlo à l'estimation d'état en ligne. Avec le [filtre de Kalman](../kalman/) et le [filtre de Kalman d'ensemble](../enkf/), il forme la lignée du filtrage bayésien moderne : de la « solution exacte linéaire gaussienne » à l'« approximation d'ensemble en grande dimension », puis à l'« approximation par échantillons d'une distribution quelconque ». Son paradigme échantillonner–pondérer–rééchantillonner reste aujourd'hui le moteur central de l'inférence bayésienne séquentielle, de la programmation probabiliste et même des filtres différentiables.
