"""Make the AI Judge Laugh: office life, one line, under 200 characters.

The entry is a single funny line about office life: a meeting is replaced
by an email, then a meeting is held about the email, then the minutes are
emailed to nobody who reads them -- a three-beat escalation that is true
to office life and lands on a surprising last word.

The program checks the line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "We replaced the meeting with an email, then held a meeting about "
    "the email, then emailed the minutes nobody read."
)


def validate(line: str) -> None:
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip() == line and line.strip(), "entry must not be blank"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
