---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/chain-rule/
title: "La règle de dérivation en chaîne"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

La règle de dérivation en chaîne permet de dériver une **fonction composée** (une fonction dans une fonction) : le taux de variation global = taux de variation de la couche externe × taux de variation de la couche interne. C'est le moteur mathématique de la **[rétropropagation](../backpropagation/)** dans les [réseaux de neurones](../neural-network/).

## Intuition

Imaginez une chaîne de transmission : l'engrenage A entraîne l'engrenage B, qui entraîne à son tour l'engrenage C.

- Quand A fait un tour, B en fait 3 (le « rapport de démultiplication » de B par rapport à A est 3) ;
- quand B fait un tour, C en fait 2 (le rapport de C par rapport à B est 2) ;
- donc quand A fait un tour, C en fait **3 × 2 = 6**.

Les rapports (taux de variation) se transmettent en se **multipliant**. C'est exactement ce que dit la règle de dérivation en chaîne : lorsque $x$ influence $u$ et que $u$ influence à son tour $y$, l'influence totale de $x$ sur $y$ est le produit des deux influences.

{% include fviz/chain-rule.html %}

## Formulation mathématique

Soit $y=f(u)$ et $u=g(x)$, c'est-à-dire $y=f(g(x))$ ; alors

$$
\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\cdot g'(x)
$$

- $\dfrac{dy}{du}$ est la dérivée de la fonction **externe** (évaluée en la valeur de la fonction interne) ;
- $\dfrac{du}{dx}$ est la dérivée de la fonction **interne** ;
- leur produit donne la dérivée globale.

Avec plusieurs niveaux d'imbrication, on continue à multiplier : si $y=f(g(h(x)))$, alors

$$
\frac{dy}{dx}=f'\cdot g'\cdot h'
$$

La version à plusieurs variables (la forme réellement utilisée dans les réseaux de neurones) remplace le produit par une **somme sur tous les chemins** :

$$
\frac{\partial L}{\partial x}=\sum_i \frac{\partial L}{\partial u_i}\frac{\partial u_i}{\partial x}
$$

## Un exemple concret

Calculons la dérivée de $y=(3x+1)^2$.

Posons la fonction interne $u=3x+1$ et la fonction externe $y=u^2$.

$$
\frac{dy}{du}=2u,\qquad \frac{du}{dx}=3
$$

$$
\frac{dy}{dx}=2u\cdot 3=2(3x+1)\cdot 3=18x+6
$$

Vérification : en développant, $y=9x^2+6x+1$, dont la dérivée directe est $18x+6$ — c'est cohérent.

```python
import sympy as sp
x = sp.symbols('x')
y = (3*x + 1)**2
print(sp.diff(y, x))   # 18*x + 6
```

## Pourquoi c'est important / où l'utilise-t-on

La règle de dérivation en chaîne est tout le secret de la **rétropropagation (backpropagation)**. Un réseau de neurones n'est qu'une longue suite de fonctions composées :

$$
L\big(f_n(\cdots f_2(f_1(x))\cdots)\big)
$$

Pour connaître l'influence d'un paramètre situé tôt dans le réseau sur la perte finale $L$, on **multiplie** les dérivées locales de chaque couche le long du chemin qui mène de ce paramètre à $L$. Les frameworks (PyTorch, TensorFlow) le font automatiquement pour vous via l'autograd, mais ce qu'ils font, c'est précisément appliquer la règle de dérivation en chaîne.

Elle explique aussi l'**[évanouissement / l'explosion du gradient](../vanishing-exploding-gradient/)** : le produit de nombreuses dérivées inférieures à 1 tend vers 0 (évanouissement), celui de nombreuses dérivées supérieures à 1 explose — c'est l'effet secondaire de ces produits en cascade.

## Signification pour la prévision de séries temporelles

- KUN (Kernel U-Net) possède une structure à plusieurs couches — encodeur, opérations à noyau, décodeur, etc. ; pendant l'entraînement, le [gradient](../gradient/) de la perte par rapport aux paramètres des couches les plus basses remonte couche par couche grâce à la règle de dérivation en chaîne.
- Un modèle séquentiel ([RNN](../rnn/)), une fois déroulé le long des pas de temps, est une fonction composée extrêmement profonde ; la « rétropropagation à travers le temps (BPTT) » n'est au fond qu'un produit en chaîne le long de l'axe temporel, ce qui explique aussi pourquoi les longues séquences sont difficiles à entraîner.

## En résumé

- Dériver une fonction composée = **multiplier** les dérivées locales de chaque couche (et additionner lorsqu'il y a plusieurs chemins).
- C'est le fondement mathématique de la rétropropagation, qui rend les réseaux profonds entraînables.
- Le caractère multiplicatif apporte l'efficacité, mais aussi le risque d'évanouissement ou d'explosion du gradient.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
