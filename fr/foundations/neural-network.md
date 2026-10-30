---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/neural-network/
title: "Réseaux de neurones"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)

Un **réseau de neurones (Neural Network)** est un modèle mathématique formé d'un grand nombre d'unités de calcul simples — les [neurones](../neuron/) — connectées en couches. Il calcule sa sortie par [propagation avant](../forward-propagation/), puis apprend ses paramètres à partir de ses erreurs par [rétropropagation](../backpropagation/), afin de transformer une « entrée » en la « sortie » souhaitée.

## Intuition

Imaginez une chaîne de production. La matière première (les données d'entrée, par exemple la température des 96 derniers instants) entre par un bout, traverse un « atelier de transformation » après l'autre, et le produit fini sort à l'autre bout (par exemple la prévision de température pour les 24 prochains instants).

Chaque atelier compte de nombreux ouvriers (les neurones). Chacun accomplit une tâche extrêmement simple :

1. multiplier chacun des nombres venus de la couche précédente par un « degré d'importance » (le poids $w$) ;
2. tout additionner, puis ajouter un biais $b$ ;
3. faire passer le résultat par un « interrupteur » non linéaire (la [fonction d'activation](../activation-function/)).

Un ouvrier seul est bien limité, mais des milliers d'ouvriers collaborant couche par couche peuvent, ensemble, reproduire des régularités extrêmement complexes. **La puissance d'un réseau de neurones ne vient pas d'un neurone isolé, mais de la composition en couches et du nombre colossal de paramètres.**

## Formulation mathématique

Le calcul d'un neurone est une « somme pondérée + activation » :

$$
a = \sigma\!\left( \sum_{i=1}^{n} w_i x_i + b \right)
$$

- $x_i$ : la $i$-ième composante de l'entrée (la sortie de la couche précédente) ;
- $w_i$ : le poids correspondant, qui indique l'importance de cette entrée ; c'est un paramètre à apprendre ;
- $b$ : le biais, qui donne au neurone une ligne de base ajustable ;
- $\sum_{i=1}^{n} w_i x_i + b$ : la somme pondérée, une opération linéaire ;
- $\sigma(\cdot)$ : la fonction d'activation (ReLU, sigmoïde, etc.), qui introduit la non-linéarité ;
- $a$ : la sortie du neurone (activation).

Il est plus compact d'écrire une couche entière de neurones sous forme matricielle :

$$
\mathbf{h}^{(l)} = \sigma\!\left( \mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)} \right)
$$

- $\mathbf{h}^{(l-1)}$ : le vecteur de sortie de la couche $l-1$ (pour la première couche, c'est l'entrée $\mathbf{x}$) ;
- $\mathbf{W}^{(l)}$ : la matrice de poids de la couche $l$, dont chaque ligne correspond à un neurone de la couche ;
- $\mathbf{b}^{(l)}$ : le vecteur de biais de la couche $l$ ;
- $\mathbf{h}^{(l)}$ : la sortie de la couche $l$.

Le réseau tout entier consiste à appliquer cette formule de la couche 1 jusqu'à la couche $L$ : l'entrée entre, la sortie sort, et ce trajet s'appelle la **propagation avant**.

### Pourquoi la fonction d'activation est indispensable

Sans $\sigma$, l'empilement de plusieurs couches $\mathbf{W}^{(3)}(\mathbf{W}^{(2)}(\mathbf{W}^{(1)}\mathbf{x}))$ n'est toujours qu'une seule transformation linéaire $\mathbf{W}'\mathbf{x}$ — quel que soit le nombre de couches, cela équivaut à une seule, incapable d'exprimer des relations non linéaires comme des courbes, des points d'inflexion ou des seuils. **La fonction d'activation est la clé qui permet au réseau d'être « profond » et « puissant ».**

## Comment il apprend

À l'initialisation, les poids sont aléatoires et la sortie n'est guère plus qu'une devinette. L'apprentissage tourne en boucle sur trois étapes :

1. **Propagation avant** : calculer la prédiction $\hat{y}$ avec les paramètres actuels ;
2. **Calcul de la perte** : mesurer l'écart entre la prédiction et la valeur réelle $y$ à l'aide d'une [fonction de perte](../loss-function/), par exemple l'erreur quadratique moyenne
   $$ \mathcal{L} = \frac{1}{N}\sum_{j=1}^{N}\left(\hat{y}_j - y_j\right)^2 $$
   où $N$ est le nombre d'exemples, $\hat{y}_j$ la prédiction et $y_j$ la valeur réelle ;
3. **[Rétropropagation](../backpropagation/) + [optimiseur](../optimizer/)** : calculer, grâce à la [règle de dérivation en chaîne](../chain-rule/), le [gradient](../gradient/) $\frac{\partial \mathcal{L}}{\partial w}$ de la perte par rapport à chaque paramètre, puis ajuster légèrement les paramètres dans la direction opposée au gradient :
   $$ w \leftarrow w - \eta \,\frac{\partial \mathcal{L}}{\partial w} $$
   $\eta$ est le [taux d'apprentissage](../learning-rate/), qui règle la taille de chaque pas.

En répétant ces trois étapes des milliers de fois sur de grandes quantités de données, les paramètres convergent peu à peu vers des valeurs qui donnent de bonnes prédictions.

## Un exemple concret

Construisons, dans le style de PyTorch, un réseau à 3 couches qui transforme 96 pas d'historique en 24 pas de prévision :

```python
import torch.nn as nn

net = nn.Sequential(
    nn.Linear(96, 128),   # couche 1 : 96 dimensions -> 128 dimensions
    nn.ReLU(),            # activation
    nn.Linear(128, 64),   # couche 2 : 128 -> 64
    nn.ReLU(),
    nn.Linear(64, 24),    # couche de sortie : 64 -> 24 pas de prévision
)

x = torch.randn(32, 96)  # un lot de 32 exemples, chacun avec 96 pas d'historique
y_hat = net(x)           # forme (32, 24)
```

Ces quelques lignes forment un réseau de neurones complet et entraînable : les trois `Linear` sont les matrices de poids, `ReLU` est la fonction d'activation, et `net(x)` effectue en interne exactement la suite de multiplications matricielles décrite plus haut.

## Intérêt pour la prévision de séries temporelles

Au fond, prévoir une série temporelle revient à apprendre une fonction $f$ qui envoie la fenêtre d'historique $[x_{t-95}, \dots, x_t]$ vers le futur $[x_{t+1}, \dots, x_{t+24}]$. Les réseaux de neurones excellent justement à **apprendre automatiquement ce genre de correspondance complexe à partir des données**, sans qu'il faille fixer à la main la forme du modèle.

Des tâches différentes ont donné naissance à des structures différentes (qui sont toutes des réseaux de neurones) : le [CNN](../cnn/) pour les motifs locaux, le [RNN](../rnn/) / [LSTM](../lstm/) pour les dépendances séquentielles, l'[attention](../attention/) et le [Transformer](../transformer/) pour les relations à longue portée ; quant au modèle de prévision multi-échelle mis en avant sur ce site, le **Kernel U-Net (KUN)**, il repose sur la structure [U-Net](../u-net/). Comprendre le cadre général des réseaux de neurones est le préalable pour saisir ces [architectures](../architectures/) spécialisées.

## En résumé

- Un réseau de neurones = un grand nombre de neurones connectés en couches, paramétrés par des **poids** et des **biais**.
- La **propagation avant** calcule la sortie ; la **rétropropagation + l'optimiseur** mettent à jour les paramètres.
- La **fonction d'activation** apporte la non-linéarité ; c'est elle qui donne son sens à la « profondeur ».
- Un même cadre se décline en architectures diverses : [MLP](../mlp/), CNN, Transformer, U-Net, etc.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble du cours de base](../)
