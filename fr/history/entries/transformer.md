---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2017 · Informatique"
permalink: /fr/history/e/transformer/
title: "Le Transformer et l'auto-attention (Vaswani et al., 2017)"
lead: "Un réseau récurrent doit se dérouler pas à pas le long du temps. Peut-on faire dialoguer directement deux positions quelconques, tout en calculant la séquence entière en parallèle ? L'auto-attention y parvient."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 9 · Apprentissage profond](../../09/).

### Contexte

À partir de 2014, la modélisation de séquences repose principalement sur les [RNN](../rnn/) et leurs variantes à portes, [LSTM](../lstm/) et GRU, associés à une architecture encodeur–décodeur et à un mécanisme d'« attention » pour la traduction automatique. L'attention n'est d'abord qu'un accessoire du RNN : à chaque pas de décodage, on revient sur tous les états cachés de l'encodeur, pondérés selon leur pertinence. Elle a déjà prouvé qu'il est très utile de « rendre l'information lointaine directement accessible ».

### Problème

Mais la structure récurrente a deux défauts rédhibitoires. Le premier est son caractère **séquentiel** : l'état caché $$h_t=f(h_{t-1},x_t)$$ doit être calculé pas à pas dans l'ordre temporel, sans parallélisation possible sur la longueur de la séquence, d'où un entraînement lent. Le second est l'**affaiblissement des dépendances à longue portée** : l'information doit se propager sur $$O(n)$$ pas pour aller d'un bout à l'autre de la séquence, et le gradient a tendance à s'évanouir en chemin. **Peut-on supprimer la récurrence, relier en un seul pas deux positions quelconques, et traiter toute la séquence en parallèle ?**

### Les autres courants de l'époque (et leurs limites)

- **Séquence-à-séquence purement LSTM/GRU** : très expressif, mais intrinsèquement séquentiel ; sur les longues séquences, le chemin de l'information est long et le débit d'entraînement limité.
- **Modèles de séquence convolutifs (ConvS2S, ByteNet)** : parallélisables, mais deux positions éloignées ne peuvent interagir qu'au prix d'un empilement de $$O(\log n)$$ ou $$O(n)$$ couches de convolution.
- **L'attention comme accessoire** : la bonne direction, mais encore greffée sur un squelette récurrent, sans remplacer complètement la récurrence.

### Méthode

Le mot d'ordre du Transformer est « Attention is All You Need » : remplacer entièrement la récurrence par l'auto-attention. On projette l'entrée en requêtes $$Q$$, clés $$K$$ et valeurs $$V$$ ; chaque position calcule sa compatibilité avec toutes les positions et en fait une somme pondérée :

$$ \mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V $$

où $$\sqrt{d_k}$$ est un facteur d'échelle qui empêche des produits scalaires trop grands de saturer le gradient du softmax. Le modèle utilise **plusieurs têtes** pour apprendre en parallèle des relations dans différents sous-espaces, et un **encodage positionnel** pour injecter l'information d'ordre (l'auto-attention étant en elle-même invariante par permutation) :

$$ PE_{(pos,2i)}=\sin\!\Big(\frac{pos}{10000^{2i/d}}\Big),\quad PE_{(pos,2i+1)}=\cos\!\Big(\frac{pos}{10000^{2i/d}}\Big) $$

Le chemin d'interaction entre deux positions quelconques est de longueur $$O(1)$$, et toute une couche se calcule d'un coup en parallèle (au prix d'une matrice d'attention en $$O(n^2)$$).

### Résultats

Sur les bancs d'essai de traduction automatique, le Transformer a battu les records BLEU de l'époque avec un temps d'entraînement moindre. Plus profondément, c'est sa **capacité de passage à l'échelle** qui compte : empiler davantage de couches et augmenter les données améliore continûment les performances, ce qui a directement donné naissance aux grands modèles préentraînés comme BERT et GPT, avant de déborder sur la vision, la parole, la prévision de séries temporelles et presque tous les domaines séquentiels.

### Portée et perspectives

Le Transformer a fait passer la modélisation de séquences de la « récursion le long du temps » à « l'attention globale + le parallélisme », et il est devenu le socle commun des grands modèles modernes ([modèles de fondation](../foundation-models/)). Il a aussi été largement adapté à la prévision de séries temporelles (attention parcimonieuse, entrées découpées en *patches*, etc., pour dompter le coût en $$O(n^2)$$). Et la quête d'efficacité sur les très longues séquences a, en retour, fait naître des modèles à espace d'états qui renouent avec la « récursion linéaire » ([S4](../s4/), [Mamba](../mamba/)) — l'histoire a ainsi orchestré un brillant dialogue entre récurrence et attention.
