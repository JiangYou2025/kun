# KUN · Kernel U-Net — documentation & learning site

<p align="center">
  <b>🇬🇧 English</b> | <a href="README.zh.md">🇨🇳 简体中文</a> | <a href="README.fr.md">🇫🇷 Français</a>
</p>

**🔗 Live site: <https://jiangyou2025.github.io/kun/en/>** · [中文](https://jiangyou2025.github.io/kun/zh/) · [Français](https://jiangyou2025.github.io/kun/fr/)

A [Jekyll](https://jekyllrb.com/) site about **time series, forecasting and the Kernel U-Net (KUN) model**, available in **English, Chinese and French**. It has grown from a small intro into a small library:

- **KUN intro** — what a time series is, how to forecast, linear autoregression, a worked forecast, the math/ML background, and how KUN works (interchangeable kernels).
- **Lecture notes** (`course/`) — a 17-lecture introductory course.
- **A history of time series** (`history/`) — “100 years of time series”: a preface, 10 chapters by decade, 72 short entries and a filterable timeline.
- **Foundations** (`foundations/`) — a map of prerequisites (math, statistics, CS, deep learning), one short page per concept.
- **Tasks** (`tasks/`) — how time-series tasks co-evolved with computing power.
- **Applications** (`applications/`) — energy, finance, weather, health, transport, retail and more.
- **Three companion essays**, each split into one short story per entry:
  - **Prehistory & contemporary applications** (`prehistory/`) — pre-1900 timekeeping, observation and naïve methods.
  - **The nature of time** (`nature-of-time/`) — cross-disciplinary takes on what *time itself* is.
  - **Paradoxes of time** (`paradoxes/`) — famous paradoxes of time.
- **Runnable notebooks** (`notebooks/`) — synthetic-data Jupyter examples.

Served by **GitHub Pages**. Entry points (English):

- Home — <https://jiangyou2025.github.io/kun/en/>
- Lecture notes — <https://jiangyou2025.github.io/kun/en/course/>
- History — <https://jiangyou2025.github.io/kun/en/history/>
- Foundations — <https://jiangyou2025.github.io/kun/en/foundations/>
- Essays: [Prehistory](https://jiangyou2025.github.io/kun/en/prehistory/) · [The nature of time](https://jiangyou2025.github.io/kun/en/nature-of-time/) · [Paradoxes](https://jiangyou2025.github.io/kun/en/paradoxes/)

## Site map

Chinese is the source language and lives at the root; `en/` and `fr/` mirror it page for page (see [TRANSLATION.md](TRANSLATION.md)).

```
.
├── _config.yml              # site config (title, baseurl, languages)
├── _data/
│   ├── i18n.yml  ui.yml     # UI strings per language
│   ├── sidebar.yml          # sidebar labels per language
│   └── timeline.yml         # history timeline (zh/en/fr)
├── _layouts/
│   ├── default.html         # intro pages: header, nav, language switcher
│   ├── history.html         # history + essays: topic-aware left sidebar
│   └── lecture.html         # lecture pages
├── assets/css/main.css      # styles (dark/light, responsive, figures, game)
├── index.html               # root: redirects to the visitor's language
│
├── zh/                      # Chinese KUN intro (index, time-series, forecasting,
│                            #   linear-autoregression, prediction-in-action,
│                            #   math-ml-foundations, kernel-u-net, kun)
├── course/  history/  foundations/  tasks/  applications/
├── prehistory/  nature-of-time/  paradoxes/   # Chinese long-form content (+ index .md)
│
├── en/  fr/                 # full English / French mirrors of all of the above
│
├── scripts/check_i18n.py    # checks that every zh page has en/fr counterparts
├── notebooks/               # runnable Jupyter examples (excluded from the build)
└── Gemfile
```

## Citation

🌟 If you find this resource useful, consider adding a star to this repository and citing our research:

- J. You, A. Cela, R. Natowicz, J. Ouanounou, P. Siarry. **Kernel-U-Net: Multivariate Time Series Forecasting using Custom Kernels.** In *2024 International Conference on INnovations in Intelligent SysTems and Applications (INISTA)*, pp. 1–8, 2024. [doi:10.1109/INISTA62901.2024.10683862](https://doi.org/10.1109/INISTA62901.2024.10683862)

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

For anomaly prediction, please use:

- J. You, A. Cela, R. Natowicz, J. Ouanounou, P. Siarry. **Anomaly Prediction: A Novel Approach with Explicit Delay and Horizon.** In *2024 IEEE 20th International Conference on Intelligent Computer Communication and Processing (ICCP)*, 2024. [arXiv:2408.04377](https://arxiv.org/abs/2408.04377)

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

Related work:

- J. You, A. Cela, R. Natowicz, J. Ouanounou, P. Siarry. **Robust Time Series Forecasting with Non-Heavy-Tailed Gaussian Loss-Weighted Sampler.** arXiv preprint [arXiv:2406.13871](https://arxiv.org/abs/2406.13871), 2024.
- C. Li, J. You, H. Moungla, V. Gauthier, M. Nunez-del-Prado, H. Alatrista-Salas. **Enhancing Spatio-Temporal Forecasting with Spatial Neighbourhood Fusion: A Case Study on Mobility in Peru.** In *ICASSP 2026 – 2026 IEEE International Conference on Acoustics, Speech and Signal Processing*, 2026. [arXiv:2507.00031](https://arxiv.org/abs/2507.00031)
- J. You, X. Wang, A. Cela. **Dynamic Perturbed Adaptive Method for Infinite Task-Conflicting Time Series.** arXiv preprint [arXiv:2505.11902](https://arxiv.org/abs/2505.11902), 2025.
