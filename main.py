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


def _check_entry(text: str) -> str:
    """Guard the forecast: one non-blank line, within the 160-char cap."""
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(_check_entry(ENTRY), encoding="utf-8")


if __name__ == "__main__":
    main()
