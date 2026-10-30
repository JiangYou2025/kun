---
updated: "2026-06-11"
layout: history
lang: fr
era: "Scénario d'application 9 · Astronomie et géophysique"
permalink: /fr/applications/geophysics/
title: "Astronomie et géophysique"
lead: "Des taches solaires aux marées et aux séismes, la nature nous a laissé les plus longues séries d'observations de l'humanité. Ce sont précisément ces relevés séculaires qui ont fait naître la théorie moderne des séries temporelles."
math: false
prev: /applications/signal/
next: /applications/language/
---

> Ceci est le scénario 9 du dossier [Applications des séries temporelles](../).

## Données et tâches

- **Données** : nombre de taches solaires, courbes de lumière stellaires, ondes sismiques, déformation crustale mesurée par GPS, niveau de la mer / marées, champ géomagnétique.
- **Tâches** : détection de périodicités, détection de phénomènes transitoires et d'exoplanètes, alerte sismique précoce, prévision des marées, prévision de la météorologie de l'espace.

## Ce qui rend ce domaine particulier

- **Durées très longues** : les observations peuvent couvrir un siècle, voire des échelles géologiques, mais l'échantillonnage est souvent irrégulier et lacunaire.
- **Événements majeurs rares** : les événements à fort impact, comme les grands séismes ou les éruptions solaires intenses, comptent très peu d'exemples, ce qui rend l'apprentissage supervisé difficile.
- **Périodes physiques + bruit** : le signal est souvent une superposition de quelques périodes déterministes noyées dans un bruit important ; extraire les périodes cachées est la difficulté centrale.

## Méthodes courantes

- **Analyse spectrale / périodogramme** pour trouver les périodes cachées (préhistoire · [le cycle des taches solaires](../../prehistory/sunspot-cycle/)).
- **Analyse harmonique** pour la prévision des marées — on décompose la marée en composantes sinusoïdales liées aux forces génératrices des astres, puis on extrapole (préhistoire et applications contemporaines).
- Appariement de gabarits / détection d'anomalies pour capter les phénomènes transitoires (ondes gravitationnelles, éruptions solaires…).
- Classification de séries par la **méthode des transits** pour repérer des exoplanètes dans les courbes de lumière.

## Un cas emblématique : le cycle des taches solaires

La série des taches solaires de Wolf est l'un des jeux de données les plus célèbres de l'histoire des séries temporelles. En 1927, c'est précisément pour expliquer son « cycle irrégulier de 11 ans » que Yule a proposé le **modèle autorégressif** (histoire [1](../../history/01/)) — expliquer le présent par le passé de la série elle-même, plutôt que de supposer une sinusoïde parfaite. Une observation astronomique a ainsi directement allumé l'étincelle de l'analyse moderne des séries temporelles.

---

**Termes clés (Key terms)** : périodogramme, analyse harmonique, taches solaires, méthode des transits, alerte sismique précoce, météorologie de l'espace.
