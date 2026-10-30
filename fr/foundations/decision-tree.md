---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/foundations/decision-tree/
title: "Arbre de décision"
no_comments: true
math: true
---

> Extrait des [Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)

Un **arbre de décision (decision tree)** est un modèle constitué d'une suite de tests « oui/non » (des divisions de type if-else) : il découpe l'espace des variables, coup après coup, en plusieurs régions, et chaque région fournit une prédiction. Intuitif et facile à interpréter, il est surtout la brique de base de modèles puissants comme les [forêts aléatoires](../model-families/) et le [GBDT](../ensemble-gbdt/).

## Intuition

Imaginez que vous jouiez aux « vingt questions » pour deviner un objet : on demande d'abord « Est-ce que ça bouge ? », puis « Est-ce plus grand qu'un chat ? »… Chaque question élimine la moitié des possibilités, et quelques tours suffisent pour trouver la réponse. C'est exactement ce que fait un arbre de décision — **décomposer un problème de prédiction complexe en un organigramme (flowchart) de tests simples**.

Prenons l'exemple « Est-ce un bon jour pour aller courir dehors ? » :

```
Température > 32℃ ?
├── Oui → Pas de course (trop chaud)
└── Non → Pleut-il ?
         ├── Oui → Pas de course
         └── Non → Vent > 8m/s ?
                  ├── Oui → Pas de course
                  └── Non → On va courir !
```

- Chaque **nœud interne (internal node)** est un test portant sur une variable (par exemple `température > 32`).
- Chaque branche correspond à une issue du test (oui / non).
- Chaque **feuille (leaf)** donne la prédiction finale.

L'arbre entier découpe ainsi l'espace des variables en « régions rectangulaires », et tous les échantillons tombant dans une même région partagent la même prédiction. Cette structure ressemble beaucoup à la façon dont le cerveau humain prend des décisions ; elle est donc **particulièrement facile à expliquer** — on peut retracer, chemin par chemin, « pourquoi le modèle a décidé ainsi ».

## Principe : la division binaire récursive

Comment l'arbre « pousse »-t-il ? Le cœur du mécanisme est la **division binaire récursive (recursive binary splitting)** :

1. Considérer tous les échantillons du nœud courant, parcourir chaque variable et chaque point de coupure possible.
2. Choisir la coupure qui rend les nœuds enfants « les plus purs » et partager les données en deux.
3. Répéter le processus pour chaque nœud enfant jusqu'à ce qu'une condition d'arrêt soit remplie (nœud suffisamment pur, trop peu d'échantillons, ou profondeur maximale atteinte).

Tout se joue à l'étape 2 — **comment mesurer qu'une division est « bonne » ?** Cela dépend du type de tâche.

**Classification** : on veut qu'après la division, chaque nœud enfant soit aussi « pur » que possible (une classe largement majoritaire). Deux critères sont couramment utilisés.

**Impureté de Gini (Gini impurity)** : la probabilité de se tromper si l'on tire un échantillon au hasard et qu'on devine sa classe au hasard selon les proportions des classes dans le nœud.

$$Gini = 1 - \sum_k p_k^2$$

où $p_k$ est la proportion de la classe $k$ dans le nœud. Lorsqu'un nœud ne contient qu'une seule classe, $Gini=0$ (pureté maximale) ; elle est maximale lorsque les classes sont à parts égales.

**Entropie (entropy)** et **gain d'information (information gain)** : l'[entropie](../entropy/) mesure le « désordre » d'un nœud.

$$H = -\sum_k p_k \log p_k$$

L'entropie avant la division moins la moyenne pondérée des entropies des nœuds enfants donne le **gain d'information**. Plus le gain est grand, plus cette coupure « met de l'ordre » dans les données, et plus elle mérite d'être faite.

Que l'on utilise Gini ou l'entropie, l'idée est la même : **choisir la coupure qui rend les nœuds enfants les plus purs, c'est-à-dire qui réduit le plus l'incertitude**.

**Régression** : la feuille doit produire une valeur numérique ; on minimise alors la **variance / l'erreur quadratique moyenne (MSE)** à l'intérieur des nœuds enfants :

$$\text{MSE} = \frac{1}{n}\sum_{i}(y_i - \bar{y})^2$$

On choisit la coupure qui minimise la somme pondérée des MSE des deux nœuds enfants — autrement dit, celle qui regroupe au mieux les valeurs de $y$ dans chaque région.

**Prédiction des feuilles** : en classification, la feuille renvoie la **classe majoritaire** parmi ses échantillons ; en régression, elle renvoie la **moyenne** des $y$ qu'elle contient.

{% include fviz/tree-split.html %}

## Surapprentissage et contrôle

L'arbre de décision a un talent dangereux : si on le laisse pousser indéfiniment, il peut apprendre l'ensemble d'entraînement **par cœur, mot pour mot** — chaque échantillon occupe sa propre feuille, l'erreur d'entraînement tombe à 0, mais c'est un cas typique de [surapprentissage](../overfitting/), et le modèle s'effondre sur de nouvelles données. Un arbre trop profond mémorise le bruit, pas les régularités.

Les moyens de contrôle (qui relèvent tous de la [régularisation](../regularization/) : accepter un peu de biais pour réduire la variance) :

- **Élagage (pruning)** : faire d'abord pousser l'arbre, puis couper les branches qui n'apportent rien sur l'ensemble de validation.
- **`max_depth`** : limiter la profondeur maximale, pour que l'arbre ne pose pas trop de questions successives.
- **`min_samples_leaf` / `min_samples_split`** : exiger un nombre minimal d'échantillons par feuille (ou par division), pour éviter de créer une feuille dédiée à quelques échantillons isolés.

Ces hyperparamètres doivent être choisis par [validation croisée](../cross-validation/) ; derrière se cache le [compromis biais-variance](../bias-variance/) : plus l'arbre est profond et complexe → biais faible, variance élevée ; en le limitant judicieusement → on trouve le point d'équilibre qui généralise le mieux.

## Un exemple concret (sklearn)

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

# Sans contrainte : apprend facilement l'ensemble d'entraînement par cœur
deep = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)
print("Sans limite      entraînement :", deep.score(Xtr, ytr), " test :", deep.score(Xte, yte))

# Avec contraintes de profondeur et de feuilles : plus stable, plus interprétable
clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(Xtr, ytr)
print("Profondeur limitée entraînement :", clf.score(Xtr, ytr), " test :", clf.score(Xte, yte))

# Afficher l'arbre entier sous forme de texte — c'est ce qui le rend si facile à interpréter
print(export_text(clf, feature_names=load_iris().feature_names))
```

Vous verrez que l'arbre sans limite obtient souvent un score d'entraînement de 1.0, sans que son score de test soit forcément meilleur ; et les règles affichées par `export_text` permettent à n'importe qui de comprendre « selon quels critères le modèle décide ».

## Avantages et inconvénients

**Avantages**

- **Très interprétable** : l'arbre entier n'est qu'un ensemble de règles if-else qu'on peut expliquer directement à des non-spécialistes.
- **Pas besoin de mise à l'échelle des variables** : une division ne regarde que « supérieur/inférieur à un seuil », elle est insensible aux unités et ne nécessite pas de standardisation.
- **Gère naturellement des variables mixtes** : variables numériques comme catégorielles ; relativement robuste aux valeurs manquantes et aux valeurs aberrantes.
- Capture automatiquement les relations **non linéaires** et les **interactions entre variables**.

**Inconvénients**

- **Variance élevée, instabilité** : une légère modification des données d'entraînement peut changer radicalement les points de coupure, et l'arbre obtenu peut être complètement différent.
- Un arbre seul a tendance à surapprendre et sa précision est souvent moyenne — c'est précisément pour cela qu'on le sauve par l'**ensemblisme**.

## Intérêt pour la prévision de séries temporelles

En prévision de séries temporelles, on commence généralement par transformer la série en tableau : on utilise des **variables retardées** ($t-1, t-7, \dots$), des **variables calendaires** (jour de la semaine, jour férié ou non, mois), etc., comme entrées du modèle. Sur un tel tableau, l'arbre de décision sait faire deux choses que les [modèles linéaires](../linear-model/) font mal :

- Capturer des **seuils non linéaires**, comme le point de rupture « au-delà de 30℃, la consommation d'électricité grimpe brusquement ».
- Capturer des **interactions entre variables**, comme le pic qui n'apparaît que « le week-end + par beau temps ».

Mais un arbre seul est trop faible et trop instable ; en pratique on l'utilise rarement isolément — sa vraie valeur est de servir d'**apprenant de base du GBDT** (voir [apprentissage ensembliste / GBDT](../ensemble-gbdt/)).

Il y a aussi un **avertissement capital** :

> **Les arbres ne savent pas extrapoler une tendance (extrapolation).**

La prédiction d'un arbre est toujours la **moyenne des échantillons d'entraînement** d'une feuille ; sa sortie **ne peut donc jamais dépasser la plage de valeurs vue pendant l'entraînement**. Si une série croît durablement (comme des ventes en hausse continue), face à une valeur future supérieure à tout l'historique, l'arbre ne renverra que « le palier le plus élevé qu'il ait vu », et **sous-estimera systématiquement la tendance**. Pour les séries à tendance marquée, la pratique courante consiste à **retirer d'abord la tendance / différencier, puis modéliser** le reste avec un modèle à base d'arbres.

## Résumé

- L'**arbre de décision** découpe l'espace des variables en régions par une suite de divisions if-else, et les feuilles fournissent les prédictions ; il est intuitif et facile à interpréter.
- Il pousse par **division binaire récursive** : en classification, on utilise **Gini $Gini=1-\sum_k p_k^2$ ou l'entropie $H=-\sum_k p_k\log p_k$** ; en régression, on minimise la **variance/MSE** des nœuds enfants.
- Prédiction d'une feuille = **classe majoritaire** (classification) ou **moyenne** (régression).
- Il **surapprend** facilement ; on le contrôle par l'**élagage, `max_depth`, `min_samples_leaf`**, etc. (voir [régularisation](../regularization/), [compromis biais-variance](../bias-variance/)).
- Avantages : interprétable, pas de mise à l'échelle, gère les variables mixtes ; inconvénients : **variance élevée, instabilité**.
- En séries temporelles, il capture les non-linéarités et les interactions à partir de **variables retardées/calendaires** ; seul, il est faible, mais c'est la pierre angulaire du [GBDT](../ensemble-gbdt/) ; il **ne sait pas extrapoler une tendance**, et les séries à tendance doivent d'abord être détendancialisées/différenciées. Voir aussi les [familles de modèles](../model-families/) pour situer sa place dans la généalogie des modèles.

[← Fondements de l'apprentissage automatique](../ml/) · [Vue d'ensemble des cours fondamentaux](../)
