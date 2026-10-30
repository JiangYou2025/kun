---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1965 · Informatique"
permalink: /fr/history/e/fft/
title: "La transformée de Fourier rapide (Cooley · Tukey, 1965)"
lead: "Faire passer la transformée de Fourier discrète de O(N²) à O(N log N) : un algorithme « diviser pour régner » a rendu l'analyse spectrale à grande échelle quotidienne sur ordinateur — et a discrètement transformé d'innombrables disciplines."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

L'idée de l'analyse de Fourier est ancienne : toute série peut se décomposer en une superposition de sinusoïdes de fréquences différentes, et la **transformée de Fourier discrète (TFD)** associe à une série de $$N$$ points $$N$$ composantes fréquentielles ; c'est l'outil central de l'analyse spectrale. Dans les années 1960, alors que les ordinateurs numériques commençaient à se répandre, on aspirait à les utiliser pour analyser la structure fréquentielle des séries sismiques, radar, de télécommunications et économiques.

### Problème

Calculer la TFD directement à partir de sa définition exige de multiplier chaque sortie par chaque entrée et de sommer, soit une complexité en $$O(N^2)$$. Lorsque $$N$$ atteint quelques dizaines de milliers, il faut des centaines de millions de multiplications, et les machines de l'époque y auraient passé une éternité. **En théorie, tout le monde savait faire de l'analyse spectrale ; en pratique, le coût de calcul la bloquait.** L'analyse fréquentielle à grande échelle était quasiment impossible.

### Autres courants de l'époque (et leurs limites)

- **Méthodes temporelles (autocorrélation, ajustement AR)** : elles évitent le calcul explicite du spectre, mais il faut tout de même une transformation pour voir clairement la structure fréquentielle, et elles sont peu parlantes pour les signaux à large bande.
- **Bancs de filtres analogiques** : on sépare les bandes de fréquences par des circuits matériels ; peu flexibles, de précision limitée, impossibles à ajuster librement en résolution.
- **Calcul direct de la TFD** : mathématiquement correct, mais le coût en $$O(N^2)$$ le rend impraticable pour de grands $$N$$ — c'est précisément le goulot d'étranglement à briser.

### Méthode

La TFD est définie par (en notant $$W_N=e^{-i2\pi/N}$$) :

$$ X_k=\sum_{n=0}^{N-1} x_n\, W_N^{\,nk},\qquad k=0,\dots,N-1 $$

L'idée clé de Cooley–Tukey est de **diviser pour régner** : lorsque $$N$$ est pair, on sépare la somme en deux moitiés selon la parité des indices,

$$ X_k=\underbrace{\sum_{m} x_{2m} W_{N/2}^{\,mk}}_{E_k}\;+\;W_N^{\,k}\underbrace{\sum_{m} x_{2m+1} W_{N/2}^{\,mk}}_{O_k} $$

autrement dit, une TFD à $$N$$ points se ramène à deux TFD à $$N/2$$ points, que l'on recombine par une opération « **papillon** » : $$X_k=E_k+W_N^k O_k$$ et $$X_{k+N/2}=E_k-W_N^k O_k$$ (en utilisant $$W_N^{k+N/2}=-W_N^k$$). En poursuivant récursivement la décomposition, la complexité totale, solution de la récurrence $$T(N)=2T(N/2)+O(N)$$, vaut

$$ T(N)=O(N\log N) $$

Pour $$N=2^{20}$$, c'est environ cinquante mille fois plus rapide que $$O(N^2)$$.

### Résultats

L'analyse spectrale de longues séries devint dès lors instantanée sur un ordinateur ordinaire. La FFT s'imposa rapidement comme l'un des algorithmes les plus utilisés en traitement du signal, télécommunications, imagerie ou géophysique, et elle est saluée comme l'un des algorithmes les plus importants du XXᵉ siècle. Convolution rapide, filtrage et calcul de corrélations lui doivent également des accélérations de plusieurs ordres de grandeur.

### Portée et perspectives

Pour les séries temporelles, la FFT a rendu véritablement praticables le **périodogramme** et l'estimation du spectre de puissance, faisant du domaine fréquentiel un paradigme d'analyse à égalité avec le domaine temporel, et offrant un outil efficace pour étudier la mise en forme par filtrage à la Slutsky. Sur le plan numérique, elle soutient aussi la convolution rapide, accélérant ainsi le calcul des modèles [ARMA/ARIMA](../box-jenkins/) et le traitement des longues séries. Une astuce algorithmique en apparence purement technique a fini par refaçonner la manière dont on « regarde » les signaux — la fréquence n'est plus coûteuse.
