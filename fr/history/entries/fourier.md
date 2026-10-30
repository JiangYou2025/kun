---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1807 · Mathématiques"
permalink: /fr/history/e/fourier/
title: "La naissance du domaine fréquentiel (Fourier, 1807)"
lead: "Comment la température d'une barre de métal chauffée se dissipe-t-elle au fil du temps ? Pour résoudre l'équation de la chaleur, Fourier affirma que toute fonction peut se décomposer en une somme de sinusoïdes — une phrase jugée « impossible » par ses pairs, qui ouvrit tout le monde du domaine fréquentiel."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

Au début du XIXᵉ siècle, l'un des problèmes centraux de l'analyse était la **conduction de la chaleur**. En 1807, Joseph Fourier soumit à l'Académie des sciences un mémoire sur la diffusion de la chaleur dans les solides, où il s'agissait de résoudre ce que l'on appellerait plus tard l'**équation de la chaleur**. La difficulté : la distribution initiale de température pouvait être une fonction de forme arbitraire, alors que les outils dont disposaient les mathématiciens pour une résolution exacte ne valaient que pour des fonctions « simples » comme les sinus et cosinus. Fourier affirma hardiment que toute distribution initiale de ce genre pouvait s'écrire comme une superposition de sinusoïdes et de cosinusoïdes ; le problème entier se résolvait alors « onde par onde, puis par superposition ».

### Problème

Les sinusoïdes sont périodiques, lisses, et oscillent sans fin ; une courbe de température arbitraire peut au contraire présenter des angles, être définie par morceaux, n'avoir aucune périodicité. **Pourquoi la somme d'une infinité de sinusoïdes lisses pourrait-elle approcher une fonction arbitraire, anguleuse et non périodique ?** C'était alors si contre-intuitif que des rapporteurs comme Lagrange refusèrent d'y croire, et le mémoire fut un temps rejeté.

### Autres courants de l'époque (et leurs limites)

- **Séries entières / développement de Taylor** : écrire une fonction comme superposition de $$1,x,x^2,\dots$$. Excellent pour les fonctions analytiques, mais exigeant une régularité suffisante et fondamentalement « local », il traite mal, de façon naturelle, les phénomènes périodiques et les oscillations globales.
- **La querelle des cordes vibrantes de d'Alembert et Euler** : au XVIIIᵉ siècle, on débattait depuis des décennies de la question « une forme initiale arbitraire peut-elle être représentée par une série trigonométrique ? », et l'opinion dominante penchait pour le **non**, estimant que les séries trigonométriques ne pouvaient représenter que des fonctions « aux bonnes propriétés ». Ce jugement conservateur sous-estimait le pouvoir expressif du système trigonométrique.
- La racine commune de ces limites : faute d'un langage rigoureux pour la convergence et les espaces de fonctions, on substituait à la question « en quel sens y a-t-il égalité ? » celle de « peut-on écrire une formule ? », si bien qu'on ne pouvait ni affirmer ni réfuter.

### Méthode

L'idée centrale de Fourier : développer les fonctions **sur la base des sinusoïdes**. Pour une fonction de période $$2\pi$$, la série de Fourier s'écrit

$$ f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\big(a_n\cos nt + b_n\sin nt\big),\qquad a_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\cos nt\,dt,\;\; b_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\sin nt\,dt $$

Chaque coefficient $$a_n,b_n$$ mesure l'importance de la composante de fréquence $$n$$. Pour une fonction non périodique, la somme devient une intégrale et l'on obtient la **transformée de Fourier** :

$$ \hat f(\omega)=\int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt $$

$$\hat f(\omega)$$ donne l'amplitude complexe du signal à la fréquence $$\omega$$ ; $$|\hat f(\omega)|$$ est l'intensité de cette fréquence, tandis que la phase encode son décalage temporel. La propriété clé de la base sinusoïdale est l'**orthogonalité** : les différentes fréquences sont indépendantes les unes des autres, si bien que « trouver le contenu d'une fréquence donnée » se réduit, proprement, à une intégrale de produit scalaire.

### Résultats

L'équation de la chaleur fut entièrement résolue : chaque composante fréquentielle décroît indépendamment selon $$e^{-k\omega^2 t}$$, les hautes fréquences se dissipant vite et les basses persistant longtemps — l'image physique selon laquelle « les angles s'émoussent d'abord » se lit directement dans les mathématiques. Plus profondément, l'analyse de Fourier offrit des « lunettes fréquentielles » : on pouvait désormais demander à n'importe quel signal « de quelles fréquences es-tu composé ? ».

### Portée et perspectives

La transformée de Fourier relie « domaine temporel » et « domaine fréquentiel » comme deux images en miroir, et elle est devenue la langue maternelle de tout le traitement du signal, de l'analyse spectrale et des méthodes fréquentielles des séries temporelles. Elle mène directement au [spectre de puissance et au théorème de Wiener–Khinchin](../wiener-khinchin/) des processus stationnaires — autocovariance et spectre de puissance forment précisément une paire de Fourier ; elle sous-tend aussi le périodogramme, le filtrage, le théorème d'échantillonnage et la transformée de Fourier rapide (FFT). Deux siècles plus tard, du codage audio à la représentation spectrale des [processus de diffusion](../brownian-motion/), jusqu'à l'attention fréquentielle des modèles profonds, c'est toujours ce pas de Fourier qui est à l'œuvre : mesurer le monde avec des sinusoïdes.
