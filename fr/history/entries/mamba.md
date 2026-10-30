---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2023 · Contrôle / Communications"
permalink: /fr/history/e/mamba/
title: "Un espace d'états qui sait choisir (Mamba, 2023)"
lead: "Faire dépendre de l'entrée les paramètres d'un modèle à espace d'états : la « sélectivité » lui donne la capacité d'oublier et de se concentrer ; associée à un balayage parallèle adapté au matériel, elle permet de modéliser des séquences très longues en temps linéaire."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

L'auto-attention du Transformer paie en $$O(L^2)$$ la connexion directe entre positions quelconques, et peine dès que la séquence s'allonge. Une autre piste vient de l'automatique : les **modèles à espace d'états (SSM)**, qui font évoluer un état caché de façon récursive dans le temps, en temps naturellement linéaire. Des SSM structurés comme S4 avaient déjà montré qu'en discrétisant un système classique à temps continu, puis en le paramétrant avec soin, on pouvait rivaliser avec le Transformer sur des bancs d'essai de longues séquences, avec une inférence récurrente en $$O(L)$$. Mamba (Gu et Dao, 2023) est le bond décisif sur cette voie.

### Problème

Les SSM antérieurs étaient pour la plupart **linéaires invariants dans le temps (LTI)** : les matrices de transition $$A,B,C$$ sont fixes, indépendantes du contenu observé. Cela les rend efficaces, mais les prive d'une capacité essentielle — **retenir ou oublier sélectivement selon le contenu**. La force de l'attention tient justement à ce qu'elle répartit dynamiquement ses poids en fonction de l'entrée. **Peut-on doter les SSM d'une sélectivité dépendant du contenu, sans perdre l'efficacité du temps linéaire ?**

### Les autres courants de l'époque (et leurs limites)

- **Le Transformer à auto-attention** : une sélectivité de contenu très forte, mais un coût en calcul et en mémoire en $$O(L^2)$$, prohibitif pour les séquences très longues.
- **Les SSM linéaires invariants dans le temps ([S4](../s4/), etc.)** : temps linéaire, stabilité à longue portée, mais des paramètres indépendants de l'entrée, incapables de traiter différemment des contenus différents, et donc mal armés pour « se concentrer / ignorer » finement.
- **L'attention linéaire / les convolutions à portes** : plus rapides, mais souvent au prix de l'expressivité ; sur les longues séquences, la qualité reste inférieure à l'attention complète.

### Méthode

Mamba introduit le **SSM sélectif** : le pas de discrétisation $$\Delta$$ ainsi que $$B,C$$ deviennent **des fonctions de l'entrée courante**, de sorte qu'un même mécanisme peut modifier sa dynamique de mémoire selon le contenu. Sa forme continue est

$$ \frac{dh(t)}{dt} = A\,h(t) + B\,x(t),\qquad y(t) = C\,h(t) $$

Après discrétisation (bloqueur d'ordre zéro), on obtient la récurrence $$h_t = \bar{A}h_{t-1} + \bar{B}x_t,\; y_t = C h_t$$, où

$$ \bar{A} = \exp(\Delta A),\qquad \bar{B} = (\Delta A)^{-1}(\exp(\Delta A)-I)\,\Delta B $$

L'essentiel est que $$\Delta,B,C$$ dépendent désormais de $$x_t$$ : un grand pas $$\Delta$$ écrit fortement la nouvelle information (concentration), un petit pas conserve l'ancien état (saut / oubli). Le prix à payer est que le modèle n'est plus invariant dans le temps et ne peut plus être calculé d'un seul coup par convolution. La solution de Mamba est un **balayage parallèle (parallel scan) adapté au matériel** : la récurrence, intrinsèquement séquentielle, est déroulée efficacement sur GPU par un algorithme parallèle de type somme préfixe, et la fusion de noyaux maintient les états intermédiaires dans la SRAM rapide ; l'entraînement est ainsi parallèle, tandis que l'inférence reste une récurrence en $$O(L)$$.

### Résultats

Sur des tâches à longues séquences — langage, audio, génomique —, Mamba égale ou dépasse des Transformers de taille comparable ; son débit d'inférence croît linéairement avec la longueur de la séquence, et ses avantages en mémoire et en vitesse sont nets en contexte long. Il montre que la sélectivité dépendant du contenu n'est pas le monopole de l'attention : elle peut aussi s'épanouir dans un modèle à espace d'états.

### Portée et perspectives

Mamba coud ensemble le langage de l'espace d'états issu de l'automatique et la « sélectivité » de l'apprentissage profond moderne, offrant un squelette candidat solide pour la « modélisation de longues séquences en temps linéaire ». C'est particulièrement pertinent pour les séries temporelles, qui sont par nature des échantillons de systèmes continus : les fondements à temps continu des SSM leur sont naturellement apparentés (voir le traitement de l'échantillonnage irrégulier par les [Neural CDE](../neural-cde/)). À l'heure des grands modèles et de [KUN](../kun/), Mamba est, aux côtés de l'attention et de la convolution, l'une des options d'« opérateur par couche » interchangeables : [Kernel U-Net](../kun/) préconise justement de découpler la structure multi-échelle des opérateurs concrets, et le SSM sélectif est précisément un noyau de qualité qui concilie efficacité et mémoire à longue portée. De la récurrence linéaire de Yule aux espaces d'états qui savent « choisir », la modélisation des séries temporelles avance toujours sur le même fil conducteur.
