---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2001 · Informatique"
permalink: /fr/history/e/gbdt/
title: "Le gradient boosting (Friedman, 2001)"
lead: "Si l'on voit l'« entraînement d'un modèle » comme une descente de gradient dans l'espace des fonctions, dans quelle direction faut-il avancer à chaque pas ? La réponse de Friedman : ajuster le gradient négatif de l'étape précédente — et y aller avec un arbre."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 8 · Apprentissage automatique](../../08/).

### Contexte

À la fin des années 1990, deux voies de l'**apprentissage ensembliste** progressent en parallèle : le Bagging et les forêts aléatoires de Breiman (en parallèle, pour réduire la variance) et l'AdaBoost de Freund et Schapire (en série, pour réduire le biais). AdaBoost donnait des résultats stupéfiants, mais la raison de son efficacité est longtemps restée une énigme. En 1999–2001, Friedman en propose une lecture unifiée et profonde : le boosting est, au fond, une **descente de gradient** dans l'**espace des fonctions**. Ainsi naît la **machine de gradient boosting (Gradient Boosting Machine, GBM/GBDT)**, qui devient l'une des références les plus solides pour les données tabulaires et pour la prévision de séries temporelles à partir de variables construites.

### Problème

Un arbre de décision isolé est facile à interpréter, mais peu expressif et de forte variance ; pour être à la fois précis et stable, il faut combiner de nombreux modèles faibles. AdaBoost ne correspond qu'au cas particulier de la perte exponentielle et ne s'applique pas directement à la régression, aux quantiles, à Poisson ou à **toute autre perte différentiable**. La question centrale est donc : **étant donné une fonction de perte quelconque, comment empiler systématiquement, pas à pas, des apprenants faibles pour en faire un apprenant fort ?**

### Les autres courants de l'époque (et leurs limites)

- **AdaBoost** : pionnier, mais lié à la perte exponentielle, **sensible aux valeurs aberrantes et au bruit d'étiquetage**, et mal expliqué.
- **Forêts aléatoires (Bagging)** : parallèles, résistantes au surapprentissage, faciles à utiliser ; mais elles réduisent uniquement la variance, sans faire baisser activement le biais, et ne peuvent pas optimiser de manière ciblée une perte personnalisée.
- **Régression par réseaux de neurones** : très expressive, mais à l'époque l'entraînement était instable et le réglage coûteux sur des données tabulaires ou temporelles de taille petite à moyenne, souvent en deçà des ensembles d'arbres.

### Méthode

On considère la fonction de prédiction $$ F(x) $$ comme l'objet à optimiser, avec pour but de minimiser la perte espérée $$ \sum_i L(y_i, F(x_i)) $$. À l'étape $$ m $$, on calcule d'abord, pour chaque exemple, le **gradient négatif** de la perte par rapport à la prédiction courante (le « pseudo-résidu ») :

$$ r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}} $$

Pour la perte quadratique, c'est exactement le **résidu** ordinaire $$ y_i - F_{m-1}(x_i) $$ ; pour les autres pertes, c'en est la généralisation. On entraîne ensuite un **arbre de régression** $$ h_m(x) $$ sur ces pseudo-résidus, puis on met à jour le modèle avec un pas (taux d'apprentissage) $$ \nu $$ :

$$ F_m(x) = F_{m-1}(x) + \nu\, \gamma_m\, h_m(x) $$

où $$ \gamma_m $$ est déterminé par une recherche linéaire. Tout le procédé revient à avancer dans l'espace des fonctions selon le gradient négatif, en prenant « un arbre » comme approximation de la direction de descente à chaque pas. Combiné à une régularisation par **rétrécissement (shrinkage)** $$ \nu<1 $$, par **sous-échantillonnage des lignes et des colonnes** et par la limitation de la profondeur des arbres, il résiste efficacement au surapprentissage.

### Résultats

Le GBDT a longtemps régné sur les données structurées et tabulaires : compétitions Kaggle, risque de crédit, recommandation, classement pour la recherche — il est partout. Les implémentations industrielles qui ont suivi, **XGBoost (2016)**, **LightGBM** et **CatBoost**, l'ont poussé à l'extrême grâce à l'approximation du second ordre, aux découpages par histogrammes ou à la croissance feuille par feuille. Pour les séries temporelles, construire des variables par fenêtre glissante, retards, statistiques mobiles, calendrier et jours fériés, puis les confier à un GBDT, constitue souvent une **référence solide** difficile à battre — dans de grandes compétitions de prévision comme M5, les solutions de type LightGBM figurent en tête du classement.

### Portée et perspectives

L'intuition de Friedman — **voir l'apprentissage comme une descente de gradient dans l'espace des fonctions** — dépasse les arbres eux-mêmes : c'est un pont entre le boosting et l'optimisation moderne, qui fait aussi écho à l'esprit de l'apprentissage profond, « s'approcher pas à pas en suivant le gradient ». Dans le domaine des séries temporelles, le GBDT et la [SVR](../svr/) ont ensemble établi le paradigme « **variables construites + apprenant puissant** » ; face aux modèles séquentiels profonds ([RNN/LSTM](../lstm/), voire Transformer), un GBDT bien réglé reste souvent le seuil honnête qui permet de juger si « la profondeur en vaut la peine ». Simple, robuste et interprétable, il traverse les années sans prendre une ride.
