---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1906 · Mathématiques"
permalink: /fr/history/e/markov/
title: "La chaîne sans mémoire (Markov, 1906)"
lead: "La loi des grands nombres exige-t-elle nécessairement l'« indépendance » ? Avec une chaîne qui ne se souvient que du présent et oublie le passé, Markov démontre que non : il suffit que l'avenir ne dépende que de l'instant présent — les processus aléatoires ont dès lors un squelette."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

À la fin du XIXe siècle, les grands résultats de la théorie des probabilités (loi des grands nombres, théorème central limite) reposaient presque tous sur l'hypothèse d'**indépendance**. La controverse entre Andreï Markov et Nekrassov portait précisément sur ce point : Nekrassov laissait entendre que la loi des grands nombres exigeait l'indépendance. Markov, en désaccord, résolut de construire une classe de variables aléatoires **dépendantes mais obéissant tout de même aux lois limites**. À partir de 1906, il proposa et étudia les « chaînes » qui porteraient plus tard son nom, et en donna une célèbre illustration empirique avec la succession des voyelles et des consonnes dans le roman en vers de Pouchkine, *Eugène Onéguine*.

### Problème

Les séquences réelles sont presque partout dépendantes : le temps d'aujourd'hui influence celui de demain, une lettre influence la suivante. **Si les variables ne sont pas indépendantes, les théorèmes limites des probabilités tiennent-ils encore ? Jusqu'à quel degré la dépendance reste-t-elle « maîtrisable » ?** Une dépendance totalement arbitraire est impossible à analyser, et l'indépendance complète est déconnectée du réel — il fallait un juste milieu à la fois réaliste et soluble.

### Les autres courants de l'époque (et leurs limites)

- **Le paradigme indépendant et identiquement distribué** : prémisse dominante des théorèmes limites de l'époque. Mathématiquement élégant, il exclut pourtant le phénomène universel de « l'influence du passé sur le présent » et ne peut décrire des séquences réelles comme la météo, la langue ou la démographie.
- **La dépendance totale / le déterminisme** : l'autre extrême, selon lequel le système est entièrement déterminé par ses conditions initiales. Sans aucune place pour le hasard, il ne peut expliquer les fluctuations observées et rend les outils probabilistes inutiles.
- Ce qui manquait, c'était une **dépendance structurée** : conserver le hasard tout en restreignant la dépendance à une forme récursive et calculable.

### Méthode

L'idée centrale de Markov est la **propriété de Markov (absence de mémoire)** : sachant le présent, l'avenir est conditionnellement indépendant du passé. Pour une suite d'états $$\{X_t\}$$,

$$ \mathbb P(X_{t+1}=j \mid X_t=i,\,X_{t-1},\dots,X_0)=\mathbb P(X_{t+1}=j\mid X_t=i)=p_{ij} $$

Toute la chaîne est déterminée par la **matrice de transition** $$P=(p_{ij})$$. Les transitions en plusieurs étapes satisfont l'**équation de Chapman–Kolmogorov** :

$$ p_{ij}^{(m+n)}=\sum_{k} p_{ik}^{(m)}\,p_{kj}^{(n)} $$

Autrement dit, aller de $$i$$ à $$j$$ en $$m+n$$ étapes revient à sommer, sur tous les états intermédiaires $$k$$, la probabilité de faire « d'abord $$m$$ étapes, puis $$n$$ étapes » — l'évolution à long terme se décompose en étapes courtes qui se multiplient. Sous des conditions appropriées (irréductibilité, apériodicité), la chaîne converge vers une unique **loi stationnaire** $$\pi$$, qui vérifie $$\pi P=\pi$$.

### Résultats

Markov a démontré que même pour des variables dépendantes, la loi des grands nombres reste valable dès lors que cette structure de chaîne est respectée — une réponse directe à la controverse avec Nekrassov. Plus important encore, il a fourni la première classe de processus aléatoires **à la fois analysables et proches de la réalité** : la dépendance est condensée dans une transition d'un pas, le comportement à long terme est décrit par la loi stationnaire, et l'analyse devient praticable.

### Portée et perspectives

La propriété de Markov est devenue le squelette commun de toute la théorie des processus aléatoires. L'[autorégression AR](../yule-ar/) en est le cas particulier linéaire gaussien à états continus ; les modèles de Markov cachés (HMM) lui superposent une couche d'observation ; les processus de décision markoviens (MDP) sont le socle de l'apprentissage par renforcement ; et les méthodes MCMC, à l'inverse, « conçoivent » une chaîne dont la loi stationnaire est la loi cible afin d'échantillonner. La version à temps continu a été systématisée par les équations progressive et rétrograde de [Kolmogorov](../kolmogorov/), dont le [mouvement brownien](../brownian-motion/) et le [processus d'OU](../ornstein-uhlenbeck/) sont des membres. Aujourd'hui, lorsque les grands modèles de langage « prédisent le prochain token à partir du contexte courant », il s'agit au fond, eux aussi, d'une chaîne de Markov à mémoire allongée.
