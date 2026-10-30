---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/architectures/
title: "Architectures courantes"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

L'**architecture d'un réseau** désigne la « conception du squelette », c'est-à-dire la manière dont les [neurones](../neuron/) sont organisés et connectés. D'un [réseau de neurones](../neural-network/) à l'autre, les structures taillées sur mesure pour des données et des tâches différentes varient énormément — cette page offre un rapide panorama des MLP, CNN, RNN / LSTM, Transformer et U-Net, et montre où se situe **Kernel U-Net (KUN)**, le modèle mis en avant sur ce site.

**Voir aussi :** [MLP](../mlp/) · [CNN](../cnn/) · [RNN](../rnn/) · [LSTM](../lstm/) · [Transformer](../transformer/) · [U-Net](../u-net/)

## Intuition : pourquoi des architectures différentes

Un [MLP](../mlp/) entièrement connecté peut en théorie approcher n'importe quelle fonction ; pourquoi inventer d'autres architectures ? Parce qu'**une bonne architecture intègre la structure des données dans le réseau sous forme d'a priori**, ce qui le rend plus économe en paramètres, plus facile à entraîner et plus précis :

- Les données présentent des **motifs locaux** (pixels voisins, instants voisins) → convolution ([CNN](../cnn/)).
- Les données présentent des **dépendances séquentielles** (ordre, mémoire) → récurrence ([RNN](../rnn/) / [LSTM](../lstm/)).
- Les données présentent des **relations à longue portée** (deux points quelconques peuvent être liés) → [attention](../attention/) ([Transformer](../transformer/)).
- La tâche demande du **multi-échelle tout en restituant les détails** (segmentation, prévision) → encodeur-décodeur ([U-Net](../u-net/)).

Choisir une architecture, c'est au fond choisir « quelle hypothèse structurelle confier au réseau ».

## Panorama des architectures

**MLP (perceptron multicouche)** — réseau à propagation avant entièrement connecté, le plus générique et le plus simple ; il peut en théorie approcher n'importe quelle fonction. Il n'exploite pas la structure des données et son nombre de paramètres explose pour les longues entrées, mais c'est souvent une baseline solide, ainsi qu'une pièce interne des autres architectures.
**Voir aussi :** [MLP](../mlp/) · [Propagation avant](../forward-propagation/) · [Fonction d'activation](../activation-function/)

**CNN (réseau de neurones convolutif)** — fait glisser des noyaux de convolution partagés pour extraire des motifs **locaux et invariants par translation**, et, combiné au sous-échantillonnage, construit des caractéristiques multi-échelles allant du fin au grossier. Peu de paramètres, parallélisable ; la convolution unidimensionnelle convient aux séries temporelles.
**Voir aussi :** [CNN](../cnn/)

**RNN (réseau de neurones récurrent)** — traite les données pas à pas dans l'ordre temporel et transmet l'historique via un état caché qui sert de « mémoire ». Naturellement adapté aux séquences, mais lent car séquentiel, et sujet à la [disparition / explosion du gradient](../vanishing-exploding-gradient/) sur les longues séquences.
**Voir aussi :** [RNN](../rnn/)

**LSTM (Long Short-Term Memory, mémoire à long et court terme)** — ajoute au RNN des « portes » et un état de cellule, ce qui lui permet de retenir plus longtemps les informations clés et d'atténuer la disparition du gradient ; ce fut le cheval de bataille de la modélisation de séquences avant le Transformer.
**Voir aussi :** [LSTM](../lstm/)

**Transformer** — entièrement fondé sur l'auto-attention, il traite toute la séquence en parallèle et relie directement deux points quelconques en une seule étape ; fort sur les dépendances à longue portée et capable de passer à l'échelle, c'est le squelette de la modélisation de séquences moderne et des grands modèles. Le prix à payer est le coût en $O(L^2)$ de l'attention.
**Voir aussi :** [Transformer](../transformer/) · [Attention](../attention/)

**U-Net** — encodeur-décodeur à connexions résiduelles (skip connections) : il sous-échantillonne niveau par niveau pour saisir la vue d'ensemble, puis sur-échantillonne pour restituer les détails ; c'est la structure classique de la modélisation multi-échelle.
**Voir aussi :** [U-Net](../u-net/)

## Un tableau comparatif

| Architecture | Hypothèse centrale | Points forts | Points faibles |
|---|---|---|---|
| MLP | Aucune (entièrement connecté) | Correspondance générique, baseline solide | Ignore la structure, beaucoup de paramètres |
| CNN | Localité + invariance par translation | Motifs locaux, multi-échelle | Les relations lointaines exigent d'empiler beaucoup de couches |
| RNN/LSTM | Mémoire séquentielle | Dépendances séquentielles | Lent car séquentiel, longue portée difficile |
| Transformer | Deux points quelconques peuvent être liés | Dépendances à longue portée, passage à l'échelle | Coût élevé en $O(L^2)$ |
| U-Net | Multi-échelle + restitution | Segmentation, tâches multi-résolution | Blocs de convolution plutôt lourds |

## Intérêt pour la prévision de séries temporelles : où se situe KUN

La prévision de séries temporelles peut recourir à n'importe laquelle des architectures ci-dessus : aplatir l'entrée pour un [MLP](../mlp/), saisir les formes d'onde locales avec un [CNN](../cnn/) unidimensionnel, mémoriser l'historique avec un [LSTM](../lstm/), relier des instants éloignés avec un [Transformer](../transformer/). Mais la prévision de longues séries pose une difficulté commune : **il faut à la fois bien voir la tendance à long terme, préserver les détails à court terme, et empêcher le coût de calcul (en particulier le $O(L^2)$ de l'attention) de devenir incontrôlable.**

**Kernel U-Net (KUN)**, le modèle mis en avant sur ce site, a été conçu précisément pour cela : c'est un **modèle encodeur-décodeur multi-échelle (multi-résolution) de type [U-Net](../u-net/)**, qui sous-échantillonne niveau par niveau **le long de l'axe temporel** pour obtenir plusieurs vues, du fin au grossier, puis sur-échantillonne pour produire la prévision future, les connexions résiduelles préservant l'information fine. À la différence du U-Net d'origine, KUN **remplace les lourds blocs de convolution par des « noyaux » (kernels) légers et apprenables**, ce qui lui permet de modéliser simultanément, à différentes échelles de temps, la tendance à long terme et les fluctuations à court terme, pour un coût **bien inférieur à $O(L^2)$**.

On peut voir KUN comme une architecture dédiée à la prévision de séries temporelles qui « **s'inscrit dans la lignée du U-Net, reprend l'intuition multi-échelle des CNN et évite le coût quadratique du Transformer** ».

## Résumé

- Architecture = intégrer la structure des données au réseau sous forme d'a priori ; choisir une architecture, c'est choisir une hypothèse structurelle.
- MLP : générique ; CNN : local ; RNN/LSTM : séquentiel ; Transformer : longue portée ; U-Net : multi-échelle.
- **Kernel U-Net (KUN)** est un modèle de prévision multi-échelle de type U-Net qui mise sur des noyaux légers pour rester efficace sur de longues séries — c'est le protagoniste de ce site.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
