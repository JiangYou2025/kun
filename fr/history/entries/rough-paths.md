---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1998 · Mathématiques"
permalink: /fr/history/e/rough-paths/
title: "Chemins rugueux et signature des chemins (Lyons, 1998)"
lead: "Toute l'information d'un chemin peut-elle se condenser en une suite de nombres ? Avec la « signature », engendrée par les intégrales itérées, Lyons a forgé une clé universelle pour les séquences."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

L'analyse stochastique classique (l'intégrale d'Itô) permet d'intégrer le long de chemins comme le mouvement brownien, mais elle est par essence probabiliste et exigeante quant à la régularité des chemins. Face à des signaux moteurs plus « rugueux » que le mouvement brownien, à la structure de corrélation plus complexe, la théorie traditionnelle peine à offrir un cadre **trajectoriel (pathwise)** et déterministe de résolution des équations différentielles. En 1998, Lyons propose la **théorie des chemins rugueux**, qui établit une théorie de résolution rigoureuse et robuste pour les équations différentielles pilotées par des signaux extrêmement irréguliers : son sous-produit — la **signature des chemins** — est ensuite devenu une caractéristique puissante pour l'analyse des données séquentielles.

### Problème

Deux niveaux de questions s'entremêlent. Sur le plan analytique : lorsque le chemin moteur est très rugueux, la définition classique de l'« intégrale » $$\int Y\,dX$$ tombe en défaut ; **comment définir et résoudre de manière stable $$dY=f(Y)\,dX$$ ?** Sur le plan des données : un chemin multidimensionnel, ordonné, de longueur variable et librement reparamétrable, **comment l'encoder en un ensemble fini et structuré de caractéristiques qui décrive complètement sa forme ?**

### Autres courants de l'époque (et leurs limites)

- **Calcul d'Itô / calcul stochastique** : remarquablement efficace pour les semi-martingales, mais dépendant de la structure probabiliste, non trajectoriel, et limité quant au degré de rugosité ; difficile d'en tirer un traitement unifié de signaux moteurs plus généraux.
- **Caractéristiques artisanales de séries temporelles (moyenne, variance, coefficients de Fourier, etc.)** : interprétables mais éparses, sensibles à la fréquence d'échantillonnage, aux points de départ et d'arrivée et au paramétrage ; elles manquent de complétude et de garanties théoriques unifiées.
- **Méthodes d'alignement comme la déformation temporelle dynamique (DTW)** : elles comparent la forme des séquences, mais ne fournissent pas de représentation combinable linéairement, utilisable comme caractéristique générique par un modèle en aval.

### Méthode

Étant donné un chemin $$X:[0,T]\to\mathbb{R}^d$$, sa **signature** est la suite tensorielle infinie de ses **intégrales itérées** de tous ordres :

$$ S(X)_{0,T}=\Big(1,\;\big\{\textstyle\int_0^T dX^{i}\big\}_i,\;\big\{\textstyle\iint_{0<s<t<T} dX^{i}_s\,dX^{j}_t\big\}_{i,j},\;\dots\Big) $$

où le terme d'ordre $$k$$ est un tenseur de composantes

$$ S(X)^{\,i_1 i_2\cdots i_k}_{0,T}=\idotsint_{0<t_1<\cdots<t_k<T} dX^{i_1}_{t_1}\,dX^{i_2}_{t_2}\cdots dX^{i_k}_{t_k} $$

La signature possède plusieurs propriétés décisives : elle est **invariante par reparamétrage** (indépendante de la vitesse de parcours, elle ne retient que la forme géométrique) ; elle satisfait l'identité de Chen (la signature d'une concaténation de chemins est le produit tensoriel des signatures des morceaux), ce qui facilite le calcul incrémental ; et, une fois ajoutée une augmentation temporelle pour écarter les cas triviaux, la signature **détermine presque de manière unique le chemin**. Le plus important est la **non-linéarité universelle (universal nonlinearity)** : toute fonctionnelle continue sur les chemins peut être approchée arbitrairement bien par une **combinaison linéaire** des termes de la signature — autrement dit, calculer d'abord la signature puis brancher un modèle linéaire permet en principe d'exprimer n'importe quelle fonction (lisse) du chemin. En pratique, on n'utilise comme caractéristiques que la signature tronquée à un certain ordre, de dimension finie.

### Résultats

En transformant une séquence en sa signature (tronquée), suivie d'un modèle simple, on a obtenu des performances solides et robustes en reconnaissance de l'écriture manuscrite chinoise, sur les séries temporelles financières, les signaux médicaux, dans des compétitions d'apprentissage automatique, etc. Les caractéristiques de signature s'accommodent naturellement de l'échantillonnage irrégulier, des données manquantes et des longueurs inégales, tout en bénéficiant de solides garanties mathématiques : elles constituent une méthode de représentation des séquences singulière et compétitive.

### Portée et perspectives

La théorie des chemins rugueux plonge d'un côté ses racines dans l'analyse stochastique (elle fournit un cadre trajectoriel de résolution des équations différentielles stochastiques, et les structures de régularité de Hairer s'en sont aussi inspirées), et s'étend de l'autre vers l'apprentissage automatique, fondant les « caractéristiques universelles des séquences » sur des mathématiques rigoureuses. Combinée aux réseaux de neurones, elle a donné naissance aux **noyaux de signature**, aux **réseaux de signature profonds** et jusqu'aux [équations différentielles contrôlées neuronales (Neural CDE)](../neural-cde/) — lesquelles font précisément de la « dynamique continue pilotée par un chemin » le cœur d'un modèle de séquence. Des mathématiques pures à l'apprentissage séquentiel, la signature offre une clé rare, à la fois complète en théorie et utile en pratique.
