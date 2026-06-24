# 动手案例

配合「[时间序列入门](https://jiangyou2025.github.io/kun/course/)」讲义的可运行 Jupyter 案例。全部使用**合成数据**，无需下载任何数据集，克隆即可运行。

| 案例 | 主题 | 对应讲义 |
|------|------|----------|
| [`01_decompose_trend_season.ipynb`](01_decompose_trend_season.ipynb) | 序列分解：趋势与周期性、滚动统计、加法分解、ACF | 第 4、5 讲 |
| [`02_linear_from_scratch.ipynb`](02_linear_from_scratch.ipynb) | 从零手写线性预测：设计矩阵、矩阵乘法、最小二乘正规方程、梯度下降 | 第 3、4 讲 |
| [`03_insect_trajectory.ipynb`](03_insect_trajectory.ipynb) | 昆虫二维轨迹：单步预测 + 自回归滚动（Linear/MLP/RNN/LSTM/GRU/Transformer） | 第 9 讲 |
| [`04_insect_multistep_kun.ipynb`](04_insect_multistep_kun.ipynb) | 多步预测：直接多输出，并引入 **KUN (Kernel U-Net)** | 第 9、11 讲 |
| [`05_adaptive_forecasting.ipynb`](05_adaptive_forecasting.ipynb) | 自适应预测：KUN 跨通道（channel）泛化（**骨架，待完成**） | 第 11 讲 |
| [`06_mnist_cv_intro.ipynb`](06_mnist_cv_intro.ipynb) | 计算机视觉入门：MNIST 手写数字分类（MLP vs CNN、混淆矩阵、错误样本）——**视频案例** | — |
| [`07_char_language_model.ipynb`](07_char_language_model.ipynb) | 字符级语言任务：把「预测下一个值」换成「预测下一个字符」——bigram 计数基线 → 神经 bigram → 带上下文的 MLP → 文本生成 | 第 3、9 讲 |

> 案例 03、04 是英文作业（TP），保持英文；其余为中文。
>
> 案例 06 会用 `torchvision` 自动下载 MNIST（约 11 MB）到 `notebooks/data/`，需联网一次。

## 运行

```bash
pip install -r notebooks/requirements.txt
jupyter lab        # 或 jupyter notebook
```

> 案例 01、02 只需 `numpy / pandas / matplotlib`；案例 03、04、05、06、07 额外需要 `torch`（案例 07 仅用内置文本，无需下载）。
>
> 案例 04 / 05 里的 KUN 是一个最简实现（线性核）。要换成仓库里真正的 KUN，见 [使用 KUN](https://jiangyou2025.github.io/kun/zh/kun/)。
