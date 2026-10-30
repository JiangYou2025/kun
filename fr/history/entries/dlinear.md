---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2022 · Informatique"
permalink: /fr/history/e/dlinear/
title: "La contre-question d'une seule couche linéaire (DLinear, 2022)"
lead: "Décomposer la série en tendance et reste, puis confier chacun à une seule application linéaire — un modèle aussi rudimentaire surpasse toute une série de Transformers en prévision à long horizon, et force une question tranchante : l'attention est-elle vraiment nécessaire ?"
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [chapitre 10 · Grands modèles et KUN](../../10/).

### Contexte

Vers 2020, la prévision de séries longues (LSTF) est devenue un terrain très disputé. Informer, Autoformer, FEDformer et toute une lignée de « X-formers » se sont succédé, repoussant l'horizon de prévision traitable à des centaines, voire des milliers de pas grâce à l'attention parcimonieuse, à la décomposition de séries ou à des opérateurs fréquentiels ; dans les articles, les courbes d'erreur descendaient d'une marche chaque année. Le récit dominant était limpide : plus la série est longue, plus il faut de l'attention pour capter les dépendances lointaines.

### Problème

Ces modèles partageaient pourtant une gêne commune : leur architecture s'alourdissait sans cesse, mais on n'avait jamais vérifié rigoureusement, par comparaison contrôlée, si le gain provenait vraiment de « l'attention » elle-même. Presque tous comportaient un prétraitement passé inaperçu — la **décomposition de la série** (séparer la tendance de la saisonnalité ou du reste). **Si l'on garde la décomposition et que l'on supprime toute l'attention, de combien le résultat se dégrade-t-il ?** Personne ne se l'était sérieusement demandé.

### Autres courants de l'époque (et leurs limites)

- **Primauté de l'attention (variantes de Transformers)** : on tient pour acquis que les dépendances longues doivent être modélisées par l'auto-attention. Limites : l'auto-attention est invariante par permutation et ne « comprend » pas en soi l'ordre temporel, d'où le besoin d'encodages positionnels correctifs ; et sa complexité en $$O(L^2)$$ impose toutes sortes d'approximations qui introduisent de nouveaux biais.
- **Références purement statistiques ([ARIMA](../box-jenkins/), lissage exponentiel)** : interprétables et robustes, mais difficiles à adapter en masse aux contextes multivariés de grande dimension et à longues fenêtres ; souvent écartées comme « dépassées ».
- Aucun des deux camps ne répondait à cette question : quelle part du gain apporté par les architectures complexes vient en réalité de la plus simple extrapolation linéaire de la tendance ?

### Méthode

DLinear donne une réponse presque provocatrice : effectuer d'abord une **décomposition par moyenne mobile**, puis projeter directement la tendance et le reste sur la fenêtre future avec **une seule couche linéaire chacun**, et additionner. Soit une fenêtre rétrospective $$X\in\mathbb{R}^{L}$$, décomposée en tendance $$X_t$$ et reste $$X_s=X-X_t$$ ; la prévision s'écrit

$$ \hat{Y} = W_t X_t + W_s X_s,\qquad W_t,W_s\in\mathbb{R}^{T\times L} $$

où $$T$$ est l'horizon de prévision et $$W_t,W_s$$ deux matrices de poids apprenables — le modèle entier ne contient ni non-linéarité, ni attention, ni récurrence. Il revient essentiellement à apprendre, pour la tendance et pour le reste, un ensemble de « poids linéaires à travers le temps », ce qui équivaut à apprendre pour chaque instant futur une moyenne pondérée de l'historique. Aussi simple, il réduit le nombre de paramètres et le calcul d'un ou deux ordres de grandeur.

### Résultats

Sur plusieurs bancs d'essai LSTF standards (électricité, trafic, météo, ETT, etc.), l'erreur de prévision de DLinear **égale, voire dépasse**, celle des Transformers complexes contemporains ; il s'entraîne vite, consomme peu de mémoire et reste presque interprétable — les matrices de poids se visualisent directement comme « la manière dont le futur pondère le passé ». Ce résultat fit l'effet d'une douche froide, rappelant à tout le domaine qu'une grande partie des gains venait de la décomposition et de l'extrapolation linéaire, et non de l'attention.

### Portée et perspectives

La valeur de DLinear n'est pas de montrer que « le linéaire suffit », mais d'avoir établi une **référence forte et honnête** et une interpellation méthodologique : avant d'empiler des architectures complexes pour les séries temporelles, prouvez d'abord que vous en avez vraiment besoin. Cette remise en question a directement fait naître deux voies — l'une redonnant au [Transformer](../patchtst/) un bon usage sur les séries temporelles (découpage en patchs, indépendance des canaux), l'autre revenant aux structures temporelles linéaires comme les espaces d'états et les convolutions. Elle fait aussi écho à la thèse centrale de [Kernel U-Net](../kun/) : séparer la « structure multi-échelle » de « l'opérateur de chaque couche » — c'est souvent la structure (décomposition, hiérarchie en U) qui fait l'essentiel du travail, et l'opérateur peut rester très léger. Aujourd'hui encore, lorsqu'on se demande quelle ossature donner aux [modèles de fondation](../foundation-models/) pour les séries temporelles, la question laissée par DLinear — « êtes-vous sûr d'avoir besoin de l'attention ? » — reste présente.
