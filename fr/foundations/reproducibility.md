---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/reproducibility/
title: "Reproductibilité"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

La **reproductibilité** signifie que, avec le même code et les mêmes données, quelqu'un d'autre (ou vous-même sur une autre machine) peut relancer l'expérience et obtenir **les mêmes résultats**. On l'obtient en fixant les graines aléatoires, en verrouillant l'environnement et en consignant les données ; c'est le minimum exigible de la recherche scientifique et d'une modélisation digne de confiance.

## Intuition

Imaginez que vous publiez une conclusion : « le modèle KUN réduit l'erreur de 10 % ». Si quelqu'un exécute votre code et n'obtient qu'une baisse de 3 %, voire pire, cette conclusion n'est **plus crédible**.

Les causes habituelles de non-reproductibilité sont les nombreux éléments « aléatoires » et « variables cachées » dissimulés dans une expérience :

- l'initialisation aléatoire des poids, le mélange aléatoire des données, la désactivation aléatoire du [Dropout](../dropout/) ;
- des versions différentes des bibliothèques ([NumPy](../numpy/) 1.24 contre 1.26) peuvent produire de légères différences numériques ;
- vous avez changé de lot de données ou modifié un hyperparamètre, mais oublié de le noter.

**La reproductibilité consiste à clouer ces « incertitudes » une à une**, pour que le résultat puisse être refait à l'identique. Ce n'est pas un luxe, c'est une exigence élémentaire de la science.

## Points essentiels

Pour qu'une expérience soit reproductible, il faut maîtriser au moins trois choses :

- **Fixer les graines aléatoires** : donner la même graine à toutes les sources d'aléa (Python, NumPy, PyTorch, CUDA).
- **Verrouiller l'environnement** : consigner la version de [Python](../python/) et les versions exactes de toutes les dépendances (`requirements.txt` / `environment.yml`), idéalement en isolant le tout avec `venv`/`conda`/Docker.
- **Figer les données et leur découpage** : noter la source des données, leur version ou instantané, ainsi que la manière dont elles sont réparties entre entraînement, validation et test (en combinant [Git](../git/) avec un outil de versionnage des données).

Il faut en outre : consigner la **configuration et les hyperparamètres**, noter le **hash du commit** du code et **archiver les résultats**. Tout cela relève des [bonnes pratiques d'ingénierie](../engineering-practice/).

## Un exemple

Un bout de code qui « cloue » les sources d'aléa :

```python
import os, random
import numpy as np
import torch

def set_seed(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # Forcer cuDNN à utiliser des algorithmes déterministes (un peu plus lent, mais reproductible)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
print(np.random.rand(3))     # les trois mêmes nombres à chaque exécution

# Le DataLoader doit lui aussi avoir un ordre de mélange fixé
g = torch.Generator(); g.manual_seed(42)
# loader = DataLoader(ds, batch_size=32, shuffle=True, generator=g)
```

Tant que la graine et l'environnement sont identiques, `np.random.rand(3)` renvoie à chaque fois **exactement** les mêmes nombres : c'est le point de départ de la reproductibilité. En verrouillant en plus les versions des dépendances avec `pip freeze > requirements.txt`, d'autres pourront reproduire vos courbes sur leur propre machine.

## Intérêt pour la prévision de séries temporelles

Dans les recherches sur **KUN / Kernel U-Net**, la reproductibilité décide directement de la solidité des conclusions :

- **Distinguer les vraies améliorations des fausses** : si vous affirmez que le nouveau module de sous-échantillonnage est meilleur, la comparaison doit se faire avec **exactement les mêmes graines, le même découpage des données et les mêmes [métriques d'évaluation](../evaluation-metrics/)** ; sinon, impossible de savoir s'il s'agit d'un vrai progrès ou d'une fluctuation aléatoire. Lancer plusieurs graines et rapporter la moyenne ± l'écart-type est plus convaincant.
- **Empêcher toute fuite d'information** : les données temporelles doivent être découpées en entraînement/test **selon le temps**, avec un point de coupure fixé ; si on les mélange aléatoirement, le modèle « jette un œil » au futur, et les résultats sont gonflés et irreproductibles en situation réelle.
- **Permettre la vérification par les pairs** : publier ensemble le commit, la configuration, les graines et l'environnement, pour qu'un simple clone suffise à tout relancer — c'est le fondement de la crédibilité d'un article.

## En résumé

- Reproductibilité = avec le même code et les mêmes données, obtenir de nouveau les mêmes résultats ; c'est le minimum d'une expérience digne de confiance.
- Trois clous : **fixer les graines aléatoires, verrouiller l'environnement, figer les données et leur découpage**.
- Il faut aussi consigner la configuration et le commit [Git](../git/), et archiver les résultats.
- Pour les séries temporelles, on insiste en plus sur le **découpage selon le temps, sans aucune fuite d'information future** ; moyenner sur plusieurs graines donne des résultats plus robustes.

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
