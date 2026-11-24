"""The One-Line Exit — entry program.

Prints one line: a resignation letter from a royal food taster whose
notice period is conditional on surviving lunch. The line is 134
characters, inside the competition's 1-140 gate. When the make.fun
program harness is present, the same text is also written to
/output/entry.txt, which is where the harness reads the artifact.
"""

import os
import sys

ENTRY = (
    "Your Majesty, I resign as your food taster, effective immediately "
    "after lunch; if lunch goes well, consider this my two weeks' notice."
)

# The gate, checked silently: one line, 1-140 characters, not blank.
assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 140 and ENTRY.strip()


def main() -> None:
    sys.stdout.write(ENTRY + "\n")
    out_dir = "/output"
    if os.path.isdir(out_dir):
        try:
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(ENTRY + "\n")
        except OSError:
            pass  # stdout already carries the entry; never fail the run.


if __name__ == "__main__":
    main()
