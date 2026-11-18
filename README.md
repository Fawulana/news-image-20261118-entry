[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/Fawulana/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/Fawulana/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

# The World Today — 18 November 2026

A newspaper front page summing up Wednesday 18 November 2026 in one
image, built for the make.fun bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118).

v3 (tuning round 2): the lead story now carries a real image-model
hero photograph — a tanker ablaze in the Gulf at dusk, with a warship
on the horizon — instead of v2's flat drawn illustration, and the
story set is wider: ten stories across war, diplomacy, markets,
climate, sport, disaster and health. Every story was verified against
reporting dated 18 November 2026 before it went on the page.

## Stories on the page

- **U.S. sinks five Iranian tankers** — Gulf war flares: Washington
  says Tehran twice targeted a U.S. warship; Iran says it struck
  10 ships and fired missiles at a U.S. base in Jordan. Oil tops $100.
- **Ukraine strikes Crimea bridge for a second night** — Kyiv says
  the road span is destroyed; Moscow claims a record 1,441 drones
  downed.
- **APEC opens in Shenzhen** — the 33rd leaders' meeting; Trump and
  Putin due ahead of Thursday's first-ever three-way summit.
- **Nvidia tops $100bn** — revenue $115.8bn, double a year ago, as
  Wall Street slides.
- **COP31 talks enter decisive phase** — negotiators in Antalya work
  through a first draft deal.
- **Haaland's late penalty sends Norway through** — Norway rally to
  beat Denmark 3-2; Portugal win 3-2 in Wales.
- **Also today** — 5.3 quake shakes Romania; Peltola wins the Alaska
  Senate seat (Democrats reach 56); UN warns of cold deaths in Gaza;
  Cyclone Akvan turns severe, landfall due Friday; Ebola cases pass
  11,000 in DR Congo.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies the front page (`image.png`, 1024×1024, under 1 MiB) to
`out/entry.png`. The program is Python 3.13, standard library only,
fully offline and deterministic: run it twice and the two outputs are
byte-identical.

## Files

- `main.py` — the entrypoint; copies `image.png` to the output dir.
- `image.png` — the composed front-page artwork (the deliverable).
- `hero.jpg` — the image-model hero photograph used in the lead story.
- `LICENSE` — MIT.
