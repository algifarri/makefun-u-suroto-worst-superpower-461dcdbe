#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes a single line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = "I can fold a fitted sheet perfectly \u2014 but only in my dreams, and I forget how the second I wake up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
