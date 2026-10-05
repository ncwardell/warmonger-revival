#!/usr/bin/env python3
"""Timestamp manual observations and summarize a local protocol log.

python tools/test_session.py mark "Alice: equipped bow; skill icons changed"
python tools/test_session.py report
Output stays in ignored out/; reports omit packet bodies and account tokens.
"""
import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    mark = sub.add_parser("mark")
    mark.add_argument("observation")
    report = sub.add_parser("report")
    report.add_argument("--log", type=Path, default=ROOT / "out" / "server.log")
    args = parser.parse_args()
    notes = ROOT / "out" / "test-observations.jsonl"
    if args.action == "mark":
        notes.parent.mkdir(exist_ok=True)
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        with notes.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"time": now, "observation": args.observation}) + "\n")
        print(now, args.observation)
        return
    counts = Counter()
    errors = []
    try:
        lines = args.log.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as error:
        parser.error(str(error))
    for line in lines:
        match = re.search(r"\[game\] <- op=(0x[0-9a-f]+)", line)
        if match:
            counts[match[1]] += 1
        if any(term in line for term in ("failed", "Traceback", "bad header", "short packet")):
            errors.append(line.split("body=", 1)[0])
    print("Client packet counts:")
    for opcode, count in sorted(counts.items()):
        print(f"  {opcode}: {count}")
    print("Server errors:", len(errors))
    for line in errors[-20:]:
        print(" ", line)
    if notes.exists():
        print("Manual observations:")
        for line in notes.read_text(encoding="utf-8").splitlines()[-30:]:
            entry = json.loads(line)
            print(" ", entry["time"], entry["observation"])


if __name__ == "__main__":
    main()
