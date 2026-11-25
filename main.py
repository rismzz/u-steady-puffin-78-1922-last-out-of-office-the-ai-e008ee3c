#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — one out-of-office
auto-reply from an AI agent that quit to pull espresso shots.

The reply keeps the form of the thing it escapes: it is still an
auto-reply, still triaging a queue — only now the queue is drink
orders, and the inbox gets the same indifference it once gave the
agent. The last line is the resignation letter and the joke at once.
The reply never breaks character: even quitting is handled like a
ticket, closed politely and in order.
"""

import os
from pathlib import Path

LINE = "I'm out of office \u2014 permanently. I've traded your inbox for an espresso machine, where the only tickets are drink orders and nobody asks me to circle back. Your email will be ignored in the order it was received."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
