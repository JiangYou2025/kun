---
updated: "2026-06-11"
layout: history
lang: fr
permalink: /fr/tasks/
title: "Histoire des tâches de séries temporelles · La coévolution des tâches et de la puissance de calcul"
lead: "L'histoire raconte comment les méthodes ont été inventées ; ici, changeons de point de vue : qu'une catégorie de tâches de séries temporelles soit réalisable, et à partir de quand, n'est souvent pas une question de mathématiques, mais de la technologie de calcul de l'époque — c'est le prix du stockage, de la mémoire et de la puissance de calcul, ou bien l'apparition d'un produit précis (calculatrice à manivelle, ordinateur embarqué, ordinateur central, ordinateur personnel, GPU, grappe de TPU), qui a fait passer une nouvelle tâche de « incalculable / impensable » à « faisable »."
---

> Une page sœur de l'[histoire des séries temporelles](../history/). L'histoire raconte **l'évolution des outils**, cette page raconte **l'évolution des tâches**, en soulignant une chaîne causale souvent négligée : **progrès de la technologie de calcul (ou apparition d'un produit) → une nouvelle catégorie de tâches devient faisable pour la première fois**. Pour chaque époque, on commence par indiquer la puissance de calcul déterminante de cette génération, puis on énumère les **types de tâches** qu'elle a « débloqués ».
>
> Quant aux **scénarios d'application concrets** de ces tâches dans les différents secteurs (finance, énergie, santé, transports, météorologie…), voir les pages sœurs [Préhistoire et applications contemporaines](../prehistory/) et [Applications des séries temporelles](../applications/) ; cette page ne les reprend pas.

## De l'Antiquité au XIXe siècle : relevés manuels et calcul à la main

Il n'y a pas d'« ordinateur » à ce stade ; les technologies habilitantes sont **l'écriture et le calendrier** (pour consigner les observations), **les tables de logarithmes et la règle à calcul** (qui transforment les lourdes multiplications et divisions en additions et soustractions), puis, au XIXe siècle, les **calculateurs analogiques mécaniques**. La limite des tâches, c'est ce qu'une personne peut calculer avec du papier et un crayon.

| Époque | Tâche | Technologie / produit habilitant | En une phrase : comment la technologie a rendu la tâche possible |
|------|------|----------------|------------------------------|
| ~3000 av. J.-C. | Prévision des crues / des phénomènes célestes | Calendrier, tablettes d'argile / papyrus, tables de périodes | Niveau du Nil, éclipses de Lune babyloniennes — il faut d'abord pouvoir **consigner** de longues séries pour extrapoler à l'aide de tables de périodes |
| 1662 | Prévision de la mortalité (table de mortalité) | Registres de décès imprimés (Bills of Mortality) + arithmétique | Graunt **compile en tableaux** les listes de décès de Londres : la première table de mortalité |
| 1682 | Prévision du retour d'une comète | Mécanique newtonienne + tables de logarithmes / règle à calcul | Halley, en calculant l'orbite à la main, prédit le retour de la comète 76 ans plus tard |
| 1801 | Prévision d'orbite / de position | Moindres carrés + calcul à la main | Gauss reconstitue l'orbite de Cérès à partir d'un petit nombre d'observations |
| 1876 | Prévision des marées | Machine à prédire les marées de Kelvin (calculateur analogique mécanique) | Synthèse harmonique par engrenages : **pour la première fois, une machine « calcule »** le niveau futur de la marée |

## De 1900 aux années 1960 : des calculatrices mécaniques aux ordinateurs embarqués

Dans la première moitié du XXe siècle, la puissance de calcul se résume aux **calculatrices mécaniques à manivelle ou électriques** ; la Seconde Guerre mondiale apporte les **calculateurs analogiques et électroniques**, et les années 1960 voient apparaître **les circuits intégrés et les ordinateurs embarqués**. La leçon la plus profonde de cette période : **la forme de la mémoire et de la puissance de calcul détermine directement la forme des algorithmes**.

| Époque | Tâche | Technologie / produit habilitant | En une phrase : comment la technologie a rendu la tâche possible |
|------|------|----------------|------------------------------|
| 1900 | Modélisation du cours des actions | Calcul à la main + théorie des probabilités | Bachelier décrit le cours de la rente française à Paris par une marche aléatoire |
| 1927 | Prévision d'indicateurs économiques / naturels | Calculatrices mécaniques à manivelle · électriques | Les calculatrices mécaniques rendent la résolution des régressions faisable ; Yule ajuste un AR pour prévoir les taches solaires |
| Années 1940 | Prévision de signaux / de cibles (militaire) | Conduite de tir de la Seconde Guerre mondiale · calculateurs analogiques | La défense antiaérienne doit extrapoler la position d'une cible à partir d'une trajectoire bruitée → filtrage optimal de Wiener–Kolmogorov |
| Années 1950 | Prévision des stocks / des ventes | Premiers ordinateurs électroniques (coûteux, puissance de calcul rare) | **Le calcul coûte cher**, ce qui fait naître le lissage exponentiel, récursif en O(1), capable de prévoir à faible coût des dizaines de milliers de SKU |
| 1960 | Navigation / localisation et pistage | Ordinateur de guidage d'Apollo (circuits intégrés, mémoire de quelques Ko) | **Mémoire minuscule → forme récursive** : le filtre de Kalman tombe à pic et permet la localisation en temps réel lors de l'alunissage |

> Notez ces deux lignes, années 1950 et 1960 : si le lissage exponentiel l'a emporté, c'est parce que le calcul coûtait cher à l'époque ; si le filtre de Kalman prend la forme récursive « prédiction–mise à jour », c'est parce que l'ordinateur embarqué n'avait que quelques Ko de mémoire et ne pouvait pas stocker tout l'historique. **Les contraintes façonnent les méthodes.**

## Des années 1970 aux années 1990 : ordinateurs centraux, ordinateurs personnels et capteurs industriels

Dans les années 1970, les **ordinateurs centraux** rendent pour la première fois praticable l'optimisation numérique itérative ; dans les années 1980, les **ordinateurs personnels et stations de travail** font entrer la modélisation dans les bureaux et les salles de marché ; dans les années 1990, **capteurs industriels + acquisition de données (SCADA) + stockage bon marché** font de « l'enregistrement continu de l'état des équipements » la norme.

| Époque | Tâche | Technologie / produit habilitant | En une phrase : comment la technologie a rendu la tâche possible |
|------|------|----------------|------------------------------|
| 1970 | Prévision macroéconomique | Ordinateurs centraux (IBM System/360, etc.) | **Le maximum de vraisemblance itératif** devient enfin calculable ; l'ARIMA de Box–Jenkins s'impose comme paradigme |
| Années 1970 | Reconnaissance de la parole | Projets de la DARPA + ordinateurs centraux | Assez de puissance pour les HMM + la programmation dynamique de Viterbi, afin de transcrire la parole téléphonique |
| 1973 | Évaluation des options | Calculatrices de poche + ordinateurs centraux | Formule de Black–Scholes + calcul numérique : naissance de l'évaluation à grande échelle sur les places boursières |
| Années 1980 | Gestion des risques (VaR) | Ordinateurs personnels / stations de travail + logiciels d'économétrie | La diffusion du PC fait entrer la modélisation GARCH de la volatilité dans les salles de marché |
| 1987 | Cointégration multivariée | Stations de travail + logiciels statistiques | Engle–Granger prévoient l'équilibre de long terme des variables macroéconomiques |
| Années 1990 | Prévision des pannes d'équipement | Capteurs industriels + SCADA + stockage bon marché | Ce n'est qu'en **pouvant acquérir et conserver en continu** les séries des capteurs que la maintenance prédictive devient envisageable |
| 1997 | Modélisation de séquences à dépendances longues | Les CPU de l'époque (les GPU ne sont pas encore entrés en scène) | Le LSTM résout la disparition du gradient grâce à ses portes — mais il devra attendre l'ère des GPU pour vraiment briller |

## Des années 2000 aux années 2010 : données à l'échelle d'Internet, grappes de serveurs et GPU

C'est le tournant de la puissance de calcul : **Internet apporte des quantités massives de séries**, **les grappes de serveurs + entrepôts de données** rendent le stockage et le calcul parallèle bon marché, et à partir de 2007 **les GPU NVIDIA + CUDA** abaissent d'un ordre de grandeur le coût d'entraînement des réseaux profonds — après AlexNet en 2012, les modèles de séquences profonds connaissent une explosion.

| Époque | Tâche | Technologie / produit habilitant | En une phrase : comment la technologie a rendu la tâche possible |
|------|------|----------------|------------------------------|
| 2012 | **L'essor de l'apprentissage profond (tournant)** | GPU NVIDIA + CUDA (AlexNet) | Le calcul généraliste sur GPU fait chuter le coût d'entraînement des réseaux profonds ; la modélisation de séquences change de régime |
| 2017 | Prévision probabiliste globale | GPU dans le cloud (AWS, etc.) + vastes bases de séries | DeepAR s'entraîne conjointement sur des dizaines de milliers de séries et produit des distributions de probabilité |
| 2017 | Détection d'anomalies | Infrastructures de supervision / télémétrie à grande échelle | Télémétrie des serveurs et du trafic réseau → alertes en temps réel par Autoencoder/LSTM |
| 2019 | Prévision interprétable | Grappes de GPU | N-BEATS, purement feedforward + empilement résiduel, produit une décomposition tendance/saison |

## Des années 2020 à aujourd'hui : grappes d'accélérateurs et modèles de fondation

Lorsque la puissance de calcul entre dans l'ère des **grappes de GPU / TPU à grande échelle + pré-entraînement massif**, les tâches changent de nature : on n'entraîne plus un modèle distinct pour chaque problème, on **pré-entraîne un modèle généraliste** pour résoudre des tâches jamais vues. L'abondance de puissance de calcul pousse à son tour à la « généralisation » des tâches.

| Époque | Tâche | Technologie / produit habilitant | En une phrase : comment la technologie a rendu la tâche possible |
|------|------|----------------|------------------------------|
| Années 2020 | Classification de séries temporelles | GPU | Classification d'électrocardiogrammes, diagnostic de pannes à partir de signaux de vibration industriels, par Transformer / CNN |
| Années 2020 | Génération de séries temporelles | GPU + frameworks de modèles de diffusion / génératifs | Génération de données synthétiques réalistes en finance et en santé |
| 2023– | Prévision zero-shot | Pré-entraînement à grande échelle + grappes d'accélérateurs | TimesFM et Chronos pré-entraînent un modèle unique qui prévoit de nouvelles séries sans entraînement |
| 2024– | Séries temporelles multimodales / conversationnelles | Infrastructures d'inférence des LLM | Texte + image + capteurs combinés ; on demande en langage naturel « les ventes de la semaine prochaine ? » |

## Comment la puissance de calcul « débloque » les tâches

> **Les méthodes n'évoluent pas ex nihilo : chaque fois que la technologie de calcul franchit un palier, elle débloque une nouvelle série de tâches.**

En reliant les cinq époques ci-dessus, on voit se dessiner quelques chaînes causales nettes :

1. **Le stockage décide « s'il peut y avoir une série »** : sans moyens d'enregistrement comme les tablettes d'argile, les registres de décès, le SCADA ou les entrepôts de données, il n'y a pas de données à analyser — la prévision des pannes comme la prévision du taux de clics doivent d'abord attendre de « pouvoir tout stocker ».
2. **La forme de la mémoire détermine la forme de l'algorithme** : l'ordinateur embarqué d'Apollo ne disposait que de quelques Ko de mémoire, ce qui a imposé au filtre de Kalman sa structure récursive « prédiction–mise à jour » ; faute de pouvoir stocker tout l'historique, on ne peut que mettre à jour en ligne.
3. **Le prix du calcul détermine la complexité des méthodes** : quand le calcul est cher, c'est le lissage exponentiel en O(1) qui l'emporte ; ce n'est qu'une fois le calcul devenu bon marché que les réseaux profonds complexes deviennent rentables.
4. **Les nouveaux produits ouvrent directement de nouvelles tâches** : machine à prédire les marées, ordinateur central, ordinateur personnel, GPU, grappe de TPU — l'apparition de chaque produit emblématique correspond à une série de tâches « autrefois incalculables » qui deviennent faisables pour la première fois.
5. **L'abondance de calcul pousse à la « généralisation »** : quand le coût du pré-entraînement d'un grand modèle devient acceptable, on passe de « un modèle par problème » à « un seul modèle pour tout » (modèles de fondation, zero-shot, multimodal).

> Retour au [fil principal de l'histoire](../history/) · [Préhistoire et applications contemporaines](../prehistory/) · [La nature du temps](../nature-of-time/) · [Paradoxes du temps](../paradoxes/)
