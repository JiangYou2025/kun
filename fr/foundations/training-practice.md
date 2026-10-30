---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/training-practice/
title: "Pratique de l'entraînement"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **pratique de l'entraînement** désigne l'ensemble des techniques d'ingénierie qui permettent à un [réseau de neurones](../neural-network/) de « s'entraîner tout court, de s'entraîner de façon stable, et de bien s'entraîner » — de l'initialisation des paramètres à la normalisation et à la [régularisation](../regularization/), en passant par la planification du taux d'apprentissage, l'arrêt précoce et le suivi de l'entraînement. Chacune est simple prise isolément, mais ensemble elles décident si un modèle est réellement utilisable.

**Voir aussi :** [Dropout](../dropout/) · [BatchNorm](../batchnorm/) · [Arrêt précoce](../early-stopping/)

## Intuition

Entraîner un réseau ressemble beaucoup à surveiller une soupe qui mijote : feu trop fort (taux d'apprentissage trop élevé), elle attache ; feu trop doux (taux trop faible), elle ne cuit jamais ; ingrédients mal lavés (données non normalisées), elle prend un goût amer ; trop d'assaisonnement d'un coup (modèle trop complexe), elle devient écœurante ([surapprentissage](../overfitting/)). La pratique de l'entraînement, c'est ce savoir-faire de « réglage du feu + dosage des ingrédients + dégustation » — avec pour but que la [perte](../backpropagation/) baisse régulièrement et que le modèle se comporte bien aussi sur des **données jamais vues**.

Passons en revue cette boîte à outils en suivant le cycle de vie de l'entraînement.

## Démarrage : initialisation et normalisation des données / variables

- **Initialisation des poids** : on ne peut pas tout mettre à 0 (tous les [neurones](../neuron/) seraient alors symétriques et n'apprendraient rien), ni utiliser des valeurs trop grandes ou trop petites (cela provoque immédiatement une [explosion ou une disparition du gradient](../vanishing-exploding-gradient/)). On utilise couramment l'initialisation de Xavier / de He, qui fixe automatiquement la variance des poids selon les dimensions d'entrée et de sortie de la couche.
- **Normalisation des entrées** : ramener chaque variable à un ordre de grandeur comparable (par exemple en soustrayant la moyenne et en divisant par l'écart-type) ; sinon, les variables de grande amplitude dominent le [gradient](../gradient/) et faussent l'entraînement.
- **Normalisation entre couches** : la [BatchNorm](../batchnorm/) ramène, sur chaque [batch](../batch/), les entrées d'une couche à une moyenne nulle et une variance unité avant de les remettre à l'échelle et de les décaler ; elle stabilise les distributions et autorise des taux d'apprentissage plus élevés. Avec de petits batchs ou pour les tâches séquentielles, on utilise plutôt la LayerNorm.

## Contre le surapprentissage : le trio de la régularisation

Surapprentissage = très bon sur le jeu d'entraînement, mauvais sur le jeu de validation. Les remèdes courants :

- **[Dropout](../dropout/)** : pendant l'entraînement, on désactive aléatoirement une partie des neurones, ce qui oblige le réseau à ne pas dépendre de quelques unités ; cela revient à un ensemble implicite de nombreux sous-réseaux.
- **Décroissance des poids (régularisation L2)** : on ajoute à la perte un terme $\frac{\lambda}{2}\lVert w\rVert^2$ qui pénalise les poids trop grands et rend le modèle plus lisse :

$$
L_{\text{total}} = L_{\text{data}} + \frac{\lambda}{2}\sum_w w^2
$$

où $\lambda$ règle l'intensité de la régularisation : plus il est grand, plus on favorise un modèle simple.

- **[Arrêt précoce](../early-stopping/)** : surveiller la perte de validation, s'arrêter dès qu'elle ne baisse plus et revenir à la meilleure version — une régularisation quasiment gratuite.
- **Augmentation de données / plus de données** : fondamentalement le plus efficace — plus les données sont nombreuses et variées, plus il est difficile de sur-apprendre.

## Régler le feu : taux d'apprentissage et optimiseur

Le [taux d'apprentissage](../learning-rate/) est l'hyperparamètre le plus important. On l'utilise avec un [optimiseur](../optimizer/) (comme [Adam](../adam/) ou SGD+Momentum) ; techniques courantes :

- **Planification du taux d'apprentissage (lr schedule)** : diminuer le taux en fin d'entraînement pour faciliter la convergence vers une meilleure solution. Les plus courantes sont la step decay et le cosine annealing :

$$
\eta_t = \eta_{\min} + \tfrac{1}{2}(\eta_{\max}-\eta_{\min})\Big(1 + \cos\tfrac{t}{T}\pi\Big)
$$

- **Warmup (préchauffage)** : pendant les quelques centaines de premières itérations, partir d'un taux très faible et l'augmenter progressivement, pour éviter de chambouler les paramètres dès le départ (quasi indispensable pour entraîner un Transformer).
- **Écrêtage du gradient** : limiter la norme du gradient à un seuil ; c'est le remède spécifique à l'[explosion du gradient](../vanishing-exploding-gradient/), et un réglage standard pour entraîner les [RNN](../rnn/) / [LSTM](../lstm/).

## Goûter : suivre les pertes d'entraînement et de validation

Pendant l'entraînement, il faut **toujours tracer ensemble les courbes de perte d'entraînement et de validation** ; elles révèlent les problèmes d'un coup d'œil :

- **Sous-apprentissage (underfitting)** : même la perte d'entraînement ne baisse pas → modèle trop faible / taux d'apprentissage trop petit / entraînement insuffisant. Remède : agrandir le modèle, entraîner plus longtemps, ajuster le taux d'apprentissage.
- **Surapprentissage (overfitting)** : la perte d'entraînement est basse, mais la perte de validation se met à **remonter** → le modèle apprend le jeu d'entraînement par cœur. Remède : le trio de régularisation ci-dessus, réduire le modèle, ajouter des données.
- **Situation idéale** : les deux courbes baissent, et la perte de validation suit de près la perte d'entraînement, avec un faible écart.

Règle empirique : **commencez par agrandir le modèle jusqu'à ce qu'il puisse sur-apprendre un petit sous-ensemble de données** (ce qui vérifie que le processus n'a pas de bug), puis ajoutez progressivement de la régularisation pour faire baisser la perte de validation. Ce rythme « d'abord sur-apprendre, ensuite régulariser » est plus efficace que de régulariser massivement dès le départ.

## Une boucle d'entraînement concrète

Assemblons les points ci-dessus dans un cadre d'entraînement PyTorch minimal mais utilisable :

```python
import torch, torch.nn as nn

opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)  # avec décroissance des poids
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs)    # planification du lr

best, wait, patience = float("inf"), 0, 10
for epoch in range(epochs):
    model.train()                                   # Dropout / BN en mode entraînement
    for x, y in train_loader:
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # écrêtage du gradient
        opt.step()
    sched.step()

    model.eval()                                    # mode inférence : BN utilise les stats running, Dropout désactivé
    with torch.no_grad():
        val = sum(loss_fn(model(x), y) for x, y in val_loader)
    if val < best:                                  # arrêt précoce + sauvegarde du meilleur
        best, wait = val, 0; torch.save(model.state_dict(), "best.pt")
    else:
        wait += 1
        if wait >= patience: break
```

## Résumé

- **Démarrage** : initialisation raisonnable + normalisation des entrées + normalisation entre couches ([BatchNorm](../batchnorm/)).
- **Contre le surapprentissage** : [Dropout](../dropout/), décroissance des poids, [arrêt précoce](../early-stopping/), plus de données.
- **Régler le feu** : planification du [taux d'apprentissage](../learning-rate/) + warmup + [optimiseur](../optimizer/) + écrêtage du gradient.
- **Lire les courbes** : diagnostiquer sous-apprentissage vs surapprentissage avec les pertes d'entraînement et de validation ; d'abord sur-apprendre, ensuite régulariser.
- Ces pratiques générales s'appliquent aussi à l'entraînement des [RNN](../rnn/), des [LSTM](../lstm/), des [Transformer](../transformer/) et du modèle multi-échelles de ce site, **Kernel U-Net (KUN)**.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
