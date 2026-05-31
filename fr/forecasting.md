---
lang: fr
ref: forecasting
permalink: /fr/forecasting/
title: "Comment prévoir"
lead: "La prévision est un flux de travail, pas un modèle unique. Cette page parcourt ce flux — d'une référence triviale jusqu'à l'apprentissage profond — et montre comment savoir si votre prévision est bonne."
prev: time-series
next: kun
math: true
---

## Le flux de travail de la prévision

Un projet de prévision fiable suit presque toujours la même boucle :

1. **Définir la tâche.** Que prédisez-vous, à quelle distance (l'horizon $$H$$), et à quelle fréquence ?
2. **Préparer les données.** Nettoyer les valeurs manquantes, rééchantillonner à une fréquence régulière, traiter les valeurs aberrantes.
3. **Découper selon le temps.** S'entraîner sur le passé, valider sur une tranche plus récente, tester sur la plus récente. *Jamais de mélange aléatoire.*
4. **Commencer par une référence.** Si votre modèle sophistiqué ne la bat pas, le problème vient du modèle.
5. **Entraîner et régler** des modèles progressivement plus puissants.
6. **Évaluer** sur des données réservées avec la bonne métrique.
7. **Surveiller** en production et réentraîner à mesure que le monde dérive.

> La plus grosse erreur des débutants est de sauter l'étape 3 ou l'étape 4. Un score de classement ne vaut rien sans un découpage temporel honnête et une référence à battre.

## Les références à battre

Calculez toujours celles-ci d'abord — elles sont quasi gratuites et étonnamment fortes :

- **Naïve / persistance :** demain = aujourd'hui, soit $$\hat{x}_{t+1} = x_t$$.
- **Naïve saisonnière :** ce lundi = lundi dernier, soit $$\hat{x}_{t+1} = x_{t+1-s}$$ pour une saison de longueur $$s$$.
- **Moyenne mobile / dérive :** prolonger la moyenne récente ou la pente récente.

## Le paysage des modèles

### 1. Modèles statistiques classiques
- **ARIMA** — modélise l'autocorrélation et la différenciation ; idéal pour une série unique et bien régulière.
- **Lissage exponentiel (ETS / Holt-Winters)** — pondère davantage les observations récentes ; excellent avec une tendance + saisonnalité nettes.

*Forces :* interprétables, solides sur peu de données. *Limites :* une série à la fois, peinent avec de nombreuses variables en interaction et les longs horizons.

### 2. Modèles d'apprentissage automatique
- **Gradient boosting (XGBoost, LightGBM)** sur des variables construites (décalages, moyennes glissantes, variables calendaires comme le jour de la semaine).

*Forces :* gèrent de nombreuses covariables, robustes. *Limites :* l'ingénierie des variables se fait à la main.

### 3. Modèles d'apprentissage profond
- **RNN / LSTM / GRU, TCN et Transformers** apprennent les motifs temporels directement à partir des fenêtres brutes.
- **Les prévisionnistes modernes** — PatchTST, DLinear, N-BEATS et **Kernel U-Net (KUN)** — sont conçus spécifiquement pour la prévision multivariée à long horizon.

*Forces :* apprennent des motifs complexes et partagés entre de nombreuses séries ; passent à l'échelle des longs horizons. *Limites :* exigent plus de données et de calcul.

## Choisir une métrique

La métrique encode ce que « bon » signifie pour *votre* problème.

| Métrique | Formule | À utiliser quand |
|---|---|---|
| **MAE** | $$\frac{1}{H}\sum\lvert x_t-\hat{x}_t\rvert$$ | Vous voulez des erreurs dans l'unité d'origine, robustes aux valeurs aberrantes |
| **RMSE** | $$\sqrt{\frac{1}{H}\sum (x_t-\hat{x}_t)^2}$$ | Les grandes erreurs doivent être plus pénalisées |
| **MAPE** | $$\frac{100}{H}\sum\frac{\lvert x_t-\hat{x}_t\rvert}{\lvert x_t\rvert}$$ | Vous voulez un pourcentage sans unité (évitez les valeurs proches de zéro) |

Reportez votre métrique **par rapport à la référence**, et non isolément.

## Valider dans le temps

Comme on ne peut pas mélanger, utilisez une **validation croisée à fenêtre glissante / extensible** : entraîner jusqu'à un point, prévoir le bloc suivant, glisser, recommencer. Cela simule l'usage réel du modèle et donne une distribution d'erreurs plutôt qu'un seul chiffre chanceux.

```
|--- entraînement ---|--- test ---|
|------ entraînement ------|--- test ---|
|--------- entraînement ---------|--- test ---|
```

## Pas unique vs. multi-pas

Pour prévoir un horizon $$H > 1$$, vous pouvez :

- **Itératif (récursif) :** prédire un pas, le réinjecter en entrée, recommencer. Simple, mais les erreurs s'accumulent.
- **Direct / multi-sortie :** prédire les $$H$$ pas d'un coup. Plus stable sur les longs horizons — et c'est exactement ainsi que **KUN** produit sa prévision.

Le flux de travail et le vocabulaire en place, vous êtes prêt à rencontrer le modèle lui-même.
