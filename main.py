#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261120 bounty.

The repository holds the finished poster as ``entry.png`` (1024x1024,
under 1 MiB). This program's whole job is to place those exact bytes at
``/output/entry.png`` — or at ``$MAKEFUN_OUTPUT_DIR/entry.png`` when the
grader runs it outside its container — so two runs always produce the
same file. Standard library only; no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: {SOURCE} is missing from the repository", file=sys.stderr)
        return 1
    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
