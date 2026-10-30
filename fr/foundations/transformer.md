---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/transformer/
title: "Transformer"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Le **Transformer** est une architecture de [réseau de neurones](../neural-network/) entièrement fondée sur l'[attention](../attention/) (l'auto-attention). Il abandonne la structure récurrente, **traite toute la séquence en parallèle et relie directement, en une seule étape, deux positions quelconques** ; il capture efficacement les dépendances à longue portée et constitue l'ossature dominante de la modélisation de séquences moderne (y compris tous les grands modèles de langage).

## Intuition

Avant le Transformer, la modélisation de séquences reposait surtout sur les [RNN](../rnn/) / [LSTM](../lstm/) : comme on lit un livre, mot après mot, l'information est transmise pas à pas par la « mémoire ». Le problème : plus on lit loin, plus l'information du début se dilue, et le traitement est forcément **séquentiel**, impossible à accélérer par le parallélisme.

L'approche du Transformer est tout autre : **déployer toute la séquence d'un coup et laisser chaque position « regarder » simultanément toutes les autres**, en décidant elle-même, selon la pertinence, à quoi prêter attention. Pas de perte due au « bouche-à-oreille », pas de goulet séquentiel. Le prix à payer : il ne connaît pas l'ordre par lui-même, il faut donc en plus **lui indiquer où se trouve chaque position** (l'encodage positionnel).

## Principe

Un Transformer est un empilement de plusieurs **blocs (block)** identiques ; chaque bloc contient deux sous-couches, chacune munie d'une connexion résiduelle et d'une normalisation de couche :

**Sous-couche 1 : auto-attention multi-têtes**

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left( \frac{QK^{\top}}{\sqrt{d_k}} \right) V
$$

où $Q, K, V$ sont tous obtenus par projection linéaire de l'entrée, $d_k$ est la dimension de chaque tête, et $\sqrt{d_k}$ sert de facteur d'échelle (détails dans [Attention](../attention/)). Multi-têtes = plusieurs jeux en parallèle, qui s'intéressent à des aspects différents avant d'être concaténés.

**Sous-couche 2 : réseau feed-forward position par position** (en fait un petit [MLP](../mlp/), appliqué indépendamment à chaque position)

$$
\mathrm{FFN}(x) = W_2\,\sigma\!\left(W_1 x + b_1\right) + b_2
$$

- $W_1, W_2$ : les poids des deux couches (la dimension intermédiaire est généralement multipliée par 4) ;
- $\sigma$ : la [fonction d'activation](../activation-function/) (par exemple ReLU/GELU).

**Résiduel + normalisation de couche** enveloppent chaque sous-couche, atténuent la [disparition / explosion du gradient](../vanishing-exploding-gradient/) et rendent les réseaux profonds entraînables :

$$
x \leftarrow \mathrm{LayerNorm}\big(x + \mathrm{Sublayer}(x)\big)
$$

**Encodage positionnel (Positional Encoding)** : comme l'auto-attention est « insensible » à l'ordre, on ajoute à l'entrée des vecteurs porteurs d'information de position, par exemple sous forme sinusoïdale

$$
PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right),\qquad
PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)
$$

- $pos$ : l'indice de position ; $i$ : l'indice de dimension ; $d$ : la dimension du modèle. Des sinus et cosinus de fréquences différentes donnent à chaque position une « empreinte » unique.

{% include fviz/attention-heat.html %}

## Un exemple concret

Le plus petit bloc encodeur (intégré à PyTorch) :

```python
import torch, torch.nn as nn

layer = nn.TransformerEncoderLayer(
    d_model=64, nhead=4,           # dimension du modèle 64, 4 têtes d'attention
    dim_feedforward=256,           # couche intermédiaire du FFN : 64*4
    batch_first=True,
)
encoder = nn.TransformerEncoder(layer, num_layers=2)

x = torch.randn(8, 96, 64)         # (batch, longueur de séquence=96, variables=64)
out = encoder(x)                   # (8, 96, 64), chaque position a intégré l'information globale
```

Chaque pas de temps de `x` entre en ne portant que sa propre information, et ressort après avoir « vu » les 96 pas et les avoir fusionnés selon leur pertinence.

## Pourquoi c'est important / où l'utiliser

- **Entraînement parallèle** : toute la séquence est calculée d'un coup, bien plus vite qu'un RNN forcément séquentiel.
- **Fortes dépendances à longue portée** : deux positions quelconques sont reliées en une étape, et leur relation ne s'affaiblit pas avec la distance.
- **Passage à l'échelle** : plus on empile de couches et plus il y a de données, meilleurs sont les résultats — c'est le socle de l'ère des grands modèles.
- Le domaine des séries temporelles compte aussi de nombreuses variantes du Transformer (Informer, Autoformer, PatchTST, etc.).

## Intérêt pour la prévision de séries temporelles

Le Transformer applique à la prévision l'avantage de « liaison directe à longue portée » apporté par l'attention, et peut relier directement des instants éloignés, d'un cycle à l'autre. Mais il hérite aussi du défaut majeur de l'attention : sur une séquence de longueur $L$, l'auto-attention coûte **$O(L^2)$** en temps et en mémoire. Les fenêtres d'historique des séries temporelles atteignent facilement des milliers, voire des dizaines de milliers de pas, et ce coût quadratique rend le Transformer standard lent et gourmand en mémoire.

Le modèle phare de ce site, **Kernel U-Net (KUN)**, propose une autre voie : en s'inspirant de la structure **encodeur–décodeur multi-échelles** du [U-Net](../u-net/), il sous-échantillonne l'axe du temps niveau par niveau et modélise les dépendances à longue portée sur des **séquences grossières plus courtes**, à moindre coût, au lieu d'encaisser de front le $O(L^2)$ sur toute la longueur de la séquence. Soulignons-le : **il ne s'agit pas d'une opposition « attention contre Transformer »** — l'attention peut toujours être intégrée à KUN comme composant local à une échelle donnée ; ce que KUN change, c'est la structure globale de la complexité, en échangeant la multi-résolution contre l'efficacité sur les longues séquences.

## Idées reçues fréquentes

- **« Le Transformer comprend naturellement l'ordre »** : non. L'information d'ordre est entièrement injectée par l'**encodage positionnel** ; sans lui, mélanger l'entrée ne change pas le résultat.
- **« L'attention est en $O(L)$ »** : l'auto-attention standard est en $O(L^2)$ — c'est précisément pourquoi la prévision de longues séquences exige des versions efficaces (ou une structure multi-échelles comme KUN).
- **« Le Transformer est toujours meilleur que RNN/[CNN](../cnn/)/MLP »** : pas forcément. Sur des séries courtes ou moyennes, avec peu de données, un simple [MLP](../mlp/) ou un modèle multi-échelles est souvent plus économique et plus précis.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
