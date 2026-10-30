---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1988–89 · Informatique"
permalink: /fr/history/e/td-qlearning/
title: "Différences temporelles et Q-learning (Sutton · Barto · Watkins, 1988–89)"
lead: "Inutile d'attendre que la poussière retombe pour apprendre : en corrigeant « la prédiction d'il y a un instant » par « la prédiction de maintenant », l'agent s'approche pas à pas, par auto-amorçage, de la récompense future le long de la séquence."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Comment un agent peut-il apprendre à prendre de bonnes décisions séquentielles au fil d'interactions répétées avec son environnement ? La [programmation dynamique de Bellman](../bellman-dp/) avait depuis longtemps fourni l'équation d'optimalité, mais elle exige un **modèle connu de l'environnement** (probabilités de transition et récompenses) et le parcours de tout l'espace d'états — or, en pratique, le modèle est souvent inconnu et l'espace d'états bien trop vaste. De l'autre côté, l'apprentissage supervisé exige pour chaque action une étiquette donnant la bonne réponse ; mais dans la décision séquentielle, la qualité d'une action n'est souvent révélée que bien plus tard, par le résultat final — **la récompense est différée**. Prédire la récompense cumulée future est, en soi, un problème de séries temporelles.

### Problème

L'agent ne perçoit qu'une suite « état — action — récompense immédiate », avec des récompenses rares et tardives. **Comment apprendre en ligne à prédire la récompense à long terme et à choisir en conséquence l'action optimale, sans connaître le modèle de l'environnement et sans devoir attendre la fin d'un épisode complet ?**

### Les autres courants de l'époque (et leurs limites)

- **Programmation dynamique ([Bellman](../bellman-dp/))** : optimale en théorie, mais elle requiert un modèle connu et le balayage de tout l'espace d'états ; en pratique, le modèle est inconnu et la dimension trop élevée.
- **Méthodes de Monte-Carlo** : attendre la fin d'un épisode complet et mettre à jour avec la récompense cumulée réelle. Sans biais, mais il faut atteindre le terme pour apprendre ; la variance est forte et elles conviennent mal aux tâches continues.
- **Apprentissage supervisé** : il faut des étiquettes correctes à chaque pas, impossibles à obtenir dans les tâches séquentielles à récompense différée.

### Méthode

Sutton et Barto proposent l'**apprentissage par différences temporelles (TD)** : au lieu d'attendre le dénouement, on corrige **la prédiction présente** par **la prédiction de l'instant suivant** — c'est l'auto-amorçage (*bootstrapping*). Soit $$V(s)$$ l'estimation de la valeur de l'état $$s$$ ; après avoir observé la récompense immédiate $$r_{t+1}$$ et l'état suivant $$s_{t+1}$$, on met à jour selon l'**erreur TD** :

$$ V(s_t) \leftarrow V(s_t) + \alpha\,\big[\,\underbrace{r_{t+1} + \gamma\, V(s_{t+1}) - V(s_t)}_{\text{erreur TD }\delta_t}\,\big] $$

où $$\alpha$$ est le taux d'apprentissage et $$\gamma\in[0,1)$$ le facteur d'actualisation. La quantité entre crochets est exactement l'écart entre « la cible de prédiction à un pas actuelle » et « l'ancienne estimation » ; elle joue le rôle d'une **erreur de prédiction** — de même nature que l'innovation dans les séries de [Yule](../yule-ar/) ou l'erreur de prédiction en [identification des systèmes](../system-identification/). Watkins va plus loin avec le **Q-learning**, qui apprend directement la valeur état — action $$Q(s,a)$$, **sans modèle de l'environnement** :

$$ Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha\,\Big[\, r_{t+1} + \gamma \max_{a} Q(s_{t+1},a) - Q(s_t,a_t)\,\Big] $$

Le $$\max_a$$ de cette formule la fait converger directement vers la solution de l'équation d'optimalité de Bellman. Watkins démontre que, sous des conditions appropriées, le Q-learning converge vers la valeur d'action optimale $$Q^*$$ — un jalon du contrôle optimal sans modèle.

### Résultats

TD et Q-learning permettent à un agent d'apprendre en ligne la récompense à long terme à partir du seul flux d'expérience, sans modèle et sans attendre la fin. Ils deviennent le cœur algorithmique de l'apprentissage par renforcement et portent une série de percées, du backgammon de TD-Gammon aux réseaux Q profonds (DQN) jouant à l'Atari, puis à AlphaGo.

### Portée et perspectives

L'apprentissage TD unifie « prédire l'avenir » et « apprendre de l'erreur de prédiction » au sein de la décision séquentielle ; son idée d'auto-amorçage s'est révélée étonnamment proche du signal d'erreur de prédiction de récompense porté par la dopamine dans le cerveau, jetant un pont entre apprentissage automatique et neurosciences. Il rejoint dans l'esprit la [MPC](../mpc/) et son principe « utiliser la prédiction pour guider la décision présente », à ceci près que l'une optimise de façon glissante à partir d'un modèle, l'autre apprend par auto-amorçage à partir de l'expérience. Apprendre à prédire et à contrôler à partir de récompenses différées : ce paradigme reste aujourd'hui le moteur de l'apprentissage par renforcement, et même des agents généralistes.
