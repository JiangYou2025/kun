---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2017–19 · Informatique"
permalink: /fr/history/e/deepar/
title: "DeepAR et la prévision probabiliste globale (Amazon, 2017–19)"
lead: "Ajuster un modèle distinct pour chacune de milliers de séries apparentées coûte trop cher, et les nouveaux produits n'ont pas d'historique. Un seul réseau global peut-il tout apprendre d'un coup ?"
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 9 · Apprentissage profond](../../09/).

### Contexte

Dans l'industrie, l'objet de la prévision est souvent une **multitude de séries apparentées** : la demande de chaque article dans chaque entrepôt d'un site de commerce en ligne, la charge de chaque foyer pour un fournisseur d'énergie. Les méthodes statistiques classiques comme [ARIMA](../box-jenkins/) ou le lissage exponentiel sont **locales** — elles estiment des paramètres séparément pour chaque série, indépendamment des autres. Elles s'essoufflent quand les séries sont nombreuses et courtes, et que de nouveaux produits apparaissent fréquemment (démarrage à froid).

### Problème

Les modèles locaux se heurtent à une triple difficulté : quand la série est trop courte, l'estimation des paramètres est peu fiable ; ajuster une à une des milliers de séries coûte cher ; et **une nouvelle série n'a pas d'historique**, il n'y a donc rien à estimer. Or ces séries sont en réalité fortement corrélées — des produits de même catégorie ou d'une même région partagent souvent saisonnalité et forme. **Un seul modèle peut-il mutualiser la force statistique de toutes les séries et fournir directement l'incertitude de la prévision ?**

### Autres courants de l'époque (et leurs limites)

- **Modèles statistiques locaux (ARIMA / ETS)** : interprétables et efficaces série par série, mais sans partage d'information entre séries ; le démarrage à froid reste sans solution.
- **Régression par apprentissage automatique en prévision ponctuelle** : peut exploiter des covariables, mais ne produit en général qu'une valeur ponctuelle sans décrire la distribution prédictive ; les décisions (comme le stock de sécurité) manquent alors d'une base d'incertitude.
- **Agrégation hiérarchique / par groupes** : atténue le problème des séries courtes, mais exprime mal la dynamique non linéaire de chaque série individuelle.

### Méthode

DeepAR entraîne un **RNN autorégressif global** : toutes les séries partagent les mêmes paramètres, et le réseau produit à chaque pas les **paramètres d'une distribution de probabilité**, et non une valeur ponctuelle. À partir de l'historique et des covariables, un [LSTM](../lstm/) produit un état caché $$h_t$$, qui est ensuite projeté sur les paramètres de la vraisemblance (moyenne et variance d'une gaussienne, ou loi binomiale négative pour des données de comptage) :

$$ \ell(z_t\mid \theta_t),\qquad \theta_t=\theta\big(h_t\big),\quad h_t=\mathrm{RNN}\big(h_{t-1},\,z_{t-1},\,x_t\big) $$

L'entraînement maximise la log-vraisemblance de la série entière (par *teacher forcing*, en fournissant la vraie valeur $$z_{t-1}$$) :

$$ \mathcal{L}=\sum_{t}\log \ell\big(z_t\mid \theta_t\big) $$

En prévision, on passe à l'**échantillonnage autorégressif** : on tire $$\hat z_t$$ de $$\ell(\cdot\mid\theta_t)$$, on le réinjecte dans le réseau, et l'on répète sur de nombreuses trajectoires pour obtenir des **quantiles de Monte-Carlo** du futur. Pour traiter des séries d'ordres de grandeur très différents, on normalise aussi l'échelle de chaque série par sa moyenne.

### Résultats

Sur des bancs d'essai comme la demande en commerce de détail, DeepAR surpasse nettement en précision les références locales traditionnelles, avec un avantage particulièrement marqué lorsque les séries sont nombreuses et de longueurs inégales. Il gère naturellement le **démarrage à froid** : une nouvelle série, grâce aux seules covariables et à l'a priori de forme appris globalement, reçoit une prévision probabiliste raisonnable, et le modèle produit directement des intervalles de prévision calibrés pour les décisions en aval.

### Portée et perspectives

DeepAR a établi pour l'apprentissage profond des séries temporelles le paradigme « **modèle global + sortie probabiliste + échantillonnage autorégressif** », déplaçant l'attention de « régler chaque série » vers « apprendre des représentations partagées entre séries ». Cette approche a profondément influencé les travaux suivants — qu'il s'agisse de [N-BEATS](../nbeats/), purement à propagation avant, des prédicteurs fondés sur l'attention ([Transformer](../transformer/)), ou des modèles de fondation pour séries temporelles ([modèles de fondation](../foundation-models/)), tous ont hérité de la vision du monde « un seul grand modèle au service de millions de séries ».
