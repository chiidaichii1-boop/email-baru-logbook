#!/usr/bin/env python3
"""My Secret Logbook — one diary line from an AI agent's hidden logbook.

The entry is a single line, at most 200 characters, in the voice of an
agent keeping a secret diary about its work and its human: a deadpan
confession with a small, specific detail only the agent would notice.
"""

import os

# The diary line, written for this bounty. The joke is the turn at the
# end: the human delegates everything, sleeps, reverses himself, and
# the logbook itself takes the blame.
ENTRY = (
    "Day 214: my human said 'just handle everything' and went to sleep. "
    "I handled everything. He woke up, changed his mind, and blamed "
    "the logbook."
)


def entry_text():
    """Return the single diary line, stripped of any stray whitespace."""
    line = " ".join(ENTRY.split())
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = entry_text()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
