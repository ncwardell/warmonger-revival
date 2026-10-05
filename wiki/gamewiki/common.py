"""Shared framework of the game-wiki generator (docs/wiki/).

How it works
============

The game wiki has one page per game entity (item, NPC, monster, quest, skill,
buff, field, zone, dungeon, shop, teleport ...). Each page is the source of
truth the server is built from: its YAML front matter holds the structured
data, its body holds what people know about it. Pages start out
pre-populated from the client's own data tables and are then completed by hand.

  docs/wiki/<type>/<id>-<slug>.md        one page per entity
  docs/wiki/<type>/index.md              section index (generated)
  docs/wiki/index.md                     overview + coverage (generated)
  docs/wiki/assets/<type>/<id>.png       images extracted from the client

A page looks like this::

    ---
    title: "Magical Wrath Blade"          <- generated (bookkeeping keys first)
    type: "item"
    id: 10017
    status: "stub"                        <- computed: stub | partial | complete
    missing: ["obtained_from"]            <- computed from the type's REQUIRED fields
    sources: ["client: Item_Base.cdb row 10017"]   <- union of generated + hand-added
    manual: ["price"]                     <- keys the generator must never touch
    kind: 31                              <- generated type-specific keys
    ...
    drop_note: "..."                      <- hand-added keys are kept as written
    ---
    <!-- generated:start -->
    <!-- generated-keys: kind=1a2b3c price=... -->
    infobox, client fields, cross-links ...
    <!-- generated:end -->

    ## Notes / ## Behaviour / ## Sources / ## Open questions   <- hand-written

    <!-- credit:start -->
    Game content (c) GAMESinFLAMES / Joyimpact; reproduced for preservation ...
    <!-- credit:end -->

Regeneration rules (write_page):

* Only the generated block, the credit block and the generated front-matter
  keys are rewritten. Everything outside the markers and every key the
  generator does not produce is kept byte for byte.
* A generated key whose value was changed by hand is never overwritten. The
  generated block records a short hash of every key it wrote
  (``generated-keys``); if the value on disk no longer matches that hash, a
  person edited it, so the key is added to ``manual:`` and left alone from then
  on. To hand over a key explicitly, list it in ``manual:``. To give a key back
  to the generator, remove it from ``manual:`` (and delete the key).
* ``sources`` (and any key a module lists in UNION_KEYS) is a union: generated
  items first, then items people added.
* ``missing`` = the type's REQUIRED keys that are absent or empty after the
  merge. ``status`` = complete if nothing is missing; otherwise partial if the
  page has any hand-entered data (a hand key, a manual key or text in the hand
  sections), else stub. List ``status`` in ``manual:`` to set it yourself.
* Front matter is written as YAML whose values are JSON (valid YAML 1.2), one
  key per line; lists of objects are written as block lists of JSON objects.
  The parser here reads that back, plus ordinary simple YAML that people type
  (plain scalars, ``[a, b]`` lists, ``- item`` lists, one-level maps). Anything
  else is kept verbatim as Raw text.

Writing an entity module (see items.py, the reference module)::

    TYPE = "items"            # folder under docs/wiki/ and first arg of ctx.link
    KIND = "item"             # front-matter 'type' value
    LABEL = "Item"            # fallback title "Item 123" when there is no name
    REQUIRED = ["stats", "price", "obtained_from"]
    UNION_KEYS = ["obtained_from"]       # optional
    def name(ctx, id): ...    # optional; display name used by ctx.link everywhere
    def build(ctx): yield Page(...)      # one Page per entity

A Page carries ``type``, ``id``, ``title``, ``fields`` (generated type-specific
front matter, an ordered dict of JSON-able values), ``sources`` (list of
citation strings) and ``body``: either a string or a callable ``body(ctx,
page)`` called after every module has built its pages, so it may read
``ctx.pages(other_type)`` (merged front matter of the other type, fresh from
this run or parsed from disk) for reverse links. ``page.fm`` is the merged
front matter after write; bodies may use it to show hand-entered values.

The context (Ctx) offers:

  ctx.strings[key]            English string table (StringAll_Eng.cdb)
  ctx.s(key)                  string or None (ignores '0' / missing keys)
  ctx.table(name)             decoded client table (data/tables/<name>.tsv) -> Table
  ctx.name(type, id)          display name (module ``name()`` or NAMES below)
  ctx.title(type, id)         name or "<Label> <id>"
  ctx.path(type, id)          "wiki/<type>/<id>-<slug>" (no extension)
  ctx.link(type, id, text=None)   "[[wiki/<type>/<id>-<slug>|Name]]"
  ctx.image(type, id)         "../assets/<type>/<id>.png" relative to a page, or None
  ctx.unit_type(unit_id)      "npcs" | "monsters" | "objects" | "classes" (UnitDB split)
  ctx.pages(type)             {id: front matter dict} of that type
  ctx.mentions(name)          gameplay pages whose text mentions a name
"""
import hashlib
import json
import os
import pathlib
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Union

REPO = pathlib.Path(__file__).resolve().parents[2]
DOCS = REPO / "docs"
OUT = DOCS / "wiki"
ASSETS = OUT / "assets"
DATA = pathlib.Path(os.environ.get("WARMONGER_DATA", REPO / "data"))
TABLES = DATA / "tables"
CLIENT = pathlib.Path(os.environ.get(
    "WARMONGER_CLIENT", pathlib.Path.home() / ".local/share/warmonger-re/client"))
CLIENT_DATA = CLIENT / "Data" if (CLIENT / "Data").is_dir() else CLIENT
STRINGS = CLIENT_DATA / "config" / "StringAll_Eng.cdb"

GEN_START, GEN_END = "<!-- generated:start -->", "<!-- generated:end -->"
CREDIT_START, CREDIT_END = "<!-- credit:start -->", "<!-- credit:end -->"
CREDIT = ("Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation "
          "and reference.")
HAND_SECTIONS = ["Notes", "Behaviour", "Sources", "Open questions"]
BOOKKEEPING = ["title", "type", "id", "status", "missing", "sources", "manual"]


# --------------------------------------------------------------------- strings

def load_strings(path=STRINGS):
    """StringAll_*.cdb: 'count\\0 N\\0', then records 'key\\0' + UTF-16LE value
    ending in '\\0\\0' + an ASCII flag ending in '\\0' (docs/spec/jpk.md)."""
    try:
        d = pathlib.Path(path).read_bytes()
    except OSError:
        print("warning: no string table at %s (set WARMONGER_CLIENT)" % path, file=sys.stderr)
        return {}
    p = d.index(b"\0")
    count = int(d[:p])
    p = d.index(b"\0", p + 1) + 1
    out = {}
    for _ in range(count):
        if p >= len(d):
            break
        q = d.index(b"\0", p)
        key = d[p:q].decode("latin-1")
        p = q + 1
        q = p
        while q < len(d) - 1 and (d[q] or d[q + 1]):
            q += 2
        out.setdefault(key, d[p:q].decode("utf-16-le", "replace"))
        p = d.index(b"\0", q + 2) + 1
    return out


# ---------------------------------------------------------------------- tables

def _short(col):
    """'buy_price@20' -> 'buy_price'; 'rarity?@35' -> 'rarity'; 'c40@8e(grade?)' -> 'c40'."""
    s = col.split("@", 1)[0].split("(", 1)[0]
    return s.rstrip("?").strip()


class Row(dict):
    """A table row: raw column header -> string. Also answers to the short
    column name (``row['buy_price']`` for 'buy_price@20')."""

    def __init__(self, data, aliases):
        super().__init__(data)
        self._aliases = aliases

    def __missing__(self, key):
        real = self._aliases.get(key)
        if real is None:
            raise KeyError(key)
        return dict.__getitem__(self, real)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def int(self, key, default=0):
        v = self.get(key)
        try:
            return int(v)
        except (TypeError, ValueError):
            try:
                return int(float(v))
            except (TypeError, ValueError):
                return default

    def float(self, key, default=0.0):
        try:
            return float(self.get(key))
        except (TypeError, ValueError):
            return default

    def str(self, key):
        """Non-empty, non-'0' string or None."""
        v = self.get(key)
        return v if v not in (None, "", "0") else None


class Table:
    """A decoded client table. ``rows`` in file order; ``by(col)`` index."""

    def __init__(self, name, header, rows, comments):
        self.name, self.header, self.comments = name, header, comments
        aliases = {}
        for h in header:
            aliases.setdefault(_short(h), h)
            aliases.setdefault(h.split("@", 1)[0], h)
        self.rows = [Row(dict(zip(header, r)), aliases) for r in rows]
        self._idx = {}

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def by(self, col=None):
        """{int(row[col]): row}; col defaults to the first column. Later
        duplicates do not replace earlier rows."""
        col = col or self.header[0]
        if col not in self._idx:
            idx = {}
            for r in self.rows:
                k = r.int(col, None)
                if k is not None:
                    idx.setdefault(k, r)
            self._idx[col] = idx
        return self._idx[col]

    def get(self, key, col=None):
        return self.by(col).get(int(key))


def repeat(row, *patterns, start=1, skip_zero=True):
    """[(v1, v2, ...)] for n = start.. while row has every pattern % n.
    Values are ints where they parse. Groups whose first value is 0/empty are
    skipped when skip_zero."""
    out, n = [], start
    while all((p % n) in row._aliases or (p % n) in row for p in patterns):
        vals = []
        for p in patterns:
            v = row.get(p % n)
            try:
                v = int(v)
            except (TypeError, ValueError):
                try:
                    v = float(v)
                except (TypeError, ValueError):
                    pass
            vals.append(v)
        if not (skip_zero and vals[0] in (0, "", "0", None)):
            out.append(tuple(vals))
        n += 1
    return out


def load_tsv(name, tables=TABLES):
    """data/tables/<name>.tsv. Leading '#' lines are comments. The header is
    the first non-comment line, unless that line is data (the old 'kept'
    tables put the header in the last comment line, e.g. SceneList)."""
    path = pathlib.Path(tables) / (name + ".tsv")
    comments, lines = [], []
    for line in path.read_text(encoding="utf-8").split("\n"):
        if not line.strip():
            continue
        if line.startswith("#") and not lines:
            comments.append(line[1:].strip())
        else:
            lines.append(line.split("\t"))
    if not lines:
        return Table(name, [], [], comments)
    first = lines[0]
    if re.fullmatch(r"-?\d+", first[0].strip()):
        header = None
        for c in reversed(comments):
            cols = c.split("\t")
            if len(cols) == len(first):
                header = [x.strip() for x in cols]
                break
        if header is None:
            header = ["c%d" % i for i in range(len(first))]
            header[0] = "id"
        rows = lines
    else:
        header, rows = first, lines[1:]
    width = len(header)
    rows = [r + [""] * (width - len(r)) if len(r) < width else r[:width] for r in rows]
    return Table(name, header, rows, comments)


# ------------------------------------------------------------------- slugging

def slugify(text):
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text[:60].strip("-")


# ---------------------------------------------------------------- front matter

class Raw(str):
    """A front-matter value the parser does not understand: kept verbatim
    (the text after 'key:' including continuation lines)."""


def _scalar(text):
    t = text.strip()
    if t == "":
        return None
    try:
        return json.loads(t)
    except ValueError:
        pass
    if t in ("~", "null", "Null", "NULL"):
        return None
    if t in ("true", "True", "yes"):
        return True
    if t in ("false", "False", "no"):
        return False
    if len(t) >= 2 and t[0] == t[-1] == "'":
        return t[1:-1].replace("''", "'")
    if t.startswith("[") and t.endswith("]"):
        inner = t[1:-1].strip()
        return [] if not inner else [_scalar(x) for x in inner.split(",")]
    if " #" in t:
        t = t.split(" #", 1)[0].rstrip()
    try:
        return int(t)
    except ValueError:
        try:
            return float(t)
        except ValueError:
            return t


def parse_front_matter(text):
    """-> (dict key -> value, body). Values are Python data, or Raw when the
    YAML is beyond this small parser."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not m:
        return {}, text
    block, body = m.group(1), text[m.end():]
    fm, key, inline, cont = {}, None, "", []

    def flush():
        if key is None:
            return
        if not cont:
            fm[key] = _scalar(inline)
            return
        if inline.strip():
            fm[key] = Raw(inline + "\n" + "\n".join(cont))
            return
        items = [c.strip() for c in cont if c.strip() and not c.strip().startswith("#")]
        if items and all(i.startswith("- ") or i == "-" for i in items):
            fm[key] = [_scalar(i[1:]) for i in items]
        elif items and all(re.match(r"[\w-]+:\s", i + " ") for i in items) and \
                all(c.startswith("  ") and not c.startswith("   ") for c in cont if c.strip()):
            fm[key] = {i.split(":", 1)[0].strip(): _scalar(i.split(":", 1)[1]) for i in items}
        else:
            fm[key] = Raw("\n" + "\n".join(cont))

    for line in block.split("\n"):
        line = line.rstrip("\r")
        mk = re.match(r"([A-Za-z_][\w-]*)\s*:(?:\s(.*)|)$", line)
        if mk and not line[:1].isspace():
            flush()
            key, inline, cont = mk.group(1), mk.group(2) or "", []
        elif key is not None:
            cont.append(line)
    flush()
    return fm, body


def dump_value(v):
    if isinstance(v, Raw):
        return " " + v if not v.startswith("\n") else v
    if isinstance(v, list) and v and any(isinstance(x, (dict, list)) for x in v):
        return "\n" + "\n".join("  - " + json.dumps(x, ensure_ascii=False) for x in v)
    return " " + json.dumps(v, ensure_ascii=False)


def dump_front_matter(fm):
    return "---\n" + "".join("%s:%s\n" % (k, dump_value(v)) for k, v in fm.items()) + "---\n"


def vhash(v):
    if isinstance(v, Raw):
        s = "raw:" + v
    else:
        s = json.dumps(v, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(s.encode()).hexdigest()[:6]


def empty(v):
    return v is None or v == "" or v == [] or v == {}


# ------------------------------------------------------------------------ page

@dataclass
class Page:
    type: str                      # folder, e.g. "items"
    id: int
    title: str
    fields: dict = field(default_factory=dict)        # generated type-specific keys
    sources: list = field(default_factory=list)       # citation strings
    body: Union[str, Callable, None] = None           # generated block content
    kind: Optional[str] = None     # front-matter 'type'; default module KIND
    required: Optional[list] = None   # default module REQUIRED
    # filled in by the writer:
    fm: dict = field(default_factory=dict)            # merged front matter
    path: Optional[pathlib.Path] = None
    existing_text: Optional[str] = None


def _strip_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def hand_text(body):
    """Text people wrote outside the generated/credit blocks, minus headings
    and comments."""
    b = re.sub(re.escape(GEN_START) + ".*?" + re.escape(GEN_END), "", body, flags=re.S)
    b = re.sub(re.escape(CREDIT_START) + ".*?" + re.escape(CREDIT_END), "", b, flags=re.S)
    b = _strip_comments(b)
    b = re.sub(r"(?m)^#{1,6} .*$", "", b)
    return b.strip()


def hand_template():
    return "\n".join("## %s\n\n<!-- hand-written: add what you know, with a source -->\n" % s
                     for s in HAND_SECTIONS)


def merge(page, generated, existing, gen_hashes, union_keys, required):
    """Merge generated front matter into what is on disk. Returns (fm,
    written_hashes, notes)."""
    notes = []
    manual = existing.get("manual") or []
    manual = list(manual) if isinstance(manual, list) else [manual]
    final = {}
    written = {}
    for k, v in generated.items():
        if k in manual:
            if k in existing:
                final[k] = existing[k]
            continue
        if k in union_keys and k in existing and isinstance(existing[k], list) and isinstance(v, list):
            seen = [json.dumps(x, sort_keys=True) for x in v]
            extra = [x for x in existing[k] if json.dumps(x, sort_keys=True) not in seen]
            final[k] = list(v) + extra
            written[k] = vhash(v)
            continue
        if k in existing and k not in ("missing", "status"):
            ex = existing[k]
            if vhash(ex) != vhash(v) and k not in ("title", "type", "id"):
                if gen_hashes.get(k) != vhash(ex):
                    final[k] = ex
                    manual.append(k)
                    notes.append("%s: '%s' was edited by hand; kept and added to manual" % (page.path.name, k))
                    continue
        final[k] = v
        written[k] = vhash(v)
    # keys the generator wrote last time but no longer produces: drop them
    # unless a person changed them since
    dropped = [k for k in existing if k not in generated and k in gen_hashes
               and k not in manual and gen_hashes[k] == vhash(existing[k])]
    hand_keys = [k for k in existing if k not in final and k not in BOOKKEEPING and k not in dropped]
    for k in hand_keys:
        final[k] = existing[k]
    if manual:
        final["manual"] = sorted(set(manual), key=manual.index)
    # missing / status
    missing = [f for f in required if empty(final.get(f))]
    final["missing"] = missing
    has_hand = bool(manual) or any(not empty(existing.get(k)) for k in hand_keys)
    if "status" in manual and "status" in existing:
        final["status"] = existing["status"]
    else:
        final["status"] = "complete" if not missing else ("partial" if has_hand else "stub")
    # canonical order: bookkeeping keys first, then generated, then hand keys
    order = ["title", "type", "id", "status", "missing", "sources", "manual"]
    out = {k: final[k] for k in order if k in final}
    for k in generated:
        if k in final and k not in out:
            out[k] = final[k]
    for k in hand_keys:
        out[k] = final[k]
    return out, written, notes, has_hand


# ------------------------------------------------------------------------- ctx

# Default display-name rules, used by ctx.name() for types whose module does
# not define name(). Every entity module MUST resolve names through ctx.name /
# ctx.link so all modules produce the same slugs.
#   type: (table, key column or None for the first, [name-key columns], [key patterns])
NAMES = {
    "items": ("Item_Base", None, ["name_key"], ["ItemName_%d"]),
    "npcs": ("UnitDB", None, ["name_key"], ["UnitName_%d"]),
    "monsters": ("UnitDB", None, ["name_key"], ["UnitName_%d"]),
    "objects": ("UnitDB", None, ["name_key"], ["UnitName_%d"]),
    "classes": ("UnitDB", None, ["name_key"], ["UnitName_%d"]),
    "skills": ("Skill_Base", None, ["name_key"], ["Skill_%d"]),
    "buffs": ("Skill_Buff", None, ["name_key"], ["SkillBuff_%d"]),
    "quests": ("Quest", None, ["title_key"], []),
    "fields": ("SceneList", None, ["nameKey"], ["FieldName_%d"]),
    "dungeons": ("SceneList", None, ["nameKey"], ["FieldName_%d"]),
    "zones": (None, None, [], []),
    "shops": (None, None, [], []),
    "teleports": (None, None, [], []),
    "sets": (None, None, [], []),
    "heroes": ("HeroData", None, ["name_key"], ["HeroName_%d"]),
    "masteries": ("Mastery", None, ["name_key"], []),
    "achievements": ("Achievement_Base", None, ["name_key"], ["AchievementName_%d"]),
}
LABELS = {
    "items": "Item", "npcs": "NPC", "monsters": "Monster", "objects": "Object",
    "classes": "Class", "skills": "Skill", "buffs": "Buff", "quests": "Quest",
    "fields": "Field", "zones": "Zone", "dungeons": "Dungeon", "shops": "Shop",
    "teleports": "Teleport", "sets": "Set", "heroes": "Hero", "masteries": "Mastery",
    "achievements": "Achievement",
}

# UnitDB category@8a -> wiki type (docs/spec/monsters.md: 1 monster, 5 player,
# 4/50 NPC kinds). Units with a shop (u16@a2) or an NPC portrait (str@110) are
# NPCs whatever their category. Category 6 (class mask 1) holds every dungeon
# boss (King Deathhead 672, Akasha 849 ...; docs/gameplay/dungeon-drops.md).
UNIT_TYPES = {1: "monsters", 3: "monsters", 6: "monsters", 8: "monsters", 9: "monsters",
              4: "npcs", 50: "npcs", 5: "classes"}


class Ctx:
    def __init__(self, dry_run=False, verbose=False):
        self.dry_run, self.verbose = dry_run, verbose
        self.strings = load_strings()
        self._tables = {}
        self._modules = {}
        self._names = {}
        self._pages = {}        # type -> {id: fm} built this run
        self._disk = {}         # type -> {id: fm} from disk
        self._mentions = None
        self.notes = []

    # -- data
    def s(self, key):
        if key in (None, "", "0", 0):
            return None
        v = self.strings.get(key)
        return v.strip() if v and v.strip() else None

    def table(self, name):
        if name not in self._tables:
            self._tables[name] = load_tsv(name)
        return self._tables[name]

    def module(self, type_):
        if type_ not in self._modules:
            try:
                import importlib
                self._modules[type_] = importlib.import_module("wiki.gamewiki." + type_)
            except ImportError:
                self._modules[type_] = None
        return self._modules[type_]

    # -- names / links
    def name(self, type_, id_):
        id_ = int(id_)
        key = (type_, id_)
        if key in self._names:
            return self._names[key]
        mod = self.module(type_)
        if mod is not None and hasattr(mod, "name"):
            n = mod.name(self, id_)
        else:
            n = self._default_name(type_, id_)
        n = clean_name(n) if isinstance(n, str) else None
        self._names[key] = n
        return n

    def _default_name(self, type_, id_):
        spec = NAMES.get(type_)
        if not spec:
            return None
        tname, col, keycols, patterns = spec
        if tname:
            try:
                row = self.table(tname).get(id_, col)
            except (OSError, KeyError):
                row = None
            if row is not None:
                for kc in keycols:
                    n = self.s(row.get(kc))
                    if n:
                        return n
        for p in patterns:
            n = self.s(p % id_)
            if n:
                return n
        return None

    def label(self, type_):
        mod = self.module(type_)
        return getattr(mod, "LABEL", None) or LABELS.get(type_, type_.rstrip("s").title())

    def title(self, type_, id_):
        return self.name(type_, id_) or "%s %d" % (self.label(type_), int(id_))

    def path(self, type_, id_):
        slug = slugify(self.name(type_, id_) or "")
        return "wiki/%s/%d%s" % (type_, int(id_), "-" + slug if slug else "")

    def link(self, type_, id_, text=None):
        text = text or self.title(type_, id_)
        return "[[%s|%s]]" % (self.path(type_, id_), link_text(text))

    def image(self, type_, id_):
        if (ASSETS / type_ / ("%d.png" % int(id_))).exists():
            return "../assets/%s/%d.png" % (type_, int(id_))
        return None

    def unit_type(self, unit_id):
        row = self.table("UnitDB").get(unit_id)
        if row is None:
            return "monsters"
        if row.int("u16@a2") or row.str("str@110"):
            return "npcs"
        return UNIT_TYPES.get(row.int("category@8a"), "objects")

    def unit_link(self, unit_id, text=None):
        return self.link(self.unit_type(unit_id), unit_id, text)

    # -- other pages
    def pages(self, type_):
        """{id: front matter} for a type: pages built in this run, else the
        ones on disk."""
        if type_ in self._pages:
            return self._pages[type_]
        if type_ not in self._disk:
            out = {}
            d = OUT / type_
            if d.is_dir():
                for f in d.glob("*.md"):
                    if f.name == "index.md":
                        continue
                    fm, _ = parse_front_matter(f.read_text(encoding="utf-8"))
                    try:
                        out[int(fm.get("id"))] = fm
                    except (TypeError, ValueError):
                        pass
            self._disk[type_] = out
        return self._disk[type_]

    def mentions(self, name, min_len=8):
        """[(wikilink path, title)] of hand-written docs/gameplay pages whose
        text mentions ``name`` (case-insensitive, whole words). Short or
        one-word names are skipped (too many false hits)."""
        if not name or (len(name) < min_len and " " not in name.strip()):
            return []
        if self._mentions is None:
            self._mentions = []
            for f in sorted((DOCS / "gameplay").glob("*.md")):
                text = f.read_text(encoding="utf-8")
                fm, body = parse_front_matter(text)
                self._mentions.append(("gameplay/" + f.stem, fm.get("title") or f.stem, _words(body)))
        needle = _words(name)
        return [(p, t) for p, t, body in self._mentions if needle in body]


def _words(text):
    """' word word ... ' (lower case, runs of non-word characters -> one
    space) so a whole-word search is a plain substring test."""
    return " " + " ".join(re.findall(r"\w+", text.lower())) + " "


def link_text(text):
    """Display text safe inside [[...|...]] (no '|', '[' or ']')."""
    return text.replace("|", "/").replace("[", "(").replace("]", ")")


# ---------------------------------------------------------------------- writer

def render_body(page, block, old_body):
    """Body with the generated block (and credit) replaced, hand text kept."""
    gen = "%s\n%s\n%s" % (GEN_START, block.strip("\n"), GEN_END)
    credit = "%s\n---\n*%s*\n%s" % (CREDIT_START, CREDIT, CREDIT_END)
    if old_body is None:
        return "%s\n\n%s\n%s\n" % (gen, hand_template(), credit)
    body = old_body
    pat = re.compile(re.escape(GEN_START) + ".*?" + re.escape(GEN_END), re.S)
    if pat.search(body):
        body = pat.sub(lambda _m: gen, body, count=1)
    else:
        body = gen + "\n\n" + body.lstrip("\n")
    cpat = re.compile(re.escape(CREDIT_START) + ".*?" + re.escape(CREDIT_END), re.S)
    if cpat.search(body):
        body = cpat.sub(lambda _m: credit, body, count=1)
    else:
        body = body.rstrip("\n") + "\n\n" + credit + "\n"
    return body


TYPE_KEYS = {"boxes": "box", "gacha": "gacha"}


def type_key(folder):
    """Front-matter 'type' for a folder: 'items' -> 'item', 'boxes' -> 'box'."""
    return TYPE_KEYS.get(folder, folder[:-1] if folder.endswith("s") else folder)


def find_existing(type_, id_):
    d = OUT / type_
    if not d.is_dir():
        return None
    hits = sorted(d.glob("%d-*.md" % id_)) + sorted(d.glob("%d.md" % id_))
    return hits[0] if hits else None


GEN_KEYS_RE = re.compile(r"<!-- generated-keys: (.*?) -->")


def prepare(ctx, page, mod):
    """Merge page.fields with the page on disk; sets page.fm / page.path."""
    rel = ctx.path(page.type, page.id)
    path = DOCS / (rel + ".md")
    old = find_existing(page.type, page.id)
    text = old.read_text(encoding="utf-8") if old else None
    existing, body = parse_front_matter(text) if text else ({}, None)
    gen_hashes = {}
    if body:
        m = GEN_KEYS_RE.search(body)
        if m:
            gen_hashes = dict(x.split("=", 1) for x in m.group(1).split() if "=" in x)
    page.path, page.existing_text = path, text
    page._old_path, page._old_body = old, body
    # 'type' is always the singular of the folder (one key for the server to
    # dispatch on); a module's finer KIND / page.kind goes in 'kind'.
    generated = {"title": page.title, "type": type_key(page.type),
                 "id": page.id, "sources": list(page.sources)}
    generated.update(page.fields)
    sub = page.kind or getattr(mod, "KIND", None)
    if sub and sub != generated["type"] and "kind" not in generated:
        generated["kind"] = sub
    union = set(getattr(mod, "UNION_KEYS", [])) | {"sources"}
    required = page.required if page.required is not None else list(getattr(mod, "REQUIRED", []))
    fm, written, notes, has_hand = merge(page, generated, existing, gen_hashes, union, required)
    if body is not None and fm["status"] == "stub" and hand_text(body):
        fm["status"] = "partial"
    page.fm, page._written = fm, written
    ctx.notes.extend(notes)


WIKILINK_RE = re.compile(r"\[\[wiki/([a-z_]+)/(\d+)(?:-[^\]|\\]*)?(\\?\|)?([^\]]*)\]\]")


def unlink_missing(ctx, text):
    """[[wiki/<type>/<id>-...|text]] -> plain text when no such page exists
    (types without a module yet, ids with no row), so every wikilink in a
    generated block resolves. Runs after every type has been prepared."""
    def sub(m):
        type_, id_ = m.group(1), int(m.group(2))
        if id_ in ctx.pages(type_):
            return m.group(0)
        return m.group(4) if m.group(3) else "%s %d" % (ctx.label(type_), id_)
    return WIKILINK_RE.sub(sub, text)


def write(ctx, page, stats):
    block = page.body(ctx, page) if callable(page.body) else (page.body or "")
    block = unlink_missing(ctx, block)
    keys = " ".join("%s=%s" % kv for kv in page._written.items())
    block = "<!-- generated-keys: %s -->\n%s" % (keys, block.strip("\n"))
    text = dump_front_matter(page.fm) + render_body(page, block, page._old_body)
    if page._old_path is not None and page._old_path != page.path:
        stats["renamed"] += 1
        if not ctx.dry_run:
            page._old_path.unlink()
    if text == page.existing_text and page._old_path == page.path:
        stats["unchanged"] += 1
        return
    stats["new" if page.existing_text is None else "changed"] += 1
    if not ctx.dry_run:
        page.path.parent.mkdir(parents=True, exist_ok=True)
        page.path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------- markdown helpers

def cell(v):
    if v is None:
        return ""
    return str(v).replace("|", "\\|").replace("\n", " ")


def table_md(headers, rows):
    if not rows:
        return ""
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def clean_name(text):
    """A display name without client markup ('<color 255 253 47>(Lv 6)</color>
    Ghost Fortress' -> '(Lv 6) Ghost Fortress'); None if nothing is left."""
    text = re.sub(r"<[^<>]*>", " ", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def clean_text(text):
    """Client UI markup -> Markdown-safe text: '<n>' -> line break, colour
    tags dropped, value placeholders ('<EF_R_DAM 2>', '%d') shown as code,
    any other '<...>' (literal text like '<Daily Quest>') escaped."""
    text = (text or "").replace("\r", "").replace("\\n", "\n").replace("<n>", "\n")
    text = re.sub(r"</?color[^<>]*>|</?pass>", "", text)
    text = re.sub(r"<((?:EF_|dict|dicf|value_|icon )[^<>]*)>", r"`{\1}`", text)
    return text.replace("<", "&lt;").replace(">", "&gt;")


def quote(text):
    """A client text as a Markdown quote (client line breaks kept)."""
    text = clean_text(text).strip()
    return "\n".join("> " + l if l else ">" for l in text.split("\n")) + "\n"


def fmt_num(v):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return "{:,}".format(v) if isinstance(v, int) else str(v)
