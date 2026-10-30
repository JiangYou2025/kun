---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 2020 · Informatique"
permalink: /fr/history/e/kun/
title: "Séparer la structure et l'opérateur (Kernel U-Net, années 2020)"
lead: "Une hiérarchie en U s'occupe uniquement de la « structure multi-échelle », un noyau interchangeable (linéaire / MLP / attention) uniquement de « l'opérateur de chaque couche » — en séparant ces deux tâches, KUN retrouve l'équilibre entre efficacité et précision."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 10 · Grands modèles et KUN](../../10/).

### Contexte

Au milieu des années 2020, le débat sur la prévision de longues séries est dans l'impasse. D'un côté, [DLinear](../dlinear/) rappelle que « l'extrapolation linéaire est déjà très forte » ; de l'autre, [PatchTST](../patchtst/) montre qu'« avec la bonne tokenisation, l'attention reste puissante » ; s'y ajoutent de nouveaux venus à espace d'états en temps linéaire comme [Mamba](../mamba/). Chaque architecture a ses points forts, mais chacune est verrouillée dans sa conception d'ensemble : pour changer d'opérateur, il faut souvent réécrire tout le modèle.

### Problème

À y regarder de près, ces méthodes répondent en réalité à **deux questions différentes** : d'une part, « comment organiser l'information sur plusieurs échelles de temps » (tendance/saison, local/global, grossier/fin) ; d'autre part, « quel opérateur utiliser pour transformer les données à une échelle donnée » (linéaire, MLP, attention, SSM). Or les architectures existantes entremêlent souvent les deux. **Peut-on découpler la « structure multi-échelle » de « l'opérateur de chaque couche », afin de réutiliser une structure stable et de remplacer l'opérateur à la demande ?**

### Les autres courants de l'époque (et leurs limites)

- **Une seule architecture pour tout (un certain Transformer, ou du purement linéaire)** : structure et opérateur sont liés ; changer d'opérateur revient à changer de modèle, et il est difficile de comparer systématiquement la « contribution de la structure » et la « contribution de l'opérateur ».
- **Réduction de longueur en une fois par patchs (PatchTST)** : découpage à une granularité unique et fixe, sans chemin d'abstraction et de reconstruction progressif entre échelles.
- **Modélisation globale lourde par attention** : l'information d'échelle est apprise implicitement par l'attention, à un coût élevé, avec une interprétabilité faible et une efficacité limitée sur les longues séries.

### Méthode

Kernel U-Net (KUN) emprunte l'idée d'**encodage-décodage hiérarchique** du U-Net de la vision par ordinateur et l'abstrait. L'encodeur sous-échantillonne la série couche après couche, produisant des représentations multi-échelles du fin au grossier ; le décodeur sur-échantillonne couche après couche et fusionne, par des connexions de saut, les caractéristiques de l'échelle correspondante, pour reconstruire la fenêtre de prévision. L'innovation clé consiste à abstraire la transformation concrète de chaque couche en un **noyau interchangeable** $$K_\ell$$ :

$$ h^{(\ell+1)} = \mathrm{Down}\big(K_\ell(h^{(\ell)})\big),\qquad K_\ell \in \{\text{Linear},\,\text{MLP},\,\text{Attention},\,\dots\} $$

La hiérarchie en U décide « à quelle échelle regarder », le noyau $$K_\ell$$ décide « comment calculer à cette échelle ». On peut ainsi utiliser, dans les couches peu profondes (granularité fine, séquence longue), des noyaux linéaires ou MLP bon marché pour maîtriser le coût, et réserver aux couches profondes (granularité grossière, séquence courte) des noyaux plus expressifs comme l'attention — en plaçant les opérateurs coûteux à l'échelle où ils coûtent le moins. La complexité totale est approximativement

$$ \mathcal{O}\!\left(\sum_{\ell} c(K_\ell)\cdot L_\ell\right),\qquad L_{\ell+1}=L_\ell / r $$

où $$L_\ell$$ est la longueur de la séquence à la couche $$\ell$$, qui décroît géométriquement avec le taux de sous-échantillonnage $$r$$, et $$c(K_\ell)$$ le coût unitaire du noyau de cette couche. Une fois structure et opérateur découplés, on peut, comme avec des briques, configurer pour chaque jeu de données la combinaison la plus rentable.

### Résultats

Sur les bancs d'essai de prévision de longues séries, KUN atteint une précision compétitive, voire supérieure, avec un coût de calcul et de mémoire GPU plus faible. Plus important encore, il fournit un **banc d'expérimentation unifié** : en fixant la structure en U et en ne changeant que le noyau, on mesure proprement « combien la structure multi-échelle apporte, et ce que contribue chaque type d'opérateur » — exactement le prolongement de la question posée par DLinear.

### Portée et perspectives

L'intérêt de KUN réside dans une philosophie de conception : **distinguer d'abord structure et opérateur, puis optimiser chacun séparément**. Les voies qui semblaient opposées ces dernières années (linéaire contre attention contre SSM) trouvent ainsi chacune leur place — ce ne sont que des noyaux différents, placés à différentes échelles d'une même ossature en U. À l'ère des [modèles de fondation](../foundation-models/) pour séries temporelles, une telle architecture hiérarchique interchangeable et extensible est particulièrement précieuse : pour qu'« un seul modèle prévoie toutes les séries », il faut une ossature capable à la fois d'accueillir des échelles hétérogènes et de changer de noyau avec souplesse selon les données et la puissance de calcul. Du noyau sélectif de [Mamba](../mamba/) à l'opérateur de chemin continu des [Neural CDE](../neural-cde/), tous pourront à l'avenir devenir une couche de KUN. Séparer structure et opérateur est peut-être une voie pragmatique vers des modèles généralistes de séries temporelles.
