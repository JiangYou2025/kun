---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/generalization/
title: "Généralisation"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

La **généralisation (generalization)** désigne la capacité d'un modèle à rester performant sur des données nouvelles qu'il **n'a jamais vues**. C'est le véritable objectif de l'apprentissage automatique — on n'entraîne pas un modèle pour qu'il apprenne par cœur le jeu d'entraînement, mais pour qu'il fasse des prédictions précises sur les données réelles à venir.

## Intuition

Imaginez deux élèves qui préparent un examen.

- Le premier **apprend par cœur** les sujets des années précédentes et leurs corrigés. Aux examens blancs (qui reprennent justement ces anciens sujets), il obtient la note maximale ; mais dès que l'examen propose de nouvelles questions, il est perdu.
- Le second **a compris les principes sous-jacents**. Il n'a peut-être pas tout juste sur les anciens sujets, mais face à une question nouvelle, il sait quand même retrouver la réponse.

C'est le second qui a vraiment « appris » : c'est la **généralisation**. En apprentissage automatique :

- Le premier élève correspond au **surapprentissage (overfitting)** : le modèle a mémorisé le bruit et les détails fortuits des données d'entraînement ; l'erreur d'entraînement est très faible, mais il s'effondre sur de nouvelles données.
- Le second correspond à une bonne généralisation : le modèle a saisi les **régularités reproductibles** des données, et reste donc fiable sur des données jamais vues.

En une phrase : **ce que nous voulons, c'est la « compréhension », pas la « récitation »**. La capacité de généralisation mesure précisément la part de compréhension et la part de récitation du modèle. Voir le [surapprentissage](../overfitting/).

## Erreur d'entraînement contre erreur de généralisation

Deux types d'erreur nous intéressent :

- **L'erreur d'entraînement (training error)** : l'erreur moyenne du modèle sur le jeu d'entraînement. C'est ce que nous voyons directement et ce que nous optimisons.
- **L'erreur de généralisation (generalization error)** : l'erreur attendue du modèle sur **toute la distribution des données**, c'est-à-dire sa performance moyenne face à toutes les données nouvelles possibles. C'est elle que nous voulons réellement minimiser, mais elle n'est pas directement observable.

Leur différence est la quantité clé :

$$\text{écart de généralisation (generalization gap)} = R(f) - R_{emp}(f)$$

- Écart faible : ce que le modèle a appris sur le jeu d'entraînement se transfère aux nouvelles données — il généralise bien.
- Écart important : le modèle surapprend, et ses bons résultats sur le jeu d'entraînement sont « illusoires ».

Un piège courant et dangereux : ne chercher qu'à faire baisser l'erreur d'entraînement. Celle-ci peut descendre jusqu'à 0 (pour peu que le modèle soit assez complexe et mémorise assez bien), alors que l'erreur de généralisation diminue souvent avant de remonter — c'est le signal du surapprentissage.

{% include fviz/learning-curve.html %}

## Formulation mathématique : risque empirique contre risque espéré

Pour formaliser l'intuition ci-dessus, on introduit deux « risques ».

Soit $L(y, f(x))$ la [fonction de perte](../loss-function/) (qui mesure l'écart entre la prédiction $f(x)$ et la vraie valeur $y$).

Le **risque empirique (empirical risk)** est la perte moyenne sur les $n$ échantillons d'entraînement dont on dispose :

$$R_{emp}(f) = \frac{1}{n}\sum_{i=1}^{n} L\big(y_i, f(x_i)\big)$$

Le **risque espéré (expected risk)** est l'espérance de la perte sur la vraie distribution des données :

$$R(f) = \mathbb{E}_{(x,y)}\big[L(y, f(x))\big]$$

Ce que nous voulons vraiment minimiser, c'est $R(f)$, mais la distribution est inconnue et on ne peut pas le calculer. On se rabat donc sur $R_{emp}(f)$, qui est calculable — c'est la **minimisation du risque empirique (ERM, Empirical Risk Minimization)**.

Pourquoi est-il raisonnable d'approcher $R$ par $R_{emp}$ ? Tout repose sur l'**hypothèse iid** : on suppose que les échantillons d'entraînement sont tirés de façon **indépendante et identiquement distribuée (independent and identically distributed)** à partir d'une même distribution. Sous cette hypothèse, par la loi des grands nombres, lorsque la taille d'échantillon $n$ est assez grande, $R_{emp}(f)$ converge vers $R(f)$ : la moyenne tend vers l'espérance.

Mais attention :

- Avec trop peu d'échantillons, $R_{emp}$ et $R$ peuvent être très éloignés, et le modèle prend facilement le bruit pour une régularité.
- Si l'hypothèse iid est violée (par exemple si la distribution des données futures diffère de celle du passé), cette approximation ne tient plus — c'est particulièrement fréquent en séries temporelles, comme on le verra plus bas.

## Comment estimer la capacité de généralisation

Puisqu'on ne peut pas calculer $R(f)$, on l'**estime** en « mettant de côté une partie des données et en faisant comme si c'était le futur ».

- **Jeu de test mis de côté (held-out test set)** : on découpe les données en un jeu d'entraînement et un jeu de test ; le modèle n'apprend que sur le jeu d'entraînement, et on ne **regarde qu'une seule fois**, à la fin, sa performance sur le jeu de test pour estimer l'erreur de généralisation. Le jeu de test ne doit jamais servir à l'entraînement ni au réglage des hyperparamètres, sinon on « divulgue le sujet ».
- **Validation croisée (cross-validation)** : on partage les données en $k$ blocs ; à tour de rôle, un bloc sert de jeu de validation et les autres de jeu d'entraînement, on répète $k$ fois et on fait la moyenne. On obtient ainsi une estimation plus robuste de la capacité de généralisation, particulièrement utile quand les données sont peu nombreuses. Voir la [validation croisée](../cross-validation/).

Le principe fondamental en une phrase : **l'évaluation doit se faire hors échantillon (out-of-sample)**. S'auto-féliciter sur des données déjà vues n'a aucun sens.

## Ce qui améliore la généralisation

Améliorer la généralisation revient, au fond, à trouver l'équilibre entre « apprendre les vraies régularités » et « ne pas mémoriser le bruit ». Les leviers habituels :

- **Plus de données** : plus il y a de données, plus $R_{emp}$ se rapproche de $R$, et plus il est difficile pour le modèle de s'en sortir par la simple mémorisation. C'est souvent la méthode la plus rentable.
- **La régularisation (regularization)** : ajouter des contraintes ou des pénalités au modèle pour limiter sa complexité et le forcer à apprendre des régularités simples et générales. Voir la [régularisation](../regularization/).
- **Un modèle plus simple** : à performance comparable, préférer le modèle le plus simple, avec le moins de paramètres (rasoir d'Ockham).
- **L'[arrêt précoce](../early-stopping/) (early stopping)** : surveiller l'erreur de validation pendant l'entraînement et s'arrêter dès qu'elle commence à remonter, pour éviter que le modèle ne se mette de plus en plus à « réciter ».

Tous ces leviers sont étroitement liés au **compromis biais–variance** :

$$\text{erreur de généralisation} \approx \text{biais}^2 + \text{variance} + \text{bruit irréductible}$$

- Modèle trop simple → **biais** élevé (il ne capte pas les régularités : sous-apprentissage).
- Modèle trop complexe → **variance** élevée (trop sensible aux données d'entraînement : surapprentissage).

Un modèle qui généralise bien est un modèle qui trouve l'équilibre entre biais et variance. Voir le [compromis biais–variance](../bias-variance/).

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, **généraliser, c'est prédire un futur que l'on n'a pas encore vu**. Il y a ici plusieurs points spécifiques qui demandent une vigilance particulière.

- **Découper dans l'ordre chronologique** : ne jamais mélanger aléatoirement les données avant de séparer entraînement et test ! Il faut entraîner sur les données **passées** et tester sur les données **postérieures**. Sinon, le modèle « voit le futur » (fuite de données), les résultats d'évaluation sont trop beaux pour être vrais, et la mise en production tourne au désastre.
- **Dérive de distribution / dérive conceptuelle (distribution shift / concept drift)** : la grande difficulté des séries temporelles est que la distribution future peut **différer** de celle du passé. Le comportement des utilisateurs change, les politiques changent, le contexte du marché change, et les régularités apprises peuvent cesser de valoir. Cela viole directement l'hypothèse iid ; même si le modèle généralise bien sur l'historique, il ne faut donc pas se fier aveuglément à ses prévisions pour un futur lointain.
- **Évaluation hors échantillon (out-of-sample evaluation)** : l'évaluation doit simuler le scénario réel de prévision ; on utilise couramment la **prévision glissante / la validation croisée pour séries temporelles** — on fixe un instant, on entraîne uniquement sur les données antérieures, on prédit la période suivante, puis on avance l'instant et on recommence. Seule l'erreur ainsi obtenue reflète vraiment la capacité du modèle face au futur.

Retenez : en séries temporelles, « généraliser » ne veut pas seulement dire « être bon sur de nouveaux échantillons », mais aussi « rester robuste sur une **nouvelle période**, avec potentiellement une **nouvelle distribution** ».

## En résumé

- La **généralisation** est la capacité d'un modèle à être performant sur des données jamais vues ; c'est le **véritable objectif** de l'apprentissage automatique.
- Il faut s'intéresser à l'**erreur de généralisation** et pas seulement à l'erreur d'entraînement ; leur différence est l'**écart de généralisation**, et un écart important signale un surapprentissage.
- En théorie, on veut minimiser le **risque espéré $R(f)$** ; en pratique, on l'approche par le **risque empirique $R_{emp}(f)$** (ERM), ce qui n'est légitime que sous l'**hypothèse iid** et avec suffisamment de données.
- On estime la généralisation avec un **jeu de test mis de côté** et la **validation croisée**, selon le principe de l'**évaluation hors échantillon**.
- Améliorer la généralisation : **plus de données, régularisation, modèles plus simples, arrêt précoce** ; au fond, il s'agit d'équilibrer **biais et variance**.
- En séries temporelles, il faut **découper dans l'ordre chronologique**, se méfier de la **dérive de distribution / conceptuelle**, et pratiquer une **évaluation glissante hors échantillon**.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
