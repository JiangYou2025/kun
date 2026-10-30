---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/bias-variance/
title: "Le compromis biais–variance"
no_comments: true
math: true
---

> Extrait de [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)

Le **compromis biais–variance** énonce que l'erreur de prédiction d'un modèle se décompose en deux parties : le **biais** (les hypothèses du modèle sont trop rigides et l'éloignent systématiquement de la vérité) et la **variance** (le modèle est trop sensible aux données d'entraînement : avec un autre jeu de données, ses conclusions changent du tout au tout). Plus un modèle est simple, plus son biais est élevé ; plus il est complexe, plus sa variance est élevée. Il faut trouver le juste milieu entre les deux.

## Intuition

Imaginez que vous tirez sur une cible.

- **Biais élevé, variance faible** : les tirs sont très groupés, mais l'ensemble est décalé par rapport au centre. Comme avec un fusil dont le viseur est faussé — aussi stable soyez-vous, vous ne toucherez pas juste. Cela correspond au **sous-apprentissage** : le modèle est trop simple pour saisir même les régularités des données d'entraînement.
- **Biais faible, variance élevée** : le point d'impact moyen est bien proche du centre, mais les impacts sont dispersés partout. Comme si votre main tremblait fortement — toucher la cible relève de la chance. Cela correspond au **[surapprentissage](../overfitting/)** : le modèle est trop complexe et mémorise aussi le bruit des données d'entraînement comme s'il s'agissait d'une régularité.
- **Biais faible, variance faible** : précis et stable, c'est ce que l'on recherche, mais en pratique on ne peut généralement que s'en approcher.

Intuition clé : **le biais et la variance évoluent le plus souvent en sens inverse**. Rendre le modèle plus complexe réduit le biais mais augmente la variance, et inversement.

## Formulation mathématique

Supposons que la vraie relation soit $y = f(x) + \varepsilon$, où $\varepsilon$ est un bruit de moyenne 0 et de variance $\sigma^2$. À partir d'un jeu d'entraînement, on apprend un modèle $\hat{f}(x)$. En un point de test fixé $x_0$, en prenant l'espérance sur « tous les jeux d'entraînement possibles », l'erreur quadratique moyenne de la prédiction se décompose exactement ainsi :

$$
\mathbb{E}\big[(y - \hat{f}(x_0))^2\big]
= \underbrace{\big(\mathbb{E}[\hat{f}(x_0)] - f(x_0)\big)^2}_{\text{biais}^2}
+ \underbrace{\mathbb{E}\big[(\hat{f}(x_0) - \mathbb{E}[\hat{f}(x_0)])^2\big]}_{\text{variance}}
+ \underbrace{\sigma^2}_{\text{erreur irréductible}}
$$

Explication terme par terme :

- **Biais$^2$** : $\mathbb{E}[\hat{f}(x_0)]$ est la « moyenne » des prédictions du modèle (sur différents jeux d'entraînement) ; le biais est son écart à la vraie valeur $f(x_0)$. Un biais important signifie que la structure même du modèle est inadaptée.
- **Variance** : l'amplitude des fluctuations des prédictions autour de leur propre moyenne. Une variance importante signifie qu'avec un autre jeu d'entraînement, les prédictions changent radicalement.
- **Erreur irréductible $\sigma^2$** : le bruit aléatoire intrinsèque aux données, qu'**aucun modèle ne peut éliminer** ; c'est la borne inférieure de l'erreur.

Seuls les deux premiers termes sont sous notre contrôle ; l'objectif est de minimiser la somme **biais$^2$ + variance** — et non de réduire à l'extrême l'un des deux isolément.

{% include fviz/bias-variance.html %}

## Un exemple concret

Ajustons une courbe bruitée avec des polynômes pour voir comment la complexité influence les deux termes :

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
x = np.linspace(0, 1, 60).reshape(-1, 1)
y = np.sin(2 * np.pi * x).ravel() + rng.normal(0, 0.2, 60)
Xtr, Xte, ytr, yte = train_test_split(x, y, test_size=0.4, random_state=0)

for deg in [1, 4, 15]:
    model = make_pipeline(PolynomialFeatures(deg), LinearRegression())
    model.fit(Xtr, ytr)
    tr = np.mean((model.predict(Xtr) - ytr) ** 2)
    te = np.mean((model.predict(Xte) - yte) ** 2)
    print(f"degré={deg:2d}  MSE entraînement={tr:.3f}  MSE test={te:.3f}")
```

La sortie typique suit cette tendance :

- **degré = 1** (une droite) : les erreurs d'entraînement et de test sont toutes deux élevées → **biais élevé** (sous-apprentissage).
- **degré = 4** : les erreurs d'entraînement et de test sont faibles et proches → **point d'équilibre**, le meilleur.
- **degré = 15** : l'erreur d'entraînement est presque nulle, mais l'erreur de test explose → **variance élevée** (surapprentissage).

## Pourquoi c'est important / où l'utilise-t-on

Ce cadre offre un point de vue unifié pour comprendre **presque tous les choix d'hyperparamètres** :

- **Régler la complexité du modèle** : profondeur d'un arbre, nombre de couches d'un [réseau de neurones](../neural-network/), degré d'un polynôme — tout cela revient à se déplacer entre biais et variance.
- **[Régularisation](../regularization/)** : les pénalités $\ell_2$ / $\ell_1$, l'[arrêt précoce](../early-stopping/) et le [Dropout](../dropout/) consistent tous à **ajouter délibérément un peu de biais en échange d'une forte baisse de la variance**.
- **Méthodes d'ensemble** : le [Bagging / les forêts aléatoires](../ensemble-gbdt/) réduisent surtout la variance (en moyennant plusieurs modèles à forte variance) ; le Boosting réduit surtout le biais (en corrigeant progressivement les résidus).
- **Ajouter des données** : davantage de données d'entraînement réduit principalement la variance — le modèle devient moins sensible à chaque point bruité.

## Signification pour la prévision de séries temporelles

Dans les tâches de prévision, ce compromis est tout aussi omniprésent, avec quelques particularités :

- **Longueur de fenêtre = bouton de complexité** : avec une fenêtre historique très courte, le modèle est simple, son biais est élevé et il risque de manquer la tendance ou la saisonnalité ; avec une fenêtre très longue et beaucoup de variables, la variance est élevée et il risque de prendre des fluctuations occasionnelles pour des régularités.
- **Modélisation de la saisonnalité** : n'utiliser que le même jour de la semaine précédente (un seul retard) donne un biais élevé ; empiler des dizaines de variables retardées donne une variance élevée. La pratique courante consiste à trouver un compromis avec **un petit nombre de retards pertinents + de la régularisation**.
- **L'évaluation doit respecter l'ordre chronologique** : pour savoir si vous êtes dans la zone de biais ou dans celle de variance, il faut recourir à la [validation croisée pour séries temporelles](../cross-validation/) (fenêtre glissante ou extensible) ; **ne mélangez jamais aléatoirement les données**, sinon une « fuite du futur » vous fera sous-estimer la variance.

## En résumé

- Erreur = biais$^2$ + variance + bruit irréductible ; le dernier terme ne peut pas être éliminé.
- **Sous-apprentissage ↔ biais élevé**, **surapprentissage ↔ variance élevée** ; les deux évoluent généralement en sens inverse.
- L'objectif n'est pas de ramener l'un des termes à 0, mais de minimiser leur somme — ce qui se produit généralement à une complexité intermédiaire.
- La régularisation, les ensembles et l'ajout de données sont autant d'outils pour régler ce compromis.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours de base](../)
