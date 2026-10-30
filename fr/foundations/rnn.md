---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/rnn/
title: "RNN (réseau de neurones récurrent)"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Le **réseau de neurones récurrent** (RNN, *Recurrent Neural Network*) est un réseau qui lit une séquence pas de temps par pas de temps et qui, grâce à un « état caché », transporte l'information passée jusqu'au présent. Il est naturellement adapté aux données ordonnées, comme le texte, la parole et les séries temporelles.

## Intuition

Imaginez que vous lisez une phrase : « Aujourd'hui, il fait très… ». Arrivé là, vous avez déjà accumulé un peu de « contexte » et pouvez deviner que le mot suivant sera sans doute « beau » ou « chaud ». Vous ne regardez pas chaque mot isolément : **vous mettez à jour votre mémoire au fil de la lecture**, et cette mémoire influence à son tour votre compréhension du mot suivant.

C'est exactement ce que fait un RNN. Il possède un « vecteur mémoire » appelé **état caché** (*hidden state*) $h_t$ :

- à chaque nouvelle entrée $x_t$, il malaxe $x_t$ avec la mémoire de l'instant précédent $h_{t-1}$ pour calculer une nouvelle mémoire $h_t$ ;
- ce $h_t$ sert à la fois à produire la sortie courante et à être transmis au pas de temps suivant.

Un [réseau de neurones](../neural-network/) ordinaire fonctionne « à coup unique » : une entrée arrive, une sortie part, et les cas sont indépendants. La différence essentielle du RNN est que **le même jeu de poids est réutilisé à chaque pas de temps**, et que la mémoire circule le long de l'axe du temps à travers $h_t$.

## Formulation mathématique

Le cœur du RNN est une **formule de récurrence**. Soit $x_t$ l'entrée à l'instant $t$ et $h_t$ la mémoire :

$$
h_t = \tanh\!\left(W_x\, x_t + W_h\, h_{t-1} + b\right)
$$

Explication symbole par symbole :

- $x_t$ : le vecteur d'entrée au pas de temps $t$ (par exemple les ventes d'un jour donné, ou le vecteur d'un mot).
- $h_{t-1}$ : l'état caché du pas de temps précédent, c'est-à-dire « la mémoire jusqu'ici ». L'état initial $h_0$ est généralement mis à zéro.
- $h_t$ : la mémoire mise à jour à ce pas de temps.
- $W_x$ : la matrice de poids qui projette l'entrée $x_t$ dans l'espace de la mémoire.
- $W_h$ : la matrice de poids qui transforme l'ancienne mémoire $h_{t-1}$ avant de la mêler à la nouvelle.
- $b$ : le vecteur de biais.
- $\tanh$ : la [fonction d'activation](../activation-function/), qui comprime le résultat dans $(-1, 1)$ et introduit de la non-linéarité dans le réseau.

La sortie (si l'on veut prédire quelque chose) passe en général par une couche supplémentaire :

$$
\hat{y}_t = W_y\, h_t + b_y
$$

Attention : $W_x, W_h, W_y, b, b_y$ sont **partagés par tous les pas de temps** — c'est de là que vient le mot « récurrent ». Une séquence de longueur 100 n'utilise pas 100 jeux de paramètres, mais un seul jeu utilisé 100 fois.

## Rétropropagation à travers le temps (BPTT) et disparition du gradient

Comment un RNN apprend-il ? Toujours par [rétropropagation](../backpropagation/), mais en remontant le long de la chaîne du « temps » ; on parle donc de **rétropropagation à travers le temps** (BPTT, *Backpropagation Through Time*).

« Déplié » dans le temps, un RNN ressemble à un réseau très profond : la sortie au pas $T$ dépend de $h_T$, qui dépend de $h_{T-1}$, et ainsi de suite jusqu'à $h_1$. Lors du calcul du gradient, la [règle de dérivation en chaîne](../chain-rule/) multiplie une longue suite de dérivées, où ce terme revient sans cesse :

$$
\frac{\partial h_t}{\partial h_{t-1}} = W_h^{\top}\,\operatorname{diag}\!\big(\tanh'(\cdot)\big)
$$

Pour faire remonter une erreur commise $T$ pas plus tôt, il faut multiplier ce facteur $T$ fois, ce qui donne un ordre de grandeur d'environ $\lambda^{T}$ ($\lambda$ étant la « taille effective » de ces facteurs) :

- si $\lambda < 1$, le produit tend rapidement vers 0 → **disparition du gradient** : le réseau ne parvient pas à apprendre les dépendances lointaines (il « oublie ce qui a été dit au début ») ;
- si $\lambda > 1$, le produit croît de façon explosive → **explosion du gradient** : l'entraînement devient numériquement instable.

C'est la manifestation typique, dans les modèles de séquences, du problème de [disparition / explosion du gradient](../vanishing-exploding-gradient/). Comme $\tanh'$ vaut au plus 1 et devient proche de 0 loin de l'origine, le RNN simple est particulièrement sujet à la disparition du gradient et **a beaucoup de mal à retenir une information vieille de quelques dizaines de pas**. L'explosion est souvent atténuée par l'« écrêtage du gradient » (*gradient clipping*), tandis que la disparition a donné naissance au [LSTM](../lstm/).

## Un exemple concret

Déroulons quelques chiffres avec un mini-RNN à une dimension pour sentir comment la mémoire s'accumule. Prenons $W_x = 0.5,\ W_h = 0.9,\ b = 0$, la séquence d'entrée $x = [1, 1, 1]$ et $h_0 = 0$ :

$$
\begin{aligned}
h_1 &= \tanh(0.5\times 1 + 0.9\times 0) = \tanh(0.5) \approx 0.462\\
h_2 &= \tanh(0.5\times 1 + 0.9\times 0.462) = \tanh(0.916) \approx 0.724\\
h_3 &= \tanh(0.5\times 1 + 0.9\times 0.724) = \tanh(1.152) \approx 0.818
\end{aligned}
$$

On voit la mémoire $h_t$ s'accumuler continuellement. Voici le code PyTorch équivalent :

```python
import torch, torch.nn as nn

rnn = nn.RNN(input_size=1, hidden_size=8, batch_first=True)
x = torch.randn(4, 20, 1)        # (taille de lot=4, pas de temps=20, variables=1)
out, h_n = rnn(x)
print(out.shape)   # (4, 20, 8) : l'état caché à chaque pas de temps
print(h_n.shape)   # (1, 4, 8) : l'état caché au dernier pas
```

`out` donne la mémoire à chaque pas, et `h_n` est la « mémoire finale » une fois la séquence lue ; on y branche souvent une couche supplémentaire pour faire la prédiction.

## Intérêt pour la prévision de séries temporelles

Le RNN a longtemps été **le cheval de bataille classique de la prévision de séries temporelles** : on met à jour pas à pas l'état caché avec les observations des derniers jours, puis on utilise l'état final pour prédire le futur. Il traite naturellement des séquences de longueur variable et sait modéliser les dépendances temporelles.

Mais il souffre de deux défauts rédhibitoires :

- **il doit calculer pas à pas, dans l'ordre chronologique**, sans pouvoir paralléliser comme les convolutions ou l'attention, ce qui rend l'entraînement et l'inférence lents sur les longues séquences ;
- **la disparition du gradient** l'empêche de saisir les dépendances très longues, ce qui le met particulièrement en difficulté pour les horizons de prévision longs (*long horizon*).

Ces limites ont poussé vers des architectures parallélisables, capables de modéliser plusieurs échelles, comme le [Transformer](../transformer/) et le modèle multi-échelle mis en avant sur ce site, **Kernel U-Net (KUN)** — qui reprend l'idée multirésolution du [U-Net](../u-net/) pour extraire et fusionner des caractéristiques à différentes échelles de temps, ce qui le rend à la fois rapide et performant en prévision à long horizon.

## En résumé

- Le RNN entretient une mémoire qui s'écoule dans le temps grâce à la récurrence à poids partagés $h_t = \tanh(W_x x_t + W_h h_{t-1} + b)$.
- Il s'entraîne par **BPTT** ; le produit de dérivées provoque la **disparition / l'explosion du gradient**, et le RNN simple retient mal les dépendances longues.
- Son calcul séquentiel se parallélise mal et le rend peu efficace sur les longues séquences — c'est précisément ce que cherchent à résoudre le [LSTM](../lstm/) et le modèle multi-échelle KUN.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
