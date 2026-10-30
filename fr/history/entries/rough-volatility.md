---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2014–18 · Mathématiques"
permalink: /fr/history/e/rough-volatility/
title: "Volatilité rugueuse (Gatheral · Jaisson · Rosenbaum, 2014–18)"
lead: "Pendant des décennies, on a cru la volatilité dotée d'une longue mémoire et plutôt « lisse ». Quand on s'est vraiment mis à mesurer sa trajectoire, on l'a découverte anormalement rugueuse — avec un exposant de Hurst bien inférieur à ½."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

La volatilité est le nerf de la finance, et pourtant elle n'est pas directement observable. Depuis le [GARCH](../garch/) et les modèles à volatilité stochastique, le consensus dominant tenait en deux points : la volatilité a une **longue mémoire** (son autocorrélation décroît lentement), et le processus qui la pilote est généralement modélisé par un **mouvement brownien** (volatilité stochastique standard) ou par un mouvement brownien fractionnaire à longue mémoire, $$ H>\tfrac12 $$. En 2014, l'article de Gatheral, Jaisson et Rosenbaum, « Volatility is rough », mène une analyse d'échelle directement sur les séries de **volatilité réalisée (realized volatility)** et aboutit à une conclusion qui ébranle la communauté : la trajectoire de la volatilité est **anormalement rugueuse**.

### Problème

Grâce aux données à haute fréquence, on peut enfin construire la **volatilité réalisée** à partir des rendements intrajournaliers, et ainsi « observer » approximativement la trajectoire de la volatilité elle-même. On peut donc répondre de front à une vieille question : **à quel point le processus aléatoire qui pilote la volatilité est-il lisse ?** Le mouvement brownien standard correspond à un exposant de Hurst $$ H=\tfrac12 $$ ; les modèles à longue mémoire défendent $$ H>\tfrac12 $$ (persistant, lisse). De quel côté penchera la mesure ?

### Autres courants de l'époque (et leurs limites)

- **Volatilité stochastique classique (par exemple Heston)** : la volatilité est pilotée par un mouvement brownien standard ($$ H=\tfrac12 $$) ; mathématiquement commode, avec des prix en forme semi-fermée, mais il peine à ajuster simultanément la pente du smile de volatilité implicite à court et à long terme.
- **Longue mémoire / volatilité stochastique fractionnaire ($$ H>\tfrac12 $$)** : la persistance est introduite pour expliquer la lente décroissance de l'autocorrélation de la volatilité ; elle va dans le sens contraire des mesures, et ne touche pas à la « rugosité à court terme ».
- **Modèles de sauts-diffusion** : ils fabriquent des pics à l'aide de sauts, mais prennent à tort la « rugosité » pour des sauts discrets, masquant la faible régularité de la trajectoire continue elle-même.

### Méthode

Le cœur de la méthode est la mesure de la **loi d'échelle** de la série du logarithme de la volatilité. Pour un décalage $$ \Delta $$, on calcule les moments d'ordre $$ q $$ des accroissements :

$$ m(q,\Delta) = \mathbb{E}\big[\,|\log\sigma_{t+\Delta} - \log\sigma_t|^q\,\big] \sim \Delta^{\,q H} $$

En coordonnées log-log, $$ \log m(q,\Delta) $$ en fonction de $$ \log\Delta $$ est une droite dont la pente donne $$ qH $$, d'où une estimation de l'**exposant de Hurst $$ H $$**. Sur de très nombreux actifs et périodes, les résultats empiriques sont étonnamment concordants :

$$ H \approx 0.1 \;(\ll \tfrac12) $$

Un $$ H $$ aussi petit signifie que la trajectoire de la volatilité est **extrêmement rugueuse** (sa régularité locale est faible, et son caractère presque partout non dérivable dépasse de loin celui du mouvement brownien). En conséquence, des modèles comme le **Bergomi rugueux (rBergomi)** modélisent la volatilité comme pilotée par un **mouvement brownien fractionnaire** $$ W^H $$ :

$$ \log\sigma_t^2 = \xi + \eta\, W_t^{H},\qquad H<\tfrac12 $$

où la structure de covariance de $$ W^H $$ est contrôlée par $$ H $$. Point à souligner : la rugosité (petit $$ H $$, faible régularité à courte portée) et la longue mémoire (lente décroissance de l'autocorrélation) sont **deux phénomènes à des échelles différentes** ; la volatilité rugueuse met l'accent sur le premier, corrigeant l'ancienne idée qui confondait les deux.

### Résultats

Avec seulement trois ou quatre paramètres, le rBergomi reproduit simultanément la **structure par terme et la pente du smile** de la surface de volatilité implicite, et ajuste en particulier avec précision la pente abrupte des options à échéance courte, que les modèles classiques ne parvenaient jamais à aplatir — c'est l'empreinte financière directe de la rugosité. La volatilité rugueuse est aussitôt devenue l'une des directions les plus actives de la finance quantitative, et a donné lieu à des algorithmes efficaces de simulation et d'évaluation pour les processus fractionnaires, ainsi qu'à des explications par les mécanismes de microstructure de marché (les processus de Hawkes auto-excitants décrivant le flux d'ordres du trading à haute fréquence engendrent, à la limite d'échelle, une volatilité rugueuse).

### Portée et perspectives

La volatilité rugueuse est un modèle du genre « **laisser parler les données** » : lorsque les données à haute fréquence nous ont enfin permis de regarder en face la trajectoire de la volatilité, elles ont renversé l'hypothèse par défaut — lisse, à longue mémoire — en vigueur depuis des décennies, et ramené **le mouvement brownien fractionnaire et les faibles exposants de Hurst** au premier plan de la modélisation financière. Elle s'inscrit dans la lignée des interrogations de l'[éconophysique](../econophysics/) sur les lois d'échelle et la longue mémoire, et fait écho, à une génération de distance, à l'analyse de l'étendue de [Hurst](../hurst/). L'explication unifiée, du flux d'ordres microscopique à la surface de volatilité macroscopique, progresse encore, mais « la volatilité est rugueuse » est désormais un fait incontournable de l'évaluation moderne des produits dérivés.
