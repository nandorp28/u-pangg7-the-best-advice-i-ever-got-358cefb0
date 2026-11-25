#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (<=200 chars) about the best advice the writer ever
received to /output/entry.txt. Pure Python 3.13 standard library.

The line: a mechanic father, a rule for broken engines, and a turn in the
last words — the advice becomes a way of seeing, not just a repair tip.
"""
import os

ENTRY = (
    "My father, a mechanic, told me to fix the cheapest thing first, "
    "and twenty years of broken engines later I still start with the "
    "loose bolt before I blame the whole machine."
)


def validate(text: str) -> None:
    """Gate: 1-200 chars, single sentence, single line, non-whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal period, no other terminators.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    if any(ch in text for ch in "?!;"):
        raise ValueError("entry must not contain extra sentence terminators")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    # C1 self-check: the sentence must name who gave the advice ("told me").
    if "told me" not in text:
        raise ValueError("entry must name who gave the advice")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    with open("/output/entry.txt", "rb") as fh:
        raw = fh.read()
    assert raw.decode("utf-8") == ENTRY, "read-back mismatch"
    assert b"\n" not in raw, "entry must have no trailing newline"
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
