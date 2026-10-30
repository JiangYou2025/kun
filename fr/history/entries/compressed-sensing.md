---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2006 · Contrôle / communications"
permalink: /fr/history/e/compressed-sensing/
title: "L'acquisition comprimée (Donoho · Candès · Tao, 2006)"
lead: "Nyquist dit qu'il faut échantillonner assez densément — mais si le signal est parcimonieux par nature ? Avec bien moins de mesures aléatoires que ne l'exige Nyquist, suivies d'une minimisation ℓ1, on peut le reconstruire exactement."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [prologue · Origines interdisciplinaires](../../foundations/).

### Contexte

Pendant plus d'un demi-siècle, la règle d'or du traitement du signal a été le **théorème d'échantillonnage de Shannon–Nyquist** : pour reconstruire sans perte un signal de largeur de bande $$ B $$, la fréquence d'échantillonnage doit être au moins $$ 2B $$. Ce paradigme « échantillonner densément, puis compresser en jetant la plupart des coefficients » (comme JPEG) paraît pourtant gaspilleur : si l'on ne garde au final que quelques grands coefficients, pourquoi en acquérir autant ? En 2006, Donoho d'une part, Candès–Romberg–Tao de l'autre, publient presque simultanément des articles fondateurs montrant que, si un signal est **parcimonieux** dans une certaine base, on peut le reconstruire exactement avec **bien moins de mesures que Nyquist**. L'**acquisition comprimée** (*compressed sensing*) était née.

### Problème

De nombreux signaux naturels et artificiels (images, audio, échos radar, spectres de séries temporelles) n'ont, dans un domaine transformé adapté (Fourier, ondelettes), que peu de coefficients non nuls : ils sont **parcimonieux**. Peut-on fusionner « échantillonnage » et « compression » et **acquérir directement l'information compressée** ? Mathématiquement : étant donné une observation linéaire $$ y = \Phi x $$ avec un nombre de mesures $$ m \ll n $$, le système sous-déterminé a une infinité de solutions ; comment retrouver de façon unique le $$ x $$ parcimonieux ?

### Autres courants de l'époque (et leurs limites)

- **Échantillonnage classique de Nyquist** : infaillible, mais **n'exploite pas la parcimonie**, ce qui entraîne, pour les signaux parcimonieux, beaucoup d'échantillons redondants ensuite jetés.
- **Minimisation directe de $$ \ell_0 $$ (chercher la solution la plus parcimonieuse)** : correcte en théorie, mais c'est une optimisation combinatoire **NP-difficile**, incalculable.
- **Méthodes gloutonnes comme le matching pursuit** : rapides, mais sans garanties théoriques d'optimalité globale ni de reconstruction exacte, et sujettes aux sous-optima.

### Méthode

Supposons que le signal $$ x\in\mathbb{R}^n $$ soit $$ k $$-parcimonieux dans une certaine base (seulement $$ k $$ coefficients non nuls, $$ k\ll n $$). On l'échantillonne avec une **matrice de mesure aléatoire** $$ \Phi $$ de taille $$ m\times n $$ :

$$ y = \Phi x,\qquad m \ll n $$

Chercher directement la solution la plus parcimonieuse $$ \min \|x\|_0 $$ est infaisable ; la percée clé consiste à utiliser la **norme convexe $$ \ell_1 $$** comme relaxation — elle retrouve exactement la solution parcimonieuse et se ramène à une optimisation convexe résoluble efficacement (programmation linéaire / cône du second ordre) :

$$ \min_{x}\ \|x\|_1 \quad \text{s.t.}\quad \Phi x = y $$

Une condition suffisante de succès est que $$ \Phi $$ satisfasse la **propriété d'isométrie restreinte (Restricted Isometry Property, RIP)** : il existe un petit $$ \delta_k\in(0,1) $$ tel que, pour tout vecteur $$ k $$-parcimonieux,

$$ (1-\delta_k)\|x\|_2^2 \le \|\Phi x\|_2^2 \le (1+\delta_k)\|x\|_2^2 $$

c'est-à-dire que $$ \Phi $$ préserve approximativement la longueur des vecteurs parcimonieux et ne « replie » pas des signaux parcimonieux différents l'un sur l'autre. Les matrices aléatoires gaussiennes ou de Bernoulli satisfont la RIP avec une probabilité écrasante, pour un nombre de mesures de seulement $$ m = O\big(k\log(n/k)\big) $$, bien inférieur à $$ n $$.

### Résultats

L'acquisition comprimée a entraîné un changement de paradigme, « échanger du calcul contre de l'échantillonnage » : temps d'examen IRM fortement réduits, caméra à pixel unique, radars et réseaux d'antennes parcimonieux, détection spectrale sous-Nyquist, radio cognitive large bande ont vu le jour. En séries temporelles et en identification de systèmes, elle sous-tend l'**estimation spectrale parcimonieuse**, la reconstruction de signaux en présence de données manquantes, et l'identification de systèmes dynamiques « parcimonie + physique » (SINDy, par exemple, qui retrouve les équations d'évolution à partir des données par régression parcimonieuse, procède de la même idée).

### Portée et perspectives

La portée profonde de l'acquisition comprimée est d'avoir élevé au rang de principe général l'idée que **la parcimonie est un a priori exploitable par l'échantillonnage**, et d'avoir prouvé que la relaxation convexe $$ \ell_1 $$ atteint, sous RIP, l'objectif de $$ \ell_0 $$ — théorie et algorithmes s'y referment parfaitement. Elle partage le même noyau mathématique que la régression parcimonieuse des statisticiens ([LASSO](../../../foundations/regularization/)) et a profondément influencé la régularisation en statistique de grande dimension et en apprentissage automatique. En séries temporelles, de la compression spectrale à la reconstruction des données manquantes et à la découverte de systèmes dynamiques parcimonieux, partout où l'on a « peu de mesures et une structure parcimonieuse », on entend l'écho de cette percée de 2006.
