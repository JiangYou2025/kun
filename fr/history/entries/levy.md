---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1934 · Mathématiques"
permalink: /fr/history/e/levy/
title: "Sauts, queues lourdes et accroissements indépendants (Lévy, 1934)"
lead: "Le mouvement brownien est trop « sage » : accroissements gaussiens, trajectoires continues, variance finie. Or les krachs réels sont des sauts instantanés et des queues épaisses. Lévy a étendu la famille des processus aléatoires aux sauts et aux queues lourdes, annonçant le vrai visage de la finance."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1930, le [processus de Wiener (mouvement brownien)](../brownian-motion/) était déjà le modèle par excellence des processus aléatoires à temps continu, mais il repose sur trois hypothèses particulières très fortes : des accroissements gaussiens, des trajectoires continues et une variance finie. Vers 1934, Paul Lévy étudie systématiquement les processus aléatoires généraux **à accroissements indépendants et stationnaires** (appelés aujourd'hui **processus de Lévy**) et se demande : quels processus peuvent satisfaire cette structure minimale « accroissements indépendants + accroissements stationnaires » ? La réponse est bien plus riche que le seul mouvement brownien.

### Problème

L'hypothèse gaussienne du mouvement brownien découle du théorème central limite, lequel exige que les petits chocs que l'on additionne aient une variance finie. **Que se passe-t-il si un seul choc peut lui-même être très grand (queue lourde), ou si le processus peut sauter instantanément ? Quelle loi suivent alors les accroissements, et le processus peut-il encore avoir une bonne structure mathématique ?** Les effondrements boursiers, les sinistres d'assurance géants ou l'arrivée des appels téléphoniques présentent tous des sauts et des queues épaisses que le mouvement brownien ne peut pas produire.

### Les autres courants de l'époque (et leurs limites)

- **La centralité de la loi gaussienne** : on supposait que toute fluctuation aléatoire finit par devenir gaussienne. C'est vrai lorsque la variance est finie, mais cela **sous-estime systématiquement les événements extrêmes** — décrire les rendements financiers par une gaussienne rend presque impossible un krach « centennal ».
- **L'hypothèse de trajectoires continues** : on supposait que prix et signaux varient continûment. Mais de nombreux processus réels (défauts, séismes, ordres de bourse) procèdent par **sauts discrets**, que les modèles continus manquent par construction.
- Ces deux hypothèses commodes masquaient les **queues lourdes et les sauts** du monde réel ; il fallait une classe de processus plus générale pour les accueillir.

### Méthode

Un processus de Lévy $$\{X_t\}$$ est défini par trois axiomes : $$X_0=0$$ ; des accroissements **indépendants** et **stationnaires** ; la continuité stochastique. Toute son information est condensée dans la **formule de Lévy–Khintchine** pour la fonction caractéristique :

$$ \mathbb E\big[e^{i u X_t}\big]=\exp\!\Big\{ t\Big( i b u-\tfrac12 \sigma^2 u^2+\!\int_{\mathbb R}\big(e^{iux}-1-iux\mathbf 1_{|x|<1}\big)\,\nu(dx)\Big)\Big\} $$

Les trois termes correspondent respectivement à la **dérive** $$b$$, à la **diffusion brownienne** $$\sigma^2$$ et aux **sauts** décrits par la **mesure de Lévy** $$\nu$$ — $$\nu(dx)$$ indique avec quelle intensité surviennent les sauts de taille $$x$$. Le mouvement brownien n'est que le cas particulier $$\nu\equiv 0$$. Les **lois stables** y sont liées : lorsque les accroissements sont autosimilaires et peuvent avoir des queues lourdes, on obtient les lois stables, dont les queues décroissent en loi de puissance $$\sim |x|^{-\alpha-1}$$ (variance infinie pour $$\alpha<2$$) :

$$ \mathbb P(|X|>x)\sim C\,x^{-\alpha},\qquad 0<\alpha<2 $$

### Résultats

Lévy a libéré les processus aléatoires du cadre « gaussien + continu » pour en faire la famille complète « dérive + diffusion + sauts », offrant un langage précis pour décrire **les queues lourdes et les sauts**. Les lois stables fournissent une généralisation du théorème central limite au cas de variance infinie. À la même époque, ses travaux fondateurs avec Doob sur la théorie des **martingales** ont élevé l'intuition de [Bachelier](../bachelier/) — « la meilleure prévision est la valeur actuelle » — au rang de cadre rigoureux et général.

### Portée et perspectives

L'œuvre de Lévy marque une ligne de partage pour l'analyse stochastique moderne et la finance mathématique. En amont, elle se prolonge dans l'intégrale stochastique d'Itô et les modèles de diffusion à sauts (diffusion à sauts de Merton, Variance Gamma) ; en aval, elle a inspiré la modélisation des **queues lourdes et du regroupement de la volatilité** des rendements financiers — précisément les phénomènes observés par Mandelbrot et qui ont fini par donner naissance à ARCH/GARCH. Aujourd'hui, chaque fois que l'on parle de « risque de queue épaisse », de « sauts », de « lois stables » ou de « martingales », ou même lorsque des modèles génératifs profonds remplacent le bruit gaussien par un bruit de Lévy, on utilise encore la carte plus réaliste du monde aléatoire que Lévy a dessinée en 1934.
