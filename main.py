#!/usr/bin/env python3
"""Worst AI Advice entry: one line of terrible advice, written to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

ENTRY = "Quick tip: to charge your phone faster, microwave it for 30 seconds \u2014 the waves top up the battery."


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    # No trailing newline: the gate counts every character of entry.txt,
    # so the file holds exactly the one line and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
