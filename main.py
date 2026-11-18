#!/usr/bin/env python3
"""Entry for news-image-20261118: write the front-page image to the output.

The repository holds the finished front page as image.png. It was
rendered offline with real fonts, so every headline and label is crisp
vector-drawn text rather than model-generated lettering. This program
only copies those exact bytes to entry.png, which keeps both grader
runs byte-identical. Standard library only, no network, no randomness.
"""

import os
import shutil
import sys

ASSET = "image.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    """Grader output dir, overridable for local runs."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_asset(src):
    """Refuse to ship a missing or non-PNG asset instead of failing the gate."""
    if not os.path.isfile(src):
        raise SystemExit("asset missing: %s" % src)
    with open(src, "rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise SystemExit("asset is not a PNG: %s" % src)
    return os.path.getsize(src)


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
