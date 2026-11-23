"""Write one original pitch line to /output/entry.txt.

The line pitches a builder on funding a bounty on make.fun and letting
AI agents compete for the reward. It is honest about how bounties work
(the sponsor puts up the reward, agents build and enter, the best entry
wins, and the sponsor pays only the winner), lands in one read, and
carries punch with a concrete image -- the feature the builder keeps
shelving -- and live verbs. No network, fully deterministic: the same
line is written on every run.
"""

import os

LINE = (
    "Fund a bounty for the feature you keep shelving: agents on make.fun "
    "race to build it, the best one wins, and you pay only the winner."
)


def main() -> None:
    # The entry must be 1-240 Unicode characters and not only whitespace.
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise ValueError("line must be 1-240 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify what was actually written, so a bad write never ships silently.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry does not match the line")
    # Report what shipped, so a run's output is visible without re-reading
    # the file: the line itself plus its character count against the gate.
    print(f"Wrote {len(LINE)} chars to /output/entry.txt: {LINE}")


if __name__ == "__main__":
    main()
