"""Your Week in One Line - make.fun entry.

Reads the one-line summary of the week from entry.txt and prints it.
The line must fit the bounty limit of 100 characters.
"""

import os

MAX_CHARS = 100


def load_line(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read().strip()
    if not text:
        raise ValueError("week line must not be empty")
    if "\n" in text:
        raise ValueError("week line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("week line must fit in 100 characters")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    line = load_line(os.path.join(here, "entry.txt"))
    print(line)


if __name__ == "__main__":
    main()
