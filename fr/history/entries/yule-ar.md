---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1927 · Mathématiques"
permalink: /fr/history/e/yule-ar/
title: "La naissance de l'autorégression (Yule, 1927)"
lead: "Pourquoi un cycle « se déforme »-t-il ? Avec un système linéaire sans cesse excité par des chocs aléatoires, Yule explique la dérive de la période des taches solaires et pose la vision du monde des séries temporelles modernes."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 1 · Autorégression](../../01/).

### Contexte

Dans les années 1920, l'une des données les plus fascinantes dont disposent les statisticiens est le **nombre de taches solaires** : une série annuelle qui remonte au XVIIIe siècle et qui, à l'œil nu, « oscille sur environ 11 ans ». L'astronomie, l'agriculture, la conjoncture économique veulent toutes lire des régularités dans ce genre de cycles. Le paradigme d'analyse dominant est alors celui du **périodogramme** (*periodogram*) et de l'**analyse harmonique** : on voit la série comme la superposition de quelques sinusoïdes cachées, plus un peu de bruit d'observation. Cette approche hérite directement des triomphes de la mécanique céleste : le mouvement des planètes est un cycle déterministe, et il suffit d'en trouver les fréquences et les amplitudes pour calculer exactement l'avenir.

### Problème

Mais les taches solaires refusent d'obéir. Lorsqu'on les ajuste par des sinusoïdes de fréquence fixe, une structure nette subsiste dans les résidus ; pire encore, ce « cycle de 11 ans » **dérive** — tantôt 9 ans, tantôt 13 —, et son amplitude varie elle aussi. S'il y avait vraiment derrière un pendule déterministe, la période ne devrait pas flotter ainsi. **Pourquoi un cycle en apparence régulier ne cesse-t-il de se déformer ?** Le modèle harmonique déterministe n'a pas de réponse.

### Les autres courants de l'époque (et leurs limites)

- **La vision du cycle déterministe (école du périodogramme)** : elle tient pour acquis que série = somme de sinusoïdes cachées, et range toutes les irrégularités dans « l'erreur de mesure ». Son hypothèse implicite est une oscillation pure, à la manière d'un pendule, incapable d'expliquer la dérive aléatoire de la période elle-même.
- **L'autre extrême, celui de Slutsky (la même année, 1927)** : [Slutsky](../slutsky/) montre que des sommes mobiles appliquées à un bruit purement aléatoire peuvent elles aussi faire « émerger » des fluctuations étonnamment périodiques. C'est un avertissement profond, mais poussé à l'extrême, il fait soupçonner que tout cycle est illusoire — ce n'est pas non plus une réponse complète.
- La vérité est entre les deux : ni purement déterministe, ni pur bruit, mais **un système doté d'une structure interne de rappel, entraîné par le bruit**.

### Méthode

Yule propose un troisième point de vue : la valeur présente est une régression linéaire sur quelques valeurs passées, à laquelle s'ajoute un choc aléatoire imprévisible. C'est le modèle **AR(p)** :

$$ X_t = c + \sum_{i=1}^{p}\phi_i X_{t-i} + \varepsilon_t,\qquad \varepsilon_t \sim \mathrm{WN}(0,\sigma^2) $$

Chaque $$\phi_i$$ mesure l'influence du retard $$i$$, et $$\varepsilon_t$$ est l'« innovation » (*innovation*) — la perturbation aléatoire subie par le système, impossible à prédire à partir de l'histoire. La clé réside dans l'équation caractéristique de l'AR(2)

$$ 1-\phi_1 z-\phi_2 z^2 = 0 $$

Lorsque ses racines sont **complexes**, le système présente une **oscillation amortie** : chaque choc aléatoire déclenche une oscillation qui s'éteint progressivement, et de nouveaux chocs la « rallument » sans cesse — le cycle existe donc, mais n'est jamais exact. C'est là l'origine mathématique de la « quasi-périodicité ». Les **équations de Yule–Walker** qui l'accompagnent relient l'autocorrélation $$\rho_k$$ aux paramètres, ce qui permet d'estimer les coefficients AR à partir des données :

$$ \rho_k = \sum_{i=1}^{p}\phi_i\, \rho_{k-i},\qquad k\ge 1 $$

### Résultats

L'ajustement d'un AR(2) à la série des taches solaires est **bien meilleur** que celui du modèle harmonique déterministe : les résidus sont plus proches d'un bruit blanc, et la dérive de la période est reproduite tout naturellement. Un modèle aléatoire à deux ou trois paramètres seulement réussit là où une batterie de sinusoïdes échoue — et il peut en outre **extrapoler et prévoir**, en donnant un avenir assorti de son incertitude.

### Portée et perspectives

En remplaçant le « cycle déterministe » par le « processus aléatoire », Yule a posé la vision du monde des séries temporelles modernes : la tâche centrale passe de « trouver les fréquences cachées » à « **identifier la structure aléatoire du système excité** ». Autorégression, innovation, racines caractéristiques et stationnarité, estimation de Yule–Walker — ce langage mène directement à la [décomposition de Wold](../wold/) de 1938, au cadre [ARMA/ARIMA de Box–Jenkins](../box-jenkins/) de 1970, et jusqu'au paradigme fondamental de la « génération autorégressive » des modèles profonds actuels. Cent ans plus tard, quand nous demandons à un réseau de neurones de « prédire la valeur suivante à partir du passé », c'est toujours, au fond, ce pas de Yule.
