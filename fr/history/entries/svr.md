---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 2000 · Informatique"
permalink: /fr/history/e/svr/
title: "La régression à vecteurs de support (Vapnik et al., années 2000)"
lead: "Qu'est-ce qu'une « bonne » régression ? La SVR donne une réponse contre-intuitive : ne rien pénaliser tant que l'on reste dans le tube ε, puis, grâce à l'astuce du noyau, courber cette droite plate dans un espace de grande dimension."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 8 · Apprentissage automatique](../../08/).

### Contexte

À la fin des années 1990, les **machines à vecteurs de support (SVM)** proposées par Vapnik et ses collègues connaissent un grand succès en classification. Elles reposent sur la **théorie statistique de l'apprentissage** et la **minimisation du risque structurel** : ne pas seulement minimiser l'erreur d'entraînement, mais aussi contrôler la complexité du modèle pour garantir la généralisation. Une question vient naturellement : peut-on appliquer la même idée à la **régression** ? Dans les années 2000, portée par l'engouement pour les méthodes à noyau, la **régression à vecteurs de support (SVR)** est largement utilisée pour la prévision de séries temporelles : on transforme la série, par fenêtre glissante, en un problème de régression supervisée « vecteur de caractéristiques → valeur suivante », et la SVR devient une référence solide.

### Problème

La régression classique par moindres carrés utilise la perte quadratique : elle pénalise **tous** les écarts, est liée à l'hypothèse de bruit gaussien, est **sensible aux valeurs aberrantes**, et le modèle tend à surajuster le bruit. Or les séries temporelles regorgent de sauts anormaux et de bruits à queues épaisses. Il faut une régression qui tolère les petites erreurs tout en restant robuste aux grandes, qui généralise bien sur des relations **non linéaires**, et qui intègre explicitement la « complexité du modèle » dans l'objectif d'optimisation.

### Les autres courants de l'époque (et leurs limites)

- **Moindres carrés / régression ridge** : analytiques et rapides, mais la perte quadratique est sensible aux valeurs aberrantes, et le pouvoir expressif d'un modèle linéaire est limité (il faut fabriquer à la main des caractéristiques non linéaires).
- **Perceptron multicouche (réseau de neurones)** : très expressif, mais à l'époque difficile à entraîner, sujet aux minima locaux, gourmand en données et en réglages, et instable sur de petits échantillons de séries temporelles.
- **k plus proches voisins / régression locale** : aucun entraînement nécessaire, mais la « malédiction de la dimension » est sévère en grande dimension, et il n'offre pas de contrôle global et lisse de la complexité.

### Méthode

Le premier élément clé de la SVR est la **perte ε-insensible** : tant que l'écart entre prédiction et valeur réelle reste inférieur à $$ \varepsilon $$, il n'est pas pénalisé, ce qui forme un « tube ».

$$ L_\varepsilon(y, f(x)) = \max\big(0,\ |y - f(x)| - \varepsilon\big) $$

L'objectif est de trouver une fonction aussi **plate** que possible (de faible norme de poids) qui fasse entrer le plus de points possible dans le tube ε. Le problème primal s'écrit

$$ \min_{w,b,\xi,\xi^*}\ \tfrac12\|w\|^2 + C\sum_{i=1}^{n}(\xi_i+\xi_i^*) \quad \text{s.t. } |y_i - (w^\top \phi(x_i)+b)| \le \varepsilon + \xi_i^{(*)} $$

où $$ C $$ arbitre entre la platitude et la tolérance aux sorties du tube, les variables d'écart $$ \xi,\xi^* $$ mesurant les dépassements par le haut et par le bas. Le second élément clé est l'**astuce du noyau** : par le problème dual, la solution peut s'écrire sous une forme qui ne dépend que de produits scalaires, et l'on remplace la projection explicite en grande dimension par une fonction noyau $$ K(x_i,x) = \phi(x_i)^\top\phi(x) $$

$$ f(x) = \sum_{i=1}^{n} (\alpha_i - \alpha_i^*)\,K(x_i, x) + b $$

Seuls les points qui sortent du tube ou se trouvent sur sa frontière ont un coefficient $$ (\alpha_i-\alpha_i^*)\neq 0 $$ : ce sont les **vecteurs de support** — la solution est parcimonieuse. Le noyau RBF courant $$ K(x_i,x)=\exp(-\gamma\|x_i-x\|^2) $$ transforme cette « régression linéaire plate » en une surface fortement non linéaire dans l'espace d'origine.

### Résultats

Pour la prévision de séries de taille petite ou moyenne, au rapport signal/bruit modeste, la SVR se montre robuste : le tube ε apporte résistance au bruit et parcimonie, l'astuce du noyau apporte l'expressivité non linéaire, et la minimisation du risque structurel une bonne généralisation. Dans les compétitions de prévision en finance, charge électrique ou vitesse du vent, elle est longtemps restée une référence difficile à battre. Le prix à payer : les trois hyperparamètres $$ C,\varepsilon,\gamma $$ doivent être réglés par validation croisée, et la matrice noyau croît comme le carré du nombre d'échantillons, ce qui devient coûteux sur de gros volumes de données.

### Portée et perspectives

La SVR a fait entrer dans la pratique des séries temporelles l'idée que « **bonne régression = tolérance aux erreurs + platitude + complexité maîtrisée** » ; avec les [GBDT](../gbdt/) de la même époque, elle a établi le paradigme de prévision « **caractéristiques + apprenant puissant** » : on transforme d'abord la série en tableau par fenêtres glissantes ou caractéristiques statistiques, puis on la confie à un régresseur puissant. Même après l'essor des modèles profonds, la SVR reste un point de comparaison honnête pour vérifier si « le profond fait vraiment mieux ». Elle nous rappelle aussi que le choix de la fonction de perte est en soi un biais inductif.
