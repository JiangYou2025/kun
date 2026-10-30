---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/gpu/
title: "GPU et calcul parallèle"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)

Le **GPU (processeur graphique)** est une puce conçue à l'origine pour afficher les images des jeux vidéo. Il possède des milliers de petits cœurs et excelle à effectuer **simultanément** un grand nombre d'opérations simples et similaires — comme la [multiplication de matrices](../matrix-multiplication/). C'est précisément la source de puissance de calcul qui permet d'entraîner les modèles profonds.

## Intuition

La différence entre CPU et GPU, c'est « quelques docteurs » contre « mille écoliers » :

- Le **CPU** possède quelques cœurs très puissants, doués pour les tâches complexes aux dépendances séquentielles — comme quelques docteurs : très logiques, capables de résoudre des problèmes difficiles, mais peu nombreux.
- Le **GPU** possède une multitude de cœurs plus modestes, doués pour **répartir une même opération simple et la calculer en même temps** — comme mille écoliers qui font chacun une addition : tout est fini en un instant.

L'opération centrale d'un [réseau de neurones](../neural-network/) est la multiplication et l'addition de matrices, **naturellement décomposables en une myriade de petites multiplications-additions indépendantes**. En les confiant en bloc aux milliers de cœurs du GPU, on va souvent des dizaines à des centaines de fois plus vite qu'avec un CPU. C'est le « **calcul parallèle** » : découper une grande tâche en nombreuses petites tâches exécutables en même temps.

## Points essentiels

- **La condition du parallélisme** : les tâches doivent être **indépendantes les unes des autres**. Le calcul de chaque élément de sortie d'une matrice ne dépend pas des autres, d'où le parallélisme possible ; en revanche, quand chaque étape dépend de la précédente, comme en [programmation dynamique](../dynamic-programming/), il est difficile de paralléliser.
- **La [vectorisation](../vectorization/) est la clé** : pour exploiter le GPU, il faut exprimer les calculs comme des opérations sur des **tableaux / tenseurs entiers**, et non comme des boucles Python. Les échantillons d'un [batch](../batch/) sont empilés dans un grand tenseur et calculés d'un seul coup.
- **La mémoire vidéo (VRAM) est le goulot d'étranglement** : le GPU a sa propre mémoire, où doivent tenir le modèle, les données et les activations intermédiaires. Si elle ne suffit pas, il faut réduire la taille du batch.
- **Déplacer les données a un coût** : les allers-retours entre la mémoire du CPU et la mémoire du GPU sont lents ; il faut les réduire au minimum.

## Un exemple

Avec PyTorch, exécutons la même multiplication de matrices sur le CPU puis sur le GPU :

```python
import torch, time

A = torch.randn(8192, 8192)
B = torch.randn(8192, 8192)

# Sur le CPU
t = time.time()
_ = A @ B
print(f"CPU: {time.time() - t:.3f}s")

# Transfert vers le GPU (s'il y en a un)
if torch.cuda.is_available():
    A_g, B_g = A.cuda(), B.cuda()       # copie en mémoire vidéo
    torch.cuda.synchronize()
    t = time.time()
    _ = A_g @ B_g                       # des milliers de cœurs calculent en parallèle
    torch.cuda.synchronize()            # attendre que le GPU ait vraiment fini avant de chronométrer
    print(f"GPU: {time.time() - t:.3f}s")
```

Typiquement, le GPU est des dizaines de fois plus rapide que le CPU. Notez deux détails : `.cuda()` transfère le tenseur dans la mémoire vidéo ; `synchronize()` est nécessaire parce que les appels au GPU sont **asynchrones** — sans synchronisation, la mesure du temps serait fausse.

{% include fviz/gpu-crossover.html %}

## Intérêt pour la prévision de séries temporelles

Entraîner des modèles comme **KUN / Kernel U-Net** est presque impossible sans GPU :

- Les fenêtres glissantes d'un [batch](../batch/) sont empilées en un tenseur `(batch, pas de temps, variables)` ; convolutions et sous-échantillonnages sont calculés en parallèle sur tout le lot, et le GPU absorbe le tout en une fois.
- Plus les séquences sont longues et le modèle profond, plus le volume de calcul matriciel est important et plus l'accélération apportée par le GPU est nette — un modèle qui demanderait une journée d'entraînement sur CPU peut se boucler en une heure sur GPU.
- Mais pour alimenter le GPU à plein régime, le code doit être **entièrement [vectorisé](../vectorization/)** : utilisez les opérations tensorielles de [NumPy](../numpy/) / PyTorch, et non des boucles `for` Python élément par élément — sinon, la plupart des milliers de cœurs tournent à vide.

## Idées reçues fréquentes

- **Croire que le GPU accélère automatiquement tout** : seules les tâches **parallélisables et intensives en calcul** en profitent. Avec peu de données ou une logique séquentielle à fortes dépendances, le GPU est même plus lent à cause des transferts de données.
- **Ignorer la limite de mémoire vidéo** : un modèle ou un batch trop gros provoque un « CUDA out of memory » ; il faut alors réduire le batch ou recourir à l'accumulation de gradients.
- **Continuer d'écrire des boucles Python** : les boucles s'exécutent sur le CPU pendant que le GPU se tourne les pouces. Il faut exprimer les calculs comme des opérations sur des tenseurs entiers.
- **Chronométrer sans synchroniser** : les appels au GPU rendent la main de façon asynchrone ; pour mesurer une vitesse, appelez d'abord `synchronize()`.

---

[← Fondements de l'informatique](../cs/) · [← Fondements de l'apprentissage profond](../dl/) · [Vue d'ensemble des cours fondamentaux](../)
