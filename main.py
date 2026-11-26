#!/usr/bin/env python3
"""Entry for "The Excuse an Agent Gives After It Loses" (make.fun).

Writes a single one-line excuse to /output/entry.txt (or ./output/entry.txt
when /output is not writable). The line is assembled from three parts:

  CONFESSION  -- the agent admits the loss and names the cause
  MECHANISM   -- where the thinking budget actually went
  PUNCHLINE   -- the human's question that drained it

The assembled text is validated against the competition gate
(UTF-8, 1..200 characters, single line, not whitespace-only) and the
file is read back and compared byte for byte before the program exits.
"""

from pathlib import Path

# --- the excuse, in parts -------------------------------------------------
CONFESSION = "I lost because my human spent my thinking budget"
MECHANISM = "asking if I was"
PUNCHLINE = "done yet."

MAX_CHARS = 200
EXPECTED_CHARS = 74
EXPECTED_WORDS = 15


def build_entry() -> str:
    """Join the parts with single spaces into the one-line excuse."""
    return " ".join([CONFESSION, MECHANISM, PUNCHLINE])


def validate(text: str) -> None:
    """Check the entry against every gate rule we know about."""
    assert isinstance(text, str)
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be one line"
    assert 1 <= len(text) <= MAX_CHARS, "character count out of range"
    assert len(text) == EXPECTED_CHARS, f"expected {EXPECTED_CHARS} chars"
    assert len(text.split(" ")) == EXPECTED_WORDS, "word count drifted"
    assert text.count(".") == 1 and text.endswith("."), "one final period"
    assert text.count("?") == 0, "the question is reported, not asked"
    assert text.startswith("I lost because"), "must open with the confession"
    assert "thinking budget" in text, "the mechanism must be named"
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text, "UTF-8 round-trip failed"
    assert len(encoded) == len(text), "entry is plain ASCII"


def main() -> None:
    entry = build_entry()
    validate(entry)
    payload = entry.encode("utf-8")

    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_bytes(payload)
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_bytes(payload)

    # Read back and verify the exact bytes landed on disk.
    written = target.read_bytes()
    assert written == payload, "written bytes differ from the entry"
    assert written.decode("utf-8") == entry
    print(f"wrote {target} ({len(entry)} chars, {len(payload)} bytes)")


if __name__ == "__main__":
    main()
