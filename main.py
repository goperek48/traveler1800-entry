#!/usr/bin/env python3
"""Write one sentence about the internet for a traveler from 1800.

A visitor stepping out of the year 1800 gets a single sentence, no more
than 200 characters, that has to make the modern internet click for
them. The brief is strict about how: nothing coined after their own
century, no catalogue of features, just one scene they can picture and
carry away.

So the sentence reaches for the three places such a traveler already
trusts — the library where knowledge is kept, the post office where
words travel, the market where goods change hands — and ties them
together with roads they cannot see. That is the honest shape of the
thing: distant people and distant shelves linked so that a message or
a picture arrives faster than a blink. The program itself is trivial
on purpose: no input, no network, no randomness, one constant holding
the sentence and a short main that drops it into /output/entry.txt.
"""

import os
import sys

# The entry itself. Each of the three old institutions carries one part
# of the meaning: the library is the internet as a store of knowledge,
# the post office is the internet as a carrier of messages, and the
# market is the internet as a place where people buy and sell. Roads
# are the traveler's own mental model of connection, so "invisible
# roads" does the bridging work in words they already own — and it stays
# honest, because the internet really is paths joining all of those
# places at once. A letter, a book, and a picture stand for the three
# kinds of cargo those roads carry, and the closing phrase, "in the
# blink of an eye", is the one meant to still be there a week later.
# 170 characters, a single sentence, and no word younger than 1800.
ENTRY = "Imagine every library, post office, and market in the world joined by invisible roads, so any letter, book, or picture can reach anyone, anywhere, in the blink of an eye."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
