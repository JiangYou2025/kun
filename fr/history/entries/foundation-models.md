---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 2020 · Informatique"
permalink: /fr/history/e/foundation-models/
title: "Un seul modèle pour prévoir toutes les séries (TimesFM · Chronos · Moirai, années 2020)"
lead: "Pré-entraînés sur d'immenses volumes de séries hétérogènes, utilisables tels quels en prévision zero-shot ou few-shot : les modèles de fondation pour séries temporelles cherchent à transformer « un modèle entraîné par tâche » en « un seul modèle face à toutes les séries »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 10 · Grands modèles et KUN](../../10/).

### Contexte

Le langage et la vision sont depuis longtemps entrés dans l'ère des « modèles de fondation » : on pré-entraîne un modèle généraliste sur une masse énorme de données, puis on le transfère aux tâches en aval, en zero-shot ou par ajustement fin. Les séries temporelles sont longtemps restées à la traîne — chaque domaine, chaque jeu de données entraînait le plus souvent son propre modèle spécialisé. Mais à mesure que des travaux comme [PatchTST](../patchtst/) ont tokenisé les séries de façon stable et que le pré-entraînement auto-supervisé inter-jeux de données s'est révélé viable, toute une série de **modèles de fondation pour séries temporelles** — TimesFM, Chronos, Moirai — a émergé en 2023–2024.

### Problème

« L'universalité » est bien plus difficile pour les séries temporelles que pour le langage. Les séries diffèrent énormément par leur **fréquence d'échantillonnage** (seconde, heure, mois), leur **échelle et unité**, leur **nombre de canaux** et leur **structure périodique**, et il n'existe aucun « vocabulaire » unifié tout prêt. **Peut-on pré-entraîner un modèle sur une masse aussi hétérogène de séries, de sorte qu'il fournisse directement des prévisions fiables sur de nouvelles données, sans réentraînement ?**

### Autres courants de l'époque (et leurs limites)

- **Modèles spécialisés par tâche (y compris l'[ARIMA](../box-jenkins/) classique et divers réseaux profonds)** : précision respectable, mais il faut réentraîner et réajuster les hyperparamètres à chaque nouveau jeu de données ; le transfert et le démarrage à froid coûtent cher.
- **Automatisation purement statistique (bibliothèques d'ARIMA automatique / de lissage exponentiel)** : robuste et utilisable en zero-shot, mais d'expressivité limitée, peu apte à exploiter les connaissances communes à plusieurs domaines.
- **Premières tentatives généralistes** : faute d'une représentation d'entrée unifiée et d'un corpus de pré-entraînement suffisamment varié, leur généralisation et leurs capacités zero-shot restaient limitées.

### Méthode

Ces modèles suivent des voies diverses, mais partagent une même recette : **tokenisation unifiée + pré-entraînement autorégressif / masqué à grande échelle**. Prenons l'approche par discrétisation (comme Chronos) : on projette d'abord la série réelle sur un « vocabulaire » fini par quantiles ou par intervalles, puis, comme un modèle de langage, on prédit de manière autorégressive le token suivant :

$$ p_\theta(x_{1:T}) = \prod_{t=1}^{T} p_\theta\big(x_t \mid x_{1:t-1}\big) $$

Le modèle minimise la log-vraisemblance négative sur un vaste corpus couvrant de nombreux domaines et fréquences

$$ \mathcal{L}(\theta) = -\,\mathbb{E}_{x\sim\mathcal{D}}\sum_{t} \log p_\theta\big(x_t \mid x_{1:t-1}\big) $$

Pour absorber l'hétérogénéité, chacun a sa parade : TimesFM utilise un Transformer de type décodeur sur des patchs et traite de façon unifiée différents horizons ; Moirai introduit plusieurs tailles de patchs et une attention « toutes variables » pour accueillir différentes fréquences et le multivarié ; Chronos quantifie les valeurs en tokens et réutilise directement l'architecture des modèles de langage. Une fois l'entraînement terminé, face à une série jamais vue, il suffit de fournir l'historique et de laisser le modèle poursuivre pour obtenir une **prévision zero-shot**, la plupart produisant des quantiles / intervalles probabilistes plutôt qu'un point unique.

### Résultats

Sur de vastes bancs d'essai zero-shot, ces modèles de fondation **approchent, voire dépassent** souvent des modèles spécialisés soigneusement réglés pour un seul jeu de données, tout en épargnant l'entraînement par tâche. Ils manifestent aussi des effets d'échelle à la manière des modèles de langage : plus il y a de données et de paramètres, plus la couverture est large, meilleure est la généralisation zero-shot — les séries temporelles disposent pour la première fois d'une voie réaliste vers un « pré-entraîné une fois, utilisable partout ».

### Portée et perspectives

Les modèles de fondation pour séries temporelles portent cette histoire centenaire vers un nouveau point de convergence : de l'[autorégression](../yule-ar/) de Yule et de l'[ARMA](../box-jenkins/) de Box–Jenkins jusqu'au [Transformer](../patchtst/), à [Mamba](../mamba/) et aux [Neural CDE](../neural-cde/), tous les biais inductifs accumulés pourraient désormais être fondus dans un modèle généraliste pré-entraîné sur une masse de séries. Les défis restent réels : échantillonnage hétérogène et données manquantes (la perspective des chemins continus des [Neural CDE](../neural-cde/) pourrait y aider), efficacité sur des contextes ultra-longs (le temps linéaire de [Mamba](../mamba/) est un candidat), et la manière d'unifier les structures multi-échelles avec une ossature extensible aux noyaux interchangeables — c'est précisément la direction de réponse proposée par [Kernel U-Net](../kun/). « Un seul modèle pour prévoir toutes les séries » n'est pas encore pleinement réalisé, mais le cap est clair : doter les séries temporelles, comme le langage, de leurs propres modèles de fondation. Un siècle plus tard, le pas de Yule — « utiliser le passé pour prévoir la valeur suivante » — se trouve démultiplié à l'infini par le pré-entraînement.
