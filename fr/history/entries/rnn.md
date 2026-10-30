---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 1990 · Informatique"
permalink: /fr/history/e/rnn/
title: "Réseaux de neurones récurrents et BPTT (Elman · Jordan · Werbos, années 1990)"
lead: "Donner une « mémoire » au réseau : réinjecter l'état caché de l'instant précédent dans l'instant présent. Le prix à payer : lorsque le gradient remonte le temps, il s'évanouit ou explose exponentiellement."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 7 · Réseaux de neurones](../../07/).

### Contexte

De la fin des années 1980 aux années 1990, les réseaux de neurones à propagation avant ont atteint leur maturité grâce à l'algorithme de rétropropagation, mais ils souffrent d'une limite congénitale ? une dimension d'entrée fixe et des exemples indépendants, ce qui les rend naturellement inadaptés aux séquences **de longueur variable et ordonnées**. Dans la langue, la parole ou les séries temporelles, le « présent » dépend du « passé », et un réseau à propagation avant n'a aucun mécanisme pour conserver l'historique. Les chercheurs ont voulu doter le réseau d'une « mémoire » qui lui permette d'encoder les dépendances temporelles dans son état interne.

### Problème

La difficulté centrale est double. D'abord, **comment faire porter au réseau un état d'un pas de temps à l'autre**, de sorte que la sortie dépende non seulement de l'entrée courante mais de toute la séquence vue jusque-là : Ensuite, une fois introduites des connexions de rétroaction dans le temps, **comment l'entraîner** — la rétropropagation standard est conçue pour des graphes à propagation avant sans cycle, alors que la structure récurrente forme une boucle le long du temps.

### Autres courants de l'époque (et leurs limites)

- **Réseaux à propagation avant à fenêtre fixe / réseaux de neurones à retard temporel (TDNN)** : on concatène les $$k$$ derniers pas en une entrée de longueur fixe. Simple et efficace, mais toute dépendance hors de la fenêtre est invisible, et l'on ne peut saisir un historique de longueur arbitraire.
- **Modèles espace d'état linéaires (ARMA, filtre de Kalman, etc.)** : ils possèdent un état récursif et une théorie complète, mais leur expressivité est bornée par l'hypothèse de linéarité, et ils peinent à modéliser des structures séquentielles non linéaires complexes.
- **Modèles de Markov cachés (HMM)** : courant dominant de la modélisation séquentielle, mais leurs états sont discrets et ils reposent sur l'hypothèse markovienne et sur une forte structure d'indépendance conditionnelle, ce qui les limite pour exprimer des dynamiques continues en grande dimension.

### Méthode

Le **réseau de neurones récurrent (RNN)** introduit un état caché $$h_t$$ calculé récursivement dans le temps, où la « mémoire » est explicitement stockée. Les réseaux d'Elman et de Jordan réinjectent respectivement la couche cachée et la sortie dans l'entrée. La récurrence de base est :

$$ h_t=f\big(W x_t + U h_{t-1} + b\big),\qquad \hat{y}_t=g\big(V h_t + c\big) $$

où $$W$$ traite l'entrée courante, $$U$$ reconnecte l'état caché de l'instant précédent et $$f$$ est une activation non linéaire (par exemple $$\tanh$$). Les mêmes poids sont partagés à tous les pas de temps, ce qui permet de traiter des séquences de longueur arbitraire. L'entraînement se fait par **rétropropagation à travers le temps (BPTT, Werbos)** : on « déplie » la structure récurrente le long du temps en un graphe à propagation avant très profond, puis on applique la rétropropagation standard, le gradient devant traverser un à un chaque pas de temps.

Mais c'est précisément là qu'apparaît la faiblesse fatale du RNN. Le gradient de la perte par rapport aux états cachés anciens contient un long produit de matrices jacobiennes :

$$ \frac{\partial h_t}{\partial h_{k}}=\prod_{\tau=k+1}^{t}\frac{\partial h_\tau}{\partial h_{\tau-1}}=\prod_{\tau=k+1}^{t}\operatorname{diag}\!\big(f'\big)\,U^{\top} $$

Lorsque les valeurs propres de ces facteurs restent inférieures à 1, le produit **décroît exponentiellement** avec l'écart $$t-k$$ — c'est l'évanouissement du gradient, et l'information ancienne ne peut être apprise ; lorsqu'elles sont supérieures à 1, il **croît exponentiellement** — c'est l'explosion du gradient, et l'entraînement diverge. Voilà le célèbre **problème des dépendances à long terme**.

### Résultats

Le RNN a permis pour la première fois à un réseau de neurones de traiter nativement des séquences de longueur variable, et s'est montré prometteur en modélisation du langage, en parole, en contrôle, etc. Mais l'évanouissement et l'explosion du gradient le rendent en pratique incapable d'apprendre des dépendances très éloignées : en théorie, il peut se souvenir d'un historique arbitrairement long ; en réalité, il n'exploite de façon fiable que les quelques pas les plus récents. L'explosion du gradient peut être atténuée par écrêtage, mais l'évanouissement est structurel.

### Portée et perspectives

Le RNN a établi le paradigme de modélisation séquentielle « récurrence d'un état caché + rétropropagation à travers le temps », et a clairement posé sur la table le problème des dépendances à long terme. C'est précisément pour vaincre l'évanouissement du gradient que la [LSTM](../lstm/) de 1997 a construit, avec ses portes et sa cellule d'état, un « carrousel d'erreur constante », avant que les GRU, les mécanismes d'attention et enfin le Transformer n'entrent en scène. Aujourd'hui encore, quand nous parlons de « mémoire » et de « dépendances à long terme » dans les modèles de séquences, c'est le langage forgé à l'époque des RNN que nous employons.
