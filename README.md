# The World in One Day — Tuesday, 17 November 2026

Entry for make.fun `news-image-20261117`: sum up the world's news of
Tuesday 17 November 2026 in one image.

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page, "THE WORLD IN
ONE DAY", dated Tuesday, 17 November 2026. It leads with Ukraine's
strike on the Kerch Bridge and covers six more stories from the day:

- Trump lands in Manila for the ASEAN–US Summit and a Quad meeting
- A fourth tanker is hit by a mine in the Strait of Hormuz; Iranian
  drones target a US base in Bahrain
- Cyclone Akvan strengthens over the Bay of Bengal, heading for
  India's Andhra Pradesh coast
- Japan scrambles jets after suspected Russian aircraft enter its
  airspace
- Western nations press Israel to open Gaza aid crossings
- The COP31 draft deal calls for a faster fossil-fuel exit and $120bn
  a year in climate adaptation finance by 2035

Every headline is a real story reported on 17 November 2026 (Reuters,
AFP, AP, IMD and other wire reports). The page was laid out as HTML
(`build/poster.html`) and rendered to PNG with headless Chromium.

## The program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. It uses no network and writes the
same bytes on every run.

## License

MIT — see `LICENSE`.
