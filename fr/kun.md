---
updated: "2026-06-11"
lang: fr
ref: kun
permalink: /fr/kun/
title: "Les questions de pointe en séries temporelles en 2026"
lead: "Après près d'un siècle de développement, la prévision de séries temporelles dispose d'une vaste panoplie d'outils éprouvés. Mais en 2026, les chercheurs se demandent toujours : peut-on faire mieux ? Cette page passe en revue les six défis de pointe les plus actifs du moment et montre comment Kernel U-Net tente de répondre à certains d'entre eux."
prev: linear-autoregression
next: kernel-u-net
math: true
---

## L'état de la prévision

Après cent ans de développement (de l'autorégression de Yule en 1927 jusqu'à aujourd'hui), la prévision de séries temporelles a accumulé une grande quantité d'outils éprouvés. Mais les chercheurs continuent de se demander : **peut-on faire mieux ?**

En 2026, les directions les plus actives du domaine peuvent se résumer en six grandes questions de pointe.

## 🧩 Six grandes questions de pointe

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌍</div>
    <h3>Modèles de fondation · Foundation Models</h3>
    <p>GPT a transformé le TAL ; les modèles de fondation peuvent-ils transformer les séries temporelles ? TimesFM (Google), Chronos (Amazon), Moirai (Salesforce) et d'autres sont pré-entraînés sur des masses de données temporelles et visent la « prévision zero-shot » — prédire sans même avoir vu vos données. Mais la diversité des distributions en séries temporelles dépasse de loin celle du texte, et l'efficacité du transfert reste une question ouverte.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> un seul modèle peut-il couvrir à la fois l'électricité, la finance, la météo et la santé&nbsp;?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📏</div>
    <h3>Séquences très longues · Ultra-Long Horizon</h3>
    <p>Les modèles classiques peinent déjà à prévoir 96 pas, alors que les besoins réels se chiffrent souvent en milliers, voire en dizaines de milliers de pas : planification électrique annuelle, modélisation du changement climatique, analyse de séquences génomiques. La complexité en O(N²) du Transformer l'empêche de traiter directement des séquences aussi longues, ce qui a donné naissance à l'attention linéaire, aux modèles à espace d'états (Mamba/S4) et aux architectures hiérarchiques.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> comment conserver la capacité à modéliser les dépendances à longue portée avec une complexité en O(N)&nbsp;?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🎯</div>
    <h3>Quantification de l'incertitude · Uncertainty</h3>
    <p>Une prévision ponctuelle (un seul nombre) est loin de suffire — les décideurs ont besoin de savoir « à quel point vous en êtes sûr ». La prévision probabiliste, la régression quantile et la prédiction conforme (conformal prediction) deviennent la norme. Entre 2024 et 2026, la prédiction conforme a connu un essor fulgurant grâce à sa « garantie de couverture en échantillon fini, sans hypothèse de distribution ».</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> comment produire des intervalles de prévision à la fois étroits et fiables&nbsp;?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚨</div>
    <h3>Prévision d'anomalies · Anomaly Prediction</h3>
    <p>Dans bien des situations, la question n'est pas « quelle sera la prochaine valeur ? » mais « va-t-il se passer quelque chose ? » : panne d'équipement, surcharge du réseau électrique, arythmie cardiaque. La difficulté tient à ce que les anomalies sont rares et changeantes, tandis que l'objectif glisse de la « détection après coup » vers « l'alerte précoce ». L'approche courante : modéliser d'abord le comportement normal, puis traiter tout écart marqué comme un signal.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> comment repérer une anomalie à l'avance, et non après coup, quand les exemples sont rarissimes et que leur forme ne cesse de changer&nbsp;?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌐</div>
    <h3>Prévision spatio-temporelle · Spatio-Temporal</h3>
    <p>Prévisions météorologiques, trafic routier, propagation d'épidémies — ces données évoluent dans le temps, mais possèdent aussi une structure spatiale. GraphCast (DeepMind) utilise des réseaux de neurones sur graphes pour la prévision météorologique mondiale et dépasse en précision les modèles numériques traditionnels. Modéliser simultanément les dépendances temporelles et la topologie spatiale est la difficulté centrale de la prévision spatio-temporelle.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> comment fusionner la structure de graphe (l'espace) et la structure séquentielle (le temps)&nbsp;?</p>
  </div>

  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🛡️</div>
    <h3>Généralisation · Generalization</h3>
    <p>Un modèle brille sur des jeux de données de référence bien propres, puis s'effondre dans le monde réel : données manquantes, dérive des capteurs, changements brusques de distribution (le COVID en a été un gigantesque). Comment éviter que le modèle ne s'effondre face à des « situations jamais vues » ? L'adaptation de domaine, l'apprentissage par transfert, le méta-apprentissage et l'apprentissage en ligne sont aujourd'hui les principales armes.</p>
    <p style="color:var(--accent);font-size:.88rem"><strong>Défi central&nbsp;:</strong> comment garder un modèle efficace sur de nouveaux domaines et de nouvelles distributions&nbsp;?</p>
  </div>
</div>

## Répondre à ces questions avec Kernel U-Net

Face à ces défis, la piste explorée sur ce site est **KUN (Kernel U-Net)**. KUN découpe un modèle en deux parties : un **squelette en U** fixe et, à chaque niveau, un **noyau interchangeable**. Répondre à un nouveau problème ne demande donc presque jamais de repenser le modèle ; il suffit en général de modifier un seul endroit : **changer de noyau**, **ajouter un composant au squelette** ou **changer de tête de sortie**. Le tableau ci-dessous indique le point d'entrée pour chacune des six questions. La plupart sont des pistes encore en cours d'exploration, non des réponses achevées :

| Question de pointe | Ce qui change | L'approche de KUN |
|--------------------|---------------|-------------------|
| Modèles de fondation | Changer de noyau | Utiliser des noyaux MoE (mélange d'experts) et davantage de niveaux, pour voir si des données de domaines plus variés peuvent être apprises par un même socle |
| Séquences très longues | Ajouter un composant | Ajouter une couche de mémoire au squelette en U pour retenir un historique plus long ; le sous-échantillonnage niveau par niveau raccourcit en outre la séquence en profondeur, où l'on peut donc se permettre des noyaux plus lourds |
| Quantification de l'incertitude | Changer de tête de sortie | Prévisions ponctuelles par défaut ; une régression quantile ou une prédiction conforme peut être branchée en sortie pour fournir des intervalles de prévision |
| Prédiction d'anomalies | Changer de tête de sortie | Remplacer « prédire les valeurs futures » par « prédire la distribution (densité) future », et donner l'alerte dès que les observations réelles tombent dans une zone de faible densité |
| Prévision spatio-temporelle | Modifier le squelette | Appliquer aussi la hiérarchie le long des axes spatiaux, afin que le sous-échantillonnage / suréchantillonnage niveau par niveau couvre à la fois le temps et l'espace |
| Généralisation | Changer de noyau | Prévision adaptative : choisir ou ajuster le noyau de chaque niveau selon les caractéristiques des données, pour se transférer à des domaines et des distributions jamais vus |

L'intuition centrale : **écrire le squelette une seule fois, et concrétiser les idées nouvelles en changeant de noyau ou en ajoutant des composants.** Ces questions de pointe n'exigent donc pas un modèle géant ; une puissance de calcul ordinaire suffit pour se lancer. Chaque nouvelle piste revient à écrire un nouveau noyau ou un nouveau module, puis à le brancher sur le même squelette léger.

> L'idée complète de KUN, son architecture couche par couche, l'analyse de complexité et le tutoriel de prise en main sont réunis sur une page dédiée :
> **[Comprendre en profondeur Kernel U-Net](../kernel-u-net/)**.

## Et ensuite ?

- **Pour voir comment KUN répond à ces défis** : lisez [Comprendre en profondeur Kernel U-Net](../kernel-u-net/), qui couvre tout, de la structure en U au tutoriel pas à pas.
- **Pour consolider vos bases en mathématiques et en apprentissage automatique** : retournez aux [cours fondamentaux](../foundations/).
- **Pour voir comment ces questions sont apparues pas à pas** : lisez l'[histoire des séries temporelles](../history/).

<div class="hint">Cette page ne fait que recenser les « questions » ; KUN est l'une des « réponses » possibles, et tous les détails se trouvent dans <a href="{{ '/fr/kernel-u-net/' | relative_url }}">Comprendre en profondeur Kernel U-Net</a>.</div>
