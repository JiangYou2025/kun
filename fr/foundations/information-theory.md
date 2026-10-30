---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/information-theory/
title: "La théorie de l'information"
no_comments: true
math: true
---

> Extrait de [Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)

La théorie de l'information quantifie la « quantité d'information » et l'« incertitude » au moyen de notions comme l'**entropie**, et en déduit des limites théoriques : « combien de bits faut-il au minimum pour décrire un événement » et « jusqu'où pouvons-nous prédire ». Elle a été fondée par Shannon en 1948.

## Intuition

L'idée centrale de la théorie de l'information : **information = réduction de l'incertitude**.

- Un message que vous connaissiez déjà (« demain, le soleil se lèvera ») ne contient presque aucune information ;
- un message inattendu (« demain, il neigera à tel endroit, alors que la probabilité n'était que de 1 % ») en contient beaucoup.

On en tire une manière de quantifier : **plus un événement est improbable, plus il apporte d'information lorsqu'il se produit**. La théorie de l'information transforme cette intuition simple en mathématiques précises, ce qui permet de « peser » l'information, de concevoir la compression et les communications, et de définir les [pertes](../loss-function/) de l'[apprentissage automatique](../ml/).

## Formulation mathématique

**Information propre** (quantité d'information d'un seul événement) :

$$
I(x)=-\log p(x)
$$

Plus la probabilité est faible, plus $-\log p$ est grand, et plus l'information est importante.

**[Entropie](../entropy/)** (incertitude moyenne d'une distribution, c'est-à-dire l'espérance de l'information propre) :

$$
H(X)=-\sum_i p_i\log p_i
$$

**[Entropie croisée](../cross-entropy/)** (coût moyen de la description de la vraie distribution $p$ à l'aide de la distribution $q$) :

$$
H(p,q)=-\sum_i p_i\log q_i
$$

**[Divergence KL](../kl-divergence/)** (écart entre deux distributions / coût supplémentaire) :

$$
D_{\mathrm{KL}}(p\parallel q)=\sum_i p_i\log\frac{p_i}{q_i}=H(p,q)-H(p)
$$

**Information mutuelle** (quantité d'information partagée par deux variables) :

$$
I(X;Y)=H(X)-H(X\mid Y)
$$

Ces quantités s'emboîtent les unes dans les autres : l'entropie est la base, entropie croisée = entropie + divergence KL, et l'information mutuelle mesure « de combien la connaissance de $Y$ réduit l'incertitude sur $X$ ».

{% include fviz/cross-entropy.html %}

## Un exemple concret

Une source de 4 lettres $\{A,B,C,D\}$ a pour probabilités $[0.5,0.25,0.125,0.125]$. Son entropie vaut :

$$
H=-(0.5\log_2 0.5+0.25\log_2 0.25+2\times 0.125\log_2 0.125)=1.75\ \text{bits}
$$

Autrement dit, **il faut au minimum 1,75 bit par lettre en moyenne** pour un codage sans perte. Le codage de Huffman y parvient exactement (A→0, B→10, C→110, D→111, de longueur moyenne précisément 1,75) et atteint ainsi la borne théorique fixée par l'entropie.

```python
import numpy as np
p = np.array([0.5, 0.25, 0.125, 0.125])
H = -np.sum(p * np.log2(p))
print(H)   # 1.75
```

## Pourquoi c'est important / où l'utilise-t-on

- **Fonctions de perte** : l'[entropie croisée](../cross-entropy/) pour la classification, la [divergence KL](../kl-divergence/) pour les modèles génératifs et l'inférence variationnelle — toutes deux issues de la théorie de l'information.
- **Sélection de variables** : l'information mutuelle mesure le lien entre une variable et l'étiquette, de façon plus générale que la corrélation linéaire.
- **Compression et communication** : l'entropie donne la limite de la compression sans perte, et le théorème de capacité du canal la borne supérieure d'une transmission fiable.

## Signification pour la prévision de séries temporelles

- La théorie de l'information fournit une **borne théorique de prévisibilité** : plus l'entropie d'une série est élevée (plus elle est proche de l'aléatoire), plus l'erreur de prévision de tout modèle est bornée inférieurement par une limite infranchissable.
- L'information mutuelle permet d'évaluer « quelle valeur prédictive la fenêtre historique a réellement pour le futur », ce qui guide le choix de la longueur de fenêtre et la conception des variables.
- Si KUN (Kernel U-Net) produit des sorties probabilistes ou de type classification, sa perte d'entraînement (entropie croisée, KL) est par nature une grandeur de la théorie de l'information ; la comprendre vous aide à savoir si une « perte qui ne baisse plus » vient d'un modèle insuffisant ou de données intrinsèquement trop aléatoires.

## En résumé

- Information = réduction de l'incertitude ; les événements rares portent beaucoup d'information.
- Entropie → entropie croisée → divergence KL → information mutuelle : une seule et même lignée.
- Elle fixe les limites théoriques de la compression et de la communication, et fonde les fonctions de perte de l'apprentissage automatique ainsi que l'analyse de la prévisibilité.

[← Fondements mathématiques](../math/) · [Vue d'ensemble des cours de base](../)
