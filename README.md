# KUN · Kernel U-Net — documentation & learning site

**🔗 在线访问 / Live site: <https://jiangyou2025.github.io/kun/zh/>** （中文）  ·  [English](https://jiangyou2025.github.io/kun/en/)  ·  [Français](https://jiangyou2025.github.io/kun/fr/)

A [Jekyll](https://jekyllrb.com/) site about **time series, forecasting and the Kernel U-Net (KUN) model**. It has grown from a small trilingual intro into a small library:

- **Trilingual KUN intro** (English / 中文 / Français) — what a time series is, how to forecast, and how to use KUN.
- **中文入门讲义** (`/course/`) — a 17-lecture course outline.
- **时间序列发展史** (`/history/`) — a narrative “100 years of time series”, a preface + 10 chapters.
- **Three companion essays** (Chinese), each split into one short story per entry:
  - **史前史与当代应用** (`/prehistory/`) — pre-1900 timekeeping, observation and naïve methods.
  - **时间的本质** (`/nature-of-time/`) — 23 cross-disciplinary takes on what *time itself* is.
  - **时间悖论** (`/paradoxes/`) — 15 famous paradoxes of time.
- **Runnable notebooks** (`/notebooks/`) — synthetic-data Jupyter examples.

Served by **GitHub Pages**. Entry points:

- 中文首页 — <https://jiangyou2025.github.io/kun/zh/>
- 入门讲义 — <https://jiangyou2025.github.io/kun/course/>
- 时间序列发展史 — <https://jiangyou2025.github.io/kun/history/>
- 专题：[史前史与当代应用](https://jiangyou2025.github.io/kun/prehistory/) · [时间的本质](https://jiangyou2025.github.io/kun/nature-of-time/) · [时间悖论](https://jiangyou2025.github.io/kun/paradoxes/)

## Site map

```
.
├── _config.yml              # site config (title, baseurl, languages)
├── _data/i18n.yml           # UI strings per language (incl. "updated" label)
├── _layouts/
│   ├── default.html         # trilingual pages: header, nav, language switcher
│   ├── history.html         # 发展史 + essays: sticky topic-aware left sidebar
│   └── lecture.html         # 讲义 pages
├── assets/css/main.css      # styles (dark/light, responsive, figures, game)
├── index.html               # root: redirects to the visitor's language
│
├── en/  zh/  fr/            # trilingual KUN intro — same 4 pages each
│   ├── index.html           #   landing / overview
│   ├── time-series.md       #   what is a time series   (zh: illustration-first)
│   ├── forecasting.md       #   what is forecasting      (zh: figures + a mini-game)
│   └── kun.md               #   using Kernel U-Net       (zh: incl. multi-scale series)
│
├── course/                  # 中文入门讲义 — 17 lectures + index
│   ├── index.md
│   └── 01.md … 15.md
│
├── history/                 # 时间序列发展史
│   ├── index.md             #   directory + filterable timeline
│   ├── foundations.md       #   序 · cross-disciplinary origins
│   └── 01.md … 10.md        #   chapters by decade (1920s → 2020s)
│
├── prehistory.md  + prehistory/    # 专题 · 史前史与当代应用 (directory + stories)
├── nature-of-time.md + nature-of-time/   # 专题 · 时间的本质 (directory + 23 stories)
├── paradoxes.md + paradoxes/       # 专题 · 时间悖论 (directory + 15 stories)
│
├── notebooks/               # runnable Jupyter examples (excluded from the build)
└── Gemfile
```

## Citation

🌟 If you find this resource useful, consider adding a star to this repository and citing our research:

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
- C. Li, J. You, H. Moungla, V. Gauthier, M. Nunez-del-Prado, H. Alatrista-Salas. **Enhancing Spatio-Temporal Forecasting with Spatial Neighbourhood Fusion: A Case Study on COVID-19 Mobility in Peru.** arXiv preprint [arXiv:2507.00031](https://arxiv.org/abs/2507.00031), 2025.
- J. You, X. Wang, A. Cela. **Dynamic Perturbed Adaptive Method for Infinite Task-Conflicting Time Series.** arXiv preprint [arXiv:2505.11902](https://arxiv.org/abs/2505.11902), 2025.
