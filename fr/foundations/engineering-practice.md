---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/engineering-practice/
title: "Pratiques d'ingénierie"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

Les **pratiques d'ingénierie** désignent un ensemble d'habitudes de travail qui rendent le code **collaboratif, reproductible et maintenable** — gestion de versions, graines aléatoires fixées, environnements isolés, tests, etc. Elles ne changent rien au modèle lui-même, mais déterminent si vos travaux pourront être crus et réutilisés par d'autres (et par vous-même, six mois plus tard).

## Intuition

Imaginez que mener des expériences d'[apprentissage automatique](../ml/), c'est tenir une cuisine :

- Sans pratiques d'ingénierie = cuisiner au feeling. Aujourd'hui c'est délicieux, demain impossible de retrouver le goût, parce que vous ne vous rappelez plus combien de sel vous avez mis (la graine aléatoire), quel lot d'ingrédients vous avez utilisé (la version des données), ni sur quelle cuisinière (les versions des dépendances).
- Avec des pratiques d'ingénierie = une recette standardisée. Quantités, cuisson et lots d'ingrédients sont consignés : **un autre cuisinier, dans une autre cuisine, peut préparer exactement le même plat**.

L'un des plus grands maux de la recherche et de l'industrie, c'est que « **les autres n'arrivent pas à reproduire mes résultats** », voire que « **je n'arrive pas moi-même à reproduire mes résultats du mois dernier** ». Les pratiques d'ingénierie sont là pour guérir ce mal à la racine.

## Points essentiels

Les habitudes les plus importantes à prendre :

- **Gestion de versions** : enregistrer chaque modification avec [Git](../git/), pour pouvoir revenir en arrière, comparer et collaborer à plusieurs.
- **[Reproductibilité](../reproducibility/)** : fixer les graines aléatoires, figer les versions des dépendances, conserver des instantanés des données.
- **Isolation de l'environnement** : enfermer les dépendances du projet dans un environnement dédié avec `venv` / `conda` / Docker, pour éviter le « ça marche sur ma machine ».
- **Séparer configuration et code** : mettre hyperparamètres et chemins dans un fichier de configuration, plutôt que de les coder en dur un peu partout.
- **Écrire des tests et des assertions** : des tests unitaires pour les fonctions clés, des `assert` pour les hypothèses clés, afin que les bugs se manifestent tôt.
- **Des journaux plutôt que des print** : journaliser par niveaux avec `logging`, pour que les expériences restent traçables.

## Un exemple

Voici à quoi ressemble une ossature d'expérience « industrialisée » :

```python
import logging, random, json
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")

def set_seed(seed: int = 42):
    """Fixer toutes les sources d'aléa pour garantir la reproductibilité"""
    random.seed(seed)
    np.random.seed(seed)
    # avec torch : torch.manual_seed(seed)

# séparer configuration et code
config = {"seed": 42, "lookback": 96, "horizon": 24, "lr": 1e-3}

def main(cfg):
    set_seed(cfg["seed"])
    logging.info("Début de l'expérience, configuration : %s", cfg)
    assert cfg["horizon"] > 0, "L'horizon de prévision doit être positif"   # vérification explicite d'une hypothèse clé
    # ... charger les données, entraîner, évaluer ...
    metrics = {"mae": 0.123}
    # archiver configuration et résultats ensemble, pour pouvoir comparer plus tard
    with open("run.json", "w", encoding="utf-8") as f:
        json.dump({"config": cfg, "metrics": metrics}, f, ensure_ascii=False, indent=2)
    logging.info("Terminé, métriques : %s", metrics)

if __name__ == "__main__":
    main(config)
```

L'essentiel n'est pas la quantité de code, mais le fait que **chaque expérience puisse être rejouée à l'identique à partir de son archive**.

## Intérêt pour la prévision de séries temporelles

Pour entraîner des modèles comme **KUN / Kernel U-Net**, les pratiques d'ingénierie sont particulièrement importantes :

- **Des résultats comparables** : si l'on change l'architecture pour voir si elle est meilleure, il faut garantir que graines, découpage des données et [métriques d'évaluation](../evaluation-metrics/) sont strictement identiques ; sinon, impossible de distinguer une « vraie amélioration » d'une « fluctuation aléatoire ».
- **La discipline du découpage des données** : les séries temporelles doivent être divisées en entraînement/validation/test **selon le temps**, jamais mélangées au hasard, sous peine de « fuite d'information du futur ». Ce sont les règles d'ingénierie qui garantissent cette discipline.
- **Des expériences longues qu'on peut reprendre** : un modèle qui s'entraîne pendant des heures doit sauvegarder régulièrement des checkpoints, pour pouvoir reprendre en cas de plantage.
- **Articles / reproduction** : consigner ensemble le commit [Git](../git/), la configuration et l'environnement, pour que d'autres puissent reproduire vos courbes simplement après un clone.

## Résumé

- Pratiques d'ingénierie = l'ensemble des habitudes qui rendent le code collaboratif, reproductible et maintenable.
- Trois piliers : **[gestion de versions](../git/), [reproductibilité](../reproducibility/), isolation de l'environnement**.
- Elles n'augmentent pas la précision du modèle, mais **garantissent que votre précision est crédible et reproductible**.
- Pour les séries temporelles s'ajoute une règle d'or : **découper strictement les données selon le temps, pour éliminer toute fuite d'information.**

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
