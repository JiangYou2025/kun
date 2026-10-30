---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2019 · Informatique"
permalink: /fr/history/e/nbeats/
title: "N-BEATS, la prévision purement feed-forward (Oreshkin et al., 2019)"
lead: "Un modèle profond doit-il forcément recourir à la récurrence ou à l'attention pour prévoir des séries temporelles ? Avec une pile de blocs feed-forward et un double résidu, N-BEATS dépasse nettement les références statistiques."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 9 · Apprentissage profond](../../09/).

### Contexte

En 2018, l'apprentissage profond se heurte à un fait embarrassant : dans les grandes compétitions de prévision comme M3 et M4, **les méthodes purement statistiques et de simples combinaisons battent souvent des réseaux de neurones complexes**. Le vainqueur de la compétition M4 était lui-même un hybride de statistique et d'apprentissage automatique. D'où un doute : un modèle purement profond peut-il l'emporter seul en prévision univariée, sans dépendre d'une ingénierie manuelle de caractéristiques propres aux séries temporelles ?

### Problème

Les prédicteurs profonds de l'époque reposaient pour la plupart sur des [RNN](../rnn/) : séquentiels, difficiles à entraîner et souvent critiqués comme des « boîtes noires ». **Peut-on concevoir une architecture purement profonde, sans aucun composant spécifique aux séries temporelles (récurrence, attention ou a priori statistique décomposable), qui soit à la fois en tête en précision et capable de conserver, au choix, une interprétabilité ?**

### Les autres courants de l'époque (et leurs limites)

- **Les références statistiques (ARIMA / ETS / Theta)** : robustes et interprétables, mais d'une expressivité limitée, et mal adaptées à l'apprentissage conjoint de formes complexes sur un grand nombre de séries.
- **La prévision profonde de type RNN (comme [DeepAR](../deepar/))** : forte expressivité, mais entraînement séquentiel et faible interprétabilité.
- **Les hybrides manuels statistique + ML (vainqueur de M4)** : très précis, mais complexes à mettre en œuvre, dépendants d'une grande part de conception manuelle et difficiles à réutiliser de bout en bout.

### Méthode

N-BEATS décompose la prévision en une pile de **blocs entièrement connectés**. Chaque bloc lit la fenêtre d'historique et produit deux sorties : un **backcast** (reconstruction de sa propre entrée) et un **forecast** (prévision du futur). Les blocs sont enchaînés par un **empilement à double résidu** — chaque bloc retranche de son entrée la part qu'il a expliquée et transmet le résidu au bloc suivant :

$$ x^{(\ell)}=x^{(\ell-1)}-\widehat{x}^{(\ell)}_{\text{back}},\qquad \widehat{y}=\sum_{\ell}\widehat{y}^{(\ell)}_{\text{fore}} $$

Chaque bloc produit d'abord, par quelques couches entièrement connectées, des coefficients de développement, puis les projette sur un ensemble de **fonctions de base** $$g$$ :

$$ \widehat{y}^{(\ell)}_{\text{fore}}=\sum_{i} \theta_i\, g_i $$

Dans la **version générique**, $$g$$ est apprise ; dans la **version interprétable**, on choisit délibérément une base polynomiale (tendance) et une base de Fourier (saisonnalité), si bien que chaque pile produit respectivement une composante de tendance et une composante saisonnière, et la prévision devient lisible par un humain. Le réseau entier est sans récurrence et s'entraîne en parallèle.

### Résultats

Sur plusieurs bancs d'essai publics — M3, M4, Tourism —, N-BEATS **surpasse sur toute la ligne** des références solides, y compris le vainqueur de M4, sans aucune ingénierie de caractéristiques spécifique aux séries temporelles. Il fait aussi preuve d'une bonne **transférabilité** : un modèle entraîné sur un ensemble de jeux de données reste compétitif sur des jeux de données inédits, laissant entrevoir la possibilité d'une « prévision zero-shot après pré-entraînement ».

### Portée et perspectives

Avec la structure feed-forward la plus simple, N-BEATS a démontré qu'**un modèle purement profond peut battre seul les références statistiques**, tout en conciliant élégamment précision et interprétabilité grâce au double résidu et à la projection sur une base. Il a inspiré les prédicteurs ultérieurs par patchs et décomposables, ainsi que l'orientation qui pousse l'idée « pré-entraînement — transfert » vers les modèles de fondation pour les séries temporelles ([../foundation-models/](../foundation-models/)). Dans la vague qui court après le [Transformer](../transformer/), il rappelle aussi qu'une architecture simple, si elle est bien conçue, reste extrêmement compétitive.
