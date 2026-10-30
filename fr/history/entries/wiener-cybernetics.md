---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1948 · Contrôle / communications"
permalink: /fr/history/e/wiener-cybernetics/
title: "Rétroaction, prédiction et filtrage optimal (Wiener, 1948)"
lead: "De la conduite de tir antiaérienne à *Cybernetics*, Wiener a fait de « prédire l'avenir à partir d'un passé bruité » une équation de filtrage optimal soluble dans le domaine fréquentiel, et a érigé la rétroaction en langage commun aux machines et au vivant."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Pendant la Seconde Guerre mondiale, Norbert Wiener étudie la manière dont un canon antiaérien peut viser un avion en manœuvre : la position de l'avion mesurée par le radar est bruitée, et l'obus a un temps de vol ; il faut donc **prédire la position future de l'avion**. Cela réduit « observation bruitée + prédiction » à un problème mathématique. Après la guerre, dans *Cybernetics: or Control and Communication in the Animal and the Machine* (1948), il élève ces idées au rang de programme interdisciplinaire — d'où le mot « cybernétique » ; leur noyau technique est le **filtre optimal de Wiener**.

### Problème

L'observation $$y(t)=s(t)+n(t)$$ est la somme du signal vrai et d'un bruit. Il s'agit de concevoir un filtre $$h$$ **linéaire, n'utilisant que le passé et le présent (causal)**, qui estime à partir de $$y$$ une cible $$d(t)$$ (pour le débruitage $$d=s$$, pour la prédiction $$d(t)=s(t+\lambda)$$), en minimisant l'erreur quadratique moyenne. **Sous la contrainte de causalité, quelle est la réponse en fréquence du filtre optimal ?**

### Les autres courants de l'époque (et leurs limites)

- **Filtres passe-bas / de lissage empiriques** : on fixe intuitivement une fréquence de coupure pour atténuer le bruit. Cela fonctionne, mais sans tenir compte des spectres réels du signal et du bruit, sans optimalité, et avec une faible capacité de prédiction.
- **Déconvolution fréquentielle sans contrainte** : si l'on s'autorise toutes les données futures, le filtre optimal est un simple rapport de spectres $$S_{sy}/S_{yy}$$. Mais il est **non causal** et ne peut être réalisé en temps réel — la vraie difficulté est précisément de le « rendre causal ».
- **Extrapolation de trajectoires déterministes** : on extrapole la trajectoire de l'avion comme une fonction déterministe. Face aux manœuvres et au bruit de mesure, ce n'est ni robuste ni optimal, et cela ignore la structure spectrale aléatoire du signal.

### Méthode

On suppose le signal et le bruit stationnaires, de spectres connus. Le filtre **causal** optimal est déterminé par l'**équation de Wiener–Hopf**, dont la clé de résolution est la **factorisation spectrale** : on écrit le spectre de l'observation sous la forme $$S_{yy}(\omega)=\lvert\Phi^{+}(\omega)\rvert^2$$, où $$\Phi^{+}$$ et son inverse sont tous deux causaux (à phase minimale). Pour le débruitage pur, la réponse en fréquence du filtre optimal est

$$ H(\omega)=\frac{1}{\Phi^{+}(\omega)}\left[\frac{S_{sy}(\omega)}{\overline{\Phi^{+}(\omega)}}\right]_{+} $$

où $$[\,\cdot\,]_{+}$$ signifie **prendre la partie causale** (en rejetant la réponse impulsionnelle aux temps négatifs). Intuitivement : on « blanchit » d'abord l'observation par $$1/\Phi^{+}$$ pour en faire une innovation de bruit blanc, on effectue ensuite la projection optimale sur cette innovation, et l'on ne conserve enfin que la partie causale, physiquement réalisable. Sans contrainte de causalité, la formule se réduit à $$H=S_{sy}/S_{yy}$$ : on voit que $$[\cdot]_+$$ est exactement le prix de la causalité. C'est l'incarnation fréquentielle de la même idée que la projection orthogonale de la [prédiction de Wiener–Kolmogorov](../wiener-kolmogorov-prediction/).

### Résultats

Le filtre de Wiener fournit une solution optimale au sens quadratique moyen, et réalisable, au problème « signal + bruit », avec en prime le spectre de l'erreur. Il fait entrer la prédiction pour la conduite de tir, le débruitage en communications et le pistage radar dans un cadre unique, et fait de la boucle « rétroaction — prédiction — correction » un objet d'ingénierie que l'on peut concevoir et analyser. *Cybernetics* va plus loin en élevant la rétroaction au rang de principe universel traversant machines et organismes vivants, avec une influence qui s'étend jusqu'aux neurosciences et à l'économie.

### Portée et perspectives

Le filtrage de Wiener est un jalon de la théorie de l'estimation optimale dans le domaine fréquentiel, mais il dépend de la **stationnarité, de spectres connus, et exige une factorisation spectrale** ; il est assez lourd pour traiter des systèmes non stationnaires ou une récurrence en temps réel. En 1960, [Kalman](../kalman/) transpose la même idée de projection optimale dans l'**espace d'états, en temps**, obtenant le filtre de Kalman, récursif pas à pas et adapté au non-stationnaire — souvent considéré comme une généralisation récursive du filtre de Wiener. Du GPS au guidage et au débruitage des signaux, toute la lignée actuelle du filtrage optimal prend racine ici, chez Wiener, en 1948.
