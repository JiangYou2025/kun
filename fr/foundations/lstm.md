---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/lstm/
title: "LSTM"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)

Le **réseau à longue mémoire à court terme (LSTM, Long Short-Term Memory)** est un [RNN](../rnn/) particulier : grâce à une « autoroute » d'état de cellule et à trois « portes », il décide activement de ce qu'il retient et de ce qu'il oublie. Il peut ainsi mémoriser des dépendances très longues et atténue le problème de l'[évanouissement du gradient](../vanishing-exploding-gradient/) des RNN simples.

## Intuition

Dans un RNN simple, la mémoire est « malaxée » à chaque pas par $\tanh$ ; elle s'estompe au fil de la transmission et, après quelques dizaines de pas, il n'en reste presque rien. Le LSTM change d'approche : il ouvre une voie séparée, l'**état de cellule** (cell state) $c_t$, qui sert d'« artère principale de la mémoire » ; l'information peut y **circuler en ligne droite presque inchangée**, à l'abri des perturbations.

Mais comment ajouter ou effacer des souvenirs ? Le LSTM dispose de trois **portes** (gates), chacune étant un petit interrupteur dont la sortie est comprise entre $0\sim1$ :

- la **porte d'oubli** décide quels éléments de l'ancienne mémoire jeter (0 = tout oublier, 1 = tout garder) ;
- la **porte d'entrée** décide quelle part de l'information nouvelle de ce pas est écrite en mémoire ;
- la **porte de sortie** décide quelle part de la mémoire est lue pour former la sortie courante.

Une image : $c_t$ est un tapis roulant ; la porte d'oubli retire du tapis les marchandises inutiles, la porte d'entrée y dépose de nouvelles marchandises, et la porte de sortie décide lesquelles montrer à l'extérieur à cet instant.

## Équations des portes

Soit l'entrée courante $x_t$ et l'état caché du pas précédent $h_{t-1}$. Les trois portes et la mémoire candidate s'écrivent ($\sigma$ est la [fonction d'activation](../activation-function/) sigmoïde, de sortie $0\sim1$) :

$$
\begin{aligned}
f_t &= \sigma\!\big(W_f [h_{t-1}, x_t] + b_f\big) &\text{(porte d'oubli)}\\
i_t &= \sigma\!\big(W_i [h_{t-1}, x_t] + b_i\big) &\text{(porte d'entrée)}\\
o_t &= \sigma\!\big(W_o [h_{t-1}, x_t] + b_o\big) &\text{(porte de sortie)}\\
\tilde{c}_t &= \tanh\!\big(W_c [h_{t-1}, x_t] + b_c\big) &\text{(mémoire candidate)}
\end{aligned}
$$

On met ensuite à jour l'état de cellule et l'état caché :

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
\qquad
h_t = o_t \odot \tanh(c_t)
$$

Explication symbole par symbole :

- $[h_{t-1}, x_t]$ : la mémoire du pas précédent et l'entrée courante **concaténées** en un long vecteur.
- $f_t, i_t, o_t$ : les trois vecteurs de portes, dont chaque composante est comprise entre $0\sim1$ et agit élément par élément comme un « interrupteur ».
- $\tilde{c}_t$ : la « nouvelle mémoire candidate » que l'on souhaite écrire à ce pas, à valeurs dans $(-1,1)$.
- $\odot$ : **produit élément par élément** (produit de Hadamard) ; la porte agit comme une vanne qui met à l'échelle chaque dimension.
- $c_t$ : l'état de cellule, $=$ (ancienne mémoire conservée selon $f_t$) $+$ (nouvelle mémoire écrite selon $i_t$).
- $h_t$ : l'état caché transmis à l'extérieur, c'est-à-dire la partie de l'état de cellule, passé par $\tanh$, lue selon $o_t$.
- $W_\ast, b_\ast$ : les poids et biais propres à chaque porte, partagés par tous les pas de temps.

## Pourquoi l'état de cellule retient l'information à long terme

Tout repose sur la mise à jour **additive** $c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$.

Rappelons le problème du RNN : $\partial h_t / \partial h_{t-1}$ fait intervenir de façon répétée $W_h$ et $\tanh'$, et le produit de ces facteurs tend vers 0. Pour le LSTM, en dérivant le long de l'état de cellule :

$$
\frac{\partial c_t}{\partial c_{t-1}} = f_t
$$

Si la porte d'oubli vérifie $f_t \approx 1$, le gradient **remonte presque intact**, et même après un produit sur de nombreux pas il ne s'effondre pas vers 0. Cette voie « addition + porte proche de 1 » est appelée **carrousel d'erreur constante (CEC, constant error carousel)** : c'est la raison fondamentale pour laquelle le LSTM peut se souvenir d'informations vieilles de plusieurs centaines de pas sans souffrir facilement de l'évanouissement du gradient.

Intuitivement : sur $c_t$, l'information « file tout droit » au lieu d'être « sans cesse multipliée par des matrices et comprimée », ce qui lui permet d'aller loin.

## Un exemple concret

Supposons qu'une dimension de l'état de cellule vaille actuellement $c_{t-1} = 0.8$ (elle encode l'information « le sujet en début de phrase est au pluriel »). À ce pas :

- porte d'oubli $f_t = 0.95$ → on décide de conserver l'essentiel de cette information ;
- porte d'entrée $i_t = 0.10$, candidate $\tilde{c}_t = 0.5$ → on n'écrit qu'un tout petit peu d'information nouvelle ;
- porte de sortie $o_t = 0.60$.

On obtient alors :

$$
c_t = 0.95\times 0.8 + 0.10\times 0.5 = 0.76 + 0.05 = 0.81
$$

$$
h_t = 0.60 \times \tanh(0.81) \approx 0.60 \times 0.670 = 0.402
$$

La mémoire passe de $0.8 \to 0.81$, quasiment inchangée — l'information « sujet au pluriel » est transportée de façon fiable vers la suite, et ne sera lue via la porte de sortie qu'au moment où elle servira réellement (par exemple pour accorder le verbe). Dans PyTorch, un simple appel suffit :

```python
import torch, torch.nn as nn

lstm = nn.LSTM(input_size=1, hidden_size=16, num_layers=1, batch_first=True)
x = torch.randn(8, 96, 1)             # (lot=8, 96 pas de temps, 1 variable)
out, (h_n, c_n) = lstm(x)
print(out.shape)             # (8, 96, 16) : état caché à chaque pas
print(h_n.shape, c_n.shape)  # h et c au dernier pas
```

## Signification pour la prévision de séries temporelles

Avant que les Transformers ne s'imposent, le LSTM était **la réponse standard pour la prévision de longues séquences** : il peut retenir des tendances et des cycles lointains (comme la saisonnalité annuelle), tout en étant bien plus stable qu'un RNN simple, et il a été largement utilisé pour prévoir les ventes, la consommation électrique, la météo, etc.

Mais il **hérite toujours du calcul séquentiel des RNN** — il faut calculer pas à pas, ce qui rend l'entraînement et l'inférence lents sur de longues séquences, et il peine encore sur des horizons de prévision très longs. Cela a poussé à adopter des architectures parallélisables et multi-échelles : le [Transformer](../transformer/), ainsi que le **Kernel U-Net (KUN)** mis en avant sur ce site. KUN reprend l'idée multirésolution de [U-Net](../u-net/) et modélise simultanément plusieurs échelles temporelles : il contourne ainsi le goulot d'étranglement de la « récurrence pas à pas » tout en captant mieux les structures à longue portée.

## En résumé

- LSTM = RNN + **état de cellule $c_t$** + **trois portes : oubli, entrée, sortie**.
- La mise à jour de la mémoire est **additive** : $c_t = f_t\odot c_{t-1} + i_t\odot\tilde{c}_t$ ; les portes décident de ce qu'on retient, oublie et lit.
- $\partial c_t/\partial c_{t-1} = f_t \approx 1$ forme un carrousel d'erreur constante qui **atténue l'évanouissement du gradient** et permet de mémoriser des dépendances longues.
- Il reste un modèle séquentiel, difficile à paralléliser — la prévision à long horizon a favorisé l'essor du [Transformer](../transformer/) et du KUN multi-échelle.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours de base](../)
