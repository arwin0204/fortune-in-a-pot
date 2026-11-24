"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant on the windowsill
to /output/entry.txt. Deterministic: the same text on every run.
No network, no dependencies, Python 3.13 standard library only.
"""

import hashlib
import os
import sys

MAX_LENGTH = 120

ENTRY = (
    "This windowsill was made for you: expect sunny mornings, "
    "one proud new leaf, and a keeper who brags about you daily."
)


def check_single_line(text: str) -> None:
    """Reject blank or multi-line text."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_length(text: str) -> None:
    """Reject text over the 120-character limit."""
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_LENGTH} limit"
        )


def validate_entry(text: str) -> str:
    """Check the entry meets the gate: 1-120 chars, one line, not blank."""
    check_single_line(text)
    check_length(text)
    return text


def write_entry(path: str, text: str) -> None:
    """Write the entry text to path as UTF-8, no trailing newline."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    entry = validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    write_entry(path, entry)
    digest = hashlib.sha256(entry.encode("utf-8")).hexdigest()
    print(f"wrote {path} ({len(entry)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
