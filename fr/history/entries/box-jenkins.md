---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1970 · Informatique"
permalink: /fr/history/e/box-jenkins/
title: "ARIMA et la méthodologie de modélisation (Box · Jenkins, 1970)"
lead: "La différenciation dompte la non-stationnarité, une procédure en trois étapes dompte la modélisation. Box et Jenkins réunissent des techniques éparses de séries temporelles en une méthodologie d'ingénierie opérationnelle et reproductible."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 5 · ARIMA](../../05/).

### Contexte

À la fin des années 1960, les séries temporelles disposaient déjà de nombreuses pièces : l'autorégression AR de [Yule](../yule-ar/), la moyenne mobile MA inspirée de [Slutsky](../slutsky/), le cadre théorique ARMA issu de la [décomposition de Wold](../wold/), ainsi que les méthodes spectrales. Mais il s'agissait surtout d'outils pour processus stationnaires, alors que les données réelles — ventes, production, prix — présentent souvent tendance et saisonnalité, et **ne sont pas stationnaires**. Face à une série réelle, ce qui manquait aux praticiens n'était pas seulement un modèle, mais une démarche : « quel modèle utiliser, comment choisir les ordres, comment vérifier ».

### Problème

Deux niveaux de difficulté s'entremêlent. D'abord, **comment traiter la non-stationnarité** : une série avec tendance ou comportement de marche aléatoire ne peut pas recevoir directement un modèle stationnaire. Ensuite, **comment systématiser la modélisation** : face à des données concrètes, comment choisir de façon argumentée parmi les nombreux ordres possibles d'AR, de MA et d'ARMA, plutôt que par tâtonnements au jugé ? Il fallait une procédure enseignable et reproductible.

### Autres courants de l'époque (et leurs limites)

- **Méthodes purement spectrales / périodogramme** : excellentes pour révéler la structure fréquentielle, mais elles ne fournissent pas directement un modèle génératif paramétré commode pour la prévision et l'extrapolation.
- **Tendance déterministe + décomposition saisonnière** : découper la série en tendance, saison et résidu. Intuitif, mais les hypothèses sur la forme de la tendance sont fortes, et le résidu conserve souvent une structure de corrélation qui pourrait être modélisée.
- **AR ou MA utilisés isolément** : chacun est efficace, mais sans critères unifiés de sélection et de diagnostic, on surajuste facilement ou l'on choisit mal les ordres.

### Méthode

Box–Jenkins introduisent l'**opérateur de différence** $$\nabla=1-B$$ ($$B$$ est l'opérateur de retard, $$B X_t=X_{t-1}$$) pour éliminer la tendance : on différencie $$d$$ fois une série non stationnaire pour la rendre stationnaire, puis on modélise la partie stationnaire par un ARMA, ce qui donne l'**ARIMA(p,d,q)** :

$$ \phi(B)\,(1-B)^{d}\,X_t=\theta(B)\,\varepsilon_t $$

où $$\phi(B)=1-\phi_1 B-\dots-\phi_p B^p$$ est l'opérateur AR et $$\theta(B)=1+\theta_1 B+\dots+\theta_q B^q$$ l'opérateur MA. En présence d'une période saisonnière $$s$$, on l'étend au **SARIMA**, en ajoutant la différence saisonnière $$(1-B^s)^D$$ et des opérateurs saisonniers. Plus important encore, ils proposent une **méthodologie en trois étapes** :

- **Identification** : à partir de la forme de l'autocorrélation (ACF) et de l'autocorrélation partielle (PACF), déterminer provisoirement $$p,d,q$$ ;
- **Estimation** : ajuster les paramètres par maximum de vraisemblance ou moindres carrés ;
- **Diagnostic** (*diagnostic checking*) : vérifier que les résidus sont proches d'un bruit blanc (par exemple avec le test de Ljung–Box) ; sinon, revenir à l'identification et itérer.

### Résultats

Cette procédure a fait passer la modélisation des séries temporelles d'un savoir-faire empirique à une ingénierie enseignable et reproductible. ARIMA/SARIMA est devenu pendant des décennies la machine de base de la prévision, largement utilisée pour l'économie, les stocks, les ventes et la demande, et reste aujourd'hui encore une référence solide de la prévision statistique. Le paradigme itératif « identification — estimation — diagnostic » est aussi devenu un modèle général de la modélisation statistique appliquée.

### Portée et perspectives

Box–Jenkins a accompli le passage décisif de l'accumulation théorique, de [Yule](../yule-ar/) et [Slutsky](../slutsky/) à [Wold](../wold/), vers une méthodologie pratique. Les développements suivants prolongent ce chemin : sélection automatique des ordres par critères d'information (AIC, BIC), tests de racine unitaire pour décider du nombre de différenciations, [ARCH/GARCH](../arch/) pour compléter la description de la dynamique de la variance. Même aujourd'hui, à l'heure de l'apprentissage automatique et de la prévision profonde, ARIMA reste l'étalon honnête qui permet de juger si un modèle complexe apporte vraiment un gain, et sa discipline d'ingénierie « modéliser — tester — corriger » n'a rien perdu de sa fraîcheur.
