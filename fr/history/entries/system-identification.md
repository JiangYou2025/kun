---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · années 1970–80 · Contrôle / communications"
permalink: /fr/history/e/system-identification/
title: "L'identification des systèmes (Åström · Ljung, années 1970–80)"
lead: "L'ingénieur n'a pas d'équation différentielle toute faite, seulement un tas de données d'entrée et de sortie — qu'à cela ne tienne, laissons les données « faire pousser » le modèle elles-mêmes : identifier un système dynamique à partir de signaux."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Au milieu du XXe siècle, la théorie du contrôle repose sur le principe « le modèle d'abord » : l'espace d'états de [Kalman](../kalman/), le contrôle optimal, l'analyse de stabilité supposent tous connues les équations différentielles ou aux différences du système. Mais les réacteurs chimiques, les avions ou les machines à papier réels ne se laissent souvent pas décrire par des équations exactes à partir des premiers principes — les paramètres sont inconnus, les mécanismes trop complexes. Ce dont dispose l'ingénieur, ce sont seulement les **séries d'entrée $$u_t$$ et de sortie $$y_t$$** enregistrées après avoir excité le système. Remonter de ces deux signaux à un modèle dynamique devient la clé du passage du contrôle à la pratique industrielle.

### Problème

Les modèles statistiques de séries temporelles (comme l'AR de [Yule](../yule-ar/) ou l'ARMA de Box–Jenkins) décrivent une série unique sans entrée extérieure ; or un système contrôlé possède des **entrées manipulables**. Il faut une classe de modèles capable à la fois d'intégrer des entrées exogènes et d'estimer de façon fiable les paramètres à partir de données bruitées, et qui réponde à trois questions d'ingénieur : **quelle structure de modèle ? quel ordre choisir ? le modèle estimé est-il digne de confiance ?**

### Les autres courants de l'époque (et leurs limites)

- **Modélisation purement physique (boîte blanche)** : dériver les équations des lois de conservation. Le sens physique est clair, mais pour les procédés industriels complexes, on ne parvient souvent pas à écrire les équations, ou les paramètres sont impossibles à mesurer.
- **Identification fréquentielle classique (balayage en fréquence)** : injecter des sinusoïdes dans le système pour mesurer sa réponse en fréquence. Intuitive, mais longue, sensible au bruit et difficile à mener en ligne lorsque la boucle fermée est en fonctionnement.
- **Ajustement ARMA purement statistique** : il ignore les entrées contrôlables et traite tout comme des fluctuations spontanées, perdant la causalité qui intéresse le plus le contrôle : « comment l'entrée influence-t-elle la sortie ? ».

### Méthode

Åström et Ljung combinent estimation statistique et contrôle pour développer l'identification des systèmes (*system identification*). Le modèle central est l'équation aux différences avec entrée exogène, **ARX** :

$$ y_t + a_1 y_{t-1} + \cdots + a_{n_a} y_{t-n_a} = b_1 u_{t-1} + \cdots + b_{n_b} u_{t-n_b} + \varepsilon_t $$

Le modèle plus général **ARMAX** ajoute en outre au bruit un terme de moyenne mobile $$C(q)\varepsilon_t$$. La formulation unificatrice est la méthode de l'erreur de prédiction (PEM) : pour des paramètres $$\theta$$, le modèle fournit une prédiction à un pas $$\hat{y}_t(\theta)$$, d'où l'erreur de prédiction $$\varepsilon_t(\theta)=y_t-\hat{y}_t(\theta)$$, et l'on minimise

$$ \hat{\theta} = \arg\min_{\theta}\; \frac{1}{N}\sum_{t=1}^{N}\varepsilon_t(\theta)^2 $$

Dans le cas ARX, il s'agit simplement de moindres carrés linéaires, avec une solution explicite ; l'ARMAX demande des itérations. Le **choix de l'ordre** s'appuie sur des critères d'information comme l'AIC ou le BIC, qui arbitrent entre qualité d'ajustement et nombre de paramètres ; la **validation du modèle** passe par les tests sur les résidus — si $$\varepsilon_t$$ est proche d'un bruit blanc et décorrélé des entrées passées, le modèle a épuisé la structure prévisible.

### Résultats

Les méthodes d'identification ont permis à des secteurs comme la papeterie, le raffinage ou l'aéronautique d'obtenir des modèles de prévision et de contrôle exploitables sans connaître précisément les mécanismes, avec une mise à jour récursive en ligne (pour suivre des procédés qui évoluent lentement). *System Identification: Theory for the User* de Ljung est devenu le manuel de référence, et la MATLAB System Identification Toolbox qui l'accompagne a industrialisé et popularisé toute la démarche.

### Portée et perspectives

L'identification des systèmes jette un pont entre séries temporelles statistiques et ingénierie du contrôle : elle a fait de « l'estimation d'un modèle dynamique à partir des données » une méthodologie d'ingénieur structurée, avec choix de l'ordre et validation. Erreur de prédiction, validation du modèle, arbitrage contre le surajustement : ces idées partagent la même origine que le paradigme entraînement–validation de l'apprentissage automatique actuel. Elle a directement fourni à la [commande prédictive](../mpc/) de 1980 les modèles sur lesquels repose sa prévision glissante, et se prolonge dans le « contrôle fondé sur les données » et la « modélisation boîte grise » modernes.
