---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1986 · Informatique"
permalink: /fr/history/e/garch/
title: "Le modèle GARCH (Bollerslev, 1986)"
lead: "Pour se souvenir de la volatilité, ARCH doit traîner de très nombreux retards ; Bollerslev donne à la variance son propre « hier », et trois paramètres suffisent alors à retenir les tempêtes de longue portée."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 6 · Volatilité et cointégration](../../06/).

### Contexte

Le [modèle ARCH d'Engle](../arch/) a été le premier à faire de la variance conditionnelle une grandeur variable dans le temps et estimable, capturant avec élégance le regroupement de la volatilité. Mais l'ajustement aux données financières réelles a mis au jour une difficulté pratique : sur les marchés, la persistance de la volatilité est **très longue** — l'effet d'un grand choc met de nombreuses périodes à s'estomper. Pour exprimer une telle mémoire longue, ARCH doit faire dépendre la variance des carrés des résidus de nombreuses périodes passées, c'est-à-dire prendre un ordre $$q$$ très élevé, ce qui entraîne **trop de paramètres**, une estimation instable et des violations fréquentes des contraintes de positivité. Comment conserver la mémoire longue tout en réduisant le nombre de paramètres ?

### Problème

Dans le cadre ARCH, la variance ne peut être qu'une somme pondérée des carrés des résidus de quelques périodes passées. Pour approcher une pondération à décroissance lente et de longue portée, une simple somme glissante doit être très longue. **Peut-on introduire une structure récursive qui permette à la variance de « se souvenir » de sa propre histoire, et ainsi exprimer un regroupement de longue portée avec très peu de paramètres ?**

### Les autres courants de l'époque (et leurs limites)

- **ARCH(q) d'ordre élevé** : on augmente directement $$q$$. Cela approche la mémoire longue, mais le nombre de paramètres croît linéairement avec $$q$$ ; l'estimation est difficile, les contraintes dures à respecter et le risque de surapprentissage élevé.
- **Variance mobile sur fenêtre fixe** : on prend la variance empirique d'une fenêtre récente. Toutes les données de la fenêtre ont le même poids, celles qui en sortent sont oubliées d'un coup : aucune structure de décroissance progressive.
- **Volatilité stochastique (SV)** : la variance est pilotée par un processus latent indépendant ; souple, mais l'estimation par maximum de vraisemblance avec variable latente restait épineuse à l'époque.

### Méthode

Bollerslev propose l'ARCH généralisé (GARCH), dont l'étape clé consiste à faire dépendre la variance conditionnelle **aussi de ses propres valeurs retardées**. Le GARCH(1,1), le plus utilisé, s'écrit :

$$ \sigma_t^2 = \omega + \alpha\,\varepsilon_{t-1}^2 + \beta\,\sigma_{t-1}^2,\qquad \omega>0,\;\alpha\ge 0,\;\beta\ge 0 $$

Trois paramètres seulement : $$\omega$$ est le niveau de variance de base, $$\alpha$$ mesure l'effet du choc le plus récent, et $$\beta$$ prolonge la variance de la période précédente dans la période courante. En déroulant cette récurrence, on obtient une **pondération à décroissance exponentielle** de tous les carrés des résidus passés — un GARCH(1,1) équivaut donc à un ARCH d'ordre infini, et trois paramètres suffisent à contenir une mémoire de longue portée. La somme $$\alpha+\beta$$ mesure la persistance de la volatilité : plus elle est proche de 1, plus les chocs s'atténuent lentement et plus le regroupement est tenace. Lorsque $$\alpha+\beta<1$$, le processus est stationnaire en covariance et sa **variance inconditionnelle** vaut

$$ \mathrm{Var}(\varepsilon_t)=\frac{\omega}{1-\alpha-\beta} $$

Le modèle s'estime lui aussi par maximum de vraisemblance, sous une hypothèse de loi conditionnelle normale (ou de Student).

### Résultats

Avec une paramétrisation minimale, le GARCH(1,1) décrit avec précision le regroupement et la persistance de la volatilité des rendements d'actions, de change ou de taux, et il est devenu le modèle de volatilité le plus cité et le plus utilisé en économétrie financière — le point de départ quasi par défaut de la gestion des risques, de l'évaluation d'options et du calcul de la VaR. Il est si souvent « suffisamment bon » dans les ajustements empiriques que « GARCH(1,1) » est devenu une formule toute faite du métier.

### Portée et perspectives

En comprimant les longs retards d'ARCH en trois paramètres grâce à un seul terme récursif, GARCH illustre la sagesse de modélisation qui consiste à « **échanger une structure autorégressive contre la parcimonie** » — exactement comme l'AR par rapport au MA au niveau de la moyenne. Il a engendré une vaste famille : EGARCH et GJR-GARCH pour l'effet de levier, FIGARCH pour la mémoire longue, DCC-GARCH dans le cas multivarié, etc. Aujourd'hui encore, les modèles de volatilité fondés sur l'apprentissage profond prennent souvent GARCH comme référence de comparaison, ce qui montre la portée fondatrice de cette étape.
