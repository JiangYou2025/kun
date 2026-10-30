---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 2020 · Mathématiques"
permalink: /fr/history/e/neural-cde/
title: "Un état caché piloté par le chemin (Neural CDE · noyaux de signature, années 2020)"
lead: "Faire piloter l'état caché par le chemin d'observation lui-même, dz=f(z)dX : les équations différentielles contrôlées neuronales et les noyaux de signature font de l'échantillonnage irrégulier et des valeurs manquantes un simple trait naturel sur un chemin continu."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Les séquences du monde réel sont souvent « indisciplinées » : en surveillance médicale, en finance haute fréquence ou dans les réseaux de capteurs, les données sont échantillonnées de façon inégale, présentent des lacunes, et les différents canaux n'avancent pas au même rythme. Or les modèles profonds dominants (RNN, Transformer) supposent par défaut des séquences discrètes **régulièrement espacées et alignées** ; face à un échantillonnage irrégulier, ils doivent recourir tant bien que mal à l'interpolation, au remplissage par des zéros ou à des masques supplémentaires. Pendant ce temps, les mathématiques disposaient depuis longtemps d'un langage mûr pour les chemins continus — les équations différentielles contrôlées (CDE) et la **signature des chemins** issue de la théorie des [rough paths](../rough-paths/). Les Neural CDE et les noyaux de signature branchent précisément ce langage sur les réseaux de neurones.

### Problème

Les Neural ODE font évoluer l'état caché de façon autonome dans le temps, $$dz=f(z)\,dt$$, mais **une fois la condition initiale fixée, il devient indépendant des observations ultérieures** — impossible d'absorber en cours de route les données nouvelles. Pour les séries temporelles, il faut justement que **les observations elles-mêmes pilotent en continu** l'état caché, et que ce pilotage accueille naturellement des données irrégulières, à n'importe quel instant et sur n'importe quel canal. **Comment faire en sorte que l'état caché soit piloté par le « chemin des données » plutôt que par « l'horloge » ?**

### Les autres courants de l'époque (et leurs limites)

- **Interpolation + RNN/Transformer standard** : on complète d'abord les données irrégulières sur une grille régulière avant de les fournir au modèle. Limites : l'interpolation fabrique artificiellement des données, déforme les propriétés statistiques, et efface le motif des valeurs manquantes (« pourquoi c'est manquant » est souvent informatif).
- **Les Neural ODE** : temps continu et élégance, mais l'état caché n'évolue qu'avec le temps et ne peut pas être « corrigé » à l'arrivée d'une observation ; inadapté à l'absorption en ligne de nouvelles données.
- **Les RNN avec caractéristiques d'intervalle de temps (GRU-D, etc.)** : ils approchent le traitement des intervalles par des portes de décroissance ; c'est un correctif d'ingénierie plutôt qu'une formulation native en temps continu, aux propriétés théoriques floues.

### Méthode

Les Neural CDE interpolent d'abord les observations discrètes $$(t_i,x_i)$$ en un chemin continu et différentiable $$X(t)$$, puis font suivre à l'état caché une équation différentielle **contrôlée** — pilotée par ce chemin de contrôle $$X$$ :

$$ z(T) = z(t_0) + \int_{t_0}^{T} f_\theta\big(z(t)\big)\,dX(t) $$

Intuitivement, $$dX$$ est un petit accroissement du chemin des données, et $$f_\theta(z)$$ détermine comment cet accroissement modifie l'état caché ; l'intégrale est calculée numériquement par un solveur d'EDO. Comme la quantité motrice est $$dX$$ et non $$dt$$, sur les périodes sans observation le chemin est plat et l'état caché glisse naturellement en douceur, tandis qu'une nouvelle observation exerce immédiatement son influence — **échantillonnage irrégulier et valeurs manquantes sont unifiés en « le chemin ne varie pas sur certains intervalles »**, sans traitement spécial. Le **noyau de signature** est complémentaire : la théorie des [rough paths](../rough-paths/) fournit la « signature » d'un chemin — une famille d'intégrales itérées

$$ S(X)^{i_1\cdots i_k} = \idotsint_{t_0<u_1<\cdots<u_k<T} dX^{i_1}_{u_1}\cdots dX^{i_k}_{u_k} $$

C'est une caractéristique universelle du chemin, indépendante de sa paramétrisation. Le noyau de signature s'en sert pour mesurer la similarité entre deux chemins, transformant l'apprentissage sur séquences en une méthode à noyau sur l'espace des chemins, tout aussi robuste au mode d'échantillonnage.

### Résultats

Sur des tâches de séquences à échantillonnage irrégulier, à longues lacunes ou à arrivée en ligne (comme la classification de séries temporelles médicales), les Neural CDE et les méthodes de signature sont plus précis et plus stables que « interpolation + RNN », avec de solides garanties théoriques en temps continu ; l'état caché peut être interrogé à tout instant et gère naturellement des données multicanaux asynchrones.

### Portée et perspectives

Les Neural CDE et les noyaux de signature relient l'analyse stochastique d'[Itô](../ito/), la théorie des rough paths et l'apprentissage profond, offrant un paradigme aux principes clairs pour la « modélisation des séries temporelles en temps continu ». Ils partagent la même origine que les modèles à espace d'états comme [Mamba](../mamba/) — tous deux voient une séquence comme l'échantillonnage d'un système dynamique continu, l'un piloté par $$dX$$, l'autre modulé par des paramètres sélectifs. Sur la route vers les [modèles de fondation](../foundation-models/) pour les séries temporelles, faire absorber de façon robuste par un grand modèle des séquences hétérogènes aux modes d'échantillonnage extrêmement variés est l'un des problèmes centraux ; le point de vue « indépendant de l'échantillonnage » qu'apportent chemins et signatures pourrait constituer une classe d'opérateurs qu'il vaudrait la peine d'intégrer à l'avenir dans des architectures modulaires comme [Kernel U-Net](../kun/). Des cycles déterministes aux processus aléatoires, puis aux états cachés continus pilotés par le chemin, la vision du monde des séries temporelles a encore gagné en profondeur.
