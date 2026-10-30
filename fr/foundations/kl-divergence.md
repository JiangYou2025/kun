---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/kl-divergence/
title: "La divergence KL"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

La divergence KL (divergence de Kullback–Leibler) mesure le coût supplémentaire (la perte d'information) que l'on paie en « **approchant la vraie distribution $p$ par une distribution $q$** ». Elle est toujours positive ou nulle, et **asymétrique** — échanger les deux distributions change le résultat.

## Intuition

Supposons que la réalité suive une distribution $p$, mais que vous ne disposiez que d'un modèle approché $q$. Si vous concevez vos codes et prenez vos décisions d'après $q$ alors que le monde fonctionne selon $p$, vous **gaspillez** des bits — et la quantité gaspillée, c'est la divergence KL.

- Plus $q$ est proche de $p$, moins on gaspille, et plus la KL est proche de 0 ;
- quand $q=p$, il n'y a aucun gaspillage : KL = 0 ;
- plus $q$ s'écarte de $p$, plus la KL est grande.

On peut la lire comme une « **distance informationnelle de $p$ à $q$** », mais attention : ce n'est pas une vraie distance (elle est asymétrique et ne vérifie pas l'inégalité triangulaire).

## Formulation mathématique

Forme discrète :

$$
D_{\mathrm{KL}}(p\parallel q)=\sum_i p_i\log\frac{p_i}{q_i}
$$

- $p_i$ — probabilité selon la vraie distribution (le poids, qui détermine quels événements « comptent ») ;
- $q_i$ — probabilité selon la distribution approchée ;
- $\log\dfrac{p_i}{q_i}$ — l'écart de $q$ par rapport à $p$ sur l'événement $i$.

Son lien avec l'[entropie](../entropy/) et l'[entropie croisée](../cross-entropy/) est essentiel :

$$
D_{\mathrm{KL}}(p\parallel q)=\underbrace{-\sum_i p_i\log q_i}_{\text{entropie croisée }H(p,q)}-\underbrace{\Big(-\sum_i p_i\log p_i\Big)}_{\text{entropie }H(p)}=H(p,q)-H(p)
$$

Autrement dit, **divergence KL = entropie croisée − entropie**. Comme $H(p)$ est une constante, minimiser l'entropie croisée pendant l'entraînement revient à minimiser la divergence KL.

Deux propriétés clés :

- **Positivité** : $D_{\mathrm{KL}}(p\parallel q)\ge 0$, avec égalité si et seulement si $p=q$ (inégalité de Gibbs).
- **Asymétrie** : $D_{\mathrm{KL}}(p\parallel q)\ne D_{\mathrm{KL}}(q\parallel p)$.

{% include fviz/kl-asym.html %}

## Un exemple concret

Vraie distribution $p=[0.5,0.5]$, approximation $q=[0.9,0.1]$ (logarithme en base 2) :

$$
D_{\mathrm{KL}}(p\parallel q)=0.5\log_2\frac{0.5}{0.9}+0.5\log_2\frac{0.5}{0.1}\approx 0.5(-0.848)+0.5(2.322)\approx 0.737
$$

Dans l'autre sens, $D_{\mathrm{KL}}(q\parallel p)\approx 0.531$ : **les deux valeurs diffèrent**, ce qui illustre concrètement l'asymétrie.

```python
import numpy as np
def kl(p, q):
    p, q = np.array(p), np.array(q)
    return np.sum(p * np.log2(p / q))
print(round(kl([0.5, 0.5], [0.9, 0.1]), 3))  # 0.737
print(round(kl([0.9, 0.1], [0.5, 0.5]), 3))  # 0.531  ≠ la valeur ci-dessus
```

## Pourquoi c'est important / où l'utilise-t-on

- **Auto-encodeur variationnel (VAE)** : la [perte](../loss-function/) comporte un terme KL qui maintient la distribution des variables latentes près d'une loi normale standard.
- **Inférence variationnelle** : on approche une loi a posteriori complexe par une $q$ calculable, l'objectif étant de minimiser la KL.
- **Distillation de modèles, [apprentissage par renforcement](../reinforcement-learning/) (par ex. PPO)** : la KL empêche la nouvelle politique / distribution de trop s'écarter de l'ancienne.
- C'est la grandeur « réellement » optimisée derrière la perte d'[entropie croisée](../cross-entropy/).

## Signification pour la prévision de séries temporelles

- En prévision probabiliste, la divergence KL mesure l'écart entre la « **distribution future prédite** » et la « **distribution réelle** ».
- Détection de **dérive de distribution** (concept drift) : si la KL entre la distribution des données d'entraînement et celle observée en production augmente, il est temps de réentraîner le modèle.
- Si KUN (Kernel U-Net) produit des prévisions sous forme de probabilités ou de quantiles, son objectif d'entraînement peut s'écrire comme la minimisation de la KL entre la distribution prédite et la vraie distribution.

## Erreurs fréquentes

- **Ce n'est pas une distance** : elle est asymétrique et ne vérifie pas l'inégalité triangulaire, ne l'utilisez donc pas comme une distance euclidienne ; si vous avez besoin d'une version symétrique, prenez la divergence de Jensen-Shannon (JS).
- Lorsqu'un $q_i=0$ alors que $p_i>0$, la KL devient infinie — en pratique, il faut lisser ou écrêter $q$.
- Le sens compte : $D_{\mathrm{KL}}(p\parallel q)$ (directe, qui « couvre » la vérité) et $D_{\mathrm{KL}}(q\parallel p)$ (inverse, qui se « concentre » sur le mode) se comportent différemment ; un mauvais choix dégrade la qualité de l'approximation.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
