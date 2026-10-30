---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1945 · Mathématiques"
permalink: /fr/history/e/wald-sprt/
title: "Le test qui décide au fil des observations (Wald, 1945)"
lead: "Inutile de fixer la taille de l'échantillon à l'avance : à chaque nouvelle donnée, on cumule les preuves, et l'on ne conclut qu'au franchissement d'un seuil haut ou bas. L'analyse séquentielle économise des observations et plante la graine de la détection de ruptures."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Pendant la Seconde Guerre mondiale, le contrôle qualité de l'industrie d'armement subit une contrainte très concrète : les tests sur échantillon sont souvent destructifs, et moins on en consomme, mieux c'est. Le test classique de Neyman–Pearson exige de **fixer à l'avance la taille d'échantillon $$n$$**, puis de décider en une seule fois. Dans le cadre de ses travaux au sein du groupe de recherche statistique de guerre, Abraham Wald propose un paradigme radicalement différent — l'**analyse séquentielle** : la taille de l'échantillon devient elle-même une variable aléatoire, et l'on décide au fur et à mesure de l'arrivée des données. Le test séquentiel du rapport de probabilités (SPRT), publié en 1945, est la cristallisation de cette idée.

### Problème

Il s'agit de choisir entre deux hypothèses simples $$H_0:\theta=\theta_0$$ et $$H_1:\theta=\theta_1$$, en contrôlant les probabilités des deux types d'erreur à $$\alpha,\beta$$. **Peut-on, au lieu de fixer la taille de l'échantillon au préalable, décider à chaque nouvelle observation « accepter, rejeter, ou en regarder encore une », de façon à atteindre le même contrôle des erreurs avec le moins d'observations possible ?**

### Les autres courants de l'époque (et leurs limites)

- **Test de Neyman–Pearson à taille fixe** : théorie élégante et taux d'erreur maîtrisés, mais la taille de l'échantillon est fixée uniformément pour le pire cas ; en moyenne, on gaspille beaucoup d'observations, ce qui coûte très cher pour des tests destructifs.
- **Arrêt anticipé empirique** : l'inspecteur regarde les données et « s'arrête quand ça suffit ». Cela modifie subrepticement le taux d'erreur effectif (problème des observations multiples), fausse le $$\alpha$$ nominal et n'offre aucune garantie théorique.
- **Mise à jour bayésienne pure de la loi a posteriori** : mettre à jour continûment la loi a posteriori va dans le bon sens, mais il manquait à l'époque une règle opérationnelle reliant « quand s'arrêter, et quelle conclusion tirer » au contrôle fréquentiste des erreurs.

### Méthode

Le SPRT cumule pas à pas le **logarithme du rapport de vraisemblance**. Pour des observations indépendantes $$x_1,x_2,\dots$$, on définit la statistique cumulée

$$ \Lambda_n=\sum_{i=1}^{n}\log\frac{f_{\theta_1}(x_i)}{f_{\theta_0}(x_i)} $$

On fixe deux seuils $$A=\log\dfrac{1-\beta}{\alpha},\quad B=\log\dfrac{\beta}{1-\alpha}$$ (de sorte que $$B<0<A$$). La règle d'arrêt est :

$$ \text{si }\Lambda_n\ge A\Rightarrow\text{accepter }H_1;\quad \Lambda_n\le B\Rightarrow\text{accepter }H_0;\quad B<\Lambda_n<A\Rightarrow\text{prendre une observation de plus} $$

C'est un problème de **temps d'arrêt optimal** : le théorème de Wald–Wolfowitz montre que, pour $$\alpha,\beta$$ donnés, le SPRT **minimise simultanément la taille d'échantillon espérée** sous les deux hypothèses. $$\Lambda_n$$ est une marche aléatoire, les seuils sont des barrières absorbantes, et le nombre moyen de pas nécessaires s'estime par l'identité de Wald.

### Résultats

À contrôle des erreurs égal, le test séquentiel **économise souvent environ la moitié** de la taille d'échantillon moyenne par rapport au test à taille fixe. Plus important encore, il introduit en statistique le paradigme dynamique « les preuves s'accumulent dans le temps, et l'on n'agit qu'au franchissement d'un seuil ». Le cumul du logarithme du rapport de vraisemblance est précisément le cœur de la future **carte de contrôle à somme cumulée (CUSUM)** : lire en temps réel, dans le flux de données, si « un changement s'est produit ».

### Portée et perspectives

Le logarithme du rapport de vraisemblance cumulé de Wald, assorti de seuils, est la source de la **détection de ruptures** et de la surveillance en ligne. Si l'on laisse $$\Lambda_n$$ cheminer sous l'hypothèse « le processus est toujours normal » et qu'on déclenche une alarme dès qu'il franchit la limite, on obtient le CUSUM de Page (1954) et l'ébauche de la détection d'anomalies en flux moderne. Du contrôle qualité industriel aux ruptures structurelles des marchés financiers, de la détection d'intrusions réseau à la surveillance en temps réel des séries temporelles, l'idée de « cumuler les preuves au fil des observations et décider de façon optimale du moment de s'arrêter » remonte tout entière à ce pas franchi par Wald en 1945.
