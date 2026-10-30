---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/u-net/
title: "U-Net"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Le **U-Net** est une architecture **encodeur–décodeur** munie de **connexions de saut (skip connections)** : l'encodeur sous-échantillonne progressivement les données pour les compresser en représentations multi-échelles de plus en plus grossières et abstraites, le décodeur les sur-échantillonne progressivement pour reconstruire, et les connexions de saut font « prendre un raccourci » aux détails de chaque niveau jusqu'au niveau de reconstruction correspondant. Il doit son nom à sa forme de lettre **U**. Le modèle de prévision phare de ce site, **Kernel U-Net (KUN)**, en est directement issu.

## Intuition

Pensez-y comme à la manière dont un peintre travaille :

- **L'encodeur (descente, voir l'ensemble)** : on plisse d'abord les yeux pour voir le tout — on réduit progressivement la résolution, on élimine le bruit local et on voit clairement « où est le sujet, quelle est la tendance générale ». À chaque sous-échantillonnage, le champ de vision s'élargit et l'information devient plus synthétique.
- **Le décodeur (montée, ajouter les détails)** : on agrandit ensuite progressivement, en repeignant cette vue d'ensemble abstraite en une sortie fine.
- **Les connexions de saut (latérales, prendre un raccourci)** : la reconstruction par le seul décodeur perdrait des détails comme les contours et les textures, écrasés lors du sous-échantillonnage. On relie donc directement, latéralement, les caractéristiques de chaque niveau de l'encodeur — **quand elles sont encore nettes** — au niveau correspondant du décodeur. **La vue d'ensemble vient des profondeurs, les détails viennent des connexions de saut** : leur fusion permet d'être à la fois juste et précis.

En une phrase : **le U-Net travaille simultanément à plusieurs échelles — les couches profondes s'occupent du « long terme, grossier », les couches superficielles du « local, fin », et les connexions de saut évitent de sacrifier l'un à l'autre.**

## Principe

Supposons que l'encodeur ait $S$ échelles. L'encodage au niveau $s$ :

$$
\mathbf{e}_s = \mathrm{Down}\big( f_s(\mathbf{e}_{s-1}) \big),\qquad \mathbf{e}_0 = \mathbf{x}
$$

- $\mathbf{x}$ : l'entrée (une image, ou une fenêtre de série temporelle) ;
- $f_s$ : la transformation de caractéristiques à cette échelle (un bloc de convolution dans le U-Net d'origine, remplacé par un « noyau » léger dans KUN) ;
- $\mathrm{Down}$ : le sous-échantillonnage (pooling ou convolution avec pas), qui réduit la taille et élargit le champ réceptif ;
- $\mathbf{e}_s$ : la sortie de l'encodeur au niveau $s$, d'autant plus grossière et abstraite qu'on descend.

Le niveau le plus bas s'appelle le **goulot (bottleneck)** : c'est la résolution la plus faible, la représentation la plus synthétique. Ensuite, le décodeur sur-échantillonne niveau par niveau en fusionnant les connexions de saut :

$$
\mathbf{d}_s = g_s\big(\, [\,\mathrm{Up}(\mathbf{d}_{s+1});\ \mathbf{e}_s\,]\,\big)
$$

- $\mathrm{Up}$ : le sur-échantillonnage (interpolation ou convolution transposée), qui augmente à nouveau la résolution ;
- $[\,\cdot\,;\,\cdot\,]$ : la **concaténation** — on accole le résultat du sur-échantillonnage aux caractéristiques d'encodage de même échelle $\mathbf{e}_s$ ; c'est cela, la connexion de saut ;
- $g_s$ : la transformation côté décodeur à cette échelle ;
- $\mathbf{d}_s$ : la sortie du décodeur au niveau $s$.

En remontant niveau par niveau jusqu'au sommet, on obtient une sortie de même taille que l'entrée. **La forme en U symétrique + les connexions de saut entre échelles identiques sont les deux signatures du U-Net.**

Les connexions de saut ont un autre avantage : elles offrent au [gradient](../gradient/) un chemin court, ce qui atténue la [disparition / explosion du gradient](../vanishing-exploding-gradient/) dans les réseaux profonds (pour la même raison que les connexions résiduelles).

## Un exemple concret (version 1D / séries temporelles)

Appliquons le U-Net à une séquence de longueur $L$ et voyons comment évoluent les tailles (chaque sous-échantillonnage divise par deux) :

```
Entrée      L = 96   ──┐ connexion de saut
  ↓ Down              │
Échelle 1   48   ──┐  │
  ↓ Down            │  │
Échelle 2   24   ─┐ │  │
  ↓ Down          │ │  │
Goulot      12    │ │  │   ← vue la plus grossière, à la plus longue portée
  ↑ Up            │ │  │
Échelle 2   24 ◄──┘ │  │   ← on recolle les détails de l'échelle 2
  ↑ Up              │  │
Échelle 1   48 ◄────┘  │
  ↑ Up                 │
Sortie      96 ◄───────┘   ← on recolle les détails les plus fins
```

En descendant, la résolution passe de $96\to48\to24\to12$, et au niveau 12 le modèle « voit tout l'ensemble d'un seul coup d'œil » ; en remontant, il reconstruit progressivement, en recollant à chaque étape les détails conservés à l'échelle correspondante. La sortie finale peut être un masque de segmentation (image) ou une séquence future (prévision).

{% include fviz/unet-1d.html %}

## Pourquoi c'est important / où l'utiliser

- **Le multi-échelles est son âme** : modéliser à la fois la « structure globale » et les « détails locaux » est crucial pour de nombreuses tâches.
- **Les connexions de saut** : elles préservent les détails tout en ouvrant un raccourci au gradient, ce qui rend les réseaux profonds faciles à entraîner.
- **Large champ d'application** : segmentation d'images médicales (son œuvre fondatrice), génération d'images (l'ossature de débruitage des modèles de diffusion), super-résolution, et — la prévision de séries temporelles.

## Intérêt pour la prévision de séries temporelles (point central de ce site)

C'est le cœur de ce site. **Kernel U-Net (KUN)** transpose les idées du U-Net à la prévision de séries temporelles, avec une modification clé :

**1. Le multi-échelles le long de l'axe du temps.** L'encodeur **sous-échantillonne** l'axe du temps niveau par niveau : la série d'origine est une agitation fine « à la minute » ; après quelques sous-échantillonnages, elle devient une tendance grossière « à l'heure, au jour » — **plus on descend, plus l'horizon temporel est long et plus on se concentre sur la structure à longue portée**. Le décodeur **sur-échantillonne** ensuite niveau par niveau pour revenir à la résolution temporelle d'origine et produire la prévision.

**2. Les connexions de saut préservent les détails.** Le sous-échantillonnage perd inévitablement les détails de haute fréquence ; les connexions de saut envoient directement l'information fine de chaque échelle, avant sous-échantillonnage, au niveau correspondant du décodeur, **afin que la tendance de long terme (issue des couches profondes) et les fluctuations de court terme (issues des connexions de saut) se rejoignent lors de la reconstruction** : la prévision est à la fois stable et fine.

**3. Des « noyaux » légers à la place des lourds blocs de convolution.** À chaque échelle, le U-Net d'origine empile des blocs de convolution riches en paramètres et coûteux en calcul ; **KUN les remplace par des « noyaux (kernels) » apprenables légers**, qui effectuent à chaque échelle une transformation locale efficace. KUN conserve ainsi l'avantage multi-résolution du U-Net tout en réduisant fortement le coût.

**4. C'est son avantage clé face au Transformer.** Le [Transformer](../transformer/) / l'[attention](../attention/) standard coûte **$O(L^2)$** sur une séquence de longueur $L$, ce qui le rend lent et gourmand en mémoire sur de longues fenêtres. L'approche multi-échelles de KUN traite les dépendances à longue portée sur des **séquences grossières plus courtes**, avec une complexité bien moindre — c'est son principal argument pour la prévision de longues séquences. (L'attention peut toujours être intégrée comme composant à une échelle donnée ; les deux ne s'opposent pas.)

La filiation de KUN en une phrase : **c'est un modèle de prévision encodeur–décodeur multi-échelles (multi-résolution) de type U-Net, qui remplace les blocs de convolution par des noyaux légers et modélise simultanément, à différentes échelles de temps, la tendance de long terme et les détails de court terme, pour un coût bien inférieur à $O(L^2)$.**

## Résumé

- U-Net = **sous-échantillonnage par l'encodeur + sur-échantillonnage par le décodeur + connexions de saut entre échelles identiques**, en forme de U.
- **Les couches profondes gèrent le long terme grossier, les couches superficielles / connexions de saut le local fin** : les échelles coopèrent.
- Les connexions de saut préservent les détails et ouvrent un raccourci au gradient.
- **Kernel U-Net (KUN)** transpose ce schéma sur l'axe du temps et remplace les blocs de convolution par des **noyaux légers**, pour concilier à faible coût court et long terme — c'est le modèle de prévision de séries temporelles phare de ce site.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
