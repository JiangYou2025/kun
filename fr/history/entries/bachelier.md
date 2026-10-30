---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1900 · Mathématiques"
permalink: /fr/history/e/bachelier/
title: "Théorie de la spéculation (Bachelier, 1900)"
lead: "Sur quel cours parier pour demain ? Dans sa thèse, Bachelier donne une réponse froide : la meilleure prévision est le cours d'aujourd'hui — une seule phrase qui sème à la fois la marche aléatoire, le mouvement brownien et la finance mathématique moderne."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

En 1900, à Paris, Louis Bachelier achève sous la direction d'Henri Poincaré sa thèse de doctorat, *Théorie de la spéculation*. Il y étudie les cours des rentes d'État à la Bourse de Paris. L'économie de l'époque n'utilisait presque aucun outil probabiliste : les prix étaient vus comme le résultat du jeu de l'offre et de la demande, et personne ne les modélisait comme un **processus aléatoire**. Le point de départ de Bachelier est très pragmatique : quel est le juste prix d'une option ou d'un contrat à terme ? Pour y répondre, il faut d'abord un modèle mathématique de « la manière dont le prix fluctue au cours du temps ».

### Problème

Les hausses et les baisses des cours semblent désordonnées, sans aucune régularité. Mais cette « absence de régularité » peut-elle elle-même être décrite mathématiquement ? Plus aigu encore : **si le marché est équitable, quelle doit être la meilleure prévision du prix futur ?** Intuitivement, tout le monde veut prédire la hausse ou la baisse ; mais dans un marché équitable et bien informé, l'espérance du futur doit-elle ou non être égale au présent ?

### Autres courants de l'époque (et leurs limites)

- **La vision déterministe de la « valeur intrinsèque »** : le prix oscillerait autour d'une vraie valeur calculable, et il suffirait de bien la calculer pour prévoir. Sa limite : elle rejette les fluctuations de court terme comme du bruit, ne peut quantifier le risque et ne fournit aucun prix d'option.
- **Graphiques et extrapolation de tendance** : « lire » une tendance sur la courbe historique et la prolonger. Cette approche suppose implicitement que « la direction passée se maintiendra » ; mais dans un marché efficient, toute tendance prévisible est effacée par l'arbitrage, et une telle extrapolation manque de fondement théorique.
- Les deux évitent le cœur du problème : la **structure probabiliste** des fluctuations de prix. Avant Bachelier, presque personne n'avait modélisé de front cette incertitude.

### Méthode

Bachelier modélise les variations de prix comme le cumul d'un grand nombre de petits chocs indépendants, et obtient une **marche aléatoire** en temps continu — ce qu'on appellera plus tard le mouvement brownien. Dans son modèle, les accroissements du prix suivent une loi gaussienne de moyenne nulle, dont la variance croît linéairement avec le temps :

$$ X_{t+\Delta}-X_t \sim \mathcal N(0,\;\sigma^2\Delta),\qquad \mathrm{Var}(X_t-X_0)=\sigma^2 t $$

On en tire immédiatement une conclusion profonde — **la prévision optimale est la valeur actuelle** :

$$ \mathbb E[X_{t+s}\mid \mathcal F_t]=X_t $$

Autrement dit, étant donné toute l'information $$\mathcal F_t$$ disponible jusqu'à $$t$$, l'espérance conditionnelle du prix futur est le prix d'aujourd'hui. C'est l'ébauche de la **martingale** : la part prévisible a déjà été absorbée par le prix, et il ne reste que des fluctuations aléatoires imprévisibles. Il en déduit aussi une formule de prix des options, reliée aux solutions de l'équation de la chaleur.

### Résultats

Bachelier n'a pas seulement introduit le langage des probabilités dans la modélisation financière : il a aussi, **cinq ans avant Einstein**, établi mathématiquement les propriétés de la loi du mouvement brownien et son lien avec l'équation de diffusion. Ses idées sur le prix des options sont l'ancêtre lointain de la formule de Black–Scholes, plus d'un demi-siècle plus tard. Le principe « meilleure prévision = prix actuel » est aussi la toute première formulation mathématique de l'efficience des marchés.

### Portée et perspectives

Longtemps ignorée, cette thèse n'a été redécouverte que dans les années 1950, notamment par Samuelson, et elle est aujourd'hui saluée comme l'œuvre fondatrice de la finance mathématique. Elle a pour la première fois noué ensemble processus aléatoires, martingales et équation de diffusion : la [théorie physique du mouvement brownien](../brownian-motion/) sera ensuite donnée par Einstein, sa formalisation mathématique rigoureuse deviendra le [processus de Wiener](../brownian-motion/), et la théorie générale des martingales sera achevée par [Lévy](../levy/) et Doob. Les corrections apportées à l'idée que « le prix suit approximativement une marche aléatoire » — accroissements à queues épaisses, sauts — mènent quant à elles aux [processus de Lévy](../levy/), à ARCH/GARCH et aux diffusions avec sauts. Chaque modèle qui prévoit aujourd'hui une série financière en la traitant comme un processus aléatoire s'appuie sur ce premier pas de Bachelier.
