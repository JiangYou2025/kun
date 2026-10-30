---
updated: "2026-06-03"
layout: history
lang: fr
permalink: /fr/history/
title: "Histoire des séries temporelles · Sommaire"
lead: "De l'autorégression de Yule en 1927 à l'apprentissage profond et aux modèles de fondation d'aujourd'hui — un siècle d'analyse et de prévision des séries temporelles. Un prologue et 10 chapitres qui racontent la genèse de chaque méthode, en écrivent les formules clés et en expliquent le sens."
---

## De quoi s'agit-il

Une chronique centenaire de l'évolution des méthodes de **séries temporelles** (*time series*) : des fondations posées par la statistique, en passant par l'espace d'état et le paradigme de Box–Jenkins, puis les vagues de l'apprentissage automatique et de l'apprentissage profond, jusqu'aux Transformers, aux modèles de fondation et à **Kernel U-Net (KUN)**.

> Contenus associés : [Cours d'introduction aux séries temporelles](../course/) · [Utiliser KUN](../kun/)
>
> Trois essais parallèles : [Préhistoire et applications contemporaines](../prehistory/) · [La nature du temps](../nature-of-time/) · [Les paradoxes du temps](../paradoxes/)

## Chronologie

Filtrez cette chronologie centenaire par **domaine** — les mathématiciens ont posé la théorie, les physiciens ont donné l'intuition physique des processus stochastiques, la cybernétique et l'ingénierie des communications ont fait de la prévision une technique calculable de façon récursive et en ligne, et l'informatique l'a poussée vers l'apprentissage automatique et l'apprentissage profond. Cliquez sur une étiquette ci-dessous pour n'afficher qu'un domaine, ou sur **Tout** pour voir l'ensemble de la trame où les quatre domaines s'entrelacent.

<div class="tl" markdown="0">
<input class="tl-radio" type="radio" name="tlf" id="tl-all" checked>
<input class="tl-radio" type="radio" name="tlf" id="tl-math">
<input class="tl-radio" type="radio" name="tlf" id="tl-phys">
<input class="tl-radio" type="radio" name="tlf" id="tl-ctrl">
<input class="tl-radio" type="radio" name="tlf" id="tl-cs">
<div class="tl-tabs">
  <label for="tl-all">Tout</label>
  <label for="tl-math" class="d-math"><span class="dot"></span>Mathématiciens</label>
  <label for="tl-phys" class="d-phys"><span class="dot"></span>Physiciens</label>
  <label for="tl-ctrl" class="d-ctrl"><span class="dot"></span>Cybernétique / communications</label>
  <label for="tl-cs" class="d-cs"><span class="dot"></span>Informatique</label>
</div>
<table class="tl-table">
<thead><tr><th>Année</th><th>Domaine</th><th>Personne</th><th>Contribution clé</th><th>Chapitre</th></tr></thead>
<tbody>
{% for item in site.data.timeline %}{% case item.domain %}{% when 'math' %}{% assign dlabel = 'Mathématiques' %}{% when 'phys' %}{% assign dlabel = 'Physique' %}{% when 'ctrl' %}{% assign dlabel = 'Contrôle' %}{% else %}{% assign dlabel = 'Informatique' %}{% endcase %}<tr class="r-{{ item.domain }}"><td class="yr">{{ item.year }}</td><td><span class="badge d-{{ item.domain }}">{{ dlabel }}</span></td><td><a href="{{ '/fr/history/e/' | append: item.slug | append: '/' | relative_url }}">{{ item.person_fr | default: item.person }}</a></td><td>{{ item.contribution_fr | escape }}</td><td><a href="{{ '/fr/history/' | append: item.chap_url | relative_url }}">{% if item.chap_url == 'foundations/' %}Prologue{% else %}{{ item.chap }}{% endif %}</a></td></tr>
{% endfor %}
</tbody>
</table>
</div>

> Ce tableau sert aussi de navigation entre les chapitres du livre : la colonne « Chapitre », tout à droite de chaque ligne, mène directement au chapitre correspondant. Le prologue retrace, discipline par discipline, les sources qui traversent le siècle (mathématiques · physique · contrôle/communications · décision séquentielle · calcul scientifique) ; les chapitres 1 à 10 se déroulent ensuite par ordre chronologique.

## Essais complémentaires

Le texte principal suit la trame des méthodes qui part de la théorie des processus stochastiques vers 1900. Chacun des essais ci-dessous a sa propre page et tourne autour de cette trame sous un angle différent :

- [**Histoire des tâches** (*Task History*)](../tasks/) — l'histoire raconte l'évolution des outils ; ici, c'est l'évolution des problèmes : de la prévision des crues il y a 3 000 ans aux séries temporelles multimodales d'aujourd'hui.
- [**Les séries temporelles en pratique** (*Applications in the Wild*)](../applications/) — comment les séries temporelles sont mises en œuvre, domaine par domaine : dix cas d'usage couvrant la finance, l'énergie, la distribution, les transports, la santé, la météorologie, l'industrie, le signal, la géophysique et le langage.
- [**Préhistoire et applications** (*Prehistory & Applications*)](../prehistory/) — comment, avant le XIXᵉ siècle, l'humanité « lisait des séries temporelles » à travers la mesure du temps, l'observation et des méthodes naïves, ainsi qu'un inventaire des applications des séries temporelles dans divers domaines.
- [**La nature du temps** (*The Nature of Time*)](../nature-of-time/) — une interrogation interdisciplinaire, par la philosophie, la physique et la littérature, sur le « temps » lui-même.
- [**Les paradoxes du temps** (*Paradoxes of Time*)](../paradoxes/) — de Zénon au paradoxe du grand-père, ces paradoxes célèbres qui nous obligent à penser clairement le « temps ».

## Conventions de lecture

- Chaque chapitre raconte sous forme de récit la genèse des méthodes, en écrit les **formules** clés et en explique le sens.
- Le prologue retrace, discipline par discipline (mathématiques · physique · contrôle/communications · décision séquentielle · calcul scientifique), les sources qui traversent le siècle ; il existe en outre trois essais parallèles : [Préhistoire et applications contemporaines](../prehistory/), [La nature du temps](../nature-of-time/) et [Les paradoxes du temps](../paradoxes/).
- Les années, noms et articles cités ont été rassemblés par l'auteur ; merci de les vérifier avant de les citer.
- Le chapitre 10 se conclut sur KUN, en écho au tutoriel pratique [Utiliser KUN](../kun/).
