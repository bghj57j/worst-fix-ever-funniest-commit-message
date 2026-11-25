# Writes the one-line commit message to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# A fix that made things worse: the warning is gone because its warner is.
# Reads like a real commit subject a tired engineer would type.
import os
LINE = "fix: silenced the warning by deleting the code that warned us"
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run; entry is 61 chars, gate allows 100
