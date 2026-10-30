---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1946 · Contrôle / communications"
permalink: /fr/history/e/gabor-stft/
title: "Horodater les fréquences (Gabor, 1946)"
lead: "Fourier vous dit quelles fréquences contient un signal, mais pas quand elles apparaissent ; avec une fenêtre glissante, Gabor donne pour la première fois une coordonnée temporelle au spectre — au prix d'un compromis d'incertitude."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

L'[analyse de Fourier](../fourier/) est la pierre angulaire du traitement du signal : tout signal peut se décomposer en une superposition de sinusoïdes de fréquences différentes. Mais la transformée de Fourier est **globale** — elle comprime tout le signal en un seul spectre, qui dit « quelles fréquences sont présentes » mais efface « à quel moment elles apparaissent ». Pour des signaux dont la fréquence évolue dans le temps, comme la parole, la musique ou les échos radar, c'est une lacune fatale. En 1946, Dennis Gabor propose dans « Theory of Communication » une représentation spectrale dotée d'une résolution temporelle.

### Problème

Un morceau de musique joue d'abord des notes graves, puis des aiguës : le spectre de Fourier montre à la fois les basses et les hautes fréquences, sans révéler leur ordre. **Comment obtenir une représentation conjointe qui porte l'information fréquentielle tout en conservant la localisation temporelle ?** Et peut-on rendre les résolutions en temps et en fréquence arbitrairement fines en même temps, ou existe-t-il une limite fondamentale ?

### Les autres courants de l'époque (et leurs limites)

- **Transformée de Fourier globale** : excellente résolution fréquentielle, résolution temporelle nulle. Adaptée aux signaux stationnaires, impuissante face aux signaux non stationnaires dont la fréquence dérive dans le temps.
- **Observation de la forme d'onde dans le domaine temporel** : on regarde directement les oscillations du signal ; la localisation temporelle est claire, mais on ne lit pas les composantes fréquentielles. Chacun des deux extrêmes ne tient qu'un bout.
- **Découpage brutal puis Fourier par segment** : on coupe le signal en tronçons sans recouvrement et on transforme chacun. La direction est bonne, mais la troncature rectangulaire introduit aux bords une forte fuite spectrale (oscillations de Gibbs), et la longueur des segments ne repose sur aucune théorie.

### Méthode

L'idée de Gabor est de multiplier le signal par une **fonction fenêtre** glissante $$g$$, puis de faire la transformée de Fourier du segment fenêtré : c'est la **transformée de Fourier à court terme (STFT)** :

$$ X(\tau,\omega)=\int_{-\infty}^{\infty} x(t)\,g(t-\tau)\,e^{-i\omega t}\,dt $$

Le centre de la fenêtre $$\tau$$ fournit la coordonnée **temporelle**, $$\omega$$ la coordonnée **fréquentielle** : le spectre reçoit ainsi un horodatage ; $$\lvert X(\tau,\omega)\rvert^2$$ est le spectrogramme. Gabor préconise en particulier la **fenêtre gaussienne**, car elle atteint la borne inférieure de l'incertitude conjointe temps-fréquence — ce qui correspond à la limite de Gabor, ou principe d'incertitude :

$$ \Delta t\,\cdot\,\Delta \omega \ \ge\ \tfrac12 $$

où $$\Delta t,\Delta\omega$$ sont les étalements (écarts-types) du signal en temps et en fréquence. Il en découle que **résolution temporelle et résolution fréquentielle ne peuvent être obtenues simultanément** : une fenêtre étroite donne un temps précis et une fréquence floue ; une fenêtre large, l'inverse. Une fois la fenêtre choisie, la résolution de toute la carte temps-fréquence est verrouillée par ce compromis.

### Résultats

La STFT rend possible l'analyse des signaux non stationnaires : le déplacement des formants de la parole dans le temps, les variations Doppler d'une cible radar, les fréquences de défaut d'une vibration mécanique deviennent « visibles » sur le spectrogramme. La concentration temps-fréquence optimale de la fenêtre gaussienne fait de la représentation de Gabor le point de départ standard de l'analyse temps-fréquence conjointe.

### Portée et perspectives

Gabor a fait de la « fréquence » une notion locale plutôt que globale, ouvrant tout le domaine de l'**analyse temps-fréquence**. Le compromis de résolution imposé par une fenêtre fixe est précisément ce que la **transformée en ondelettes** cherchera à dépasser — les ondelettes utilisent une fenêtre dont l'échelle s'adapte à la fréquence (fenêtres courtes pour les hautes fréquences, longues pour les basses) afin de réaliser une analyse multirésolution. Des spectrogrammes au spectre Mel jusqu'aux caractéristiques d'entrée des modèles profonds de parole et d'audio, la première étape pour traiter un « signal dont la fréquence change » reste bien souvent, aujourd'hui encore, la fenêtre glissante de Gabor.
