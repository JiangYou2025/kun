# KUN · Kernel U-Net — documentation et site d’apprentissage

<p align="center">
  <a href="README.md">🇬🇧 English</a> | <a href="README.zh.md">🇨🇳 简体中文</a> | <b>🇫🇷 Français</b>
</p>

**🔗 Site en ligne : <https://jiangyou2025.github.io/kun/fr/>** · [English](https://jiangyou2025.github.io/kun/en/) · [中文](https://jiangyou2025.github.io/kun/zh/)

Un site [Jekyll](https://jekyllrb.com/) consacré aux **séries temporelles, à la prévision et au modèle Kernel U-Net (KUN)**, disponible en **français, anglais et chinois**. D’une petite introduction, il est devenu une petite bibliothèque :

- **Introduction à KUN** — qu’est-ce qu’une série temporelle, comment prévoir, l’autorégression linéaire, une prévision réussie, les bases mathématiques et d’apprentissage automatique, et le fonctionnement de KUN (noyaux interchangeables).
- **Cours** (`course/`) — un cours d’introduction en 17 leçons.
- **Histoire des séries temporelles** (`history/`) — « 100 ans de séries temporelles » : une préface, 10 chapitres par décennie, 72 courtes entrées et une frise chronologique filtrable.
- **Cours de base** (`foundations/`) — une carte des prérequis (mathématiques, statistiques, informatique, apprentissage profond), une page courte par notion.
- **Tâches** (`tasks/`) — la coévolution des tâches de séries temporelles et de la puissance de calcul.
- **Applications** (`applications/`) — énergie, finance, météo, santé, transport, commerce, etc.
- **Trois essais complémentaires**, chacun découpé en une courte histoire par entrée :
  - **Préhistoire et applications contemporaines** (`prehistory/`) — mesure du temps, observation et méthodes naïves avant 1900.
  - **La nature du temps** (`nature-of-time/`) — regards interdisciplinaires sur ce qu’est *le temps lui-même*.
  - **Paradoxes du temps** (`paradoxes/`) — les paradoxes célèbres du temps.
- **Notebooks exécutables** (`notebooks/`) — exemples Jupyter sur données synthétiques.

Hébergé par **GitHub Pages**. Points d’entrée (français) :

- Accueil — <https://jiangyou2025.github.io/kun/fr/>
- Cours — <https://jiangyou2025.github.io/kun/fr/course/>
- Histoire — <https://jiangyou2025.github.io/kun/fr/history/>
- Cours de base — <https://jiangyou2025.github.io/kun/fr/foundations/>
- Essais : [Préhistoire](https://jiangyou2025.github.io/kun/fr/prehistory/) · [La nature du temps](https://jiangyou2025.github.io/kun/fr/nature-of-time/) · [Paradoxes](https://jiangyou2025.github.io/kun/fr/paradoxes/)

## Plan du site

Le chinois est la langue source, à la racine ; `en/` et `fr/` en sont le miroir page par page (voir [TRANSLATION.md](TRANSLATION.md)).

```
.
├── _config.yml              # configuration (titre, baseurl, langues)
├── _data/
│   ├── i18n.yml  ui.yml     # textes de l’interface par langue
│   ├── sidebar.yml          # libellés de la barre latérale par langue
│   └── timeline.yml         # frise de l’histoire (zh/en/fr)
├── _layouts/
│   ├── default.html         # pages d’intro : en-tête, navigation, choix de langue
│   ├── history.html         # histoire + essais : barre latérale par thème
│   └── lecture.html         # pages du cours
├── assets/css/main.css      # styles (sombre/clair, responsive, figures, jeu)
├── index.html               # racine : redirige vers la langue du visiteur
│
├── zh/                      # intro KUN en chinois (index, time-series, forecasting,
│                            #   linear-autoregression, prediction-in-action,
│                            #   math-ml-foundations, kernel-u-net, kun)
├── course/  history/  foundations/  tasks/  applications/
├── prehistory/  nature-of-time/  paradoxes/   # contenus longs en chinois (+ index .md)
│
├── en/  fr/                 # miroirs anglais / français de tout ce qui précède
│
├── scripts/check_i18n.py    # vérifie que chaque page zh a ses versions en/fr
├── notebooks/               # exemples Jupyter exécutables (hors build)
└── Gemfile
```

## Citation

🌟 Si cette ressource vous est utile, n’hésitez pas à ajouter une étoile à ce dépôt et à citer nos travaux :

```bibtex
@inproceedings{you_2024_kernel_u_net,
  author={You, Jiang and Cela, Arben and Natowicz, René and Ouanounou, Jacob and Siarry, Patrick},
  booktitle={2024 International Conference on INnovations in Intelligent SysTems and Applications (INISTA)},
  title={Kernel-U-Net: Multivariate Time Series Forecasting using Custom Kernels},
  year={2024},
  volume={},
  number={},
  pages={1-8},
  keywords={Time series Forecasting;Architecture;U-Net;Transformers;},
  doi={10.1109/INISTA62901.2024.10683862}}
```

Pour la prédiction d’anomalies, veuillez citer :

```bibtex
@inproceedings{you_2024_anomaly_prediction,
  author={You, Jiang and Cela, Arben and Natowicz, René and Ouanounou, Jacob and Siarry, Patrick},
  booktitle={2024 IEEE 20th International Conference on Intelligent Computer Communication and Processing (ICCP)},
  title={Anomaly Prediction: A Novel Approach with Explicit Delay and Horizon},
  year={2024},
  volume={},
  number={},
  pages={-},
  keywords={Time series;Anomaly Prediction;Anomaly Detection;U-Net;Transformers;},
  url={https://arxiv.org/abs/2408.04377}}
```

Travaux connexes :

- J. You, A. Cela, R. Natowicz, J. Ouanounou, P. Siarry. **Robust Time Series Forecasting with Non-Heavy-Tailed Gaussian Loss-Weighted Sampler.** arXiv preprint [arXiv:2406.13871](https://arxiv.org/abs/2406.13871), 2024.
- C. Li, J. You, H. Moungla, V. Gauthier, M. Nunez-del-Prado, H. Alatrista-Salas. **Enhancing Spatio-Temporal Forecasting with Spatial Neighbourhood Fusion: A Case Study on Mobility in Peru.** In *ICASSP 2026 – 2026 IEEE International Conference on Acoustics, Speech and Signal Processing*, 2026. [arXiv:2507.00031](https://arxiv.org/abs/2507.00031)
- J. You, X. Wang, A. Cela. **Dynamic Perturbed Adaptive Method for Infinite Task-Conflicting Time Series.** arXiv preprint [arXiv:2505.11902](https://arxiv.org/abs/2505.11902), 2025.
