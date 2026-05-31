# 动手案例 (Hands-on notebooks)

配合「[时间序列入门](https://jiangyou2025.github.io/kun/course/)」讲义的可运行 Jupyter 案例。全部使用**合成数据**，无需下载任何数据集，克隆即可运行。

| 案例 | 主题 | 对应讲义 |
|------|------|----------|
| [`01_explore_and_decompose.ipynb`](01_explore_and_decompose.ipynb) | 探索、滚动统计、加法分解、ACF | 第 3、4 讲 |
| [`02_forecasting_baselines.ipynb`](02_forecasting_baselines.ipynb) | 时间切分、基线模型、MAE/RMSE/MAPE、滚动回测 | 第 7、8 讲 |
| [`03_kun_style_window_forecast.ipynb`](03_kun_style_window_forecast.ipynb) | 滑动窗口 + 神经网络直接多步预测（KUN 思想） | 第 11、14 讲 |

## 运行

```bash
pip install -r notebooks/requirements.txt
jupyter lab        # 或 jupyter notebook
```

> 案例 1、2 只需 `numpy / pandas / matplotlib`；案例 3 额外需要 `torch`。
>
> 案例 3 里的 `LinearForecaster` 是 KUN 最简单的 kernel；要换成真正的模型，见 [使用 KUN](https://jiangyou2025.github.io/kun/zh/kun/)。
