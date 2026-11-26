"""Deadpan forecast for a city that does not exist.

Writes one line (138 characters) to /output/entry.txt: a deadpan TV
weather forecast for Quibblewick, where the rain is unposted letters
and one postman is 40 years behind schedule.
"""

import os
from pathlib import Path

ENTRY = (
    "In Quibblewick, expect heavy rain of unposted letters, "
    "highs of 11 degrees, and one postman finally catching up "
    "on 40 years of deliveries."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
