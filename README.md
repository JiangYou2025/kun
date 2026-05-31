# KUN · Kernel U-Net — documentation site

A small, trilingual (English / 中文 / Français) [Jekyll](https://jekyllrb.com/) website that introduces:

1. **Time series** — the core vocabulary and structure.
2. **Forecasting** — the workflow, from baselines to deep learning.
3. **KUN (Kernel U-Net)** — what the model is and how to use it.

It is built to be served by **GitHub Pages** at `https://jiangyou2025.github.io/kun/`.

## Structure

```
.
├── _config.yml          # site config (title, baseurl, languages)
├── _data/i18n.yml       # UI strings for each language
├── _layouts/default.html# shared layout: header, nav, language switcher, footer
├── assets/
│   ├── css/main.css     # styles (dark/light, responsive)
│   └── favicon.svg
├── index.html           # root: redirects to the visitor's language
├── en/  zh/  fr/        # one folder per language, same three pages each
│   ├── index.html       #   landing / overview
│   ├── time-series.md   #   what is a time series
│   ├── forecasting.md   #   how to forecast
│   └── kun.md           #   using Kernel U-Net
└── Gemfile
```

Adding a language = copy a folder, translate the pages (keep the `ref:` values), and add a block to `_data/i18n.yml` plus the code to `languages:` in `_config.yml`.

## Run locally

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/kun/
```

(Requires Ruby + Bundler. On Windows, install Ruby+Devkit from rubyinstaller.org.)

## Deploy on GitHub Pages

1. Push to the `main` branch of `JiangYou2025/kun`.
2. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Wait ~1 minute; the site goes live at `https://jiangyou2025.github.io/kun/`.

GitHub Pages builds the Jekyll site automatically — no extra Actions workflow needed.

> **Note:** the KUN code snippets are an illustrative *template* of a typical PyTorch training loop. Update the import path, class name and argument names to match the real Kernel U-Net API once the model code is published in this repo.
