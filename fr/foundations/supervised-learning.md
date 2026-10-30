---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/supervised-learning/
title: "Apprentissage supervisé"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

L'**apprentissage supervisé** (*supervised learning*) désigne la situation où chaque échantillon des données d'entraînement est accompagné de sa « réponse de référence » (son étiquette) ; la tâche du modèle est d'apprendre une règle qui associe une **sortie** à chaque **entrée**, de sorte qu'il puisse aussi donner la bonne sortie face à des entrées nouvelles.

## Intuition

Imaginez un élève qui fait un cahier d'exercices : à côté de chaque exercice est imprimée la **bonne réponse**. L'élève lit d'abord l'énoncé (l'entrée), écrit sa propre réponse, puis la compare à la réponse de référence ; s'il s'est trompé, il corrige son raisonnement. Plus il fait d'exercices, plus il sera juste la prochaine fois qu'il rencontrera un exercice semblable.

L'apprentissage supervisé, c'est ce processus :

- **L'énoncé** = les variables d'entrée $x$ (par exemple la surface d'un logement, son nombre de pièces).
- **La réponse de référence** = l'étiquette $y$ (par exemple le prix de vente réel du logement).
- **Le raisonnement de l'élève** = le modèle $f$.
- **Comparer à la réponse et corriger** = mesurer l'erreur avec une **[fonction de perte](../loss-function/)**, puis ajuster le modèle.

Le point clé : quelqu'un (ou une certaine source) doit avoir préparé les réponses à l'avance. Sans étiquettes, ce n'est pas de l'apprentissage supervisé — c'est de l'[apprentissage non supervisé](../unsupervised-learning/).

## Formulation mathématique

Nous disposons d'un **jeu de données** étiqueté :

$$
\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}
$$

où chaque $x_i \in X$ est une entrée (un nombre ou un vecteur) et chaque $y_i \in Y$ la sortie correcte correspondante. Le but est d'apprendre une fonction :

$$
f: X \to Y
$$

telle que $f(x_i)$ soit aussi proche que possible de $y_i$. Comment mesurer cette « proximité » ? Avec une **fonction de perte** $L(\hat{y}, y)$, qui note « l'écart entre la valeur prédite $\hat{y}=f(x)$ et la valeur réelle $y$ ». Entraîner, c'est minimiser la perte moyenne sur l'ensemble des échantillons :

$$
\min_{f}\ \frac{1}{n}\sum_{i=1}^{n} L\big(f(x_i),\, y_i\big)
$$

- Pour les tâches de prédiction de valeurs continues, on utilise souvent l'**erreur quadratique moyenne (MSE)** : $L(\hat{y}, y) = (\hat{y}-y)^2$.
- Pour les tâches de prédiction de catégories, on utilise souvent l'**[entropie croisée](../cross-entropy/)** ou d'autres pertes de classification.

## Deux grandes sous-familles : régression et classification

L'apprentissage supervisé se divise en deux grandes familles selon le « type de la sortie $y$ » :

- **Régression** (*regression*) : $y$ est une **valeur continue**. Exemples : prédire le prix d'un logement à partir de sa surface, prédire les ventes de demain à partir de l'historique, prédire la température. La sortie est un nombre réel.
- **Classification** (*classification*) : $y$ est une **catégorie discrète**. Exemples : déterminer si un e-mail est un spam (oui/non), reconnaître si une image montre un chat ou un chien, détecter si une transaction est frauduleuse. La sortie est une étiquette.

Pour les distinguer en une phrase : **demander « combien », c'est de la régression ; demander « quelle catégorie », c'est de la classification.**

## Un exemple concret

Avec `scikit-learn` en [Python](../python/), entraînons le modèle de régression le plus simple qui soit — prédire le prix d'un logement à partir de sa surface :

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Entrée X : surface du logement (m²), une ligne par échantillon
X = np.array([[50], [60], [80], [100], [120]])
# Étiquette y : prix de vente correspondant (en dizaines de milliers de yuans) — c'est la « réponse de référence »
y = np.array([150, 175, 230, 280, 330])

model = LinearRegression()
model.fit(X, y)          # apprendre f : surface -> prix

print(model.predict([[90]]))   # prédire le prix d'un logement de 90 m²
```

L'étape `fit`, c'est « faire les exercices en s'appuyant sur les réponses » : le modèle trouve automatiquement la droite qui colle le mieux aux données, celle qui minimise l'erreur quadratique moyenne entre prix prédits et prix réels. Pour une tâche de classification, il suffit de remplacer `LinearRegression` par `LogisticRegression` et de faire de `y` des étiquettes de catégorie (par exemple 0/1).

## Pourquoi c'est important (où l'utilise-t-on ?)

L'apprentissage supervisé est la branche **la plus répandue et la plus mûre** de l'[apprentissage automatique](../ml/). Dès que vous pouvez collecter des paires « entrée + bonne réponse », vous pouvez presque toujours l'appliquer : notation de crédit, diagnostic médical, systèmes de recommandation, reconnaissance vocale, traduction automatique… Il s'oppose aux deux autres grands paradigmes :

- l'[apprentissage non supervisé](../unsupervised-learning/) : les données **n'ont pas** d'étiquettes, et le but est de découvrir des structures cachées (comme le [partitionnement](../clustering/) ou la réduction de dimension) ;
- l'[apprentissage par renforcement](../reinforcement-learning/) : pas de réponses toutes prêtes, on apprend par essais et erreurs grâce aux **récompenses issues de l'interaction avec l'environnement**.

Si l'apprentissage supervisé est si pratique, c'est justement parce que des « réponses explicites » rendent l'objectif d'entraînement très clair, et l'évaluation directe : il suffit de vérifier si les prédictions sont justes sur des échantillons jamais vus.

## Intérêt pour la prévision de séries temporelles

C'est le point le plus important de cette leçon : **la prévision de séries temporelles est fondamentalement de l'apprentissage supervisé.** En apparence, une série temporelle n'est qu'une suite de nombres sans étiquettes ; mais on peut la « supervisionner » avec une **fenêtre glissante** (*sliding window*), en construisant artificiellement des paires $(X, y)$.

Le principe : on prend les valeurs des $k$ instants consécutifs passés comme variables $X$, et la valeur qui suit immédiatement, $y_t$, comme étiquette :

$$
X = [\,x_{t-k},\, \dots,\, x_{t-2},\, x_{t-1}\,] \quad\Longrightarrow\quad y = x_t
$$

Prenons un exemple chiffré. Supposons que la série d'origine soit :

```
Instant : 1   2   3   4   5   6   7
Valeur : 10  12  13  15  16  18  19
```

Avec une fenêtre de longueur $k = 3$ que l'on fait glisser dans le temps, on transforme cette série en un **tableau d'apprentissage supervisé** :

| Variables $x_{t-3}, x_{t-2}, x_{t-1}$ | Étiquette $y = x_t$ |
| :--- | :--- |
| 10, 12, 13 | 15 |
| 12, 13, 15 | 16 |
| 13, 15, 16 | 18 |
| 15, 16, 18 | 19 |

Avec ce tableau, le problème de prévision devient exactement le problème de régression vu plus haut : apprendre un $f$ qui prend trois valeurs passées en entrée et renvoie la suivante. Régression linéaire, modèles à base d'arbres ou [réseaux de neurones](../neural-network/) peuvent alors être entraînés directement.

**Un détail auquel il faut absolument veiller : le découpage selon le temps.** À l'évaluation, on ne peut pas, comme en apprentissage supervisé ordinaire, mélanger aléatoirement les données avant de les répartir entre entraînement et test, car le modèle « jetterait un œil au futur ». La bonne pratique est de **découper dans l'ordre chronologique** : entraîner sur les données les plus anciennes et tester sur les plus récentes, pour simuler la situation réelle où l'on « prédit le futur depuis le présent ».

## En résumé

- **Apprentissage supervisé** = des données étiquetées ; on apprend une application $f$ de l'entrée $x$ vers la sortie $y$, en minimisant une **fonction de perte**.
- Deux grandes sous-familles : la **régression** (sortie continue, on demande « combien ») et la **classification** (catégorie discrète, on demande « quelle catégorie »).
- Il s'oppose à l'[apprentissage non supervisé](../unsupervised-learning/) (sans étiquettes, recherche de structure) et à l'[apprentissage par renforcement](../reinforcement-learning/) (essais et erreurs guidés par des récompenses).
- **La prévision de séries temporelles est de l'apprentissage supervisé** : une **fenêtre glissante** transforme la série en tableau $(X, y)$, et l'on prédit le futur à partir du passé.
- L'évaluation doit impérativement **se découper selon le temps**, pour éviter de « jeter un œil » au futur en s'entraînant sur des données ultérieures.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
