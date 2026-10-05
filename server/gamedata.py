"""Read the committed game wiki; no extracted client files or YAML dependency.

Use the generator's front-matter parser so editing an entity has the same
meaning to both readers. Unsupported or missing runtime data fails at startup.
"""
import sys

import paths

if str(paths.REPO) not in sys.path:
    sys.path.insert(0, str(paths.REPO))
from wiki.gamewiki.common import parse_front_matter

WIKI = paths.REPO / "docs" / "wiki"


def entity(kind, entity_id):
    matches = list((WIKI / kind).glob(f"{entity_id}-*.md"))
    if len(matches) != 1:
        raise ValueError(f"expected one wiki/{kind} page for id {entity_id}")
    data, _ = parse_front_matter(matches[0].read_text(encoding="utf-8"))
    if data.get("id") != entity_id:
        raise ValueError(f"wiki id mismatch: {matches[0]}")
    return data


def integer(value, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"expected integer in {low}..{high}, got {value!r}")
    return value
