#!/usr/bin/env python3
"""Invent a Word We Need — writes one invented word and its one-line
definition to /output/entry.txt.

Stdlib only, deterministic.
"""

import os

LINE = "Planfall \u2014 the quiet relief when a plan you dreaded falls through."


def main():
    # Validate against the sealed scorer's gate before writing: the entry
    # must be 1-140 characters of UTF-8 text, not only whitespace, and a
    # single line, or it scores 0 and never reaches the judge. It must also
    # be one invented word plus its definition: a single word before the
    # em dash, so a multi-word phrase can never slip in as the "word".
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    word, sep, definition = LINE.partition("\u2014")
    if not sep or len(word.split()) != 1 or not definition.strip():
        raise ValueError("line must be one word, an em dash, and a definition")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
