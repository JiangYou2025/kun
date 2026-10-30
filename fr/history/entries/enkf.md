---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1994 · Automatique / Télécommunications"
permalink: /fr/history/e/enkf/
title: "Le filtre de Kalman d'ensemble (Evensen, 1994)"
lead: "L'état d'une prévision météorologique compte des centaines de millions de dimensions : la matrice de covariance de Kalman est impossible à stocker comme à calculer. Evensen répond : ne stockez pas la matrice, stockez simplement une population d'échantillons."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

La prévision numérique du temps est, au fond, un gigantesque problème d'estimation d'état : on fait avancer l'état de l'atmosphère avec un modèle physique, puis on le corrige sans cesse à l'aide d'observations (radiosondages, satellites, stations au sol). C'est exactement le terrain du [filtre de Kalman](../kalman/) — à un obstacle fatal près. Le filtre de Kalman doit stocker et propager explicitement la **matrice de covariance d'erreur** $$\mathbf{P}$$. Or la dimension $$n$$ de l'état atmosphérique dépasse couramment $$10^7$$ : une matrice $$n\times n$$ est impossible à stocker, et sa mise à jour selon l'évolution du modèle exigerait un calcul astronomique.

### Problème

Le goulot d'étranglement du filtre de Kalman classique est le **stockage et la propagation** de la matrice de covariance : en grande dimension, $$\mathbf{P}$$ ne peut être maintenue explicitement, et la stratégie du filtre de Kalman étendu, qui propage la covariance par linéarisation, est à la fois coûteuse et instable en grande dimension et en forte non-linéarité. **Comment, dans un système à des millions voire des centaines de millions de dimensions, représenter et faire évoluer approximativement l'incertitude de l'état pour réaliser l'assimilation de données ?**

### Autres courants de l'époque (et leurs limites)

- **Filtre de Kalman étendu (EKF)** : propage explicitement la covariance et linéarise le modèle. Dans les systèmes de grande dimension, le coût de propagation de la covariance est prohibitif, et la forte non-linéarité des modèles atmosphériques rend l'erreur de linéarisation sévère.
- **Assimilation variationnelle (3D/4D-Var)** : formule l'assimilation comme un problème d'optimisation, contournant la covariance explicite, avec un grand succès opérationnel ; mais elle exige de dériver et de maintenir un **modèle adjoint (adjoint)**, au coût de développement élevé, et suppose par défaut une covariance d'erreur d'ébauche statique, peu capable de suivre l'évolution de la situation météorologique.
- **Interpolation optimale (OI)** : utilise une covariance d'ébauche prédéfinie et fixe ; simple, mais incapable de refléter la structure de dépendance induite par « la circulation du jour ».

### Méthode

L'idée centrale de l'EnKF : ne pas stocker la matrice de covariance, mais la représenter implicitement par un ensemble de $$N$$ échantillons d'état (l'**ensemble**). La moyenne de l'ensemble est l'estimation de l'état, et sa dispersion encode la covariance d'erreur :

$$ \mathbf{P}^f\;\approx\;\frac{1}{N-1}\sum_{i=1}^{N}\big(\mathbf{x}_i^f-\bar{\mathbf{x}}^f\big)\big(\mathbf{x}_i^f-\bar{\mathbf{x}}^f\big)^{\!\top} $$

Chaque membre est intégré en avant avec le modèle non linéaire complet (étape de prévision), sans aucune linéarisation ni adjoint. Lorsqu'une observation $$\mathbf{y}$$ arrive, on applique à chaque membre une mise à jour de type Kalman (étape d'analyse) :

$$ \mathbf{x}_i^a=\mathbf{x}_i^f+\mathbf{K}\big(\mathbf{y}_i-\mathbf{H}\mathbf{x}_i^f\big),\qquad \mathbf{K}=\mathbf{P}^f\mathbf{H}^{\top}\big(\mathbf{H}\mathbf{P}^f\mathbf{H}^{\top}+\mathbf{R}\big)^{-1} $$

où le gain $$\mathbf{K}$$ est entièrement calculé à partir des statistiques de l'ensemble, sans jamais former la matrice $$\mathbf{P}$$ complète. En dotant chaque membre d'une observation perturbée $$\mathbf{y}_i=\mathbf{y}+\boldsymbol{\varepsilon}_i$$, on garantit que la variance de l'ensemble mis à jour est statistiquement correcte. L'ensemble de la procédure ne requiert que l'exécution du modèle lui-même, et sa complexité croît linéairement avec la taille de l'ensemble $$N$$ (typiquement de quelques dizaines à quelques centaines), au lieu d'exploser avec la dimension $$n$$.

### Résultats

L'EnKF a permis pour la première fois d'appliquer réellement l'idée de Kalman à des systèmes de très grande dimension comme l'océan et l'atmosphère : la covariance s'adapte « au fil de l'écoulement » à la circulation, sans modèle adjoint, avec une mise en œuvre relativement simple. Il fut rapidement adopté par les centres météorologiques et océanographiques du monde entier, devenant l'un des piliers de l'assimilation de données opérationnelle, et a engendré de nombreuses variantes comme l'ETKF ou le LETKF (associées aux techniques de **localisation** et d'**inflation** pour supprimer les corrélations parasites dues à la taille finie de l'ensemble).

### Portée et perspectives

L'EnKF a introduit dans le filtrage en grande dimension l'idée Monte-Carlo « approcher l'incertitude par un ensemble d'échantillons » ; il appartient, comme le [filtre particulaire](../particle-filter/), à la vague des filtres d'ensemble et par échantillonnage des années 1990, mais il est mieux adapté aux systèmes géophysiques de très grande dimension et quasi gaussiens. Il reste aujourd'hui une pierre angulaire de la prévision numérique du temps, de la modélisation océanique et des eaux souterraines et de la production de réanalyses, et l'œuvre emblématique de la philosophie moderne de la prévision : la fusion continue « modèle + observations ».
