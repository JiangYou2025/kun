---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/training-pipeline/
title: "Le processus d'entraînement"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

Le **processus d'entraînement (training pipeline)** désigne le **flux de travail de bout en bout** qui va de la définition de la tâche et de la perte, au découpage et à la validation des données, jusqu'au réglage des hyperparamètres, à l'évaluation finale et au déploiement. Ce n'est pas un algorithme particulier, mais un ensemble d'**étapes standard — une « chaîne de production » — pour faire de l'apprentissage automatique**.

## Intuition

Imaginez qu'entraîner un modèle, c'est **cuisiner un plat** : on ne se met pas à faire sauter n'importe quoi d'emblée. On décide d'abord du plat (la tâche), on prépare et lave les ingrédients (les données), on suit la recette pas à pas (le processus), on goûte en cours de route pour ajuster l'assaisonnement (le réglage), et on vérifie une dernière fois le goût avant de servir (l'évaluation sur le jeu de test).

L'apprentissage automatique, c'est pareil. L'erreur la plus fréquente des débutants est de **ne penser qu'à « quel modèle choisir, quel paramètre régler »** en négligeant tout le processus qui l'entoure. En réalité, **un processus rigoureux décide souvent davantage du succès que le passage à un modèle plus sophistiqué** — car ce processus recèle d'innombrables pièges qui vous amènent à « vous mentir à vous-même » (surtout la fuite de données).

Cette leçon décompose cette chaîne étape par étape.

## Les étapes standard (dans l'ordre)

**1. Définir le problème et la métrique.** Commencez par clarifier : que veut-on prédire ? S'agit-il de régression ou de classification ? Quelle [métrique d'évaluation](../evaluation-metrics/) définit ce qui est « bon » (RMSE ? exactitude ? MAPE ?) ? La métrique doit être fixée avant de commencer, sinon il est très tentant ensuite de « choisir la métrique la plus flatteuse pour se faire valoir ».

**2. Préparer les données.** Cela comprend le **nettoyage** (valeurs manquantes, valeurs aberrantes, doublons), l'**ingénierie des variables** (construire des variables d'entrée utiles) et la **standardisation / normalisation** (ramener des variables d'unités différentes à des échelles comparables). C'est généralement l'étape qui prend le plus de temps, et celle qui influe le plus sur le résultat.

**3. Découper les données.** Séparer les données en trois parties : **jeu d'entraînement / jeu de validation / jeu de test** (voir la section suivante). Pour des données ordinaires, un découpage aléatoire convient ; mais **une série temporelle doit être découpée selon le temps** — c'est le point capital.

**4. Choisir le modèle et définir la fonction de perte.** Choisissez une [famille de modèles](../model-families/) ([modèle linéaire](../linear-model/), arbres, réseaux de neurones…) et une [fonction de perte](../loss-function/) — c'est elle qui définit, pendant l'entraînement, « ce qu'est une erreur ». Le modèle et la perte doivent être adaptés à la tâche.

**5. Entraîner (ajuster les paramètres).** Sur le **jeu d'entraînement**, on exécute un algorithme d'optimisation (le plus souvent la [descente de gradient](../gradient-descent/)) qui ajuste sans cesse les paramètres pour faire baisser la perte et « ajuster » le modèle aux données.

**6. Valider et régler les hyperparamètres.** Les **hyperparamètres** ([taux d'apprentissage](../learning-rate/), profondeur des arbres, intensité de régularisation $\lambda$, etc.) ne s'apprennent pas sur le jeu d'entraînement : il faut les choisir sur le **jeu de validation**. On utilise souvent la [validation croisée](../cross-validation/) pour estimer les performances de manière plus stable, combinée à une **recherche en grille (grid search)** ou une **recherche aléatoire (random search)** pour essayer systématiquement différentes combinaisons.

**7. Évaluation finale sur le jeu de test.** Une fois le modèle et les hyperparamètres choisis, on l'exécute une seule fois sur le **jeu de test jamais touché**, pour obtenir une estimation honnête de sa véritable capacité de [généralisation](../generalization/). **Le jeu de test ne s'utilise qu'une fois** — si on le consulte plusieurs fois, il « fuit », et l'estimation n'est plus fiable.

**8. Déployer et surveiller.** Une fois en production, il faut continuer à surveiller : le monde réel change (**dérive conceptuelle / concept drift**), le modèle se dégrade peu à peu, et il faut le **réentraîner périodiquement (retraining)**.

## Le rôle des trois jeux de données

C'est l'ossature de tout le processus ; il faut absolument bien les distinguer :

| Jeu de données | Qui l'utilise | Rôle |
|---|---|---|
| **Jeu d'entraînement (train)** | Les paramètres du modèle | **Apprendre** — la descente de gradient y ajuste les paramètres |
| **Jeu de validation (validation)** | Vous (celui qui règle) | **Choisir** — comparer hyperparamètres et modèles, garder le meilleur |
| **Jeu de test (test)** | Personne, jusqu'à la fin | **Examiner** — estimer une seule fois, honnêtement, la généralisation |

Une métaphore facile à retenir : le jeu d'entraînement, ce sont les **exercices faits au quotidien** ; le jeu de validation, l'**examen blanc** (qui sert à ajuster sa stratégie de révision) ; le jeu de test, l'**examen final** (qu'on ne passe qu'une fois — le regarder avant, c'est tricher). Si vous utilisez à répétition le jeu de test pour choisir le modèle, il dégénère en second jeu de validation : vous **[sur-apprenez](../overfitting/) le jeu de test**, et vous finissez trop optimiste sur les performances en production.

## Le plus grand piège : la fuite de données

La **fuite de données (data leakage)** désigne le fait d'**utiliser en douce, pendant l'entraînement, des informations qu'on n'aurait pas dû voir** (en particulier des informations futures ou issues du jeu de test). Les métriques hors ligne sont alors incroyablement bonnes, et tout s'effondre dès la mise en production.

Le cas le plus classique : **standardiser ou sélectionner les variables avant le découpage**. Par exemple, si vous calculez la moyenne et la variance sur **toutes les données** pour standardiser, le jeu d'entraînement a « jeté un œil » aux statistiques des jeux de validation et de test — c'est une fuite.

La bonne pratique : **tout prétraitement qui « apprend quelque chose des données » doit être ajusté (fit) uniquement sur le jeu d'entraînement, puis appliqué (transform) aux jeux de validation et de test**.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Regrouper « standardisation + modèle » dans un Pipeline —
# avantage clé : en validation croisée, le scaler n'est ajusté que sur la partie entraînement de chaque pli, ce qui évite automatiquement la fuite
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  Ridge()),
])

param_grid = {"model__alpha": [0.1, 1.0, 10.0]}   # régler l'hyperparamètre d'intensité de régularisation

grid = GridSearchCV(pipe, param_grid, cv=5, scoring="neg_mean_squared_error")
grid.fit(X_train, y_train)        # validation croisée sur le seul jeu d'entraînement pour choisir les hyperparamètres

print(grid.best_params_)
# Le jeu de test ne sert qu'une fois, à la toute fin :
final_score = grid.score(X_test, y_test)
```

Tout l'intérêt du `Pipeline` est de garantir que des étapes comme la standardisation restent **« enfermées » dans la partie entraînement de chaque pli**, sans jamais laisser filtrer d'information des données de validation ou de test. Faire à la main un `fit_transform` sur tout `X` est l'erreur de fuite la plus fréquente chez les débutants.

## Intérêt pour la prévision de séries temporelles

Le processus d'entraînement des séries temporelles obéit à quelques règles **particulières mais impératives**, car les données ont un **ordre temporel** et ne peuvent pas être mélangées aléatoirement comme des données ordinaires.

- **Découper impérativement dans l'ordre chronologique.** L'entraînement d'abord, le test ensuite (par exemple, entraîner sur les premiers 80 % de la période et tester sur les 20 % restants). **Ne jamais mélanger aléatoirement** — sinon on « prédit le passé avec le futur », un cas typique de fuite.
- **Utiliser une validation croisée pour séries temporelles (walk-forward / glissante).** On ne peut pas utiliser un K-fold ordinaire (qui casse l'ordre temporel) ; il faut **avancer pas à pas** : à chaque fois, « entraîner sur le passé et prédire le futur immédiat », puis faire glisser la fenêtre. La validation correspond alors au véritable scénario de prévision. Voir la [validation croisée](../cross-validation/).
- **Prévenir la fuite du futur dans l'ingénierie des variables.** Lorsqu'on construit des **statistiques glissantes** (moyenne mobile, écart-type mobile, etc.), on **ne peut utiliser que les données antérieures à l'instant courant**. Si votre moyenne mobile inclut aussi « le futur », le modèle « triche » hors ligne et échouera à coup sûr en production.
- **Surveiller la dérive conceptuelle et réentraîner périodiquement.** Les régularités d'une série temporelle changent avec le temps (jours fériés, politiques publiques, évolutions du marché) ; une fois en production, il faut surveiller l'erreur en continu et, dès que les performances baissent, **réentraîner** avec les nouvelles données.
- **Toujours se comparer à une référence naïve.** En séries temporelles, il existe un adversaire redoutable : la **prévision naïve** (« demain = aujourd'hui », ou « demain = le même jour de la semaine dernière »). Si votre modèle complexe ne la bat pas, c'est qu'il n'a rien appris de réel. Tout résultat doit d'abord être comparé à cette référence.

## Erreurs fréquentes / résumé

- **Ne penser qu'au choix du modèle et au réglage, en négligeant le processus** — les pièges du processus sont souvent plus fatals que le choix du modèle.
- **Fuite de données** : standardiser / sélectionner les variables avant le découpage, ou laisser l'information future entrer dans l'entraînement — on s'en prémunit avec un `Pipeline` et en n'ajustant que sur le jeu d'entraînement.
- **Réutiliser le jeu de test** : il ne s'utilise qu'une fois ; à force de s'en servir, on le sur-apprend, l'estimation devient optimiste, et l'évaluation de la véritable [généralisation](../overfitting/) en pâtit.
- **Découper / mélanger aléatoirement une série temporelle** : il faut découper selon le temps, valider en walk-forward, et ne construire les variables glissantes qu'avec le passé.
- **Ne pas fixer de référence** : toujours se comparer d'abord à la prévision naïve, pour vérifier que le modèle apporte vraiment quelque chose.
- **Considérer la mise en production comme la fin** : il faut surveiller la **dérive conceptuelle** et réentraîner régulièrement.
- En une phrase : processus d'entraînement = **fixer la métrique → préparer les données → découper en trois → choisir le modèle et la [perte](../loss-function/) → entraîner → régler par [validation croisée](../cross-validation/) → un seul passage sur le jeu de test → déployer et surveiller**, en se gardant tout du long de la fuite et du [surapprentissage](../overfitting/).

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
