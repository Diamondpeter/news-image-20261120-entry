# news-image-20261120-entry

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Diamondpeter/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Diamondpeter/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The Planet in One Picture — Friday 20 November 2026

One image that sums up the world news of **Friday 20 November 2026**:
a single dominant lead visual under a headline built to stop a scroll,
the day's other stories numbered and pinned on a world map, a Day in
Numbers strip, and a sources line at the foot — so a viewer who missed
the day can tell what happened from the picture alone.

This repository is an entry in make.fun's bounty
[**"Sum up 20 November's world news in one image"**](https://make.fun/bounty/news-image-20261120)
($250 in USDC, deadline Sun 22 November 2026, 01:00 Africa/Lagos).

The lead: Cyclone Akvan comes ashore near Gopalpur in Odisha after more
than 300,000 people were moved to safety — drawn as one huge storm
spiral over the coast. Around it, 26 stories from six continents:
COP31's closing day in Antalya, Anthropic's record first close in New
York, a history-making hundred in Wellington, embassies hit in Kyiv,
a capsized pirogue off Senegal, a drought emergency in Tonga, and more.

## How it runs

- `entry.png` — the finished image: a PNG, exactly 1024×1024, at most 1 MiB.
- `main.py` — Python 3.13, standard library only, no network. It copies
  `entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR/entry.png`
  outside the grader's container). Two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Design

- White poster, black ink, one red accent — a broadsheet front page.
- Masthead: "FRIDAY 20 NOVEMBER 2026" + "THE PLANET IN ONE PICTURE".
- One scroll-stopping lead story filling the top of the frame, its
  headline large enough to read at 300 px across.
- A world map with numbered pins, and a numbered grid of the day's
  stories that traces pin-to-story.
- A "Day in Numbers" strip of the day's hardest figures.
- Foot folio: "Compiled from reports by …" naming the day's sources.

## License

MIT — see [LICENSE](LICENSE).
