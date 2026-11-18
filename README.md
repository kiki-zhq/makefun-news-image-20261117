# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/kiki-zhq/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/kiki-zhq/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

"The World in One Day" — a newspaper front page summing up Tuesday 17 November 2026 in one image. Entry for make.fun `news-image-20261117`.

`entry.png` (1024×1024, PNG) leads with Ukraine's strike on the Kerch Bridge and covers six more stories from the day:

- Trump lands in Manila for the ASEAN–US Summit and a Quad meeting
- A fourth tanker is hit by a mine in the Strait of Hormuz; Iranian drones target a US base in Bahrain
- Cyclone Akvan strengthens over the Bay of Bengal, heading for India's Andhra Pradesh coast
- Japan scrambles jets after suspected Russian aircraft enter its airspace
- Western nations press Israel to open Gaza aid crossings
- The COP31 draft deal calls for a faster fossil-fuel exit and $120bn a year in climate adaptation finance by 2035

Every headline is a real story reported on 17 November 2026 (Reuters, AFP, AP, IMD and other wire reports). The page was laid out as HTML (`build/poster.html`) and rendered to PNG with headless Chromium.

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png` to `/output/entry.png`. It uses no network and writes the same bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t49c36pe&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
