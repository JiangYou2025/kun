---
updated: "2026-06-11"
layout: history
lang: fr
era: "Récit de la préhistoire 12 · Méthode · Calcul"
permalink: /fr/prehistory/kelvin-tides/
title: "La machine à prédire les marées de Kelvin (Kelvin's Tide Machine)"
lead: "La marée d'un port est la superposition de dizaines de cycles astronomiques. Prédire le niveau de l'eau heure par heure pour toute l'année suivante prendrait une éternité à la main. Kelvin construisit une machine en laiton pour « additionner les sinusoïdes » à la place des hommes."
math: false
prev: /prehistory/jevons-sunspots/
next: /prehistory/sunspot-cycle/
---

> Ceci est l'un des récits de la [préhistoire et des applications contemporaines](../).

### La marée, une superposition de cycles

La marée semble n'être qu'une montée et une descente, mais derrière elle joue tout un orchestre de cycles astronomiques : lunaires, solaires, semi-diurnes, diurnes, semi-mensuels… Chaque force génératrice de marée correspond à une sinusoïde, appelée **composante harmonique** (harmonic constituent). Le niveau de la mer dans un port donné est à peu près la somme de quelques dizaines de ces sinusoïdes, chacune avec son amplitude et sa phase, qu'il faut d'abord **ajuster** sur des années d'observations locales du niveau de l'eau. C'est l'une des grandes applications concrètes de l'analyse harmonique de Fourier.

### La difficulté : additionner des dizaines de sinusoïdes, sans fin

La difficulté tenait à la quantité de travail de la prédiction elle-même. Une fois fixées les amplitudes et les phases de quelques dizaines de composantes, prédire le niveau de la marée dans un port pour **chaque heure** de l'année à venir exigeait de calculer chacune de ces sinusoïdes à chaque instant, puis de les additionner. Au papier et au crayon, une seule table annuelle des marées suffisait à épuiser un calculateur — or la navigation, les ports et la marine en avaient besoin tous les jours.

### La solution : laisser la machine additionner les sinusoïdes

William Thomson (c'est-à-dire Lord Kelvin) construisit vers 1876 une **machine à prédire les marées** : un calculateur analogique fait de poulies, d'engrenages et de fil d'acier. Chaque roue de la machine produit la sinusoïde d'une composante, son rayon correspondant à l'amplitude et son angle initial à la phase ; un fil d'acier passe sur toutes les roues et **additionne automatiquement** leurs déplacements, et son extrémité entraîne une plume qui **trace**, sur un rouleau de papier en rotation, la courbe horaire de la marée pour toute l'année à venir. Quelques heures à tourner la manivelle, et une table des marées qui aurait demandé des mois de calcul était prête. Ces machines restèrent en service pendant plus d'un demi-siècle et étaient encore utilisées au milieu du XXe siècle — le choix de la marée pour le débarquement de Normandie, pendant la Seconde Guerre mondiale, reposait sur leurs descendantes.

### Ce que cela signifie pour les séries temporelles aujourd'hui

La machine de Kelvin a concrétisé les deux étapes de l'analyse des séries temporelles : d'abord **décomposer** (séparer la série observée en un ensemble de composantes harmoniques), puis **synthétiser / extrapoler** (recombiner les composantes et les prolonger vers l'avenir pour prévoir). Ce paradigme « analyse–synthèse » est au cœur même de l'analyse spectrale ultérieure et de toutes les méthodes de prévision dans le domaine fréquentiel. Et en tant que dispositif qui « fige les lois dans le matériel et livre une prévision d'un tour de manivelle », elle est aussi l'écho moderne, à deux mille ans de distance, de la [machine d'Anticythère](../antikythera/) — l'obsession humaine pour les « machines à prédire automatiques » court des engrenages de bronze jusqu'aux systèmes de prévision d'aujourd'hui.
