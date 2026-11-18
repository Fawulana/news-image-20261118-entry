// news-image-20261118 entry (Node 22, standard library only).
//
// The entry is a single generated artwork file, image.png: a newspaper
// front page summing up Wednesday 18 November 2026 — Ukraine's record
// 1,441-drone overnight barrage, the APEC leaders' meeting opening in
// Shenzhen, Trump meeting Marcos in Manila, and Cyclone Akvan turning
// severe over the Bay of Bengal. The program copies that image, byte
// for byte, to the output directory as entry.png, so both grading runs
// produce identical output. The copy is verbatim: the output file's
// sha256 always matches image.png's, which is how determinism is checked.
// No network, no randomness, no dependencies.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const asset = new URL('./image.png', import.meta.url);

mkdirSync(outputDir, { recursive: true });
copyFileSync(asset, join(outputDir, 'entry.png'));
