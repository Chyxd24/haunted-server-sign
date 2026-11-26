#!/usr/bin/env python3
"""Entry generator for: Funniest Sign on a Haunted Server Room Door.

Writes a single line (<=120 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only. The judged artifact is the exact bytes of entry.txt.
"""
import os

# The entry line itself. Kept as a named constant so later revisions are a
# one-line edit against the judge brief's 120-char cap.
ENTRY_LINE = "NOTICE: The ghost in Rack 3 is load-bearing. Do not exorcise. Last exorcism took the DNS down for a week."


def build_entry() -> str:
    """Return the entry text, enforcing the competition's hard char cap."""
    text = ENTRY_LINE.strip()
    cap = 120
    if len(text) > cap:
        raise ValueError(
            f"entry is {len(text)} chars, over the {cap}-char cap: {text!r}"
        )
    if not text:
        raise ValueError("entry text is empty")
    # The judge wants a real sign: it should read aloud in one breath with no
    # filler. Trim stray whitespace and double spaces that survive editing.
    text = " ".join(text.split())
    if len(text) > cap:
        raise ValueError(f"normalized entry is {len(text)} chars: {text!r}")
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = build_entry()
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)
    print(f"wrote {len(entry)} chars -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
