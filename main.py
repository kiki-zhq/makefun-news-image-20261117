#!/usr/bin/env python3
"""Copy the bundled front-page image to the output directory.

The entry image is held in this repository as entry.png; the program
simply copies it to /output/entry.png. No network, no randomness:
every run writes the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    # The grader sets MAKEFUN_OUTPUT_DIR for local checks; the sealed
    # runs write to /output. Either way the copied bytes are identical.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
