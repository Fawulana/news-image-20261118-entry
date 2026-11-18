#!/usr/bin/env python3
"""Entry for news-image-20261118: write the front-page image to the output.

The repository holds the finished front page as image.png: an
image-model hero photograph of a tanker ablaze in the Gulf, composed
with crisp programmatic text (masthead, date, headlines, ticker) that
was rendered offline with real fonts, so no lettering is garbled.
The lead photograph itself is kept in the repository as hero.jpg;
image.png is the composed front page that carries it.
This program only copies those exact bytes to entry.png, which keeps
both grader runs byte-identical. Standard library only, no network,
no randomness.
"""

import os
import shutil
import sys

ASSET = "image.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def output_dir():
    """Grader output dir, overridable for local runs."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_asset(src):
    """Refuse to ship a missing, oversized or non-image asset."""
    if not os.path.isfile(src):
        raise SystemExit("asset missing: %s" % src)
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise SystemExit("asset over 1 MiB: %s (%d bytes)" % (src, size))
    with open(src, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if not (head.startswith(PNG_MAGIC) or head.startswith(JPEG_MAGIC)):
        raise SystemExit("asset is not a PNG or JPEG: %s" % src)
    return size


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ASSET)
    expected = check_asset(src)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != expected:
        raise SystemExit("short copy: %s" % dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
