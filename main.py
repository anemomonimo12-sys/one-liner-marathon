#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

import os

JOKE = (
    "My smoke alarm only goes off when I cook, which is its way of saying "
    "it trusts the fire department more than it trusts me."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
