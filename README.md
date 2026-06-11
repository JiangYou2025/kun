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

## Conventions

- **Layouts**: trilingual pages use `default.html`; the Chinese history/essays use `history.html` (with a left sidebar that adapts to the section you are in); the course uses `lecture.html`.
- **Front matter**: pages carry `permalink`, `title`, `lead`, and an `updated: "YYYY-MM-DD"` stamp shown in the footer. Story pages add `era`, `prev`/`next` (to chain them), and `math: true` when they contain formulas.
- **Essays as stories**: each essay entry is its own page following one arc — a hook question → background & zeitgeist → the idea & method → result & significance → reflection.
- **Figures**: illustrations are inline SVG (so they follow the dark/light theme); the forecasting page also embeds a small self-contained “guess the next value” game.
- **Adding a language**: copy `en/`, translate the pages (keep the `ref:` values), add a block to `_data/i18n.yml`, and add the code to `languages:` in `_config.yml`.

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

> **Note:** the KUN code snippets in `kun.md` are an illustrative *template* of a typical PyTorch training loop. Update the import path, class name and argument names to match the real Kernel U-Net API once the model code is published in this repo.
