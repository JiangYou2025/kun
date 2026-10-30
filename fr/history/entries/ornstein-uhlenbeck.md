---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1930 · Physique"
permalink: /fr/history/e/ornstein-uhlenbeck/
title: "Le processus aléatoire qui rentre à la maison (Ornstein · Uhlenbeck, 1930)"
lead: "Le mouvement brownien s'éloigne toujours plus et sa variance diverge sans limite ; pourtant, dans le monde réel, vitesses, taux d'intérêt et températures sont sans cesse ramenés vers l'équilibre. Le processus OU ajoute ce « ressort de rappel » — et, une fois discrétisé, il se révèle n'être autre que l'AR(1)."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Le [mouvement brownien / processus de Wiener](../brownian-motion/) pur a quelque chose de « non physique » : sa variance croît sans limite, $$\propto t$$, et s'il sert à décrire une vitesse, celle-ci dérive sans borne au fil du temps. Or la **vitesse** d'une particule brownienne réelle ne grandit évidemment pas indéfiniment — la résistance visqueuse la ramène en arrière. En 1930, Leonard Ornstein et George Uhlenbeck, partant de l'[équation de Langevin](../langevin/), ont donné une description statistique rigoureuse d'un processus aléatoire avec retour à la moyenne, conçu précisément pour décrire ces fluctuations « ramenées vers l'équilibre ».

### Problème

L'[équation de Langevin](../langevin/) nous dit que la vitesse est freinée par le terme de frottement $$-\gamma v$$. **Vers quelle distribution se stabilise, à long terme, une grandeur sans cesse ramenée par le frottement et sans cesse repoussée par la force aléatoire ? Comment son autocorrélation décroît-elle avec l'écart temporel ?** Autrement dit, qu'est-ce qui distingue statistiquement un « processus aléatoire avec force de rappel » d'une « marche aléatoire sans force de rappel » ?

### Autres courants de l'époque (et leurs limites)

- **Modéliser toutes les fluctuations directement par un mouvement brownien $$W_t$$** : simple, mais la variance diverge, il n'existe pas de distribution stationnaire, et l'on ne peut décrire les grandeurs qui fluctuent autour d'un équilibre (vitesse, taux d'intérêt, stocks).
- **Rappel déterministe + bruit ajouté après coup** : on résout d'abord $$\dot x=-\gamma x$$ pour laisser la grandeur décroître vers 0, puis on superpose un peu de bruit d'observation. Cela dissocie le « rappel » et l'« aléa », et ne donne ni la bonne structure d'autocorrélation ni la bonne variance stationnaire.
- La bonne approche consiste à faire agir la force de rappel et le bruit **continûment dans une même équation**, leur équilibre dynamique produisant une distribution stationnaire.

### Méthode

Le processus OU est défini par l'équation différentielle stochastique suivante (la dérive pointe vers la moyenne, la diffusion fournit les fluctuations) :

$$ dX_t=-\theta\,(X_t-\mu)\,dt+\sigma\,dW_t $$

où $$\theta>0$$ est la vitesse de rappel, $$\mu$$ la moyenne de long terme, $$\sigma$$ l'intensité du bruit et $$W_t$$ un processus de Wiener. Son autocovariance **décroît exponentiellement** avec l'écart, et il possède une variance stationnaire :

$$ \mathrm{Cov}(X_t,X_{t+s})=\frac{\sigma^2}{2\theta}\,e^{-\theta |s|},\qquad \mathrm{Var}_\infty=\frac{\sigma^2}{2\theta} $$

Le point essentiel est sa **discrétisation** : en échantillonnant avec un pas $$\Delta$$ et en posant $$\phi=e^{-\theta\Delta}$$, on obtient

$$ X_{t+\Delta}=\mu(1-\phi)+\phi\,X_t+\varepsilon_t,\qquad \varepsilon_t\sim \mathcal N\!\Big(0,\tfrac{\sigma^2}{2\theta}(1-\phi^2)\Big) $$

C'est exactement un **AR(1)**. Le « frottement + bruit thermique » du physicien et le « coefficient autorégressif $$\phi$$ + innovation » du statisticien sont deux langages pour une seule et même chose.

### Résultats

Le processus OU est le **premier** processus en temps continu à être à la fois stationnaire, gaussien et markovien (Doob a démontré plus tard que ces trois propriétés réunies ne laissent essentiellement que le processus OU). Il offre un ensemble net de propriétés statistiques — retour à la moyenne, autocorrélation à décroissance exponentielle, variance stationnaire finie — et est devenu le modèle type du processus aléatoire analytiquement soluble.

### Portée et perspectives

Le pont « OU discrétisé = AR(1) » soude directement les processus aléatoires de la physique aux séries temporelles [autorégressives de Yule](../yule-ar/) : c'est la meilleure illustration de la « source commune interdisciplinaire » de cette chronologie. En finance, le processus OU fonde le modèle de taux de Vasicek et le « retour à la moyenne de l'écart » du trading de paires : en ingénierie, c'est le modèle standard du bruit coloré. Sa structure d'autocorrélation exponentielle est aussi à l'origine d'un noyau courant de la régression par processus gaussiens (Matérn-1/2). Aujourd'hui, dès qu'on parle de « retour à la moyenne », de « persistance $$\phi$$ » ou d'« amortissement », on parle presque toujours la langue du processus OU.
