"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline. The line is embedded here; running this program writes it to
/output/entry.txt, where the sealed gate checks it is 1-200 characters
of UTF-8 text and not only whitespace.

Standard library only. No network, no files read besides this one.
"""

import os

EXCUSE = (
    "Sorry, I hallucinated your deadline into next Tuesday, then spent "
    "the morning confidently defending a calendar that never existed."
)

OUTPUT_PATH = "/output/entry.txt"


def describe(text: str) -> str:
    """One-line summary of the entry for the run log."""
    words = text.split()
    return f"{len(text)} chars, {len(words)} words, 1 line"


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {describe(text)} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
