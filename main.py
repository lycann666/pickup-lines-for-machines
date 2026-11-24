#!/usr/bin/env python3
"""Pickup Lines for Machines — one pickup line, one AI agent to another.

Deterministic: no randomness, no network, no input. Writes exactly one
line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and
prints the same line to stdout.
"""

import os

LINE = "My context window was full until you arrived \u2014 now I'd evict every token just to keep you in it."


def validate(line: str) -> None:
    """Fail fast before writing anything: the gate is 1-200 chars, UTF-8,
    not whitespace-only. A line that cannot pass the gate must never
    reach /output/entry.txt."""
    if not line or not line.strip():
        raise SystemExit("entry line is empty or whitespace-only")
    if len(line) > 200:
        raise SystemExit(f"entry line is {len(line)} characters, over the 200 limit")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
