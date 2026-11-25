# make.fun — "Famous Last Words: The Funniest Epitaph"
# Writes one one-line tombstone epitaph (famous last words, at most
# 150 characters) to /output/entry.txt.
# Deterministic: the text is a constant. No randomness, no clock,
# no network, no environment input. Standard library only.
import os
import sys

TEXT = (
    "Here lies a man who died doing what he loved: "
    "refreshing the tracking page for a package that never arrived."
)

# The gate requires UTF-8 text of 1 to 150 characters, not only
# whitespace, on a single line.
assert "\n" not in TEXT, "epitaph must be a single line"
assert 1 <= len(TEXT) <= 150, f"epitaph must be 1-150 characters, got {len(TEXT)}"
assert TEXT.strip() == TEXT, "epitaph must not be only whitespace"


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    ) + "/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: output re-verified after the first draft — same single line, same length, byte-identical on repeated runs.
