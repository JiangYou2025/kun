---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/dl/
title: "Fondements de l'apprentissage profond"
lead: "Réseaux de neurones, rétropropagation, optimiseurs, architectures courantes et pratique de l'entraînement — le moteur des modèles de prévision modernes. On n'y pose que la charpente et les concepts."
prev: /foundations/ml/
next: /foundations/
math: true
---

> Ceci est une **carte conceptuelle** : elle indique « de quoi est fait l'apprentissage profond, comment on l'entraîne et quelles architectures existent » ; les mathématiques et l'implémentation détaillées relèvent de manuels spécialisés.

## 1. Composition d'un [réseau de neurones](../neural-network/)

- **[Neurone](../neuron/)** : somme pondérée + biais, puis une non-linéarité
- **Couches et réseau** : les neurones s'empilent en couches, les couches en réseau
- **[Propagation avant](../forward-propagation/)** : l'entrée est transformée couche après couche pour produire la sortie
- **[Fonctions d'activation](../activation-function/)** : ReLU, Sigmoid, Tanh, GELU — elles introduisent la **non-linéarité**, sans laquelle tout le réseau se réduirait à un [modèle linéaire](../linear-model/)

$$h = \sigma(Wx + b)$$

## 2. Comment entraîner : la [rétropropagation](../backpropagation/)

- **[Fonction de perte](../loss-function/)** : mesure l'écart entre la prédiction et la réalité
- **Rétropropagation** : grâce à la **[règle de dérivation en chaîne](../chain-rule/)**, l'erreur est renvoyée couche par couche depuis la sortie, ce qui donne le gradient de chaque paramètre
- **[Différentiation automatique](../autodiff/)** : le framework calcule ces dérivées automatiquement (vous n'écrivez que la propagation avant)
- **[Optimiseurs](../optimizer/)** : SGD, Momentum, RMSProp, **[Adam](../adam/)** (le plus utilisé)
- **[Taux d'apprentissage](../learning-rate/)** : l'hyperparamètre le plus important — trop grand, l'entraînement diverge ; trop petit, il est trop lent

## 3. Éviter le [surapprentissage](../overfitting/)

Les modèles profonds ont énormément de paramètres : la généralisation est la difficulté centrale.

- **[Dropout](../dropout/)** : désactiver aléatoirement des neurones pendant l'entraînement
- **[Normalisation par lots (BatchNorm)](../batchnorm/) / normalisation par couche (LayerNorm)** : stabiliser l'entraînement
- **[Arrêt précoce (early stopping)](../early-stopping/)** : s'arrêter quand la validation se dégrade
- **Augmentation de données / décroissance des poids** : régularisation supplémentaire

## 4. [Architectures](../architectures/) courantes

| Architecture | Point fort | Liens avec les séries temporelles |
|------|------|-------------|
| **MLP / entièrement connecté** | Généraliste | DLinear, N-BEATS |
| **CNN** | Motifs locaux | TCN, prédicteurs convolutifs |
| **RNN / LSTM / GRU** | Séquences, mémoire | Prévision séquentielle classique |
| **Transformer / attention** | Dépendances à longue portée | Modèles séquentiels modernes |
| **U-Net** | Multi-échelle | **Kernel U-Net (KUN)** |

## 5. [Pratique de l'entraînement](../training-practice/)

- **[Taille de lot (batch size)](../batch/)** et **époque (epoch)**
- **Accélération [GPU](../gpu/)** : rend possible l'entraînement de grands modèles
- **Problèmes de gradient** : disparition / explosion du gradient, et leurs remèdes (connexions résiduelles, normalisation, écrêtage du gradient)
- **Apprentissage par transfert et préentraînement** : réutiliser des représentations déjà apprises

> Lien avec le cours principal : les leçons 12 à 14 appliquent ces architectures à la prévision de séries temporelles, pour aboutir au **Kernel U-Net (KUN)** de ce dépôt.

---

**Termes clés :** [neurone](../neuron/), [fonction d'activation](../activation-function/), [propagation avant](../forward-propagation/), [rétropropagation](../backpropagation/), [différentiation automatique](../autodiff/), [Adam](../adam/), [taux d'apprentissage](../learning-rate/), [Dropout](../dropout/), [BatchNorm](../batchnorm/), [arrêt précoce](../early-stopping/), [MLP](../mlp/), [CNN](../cnn/), [RNN](../rnn/) / [LSTM](../lstm/), [Transformer](../transformer/), [attention](../attention/), [U-Net](../u-net/), [GPU](../gpu/), [disparition / explosion du gradient](../vanishing-exploding-gradient/).
