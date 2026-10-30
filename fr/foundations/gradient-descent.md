---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/gradient-descent/
title: "Descente de gradient"
no_comments: true
math: true
---

> Extrait des [Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)

La descente de gradient est un [algorithme](../algorithms/) d'[optimisation](../optimization/) itératif : à chaque étape, on fait un petit pas dans la **direction opposée** au [gradient](../gradient/) de la [fonction de perte](../loss-function/), pour se rapprocher progressivement du minimum. Presque tous les modèles modernes sont entraînés grâce à elle.

## Intuition

Imaginez-vous sur le flanc d'une montagne, dans un épais brouillard : vous ne voyez pas la montagne entière et voulez simplement rejoindre le fond de la vallée au plus vite. Tout ce que vous percevez, c'est **la direction la plus pentue sous vos pieds**. La stratégie est simple :

1. repérer la direction de descente la plus raide sous vos pieds (c'est-à-dire la direction du gradient négatif) ;
2. faire un pas dans cette direction ;
3. recommencer, jusqu'à ce que tout soit plat autour de vous (gradient proche de 0).

La longueur du pas est le **[taux d'apprentissage](../learning-rate/)**. Des pas trop petits rendent la descente désespérément lente ; des pas trop grands risquent d'enjamber le fond de la vallée, de faire des allers-retours d'un versant à l'autre, voire de remonter de plus en plus haut.

{% include fviz/optimizer.html %}

## Formulation mathématique

La règle de mise à jour :

$$
\theta \leftarrow \theta - \eta\,\nabla L(\theta)
$$

- $\theta$ — les paramètres du modèle (parfois un vecteur de plusieurs millions de dimensions) ;
- $L(\theta)$ — la fonction de perte, qui mesure à quel point les paramètres actuels sont mauvais ;
- $\nabla L(\theta)$ — le [gradient](../gradient/) de la perte par rapport aux paramètres, qui pointe vers la direction de **montée la plus rapide**, d'où le signe moins ;
- $\eta$ — le **taux d'apprentissage (learning rate)**, qui contrôle la longueur de chaque pas.

Trois variantes courantes, qui diffèrent par « la quantité de données utilisée à chaque pas pour estimer le gradient » :

- **Descente par [lot](../batch/) complet (Batch GD)** : utilise toutes les données ; gradient précis mais lent.
- **Stochastique (SGD)** : un seul échantillon à la fois ; rapide mais très bruité.
- **Par mini-lots (Mini-batch)** : un petit lot à chaque fois (par exemple 32 ou 64 échantillons) ; c'est la pratique standard en apprentissage profond, qui concilie vitesse et stabilité.

En pratique, on utilise souvent des versions améliorées avec quantité de mouvement (Momentum, [Adam](../adam/), etc.), qui accélèrent la convergence et atténuent les oscillations.

## Un exemple concret

Minimisons $L(\theta)=\theta^2$, dont le gradient est $\nabla L=2\theta$. Avec un taux d'apprentissage $\eta=0.1$ et en partant de $\theta_0=5$ :

$$
\theta_1=5-0.1\cdot 10=4.0,\quad \theta_2=4-0.1\cdot 8=3.2,\quad \theta_3=3.2-0.1\cdot 6.4=2.56,\ \dots
$$

Le paramètre se rapproche pas à pas de l'optimum 0.

```python
theta, lr = 5.0, 0.1
for step in range(20):
    grad = 2 * theta          # gradient de L = theta^2
    theta -= lr * grad
    print(step, round(theta, 4))
# theta tend progressivement vers 0
```

Essayez de passer $\eta$ à $1.1$ : vous verrez que $\theta$ ne converge pas mais **diverge** — c'est la conséquence d'un taux d'apprentissage trop grand.

## Pourquoi c'est important / où l'utilise-t-on

- **Le moteur universel de l'entraînement** : de la régression linéaire aux grands réseaux de neurones, l'apprentissage des paramètres repose presque toujours sur la descente de gradient (ou l'une de ses variantes).
- Associée à la **[rétropropagation](../backpropagation/)** (la [règle de dérivation en chaîne](../chain-rule/)), qui calcule efficacement le gradient, elle met ensuite à jour les paramètres selon cette règle.
- Sur les problèmes d'[optimisation convexe](../convex-optimization/), elle converge vers l'optimum global ; sur les problèmes non convexes (apprentissage profond), elle converge vers une solution locale « suffisamment bonne ».

## Intérêt pour la prévision de séries temporelles

- Tous les paramètres apprenables de KUN (Kernel U-Net) sont entraînés par descente de gradient par mini-lots + Adam sur la perte de prévision (par exemple la MSE).
- Les plans de taux d'apprentissage (warmup, décroissance cosinus), l'écrêtage du gradient et autres techniques visent précisément à faire converger la descente de gradient de façon stable sur de longues séquences et des réseaux profonds.
- Comprendre le compromis « longueur du pas contre convergence » aide à diagnostiquer les problèmes courants : entraînement qui ne converge pas, loss qui oscille ou qui explose.

## Idées reçues fréquentes

- **Le taux d'apprentissage est l'hyperparamètre numéro un** : trop grand, on diverge ; trop petit, on stagne ; il faut le régler.
- Un gradient nul n'indique pas forcément un minimum (ce peut être un point selle ou un minimum local) ; il faut y être particulièrement attentif dans les problèmes non convexes.
- Pensez impérativement à **normaliser les variables** : des variables d'échelles très différentes transforment la surface de perte en une vallée étroite et allongée, où la descente est très inefficace.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours fondamentaux](../)
