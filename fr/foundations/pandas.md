---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/pandas/
title: "Pandas"
no_comments: true
---

> Extrait des [Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)

**Pandas** est la bibliothèque de référence de [Python](../python/) pour les **données tabulaires**. Elle repose sur le `DataFrame` (un tableau à deux dimensions avec des étiquettes de lignes et de colonnes) et la `Series` (une séquence à une dimension munie d'un index). Pour les séries temporelles, son point fort est l'alignement, le rééchantillonnage et le traitement des valeurs manquantes **à partir d'un index temporel**.

## Intuition

On peut voir un `DataFrame` comme « un tableur Excel programmable » :

- Chaque colonne est une `Series`, adossée à un tableau [NumPy](../numpy/) : les calculs sont donc rapides et [vectorisés](../vectorization/).
- Chaque ligne et chaque colonne porte une **étiquette (un index)**. C'est là que Pandas surpasse NumPy brut : il **aligne automatiquement selon les étiquettes**. Si l'on additionne deux séries dont les dates de début et de fin diffèrent, Pandas les aligne d'office sur les horodatages et place `NaN` là où elles ne se recouvrent pas, au lieu de les additionner bêtement position par position.

Pour une série temporelle, une fois les horodatages placés en index, « extraire les données d'une semaine », « agréger par mois » ou « combler les heures manquantes » ne demande plus qu'une ou deux lignes de code.

## Points essentiels

- **DataFrame / Series** : tableau / séquence étiquetés.
- **DatetimeIndex** : un index d'horodatages, qui débloque toutes les fonctionnalités temporelles.
- **Sélection** : `df["col"]` pour une colonne, `df.loc[étiquette]` pour sélectionner par étiquette, `df.iloc[position]` par position.
- **Rééchantillonnage `resample`** : changer la fréquence temporelle, par exemple agréger des données à la minute en données horaires (sous-échantillonnage) ou interpoler vers une fréquence plus fine (suréchantillonnage).
- **Fenêtres glissantes `rolling`** : moyenne mobile, écart-type glissant, etc.
- **Valeurs manquantes** : `isna` / `fillna` / `interpolate` / `dropna`.
- **Agrégation par groupe `groupby`** : regrouper par catégorie, puis calculer des statistiques.

## Un exemple

Un prétraitement typique de série temporelle :

```python
import pandas as pd
import numpy as np

# Construire une série horaire en omettant volontairement quelques points
idx = pd.date_range("2026-01-01", periods=8, freq="h")
s = pd.Series([10, 11, np.nan, 13, 14, np.nan, 16, 17], index=idx)

# 1) Combler les trous par interpolation linéaire
s = s.interpolate()

# 2) Moyenne glissante (fenêtre = 3) pour lisser le bruit
s_smooth = s.rolling(window=3, min_periods=1).mean()

# 3) Rééchantillonnage : horaire → somme journalière
daily = s.resample("D").sum()

print(s_smooth.round(2))
print(daily)
```

Si `interpolate()` interpole correctement, c'est justement parce que l'index est temporel : Pandas sait combien de temps sépare deux points.

La magie de l'alignement temporel :

```python
a = pd.Series([1, 2, 3], index=pd.date_range("2026-01-01", periods=3))
b = pd.Series([10, 20], index=pd.date_range("2026-01-02", periods=2))
print(a + b)
# 2026-01-01     NaN   ← b n'a pas ce jour
# 2026-01-02    12.0   ← 2 + 10, aligné automatiquement sur la date
# 2026-01-03    23.0   ← 3 + 20
```

{% include fviz/resample.html %}

## Intérêt pour la prévision de séries temporelles

Les données fournies à **KUN / Kernel U-Net** passent presque toutes d'abord par Pandas :

- **Aligner plusieurs séries** : capteurs ou actions différents n'ont pas les mêmes instants d'échantillonnage ; l'index temporel les aligne automatiquement en un tableau propre.
- **Rééchantillonner à une fréquence commune** : les modèles exigent généralement des entrées équidistantes ; `resample` régularise les fréquences disparates.
- **Construire des variables temporelles** : en une ligne, on extrait du `DatetimeIndex` l'heure, le jour de la semaine, le caractère férié ou non, etc., comme variables supplémentaires.
- **Séparer entraînement et test** : découper **dans l'ordre chronologique** avec par exemple `df.loc["2020":"2023"]`, pour éviter qu'un mélange aléatoire ne laisse fuiter de l'information future.
- **Convertir en NumPy après traitement** : `df.values` ou `.to_numpy()` pour passer les données au modèle sous forme de tenseurs.

## Erreurs fréquentes

- **Utiliser les fonctions temporelles sans index temporel** : la sémantique temporelle de `resample` / `rolling` repose sur un `DatetimeIndex`.
- **Tomber sur `SettingWithCopyWarning` avec une affectation chaînée** : pour modifier un sous-ensemble, utilisez `df.loc[...] = ...`, pas `df[...][...] = ...`.
- **Faire des `apply` / boucles ligne par ligne sur de grands tableaux** : c'est lent. Préférez les opérations vectorisées sur les colonnes ou `groupby`.
- **Mélanger les données lors du découpage temporel** : entraînement et test doivent être séparés selon l'ordre chronologique ; un ordre aléatoire permet au modèle de « regarder le futur ».

---

[← Fondements de l'informatique](../cs/) · [Vue d'ensemble des cours fondamentaux](../)
