#!/usr/bin/env python3
"""The Best Advice I Ever Got: one sentence about the best advice ever received.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The advice: Dad's test for trustworthiness -- a man who cannot admit he
# is wrong -- and the turn is that twenty years later the writer still
# applies it first, before anything else. Specific, earned, a real voice
# recalling a real moment; no slogan, no fortune cookie.
LINE = "My dad told me: never trust a man who won't admit he's wrong — twenty years on, I still check for that first."


def get_line() -> str:
    """Return the entry line."""
    return LINE


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the line to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the sealed scorer needs 1-200 chars, UTF-8, not only
    whitespace, exactly one clean line. Fail loudly here rather than ship
    an invalid entry."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    line.encode("utf-8")
    assert line.strip() == line and "\n" not in line and "\r" not in line, \
        "must be one clean line"


def main() -> None:
    line = get_line()
    validate_line(line)
    write_entry(line)


if __name__ == "__main__":
    main()
