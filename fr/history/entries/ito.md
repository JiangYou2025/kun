---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1944 · Mathématiques"
permalink: /fr/history/e/ito/
title: "Le calcul différentiel d'un monde aléatoire (Itô, 1944)"
lead: "Les trajectoires du mouvement brownien ne sont dérivables nulle part, et le calcul ordinaire y échoue ; Itô construit une nouvelle règle de dérivation en chaîne, d'où surgit un demi-terme du second ordre — la modélisation stochastique en temps continu a désormais son moteur."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Bachelier en 1900, Einstein en 1905 et Wiener en 1923 ont décrit, chacun sous un angle différent, le **mouvement brownien** : une trajectoire aléatoire continue mais extrêmement irrégulière. On voulait s'en servir pour écrire des « équations différentielles aléatoires » $$dX_t=\mu\,dt+\sigma\,dW_t$$ décrivant des systèmes continus perturbés en permanence par du bruit. Mais la trajectoire brownienne est **continue partout et dérivable nulle part**, et $$dW_t$$ n'est pas une différentielle au sens ordinaire. En 1944, le mathématicien japonais Kiyosi Itô donne l'intégrale stochastique et le calcul qui rendent cette notation rigoureuse.

### Problème

La pierre angulaire du calcul ordinaire est la règle de dérivation en chaîne $$df=f'(x)\,dx$$, qui suppose implicitement que $$(dx)^2$$ est un infiniment petit d'ordre supérieur, négligeable. Mais pour le mouvement brownien, **$$(dW_t)^2$$ n'est pas négligeable** — il vaut $$dt$$ au sens de la moyenne quadratique. Dès lors : comment définir $$\int H_t\,dW_t$$ pour qu'il soit bien posé ? À quoi doit ressembler la différentielle d'une fonction composée $$f(W_t)$$ ? **Quand le terme du second ordre ne disparaît plus, comment réécrire le calcul différentiel ?**

### Les autres courants de l'époque (et leurs limites)

- **Intégrale classique trajectoire par trajectoire (Riemann–Stieltjes)** : on tente d'intégrer directement sur chaque trajectoire. Échec — la variation totale d'une trajectoire brownienne est presque sûrement infinie, et l'intégrale classique ne converge tout simplement pas.
- **Intégrale symétrique de Stratonovich (un peu plus tard)** : évaluation au point milieu ; elle conserve la règle de dérivation en chaîne ordinaire et est géométriquement plus naturelle, mais elle **détruit la propriété de martingale** et l'adaptation causale (« l'intégrande ne dépend que du passé »), ce qui la rend moins nette qu'Itô dans les concepts des probabilités et de la finance.
- **Négliger formellement le terme du second ordre** : les physiciens appliquaient souvent directement les règles classiques. On obtient alors un biais systématique — ce qui manque, c'est précisément le terme correctif $$\tfrac12\sigma^2$$.

### Méthode

Itô définit l'intégrale comme la limite en moyenne quadratique, évaluée à l'extrémité gauche, pour des intégrandes **adaptés, qui ne voient pas l'avenir**, de sorte que $$\int_0^t H_s\,dW_s$$ est une martingale. Son résultat central est le **lemme d'Itô** : si $$dX_t=\mu_t\,dt+\sigma_t\,dW_t$$, alors pour $$f$$ suffisamment régulière,

$$ df(t,X_t)=\Big(f_t+\mu_t f_x+\tfrac12\sigma_t^2 f_{xx}\Big)dt+\sigma_t f_x\,dW_t $$

Par rapport à la règle de dérivation classique, **le terme $$\tfrac12\sigma_t^2 f_{xx}\,dt$$ surgi de nulle part** est exactement la contribution du second ordre due à $$(dW_t)^2=dt$$. En l'appliquant au mouvement brownien géométrique $$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$$ avec $$f=\ln S$$, on obtient la solution explicite

$$ S_t=S_0\exp\!\Big(\big(\mu-\tfrac12\sigma^2\big)t+\sigma W_t\Big) $$

La correction de dérive $$-\tfrac12\sigma^2$$ est la conséquence directe du terme supplémentaire du lemme d'Itô.

### Résultats

Le calcul d'Itô fait des « équations différentielles stochastiques » un outil qu'on peut résoudre rigoureusement et dont on peut calculer les espérances. Propriété de martingale, adaptation et correction du second ordre forment un tout, qui dote l'analyse des processus stochastiques d'un système opératoire équivalent à celui de l'analyse classique. Le mouvement brownien géométrique devient le modèle stochastique standard en temps continu ; l'intégrale d'Itô devient la langue commune de la [formule de Feynman–Kac](../feynman-kac/), du contrôle stochastique et de la théorie du filtrage.

### Portée et perspectives

Ce calcul est le moteur de la modélisation stochastique en temps continu. L'[évaluation d'options de Black–Scholes](../black-scholes/) en 1973 a précisément été obtenue en appliquant le lemme d'Itô au mouvement brownien géométrique — le célèbre terme de diffusion $$\tfrac12\sigma^2 S^2\,\partial_{SS}$$ descend en droite ligne de ce demi-terme du second ordre de 1944. De l'ingénierie financière au filtrage, de la génétique des populations aux modèles génératifs à équations différentielles stochastiques de l'apprentissage automatique (les modèles de diffusion), partout où il y a « temps continu + bruit moteur », c'est la langue d'Itô qui est parlée en profondeur.
