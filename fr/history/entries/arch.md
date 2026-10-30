---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1982 · Informatique"
permalink: /fr/history/e/arch/
title: "Le modèle ARCH (Engle, 1982)"
lead: "Sur les marchés financiers, les « tempêtes » arrivent en grappes : le calme suit le calme, l'agitation suit l'agitation. Engle laisse la variance fluctuer d'elle-même au fil du temps et inscrit ainsi le « regroupement de la volatilité » dans le modèle."
math: true
---

> Cette entrée fait partie de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 6 · Volatilité et cointégration](../../06/).

### Contexte

Les séries temporelles classiques (l'AR de [Yule](../yule-ar/), l'ARMA de Box–Jenkins) se concentrent sur l'**espérance conditionnelle** de la série : quelle sera, à peu près, la prochaine valeur ? Elles supposent par défaut que le terme d'erreur est **homoscédastique** — que l'amplitude des fluctuations reste constante. C'est souvent suffisant, mais les données financières s'y refusent manifestement : la volatilité quotidienne des rendements boursiers tantôt enfle, tantôt retombe, et elle se **regroupe** (*clustering*) — les fortes hausses et les fortes baisses s'enchaînent, et les périodes calmes viennent elles aussi par blocs. Le risque se cache précisément dans cette variance changeante, que les modèles classiques ignorent.

### Problème

La série des rendements est elle-même presque sans autocorrélation (sa moyenne est difficile à prévoir), mais son **carré** (ou sa valeur absolue) est fortement autocorrélé — si la volatilité est forte aujourd'hui, elle le sera probablement encore demain. Cela montre que **la variance conditionnelle varie dans le temps et qu'elle est prévisible**. Comment faire de la variance une fonction du passé plutôt qu'une constante fixe, tout en gardant un modèle estimable ?

### Autres courants de l'époque (et leurs limites)

- **ARMA homoscédastique** : suppose une variance d'erreur constante. Il modélise bien la moyenne, mais sous-estime systématiquement le risque dans les périodes agitées et le surestime dans les périodes calmes.
- **Estimation de la variance sur fenêtre glissante** : on prend la variance empirique des dernières périodes comme volatilité courante. C'est simple, mais la longueur de la fenêtre est entièrement arbitraire, et les observations anciennes au bord de la fenêtre sont oubliées « d'un coup ».
- **Approche de la volatilité stochastique (SV)** : la variance suit elle-même un processus latent. Flexible en théorie, mais à l'époque les modèles à variables latentes étaient difficiles à estimer et aucune méthode de maximum de vraisemblance clé en main n'existait.

### Méthode

Engle propose le modèle autorégressif conditionnellement hétéroscédastique (ARCH). On pose le résidu $$\varepsilon_t = \sigma_t z_t$$, où $$z_t$$ est un bruit standard indépendant et identiquement distribué, de moyenne 0 et de variance 1, tandis que la **variance conditionnelle** $$\sigma_t^2$$ est déterminée par les carrés des résidus passés :

$$ \sigma_t^2 = \alpha_0 + \sum_{i=1}^{q}\alpha_i\,\varepsilon_{t-i}^2,\qquad \alpha_0>0,\;\alpha_i\ge 0 $$

L'interprétation est intuitive : si un choc important s'est produit à la période précédente ($$\varepsilon_{t-i}^2$$ grand), la variance de la période courante est poussée à la hausse — le **regroupement de la volatilité** en découle naturellement. Les contraintes $$\alpha_0>0,\alpha_i\ge0$$ garantissent que la variance reste toujours positive. Sous les hypothèses du modèle, étant donné l'information passée $$\mathcal{F}_{t-1}$$, on a

$$ \varepsilon_t \mid \mathcal{F}_{t-1} \sim \mathcal{N}\!\big(0,\ \sigma_t^2\big) $$

Le modèle tout entier peut donc être estimé par **maximum de vraisemblance** — c'est précisément ce qui le rend plus facile à mettre en œuvre que la volatilité stochastique. La somme $$\sum_i \alpha_i$$ mesure la persistance des chocs de volatilité.

### Résultats

ARCH a été le premier modèle statistique à rendre l'idée que « la variance bouge » estimable, testable et prévisible ; il décrit la volatilité de l'inflation et des rendements financiers bien mieux que les modèles homoscédastiques. Il a ouvert tout un programme de recherche sur la modélisation de la volatilité et fourni une base aux mesures de risque (comme la VaR). Engle a reçu pour ARCH le prix Nobel d'économie 2003.

### Portée et perspectives

ARCH a élargi le centre de gravité de la modélisation de la « prévision de la moyenne » à la « **prévision du risque** », et fait de la variance conditionnelle un objet d'étude de premier plan. Sa limite immédiate : pour décrire une persistance de la volatilité à longue mémoire, il faut souvent un ordre $$q$$ très élevé et trop de paramètres. Ce défaut a été élégamment corrigé quatre ans plus tard par le [GARCH de Bollerslev](../garch/), qui ajoute à la variance ses propres retards. D'ARCH sont nés EGARCH, GJR, la volatilité stochastique, la volatilité réalisée et jusqu'aux modèles de volatilité à réseaux de neurones d'aujourd'hui : la modélisation de la volatilité est restée le champ de bataille central des séries temporelles financières.
