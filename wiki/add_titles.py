#!/usr/bin/env python3
"""Give every wiki page a `title:` front matter taken from its first `# ` heading.

Quartz titles pages from front matter, else from the file name. Pages that
already have front matter are left alone. Run from the repo root:
  python3 wiki/add_titles.py docs
"""
import pathlib
import sys

for path in sorted(pathlib.Path(sys.argv[1]).rglob("*.md")):
    text = path.read_text()
    if text.startswith("---\n"):
        continue
    heading = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), None)
    if heading:
        title = heading.replace('"', "'")
        path.write_text(f'---\ntitle: "{title}"\n---\n\n{text}')
        print(f"{path}: {title}")
