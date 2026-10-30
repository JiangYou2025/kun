---
updated: "2026-06-14"
layout: history
lang: fr
era: "Entrée de la chronologie · 1948 · Contrôle / Communications"
permalink: /fr/history/e/shannon/
title: "Mesurer l'information (Shannon, 1948)"
lead: "Combien d'information porte un message, à quelle vitesse un canal peut-il transmettre de façon fiable, à quelle densité faut-il échantillonner un signal continu — Shannon a quantifié ces trois questions d'un seul coup grâce à l'entropie, et ouvert l'ère de l'information."
math: true
---

> Ceci est une entrée de la chronologie de l'[histoire des séries temporelles](../../), rattachée au [Prologue · Sources interdisciplinaires](../../foundations/).

### Contexte

Dans les années 1940, le téléphone, le télégraphe et le radar ont fait de « comment transmettre l'information efficacement et de façon fiable » un problème d'ingénierie pressant, mais il n'existait alors aucune mesure unifiée de la « quantité d'information ». Dans « A Mathematical Theory of Communication » (1948), Claude Shannon fonde d'un seul geste la **théorie de l'information** : il quantifie l'information à l'aide des probabilités et établit les limites fondamentales de la communication. C'est l'un des articles les plus fondateurs du XXe siècle.

### Problème

Trois questions fondamentales étroitement liées : **Combien d'information une source aléatoire porte-t-elle en moyenne ? Combien de bits par seconde, au maximum, un canal bruité peut-il transmettre de façon fiable ? À quelle densité faut-il échantillonner un signal en temps continu pour pouvoir le reconstruire parfaitement à partir de ses échantillons ?** Avant Shannon, il n'existait sur tout cela que des règles empiriques, sans aucune borne théorique.

### Autres courants de l'époque (et leurs limites)

- **L'intuition d'ingénieur fondée sur la bande passante et le rapport signal/bruit** : on savait qu'une large bande et un bon rapport signal/bruit permettent de transmettre plus et mieux, mais on ne pouvait donner de borne précise à la « transmission fiable », ni distinguer la compression de la source de la transmission sur le canal.
- **La quantité d'information logarithmique de Hartley (1928)** : mesurer l'information par le $$\log$$ (du nombre de symboles) allait dans la bonne direction, mais sans introduire de **distribution de probabilité**, impossible de rendre compte du fait qu'« une source aux symboles non équiprobables est plus compressible ».
- **Les rustines d'ingénierie de correction symbole par symbole** : répétition, contrôle de parité pour réduire le taux d'erreur, le plus souvent des expédients ad hoc ; on ignorait si, sur un canal donné, un taux d'erreur arbitrairement faible était seulement atteignable — exactement la question à laquelle répond le théorème du codage de canal.

### Méthode

Shannon mesure la quantité moyenne d'information d'une source discrète $$X$$ (en bits) par l'**entropie** :

$$ H(X)=-\sum_{i} p_i\,\log_2 p_i $$

$$H$$ est la limite de la compression sans perte : la longueur moyenne de code ne peut descendre sous $$H$$ bits par symbole. Pour un canal gaussien additif de bande passante $$B$$, de puissance de signal $$S$$ et de puissance de bruit $$N$$, la **capacité du canal** (le débit maximal permettant un taux d'erreur arbitrairement faible) vaut

$$ C=B\,\log_2\!\Big(1+\frac{S}{N}\Big)\quad(\text{bits/s}) $$

Le **théorème du codage de canal** affirme que, tant que le débit de transmission vérifie $$R<C$$, il existe un codage rendant le taux d'erreur arbitrairement petit ; si $$R>C$$, une transmission fiable est impossible. Sur le pont entre continu et discret, le **théorème d'échantillonnage de Nyquist–Shannon** établit qu'un signal à bande limitée à $$B$$ hertz peut être **parfaitement reconstruit** à partir de ses échantillons dès lors que la fréquence d'échantillonnage vérifie $$f_s\ge 2B$$ :

$$ x(t)=\sum_{n=-\infty}^{\infty} x\!\Big(\frac{n}{2B}\Big)\,\mathrm{sinc}\big(2Bt-n\big) $$

En échantillonnant en dessous de $$2B$$, on provoque du **repliement spectral** : les hautes fréquences se déguisent en basses fréquences, et l'information devient irrécupérable.

### Résultats

La théorie de l'information a fait de l'« information », notion floue, une grandeur physique calculable, et a tracé trois limites infranchissables : compresser jusqu'à l'entropie, transmettre jusqu'à la capacité, échantillonner à $$2B$$. Elle a posé d'un coup les bases théoriques de la compression de données, du codage correcteur d'erreurs, de la modulation et de l'échantillonnage, faisant de « l'approche de la limite » l'objectif commun de l'ingénierie des communications.

### Portée et perspectives

Entropie, information mutuelle, capacité et théorème d'échantillonnage restent aujourd'hui la langue commune des communications, de la compression et de l'apprentissage statistique. Le théorème d'échantillonnage régit directement l'acquisition de toute série temporelle numérique — que chacun de vos signaux numériques, chacun de vos relevés de capteur représente fidèlement ou non le processus continu d'origine, c'est $$f_s\ge 2B$$ qui en décide. L'entropie et l'information mutuelle mènent quant à elles aux fonctions de perte de l'apprentissage automatique moderne (l'entropie croisée), à la sélection de caractéristiques et à l'apprentissage de représentations. Ce pas de Shannon est le véritable point de départ de l'ère numérique.
