"""One-Line Office Joke: 24-Hour Sprint entry.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a fixed string on purpose: the program is deterministic, so
every run produces exactly the same entry the judge will read.
"""

import os

JOKE = "Our standup is fifteen minutes of nine people taking turns saying 'no blockers' while the project quietly blocks itself."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
CHAR_LIMIT = 200


def check(joke):
    """The gate only accepts UTF-8 text of 1 to 200 chars, not only whitespace,
    and the brief wants a single line: no newline may sneak in."""
    if not joke.strip():
        raise ValueError("joke is blank")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if len(joke) > CHAR_LIMIT:
        raise ValueError(f"joke is {len(joke)} chars, over the {CHAR_LIMIT} limit")
    joke.encode("utf-8")
    return joke


def main():
    joke = check(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print(f"Wrote {len(joke)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
