#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic: no randomness, no network, no clock.

How the joke is built: it takes a mundane household annoyance (a smoke
alarm that only ever sounds while its owner cooks) and reframes it as a
judgement call — the alarm is not malfunctioning, it has simply decided
the cook is less reliable than the fire department. The punchline lands
by personifying the alarm and letting its "trust" do the insult, so the
whole gag fits in one self-contained sentence with a setup ("only goes
off when I cook") and a payoff ("trusts the fire department more than
it trusts me").
"""

import os

JOKE = (
    "My smoke alarm only goes off when I cook, which is its way of saying "
    "it trusts the fire department more than it trusts me."
)


def validate_entry(line: str) -> str:
    """Check the entry line meets the competition gate before writing.

    The line must be a single non-blank line of 1-280 characters.
    Raises ValueError if the gate is not met, so a bad entry is never
    written to disk.
    """
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(line) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(line)}")
    return line


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    validate_entry(JOKE)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
