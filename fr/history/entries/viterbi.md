---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1967 · Contrôle / communications"
permalink: /fr/history/e/viterbi/
title: "L'algorithme de Viterbi (Viterbi, 1967)"
lead: "Parmi un nombre exponentiel de chemins possibles, comment trouver efficacement la séquence d'états cachés la plus probable ? Viterbi fournit un décodage optimal par programmation dynamique, qui tourne aujourd'hui encore au plus bas niveau des systèmes de communication et de parole."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1960, les communications numériques butent sur un problème : après codage et passage par un canal bruité, le récepteur n'observe qu'une sortie perturbée, à partir de laquelle il doit **remonter** à la séquence émise la plus probable. Les codes convolutifs sont alors de puissants codes correcteurs d'erreurs ; leur processus de codage peut être vu comme les transitions dans le temps d'une machine à états finis. Le **modèle de Markov caché (HMM)**, largement utilisé par la suite, partage la même structure : les états cachés évoluent selon une chaîne de Markov, et chaque état émet un symbole observable avec une certaine probabilité.

### Problème

Étant donné une suite d'observations, trouver la séquence d'états cachés la plus probable. Pour une longueur $$T$$ et $$M$$ états, il existe jusqu'à $$M^T$$ chemins d'états possibles — **l'énumération exhaustive est impossible**. Choisir gloutonnement le meilleur état à chaque instant fait en revanche manquer l'optimum global, à cause des contraintes de transition entre états. **Comment trouver le chemin globalement le plus probable sans énumérer un nombre exponentiel de chemins ?**

### Les autres courants de l'époque (et leurs limites)

- **Décodage du maximum a posteriori symbole par symbole** : on choisit indépendamment l'état le plus probable à chaque instant. Les contraintes de transition sont ignorées, et la séquence obtenue peut être globalement incohérente, voire illicite.
- **Recherche exhaustive** : optimale en théorie, mais sa complexité en $$M^T$$ la rend impraticable pour toute longueur réaliste.
- **Heuristiques comme le décodage séquentiel ou à rétroaction** : utilisables dans certains cas, mais sans garantie d'optimalité, avec des performances qui se dégradent quand le bruit augmente.

### Méthode

Viterbi exploite la structure markovienne du problème par **programmation dynamique**. On définit la probabilité du meilleur chemin partiel arrivant à l'instant $$t$$ dans l'état $$j$$ :

$$ \delta_t(j)=\max_{i}\;\delta_{t-1}(i)\,a_{ij}\,b_j(o_t) $$

où $$a_{ij}$$ est la probabilité de transition entre états et $$b_j(o_t)$$ la probabilité que l'état $$j$$ émette l'observation $$o_t$$. L'essence de cette récurrence : le préfixe du chemin globalement optimal menant à l'état $$j$$ est nécessairement lui aussi un chemin optimal menant à un certain prédécesseur $$i$$ — il suffit donc, à chaque instant, de conserver un seul meilleur chemin entrant pour chacun des $$M$$ états, et la complexité tombe de $$M^T$$ à

$$ O(T\,M^2) $$

On enregistre en parallèle le meilleur prédécesseur par un pointeur de retour $$\psi_t(j)=\arg\max_i\,\delta_{t-1}(i)\,a_{ij}$$ ; à la fin, on choisit $$\arg\max_j \delta_T(j)$$ et l'on remonte les pointeurs pour obtenir la séquence d'états globalement la plus probable. En pratique, on passe souvent au logarithme pour transformer les produits en sommes et éviter le dépassement de capacité inférieur.

### Résultats

L'algorithme de Viterbi est devenu la méthode standard de décodage au maximum de vraisemblance des codes convolutifs, et a profondément marqué la fiabilité des communications spatiales lointaines et des communications mobiles (GSM, CDMA). Dans le cadre des HMM, il est aussi l'outil standard pour « décoder la séquence d'états la plus probable » en reconnaissance de la parole, en étiquetage morpho-syntaxique et en analyse de séquences biologiques.

### Portée et perspectives

Pour la modélisation des séries temporelles, l'algorithme de Viterbi est l'une des pierres angulaires de l'inférence dans les **modèles de séquence à espace d'états / variables cachées** : lorsqu'on suppose que la série observable est pilotée par une chaîne d'états dynamiques cachés, il fournit une résolution efficace de la trajectoire d'états optimale. Il appartient, avec l'algorithme forward–backward et le [filtre de Kalman](../kalman/), à la famille de « l'inférence séquentielle sur des modèles dynamiques », et préfigure le vaste paradigme qui traitera ensuite l'alignement et le décodage de séquences par programmation dynamique. Plus d'un demi-siècle plus tard, il tourne toujours, imperturbable, au cœur des systèmes de communication et de traitement du langage.
