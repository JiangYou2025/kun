---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1951 · Physique"
permalink: /fr/history/e/hurst/
title: "Dépendance de longue portée et exposant de Hurst (Hurst, 1951)"
lead: "Quelle taille donner au réservoir du Nil ? Un hydrologue examine huit siècles de niveaux d'eau, découvre que la mémoire de la nature est bien plus longue que celle d'une marche aléatoire, et mesure un exposant anormal."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Harold Edwin Hurst a travaillé des décennies au service hydrologique égyptien, avec pour mission principale de dimensionner le réservoir d'Assouan. C'est un problème de stockage : pour que le réservoir ne déborde ni ne s'assèche au fil de l'alternance pluriannuelle des années humides et sèches, il faut savoir quelle est l'ampleur réelle des fluctuations à long terme des apports. Le Nil a laissé des relevés d'une longueur rare dans l'histoire humaine — les marques de niveau remontent à près de mille ans —, ce qui lui offrait un échantillon idéal pour tester les lois des fluctuations naturelles.

### Problème

Selon l'intuition probabiliste dominante de l'époque, si les débits annuels étaient à peu près indépendants et identiquement distribués, l'étendue de l'écart cumulé (niveau le plus haut moins niveau le plus bas) devrait croître avec la durée $$n$$ comme $$\sqrt{n}$$ — l'échelle standard de la marche aléatoire. Or, sur le Nil et sur de nombreuses séries géophysiques, Hurst mesure de façon répétée une croissance **nettement plus rapide que $$\sqrt{n}$$**. **Pourquoi les fluctuations naturelles « se souviennent-elles plus longtemps et vont-elles plus loin » qu'un processus purement aléatoire ?**

### Les autres courants de l'époque (et leurs limites)

- **Hypothèse d'indépendance (bruit blanc)** : simple et commode mathématiquement, mais elle donne une échelle en $$\sqrt{n}$$, sous-estime systématiquement l'étendue à long terme et conduit à des réservoirs sous-dimensionnés.
- **Mouvement brownien à la [Bachelier](../bachelier/)** : relève lui aussi du paradigme de la marche aléatoire avec $$H=\tfrac12$$ et ne peut pas décrire la persistance « années humides en série, années sèches en série ».
- **Autorégression à mémoire courte ([AR](../yule-ar/))** : la corrélation décroît exponentiellement avec le retard et la mémoire s'efface vite ; elle n'explique toujours pas une persistance lente qui s'étend sur des décennies.

### Méthode

Hurst propose l'**analyse de l'étendue normalisée (analyse R/S)**. On centre une série de longueur $$n$$, on la cumule, et l'on obtient l'étendue des écarts

$$ R(n) = \max_{1\le k\le n}\sum_{i=1}^{k}(x_i-\bar{x}) - \min_{1\le k\le n}\sum_{i=1}^{k}(x_i-\bar{x}) $$

que l'on rend sans dimension (« normalise ») par l'écart-type empirique $$S(n)$$. La loi empirique centrale de Hurst est

$$ \mathbb{E}\!\left[\frac{R(n)}{S(n)}\right] \sim c\, n^{H},\qquad n\to\infty $$

L'exposant $$H$$ est l'**exposant de Hurst**. $$H=\tfrac12$$ correspond à une marche aléatoire sans mémoire ; $$H>\tfrac12$$ indique une **persistance** — les écarts tendent à se prolonger, avec une corrélation positive de longue portée ; $$H<\tfrac12$$ correspond à un retour à la moyenne antipersistant. La pente ajustée en coordonnées log-log donne $$H$$. Le Nil et de nombreuses autres séries donnent $$H\approx 0.7$$, nettement supérieur à $$\tfrac12$$.

### Résultats

Cette découverte a directement modifié les critères de dimensionnement des réservoirs, et elle a été confirmée à maintes reprises comme un phénomène général en géophysique, en climatologie et en hydrologie. Elle a appris aux ingénieurs que les fluctuations à long terme sont bien plus violentes que ne le prédit l'hypothèse d'indépendance, et que la planification doit laisser une marge suffisante à la « persistance ».

### Portée et perspectives

La **dépendance de longue portée** révélée par $$H>\tfrac12$$ est devenue le point de départ empirique de la géométrie fractale de Mandelbrot et du **mouvement brownien fractionnaire**, et elle mène aux modèles **ARFIMA à différenciation fractionnaire** — qui décrivent par une différence d'ordre fractionnaire des autocorrélations à décroissance très lente. De la mémoire longue de la volatilité financière à l'autosimilarité du trafic réseau, jusqu'à l'intérêt actuel pour les « dépendances à long contexte », cet exposant anormal mesuré par Hurst au bord du Nil nous rappelle encore que la mémoire de bien des séries réelles est beaucoup plus longue que celle d'une marche aléatoire.
