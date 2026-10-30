---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1997 · Informatique"
permalink: /fr/history/e/lstm/
title: "Les réseaux à longue mémoire à court terme (Hochreiter · Schmidhuber, 1997)"
lead: "Dans un RNN ordinaire, le gradient décroît exponentiellement au fil du temps. Le LSTM construit un « tapis roulant » qui ne s'atténue presque pas, puis utilise trois portes pour décider quoi mémoriser, quoi oublier et quoi laisser sortir."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 7 · Réseaux de neurones](../../07/).

### Contexte

Au milieu des années 1990, le potentiel des [réseaux de neurones récurrents (RNN)](../rnn/) pour traiter les séquences était reconnu, mais leur problème de **disparition / explosion du gradient** constituait un obstacle pratique majeur. Hochreiter en a précisément caractérisé la cause : lors de la rétropropagation à travers le temps, le gradient est multiplié de façon répétée par le même ensemble de facteurs, si bien que le signal d'erreur décroît ou explose exponentiellement au fil du temps, et le réseau ne parvient pas à apprendre les dépendances éloignées. Pour qu'un modèle de séquence « se souvienne » vraiment de ce qui est loin, il fallait remédier au problème à la racine, par la structure même du réseau.

### Problème

La difficulté se formule précisément : dans la BPTT, le gradient de la perte par rapport aux états antérieurs est un long produit de jacobiennes, dont les propriétés spectrales font que le signal d'erreur soit disparaît, soit explose. **Peut-on concevoir une unité récurrente dans laquelle le signal d'erreur circule dans le temps presque sans perte (ni disparition ni explosion), afin d'apprendre de manière stable des dépendances à long terme ?**

### Les autres courants de l'époque (et leurs limites)

- **Écrêtage du gradient + RNN ordinaire** : permet de contenir l'explosion du gradient, mais ne peut rien contre sa disparition ; les dépendances à long terme restent inaccessibles.
- **Optimiseurs du second ordre / spécialisés** : tentent de contourner les gradients pathologiques, mais sont coûteux, instables et ne touchent pas la cause structurelle.
- **Réseaux à états d'écho / RNN à constantes de temps (un peu plus tard)** : atténuent le problème par des poids récurrents aléatoires fixes ou des constantes de temps multi-échelles ; l'idée est originale, mais soit la couche récurrente n'est pas entraînée, soit l'expressivité est limitée.

### Méthode

Le cœur du LSTM est l'introduction d'un **état de cellule (cell state)** $$c_t$$, un « tapis roulant d'information » qui traverse le temps et dont la mise à jour repose essentiellement sur l'**addition** plutôt que sur des multiplications répétées ; il forme ainsi un **carrousel d'erreur constante (Constant Error Carousel)** — l'erreur peut remonter le temps presque sans atténuation. Autour de lui se trouvent trois **portes** (des vannes $$\sigma$$ à valeurs dans $$[0,1]$$) qui régulent l'écriture, la conservation et la lecture de l'information :

$$ f_t=\sigma(W_f[h_{t-1},x_t]+b_f),\quad i_t=\sigma(W_i[h_{t-1},x_t]+b_i),\quad o_t=\sigma(W_o[h_{t-1},x_t]+b_o) $$

L'information candidate et les mises à jour de la cellule et de l'état caché sont :

$$ \tilde{c}_t=\tanh(W_c[h_{t-1},x_t]+b_c),\qquad c_t=f_t\odot c_{t-1}+i_t\odot \tilde{c}_t,\qquad h_t=o_t\odot \tanh(c_t) $$

Intuitivement : la **porte d'oubli** $$f_t$$ décide quelle part de l'ancienne mémoire conserver, la **porte d'entrée** $$i_t$$ quelle part de l'information nouvelle écrire, et la **porte de sortie** $$o_t$$ quelle part exposer à l'extérieur. Tout repose sur le chemin additif $$c_t=f_t\odot c_{t-1}+\dots$$ : lorsque $$f_t\approx 1$$, le gradient de $$c_t$$ par rapport à $$c_{t-1}$$ vaut environ 1, et le signal d'erreur peut franchir des centaines, voire des milliers de pas presque sans s'atténuer — c'est la raison mathématique pour laquelle il peut apprendre des dépendances à long terme.

### Résultats

Le LSTM apprend de façon fiable des dépendances séparées de centaines, voire de milliers de pas, bien au-delà des RNN ordinaires. Il a longtemps dominé les tâches séquentielles — reconnaissance de la parole, reconnaissance de l'écriture manuscrite, traduction automatique, modélisation du langage — jusqu'à l'ère du Transformer, et a donné naissance à des variantes plus légères comme le GRU. « Portes + canal de mémoire additif » est devenu le paradigme standard de la modélisation de séquences.

### Portée et perspectives

Le LSTM a résolu de front, par une innovation structurelle plutôt que par une optimisation plus agressive, le problème des dépendances à long terme qui minait les RNN depuis des années ; c'est l'un des travaux fondateurs de l'apprentissage profond appliqué aux séquences. Il a introduit dans les réseaux de neurones l'idée d'une « mémoire contrôlable », influençant profondément les mécanismes d'attention ultérieurs (qui choisissent eux aussi « quelle partie de l'historique regarder »). Même aujourd'hui, à l'ère dominée par le Transformer, l'intuition des portes et de la transmission d'état reste vivante dans les divers modèles de séquences à espace d'états et dans les architectures efficaces pour les longues séquences.
