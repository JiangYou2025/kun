---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/batchnorm/
title: "BatchNorm (normalisation par lots)"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **normalisation par lots (BatchNorm, Batch Normalization)** est une opération placée entre les couches d'un réseau : sur chaque [mini-lot](../batch/) (mini-batch), elle « ramène » l'entrée d'une couche à une moyenne nulle et une variance unitaire, puis la remet à l'échelle et la décale à l'aide de deux paramètres apprenables, ce qui rend l'entraînement plus stable et la convergence plus rapide.

## Intuition

Pendant l'entraînement, la distribution des entrées de chaque couche dérive sans cesse à mesure que les paramètres des couches précédentes sont mis à jour — c'est le **décalage de covariables interne** (internal covariate shift). Les couches en aval poursuivent en quelque sorte une cible mouvante : l'apprentissage est laborieux, et la moindre augmentation du taux d'apprentissage le rend instable.

BatchNorm installe à l'entrée de chaque couche un « poste de standardisation » : **quelle que soit l'échelle des données transmises par les couches précédentes, on les ramène d'abord dans une plage stable** (moyenne nulle, variance unitaire) avant de les confier à la couche. Chaque couche voit ainsi une distribution d'entrée relativement stable, et donc :

- on peut utiliser un **[taux d'apprentissage](../learning-rate/) plus élevé**, et l'entraînement est plus rapide ;
- le réseau est moins sensible à l'[initialisation](../training-practice/) des paramètres ;
- on obtient en prime un léger effet de [régularisation](../regularization/) (la normalisation de chaque exemple dépend de tout le batch, ce qui introduit un peu de bruit).

## Formulation mathématique

Soit un mini-batch de $m$ exemples ; pour une dimension de caractéristique donnée, notons $x_1, \dots, x_m$ ses valeurs.

Première étape : calculer la moyenne et la variance du lot :

$$
\mu_B = \frac{1}{m}\sum_{i=1}^{m} x_i,
\qquad
\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m} (x_i - \mu_B)^2
$$

Deuxième étape : **normaliser** (normalize) :

$$
\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

Troisième étape : **mettre à l'échelle et décaler** (scale and shift) :

$$
y_i = \gamma\,\hat{x}_i + \beta
$$

Explication symbole par symbole :

- $\mu_B,\ \sigma_B^2$ : la moyenne et la variance du batch courant sur cette dimension de caractéristique.
- $\epsilon$ : une très petite constante (par exemple $10^{-5}$) qui évite un dénominateur nul et garantit la stabilité numérique.
- $\hat{x}_i$ : la valeur normalisée, de distribution approximativement centrée réduite (moyenne 0, variance 1).
- $\gamma$ (échelle), $\beta$ (décalage) : des **paramètres apprenables**, un jeu par dimension de caractéristique, mis à jour par [rétropropagation](../backpropagation/).
- $y_i$ : la sortie finale de la BN.

Pourquoi ajouter $\gamma, \beta$ après la normalisation ? Parce que forcer chaque couche à suivre une « loi normale centrée réduite » pourrait nuire à son pouvoir d'expression. En donnant au réseau ces deux boutons de réglage $\gamma, \beta$, il peut **réapprendre la distribution** si nécessaire (et même retrouver l'entrée d'origine lorsque $\gamma=\sqrt{\sigma_B^2+\epsilon},\ \beta=\mu_B$) ; la BN n'affaiblit donc pas la capacité du modèle.

{% include fviz/batchnorm-hist.html %}

## Entraînement et inférence : la différence (point clé)

C'est là que la BN donne le plus souvent lieu à des erreurs.

- **À l'entraînement** : on utilise $\mu_B, \sigma_B^2$ du **batch courant**. En parallèle, on entretient discrètement des **statistiques globales en moyenne mobile** (running mean / running variance) :

$$
\mu_{run} \leftarrow (1-\alpha)\,\mu_{run} + \alpha\,\mu_B
$$

(de même pour la variance ; $\alpha$ est le momentum, 0,1 par défaut dans PyTorch.)

- **À l'inférence** : un exemple isolé ne forme pas de « batch », et la prédiction ne devrait pas dépendre des autres exemples qui se trouvent fournis en même temps. À l'inférence, on **n'utilise donc plus les statistiques du lot courant**, mais les $\mu_{run}, \sigma_{run}^2$ accumulées pendant l'entraînement, pour une normalisation fixe :

$$
y = \gamma\,\frac{x - \mu_{run}}{\sqrt{\sigma_{run}^2 + \epsilon}} + \beta
$$

Conseil pratique : dans PyTorch, passez impérativement en mode inférence avec `model.eval()` pour que la BN utilise les statistiques running ; oublier ce changement fait fluctuer les prédictions selon la composition du batch et dégrade les résultats. Par ailleurs, lorsque le **batch est très petit** (1 ou 2 exemples, par exemple), les statistiques sont très bruitées et la BN fonctionne mal ; on lui préfère alors souvent LayerNorm.

## Un exemple concret

Supposons qu'une caractéristique prenne 4 valeurs dans un batch, $x = [1, 2, 3, 4]$, et négligeons $\epsilon$ :

$$
\mu_B = \frac{1+2+3+4}{4} = 2.5,\qquad
\sigma_B^2 = \frac{(1.5)^2+(0.5)^2+(0.5)^2+(1.5)^2}{4} = 1.25
$$

$$
\hat{x} = \frac{[1,2,3,4] - 2.5}{\sqrt{1.25}} \approx [-1.342,\ -0.447,\ 0.447,\ 1.342]
$$

Après normalisation, la moyenne vaut environ 0 et la variance environ 1. Si le réseau a appris $\gamma=2,\ \beta=5$, la sortie est $y = 2\hat{x}+5 \approx [2.32,\ 4.11,\ 5.89,\ 7.68]$. Le code correspondant :

```python
import torch, torch.nn as nn

net = nn.Sequential(
    nn.Linear(32, 64),
    nn.BatchNorm1d(64),   # normalise séparément chacune des 64 caractéristiques
    nn.ReLU(),
    nn.Linear(64, 1),
)
net.train(); y = net(torch.randn(16, 32))   # entraînement : statistiques du batch
net.eval();  y = net(torch.randn(16, 32))   # inférence : statistiques running
```

## Résumé

- La BN **normalise** sur chaque batch (soustraction de la moyenne, division par l'écart-type), puis **met à l'échelle et décale** avec les paramètres apprenables $\gamma,\beta$.
- $\epsilon$ évite la division par zéro ; $\gamma,\beta$ préservent le pouvoir d'expression.
- **Statistiques du batch à l'entraînement, statistiques en moyenne mobile à l'inférence** — pensez à passer en `eval()`.
- Elle stabilise les distributions, autorise un [taux d'apprentissage](../learning-rate/) plus élevé, accélère la convergence et apporte une légère régularisation ; à utiliser avec prudence avec de petits batchs.
- Avec le [Dropout](../dropout/) et l'[arrêt précoce](../early-stopping/), elle fait partie des outils courants des [bonnes pratiques d'entraînement](../training-practice/).

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
