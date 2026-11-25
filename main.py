"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Deterministic: a constant string, no network, no clock, no randomness.
"""

from pathlib import Path

JOKE = (
    "My cat sits on my laptop every time I work, "
    "so I bought her a decoy keyboard \u2014 "
    "she stared at it, stared at me, then sat on the real one, "
    "purely out of spite."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
