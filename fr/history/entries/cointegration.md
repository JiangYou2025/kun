---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1987 · Informatique"
permalink: /fr/history/e/cointegration/
title: "Cointégration et correction d'erreur (Engle · Granger, 1987)"
lead: "Deux séries qui errent chacune sans but, mais reliées par un élastique invisible — la cointégration vous dit lesquelles de ces « fausses corrélations » sont en réalité de vraies relations."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 6 · Volatilité et cointégration](../../06/).

### Contexte

De nombreuses séries économiques (PIB, prix, taux de change, taux d'intérêt) sont **non stationnaires** : elles n'ont pas de moyenne fixe et dérivent comme une marche aléatoire ; on parle de processus à **racine unitaire** ou $$I(1)$$. Granger et Newbold ont tiré la sonnette d'alarme en 1974 : en régressant l'une sur l'autre deux marches aléatoires indépendantes, on obtient souvent un $$R^2$$ très élevé et des coefficients « significatifs » — c'est la **régression fallacieuse** (*spurious regression*). La corrélation semble forte, mais il n'y a aucune relation : les deux séries ont simplement dérivé, par hasard, dans le même sens. La régression classique devient alors dangereuse sur des données non stationnaires. Pourtant, la théorie économique affirme que certaines variables entretiennent un équilibre de long terme (consommation et revenu, par exemple). Comment distinguer la « fausse corrélation » de la « vraie relation de long terme » ?

### Problème

Si les deux séries sont $$I(1)$$, une régression directe n'est pas fiable. Mais s'il existe entre elles un lien stable de long terme, comment le définir rigoureusement et le tester ? Autrement dit : **quand une combinaison linéaire de deux séries non stationnaires est-elle, au contraire, stationnaire ?**

### Autres courants de l'époque (et leurs limites)

- **Régression directe en niveaux** : MCO sur les séries non stationnaires brutes. C'est précisément le terreau de la régression fallacieuse : les statistiques sont faussées et les conclusions peu fiables.
- **Différencier systématiquement puis régresser** : rendre chaque série stationnaire par différenciation avant de modéliser. La régression fallacieuse disparaît, mais **l'information sur l'équilibre de long terme entre variables est perdue**, et il ne reste que les variations de court terme.
- **Modèles économiques structurels** : imposer des contraintes issues de la théorie. Ils dépendent de la justesse de la spécification et manquent de tests statistiques partant des données.

### Méthode

Engle et Granger proposent la **cointégration** : si $$x_t,y_t$$ sont chacune $$I(1)$$, mais qu'il existe une constante $$\beta$$ rendant la combinaison linéaire stationnaire,

$$ z_t = y_t - \beta\, x_t \;\sim\; I(0)\quad(\text{stationnaire}) $$

alors les deux séries sont dites cointégrées, et $$z_t$$ est l'écart à l'équilibre de long terme. Le test se fait en deux étapes : on régresse d'abord les séries en niveaux pour estimer $$\beta$$ et obtenir les résidus $$\hat z_t$$, puis on utilise le **test de racine unitaire ADF (Dickey–Fuller augmenté)** pour juger si $$\hat z_t$$ est stationnaire — le test ADF estime la régression

$$ \Delta \hat z_t = \rho\,\hat z_{t-1} + \sum_{i=1}^{p}\gamma_i\,\Delta \hat z_{t-i} + u_t $$

et teste $$\rho=0$$ (racine unitaire, pas de cointégration) contre $$\rho<0$$ (stationnarité, cointégration). Si la cointégration est établie, le **théorème de représentation de Granger** garantit que le système peut s'écrire sous forme de **modèle à correction d'erreur (MCE)** :

$$ \Delta y_t = \gamma\, z_{t-1} + \sum_i a_i \Delta y_{t-i} + \sum_j b_j \Delta x_{t-j} + \varepsilon_t,\qquad \gamma<0 $$

Il fond en un seul modèle la dynamique de court terme (les termes en différences) et l'équilibre de long terme ($$z_{t-1}$$) : dès que le système s'écarte de l'équilibre, $$z_{t-1}\neq 0$$, « l'élastique » le ramène à la vitesse $$\gamma$$.

### Résultats

La cointégration fournit une définition rigoureuse et un test opérationnel des relations de long terme entre séries non stationnaires ; elle dissout d'un coup le piège de la régression fallacieuse sans perdre, comme la différenciation aveugle, l'information de long terme. Le MCE est devenu un outil standard de modélisation en macroéconomie et en finance (trading de paires, arbitrage comptant-terme, par exemple). Granger pour la cointégration et Engle pour [ARCH](../arch/) ont partagé le prix Nobel d'économie 2003.

### Portée et perspectives

Engle–Granger a traduit l'intuition économique « équilibre de long terme + ajustement de court terme » dans le langage mathématique de la stationnarité, et refondé l'économétrie des séries temporelles non stationnaires. Leur méthode en deux étapes a ensuite été généralisée par l'approche multivariée par maximum de vraisemblance de Johansen, qui admet plusieurs vecteurs de cointégration. L'idée de la cointégration et de la correction d'erreur — **chercher, dans un monde qui dérive, les combinaisons stables qui restent attachées** — demeure un fondement de l'arbitrage statistique, de la modélisation des relations entre marchés et même de l'analyse causale moderne des séries temporelles.
