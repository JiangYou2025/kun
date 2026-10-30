---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1989 · Mathématiques"
permalink: /fr/history/e/wavelet-mra/
title: "L'analyse multirésolution (Mallat, 1989)"
lead: "Fourier voit les fréquences mais pas les instants ; le fenêtrage, lui, fige la résolution. Avec un « microscope » à grossissement variable, Mallat donne aux basses fréquences un champ large et aux hautes fréquences un trait fin."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1980, les deux grands outils de l'analyse du signal ont chacun un défaut rédhibitoire. La [transformée de Fourier](../fourier/) décompose entièrement le signal en sinusoïdes globales : excellente résolution fréquentielle, mais perte totale de « l'instant où l'événement se produit ». La [transformée de Fourier à court terme (STFT) de Gabor](../gabor-stft/) ajoute une fenêtre glissante et obtient une vision conjointe temps-fréquence, mais une fois la fenêtre choisie, la résolution de tout le plan temps-fréquence est figée. Parallèlement, Morlet, Grossmann, Meyer, Daubechies et d'autres convergent, depuis la prospection sismique d'un côté et les mathématiques pures de l'autre, vers la construction d'une famille de bases d'ondelettes capables de « dilatation + translation ». Il manque un cadre unifié pour organiser ces constructions éparses, accompagné d'un algorithme rapide comparable à la FFT.

### Problème

La fenêtre fixe de la STFT engendre une contradiction de fond : un signal basse fréquence demande une longue fenêtre temporelle pour être bien vu, alors qu'un transitoire haute fréquence exige une fenêtre courte pour être localisé, et aucune longueur de fenêtre unique ne satisfait les deux. **Peut-on rendre la fenêtre d'analyse adaptative selon la fréquence — qu'elle s'élargisse automatiquement pour les basses fréquences et se rétrécisse pour les hautes ?** Plus encore, peut-on, à la manière d'une pyramide, organiser le signal en plusieurs niveaux de résolution « du grossier au fin », avec une récurrence rapide d'un niveau à l'autre ?

### Les autres courants de l'époque (et leurs limites)

- **Fourier fenêtré / transformée de Gabor** : la résolution temps-fréquence est verrouillée par une seule longueur de fenêtre, impossible de traiter à la fois les tendances de longue période et les transitoires brefs.
- **Codage d'images pyramidal (Burt–Adelson, 1983)** : l'ingénierie disposait déjà de représentations multi-échelles « du grossier au fin », mais sans fondement mathématique orthogonal permettant une reconstruction parfaite ; elles restaient redondantes, avec un choix d'échelles arbitraire.
- **Premières transformées en ondelettes continues** : théoriquement élégantes, mais fortement redondantes et coûteuses en calcul, sans base orthogonale discrète ni algorithme rapide, donc difficiles à mettre en pratique.

### Méthode

Mallat propose l'**analyse multirésolution (MRA)** : on construit une suite de sous-espaces d'approximation emboîtés $$\cdots\subset V_1\subset V_0\subset V_{-1}\subset\cdots$$, la différence entre deux échelles voisines étant comblée par un espace de détails d'ondelettes $$W_j$$, de sorte que $$V_{j-1}=V_j\oplus W_j$$. La fonction d'échelle $$\varphi$$ et l'ondelette $$\psi$$ vérifient la relation à deux échelles (de raffinement) :

$$ \varphi(t)=\sqrt{2}\sum_k h_k\,\varphi(2t-k),\qquad \psi(t)=\sqrt{2}\sum_k g_k\,\varphi(2t-k) $$

où $$h_k$$ est un filtre passe-bas et $$g_k$$ un filtre passe-haut. Le signal se développe à chaque échelle sous la forme

$$ f(t)=\sum_k a_{J,k}\,\varphi_{J,k}(t)+\sum_{j\le J}\sum_k d_{j,k}\,\psi_{j,k}(t),\qquad \psi_{j,k}(t)=2^{-j/2}\psi(2^{-j}t-k) $$

Les fonctions de base $$\psi_{j,k}$$ ajustent automatiquement leur largeur par l'échelle $$2^j$$ : une grande échelle correspond à une fenêtre temporelle large, aux basses fréquences et à une haute résolution fréquentielle ; une petite échelle à une fenêtre étroite, qui localise les transitoires haute fréquence — c'est exactement la « résolution adaptative ». La **transformée en ondelettes rapide (algorithme de Mallat)** qui l'accompagne ramène le tout à des convolutions sur les coefficients suivies d'une décimation d'un facteur deux, en récurrence niveau par niveau :

$$ a_{j+1,k}=\sum_n h_{n-2k}\,a_{j,n},\qquad d_{j+1,k}=\sum_n g_{n-2k}\,a_{j,n} $$

pour une complexité de seulement $$O(N)$$, inférieure même au $$O(N\log N)$$ de la FFT.

### Résultats

La MRA a unifié les ondelettes, jusque-là constructions éparses, en une « pyramide de bancs de filtres », théorie et algorithme d'un seul tenant : la base orthogonale garantit une reconstruction parfaite sans redondance, et la transformée rapide l'a fait se répandre rapidement en compression d'images, débruitage et détection de contours. Elle a directement donné naissance à des normes comme JPEG2000, et est devenue l'outil principal de l'analyse temps-fréquence des signaux non stationnaires.

### Portée et perspectives

La MRA a offert à l'analyse des séries temporelles un « microscope à focale variable » : tendances de longue période et anomalies brèves peuvent être extraites par niveaux dans un même cadre, ce qui convient particulièrement aux données **non stationnaires** comme la finance, la fréquence cardiaque ou les séismes. Son opposition à la STFT traduit au fond un changement de paradigme, de la « résolution fixe » à la « résolution adaptée à l'échelle ». Cette pensée multi-échelle, du grossier au fin, résonnera plus tard dans les architectures pyramidales de l'apprentissage profond et dans les réseaux de diffusion en ondelettes (*wavelet scattering*) — voir le monde par niveaux est depuis devenu une intuition universelle du traitement du signal.
