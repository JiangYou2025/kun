# KUN · Kernel U-Net —— 文档与学习站点

<p align="center">
  <a href="README.md">🇬🇧 English</a> | <b>🇨🇳 简体中文</b> | <a href="README.fr.md">🇫🇷 Français</a>
</p>

**🔗 在线访问：<https://jiangyou2025.github.io/kun/zh/>** · [English](https://jiangyou2025.github.io/kun/en/) · [Français](https://jiangyou2025.github.io/kun/fr/)

一个关于**时间序列、预测与 Kernel U-Net（KUN）模型**的 [Jekyll](https://jekyllrb.com/) 站点，提供**中文、英文、法文**三种语言。它从一个小小的入门介绍，逐渐长成了一个小型资料库：

- **KUN 入门** —— 什么是时间序列、如何预测、线性自回归、一次成功的预测、数学与机器学习基础，以及 KUN 的原理（可替换的核）。
- **入门讲义**（`course/`）—— 17 讲的时间序列入门课程。
- **时间序列发展史**（`history/`）—— “时间序列百年”：序言、按年代划分的 10 章、72 个小故事和可筛选的时间轴。
- **基础课**（`foundations/`）—— 预备知识地图（数学、统计、计算机、深度学习），每个概念一篇短文。
- **任务史**（`tasks/`）—— 时间序列任务与算力的协同进化。
- **应用**（`applications/`）—— 能源、金融、气象、医疗、交通、零售等领域。
- **三篇专题文章**，每个条目拆成一个短故事：
  - **史前史与当代应用**（`prehistory/`）—— 1900 年以前的计时、观测与朴素方法。
  - **时间的本质**（`nature-of-time/`）—— 从多个学科看“时间本身”是什么。
  - **时间悖论**（`paradoxes/`）—— 关于时间的著名悖论。
- **可运行的 Notebook**（`notebooks/`）—— 基于合成数据的 Jupyter 示例。

由 **GitHub Pages** 托管。中文入口：

- 中文首页 —— <https://jiangyou2025.github.io/kun/zh/>
- 入门讲义 —— <https://jiangyou2025.github.io/kun/course/>
- 时间序列发展史 —— <https://jiangyou2025.github.io/kun/history/>
- 基础课 —— <https://jiangyou2025.github.io/kun/foundations/>
- 专题：[史前史与当代应用](https://jiangyou2025.github.io/kun/prehistory/) · [时间的本质](https://jiangyou2025.github.io/kun/nature-of-time/) · [时间悖论](https://jiangyou2025.github.io/kun/paradoxes/)

## 站点结构

中文是源语言，放在根目录；`en/` 和 `fr/` 逐页镜像（见 [TRANSLATION.md](TRANSLATION.md)）。

```
.
├── _config.yml              # 站点配置（标题、baseurl、语言）
├── _data/
│   ├── i18n.yml  ui.yml     # 各语言的界面文字
│   ├── sidebar.yml          # 各语言的侧边栏标签
│   └── timeline.yml         # 发展史时间轴（中/英/法）
├── _layouts/
│   ├── default.html         # 入门页面：页头、导航、语言切换
│   ├── history.html         # 发展史与专题：按主题的左侧边栏
│   └── lecture.html         # 讲义页面
├── assets/css/main.css      # 样式（深色/浅色、响应式、插图、小游戏）
├── index.html               # 根页面：按访客语言跳转
│
├── zh/                      # 中文 KUN 入门（index、time-series、forecasting、
│                            #   linear-autoregression、prediction-in-action、
│                            #   math-ml-foundations、kernel-u-net、kun）
├── course/  history/  foundations/  tasks/  applications/
├── prehistory/  nature-of-time/  paradoxes/   # 中文长篇内容（及目录 .md）
│
├── en/  fr/                 # 以上全部内容的英文 / 法文镜像
│
├── scripts/check_i18n.py    # 检查每个中文页面都有对应的英/法页面
├── notebooks/               # 可运行的 Jupyter 示例（不参与构建）
└── Gemfile
```

## 引用

🌟 如果这些资料对你有帮助，欢迎给本仓库点个 Star，并引用我们的研究：

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

异常预测相关工作请引用：

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

相关工作：

- J. You, A. Cela, R. Natowicz, J. Ouanounou, P. Siarry. **Robust Time Series Forecasting with Non-Heavy-Tailed Gaussian Loss-Weighted Sampler.** arXiv preprint [arXiv:2406.13871](https://arxiv.org/abs/2406.13871), 2024.
- C. Li, J. You, H. Moungla, V. Gauthier, M. Nunez-del-Prado, H. Alatrista-Salas. **Enhancing Spatio-Temporal Forecasting with Spatial Neighbourhood Fusion: A Case Study on Mobility in Peru.** In *ICASSP 2026 – 2026 IEEE International Conference on Acoustics, Speech and Signal Processing*, 2026. [arXiv:2507.00031](https://arxiv.org/abs/2507.00031)
- J. You, X. Wang, A. Cela. **Dynamic Perturbed Adaptive Method for Infinite Task-Conflicting Time Series.** arXiv preprint [arXiv:2505.11902](https://arxiv.org/abs/2505.11902), 2025.
