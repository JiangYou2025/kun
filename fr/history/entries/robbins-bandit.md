---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1952 · Mathématiques"
permalink: /fr/history/e/robbins-bandit/
title: "Bandits manchots et plans d'expérience séquentiels (Robbins, 1952)"
lead: "Face à plusieurs machines à sous aux gains inconnus, faut-il toujours jouer celle qui rapporte le plus, ou prendre le risque d'en essayer d'autres ? Robbins a mis en équations le dilemme « exploration contre exploitation »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Après la Seconde Guerre mondiale, la statistique passe de « collecter toutes les données, puis analyser » à « décider au fil de la collecte ». L'analyse séquentielle de Wald avait déjà montré qu'arrêter l'échantillonnage au besoin économise des échantillons. Dans son article de 1952, « Some aspects of the sequential design of experiments », Herbert Robbins pousse cette perspective plus loin : une expérience peut non seulement **décider quand s'arrêter**, mais aussi, à chaque pas, **décider où prélever l'observation suivante**. Essais cliniques, contrôles de production, diffusion publicitaire : autant de situations où l'on « apprend en faisant ».

### Problème

Imaginez $$K$$ machines à sous (les « bras »), chacune d'espérance de gain inconnue. Vous disposez d'un nombre limité de tirages, et chaque tirage ne révèle que le gain aléatoire de la machine choisie. **Faut-il miser toutes ses chances sur la machine qui semble actuellement la meilleure (exploitation), ou en consacrer une partie à essayer les autres pour ne pas passer à côté d'une meilleure (exploration) ?** Miser trop fort, c'est risquer de rester bloqué sur un bras sous-optimal ; trop essayer, c'est gaspiller des tours — telle est la tension fondamentale **exploration contre exploitation**, qui est aussi un problème de décision séquentielle en ligne.

### Autres courants de l'époque (et leurs limites)

- **Plans d'expérience fixes + tests d'hypothèses classiques** : on fixe à l'avance la taille d'échantillon de chaque traitement, puis on collecte en une fois. Rigoureux statistiquement, mais impossible en cours de collecte de répercuter « ce qu'on a déjà observé de bon ou de mauvais » sur les allocations suivantes, d'où un gaspillage d'échantillons et des gains retardés.
- **Glouton pur (toujours choisir le bras dont l'estimation actuelle est la plus haute)** : optimal à court terme, mais une malchance précoce peut faire abandonner trop tôt le véritable meilleur bras et enfermer durablement dans le sous-optimal.
- **Essais aléatoires uniformes purs** : l'information est collectée à fond, mais on gaspille continuellement des tours sur des bras manifestement sous-optimaux, et la perte cumulée est importante.

### Méthode

Robbins a formalisé la mesure centrale qu'est le **regret** : on cumule l'écart entre « le gain espéré de la meilleure stratégie fixe, connue a posteriori » et le gain de la stratégie réellement suivie. Notons $$\mu_a$$ l'espérance de gain du bras $$a$$, $$\mu^{*}=\max_a \mu_a$$ celle du meilleur bras, et $$A_t$$ le bras choisi au pas $$t$$ au cours de $$T$$ tours : le regret cumulé vaut alors

$$ R_T = T\,\mu^{*} - \mathbb{E}\!\left[\sum_{t=1}^{T}\mu_{A_t}\right] = \sum_{a}\Delta_a\,\mathbb{E}[N_a(T)] $$

où $$\Delta_a=\mu^{*}-\mu_a$$ est l'écart de sous-optimalité du bras $$a$$ et $$N_a(T)$$ le nombre de fois qu'il a été choisi. Une bonne stratégie vise à faire croître $$R_T$$ aussi lentement que possible (de façon **sous-linéaire**, c'est-à-dire $$R_T/T\to0$$). Robbins a proposé des règles simples garantissant de choisir asymptotiquement le meilleur bras, et a montré que pour maîtriser le regret, il faut réduire progressivement l'exploration au fil du temps et concentrer les tours sur les bras à fort rendement.

### Résultats

Cet article a posé le problème originel des plans d'expérience séquentiels et de l'**apprentissage par renforcement**. Plus tard, Lai et Robbins (1985) ont démontré une borne inférieure logarithmique du regret, $$\Omega(\log T)$$, atteinte par des algorithmes comme UCB (borne supérieure de confiance) ou l'échantillonnage de Thompson. Aujourd'hui, l'« allocation adaptative du trafic » dans les tests A/B, les systèmes de recommandation et la publicité en ligne n'est, au fond, que la mise en œuvre industrielle des bandits manchots.

### Portée et perspectives

Les bandits manchots ont distillé le dilemme « apprendre en gagnant dans l'incertitude » en un objet mathématique analysable et optimisable, et le « regret » est devenu l'étalon universel de la décision en ligne. Ils se raccordent en aval à la [programmation dynamique de Bellman](../bellman-dp/) et aux processus de décision markoviens (un bandit avec état, c'est l'apprentissage par renforcement), et irriguent les plans d'expérience, l'optimisation bayésienne et la décision automatisée. Chaque fois qu'un système moderne doit arbitrer entre « exploiter le meilleur connu » et « explorer un inconnu peut-être meilleur », c'est encore le regret légué par Robbins qu'il mesure.
