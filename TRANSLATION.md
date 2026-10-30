# Translating the Chinese pages into English and French

Most of the site (history, timeline entries, course, foundations, the essays, applications, tasks, and the extra `zh/` KUN pages) was written in Chinese first. Each page gets an English and a French mirror under `en/` and `fr/`. The Chinese page stays at its current URL.

Check progress at any time:

```bash
python scripts/check_i18n.py          # summary + problems in existing translations
python scripts/check_i18n.py --todo   # also list pages still to translate
```

## Where a translation goes

| Chinese source | English target | URL |
|---|---|---|
| `history/03.md` | `en/history/03.md` | `/en/history/03/` |
| `history/entries/kalman.md` | `en/history/entries/kalman.md` | `/en/history/e/kalman/` |
| `prehistory.md` | `en/prehistory.md` | `/en/prehistory/` |
| `paradoxes/twin.md` | `en/paradoxes/twin.md` | `/en/paradoxes/twin/` |
| `tasks/index.md` | `en/tasks/index.md` | `/en/tasks/` |
| `zh/kernel-u-net.md` | `en/kernel-u-net.md` | `/en/kernel-u-net/` |

The four original intro pages (`zh/index.html`, `time-series`, `forecasting`, `kun`) already had en/fr versions, but the Chinese ones have since been rewritten and expanded. Their en/fr versions are re-translated from the current Chinese, keeping the same file names.

The rule: put the same relative path under `en/` or `fr/`, and prefix the permalink with `/en` or `/fr`. A `zh/` page drops its `zh/` folder. French follows the same pattern under `fr/`.

## Front matter

- `lang: en` or `lang: fr`, and the prefixed `permalink`.
- Translate `title`, `lead` and `era`.
- Keep `layout`, `math`, `ref`, `no_comments` and `updated` exactly as in the source. Keeping `updated` makes a stale translation detectable: if the Chinese page's date moves past it, the translation needs a refresh.
- Keep `prev` and `next` **unchanged** (for example `/paradoxes/ladder-barn/`). The layouts add the `/en` or `/fr` prefix themselves.

## Body

- Translate everything a reader sees: prose, headings, tables, image `alt` text, text inside inline `<svg>`, HTML attributes such as `title` and `aria-label`, and comments and strings in code blocks.
- Do not change code logic, math (`$…$`, `$$…$$`), HTML/SVG structure, CSS classes, ids or numbers.
- Use the original-language names of people, works and methods: 柯尔莫哥洛夫 → Kolmogorov, 《时间简史》 → *A Brief History of Time*, 指数平滑 → exponential smoothing. Use the standard French technical terms (lissage exponentiel, réseau de neurones, apprentissage profond, série temporelle).
- Chinese typography becomes the target language's: `“…”` → "…" in English, « … » in French (with non-breaking spaces before `: ; ? !` in French), `——` → em dash, `、` → comma.
- Write natural, fluent text. Restructure sentences when needed, but do not add or drop content.

## Links

- Relative links between mirrored pages stay as they are. For example, `../04/` from `en/history/entries/kalman.md` correctly reaches `/en/history/04/`.
- Links into the Chinese KUN pages must point to the same-language page. From `history/index.md`, `../zh/kun/` becomes `../kun/` (that is, `/en/kun/`). From an entry, `../../zh/kun/` becomes `../../kun/`.
- In Liquid URLs, add the prefix: `'/history/e/' | append: …` becomes `'/en/history/e/' | append: …`, and `'/zh/kernel-u-net/'` becomes `'/en/kernel-u-net/'`.
- Anchors that contain Chinese (`#时间线-timeline`) must point to the translated heading's id (kramdown: lowercase ASCII words joined by `-`). If you are unsure, drop the anchor.
- `python scripts/check_i18n.py en/xxx.md` must report no problems other than links to pages that are not translated yet.

## Data and layouts

- `_data/ui.yml`: layout strings (navigation, pager, footer) per language.
- `_data/sidebar.yml`: left-sidebar labels per language.
- `_data/timeline.yml`: each entry has `contribution_en` and `contribution_fr`. The translated `history/index.md` uses them.
