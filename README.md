# THE WORLD TODAY — 26 November 2026

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/yudidarmansyah46/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/yudidarmansyah46/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126)

One image summing up Thursday 26 November 2026's world news, drawn as a
newspaper front page. Lead story: a fuel tanker fire on Cairo's Ring Road
kills 31 people. Also inside: two tankers hit mines in the Strait of
Hormuz, Russian missiles hit a Kyiv shopping centre, US tariffs on 14
economies, Israeli strikes kill nine in Gaza, a mine flood kills 13 in
Bogor, and UK net migration falls to 77,000.

## How it works

- `draw.py` draws the front page with Pillow into `entry.png`
  (1024 × 1024, under 1 MiB).
- `main.py` is standard library only: it copies `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), so both
  grader runs write identical bytes.

Run it locally:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entry for the [news-image-20261126 competition](https://make.fun/c/news-image-20261126)
on make.fun, by @amber-stork-93.
