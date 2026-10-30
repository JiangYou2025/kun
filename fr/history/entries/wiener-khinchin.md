---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1934 · Mathématiques"
permalink: /fr/history/e/wiener-khinchin/
title: "La dualité entre autocorrélation et spectre de puissance (Khinchin, 1934)"
lead: "Un signal aléatoire n'a pas de transformée de Fourier — son énergie est infinie. Khinchin contourne l'obstacle : au lieu de transformer le signal lui-même, il transforme son autocovariance, et « corrélation » et « spectre » deviennent les deux faces d'une même pièce."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

La [transformée de Fourier](../fourier/) décompose un signal déterministe en fréquences, mais elle exige un signal intégrable (d'énergie finie). Un **processus aléatoire stationnaire** (bruit thermique, houle, taches solaires) fluctue indéfiniment ; ses trajectoires ne s'amortissent pas et ne sont pas périodiques, et la transformée de Fourier ordinaire diverge, impossible à définir. Pourtant, les ingénieurs mesurent bel et bien le « spectre de puissance » d'un bruit — l'énergie se concentre davantage dans certaines bandes de fréquences. En 1934, Aleksandr Khinchin (s'appuyant sur les travaux d'analyse harmonique généralisée de Norbert Wiener de 1930) établit le pont rigoureux connu sous le nom de **théorème de Wiener–Khinchin**.

### Problème

Un processus stationnaire n'a pas de transformée de Fourier convergente : **le « spectre de puissance » est donc la transformée de Fourier de quoi, au juste ? Comment définir rigoureusement le contenu fréquentiel d'un signal stationnaire ?** Transformer directement des trajectoires aléatoires ne fonctionne pas ; il faut trouver un objet qui représente le processus tout en étant assez « docile » pour être transformé.

### Les autres courants de l'époque (et leurs limites)

- **Estimation directe du spectre par le périodogramme** : on applique la transformée de Fourier à un échantillon et l'on prend le carré du module comme spectre. C'est une quantité empirique définie sur un échantillon fini, mais **non convergente** — sa variance ne diminue pas quand l'échantillon s'allonge, l'estimation reste toujours très agitée, et la théorie esquive la difficulté de fond : « un signal aléatoire n'a pas de transformée de Fourier ».
- **Décomposition harmonique déterministe (école de [Fourier](../fourier/))** : on suppose le signal somme d'un petit nombre de sinusoïdes fixes. Pour un signal purement aléatoire à spectre continu, cette recherche de « quelques raies spectrales » déforme systématiquement la réalité.
- Le nœud du problème : on cherchait à transformer directement le **signal**, alors qu'un signal aléatoire stationnaire n'est pas transformable en lui-même.

### Méthode

L'idée centrale de Khinchin : **ne pas transformer le signal, mais sa fonction d'autocovariance**. L'autocovariance d'un processus stationnaire

$$ \gamma(\tau)=\mathbb E\big[(X_t-\mu)(X_{t+\tau}-\mu)\big] $$

est une fonction déterministe, bien intégrable. Le théorème affirme que l'autocovariance $$\gamma(\tau)$$ et la **densité spectrale de puissance** $$S(\omega)$$ forment une paire de transformées de Fourier :

$$ S(\omega)=\int_{-\infty}^{\infty}\gamma(\tau)\,e^{-i\omega\tau}\,d\tau,\qquad \gamma(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S(\omega)\,e^{i\omega\tau}\,d\omega $$

Ainsi $$S(\omega)\ge 0$$ décrit la répartition de la puissance entre les fréquences, et $$\gamma(0)=\frac1{2\pi}\int S(\omega)\,d\omega$$ est précisément la variance totale (la puissance totale) du processus. « La structure de corrélation dans le domaine temporel » et « la répartition de l'énergie dans le domaine fréquentiel » se révèlent parfaitement équivalentes, traduisibles l'une dans l'autre de façon réversible.

### Résultats

Le spectre de puissance reçoit dès lors une définition mathématique sans ambiguïté, et l'analyse spectrale un fondement solide. Le théorème explique aussi pourquoi le périodogramme naïf n'est pas fiable, et inspire des méthodes d'estimation spectrale **convergentes** comme le lissage par fenêtres ou la méthode de Blackman–Tukey. Tout processus stationnaire peut être étudié de façon équivalente dans le domaine temporel (autocorrélation) ou fréquentiel (spectre de puissance), en passant de l'un à l'autre selon les besoins.

### Portée et perspectives

Le théorème de Wiener–Khinchin est le lien essentiel entre le [domaine fréquentiel de Fourier](../fourier/) et les [processus aléatoires de Kolmogorov](../kolmogorov/), la pierre angulaire de toutes les méthodes spectrales. C'est grâce à lui que les modèles [AR/ARMA](../yule-ar/) laissent lire des pics spectraux (résonances) dans le domaine fréquentiel ; il sous-tend aussi le filtrage de Wiener, la prédiction optimale et l'analyse du bruit en océanographie et en télécommunications. La dualité « autocorrélation $$\leftrightarrow$$ spectre de puissance » enseignée aujourd'hui en cours de traitement du signal, et jusqu'à l'usage des caractéristiques spectrales des séquences dans les modèles profonds, prolongent directement ce théorème de 1934.
