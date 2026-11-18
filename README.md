[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/Fawulana/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/Fawulana/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

# The World Today — 18 November 2026

A newspaper front page summing up Wednesday 18 November 2026 in one
image, built for the make.fun bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118).

The front page leads with the day's biggest story — Ukraine's record
1,441-drone overnight barrage, the largest of the war — and carries
three more: the APEC leaders' meeting opening in Shenzhen, Trump
meeting President Marcos in Manila, and Cyclone Akvan turning into a
severe cyclonic storm over the Bay of Bengal. Every story was verified
against reporting dated 18 November 2026 before it went on the page.

## Stories on the page

- **1,441 drones in one night** — Ukraine's biggest drone barrage of
  the war, overnight 17–18 November, first reported 18 November.
- **APEC opens in Shenzhen** — the 33rd APEC leaders' meeting opens
  18–19 November; Xi keynotes, Trump arrives today, and a first-ever
  Trump–Xi–Putin meeting is set for Thursday.
- **Trump meets Marcos today** — in Manila after Tuesday's Quad
  summit, before flying on to Shenzhen.
- **Cyclone Akvan turns severe** — the IMD has it a severe cyclonic
  storm from the morning of 18 November, with landfall due Friday
  20 November on the Andhra coast.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This copies the artwork (`image.png`, 1024×1024, under 1 MiB) to
`out/entry.png`. The program is Node 22, standard library only, fully
offline and deterministic: run it twice and the two outputs are
byte-identical.

## Files

- `main.ts` — the entrypoint; copies `image.png` to the output dir.
- `image.png` — the generated front-page artwork (the deliverable).
- `LICENSE` — MIT.
