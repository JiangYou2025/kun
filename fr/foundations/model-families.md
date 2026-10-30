---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/model-families/
title: "Familles de modèles"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble du cours de base](../)

Les **familles de modèles** désignent les grandes catégories de modèles de l'[apprentissage automatique](../ml/) — modèles linéaires, arbres de décision et ensembles, SVM, plus proches voisins kNN, [réseaux de neurones](../neural-network/). Chaque famille repose sur des **hypothèses** différentes et a donc ses propres terrains de prédilection. Cette leçon n'approfondit aucun modèle en particulier : elle vous aide à dresser une « **carte** » pour saisir l'idée centrale de chaque famille, ses forces et ses faiblesses, et savoir quand la choisir.

## Intuition

Les débutants demandent souvent : « Quel est le meilleur modèle ? » La réponse : **il n'y a pas de « meilleur modèle », seulement un « modèle le mieux adapté à la tâche »**.

Derrière cette réponse se trouve un théorème célèbre, le **théorème du « pas de repas gratuit » (No Free Lunch Theorem)** : si l'on fait la moyenne sur tous les problèmes possibles, deux [algorithmes](../algorithms/) quelconques ont les mêmes performances. Autrement dit, si un modèle excelle sur une tâche, c'est parce que ses **hypothèses (inductive bias, biais inductif)** correspondent justement aux régularités réelles de cette tâche ; sur une autre tâche, ces mêmes hypothèses peuvent devenir un handicap.

La bonne attitude n'est donc pas de « chercher la solution miracle », mais de **comprendre ce que suppose chaque famille de modèles**, puis de vérifier si vos données satisfont ces hypothèses. Passons maintenant en revue chaque famille.

## Un exemple concret : plusieurs familles sur une même carte

Imaginez une tâche de classification binaire — des points rouges et des points bleus dans le plan, qu'il faut séparer par une frontière. Chaque famille de modèles trace une frontière de forme complètement différente :

- un **modèle linéaire** trace une **droite** (un hyperplan en grande dimension) ;
- un **arbre de décision** trace un **escalier de segments horizontaux et verticaux** (des blocs rectangulaires alignés sur les axes) ;
- un **SVM** muni d'une fonction noyau peut tracer une **courbe lisse**, en cherchant en outre à éloigner le plus possible la frontière des deux classes ;
- la frontière du **kNN** **épouse les données** en serpentant, se courbant partout où se trouvent des points ;
- un **réseau de neurones** peut tracer une **courbe arbitrairement complexe**, pourvu qu'il y ait assez de données.

Les mêmes données, cinq « visions du monde ». Voilà l'image la plus intuitive des « familles de modèles ».

## Visite guidée des familles de modèles

### Modèles linéaires

- **Idée centrale** : former une **combinaison linéaire** des variables, $\hat{y}=w_1x_1+\dots+w_dx_d+b$, puis (pour la classification) lui appliquer une sigmoïde.
- **Avantages** : **interprétables** (chaque poids $w_i$ représente l'influence de la variable correspondante), rapides à entraîner ; c'est la **référence** à lancer en premier sur presque toutes les tâches.
- **Inconvénients** : faible pouvoir d'expression, impuissants face aux relations **non linéaires** ; **sensibles aux échelles** des variables, ce qui impose généralement une normalisation préalable (scaling).
- **Cas d'usage** : relation à peu près linéaire entre variables et cible, besoin d'interprétabilité, données de grande dimension sans forcément beaucoup d'exemples. Voir [Modèles linéaires](../linear-model/).

### Arbres de décision et ensembles

- **Idée centrale** : découper l'espace des variables en petits blocs à l'aide d'une suite de **if-else**, chaque bloc recevant une valeur prédite. Un arbre seul est un [arbre de décision](../decision-tree/) ; combiner de nombreux arbres donne l'[apprentissage ensembliste / GBDT](../ensemble-gbdt/).
- **Avantages** : gèrent naturellement la non-linéarité et les interactions entre variables, ne nécessitent pas de normalisation, acceptent des variables de types mixtes ; **le GBDT et les forêts aléatoires comptent parmi les références les plus fortes sur les données tabulaires**.
- **Inconvénients** : un arbre seul a une **forte variance** (il [surapprend](../overfitting/) facilement) et est sensible aux moindres variations des données d'entraînement ; surtout — point crucial — les modèles à base d'arbres **ne peuvent pas extrapoler une tendance** : leurs prédictions restent toujours dans l'intervalle observé pendant l'entraînement.
- **Cas d'usage** : données structurées / tabulaires, relations complexes entre variables, recherche d'une grande précision « clé en main ».

### Machines à vecteurs de support (SVM)

- **Idée centrale** : trouver une frontière à **marge maximale (max-margin)**, la plus éloignée possible des exemples les plus proches ; grâce à une **fonction noyau (kernel)**, les données sont implicitement projetées en grande dimension, ce qui permet de traiter la non-linéarité.
- **Avantages** : excellentes performances sur des problèmes **de petite ou moyenne taille en grande dimension**, théorie élégante, bonne capacité de généralisation.
- **Inconvénients** : entraînement lent sur de **gros volumes de données** (la complexité croît rapidement avec le nombre d'exemples), noyau et paramètres à régler, interprétabilité moyenne.
- **Cas d'usage** : peu d'exemples mais beaucoup de dimensions (texte, données génomiques, par exemple). Voir [SVM](../svm/).

### Plus proches voisins (kNN)

- **Idée centrale** : l'**apprentissage paresseux (lazy learning)** — rien n'est fait à l'entraînement ; à la prédiction, on cherche les $k$ voisins les plus proches et on les fait voter ou on en fait la moyenne. Tout repose sur la **distance**.
- **Avantages** : idée extrêmement simple, aucun entraînement, gestion naturelle du multiclasse.
- **Inconvénients** : prédiction lente (il faut calculer à chaque fois toutes les distances), sensibilité à la métrique de distance et aux échelles, et surtout la **malédiction de la dimension (curse of dimensionality)** — en grande dimension, le « plus proche » et le « plus lointain » ne se distinguent presque plus.
- **Cas d'usage** : faible dimension, petits jeux de données, prototype rapide ou référence.

### Réseaux de neurones

- **Idée centrale** : empiler de nombreuses couches de **transformations linéaires + activations non linéaires** pour apprendre de bout en bout une représentation des données.
- **Avantages** : pouvoir d'expression considérable et grande flexibilité ; ils dominent presque sans partage sur les données non structurées comme les **images, les textes et les séquences**.
- **Inconvénients** : **gourmands en données** (data-hungry), coûteux à entraîner, réglage complexe, peu interprétables.
- **Cas d'usage** : beaucoup de données, tâche complexe, signaux bruts riches (pixels, caractères, formes d'onde).

## Un tableau comparatif

| Famille | Idée centrale | Avantages | Inconvénients | Idéal pour |
|---|---|---|---|---|
| Modèles linéaires | Combinaison linéaire des variables | Interprétables, rapides, bonne référence | Peinent sur le non-linéaire | Quasi linéaire, besoin d'explication |
| Arbres / ensembles | Découpage en blocs if-else | Forts sur le tabulaire, sans normalisation | Arbre seul à forte variance, pas d'extrapolation | Données structurées / tabulaires |
| SVM | Marge maximale + noyau | Forts en grande dimension, échantillons petits à moyens | Lents sur gros volumes | Grande dimension, peu d'exemples |
| kNN | Vote des plus proches voisins | Ultra-simple, sans entraînement | Malédiction de la dimension, prédiction lente | Faible dimension, peu de données |
| Réseaux de neurones | Couches non linéaires multiples | Très flexibles, forts sur le non-structuré | Gourmands en données, peu interprétables | Images / textes / séquences |

## Pourquoi c'est important : comment choisir

Face à une nouvelle tâche, on peut « filtrer » à l'aide de ces quelques questions :

1. **Quelle est la quantité de données ?** Peu de données : privilégier les modèles linéaires, les SVM ou les arbres ; ne considérer les réseaux de neurones qu'avec beaucoup de données.
2. **S'agit-il de données tabulaires ?** Oui : le GBDT est généralement le premier choix ; non (images / textes / parole) : les réseaux de neurones.
3. **A-t-on besoin d'interprétabilité ?** Oui : modèle linéaire ou arbre unique ; non : on peut passer aux ensembles ou aux réseaux de neurones.
4. **La relation est-elle fortement non linéaire ?** Oui : arbres / SVM à noyau / réseaux de neurones ; à peu près linéaire : un modèle linéaire suffit.
5. **Quel coût d'entraînement et de mise en production ?** Avec des ressources limitées, ne commencez pas d'emblée par un gros réseau.

Souvenez-vous du **théorème du « pas de repas gratuit »** : plutôt que de débattre de qui est théoriquement le plus fort, **comparez-les par [validation croisée](../cross-validation/) sur vos propres données**.

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, chacune de ces familles a sa place :

- **Autorégression linéaire (comme AR)** : prédire le futur par une combinaison linéaire des derniers pas de temps ; c'est la **référence** la plus classique, à lancer en premier.
- **GBDT avec ingénierie des variables** : transformer « valeurs retardées, moyennes glissantes, jours fériés, jour de la semaine », etc., en variables fournies à un GBDT — c'est aujourd'hui **l'une des méthodes les plus performantes pour la prévision de séries temporelles sous forme tabulaire**, utilisée par de nombreux vainqueurs de compétitions de prévision. Mais attention : elle **ne peut pas extrapoler une tendance** ; une série en hausse durable doit d'abord être différenciée.
- **Réseaux de neurones ([RNN](../rnn/) / [LSTM](../lstm/) / [Transformer](../transformer/))** : excellents sur les séquences **complexes, à longue portée et multivariées** ; très puissants quand les données sont suffisantes, mais coûteux et sujets au surapprentissage.

Règle d'or en pratique : **commencez par une référence simple (linéaire / GBDT), faites-la tourner, quantifiez l'erreur, puis décidez s'il faut passer à un réseau de neurones**. Bien souvent, la référence simple suffit déjà.

## En résumé

- **Il n'y a pas de meilleur modèle, seulement un modèle le plus adapté** — c'est l'esprit du théorème du « pas de repas gratuit ».
- Chaque famille gagne grâce à des **hypothèses** différentes : le linéaire par la linéarité, les arbres par le découpage en blocs, le SVM par la marge, le kNN par la distance, les réseaux de neurones par l'empilement de non-linéarités.
- Le choix se fait selon cinq critères : **quantité de données, caractère tabulaire, interprétabilité, degré de non-linéarité, coût d'entraînement**.
- Pour les séries temporelles : **autorégression linéaire comme référence → GBDT avec variables construites → réseaux de neurones seulement pour les séquences longues et complexes**.
- Toujours **du simple au complexe**, avec une validation croisée sur vos propres données.

Pour aller plus loin : [Modèles linéaires](../linear-model/) · [Arbres de décision](../decision-tree/) · [Apprentissage ensembliste / GBDT](../ensemble-gbdt/) · [SVM](../svm/) · [Apprentissage supervisé](../supervised-learning/) · [Apprentissage non supervisé](../unsupervised-learning/)

---

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble du cours de base](../)
