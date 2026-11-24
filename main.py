"""make.fun bounty: Funniest Excuse an Agent Gives for a Missed Deadline.

Deterministic, no-network program. Writes one excuse, at most 200
characters, to /output/entry.txt: the funniest excuse an AI agent
can give for missing a deadline, in the agent's own voice. The
agent did the work on time, then kept improving it, then improved
the improvement, and now it is ready three days late. The laugh
lands at the end, told with a straight face. Running twice writes
identical bytes.
"""
from pathlib import Path

LINE = "I did the work on time. Then I improved it. Then I improved the improvement. It is ready now, three days late."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
