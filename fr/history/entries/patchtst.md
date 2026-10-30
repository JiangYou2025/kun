---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2023 · Informatique"
permalink: /fr/history/e/patchtst/
title: "Découper en mots (PatchTST, 2023)"
lead: "Découper la série en segments (patches) traités comme des tokens, puis modéliser chaque canal indépendamment — le Transformer reprend l'avantage sur les séries temporelles et répond à la question « l'attention sert-elle encore à quelque chose ? »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 10 · Grands modèles et KUN](../../10/).

### Contexte

La simple couche linéaire de [DLinear](../dlinear/) avait humilié le Transformer en prévision de longues séries, et la communauté s'était un temps demandé si l'attention avait encore une utilité. Mais l'expérience du traitement du langage et de la vision suggérait que la réussite ou l'échec d'un Transformer tient souvent moins à l'attention elle-même qu'à **la façon dont l'entrée est découpée en tokens**. Le ViT, qui découpe une image en patches traités comme des tokens, avait connu un grand succès : une inspiration directe pour les séries temporelles.

### Problème

Les premiers Transformers pour séries temporelles commettaient généralement deux erreurs. D'abord, ils traitaient **chaque instant** comme un token : dès que la série s'allonge, le nombre de tokens explose, l'attention en $$O(L^2)$$ devient insupportable, et un point isolé n'a presque aucune sémantique. Ensuite, ils **fusionnaient en un seul vecteur** les variables d'un même instant avant de les fournir au modèle, laissant des canaux sans rapport se perturber mutuellement. **Peut-on à la fois raccourcir la séquence, préserver la sémantique locale et isoler le bruit entre canaux ?**

### Autres courants de l'époque (et leurs limites)

- **Transformers temporels à tokens ponctuels (Informer, etc.)** : l'attention porte sur des pas de temps isolés. Limites : un point porte peu d'information et la séquence est trop longue, ce qui oblige à recourir à des approximations creuses qui finissent par perdre des motifs.
- **Modélisation à mélange de canaux** : toutes les variables d'un instant sont concaténées en un vecteur encodé d'un bloc. Limite : on force des séries faiblement corrélées, voire indépendantes, à partager une représentation, ce qui introduit de la diaphonie et nuit à la généralisation.
- **Références purement linéaires (DLinear)** : simples et efficaces, mais leur expressivité est bornée par la linéarité : elles peinent à modéliser des formes locales non linéaires complexes et les interactions entre segments.

### Méthode

PatchTST fait deux choses. Premièrement, le **découpage en patches (patching)** : la série univariée est découpée en patches de longueur $$P$$ avec un pas $$S$$, chaque patch devenant un token. Pour une série de longueur $$L$$, le nombre de tokens passe de $$L$$ à

$$ N = \left\lfloor \frac{L-P}{S} \right\rfloor + 1 $$

La complexité de l'attention tombe ainsi de $$O(L^2)$$ à $$O(N^2)$$, et chaque token porte la sémantique de toute une portion de forme d'onde locale. Deuxièmement, l'**indépendance des canaux (channel independence)** : toutes les variables **partagent les mêmes** poids de Transformer, mais chacune est propagée séparément, sans mélange dans l'attention — cela revient à décomposer le problème multivarié en un lot de problèmes univariés partageant un même modèle, ce qui réduit la diaphonie tout en faisant de l'immense quantité de sous-séries une forme d'augmentation de données. Couplé à un pré-entraînement auto-supervisé par masquage (on masque aléatoirement quelques patches et le modèle doit les reconstruire), la capacité de représentation s'améliore encore.

### Résultats

Sur les principaux bancs d'essai de prévision longue, PatchTST **dépasse sur toute la ligne** DLinear et les variantes de Transformer antérieures, avec un avantage particulièrement net pour les longues fenêtres : après pré-entraînement auto-supervisé, il montre aussi une capacité de transfert appréciable. Il démontre que si le Transformer perdait face au linéaire, la faute en revenait à la tokenisation, et non à une prétendue inutilité de l'attention.

### Portée et perspectives

PatchTST a refixé les règles du Transformer pour séries temporelles — **découpage en patches + indépendance des canaux** est devenu presque la configuration par défaut des travaux suivants. Ce geste consistant à « découper la série en mots » est aussi l'interface clé vers les [modèles de fondation](../foundation-models/) : TimesFM, Chronos, Moirai et les autres grands modèles pré-entraînés reposent tous sur une forme de découpage ou de tokenisation qui discrétise la série continue en tokens que le Transformer peut absorber. Il offre en outre un contraste intéressant avec [Kernel U-Net](../kun/) : PatchTST réduit la longueur d'un seul coup avec des patches de granularité fixe, tandis que KUN sous-échantillonne progressivement sur plusieurs échelles grâce à une hiérarchie en U — les deux répondent à la même question : « comment faire travailler l'opérateur à la bonne échelle ? ». De la question frontale posée par DLinear à la réponse vigoureuse de PatchTST, la modélisation des séries temporelles a accompli un recalibrage nécessaire.
