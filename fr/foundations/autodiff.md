---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/autodiff/
title: "Différentiation automatique"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

La **différentiation automatique (automatic differentiation, autodiff)** est la technique par laquelle les frameworks (PyTorch, TensorFlow, JAX) calculent automatiquement et **exactement** les dérivées de n'importe quel graphe de calcul. Vous écrivez seulement le calcul avant, et le framework calcule le [gradient](../gradient/) — plus besoin de dériver à la main. La [rétropropagation](../backpropagation/) n'en est qu'un cas particulier appliqué aux [réseaux de neurones](../neural-network/).

## Intuition

Tout calcul, aussi complexe soit-il, se ramène en fin de compte à un assemblage d'**opérations élémentaires** (addition, multiplication, exponentielle, produit matriciel…). Or la dérivée de chacune de ces opérations est connue depuis longtemps ($\frac{d}{dx}e^x = e^x$, règle du produit pour la multiplication…).

L'idée centrale de la différentiation automatique est toute simple : **puisque la dérivée de chaque petite brique est connue, il suffit de les assembler mécaniquement avec la [règle de dérivation en chaîne](../chain-rule/)**, et la dérivée du graphe entier en découle naturellement. Pendant que vous effectuez le calcul avant, le framework enregistre discrètement chaque opération dans un **graphe de calcul** ; pour obtenir le gradient, il suffit de parcourir ce graphe en sens inverse.

Elle se distingue des deux autres manières de dériver :

- **La différentiation numérique** : approximation par $\frac{f(x+h)-f(x)}{h}$ — elle souffre d'**erreurs d'arrondi** et doit tout recalculer pour chaque paramètre, ce qui la rend bien trop lente pour des millions de paramètres.
- **La différentiation symbolique** : établir la formule de la dérivée comme en cours de mathématiques — les expressions **enflent de manière explosive**.
- **La différentiation automatique** : exacte à la précision machine près, avec une complexité maîtrisée. C'est pourquoi elle l'emporte.

## Principe : deux modes

La différentiation automatique peut se faire dans deux directions :

**Mode direct (forward mode)** : on suit le graphe de calcul dans le sens direct en transportant simultanément l'information de dérivée. Adapté aux cas « peu d'entrées, beaucoup de sorties ».

**Mode inverse (reverse mode)** : on effectue d'abord un passage avant en enregistrant le graphe, puis on propage les dérivées **en partant de la sortie, à rebours**. Adapté aux cas « beaucoup d'entrées, peu de sorties » — or l'[apprentissage profond](../dl/) est précisément le cas « des millions de paramètres en entrée, une perte scalaire en sortie » ; c'est pourquoi tous les frameworks utilisent le mode inverse. **La rétropropagation n'est autre que la différentiation automatique en mode inverse.**

Le cœur du mode inverse reste la règle de dérivation en chaîne. Pour chaque variable intermédiaire $v$ du graphe, le framework maintient l'adjoint

$$
\bar{v} = \frac{\partial \mathcal{L}}{\partial v}
$$

et le propage dans l'ordre topologique inverse : si $v$ influence $u_1, u_2, \dots$, alors

$$
\bar{v} = \sum_{i} \bar{u}_i \, \frac{\partial u_i}{\partial v}
$$

Explication des symboles : $\mathcal{L}$ est la sortie scalaire finale (la perte) ; $\bar v$ indique « de combien varie $\mathcal{L}$ quand $v$ varie un peu » ; $\frac{\partial u_i}{\partial v}$ est la **dérivée locale** d'une seule opération élémentaire (connue). Un seul balayage à rebours suffit à remplir tous les $\bar v$.

{% include fviz/backprop-graph.html %}

## Un exemple concret

Calculons la dérivée de $f(x) = x^2 \cdot \sin(x)$ en $x=2$. À la main, on obtient $f'(x) = 2x\sin x + x^2\cos x$, soit pour $x=2$ : $4\sin2 + 4\cos2 \approx 4(0.909) + 4(-0.416) \approx 1.97$.

Avec la différentiation automatique de PyTorch :

```python
import torch
x = torch.tensor(2.0, requires_grad=True)   # indique qu'il faut suivre le gradient
y = x**2 * torch.sin(x)                       # passage avant : le framework construit le graphe au passage
y.backward()                                  # passage arrière : dérivation automatique
print(x.grad)                                 # tensor(1.9726) —— identique au calcul à la main
```

Nous n'avons **écrit aucune formule de dérivée** : le framework a assemblé automatiquement le résultat à partir des dérivées locales des trois opérations élémentaires `pow`, `sin` et `mul`. Voilà toute la puissance de l'autodiff.

## Pourquoi c'est important / où l'utiliser

- **C'est le moteur des frameworks d'apprentissage profond.** Quel que soit le réseau, aussi complexe soit-il (boucles, branchements, attention…), vous obtenez le gradient automatiquement, sans dérivation manuelle.
- **Elle gère les structures dynamiques.** Un graphe qui change avec la longueur de l'entrée, comme celui d'un [RNN](../rnn/), ne lui pose aucun problème.
- Elle a libéré les chercheurs : pour inventer une nouvelle couche ou une nouvelle [fonction de perte](../loss-function/), **inutile de se soucier de sa dérivée** — ce qui a considérablement accéléré l'innovation en matière de modèles.
- Le gradient obtenu est ensuite transmis à un [optimiseur](../optimizer/) (comme [Adam](../adam/)) qui met à jour les paramètres.

## Idées reçues

- **« autodiff = différentiation numérique »** — non. L'autodiff est **exacte** (à la précision machine près), la différentiation numérique est une approximation.
- **« autodiff = différentiation symbolique »** — non. Elle ne produit pas d'immenses formules de dérivées : elle propage numériquement les dérivées le long du graphe.
- **« La rétropropagation et l'autodiff sont deux choses distinctes »** — la rétropropagation est l'application concrète de l'autodiff (en mode inverse) aux réseaux de neurones ; les deux relèvent d'une même filiation.

[← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
