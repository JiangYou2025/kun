---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/dropout/
title: "Dropout"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Le **Dropout (désactivation aléatoire)** est une technique de [régularisation](../regularization/) : pendant l'entraînement, on met temporairement à zéro, au hasard, la sortie d'une partie des [neurones](../neuron/), ce qui oblige le réseau à ne pas trop dépendre de quelques unités ; on réduit ainsi le [surapprentissage](../overfitting/) et l'on améliore la [généralisation](../generalization/).

## Intuition

Imaginez une équipe projet qui s'en remet toujours à une ou deux vedettes : le jour où elles sont absentes, toute l'équipe est paralysée. Changeons de méthode de management : à chaque réunion, on désigne au hasard des membres qui « ne prendront pas la parole aujourd'hui ». À la longue, chacun doit apprendre à travailler de façon autonome et à suppléer les autres, et l'équipe entière devient plus robuste.

Le Dropout fait exactement cela avec les neurones. Pendant l'entraînement, **à chaque [batch](../batch/), un groupe de neurones est déclaré « absent » au hasard** (sa sortie passe à 0), et les neurones restants doivent accomplir la tâche quelle que soit la « formation incomplète » du moment. Les caractéristiques apprises par le réseau deviennent ainsi **redondantes et robustes**, au lieu de tout miser sur un chemin fragile.

Il en existe aussi une belle interprétation : chaque désactivation aléatoire revient à entraîner un **sous-réseau différent**, et le modèle final approche un « ensemble » (ensemble) d'un nombre exponentiel de sous-réseaux — or un ensemble surapprend généralement moins qu'un modèle isolé.

## Principe : le masque pendant l'entraînement

Soit $x = (x_1, x_2, \dots, x_n)$ le vecteur de sortie d'une couche, et une **probabilité de conservation** $p$ (keep probability ; par exemple $p=0.8$ signifie que chaque unité a 80 % de chances d'être conservée). Pendant l'entraînement, on tire indépendamment un masque 0/1 pour chaque unité :

$$
m_i \sim \text{Bernoulli}(p), \qquad \tilde{x}_i = m_i \cdot x_i
$$

- $m_i$ : le masque de l'unité $i$, qui vaut 1 (conservée) avec probabilité $p$ et 0 (supprimée) avec probabilité $1-p$.
- $1-p$ s'appelle le **taux de dropout** (drop rate), généralement entre 0,2 et 0,5.
- $\tilde{x}_i$ : la sortie après désactivation ; une unité supprimée vaut simplement 0 et ne participe ni à la propagation avant ni à la rétropropagation de cette étape.

Remarque : une unité mise à zéro **n'a pas de [gradient](../gradient/)** à cette étape ; on « entraîne aléatoirement un sous-réseau » au sens propre.

## Mise à l'échelle à l'inférence (détail crucial)

Au test / à l'inférence, on **ne supprime plus rien au hasard** — on veut une prédiction déterministe avec le réseau complet. Mais cela pose un problème : pendant l'entraînement, une unité n'est active qu'avec probabilité $p$ en moyenne, si bien que la couche suivante reçoit une entrée d'espérance $p\cdot x$ ; à l'inférence, toutes les unités sont actives et l'entrée devient soudain $x$, soit une amplitude multipliée par $1/p$ : les distributions ne correspondent plus.

La solution consiste à **remettre les espérances à l'échelle**. Deux approches équivalentes :

1. **Mise à l'échelle à l'inférence** : lors de la prédiction, on multiplie les poids (ou les activations) par $p$ pour retrouver l'ordre de grandeur moyen de l'entraînement.
2. **Inverted Dropout (la plus courante)** : dès l'entraînement, on divise par $p$ les unités conservées ; à l'inférence, **il n'y a rien à faire** :

$$
\text{Entraînement :}\ \tilde{x}_i = \frac{m_i \cdot x_i}{p}, \qquad \text{Inférence :}\ \tilde{x}_i = x_i
$$

Dans les deux cas, l'objectif est de garantir que **la sortie attendue soit la même à l'entraînement et à l'inférence**. Les frameworks modernes (comme `nn.Dropout` de PyTorch) utilisent par défaut l'Inverted Dropout, qui n'agit qu'en mode `model.train()` et se désactive automatiquement en mode `model.eval()` — à retenir absolument.

{% include fviz/dropout.html %}

## Un exemple concret

Prenons un taux de dropout $1-p = 0.5$ (soit $p=0.5$) et une sortie de couche $x = [2, 4, 6, 8]$. Lors d'une itération d'entraînement, on tire le masque $m = [1, 0, 1, 0]$ ; avec l'Inverted Dropout :

$$
\tilde{x} = \frac{[1,0,1,0]\odot[2,4,6,8]}{0.5} = \frac{[2,0,6,0]}{0.5} = [4, 0, 12, 0]
$$

Les deux unités conservées sont multipliées par 2 pour compenser la moitié supprimée. Vérifions l'espérance : $\mathbb{E}[\tilde{x}_1] = 0.5\times 4 + 0.5\times 0 = 2 = x_1$, identique à la valeur d'origine. À l'inférence, on utilise directement $[2,4,6,8]$. Le code correspondant :

```python
import torch, torch.nn as nn

net = nn.Sequential(
    nn.Linear(64, 128), nn.ReLU(),
    nn.Dropout(p=0.3),          # ici, p est le « taux de dropout »
    nn.Linear(128, 1),
)
net.train()   # entraînement : le Dropout est actif
y = net(torch.randn(16, 64))
net.eval()    # inférence : le Dropout est automatiquement désactivé, aucun aléa
```

Attention : dans PyTorch, le `p` de `nn.Dropout(p=...)` est la **probabilité de suppression**, soit l'inverse de la probabilité de conservation $p$ de la formule ci-dessus ; ne les confondez pas.

## Pièges courants

- **Croire que l'inférence supprime encore des neurones au hasard** : non. L'inférence est déterministe ; le Dropout n'agit que pendant l'entraînement.
- **Oublier de passer en mode `eval()`** : si l'on évalue en restant en mode `train()`, les prédictions sont aléatoires et les résultats dégradés.
- **Croire qu'un taux de dropout plus élevé est toujours meilleur** : un taux trop grand (par exemple 0,8) supprime trop d'information et provoque un sous-apprentissage ; on reste généralement entre 0,2 et 0,5.
- **L'empiler sans réfléchir avec [BatchNorm](../batchnorm/)** : utilisés ensemble, ils interfèrent parfois l'un avec l'autre ; la pratique courante est de privilégier BN, ou de placer le Dropout après BN, dans les couches entièrement connectées proches de la sortie.

## Intérêt pour la prévision de séries temporelles

Les échantillons de séries temporelles sont fortement corrélés et le modèle surapprend facilement le bruit de la période d'entraînement. Le Dropout (et ses variantes, comme le dropout récurrent ou le dropout sur la dimension temporelle) est un moyen courant de limiter la complexité du modèle et d'améliorer la généralisation aux données futures. Il est souvent combiné à l'[arrêt précoce](../early-stopping/), à la décroissance des poids, etc., dans la boîte à outils anti-surapprentissage de la [pratique de l'entraînement](../training-practice/), et il est aussi utilisé dans des architectures comme le modèle multi-échelle de ce site, **Kernel U-Net (KUN)**.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
