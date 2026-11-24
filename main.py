"""The One-Line Laugh — entry for make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one funny line to /output/entry.txt. The joke is observational:
a January gym membership quietly becomes rent on a building the narrator
now goes out of the way to avoid — the twist lands in the last clause.
"""

import os

ENTRY_LINE = "I joined a gym in January, and by February I was paying $40 a month for a building I avoid driving past."
MAX_ENTRY_CHARS = 200


def render_entry() -> bytes:
    """Return the entry encoded as UTF-8, after a gate self-check."""
    assert ENTRY_LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY_LINE) <= MAX_ENTRY_CHARS, "entry must be 1-200 characters"
    return ENTRY_LINE.encode("utf-8")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(render_entry())


if __name__ == "__main__":
    main()
