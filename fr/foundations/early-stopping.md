---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/early-stopping/
title: "Arrêt précoce"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

L'**arrêt précoce (Early Stopping)** est un moyen simple et efficace de lutter contre le [surapprentissage](../overfitting/) : pendant l'entraînement, on surveille en continu les performances sur l'ensemble de validation, et dès qu'elles **cessent de s'améliorer**, on arrête l'entraînement et l'on revient à la meilleure version du modèle.

## Intuition

Un élève qui enchaîne les exercices progresse d'abord ; mais s'il s'acharne toujours sur le même recueil, il finit par **apprendre les réponses par cœur** — il retient les détails des énoncés, et même les erreurs, et se retrouve démuni devant de nouveaux exercices. Le meilleur moment pour s'arrêter est celui où « le taux de réussite sur des exercices nouveaux » commence tout juste à baisser.

Il en va de même pour l'entraînement d'un modèle. À mesure que le nombre d'époques (epoch) augmente :

- la **[perte](../loss-function/) d'entraînement** diminue presque toujours de façon monotone (le modèle colle de plus en plus aux données d'entraînement) ;
- la **perte de validation** commence généralement par baisser puis remonte — au début, le modèle apprend de vraies régularités ; ensuite, il se met à apprendre le **bruit** de l'ensemble d'entraînement et généralise moins bien.

Le minimum de la perte de validation est le « point idéal » où la capacité de [généralisation](../generalization/) du modèle est la meilleure. L'arrêt précoce trouve automatiquement ce point et s'arrête à proximité, ce qui évite de surveiller à la main et de gaspiller de la puissance de calcul à poursuivre l'entraînement jusqu'au surapprentissage.

## Principe et algorithme

L'arrêt précoce repose sur trois hyperparamètres :

- **patience** : le nombre d'époques consécutives sans amélioration de la métrique de validation après lequel on s'arrête, par exemple 10.
- **min_delta (amélioration minimale)** : une amélioration ne compte comme « réelle » que si elle dépasse ce seuil, ce qui filtre les petites fluctuations.
- **Métrique surveillée** : généralement la perte de validation $L_{val}$ (plus elle est petite, mieux c'est), mais ce peut aussi être la précision, etc.

La logique de l'algorithme :

```python
best = float("inf"); wait = 0; best_weights = None
for epoch in range(max_epochs):
    train_one_epoch()
    val = evaluate_on_validation()          # perte sur l'ensemble de validation
    if val < best - min_delta:              # amélioration réelle
        best = val
        best_weights = copy_weights()       # sauvegarder le meilleur modèle actuel
        wait = 0
    else:
        wait += 1
        if wait >= patience:                # aucun progrès pendant patience époques consécutives
            break
model.load(best_weights)                     # revenir à la meilleure version
```

Deux points essentiels :

1. **Il faut sauvegarder les meilleurs poids.** Au moment où l'on constate « l'absence de progrès », le modèle a déjà été entraîné patience époques de plus et s'est peut-être dégradé : il faut revenir à la version dont la perte de validation était la plus basse.
2. **La patience offre une marge.** La perte de validation fluctue souvent ; on ne peut pas s'arrêter à la première hausse. La patience permet de tolérer les fluctuations de court terme et de n'intervenir qu'en cas de dégradation durable.

## Un exemple concret

Prenons patience=3 et min_delta=0. Lors d'un entraînement, la perte de validation évolue ainsi :

| epoch | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|------|---|---|---|---|---|---|---|
| $L_{val}$ | 0.50 | 0.42 | 0.39 | 0.40 | 0.41 | 0.43 | 0.45 |
| wait | 0 | 0 | 0 | 1 | 2 | 3 ✋ | – |

À l'époque 3, on atteint le minimum de 0.39 et on le sauvegarde. Ensuite, les époques 4, 5 et 6 n'apportent aucune amélioration trois fois de suite ; wait atteint patience=3, on **s'arrête** donc à l'époque 6 et l'on **revient aux poids de l'époque 3**. Même si l'époque 7 pouvait (ou non) amener un rebond, on ne parie pas — l'arrêt précoce choisit prudemment de s'arrêter au meilleur point connu.

## Pourquoi c'est important / où l'utiliser

- **Une [régularisation](../regularization/) presque gratuite** : sans modifier l'architecture du réseau ni la fonction de perte, simplement en « s'arrêtant au bon moment », on améliore nettement la généralisation.
- **Économie de temps et de calcul** : on évite d'entraîner inutilement jusqu'au bout.
- **Un contrôle implicite de la complexité** : plus l'entraînement dure, plus les degrés de liberté effectifs du modèle augmentent ; l'arrêt précoce limite cette complexité effective, ce qui l'apparente à la régularisation L2.
- Il est **complémentaire** du [Dropout](../dropout/), de [BatchNorm](../batchnorm/), de la décroissance des poids, etc. ; on les utilise souvent ensemble, et ils forment la panoplie anti-surapprentissage de la [pratique de l'entraînement](../training-practice/).

## Pièges courants

- **Ne regarder que la perte d'entraînement** : elle ne cesse de baisser, elle ne vous dira jamais de vous arrêter ; il faut juger sur un **ensemble de validation indépendant**.
- **Ne pas sauvegarder les meilleurs poids** : le modèle au moment de l'arrêt n'est souvent pas la meilleure version ; si l'on oublie de revenir en arrière, tout le travail est perdu.
- **Une patience trop faible** : on se laisse tromper par des fluctuations normales et l'on s'arrête trop tôt, en état de sous-apprentissage.
- **Faire l'arrêt précoce sur l'ensemble de test** : l'information du test fuiterait alors dans la sélection du modèle, et l'évaluation ne serait plus impartiale — l'arrêt précoce doit reposer sur l'ensemble de validation.

## Intérêt pour la prévision de séries temporelles

Les modèles de séries temporelles ont particulièrement tendance à prendre le bruit ponctuel de la période d'entraînement pour une régularité ; l'arrêt précoce est un moyen standard de contrôler ce surapprentissage et de garantir la généralisation aux données futures. Pour entraîner des [RNN](../rnn/), des [LSTM](../lstm/), et jusqu'au modèle multi-échelle de ce site, **Kernel U-Net (KUN)**, l'arrêt précoce fondé sur la perte de validation fait partie des pratiques d'ingénierie par défaut.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
