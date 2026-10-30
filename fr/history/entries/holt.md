---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1957 · Contrôle / communications"
permalink: /fr/history/e/holt/
title: "La méthode de tendance linéaire de Holt (Holt, 1957)"
lead: "Le lissage exponentiel simple ne sait qu'« extrapoler à plat » et a toujours un temps de retard sur des ventes en croissance régulière. Holt lui ajoute une seconde récurrence pour suivre séparément le « niveau » et la « tendance »."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Chapitre 3 · Lissage exponentiel](../../03/).

### Contexte

En 1957, dans un mémorandum de recherche pour la Marine rédigé au Carnegie Institute of Technology, Charles C. Holt étend le [lissage exponentiel simple (SES)](../brown-ses/) aux séries avec tendance. Le contexte reste la planification de la production et des stocks : dans la réalité, la demande ne fluctue souvent pas autour d'un niveau fixe, elle **croît ou décroît durablement** — la population augmente, les marchés s'étendent, les prix évoluent. Un système de prévision doit suivre cette dérive orientée.

### Problème

Le SES ne maintient qu'un « niveau » $$\ell_t$$, et sa prévision est plate : $$\hat{x}_{t+h}=\ell_t$$. Lorsque la série présente une tendance stable, cette extrapolation plate **accuse un retard systématique** : une série croissante est toujours sous-estimée, une série décroissante toujours surestimée, et l'erreur s'amplifie avec l'horizon $$h$$. **Peut-on conserver les atouts du lissage exponentiel — « en ligne et économe en mémoire » — tout en permettant au modèle d'apprendre et d'extrapoler la tendance ?**

### Les autres courants de l'époque (et leurs limites)

- **[SES](../brown-ses/)** : efficace en ligne, mais ne connaît que le niveau et extrapole à plat ; biais structurel sur les séries à tendance.
- **Régression linéaire globale (droite ajustée en fonction du temps)** : exprime la tendance, mais la suppose constante et doit tout recalculer par lots ; incapable de s'adapter en ligne à une pente qui évolue lentement.
- **SES sur la série différenciée** : supprime la tendance, mais mêle « niveau » et « tendance », qu'on peine alors à interpréter et à extrapoler séparément, et le réglage est peu intuitif.

### Méthode

Holt introduit **deux états et deux coefficients de lissage** : le niveau $$\ell_t$$ et la tendance (pente) $$b_t$$, mis à jour chacun par récurrence :

$$ \ell_t = \alpha\, x_t + (1-\alpha)\,(\ell_{t-1}+b_{t-1}) $$

$$ b_t = \beta\,(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1} $$

Dans la mise à jour du niveau, « niveau précédent plus tendance précédente », $$\ell_{t-1}+b_{t-1}$$, est la prévision interne pour la période courante, pondérée par $$\alpha$$ avec la nouvelle observation $$x_t$$ ; la mise à jour de la tendance pondère par $$\beta$$ l'« accroissement effectif du niveau » $$\ell_t-\ell_{t-1}$$ et l'ancienne tendance. La prévision à $$h$$ pas est une **extrapolation linéaire** :

$$ \hat{x}_{t+h} = \ell_t + h\,b_t $$

$$\alpha,\beta\in(0,1)$$ règlent respectivement la vitesse de mise à jour du niveau et de la tendance. L'ensemble reste une récurrence en ligne en O(1), qui ne demande de stocker qu'un $$b_{t-1}$$ supplémentaire.

### Résultats

Sur les séries de demande et de ventes à tendance, la méthode de Holt est nettement plus précise que le SES, et la courbe de prévision s'incline naturellement avec $$h$$ au lieu de rester à la traîne. Elle fait passer le lissage exponentiel de « suivre un niveau stable » à « suivre niveau + tendance », tout en conservant tous ses avantages : simplicité, adaptativité et coût de calcul minime. En pratique, on l'associe souvent à une **tendance amortie** (un facteur de décroissance $$\phi<1$$ appliqué à la tendance) pour éviter que la pente ne diverge lors d'extrapolations à long terme.

### Portée et perspectives

Holt a étendu le lissage exponentiel d'une récurrence à un seul état à des récurrences à plusieurs états, fondant le paradigme « décomposer par composantes, lisser chacune séparément ». En ajoutant encore un terme saisonnier, on obtient la [méthode saisonnière de Holt–Winters](../holt-winters/) de la même époque ; et la structure d'extrapolation linéaire à deux états « niveau + tendance » est précisément un cas particulier du modèle espace d'états à tendance linéaire locale du [filtre de Kalman](../kalman/). Du cadre ETS aux références par défaut des bibliothèques de prévision actuelles, ces deux lignes de récurrence de Holt restent un point de départ incontournable.
