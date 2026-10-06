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


_PAGES = {}


def pages(kind):
    """Every entity page of one wiki section, id -> front matter (cached)."""
    if kind not in _PAGES:
        found = {}
        for path in sorted((WIKI / kind).glob("*.md")):
            if path.name == "index.md":
                continue
            data, _ = parse_front_matter(path.read_text(encoding="utf-8"))
            if "id" not in data:
                continue  # a hand-written category page, not an entity
            if type(data["id"]) is not int or data["id"] in found:
                raise ValueError(f"invalid or duplicate wiki id: {path}")
            found[data["id"]] = data
        _PAGES[kind] = found
    return _PAGES[kind]


def number(value):
    """A finite world coordinate."""
    if type(value) not in (int, float) or value != value or abs(value) > 1e6:
        raise ValueError(f"expected a finite coordinate, got {value!r}")
    return float(value)


def integer(value, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"expected integer in {low}..{high}, got {value!r}")
    return value
