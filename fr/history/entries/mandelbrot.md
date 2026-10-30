---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1963 · Mathématiques"
permalink: /fr/history/e/mandelbrot/
title: "Queues lourdes, fractales et mémoire longue (Mandelbrot, 1963)"
lead: "Les flambées et les effondrements du prix du coton sont bien plus violents et bien plus fréquents que ne le permet la courbe en cloche. Mandelbrot déchire ainsi l'hypothèse gaussienne et introduit queues lourdes, fractales et mémoire longue dans les séries temporelles financières."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans la première moitié du XXe siècle, l'hypothèse par défaut de la modélisation financière et économique était **gaussienne** : les variations de prix suivent une loi normale, indépendantes et de variance finie. C'était le socle de la tradition de la marche aléatoire depuis Bachelier, et ce sera plus tard l'une des prémisses de [Black–Scholes](../black-scholes/). La normalité implique que les événements extrêmes sont quasi impossibles et que l'écart type suffit à décrire le risque. Mandelbrot dispose d'une longue série de **prix du coton** couvrant un siècle et entreprend de tester cette hypothèse.

### Problème

Les données ne se plient pas à la gaussienne. La distribution des rendements présente un **pic haut et pointu** et des **queues longues et lourdes** : des fluctuations violentes censées survenir une fois tous les dix mille ans se produisent tous les quelques années. De plus, la volatilité se **regroupe** — les grandes fluctuations sont souvent suivies de grandes fluctuations. **Si les événements extrêmes sont bien plus fréquents que ne le prévoit la loi normale, alors toutes les mesures de risque fondées sur la normalité et la variance finie sous-estiment systématiquement le risque.** C'est une question qui touche aux fondements mêmes de la modélisation.

### Les autres courants de l'époque (et leurs limites)

- **La marche aléatoire gaussienne** : mathématiquement élégante et commode pour les calculs, mais elle sous-estime les queues et ne peut expliquer la fréquence des flambées et des krachs.
- **L'hypothèse d'accroissements indépendants** : les rendements à différents instants seraient décorrélés. Or les données montrent que la volatilité présente une dépendance à longue portée (mémoire longue) ; l'hypothèse d'indépendance est trop forte.
- **La vision purement déterministe en cycles / tendances** : elle tente d'ajuster le marché par des courbes régulières, mais ignore la rugosité et l'autosimilarité de la trajectoire des prix elle-même.

### Méthode

Mandelbrot propose de décrire les rendements par les **lois stables de Lévy**. Une loi stable est paramétrée par un exposant $$\alpha\in(0,2]$$, et ses queues décroissent en loi de puissance :

$$ \mathbb{P}(|X|>x)\sim C\,x^{-\alpha},\qquad 0<\alpha<2 $$

Pour $$\alpha<2$$, la variance diverge : c'est l'origine des queues lourdes ($$\alpha=2$$ redonne la gaussienne). Il développe ensuite les **fractales** et le **mouvement brownien fractionnaire** $$B_H(t)$$ pour décrire la mémoire longue, la covariance étant déterminée par l'exposant de Hurst $$H$$ :

$$ \mathbb{E}\!\left[B_H(t)\,B_H(s)\right]=\tfrac{1}{2}\left(|t|^{2H}+|s|^{2H}-|t-s|^{2H}\right) $$

Pour $$H>1/2$$, les accroissements sont positivement corrélés, avec une mémoire longue persistante ; pour $$H<1/2$$, ils sont antipersistants. La trajectoire des prix est donc une **fractale autosimilaire** : agrandissez n'importe quel segment, sa forme statistique ressemble à celle de l'ensemble, sans aucune échelle « suffisamment lisse ».

### Résultats

Queues lourdes et mémoire longue sont dès lors devenues des sujets centraux de la modélisation financière. Les travaux de Mandelbrot expliquent pourquoi les crises sont bien plus fréquentes que ne le prévoit la loi normale, et ont introduit dans la gestion des risques un respect salutaire pour les queues. Même si les lois stables pures, à variance infinie, sont difficiles à appliquer directement, elles ont engendré toute une série de modèles successeurs plus opérationnels.

### Portée et perspectives

Ce fil mène à deux grandes branches : d'une part, la voie à variance finie des modèles [ARCH/GARCH](../arch/) qui décrivent le regroupement de la volatilité ; d'autre part, l'introduction de la mémoire longue dans la moyenne et la volatilité avec l'**ARFIMA** (différenciation fractionnaire) et, plus récemment, la [volatilité rugueuse](../rough-volatility/) (qui modélise la trajectoire rugueuse de la volatilité par un mouvement brownien fractionnaire avec $$H<1/2$$). La contribution fondamentale de Mandelbrot est d'avoir fait admettre que la **rugosité, les queues lourdes et l'autosimilarité** des marchés sont la norme et non l'exception — une vision du monde des séries temporelles financières modernes qui perdure aujourd'hui.
