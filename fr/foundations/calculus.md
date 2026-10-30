---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/calculus/
title: "Le calcul différentiel et intégral"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

Le calcul différentiel et intégral est la mathématique du « **changement** » et de l'« **accumulation** » : la dérivée mesure la vitesse à laquelle une grandeur varie, l'intégrale additionne une infinité de petites variations. C'est le socle sur lequel reposent la compréhension du [gradient](../gradient/), de l'[optimisation](../optimization/) et de l'entraînement des modèles.

## Intuition

Représentons un chemin de montagne par une fonction $y=f(x)$, où $x$ est la position horizontale et $y$ l'altitude.

- La **dérivée** répond à la question : « en ce point, quelle est la pente du chemin ? » Une montée raide a une dérivée grande et positive, une descente une dérivée négative, un terrain plat une dérivée nulle.
- L'**intégrale** répond à la question : « du départ à l'arrivée, de combien l'altitude a-t-elle varié au total ? » Elle additionne les aires d'une infinité de fines bandes sous la courbe.

Les deux piliers du calcul — dérivée et intégrale — sont en fait des opérations **réciproques** l'une de l'autre : c'est le théorème fondamental de l'analyse.

{% include fviz/derivative.html %}

## Formulation mathématique

La **limite** est le point de départ de tout ; elle exprime l'idée d'« approcher indéfiniment » :

$$
\lim_{x\to a} f(x)=L
$$

La **dérivée** est définie comme la limite de la pente de la sécante lorsque l'écart tend vers 0 :

$$
f'(x)=\frac{df}{dx}=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$

- $h$ est un pas infinitésimal ;
- le numérateur est la variation de la fonction, le dénominateur la variation de la variable ;
- ce rapport est le « taux de variation » ; en passant à la limite, on obtient la **pente instantanée** en ce point.

Quelques règles de dérivation à connaître par cœur :

$$
(x^n)'=n x^{n-1},\quad (e^x)'=e^x,\quad (\ln x)'=\frac1x
$$

L'**intégrale** est l'opération inverse de la dérivée ; l'intégrale définie est égale à l'aire sous la courbe :

$$
\int_a^b f(x)\,dx
$$

Le **théorème fondamental de l'analyse** relie les deux : si $F'(x)=f(x)$, alors $\int_a^b f(x)\,dx=F(b)-F(a)$.

## Un exemple concret

Soit $f(x)=x^2$ ; calculons sa dérivée en $x=3$.

D'après les règles, $f'(x)=2x$, donc $f'(3)=6$. Vérifions avec la définition, en prenant $h=0.001$ :

$$
\frac{f(3.001)-f(3)}{0.001}=\frac{9.006001-9}{0.001}=6.001\approx 6
$$

```python
f  = lambda x: x**2
h  = 1e-5
x  = 3
print((f(x+h) - f(x)) / h)   # ≈ 6.00001, dérivée approchée numériquement
```

Cette idée d'« approcher la dérivée avec un pas infinitésimal » est exactement le principe de la **vérification numérique du gradient** en apprentissage profond.

## Pourquoi c'est important / où l'utilise-t-on

- **Entraîner = dériver + faire un pas** : on dérive la [fonction de perte](../loss-function/) par rapport aux paramètres pour obtenir le [gradient](../gradient/), puis on met à jour les paramètres par [descente de gradient](../gradient-descent/).
- **[Rétropropagation](../backpropagation/)** : un [réseau de neurones](../neural-network/) se dérive couche par couche grâce à la [règle de dérivation en chaîne](../chain-rule/) — qui n'est autre que la règle de dérivation des fonctions composées.
- **Probabilités et intégrales** : l'espérance et les probabilités d'une [variable aléatoire](../random-variable/) continue sont définies par des intégrales, ce qui fait le lien avec les [probabilités et statistiques](../probability-statistics/).

## Signification pour la prévision de séries temporelles

- La question « la tendance d'une série monte-t-elle ou descend-elle rapidement ? » porte sur la dérivée de la série par rapport au temps (la différenciation en est la version discrète).
- Lors de l'entraînement d'un modèle comme KUN (Kernel U-Net), chaque étape consiste à dériver la fonction de perte : sans calcul différentiel, pas d'apprentissage.
- « Cumuler » une erreur sur une période (par exemple l'erreur absolue cumulée) est une application discrète de l'idée d'intégrale.

## En résumé

- Dérivée = taux de variation instantané = pente ; intégrale = accumulation = aire.
- Les deux sont réciproques (théorème fondamental de l'analyse).
- C'est le fondement mathématique du gradient, de la règle de dérivation en chaîne, de l'optimisation et de tout l'entraînement en apprentissage profond.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
