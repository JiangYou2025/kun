---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1994 · Physique"
permalink: /fr/history/e/dfa/
title: "Analyse des fluctuations redressées (Peng et al., 1994)"
lead: "Battements cardiaques, ADN, cours boursiers : tous recèlent une « mémoire à longue portée », que les tendances lentes viennent pourtant masquer. La solution de Peng : retirer d'abord la tendance segment par segment, puis mesurer comment les fluctuations croissent avec l'échelle."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

De nombreuses séries naturelles et physiologiques présentent des **corrélations à longue portée (long-range correlation)** : les fluctuations d'aujourd'hui restent statistiquement liées à celles d'un passé lointain, et la fonction d'autocorrélation décroît lentement selon une loi de puissance au lieu de s'annuler rapidement de façon exponentielle. Ce comportement « fractal » réapparaît sans cesse dans le rythme cardiaque, les séquences de bases de l'ADN, les débits des rivières ou les rendements financiers. L'outil classique de la physique statistique pour le caractériser est l'exposant de Hurst et l'analyse de l'étendue normalisée (R/S). Mais les données réelles portent presque toujours, en surimpression, des **tendances non stationnaires** à dérive lente (dérive de la ligne de base, forçages extérieurs), qui faussent gravement l'estimation des corrélations à longue portée.

### Problème

Estimer les corrélations à longue portée directement sur la série brute ne permet pas de distinguer les « véritables corrélations intrinsèques à longue portée » des « corrélations factices créées par une tendance non stationnaire extérieure » — la tendance fait paraître la série plus « mémorielle » qu'elle ne l'est. **Peut-on concevoir une mesure d'échelle robuste aux tendances non stationnaires, qui extraie proprement les corrélations intrinsèques en loi de puissance de la contamination par la tendance ?**

### Autres courants de l'époque (et leurs limites)

- **Analyse de l'étendue normalisée (R/S) (école de Hurst)** : méthode classique d'estimation de l'exposant de Hurst, mais très sensible aux tendances non stationnaires comme aux corrélations à courte portée, elle donne souvent des résultats biaisés, voire trompeurs.
- **Lois d'échelle du spectre de puissance (exposant spectral $$\beta$$)** : on estime l'échelle à partir de la loi de puissance $$S(f)\sim f^{-\beta}$$ dans les basses fréquences. Or les tendances injectent une grande quantité de puissance factice aux basses fréquences, contaminant précisément la bande la plus décisive.
- **Ajustement direct de l'autocorrélation** : sous corrélations à longue portée, l'autocorrélation décroît elle-même très lentement et son estimation a une forte variance ; dès qu'une tendance s'y superpose, elle devient presque inutilisable.

### Méthode

L'astuce de la DFA tient en trois temps : « intégrer, retirer la tendance par segment, puis mesurer les fluctuations ». Soit $$x_k$$ la série centrée ; on construit d'abord le profil cumulé (en voyant la série comme une marche aléatoire) :

$$ Y(i)=\sum_{k=1}^{i}\big(x_k-\bar{x}\big) $$

On découpe $$Y$$ en segments disjoints de longueur $$n$$ ; dans chacun, on ajuste la tendance locale $$Y_n(i)$$ par un polynôme (le plus simple étant une droite) et on la soustrait — c'est l'étape qui **élimine la tendance locale**. On calcule ensuite la fluctuation quadratique moyenne des résidus redressés :

$$ F(n)=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\big[\,Y(i)-Y_n(i)\,\big]^2} $$

On répète l'opération pour une série de longueurs de fenêtre $$n$$ ; s'il existe une loi d'échelle en puissance

$$ F(n)\sim n^{\alpha} $$

alors, en échelle log-log, $$\log F(n)$$ est une droite en fonction de $$\log n$$, dont la pente est l'exposant d'échelle $$\alpha$$. Son interprétation est intuitive : $$\alpha=0.5$$ signifie l'absence de corrélation à longue portée (type bruit blanc) ; $$0.5<\alpha<1$$, des corrélations positives persistantes à longue portée ; $$\alpha>1$$, des corrélations plus fortes, non stationnaires ; $$\alpha<0.5$$, un comportement antipersistant. Plus l'ordre du polynôme est élevé, plus les tendances d'ordre élevé peuvent être éliminées.

### Résultats

Parce qu'elle retranche la tendance segment par segment, la DFA est bien plus robuste que les méthodes R/S et spectrales face aux dérives non stationnaires superposées, et sépare de manière stable les corrélations intrinsèques à longue portée dans des données réelles affectées de tendances. Peng et ses collègues l'ont d'abord utilisée pour révéler des corrélations à longue portée dans les séquences d'ADN et la variabilité du rythme cardiaque ; elle a ensuite été largement employée pour les signaux physiologiques (distinguer rythmes cardiaques sains et pathologiques), le climat, la sismologie ou la volatilité financière, et a donné naissance à la **DFA multifractale (MF-DFA)**.

### Portée et perspectives

La DFA a transformé la notion de « fractalité / mémoire longue », jusque-là théorique, en un indicateur diagnostique fiable et calculable sur des séries réelles non stationnaires, devenant l'un des outils standards de l'analyse d'échelle des systèmes complexes. Elle incarne une philosophie importante des séries temporelles : **commencer par retirer la composante non stationnaire qu'est la tendance, puis examiner la structure d'échelle des fluctuations restantes** — dans la droite lignée des idées de différenciation, de filtrage et de décomposition. Elle nous rappelle aussi que toute mesure de la « mémoire » doit reposer sur un traitement honnête de la tendance.
