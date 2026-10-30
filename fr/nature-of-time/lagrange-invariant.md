---
updated: "2026-06-14"
layout: history
lang: fr
era: "La nature du temps 9 · Physique"
permalink: /fr/nature-of-time/lagrange-invariant/
title: "L'invariant de Lagrange : l'espace des phases ne se comprime pas"
lead: "Si les équations du mouvement ne laissent jamais « rétrécir » un nuage de conditions initiales, comment le temps pourrait-il avoir une direction ? Une loi de conservation cachée dans la mécanique hamiltonienne est la carte maîtresse physique de l'énigme de la « flèche du temps »."
math: true
prev: /nature-of-time/kant/
next: /nature-of-time/arrow-of-time/
---

> Ceci est l'un des volets de [la nature du temps](../). C'est la carte maîtresse mécanique de [la flèche du temps](../arrow-of-time/), et il mène aussi aux [Paradoxes du temps · le paradoxe de réversibilité de Loschmidt](../../paradoxes/loschmidt/).

### Un invariant né de la mécanique céleste

Au début du XIXe siècle, Lagrange, étudiant les perturbations des orbites planétaires, se heurte à un problème : l'attraction mutuelle des planètes fait lentement dériver les éléments orbitaux (demi-grand axe, excentricité…) ; comment les suivre ? Il écrit chaque état comme un ensemble de coordonnées canoniques $q_i$ (positions) et de moments conjugués $p_i$, et définit, pour des paramètres $u,v$, le **crochet de Lagrange** :

$$ [u,v] = \sum_i\left(\frac{\partial q_i}{\partial u}\frac{\partial p_i}{\partial v}-\frac{\partial p_i}{\partial u}\frac{\partial q_i}{\partial v}\right). $$

Il démontre un fait étonnant : lorsque le système évolue dans le temps selon les équations de la mécanique, la valeur de ces crochets **ne change pas du tout**. C'est le tout premier « invariant de Lagrange » — avec le crochet dual introduit plus tard par Poisson, il est devenu l'ossature de la mécanique canonique.

### Ce qu'il dit vraiment : la conservation de la structure symplectique

Imaginez un grand nombre de conditions initiales voisines comme un petit nuage de points dans l'espace des phases $(q,p)$. L'évolution du système est donnée par les **équations canoniques de Hamilton** :

$$ \dot q_i = \frac{\partial H}{\partial p_i},\qquad \dot p_i = -\frac{\partial H}{\partial q_i}. $$

Dire que le crochet de Lagrange est invariant revient à dire que la **2-forme symplectique** de l'espace des phases est transportée intacte par ce « flot du temps » ($\phi_t$ désignant le flot de phase à l'instant $t$) :

$$ \omega = \sum_i dp_i\wedge dq_i,\qquad \phi_t^{*}\,\omega=\omega. $$

Sa version intégrale est l'**invariant intégral** généralisé par Poincaré (années 1890) dans *Les Méthodes nouvelles de la mécanique céleste* : le long de toute courbe fermée $\gamma$ de l'espace des phases transportée par le flot,

$$ \oint_{\gamma}\sum_i p_i\,dq_i \;=\; \text{constante}. $$

Au cours de l'évolution, la courbe peut être étirée, tordue, enroulée jusqu'à devenir méconnaissable, mais cette intégrale de contour ne bouge pas d'un iota.

### Conséquence : le théorème de Liouville et l'« incompressibilité de l'espace des phases »

En élevant la 2-forme symplectique à la puissance $N$ ($\omega^N/N!$), on obtient exactement l'élément de volume de l'espace des phases $dq_1\cdots dq_N\,dp_1\cdots dp_N$. L'invariant donne donc immédiatement le **théorème de Liouville** : le volume dans l'espace des phases est conservé, et le flot hamiltonien se comporte comme un **fluide incompressible**, $\nabla\!\cdot(\dot q,\dot p)=0$. Un nuage de conditions initiales peut être brassé jusqu'à devenir ténu et filamenteux, mais son volume ne diminue ni n'augmente jamais.

L'énoncé paraît technique, mais il touche au cœur du problème : dans un système conservatif, **il n'y a ni attracteur, ni convergence par frottement**. Le nuage de points ne s'effondre pas en un point et ne se disperse pas jusqu'à disparaître — il ne fait que se **mélanger**.

### Quel rapport avec la direction du temps ?

C'est précisément la carte maîtresse physique de l'énigme de [la flèche du temps](../arrow-of-time/). Les lois microscopiques sont réversibles et le volume dans l'espace des phases est strictement conservé ; alors pourquoi l'entropie — $S=k_B\ln W$ — croîtrait-elle de façon monotone ? L'invariant de Lagrange impose la bonne réponse : **la croissance de l'entropie ne peut pas venir d'une compression de l'espace des phases** (il ne se comprime tout simplement pas) ; elle ne peut venir que du **mélange sous un regard à gros grain**, auquel s'ajoute la condition initiale très particulière, d'entropie extrêmement basse, de l'origine de l'univers. La direction n'est pas dans les équations, mais dans les conditions initiales.

La même loi de conservation nourrit directement deux objections célèbres :

- **La récurrence de Poincaré** : dans un espace des phases borné où le volume est conservé, presque tout état finit par revenir arbitrairement près de son point de départ — une tasse brisée pourrait en principe « se recoller toute seule », à condition d'attendre un temps qui dépasse de très loin l'âge de l'univers.
- **[Le paradoxe de réversibilité de Loschmidt](../../paradoxes/loschmidt/)** : si l'on inverse le signe de tous les moments, l'évolution se rembobine de façon parfaitement légitime, et l'entropie diminue. La tension entre réversible et irréversible prend sa source dans cet invariant.

### Pourquoi les séries temporelles lui doivent aussi quelque chose

Un fil plus discret mène au [prélude de l'histoire](../../history/foundations/). Si nous osons estimer la moyenne et l'autocorrélation d'un processus à partir d'**une seule** trajectoire observée, c'est grâce au **théorème ergodique** (Birkhoff, Kolmogorov) : la moyenne temporelle converge vers la moyenne d'ensemble

$$ \lim_{T\to\infty}\frac1T\sum_{t=1}^{T} f(X_t)=\mathbb E[f(X)]. $$

Or le théorème ergodique suppose l'existence d'une **mesure invariante** sous la dynamique. Pour un système hamiltonien, cette mesure invariante est précisément le volume de Liouville, c'est-à-dire l'incarnation de l'invariant de Lagrange. Autrement dit : chaque fois que nous prenons « la moyenne historique comme espérance » d'une série temporelle, nous empruntons en silence cette loi de conservation née il y a deux siècles des orbites planétaires. La direction du temps reste une énigme, mais si la statistique dans le temps est légitime, c'est justement grâce à cette **constance qui ne se laisse pas comprimer**.
