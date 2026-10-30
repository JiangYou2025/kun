---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1938 · Mathématiques"
permalink: /fr/history/e/wold/
title: "L'anatomie des processus stationnaires (Wold, 1938)"
lead: "Toute série stationnaire peut être proprement séparée en « une partie entièrement déterminée par son histoire » et « une partie pilotée par une suite de bruits blancs » — ce pas a transformé l'ARMA, d'astuce empirique, en théorème."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 2 · Fondements théoriques](../../02/).

### Contexte

Après que [Yule](../yule-ar/) eut, en 1927, élucidé les « quasi-cycles » par l'autorégression, les statisticiens disposaient de l'AR, et certains ajustaient aussi les données par moyennes mobiles (MA). Mais tout cela relevait de **l'intuition empirique dans le choix du modèle** : faut-il utiliser un AR ou un MA ? De quel ordre ? Existe-t-il une théorie unifiée qui dise clairement « à quoi ressemble au juste une série stationnaire » ? L'économiste suédois Herman Wold répond à cette question fondamentale dans sa thèse de doctorat de 1938, *A Study in the Analysis of Stationary Time Series*.

### Problème

Étant donné un processus (faiblement / en covariance) stationnaire $$\{X_t\}$$ — de moyenne constante, dont l'autocovariance ne dépend que de l'écart temporel —, que peut-on affirmer de sa structure interne ? **Existe-t-il une décomposition universelle séparant complètement « la composante prévisible » de « l'excitation aléatoire imprévisible »**, sans dépendre d'aucune hypothèse de modèle paramétrique particulier ? Si oui, elle pourrait servir de socle commun à tous les modèles linéaires de séries temporelles.

### Les autres courants de l'époque (et leurs limites)

- **L'école harmonique / du périodogramme** : elle voit encore une série stationnaire comme des sinusoïdes déterministes plus du bruit. Elle sait décrire la composante déterministe, mais ne peut caractériser les dynamiques aléatoires « entretenues en permanence par un bruit blanc », et reste démunie face aux quasi-cycles de type AR.
- **Ajustement de modèles purement empirique** : on applique directement un AR(p) ou un MA(q), on règle les paramètres, et l'on garde celui dont les résidus sont les plus petits. Aucune garantie théorique — on ignore si ces classes de modèles sont « assez grandes » pour approcher tout processus stationnaire.
- **Extrapolation déterministe** : on suppose la série entièrement déterminée par un petit nombre de tendances ou de cycles déterministes. C'est précisément un cas particulier de la « composante déterministe » de la décomposition de Wold, qui laisse de côté toute la dynamique aléatoire représentée par la moyenne mobile d'ordre infini.

### Méthode

Wold démontre que tout processus de moyenne nulle stationnaire en covariance se décompose de façon unique en deux parties décorrélées — une **composante déterministe** $$V_t$$ (entièrement prévisible linéairement à partir de son passé infiniment lointain) et une **composante purement non déterministe** (une moyenne mobile d'ordre infini) :

$$ X_t = \sum_{j=0}^{\infty}\psi_j\,\varepsilon_{t-j} + V_t,\qquad \psi_0=1,\ \sum_{j=0}^{\infty}\psi_j^2<\infty $$

où $$\varepsilon_t \sim \mathrm{WN}(0,\sigma^2)$$ est l'**innovation** : $$\varepsilon_t$$ est égal à $$X_t$$ moins sa prédiction optimale obtenue par projection linéaire sur le passé $$\{X_s:s<t\}$$, c'est-à-dire l'erreur de prédiction à un pas. Les coefficients $$\psi_j$$ sont la réponse impulsionnelle du filtre linéaire qui « filtre » cette suite de bruits blancs pour en faire $$X_t$$ ; leur sommabilité au carré garantit la convergence et la stationnarité. La composante déterministe $$V_t$$ est orthogonale à tous les $$\varepsilon_s$$. Intuitivement : **processus stationnaire = une enveloppe entièrement prévisible + une dynamique, excitée par un bruit blanc passé dans un filtre linéaire, qui restera toujours imparfaitement prévisible**.

### Résultats

Ce résultat élève l'ARMA au rang de théorème plutôt que d'astuce. La forme MA(∞) montre que, dès que la densité spectrale de la partie aléatoire est rationnelle, on peut approcher cette somme infinie par le quotient d'un AR et d'un MA d'ordres finis — c'est exactement le fondement de l'existence de l'ARMA($$p,q$$). « AR ou MA ? » cesse dès lors d'être une affaire de mystère : tous deux sont des **approximations à nombre fini de paramètres** d'une même représentation de Wold, convertibles l'une en l'autre (AR(∞) ↔ MA(∞)). L'innovation $$\varepsilon_t$$ devient aussi l'objet standard de « l'erreur de prédiction optimale à un pas » dans le filtre de Kalman et la théorie de la prédiction ultérieurs.

### Portée et perspectives

La décomposition de Wold est la constitution des séries temporelles linéaires modernes. Elle a établi une vision du monde : étudier un processus stationnaire, c'est au fond étudier « le filtre linéaire qui transforme le bruit blanc en série observée ». Cette ligne mène directement à la [théorie de la prédiction de Wiener–Kolmogorov](../wiener-kolmogorov-prediction/) (la prédiction optimale est la projection orthogonale sur l'espace engendré par le passé), au cadre de modélisation [ARMA/ARIMA de Box–Jenkins](../box-jenkins/) de 1970, ainsi qu'à la factorisation spectrale dans le domaine fréquentiel. Quand nous disons aujourd'hui que « tout signal stationnaire peut être vu comme un bruit blanc façonné par un filtre », c'est ce pas franchi par Wold en 1938 que nous citons.
