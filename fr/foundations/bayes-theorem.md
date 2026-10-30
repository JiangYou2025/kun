---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/bayes-theorem/
title: "Le théorème de Bayes"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

Le théorème de Bayes nous dit comment **réviser rationnellement un jugement initial** lorsqu'un nouvel indice se présente. Il combine en une seule formule « ce que je croyais au départ » et « ce que disent les données ».

## Intuition

Imaginez qu'en vous réveillant, vous estimiez **a priori** à 30 % la probabilité qu'il pleuve aujourd'hui (c'est votre « prior »). Puis vous ouvrez les rideaux et voyez un ciel chargé de nuages noirs (c'est l'« indice »). Ces nuages vont vous faire **revoir à la hausse** votre estimation — mais de combien ? Cela dépend de deux choses :

- quelle proportion des jours de pluie s'accompagne de nuages noirs (à quel point l'indice « colle » à la pluie) ;
- si les nuages noirs sont fréquents aussi les jours sans pluie (à quel point l'indice est « banal »).

Le théorème de Bayes transforme ce raisonnement naïf en une formule précise. Son idée centrale : **nouveau jugement = ancien jugement × correction apportée par l'indice**.

## Formulation mathématique

$$
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}
$$

Signification de chaque symbole :

- $P(A)$ — **probabilité a priori (prior)** : votre croyance en l'événement $A$ (par exemple « il pleut ») avant d'avoir vu l'indice.
- $P(B\mid A)$ — **vraisemblance (likelihood)** : la probabilité d'observer l'indice $B$ (par exemple « nuages noirs ») en supposant $A$ vrai.
- $P(A\mid B)$ — **probabilité a posteriori (posterior)** : la croyance mise à jour après avoir vu l'indice $B$.
- $P(B)$ — **probabilité marginale de l'indice (evidence)** : la probabilité totale que l'indice apparaisse ; elle joue un rôle de normalisation et garantit que la probabilité a posteriori est une probabilité valide.

Le dénominateur se développe grâce à la **formule des probabilités totales** :

$$
P(B)=P(B\mid A)\,P(A)+P(B\mid \lnot A)\,P(\lnot A)
$$

Cette étape est souvent oubliée, alors qu'elle est la clé du calcul : elle additionne la probabilité de l'indice dans les deux cas, « $A$ se produit » et « $A$ ne se produit pas ».

## Un exemple concret

Le problème classique du « test médical ». Une maladie touche $P(\text{malade})=1\%$ de la population. Il existe un test :

- la probabilité qu'un malade soit testé positif (sensibilité) est $P(\text{pos}\mid\text{malade})=99\%$ ;
- une personne saine peut aussi obtenir un faux positif : $P(\text{pos}\mid\text{sain})=5\%$.

**Votre test est positif : quelle est la probabilité que vous soyez réellement malade ?** Beaucoup répondent d'instinct 99 %, mais faisons le calcul :

$$
P(\text{pos})=0.99\times0.01+0.05\times0.99=0.0099+0.0495=0.0594
$$

$$
P(\text{malade}\mid\text{pos})=\frac{0.99\times0.01}{0.0594}\approx 0.167
$$

Seulement environ **16,7 %** ! La raison : les personnes saines sont si nombreuses que, même avec un taux de faux positifs de 5 %, le nombre absolu de faux positifs dépasse de loin celui des vrais malades. C'est le célèbre **oubli de la fréquence de base (base rate fallacy)**.

```python
prior   = 0.01            # P(malade)
sens    = 0.99            # P(pos|malade)
fpr     = 0.05            # P(pos|sain)
evidence = sens*prior + fpr*(1-prior)
posterior = sens*prior / evidence
print(round(posterior, 3))   # 0.167
```

## Pourquoi c'est important / où l'utilise-t-on

Le théorème de Bayes est un cadre unifié pour **apprendre à partir des données** :

- **Classifieur bayésien naïf** : filtrage du spam, etc. ; on l'utilise directement pour calculer « la probabilité qu'un message soit du spam, étant donné ses mots ».
- **Inférence bayésienne** : on traite les paramètres du modèle comme des [variables aléatoires](../random-variable/) et l'on utilise les données pour transformer le prior en posterior, ce qui fournit naturellement une **estimation de l'incertitude**.
- Il forme un couple avec le [maximum de vraisemblance](../maximum-likelihood/) : le maximum de vraisemblance ne regarde que $P(B\mid A)$, tandis que l'approche bayésienne multiplie en plus par le prior $P(A)$.

## Signification pour la prévision de séries temporelles

Prévoir, c'est par essence « mettre à jour ses croyances sur l'avenir à partir de l'historique observé » — exactement la structure du raisonnement bayésien :

$$
P(\text{avenir}\mid\text{historique})\propto P(\text{historique}\mid\text{modèle})\,P(\text{modèle})
$$

- **Filtrage bayésien / filtre de Kalman** : à chaque nouvelle observation, on met à jour la loi a posteriori de l'état ; c'est le mécanisme central de la prévision en ligne avec les modèles à espace d'états.
- Dans des modèles profonds comme KUN (Kernel U-Net), la formule de Bayes n'est pas écrite explicitement, mais l'idée — « corriger son jugement sur la suite à l'aide des indices fournis par la fenêtre historique » — est exactement la même ; et si l'on ajoute des **intervalles de confiance** aux prévisions, c'est le langage de la loi a posteriori qui est à l'œuvre.

## En résumé

- Posterior $\propto$ vraisemblance $\times$ prior ; le dénominateur n'est qu'une normalisation.
- N'oubliez pas de développer $P(B)$ avec la formule des probabilités totales.
- Le prior compte : quand un événement est **rare au départ**, même un indice très sensible ne le rend pas forcément probable (oubli de la fréquence de base).

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
