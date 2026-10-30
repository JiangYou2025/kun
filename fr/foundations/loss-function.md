---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/loss-function/
title: "La fonction de perte"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)

Une **fonction de perte (loss function)** est une fonction qui **mesure l'écart entre la « prédiction du modèle » et la « vraie réponse »**. En une phrase : plus la perte est faible, plus la prédiction est juste ; et **entraîner un modèle consiste essentiellement à ajuster sans cesse ses paramètres pour amener cette perte au plus bas**.

## Intuition

Imaginez que vous fassiez travailler un élève sur des exercices. Pour chaque exercice, vous lui retirez des « points » : plus sa réponse est aberrante, plus vous en retirez ; plus elle est proche de la bonne réponse, moins vous en retirez. Cette **règle de pénalité**, c'est la fonction de perte.

- Elle donne au modèle une **note** qui lui dit clairement : « voici à quel point tu te trompes en ce moment ».
- C'est aussi la **boussole** de la **descente de gradient (gradient descent)** : le modèle ne sait pas dans quel sens ajuster ses paramètres, mais il lui suffit de regarder « dans quelle direction la perte baisse le plus vite » et de suivre cette direction pour devenir de plus en plus précis.

La fonction de perte joue donc deux rôles : elle est à la fois **arbitre** (elle note) et **guide** (elle indique la direction). Sans elle, le modèle marcherait les yeux bandés, sans savoir s'il apprend bien ni où poser le pied ensuite.

## Formulation mathématique

Supposons que nous ayons $n$ échantillons d'entraînement $(x_i, y_i)$ et un modèle $f_\theta$ ($\theta$ désigne l'ensemble des paramètres ajustables), dont la prédiction pour le $i$-ième échantillon est $\hat y_i = f_\theta(x_i)$. La **perte totale** s'écrit en général comme la moyenne des pertes individuelles :

$$\mathcal{L}(\theta)=\frac{1}{n}\sum_{i=1}^{n} \ell\big(y_i,\; f_\theta(x_i)\big)$$

Décomposons symbole par symbole :

- $\theta$ : les **paramètres** du modèle (par exemple les poids et le biais d'un [modèle linéaire](../linear-model/)). Entraîner, c'est trouver un bon $\theta$.
- $\ell(y_i, \hat y_i)$ : la perte d'**un seul échantillon**, qui mesure la gravité de l'erreur sur cette prédiction.
- $\frac{1}{n}\sum$ : on fait la **moyenne** des pertes de tous les échantillons pour obtenir le « degré d'erreur » global.
- $\mathcal{L}(\theta)$ : on la voit comme **une fonction des paramètres $\theta$** — c'est exactement l'objet que la descente de gradient cherche à minimiser.

La forme précise de $\ell$ dépend de la tâche. Voyons les deux grandes familles : régression et classification.

## Pertes de régression : prédire une valeur numérique

Lorsque $y$ est une valeur continue (prix d'un logement, température, volume de ventes), on utilise couramment les pertes suivantes.

**Erreur quadratique moyenne MSE / perte quadratique (squared loss)** :

$$\ell = (y-\hat y)^2$$

Elle **élève l'erreur au carré**, de sorte que **les grandes erreurs sont fortement amplifiées** (un écart de 2 coûte 4 points, un écart de 10 en coûte 100). Avantages : elle est lisse partout, a de bonnes propriétés mathématiques et se dérive facilement ; inconvénient : elle est **très sensible aux valeurs aberrantes (outliers)** — un seul point aberrant peut faire grimper la perte globale et « dévoyer » le modèle.

**Erreur absolue moyenne MAE / perte absolue (absolute loss)** :

$$\ell = |y-\hat y|$$

L'erreur n'est pas élevée au carré, on en prend seulement la valeur absolue : elle est donc **plus robuste aux valeurs aberrantes** — un point isolé n'est pas exagérément amplifié. En contrepartie, elle n'est pas dérivable en $\hat y = y$ (elle y présente un point anguleux), ce qui demande un traitement particulier lors de l'optimisation.

**Perte de Huber** : elle se comporte comme la MSE quand l'erreur est petite (lisse) et comme la MAE quand l'erreur est grande (robuste), réunissant ainsi les avantages des deux :

$$\ell_\delta(y,\hat y)=\begin{cases}\frac12 (y-\hat y)^2 & |y-\hat y|\le \delta\\[4pt]\delta\,\big(|y-\hat y|-\tfrac12\delta\big) & |y-\hat y|> \delta\end{cases}$$

$\delta$ est le point de bascule : en deçà de $\delta$, l'erreur est élevée au carré (sensible et lisse) ; au-delà, elle devient linéaire (pour ne pas être emportée par les valeurs aberrantes).

## Pertes de classification : prédire une classe

Lorsque la tâche est une classification (chat ou chien, courriel indésirable ou non), le modèle produit généralement une **probabilité** $\hat p$. On utilise alors le plus souvent l'**[entropie croisée](../cross-entropy/) (cross-entropy)**.

Classification multiclasse ($K$ classes, $y_k$ est l'encodage one-hot de la vraie étiquette, $\hat p_k$ la probabilité prédite) :

$$\ell = -\sum_{k=1}^{K} y_k \log \hat p_k$$

Classification binaire ($y\in\{0,1\}$, $p$ est la probabilité prédite pour la classe positive) :

$$\ell = -\big[\,y\log p+(1-y)\log(1-p)\,\big]$$

Intuition : l'entropie croisée récompense le fait « d'attribuer une forte probabilité à la bonne réponse ». Si la vérité est « chat » et que le modèle n'accorde au chat qu'une probabilité de 0,1, alors $-\log 0.1$ est grand et la pénalité est lourde ; s'il lui accorde 0,99, $-\log 0.99$ est proche de 0 et la pénalité quasi nulle.

**Pourquoi utiliser l'entropie croisée plutôt que directement l'« exactitude » (accuracy) comme perte ?** Parce que **l'exactitude n'est pas dérivable** : elle ne « saute » qu'au moment où une prédiction change de classe, sa courbe est un escalier et son gradient est nul presque partout — quand le modèle ajuste légèrement ses paramètres, l'exactitude ne bouge pas d'un iota, et la descente de gradient ne peut tout simplement pas fonctionner. L'entropie croisée, elle, est **lisse et dérivable** : à chaque infime variation de la probabilité, la perte varie continûment et fournit un gradient utile. D'où une exigence essentielle 👇

## Pourquoi la perte doit être « dérivable »

L'entraînement par gradient (la descente de gradient et toutes ses variantes) repose sur **la dérivation de la perte**, qui donne $\nabla_\theta \mathcal{L}$, puis sur la mise à jour des paramètres dans la direction qui fait baisser la perte :

$$\theta \leftarrow \theta - \eta\,\nabla_\theta \mathcal{L}(\theta)$$

Pour que cette étape fonctionne, la perte doit être **dérivable (differentiable)** (presque partout), afin que la dérivée nous dise « dans quel sens ajuster, et de combien ». Voilà pourquoi on utilise l'entropie croisée plutôt que l'exactitude, et la perte quadratique plutôt qu'un jugement 0/1 du type « juste ou faux » — **pour pouvoir optimiser, il faut d'abord pouvoir dériver**.

## Comment la fonction de perte se relie aux autres notions

- **Entraîner = minimiser la perte** : tout le processus d'entraînement consiste à faire baisser $\mathcal{L}(\theta)$ sans relâche par [descente de gradient](../ml/). La fonction de perte définit « ce qu'est un bon modèle », et les [algorithmes](../algorithms/) d'[optimisation](../optimization/) se chargent du « comment s'améliorer ».
- **Lien avec la régularisation** : la [régularisation](../regularization/) consiste à **ajouter un terme de pénalité** $\lambda\,\Omega(\theta)$ à la perte, qui devient $\mathcal{L}(\theta)+\lambda\,\Omega(\theta)$, pour empêcher le modèle d'être trop complexe et ainsi limiter le [surapprentissage](../overfitting/).
- **Fonction de perte vs métrique d'évaluation** : on les confond facilement. **La fonction de perte sert à « optimiser »** (elle doit être dérivable et s'utilise pendant l'entraînement), tandis que la [métrique d'évaluation](../evaluation-metrics/) sert à « rendre compte » (elle s'adresse aux humains et peut ne pas être dérivable : exactitude, F1, MAPE…). La pratique courante : on optimise l'entropie croisée pendant l'entraînement, puis on présente l'exactitude à sa hiérarchie. Les deux vont dans le même sens, mais ce n'est pas la même chose.

## Un petit exemple concret

Calculons à la main avec la perte quadratique pour sentir comment « les grandes erreurs sont amplifiées ». Trois échantillons, avec les valeurs réelles et prédites suivantes :

```python
y      = [3.0, 5.0, 10.0]
y_hat  = [2.5, 5.5,  7.0]   # les deux premiers s'écartent de 0,5, le dernier de 3

errors = [yi - pi for yi, pi in zip(y, y_hat)]   # [0.5, -0.5, 3.0]
mse = sum(e**2 for e in errors) / len(errors)    # (0.25+0.25+9)/3 = 3.17
mae = sum(abs(e) for e in errors) / len(errors)  # (0.5+0.5+3)/3   = 1.33
```

Regardez le point qui s'écarte de 3 : dans la MAE il contribue pour 3, dans la MSE pour $3^2=9$ — **la MSE amplifie beaucoup plus cette grande erreur**, si bien qu'un modèle qui minimise la MSE fera davantage d'efforts pour tenir compte de ce point aberrant.

## Signification pour la prévision de séries temporelles

En prévision de séries temporelles, le choix de la fonction de perte détermine directement « ce à quoi le modèle tient » :

- **MSE** : comme elle amplifie les grandes erreurs, elle **pénalise surtout les pics (spikes) prédits de façon grossièrement erronée**. Si ce que vous redoutez le plus, c'est « une grosse erreur de temps en temps » (par exemple en pilotage du réseau électrique), la MSE convient.
- **MAE** : elle est **plus robuste aux valeurs aberrantes et aux fluctuations isolées**. Si votre série contient souvent du bruit soudain ou quelques valeurs aberrantes par lesquelles vous ne voulez pas être dévoyé, la MAE est plus stable.
- **Perte quantile / Pinball Loss (quantile loss)** : quand vous ne voulez pas seulement une prévision ponctuelle, mais une **prévision probabiliste / par intervalle** (« les ventes de demain ont 90 % de chances de tomber dans tel intervalle »), utilisez la perte quantile. Pour le quantile d'ordre $\tau$, elle se définit ainsi :

$$\ell_\tau(y,\hat y)=\max\big(\tau\,(y-\hat y),\;(\tau-1)(y-\hat y)\big)$$

Elle **pénalise de façon asymétrique la surestimation et la sous-estimation** : en entraînant avec différentes valeurs de $\tau$ (par exemple 0,1, 0,5, 0,9), on obtient les bornes inférieure et supérieure de l'intervalle de prévision.

Le principe central tient en une phrase : **choisissez la perte en fonction du coût de vos erreurs**. Sous-estimer ou surestimer un stock n'a pas le même coût ? Alors n'utilisez pas aveuglément la MSE symétrique, passez à la perte quantile, asymétrique.

## En résumé

- La **fonction de perte** mesure l'écart entre prédiction et vérité ; elle est l'**arbitre + la boussole** de l'entraînement ; entraîner = minimiser la perte.
- Perte totale $\mathcal{L}(\theta)=\frac1n\sum_i \ell(y_i, f_\theta(x_i))$, où $\ell$ dépend de la tâche.
- Régression : la **MSE** amplifie les grandes erreurs et est sensible aux valeurs aberrantes ; la **MAE** est robuste mais présente un point anguleux ; la **perte de Huber** fait le compromis.
- Classification : l'**entropie croisée**, lisse et dérivable, est bien supérieure à l'exactitude, non dérivable.
- La perte doit être **dérivable** pour que la descente de gradient fonctionne.
- **Perte (pour optimiser) ≠ métrique d'évaluation (pour rendre compte)** ; la [régularisation](../regularization/) ajoute un terme de pénalité à la perte.
- Séries temporelles : la MSE pour les pics, la MAE contre les valeurs aberrantes, la **perte quantile** pour les prévisions par intervalle — choisissez selon le coût de vos erreurs.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)
