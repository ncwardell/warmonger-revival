"""Images for the game wiki, extracted from the client's archives.

  python3 -m wiki.gamewiki assets [types...] [--force]

writes docs/wiki/assets/<type>/<id>.png (small PNGs) for every entity that
has art in the client, and docs/wiki/assets/manifest.json ({type: {id:
"archive path [cell n]"}}) so pages can cite where each image came from.
Existing PNGs are kept unless --force. Needs Pillow (it decodes DXT1/3/5
.dds); everything else in the generator is stdlib-only. Without Pillow on
the default python3, run it as

  nix shell --impure --expr 'with import <nixpkgs> {}; python3.withPackages (p: [ p.pillow ])' \\
      -c python3 -m wiki.gamewiki assets

The archives are read in place with tools/jpk.py (no extraction step). MPQ
names are case-insensitive, so table spellings like 'Items_15.Png' or
'ui/NPCprofile/...' resolve.

How the client stores and finds its art (all *client*, Client.exe)
==================================================================

Icon atlases -- ui.jpk ui/icons/<file>, 512 x 512 textures (.png or DXT
.dds) cut into an 8 x 8 grid of 64 x 64 cells. A table row names the atlas
file and a cell index 0..63; the icon slot code (FUN_004e9080, switch on the
slot type, every case formats "ui/icons/%s") takes

    x = (index & 7) * 64        y = (index >> 3) * 64        size 64 x 64

Which row field feeds each slot type (record offsets = the decoded TSV
column suffixes):

  items     Item_Base   icon_file (+0x9a)  icon_idx@9e     slot type 2
  skills    Skill_Base  icon_file@c9       icon_idx@cd     slot types 1, 6
  buffs     Skill_Buff  icon_file@54       icon_idx@58     slot type 3
  masteries Mastery     icon_file@20       icon_idx@24     slot type 4
            (+ FortMastery, GuildMastery; saved under the masteries page ids)
  also      CommonIcon (GUI_* keys -> Policy/CommonIcon atlases), Policy, PolicyActive, AddonData, LabData, Item_Jewel
            use the same (file, index) pair; not extracted here (no wiki type
            yet). Add a SOURCES entry when a type needs them.

Nine Skill_Base atlases are not in the shipped ui.jpk ('skill\\10703.png',
'Skill_Warrior_MoraleBoostStamina.png', 'Spell_Nature_WispHeal.png' ...):
developer placeholders on unused skills. Those skills get no image.
Item_Base 'Artifacts_01.png' / 'Artifacts_02.png' (19 Crush-era artifact
items) are missing from ui.jpk too.

Portraits -- whole images in ui.jpk ui/NPCProfile/ (64 x 64 .png or larger
.dds); scaled to at most 128 px:

  npcs      UnitDB str@110 (the quest-talk portrait path; only talking NPCs
            have one; the folder comes from ctx.unit_type, so a unit that is
            not classed as an NPC lands under its own type); else the
            QuestTalk portrait@7c of dialogue rows whose speaker_unit_key is
            the unit's name or title key (Shaia, Floyd, Guard ...)
  nodes     QuestTalk portrait@7c for Trigger quest gadgets (speaker_unit_key
            = Trigger name_key: Scout, Scout Leader, Ghost soldier ...)
  heroes   HeroData portrait@54
  classes   Create_Char portraits_F (first face of the class; key = the
            class's UnitDB unit_id@0c)

Monsters have no 2-D portrait in the client (only 3-D models in model.jpk).
The exception is a boss that is also a hero transform: monsters/<unit>.png
is the HeroData portrait of the hero with the same name (King Deathhead,
Tempest Fisher ...). The other pages have no image until someone renders one.

Minimaps -- map.jpk map/minimap/minimap_z<zone>_00.dds, loaded by the
minimap panel as "map/minimap/minimap_z%d_00.dds" with the zone number
(= ZoneDB row id; e.g. z2 = tutorial_map_01). Written as zones/<zone>.png,
scaled to at most 384 px. 143 zones have one.

Dungeon art -- DungeonAdmission image@24 ('UI/FieldImages/<n>.png', the
entry-panel banner) -> dungeons/<field id>.png, at most 384 px.

Quest tip art -- Quest help_image ('ui/HelpImage/Help_NN.png', shown in the
quest's tip window) -> quests/<quest id>.png, at most 384 px.
"""
import importlib.util
import io
import json
import sys

from . import common

ICON = 64
CELLS = 8          # cells per atlas row
PORTRAIT_MAX = 128
MAP_MAX = 384


def _load_jpk():
    spec = importlib.util.spec_from_file_location("jpk", common.REPO / "tools" / "jpk.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Client:
    """Reads files out of Data/*.jpk by path, caches decoded images."""

    def __init__(self):
        self.jpk = _load_jpk()
        self.archives = {}
        self.images = {}

    def archive(self, name):
        if name not in self.archives:
            path = common.CLIENT_DATA / (name + ".jpk")
            self.archives[name] = self.jpk.Archive(str(path)) if path.exists() else None
        return self.archives[name]

    def read(self, path):
        """Bytes of 'ui/icons/x.png' (archive = first path part), or None."""
        path = path.replace("/", "\\").lstrip("\\")
        arc = self.archive(path.split("\\", 1)[0].lower())
        if arc is None:
            return None
        block = arc.lookup(path)
        if block is None:
            return None
        try:
            return arc.read(block)
        except ValueError:
            return None

    def image(self, path):
        from PIL import Image
        key = path.lower().replace("\\", "/")
        if key not in self.images:
            data = self.read(path)
            im = None
            if data:
                try:
                    im = Image.open(io.BytesIO(data))
                    im.load()
                    im = im.convert("RGBA")
                except Exception as e:   # unsupported DDS flavour etc.
                    print("warning: cannot decode %s: %s" % (path, e), file=sys.stderr)
                    im = None
            self.images[key] = im
        return self.images[key]


# --------------------------------------------------------------- what to make
# Each source yields (id, archive path, cell index or None, max size).

def _icons(table, file_col, idx_col):
    def gen(ctx):
        for r in ctx.table(table):
            f = (r.get(file_col) or "").strip()
            if f in ("", "0"):
                continue
            yield r.int("id"), "ui/icons/" + f.replace("\\", "/"), r.int(idx_col), None
    return gen


def _unit_portraits(ctx, want):
    for r in ctx.table("UnitDB"):
        p = r.str("str@110")
        if p and p.lower().startswith("ui/") and ctx.unit_type(r.int("id")) == want:
            yield r.int("id"), p, None, PORTRAIT_MAX


def _heroes(ctx):
    for r in ctx.table("HeroData"):
        p = r.str("portrait")
        if p:
            yield r.int("id"), p, None, PORTRAIT_MAX


def _masteries(ctx):
    """Mastery / FortMastery / GuildMastery icons under the masteries page ids
    (class unit x 100 + id, 1000 + fort id, 2000 + legion id; masteries.py)."""
    from . import masteries
    for pid, f, idx in masteries.icons(ctx):
        if f != "0":
            yield pid, "ui/icons/" + f.replace("\\", "/"), idx, None


def _classes(ctx):
    for r in ctx.table("Create_Char"):
        faces = (r.get("portraits_F") or "").split(",")
        if faces and faces[0].strip():
            yield r.int("unit_id"), "ui/" + faces[0].strip().replace("\\", "/"), None, PORTRAIT_MAX


def _monster_portraits(ctx):
    """Bosses that are also hero transforms (HeroData row with the same name,
    e.g. King Deathhead 672 -> Hero_Deathhead): the hero portrait is the only
    2-D art of the monster in the client."""
    heroes = {}
    for h in ctx.table("HeroData"):
        n = ctx.s(h.get("name_key"))
        if n and h.str("portrait"):
            heroes.setdefault(n.lower(), h.str("portrait"))
    for r in ctx.table("UnitDB"):
        id_ = r.int("id")
        if ctx.unit_type(id_) != "monsters":
            continue
        p = heroes.get((ctx.name("monsters", id_) or "").lower())
        if p:
            yield id_, p, None, PORTRAIT_MAX


def _zones(ctx):
    for r in ctx.table("ZoneDB"):
        z = r.int(ctx.table("ZoneDB").header[0])
        yield z, "map/minimap/minimap_z%d_00.dds" % z, None, MAP_MAX


def _dungeons(ctx):
    for r in ctx.table("DungeonAdmission"):
        p = r.str("image")
        if p:
            yield r.int("field"), p, None, MAP_MAX


def _talk_portraits(ctx, want):
    """QuestTalk portrait@7c for units the dialogue names (speaker_unit_key =
    the unit's name key or UnitDB str@40 title key): the face the client shows
    in quest dialogue. Fills in NPCs without a UnitDB str@110 portrait (Shaia,
    Floyd ...) and the Trigger quest gadgets (nodes: Trigger name_key)."""
    talk = {}
    for r in ctx.table("QuestTalk"):
        p = r.str("portrait")
        if p and p.lower().startswith("ui/"):
            talk.setdefault(r.get("speaker_unit_key"), p)
    if want == "nodes":
        for r in ctx.table("Trigger"):
            p = talk.get(r.get("name_key"))
            if p:
                yield r.int("id"), p, None, PORTRAIT_MAX
        return
    for r in ctx.table("UnitDB"):
        if ctx.unit_type(r.int("id")) != want:
            continue
        for key in (r.get("name_key"), r.get("str@40")):
            if key and key in talk:
                yield r.int("id"), talk[key], None, PORTRAIT_MAX
                break


def _chain(*gens):
    def gen(ctx):
        for g in gens:
            yield from g(ctx)
    return gen


def _quest_help(ctx):
    """Quest help_image ('ui/HelpImage/Help_NN.png', the quest's tip-window
    picture) -> quests/<quest id>.png, at most 384 px."""
    for r in ctx.table("Quest"):
        p = r.str("help_image")
        if p and p.lower().startswith("ui/"):
            yield r.int("id"), p, None, MAP_MAX


SOURCES = {
    "items": _icons("Item_Base", "icon_file", "icon_idx"),
    "skills": _icons("Skill_Base", "icon_file", "icon_idx"),
    "buffs": _icons("Skill_Buff", "icon_file", "icon_idx"),
    "masteries": _masteries,
    "npcs": _chain(lambda ctx: _unit_portraits(ctx, "npcs"), lambda ctx: _talk_portraits(ctx, "npcs")),
    "nodes": lambda ctx: _talk_portraits(ctx, "nodes"),
    "heroes": _heroes,
    "monsters": _monster_portraits,
    "classes": _classes,
    "zones": _zones,
    "dungeons": _dungeons,
    "quests": _quest_help,
}


def crop(im, index):
    x, y = (index % CELLS) * ICON, (index // CELLS) * ICON
    if x + ICON > im.width or y + ICON > im.height:
        return None
    return im.crop((x, y, x + ICON, y + ICON))


def fit(im, limit):
    if limit and max(im.size) > limit:
        im = im.copy()
        im.thumbnail((limit, limit))
    return im


def save(im, dest):
    """Small PNG: 256-colour palette (alpha kept). Icons come out of DXT
    textures already reduced to few colours, so this is visually lossless and
    about half the size of RGBA (minimaps: a tenth)."""
    from PIL import Image
    try:
        im = im.quantize(256, method=Image.Quantize.FASTOCTREE)
    except (ValueError, AttributeError):
        pass
    im.save(dest, optimize=True)


def main(types, force=False):
    try:
        import PIL  # noqa: F401
    except ImportError:
        sys.exit("assets needs Pillow. Run:\n  nix shell --impure --expr 'with import <nixpkgs> {}; "
                 "python3.withPackages (p: [ p.pillow ])' -c python3 -m wiki.gamewiki assets")
    ctx = common.Ctx()
    client = Client()
    manifest_path = common.ASSETS / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        manifest = {}
    chosen = types or list(SOURCES)
    bad = [t for t in chosen if t not in SOURCES]
    if bad:
        sys.exit("no image source for: %s (have: %s)" % (", ".join(bad), ", ".join(SOURCES)))
    for t in chosen:
        out_dir = common.ASSETS / t
        out_dir.mkdir(parents=True, exist_ok=True)
        made = kept = 0
        missing = {}
        entries = {}
        for id_, path, index, limit in SOURCES[t](ctx):
            if id_ in entries:
                continue
            src = path + ("" if index is None else " cell %d" % index)
            dest = out_dir / ("%d.png" % id_)
            if dest.exists() and not force:
                entries[id_] = src
                kept += 1
                continue
            im = client.image(path)
            if im is not None and index is not None:
                im = crop(im, index)
            if im is None or im.getbbox() is None:     # absent, or an empty cell
                missing[path] = missing.get(path, 0) + 1
                continue
            save(fit(im, limit), dest)
            entries[id_] = src
            made += 1
        manifest[t] = {str(k): v for k, v in sorted(entries.items())}
        miss = sum(missing.values())
        print("%-10s %5d images (%d new, %d kept)  %d without art%s" % (
            t, len(entries), made, kept, miss,
            ("  e.g. " + ", ".join(sorted(missing)[:4])) if missing else ""))
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
