---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 2010 · Contrôle / Communications"
permalink: /fr/history/e/particle-mcmc/
title: "MCMC particulaire (Andrieu et al., 2010)"
lead: "Dans un modèle espace d'état non linéaire, comment estimer conjointement les paramètres et les états cachés ? Glissez l'estimation de vraisemblance fournie par un filtre particulaire dans un MCMC — même si ce n'est qu'une estimation, la chaîne converge toujours vers la bonne distribution."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Le modèle espace d'état est le squelette universel des séries temporelles : un état caché $$ x_t $$ évolue selon une certaine dynamique, et l'observation $$ y_t $$ en est un reflet bruité. Le cas linéaire gaussien admet la solution exacte du [filtre de Kalman](../kalman/) : le cas non linéaire ou non gaussien dispose depuis les années 1990 du **filtre particulaire (Monte-Carlo séquentiel)**, qui approche la loi de filtrage et fournit au passage une **estimation sans biais de la vraisemblance marginale**. Mais le filtre particulaire suppose les paramètres connus. La vraie difficulté est la suivante : **lorsque les paramètres sont inconnus, comment faire une inférence bayésienne simultanée sur les paramètres et les états cachés ?** En 2010, Andrieu, Doucet et Holenstein ont apporté dans JRSS-B une réponse élégante : le **MCMC particulaire (PMCMC)**.

### Problème

L'inférence bayésienne sur le paramètre $$ \theta $$ exige la vraisemblance marginale $$ p(y_{1:T}\mid\theta) $$, qui intègre sur toutes les trajectoires d'états cachés : pour un modèle non linéaire, cette intégrale **n'a pas de solution analytique**. Faire directement un Gibbs/MCMC conjoint sur $$ (\theta, x_{1:T}) $$ mélange par ailleurs très mal, car les états sont fortement corrélés. Peut-on construire un MCMC dont la loi stationnaire en $$ \theta $$ soit exactement la vraie loi a posteriori $$ p(\theta\mid y_{1:T}) $$, tout en confiant l'intégration sur les états au filtre particulaire :

### Autres courants de l'époque (et leurs limites)

- **Kalman étendu / sans parfum (EKF/UKF)** : rapides, mais reposent sur une linéarisation ou un appariement de moments : le biais est important en cas de forte non-linéarité ou de multimodalité, et ils ne donnent pas la loi a posteriori complète.
- **Échantillonnage de Gibbs direct des trajectoires d'état** : faisable en principe, mais la forte corrélation entre états voisins rend le **mélange extrêmement lent** : sur de longues séries, la chaîne ne bouge presque plus.
- **Filtre particulaire seul** : traite les états non linéaires, mais **n'estime pas les paramètres** : et même à paramètres fixés, il souffre de la dégénérescence des chemins.

### Méthode

Le cœur du PMCMC est le **principe pseudo-marginal** : dans le taux d'acceptation de Metropolis–Hastings, on remplace la vraisemblance réelle, inaccessible, par une **estimation sans biais de la vraisemblance** $$ \hat{p}(y_{1:T}\mid\theta) $$, et la chaîne de Markov obtenue a **toujours exactement** pour loi stationnaire la loi a posteriori cible. Le filtre particulaire fournit justement une telle estimation sans biais :

$$ \hat{p}(y_{1:T}\mid\theta) = \prod_{t=1}^{T}\Big(\frac{1}{N}\sum_{i=1}^{N} w_t^{(i)}\Big),\qquad \mathbb{E}\big[\hat{p}\big] = p(y_{1:T}\mid\theta) $$

où $$ N $$ est le nombre de particules et $$ w_t^{(i)} $$ les poids d'importance. Le **Metropolis–Hastings marginal particulaire (PMMH)** propose à chaque pas un nouveau paramètre selon $$ q(\theta'\mid\theta) $$, exécute un filtre particulaire pour obtenir $$ \hat{p}(y_{1:T}\mid\theta') $$, puis accepte avec la probabilité

$$ \alpha = \min\!\left\{1,\ \frac{\hat{p}(y_{1:T}\mid\theta')\,p(\theta')\,q(\theta\mid\theta')}{\hat{p}(y_{1:T}\mid\theta)\,p(\theta)\,q(\theta'\mid\theta)}\right\} $$

L'absence de biais garantit que, bien que $$ \hat p $$ soit bruité, la chaîne converge vers la loi a posteriori jointe exacte $$ p(\theta, x_{1:T}\mid y_{1:T}) $$. Une autre variante, le **Gibbs particulaire**, rééchantillonne les états par un « filtre particulaire conditionnel » qui conserve une trajectoire de référence, ce qui améliore le mélange.

### Résultats

Le PMCMC a rendu possible l'inférence bayésienne complète pour une vaste classe de **modèles espace d'état non linéaires et non gaussiens** jusque-là difficiles à traiter : volatilité stochastique, dynamique des populations en écologie, propagation des épidémies, réseaux de réactions biochimiques, etc. Il transforme le fait que « la vraisemblance ne peut qu'être estimée, pas calculée exactement » d'obstacle en coût acceptable, et ne requiert que la **simulation directe** du modèle, sans avoir à écrire la vraisemblance — ce qui convient parfaitement aux modèles mécanistes complexes. Le prix à payer est un calcul coûteux (chaque pas de MCMC embarque un filtre particulaire complet), et un $$ N $$ trop petit rend la variance de l'estimation de vraisemblance trop grande, au point de bloquer la chaîne.

### Portée et perspectives

L'héritage intellectuel du PMCMC est le **MCMC pseudo-marginal** : dès qu'on dispose d'une estimation sans biais de la vraisemblance, on obtient en échange une inférence bayésienne exacte — ce qui **coud rigoureusement** ensemble les deux piliers que sont le Monte-Carlo et le MCMC. Avec l'inférence variationnelle, la programmation probabiliste et les filtres particulaires différentiables qui ont suivi, il forme le socle de l'inférence bayésienne moderne pour les séries temporelles non linéaires. Les cadres de programmation probabiliste actuels utilisent toujours le MCMC particulaire comme outil généraliste pour les modèles espace d'état arbitraires, prolongeant le puissant paradigme « simuler, c'est inférer ».
