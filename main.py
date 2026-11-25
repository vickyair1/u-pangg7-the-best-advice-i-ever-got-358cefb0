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


def main() -> None:
    # Gate guard: the sealed scorer needs 1-200 chars, UTF-8, not only
    # whitespace, exactly one sentence. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
