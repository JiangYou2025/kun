---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/forward-propagation/
title: "Propagation avant"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **propagation avant (forward propagation)** désigne le processus qui consiste à « faire passer » les données d'entrée de la première couche du réseau jusqu'à la dernière, en effectuant couche après couche une « somme pondérée + activation », pour finalement calculer la prédiction. C'est la moitié d'un [réseau de neurones](../neural-network/) qui « prédit » (l'autre moitié, la [rétropropagation](../backpropagation/), se charge de l'« apprentissage »).

## Intuition

Imaginez le réseau de neurones comme une **chaîne de production**. La matière première (les variables d'entrée) arrive à l'entrée, et à chaque poste (chaque couche), elle est transformée une fois : d'abord mélangée selon une certaine recette (somme pondérée linéaire), puis passée à travers une « vanne de contrôle qualité » (la [fonction d'activation](../activation-function/)) qui décide quelle part du signal laisser passer. La matière avance sans jamais revenir en arrière, et le produit fini qui sort à l'autre bout est la **prédiction** du réseau.

Le mot « avant » souligne justement ce **flux à sens unique** : les données ne vont que vers la sortie. Ce n'est que lorsqu'on veut ajuster le réseau en fonction de l'erreur que l'information repart en sens inverse — c'est la rétropropagation.

## Formulation mathématique

Soit un réseau à $L$ couches. Notons $a^{(l-1)}$ le vecteur d'entrée de la couche $l$ (c'est-à-dire la sortie de la couche précédente) ; cette couche possède une matrice de poids $W^{(l)}$ et un vecteur de biais $b^{(l)}$. Elle effectue alors deux opérations :

$$
z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}
$$

$$
a^{(l)} = \sigma\big(z^{(l)}\big)
$$

Explication symbole par symbole :

- $a^{(l-1)}$ : la **sortie activée** de la couche $l-1$ (la couche 0 est l'entrée brute $x$, soit $a^{(0)} = x$).
- $W^{(l)}$ : la **matrice de poids** de la couche $l$, de forme $(\text{neurones de cette couche} \times \text{neurones de la couche précédente})$.
- $b^{(l)}$ : le **biais** de la couche $l$, qui donne à chaque [neurone](../neuron/) une valeur de référence ajustable.
- $z^{(l)}$ : la **somme pondérée** (aussi appelée pre-activation, la valeur avant activation).
- $\sigma(\cdot)$ : la **fonction d'activation**, par exemple ReLU ou sigmoïde (appliquée élément par élément).
- $a^{(l)}$ : la sortie de cette couche, qui devient à son tour l'entrée de la couche suivante.

En enchaînant ces deux étapes de $l=1$ jusqu'à $l=L$, la sortie finale $a^{(L)} = \hat{y}$ est la prédiction du réseau. Toute la chaîne s'écrit comme une composition de fonctions :

$$
\hat{y} = \sigma^{(L)}\Big(W^{(L)} \, \sigma^{(L-1)}\big(\cdots \sigma^{(1)}(W^{(1)} x + b^{(1)}) \cdots\big) + b^{(L)}\Big)
$$

{% include fviz/backprop-graph.html %}

## Un exemple concret

Prenons un réseau minimal : entrée de dimension 2, couche cachée de 2 neurones avec ReLU, couche de sortie à 1 neurone (linéaire). On se donne

$$
x = \begin{bmatrix} 1 \\ 2 \end{bmatrix},\quad
W^{(1)} = \begin{bmatrix} 0.5 & -0.5 \\ 1.0 & 0.0 \end{bmatrix},\quad
b^{(1)} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}
$$

Première étape, la somme pondérée :

$$
z^{(1)} = \begin{bmatrix} 0.5\cdot1 + (-0.5)\cdot2 \\ 1.0\cdot1 + 0\cdot2 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \end{bmatrix}
= \begin{bmatrix} -0.5 \\ 1.0 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \end{bmatrix}
= \begin{bmatrix} -0.5 \\ 0 \end{bmatrix}
$$

Passage par ReLU (les valeurs négatives sont mises à zéro) :

$$
a^{(1)} = \mathrm{ReLU}(z^{(1)}) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Oups — les deux neurones cachés ont été « éteints ». Cela nous rappelle que ReLU fait sortir 0 à une partie des neurones pour certaines entrées. Enfin, la couche de sortie (avec $W^{(2)} = [1, 1],\, b^{(2)} = 0.3$) :

$$
\hat{y} = 1\cdot0 + 1\cdot0 + 0.3 = 0.3
$$

Vérification en code :

```python
import numpy as np

x  = np.array([1.0, 2.0])
W1 = np.array([[0.5, -0.5], [1.0, 0.0]])
b1 = np.array([0.0, -1.0])
W2 = np.array([1.0, 1.0])
b2 = 0.3

z1 = W1 @ x + b1          # [-0.5, 1.0] -> +b1 -> [-0.5, 0.0]
a1 = np.maximum(0, z1)    # ReLU -> [0, 0]
y  = W2 @ a1 + b2         # 0.3
print(z1, a1, y)          # [-0.5  0. ] [0. 0.] 0.3
```

## Pourquoi c'est important / où l'utilise-t-on

- **C'est l'intégralité de l'inférence (inference).** Une fois le modèle déployé, faire une prédiction revient à exécuter la propagation avant — simple et rapide.
- **C'est la première moitié de l'entraînement.** Chaque itération commence par une passe avant pour obtenir $\hat{y}$, puis le calcul de la [perte](../loss-function/) $\mathcal{L}(\hat{y}, y)$, avant de pouvoir rétropropager pour obtenir les gradients.
- Les valeurs intermédiaires $z^{(l)}, a^{(l)}$ conservées pendant la propagation avant sont réutilisées par la [rétropropagation](../backpropagation/) — c'est précisément pourquoi les frameworks de [différentiation automatique](../autodiff/) (PyTorch / TensorFlow) gèrent automatiquement le « graphe de calcul » pour vous.

## Intérêt pour la prévision de séries temporelles

Pour des modèles séquentiels comme les [RNN](../rnn/) et les [LSTM](../lstm/), la propagation avant se déroule le long des **pas de temps** : l'état caché au pas $t$ dépend de celui du pas $t-1$, et l'information avance pas à pas. Le modèle phare de ce site, [Kernel U-Net (KUN)](../../kun/), a quant à lui une structure multi-échelles : la propagation avant sous-échantillonne la longue fenêtre d'historique niveau par niveau, puis la sur-échantillonne niveau par niveau pour la reconstruire — mais le principe reste le même : « transformer l'entrée couche après couche pour obtenir une prédiction ». Comprendre la propagation avant est la première étape pour comprendre le fonctionnement de n'importe quel modèle de prévision.

## En résumé

- Propagation avant = **les données circulent à sens unique de l'entrée vers la sortie**, avec à chaque couche « transformation linéaire + activation ».
- Formules centrales : $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$, $a^{(l)} = \sigma(z^{(l)})$.
- C'est à la fois **la prédiction** elle-même et **la première étape de la boucle d'entraînement** ; les valeurs intermédiaires sont conservées pour la rétropropagation.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
