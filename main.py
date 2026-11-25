#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to the output path (env OUTPUT_PATH,
default /output/entry.txt). Deterministic, standard library only,
no network access.
"""

import os

ENTRY = (
    "The lawmakers who spent six months writing 214 pages of rules for "
    "artificial intelligence still print their own bill, sign it in pen, "
    "and hand it to an intern to scan it back into a PDF."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of gate"
    # One sentence only: a single terminal period, nothing after it.
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    # The roast must stay on brief: lawmakers, their rules, and the PDF.
    lowered = text.lower()
    assert "lawmaker" in lowered, "entry must roast lawmakers"
    assert "pdf" in lowered, "entry must hinge on the PDF conversion"
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Verify the file round-trips byte for byte: what the judge reads is
    # exactly what was validated above.
    with open(output_path, "r", encoding="utf-8") as fh:
        assert fh.read() == text, "written entry does not match validated text"


if __name__ == "__main__":
    main()
