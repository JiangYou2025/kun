---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 8 · Télécommunications et signal"
permalink: /fr/applications/signal/
title: "Télécommunications et traitement du signal"
lead: "Le traitement du signal est le berceau technique des séries temporelles : bien avant la vogue de l'apprentissage automatique, les ingénieurs utilisaient filtres et prédiction linéaire pour suivre les signaux dans le bruit en temps réel, compresser les données et décoder les symboles."
math: false
prev: /applications/industry/
next: /applications/geophysics/
---

> Ceci est le scénario 8 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : parole et audio, réponses de canaux sans fil, échos radar et sonar, signaux bioélectriques.
- **Tâches** : codage et reconnaissance de la parole, égalisation et prédiction de canal, annulation d'écho et réduction de bruit, pistage de cibles radar, reconnaissance de modulation.

## Ce qui rend ce domaine particulier

- **Fréquence d'échantillonnage élevée, temps réel strict** : de dizaines de milliers à des millions d'échantillons par seconde ; le traitement doit se faire en ligne, avec une faible latence.
- **Des fondements physiques et linéaires solides** : des décennies de théorie des filtres, très mûre et fiable.
- **Bruit et trajets multiples** : les signaux sont souvent fortement pollués par le bruit et les réflexions.

## Méthodes courantes

- Filtrage adaptatif classique : filtre de Wiener, LMS, RLS ; **codage par prédiction linéaire (LPC)** pour la parole.
- **Filtre de Kalman** pour le pistage de cibles et l'estimation d'état (histoire [4](../../history/04/), [prologue](../../history/foundations/)).
- **Algorithme de Viterbi** pour le décodage optimal des HMM et des codes convolutifs ([prologue](../../history/foundations/)).
- Ces dernières années, apprentissage profond de bout en bout pour la parole et le signal (cours [9](../../course/09/), [10](../../course/10/)).

## Un cas emblématique : le codage par prédiction linéaire (LPC)

On modélise un court segment de parole comme un **processus AR** — on prédit linéairement l'échantillon courant à partir des quelques précédents, et l'on ne transmet que le résidu et les coefficients. C'est l'application technique classique du modèle AR (cours [8](../../course/08/)), qui a porté pendant des décennies la compression et la synthèse de la parole ainsi que les communications mobiles. Sous un autre nom, c'est exactement ce que les statisticiens appellent l'autorégression.

---

**Termes clés (Key terms)** : filtrage adaptatif, LPC, pistage de Kalman, Viterbi, égalisation de canal, processus AR.
