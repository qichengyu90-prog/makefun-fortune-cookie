#!/usr/bin/env python3
"""Entry for make.fun's "Fortune Cookie Wisdom for Developers" bounty.

Writes one line of fortune-cookie wisdom (at most 120 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "You will ship on Friday. The bug you fear is already in production, and it is named after you."


def main():
    # Fail fast if the entry ever stops being one line of at most 120 chars.
    if len(LINE) > 120 or "\n" in LINE:
        raise SystemExit("LINE must be one line of at most 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
