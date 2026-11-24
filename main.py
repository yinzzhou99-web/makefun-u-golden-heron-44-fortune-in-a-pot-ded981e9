#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Stdlib only. Writes one good and funny fortune for a houseplant on a
windowsill to /output/entry.txt. Clears nothing; the grader owns /output.
"""

from pathlib import Path

LINE = "Good fortune grows toward you: a sunny spot, a gentle watering, and a human who finally reads the care tag."

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to /output/entry.txt")
