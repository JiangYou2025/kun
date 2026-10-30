---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1999 · Physique"
permalink: /fr/history/e/econophysics/
title: "L'éconophysique (Mantegna · Stanley, 1999)"
lead: "Pourquoi les séries financières ont-elles des queues épaisses et une volatilité en grappes ? Un groupe de physiciens statisticiens a transposé aux marchés les lois d'échelle, les lois de puissance et les phénomènes critiques, en se demandant non pas « comment ajuster », mais « pourquoi cette forme »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prélude · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1990, les bourses commencèrent à conserver des **données haute fréquence, transaction par transaction**, permettant pour la première fois d'observer les prix comme un physicien regarde au microscope. Parallèlement, la physique statistique avait accumulé tout un arsenal d'outils puissants sur les **phénomènes critiques, les lois d'échelle et les fractales** : au voisinage du point critique, des systèmes très différents présentent les mêmes **lois de puissance** et la même **invariance d'échelle** (universalité). Dans *An Introduction to Econophysics* (1999), Mantegna et Stanley relièrent ces deux fils et baptisèrent officiellement l'« **éconophysique (econophysics)** ».

### Problème

La théorie financière classique, représentée par Bachelier et [Black–Scholes](../black-scholes/), suppose que les log-rendements suivent une **loi gaussienne**, indépendants et identiquement distribués. Mais les données s'y refusent obstinément : la distribution des rendements a des **queues épaisses** (les événements extrêmes sont bien plus fréquents que sous la gaussienne), la volatilité se présente en **grappes** (les grandes fluctuations suivent les grandes fluctuations), et ces caractéristiques sont **auto-similaires** d'une échelle de temps à l'autre. L'économétrie dominante « ajustait » le regroupement de la volatilité avec des modèles comme [GARCH](../garch/), mais se demandait rarement : **pourquoi les marchés ont-ils universellement cette allure ?** Les physiciens voulaient des mécanismes et des lois universelles, pas seulement des paramètres.

### Autres courants de l'époque (et leurs limites)

- **Marchés efficients + marche aléatoire gaussienne** : mathématiquement élégante, permettant une valorisation analytique, mais sous-estimant systématiquement le risque de queue ; les krachs de 1987 et 1998 en exposèrent crûment les défauts.
- **École économétrique [GARCH](../garch/)** : décrit avec succès l'hétéroscédasticité conditionnelle, mais reste essentiellement un **ajustement phénoménologique**, sans explication de premier principe à la question « pourquoi l'exposant de la loi de puissance est-il universellement proche d'une certaine valeur ? ».
- **Les lois stables de [Mandelbrot](../mandelbrot/) (1963)** : proposèrent les premières queues épaisses et la fractalité, mais la loi stable de Lévy a une variance infinie, en contradiction avec la variance finie mesurée — l'éconophysique corrigea cet extrême avec des **lois de Lévy tronquées / queues en loi de puissance**.

### Méthode

L'outil central est l'**analyse d'échelle**. Soit le log-rendement $$ r = \ln P_{t+\Delta t} - \ln P_t $$ ; on étudie le comportement d'échelle de sa distribution selon l'échelle de temps $$ \Delta t $$. On constate empiriquement que la queue de la distribution des rendements suit une **loi de puissance inverse** :

$$ P(|r| > x) \sim x^{-\alpha},\qquad \alpha \approx 3 $$

Cette célèbre « **loi cubique inverse (inverse cubic law)** » réapparaît sur de nombreux marchés et actifs, révélant une universalité. La région centrale est proche d'une **loi stable de Lévy**, mais doit être tronquée dans les grandes queues pour garantir une variance finie. Le regroupement de la volatilité correspond à des **corrélations à longue portée** : l'autocorrélation des rendements absolus décroît lentement avec le décalage $$ \tau $$

$$ \langle |r_t|\,|r_{t+\tau}| \rangle - \langle |r| \rangle^2 \sim \tau^{-\gamma},\qquad 0<\gamma<1 $$

Un exposant de décroissance $$ \gamma $$ inférieur à 1 signifie que la somme des corrélations diverge — c'est la signature de la **mémoire longue**, que les modèles AR/GARCH à mémoire courte ne peuvent pas entièrement capter. Plus encore, les séries de prix s'avèrent **multifractales** : différents ordres de moments correspondent à différents exposants d'échelle, et un exposant de Hurst unique (voir [../hurst/]) ne suffit pas à les décrire.

### Résultats

L'éconophysique a systématisé un ensemble de « **faits stylisés (stylized facts)** » robustes : queues épaisses, regroupement de la volatilité, mémoire longue, effet de levier, multifractalité. Ces faits sont devenus la **liste de contrôle** de tout modèle ultérieur de séries temporelles financières — un modèle incapable de reproduire la loi cubique et la mémoire longue de la volatilité est jugé insuffisant. Elle a aussi suscité de nouvelles méthodes pour décrire la structure des marchés, comme les **modèles multi-agents (agent-based models)** ou la **théorie des matrices aléatoires appliquée aux arbres couvrants minimaux et aux matrices de corrélation**.

### Portée et perspectives

Sa véritable contribution est une **manière de questionner** : passer de « comment ajuster » à « pourquoi en est-il ainsi », en considérant le marché comme un système complexe émergeant d'un grand nombre d'agents en interaction, et en expliquant les formes statistiques par des lois universelles. Cette voie mène directement à la [volatilité rugueuse](../rough-volatility/) de 2014 — qui, précisément dans l'esprit de mémoire longue et de lois d'échelle de l'éconophysique, découvrit que l'exposant de Hurst des trajectoires de volatilité vérifie $$ H < \tfrac12 $$. Si puissants que soient aujourd'hui les modèles d'apprentissage profond, ceux qui ne respectent pas ces faits d'échelle trébucheront encore sur le risque de queue. Ce que laisse l'éconophysique n'est pas un modèle particulier, mais l'exigence d'une « intuition physique » des données financières.
