"""Dungeons: one page per dungeon field (id = field id): every field with a
DungeonAdmission row, a slot in a Dungeon group or an Event_Dungeon schedule.
The map itself (gates, monsters, nodes, navmesh) is on the field page with
the same id; this page holds what makes it a dungeon.

Client sources (see maps.py):
  DungeonAdmission  entry tickets (cost1 / cost2 = normal / hard, *inferred*
                    from the guides' tables in docs/gameplay/maps-and-dungeons
                    §2), 'event' flag, up to 10 reward items shown on the entry
                    panel (not a drop table), banner image, c17, notice text
  Dungeon           3 groups x 15 slots of field ids (slot = tier step by
                    distance from the nation's forts, *guess*)
  Event_Dungeon     event schedule: target field, hour?, minutes open, c2..c4
  SceneList         max users (5 for every dungeon; guides: "max 5 players")
Hand sources: boss and gear tier from the border-area table in
docs/gameplay/maps-and-dungeons.md; FACTS below.

REQUIRED: entry_cost, boss, time_limit_s.
"""
import re

from . import common, maps
from .common import Page, fmt_num, table_md

TYPE = "dungeons"
KIND = "dungeon"
LABEL = "Dungeon"
DESCRIPTION = ("Every dungeon the client knows: the nine border-area dungeons and Dragon Island "
               "(`DungeonAdmission`, `Dungeon`), and the event dungeons (`Event_Dungeon`). Entry "
               "cost, the rewards the entry panel shows, the boss and the event schedule. The map "
               "itself is on the [[wiki/fields/index|field page]] with the same id.")
REQUIRED = ["entry_cost", "boss", "time_limit_s"]
UNION_KEYS = ["boss"]

# Numbers copied from docs/gameplay, each with its source (field -> {key: (value, source)}).
FACTS = {
    124: {"time_limit_s": (1200, "doc: gameplay/video-dungeon-run §5 (Crush Online 2016 video: "
                                 "the instance timer counts down from 20:00)")},
}


def build(ctx):
    ix = maps.index(ctx)
    for fid in ix.dungeon_ids:
        f = {"field": fid}
        sources = []
        sc = ix.scenes.get(fid)
        if sc is not None:
            f["max_users"] = sc.int("maxUsers")
            sources.append("client: SceneList.cdb id %d" % fid)
        name = ctx.name(TYPE, fid) or ""
        m = re.match(r"\(Lv\s*(\d+)\)|\[Lv\s*(\d+)\]", name)
        if m:
            f["level"] = int(m.group(1) or m.group(2))
        ad = ix.admission.get(fid)
        if ad is not None:
            sources.append("client: DungeonAdmission.cdb field %d" % fid)
            cost = []
            for n, mode in ((1, "normal"), (2, "hard")):
                if ad.int("cost%d_item" % n):
                    cost.append({"mode": mode, "item": ad.int("cost%d_item" % n), "count": ad.int("cost%d_count" % n)})
            f["entry_cost"] = cost
            f["event"] = bool(ad.int("flag"))
            f["shown_rewards"] = [ad.int("show_item%d" % n) for n in range(1, 11) if ad.int("show_item%d" % n)]
            f["c17"] = ad.int("c17")
            if ad.str("image"):
                f["image"] = ad.str("image")
            if ad.str("name_key"):
                f["notice_key"] = ad.str("name_key")
        else:
            f["entry_cost"] = []
        if fid in ix.groups:
            sources.append("client: Dungeon.cdb")
            f["dungeon_slots"] = [{"group": g, "slot": s} for g, s in ix.groups[fid]]
        if fid in ix.events:
            sources.append("client: Event_Dungeon.cdb")
            f["event"] = True
            f["schedule"] = [{"from_field": r.int("field"), "hour": r.int("hour"), "minutes": r.int("minutes"),
                              "c2": r.int("c2"), "c3": r.int("c3"), "c4": r.int("c4")} for r in ix.events[fid]]
        boss = ix.doc_boss.get(fid)
        f["boss"] = list(boss[0]) if boss else []
        if boss:
            sources.append("doc: gameplay/maps-and-dungeons § %s (boss)" % boss[2])
            if boss[1]:
                f["gear_tier"] = boss[1]
        nodes = []
        for r in ix.triggers.get(fid, []):
            if r.int("item_or_quest") and r.int("item_or_quest") not in nodes:
                nodes.append(r.int("item_or_quest"))
        if nodes:
            f["gathering"] = nodes
            sources.append("client: Trigger.cdb field %d" % fid)
        f["time_limit_s"] = None
        note = ctx.s(f.get("notice_key"))
        m = re.search(r"time limit\s*:\s*(\d+)\s*(hour|minute|min)", note or "", re.I)
        if m:
            f["time_limit_s"] = int(m.group(1)) * (3600 if m.group(2).lower() == "hour" else 60)
            sources.append("client: %s \"%s\" (entry-panel text)" % (f["notice_key"], note))
        for k, (v, src) in FACTS.get(fid, {}).items():
            f[k] = v
            sources.append(src)
        yield Page(TYPE, fid, ctx.title(TYPE, fid), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, fid = page.fm, page.id
    L, info = [], []
    img = ctx.image(TYPE, fid)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Field", ctx.link("fields", fid, "%s (field %d)" % (page.title, fid))))
    if fm.get("level"):
        info.append(("Level", fm["level"]))
    if fm.get("gear_tier"):
        info.append(("Gear tier dropped", "%s (guides)" % fm["gear_tier"]))
    if fm.get("max_users"):
        info.append(("Max players", "%s (SceneList%s)" % (fm["max_users"], "; guides: max 5 per portal" if fm["max_users"] == 5 else "")))
    info.append(("Event dungeon", "yes" if fm.get("event") else "no"))
    if fm.get("time_limit_s"):
        info.append(("Time limit", "%s min" % fmt_num(fm["time_limit_s"] / 60)))
    if fm.get("notice_key"):
        info.append(("Panel notice", "%s (`%s`)" % (ctx.s(fm["notice_key"]) or "", fm["notice_key"])))
    if fm.get("image"):
        info.append(("Banner", "`%s`" % fm["image"]))
    if fm.get("c17"):
        info.append(("c17 (unknown)", fm["c17"]))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    cost = [c for c in fm.get("entry_cost") or [] if isinstance(c, dict)]
    L += ["### Entry cost", ""]
    if cost:
        L += [table_md(["mode", "ticket", "count"], [(c.get("mode"), ctx.link("items", c["item"]) if isinstance(c.get("item"), int) else c.get("item"), c.get("count")) for c in cost]),
              "`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows "
              "the guides' tables (*inferred*). The 2018 guide numbers differ: "
              "[[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].", ""]
    else:
        L += ["No `DungeonAdmission` row.", ""]

    boss = [b for b in fm.get("boss") or [] if isinstance(b, int)]
    L += ["### Boss", ""]
    if boss:
        L += ["- " + ctx.unit_link(b) + (" (main)" if i == 0 else " (other id in the guides' list; *client* variant)")
              for i, b in enumerate(boss)]
        L.append("")
    else:
        L += ["Not known. Add `boss:` (UnitDB ids) with a source.", ""]

    rew = [r for r in fm.get("shown_rewards") or [] if isinstance(r, int)]
    if rew:
        L += ["### Rewards shown on the entry panel", "",
              "What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates "
              "go on the monster pages.", "", ", ".join(ctx.link("items", r) for r in rew), ""]
    nodes = [n for n in fm.get("gathering") or [] if isinstance(n, int)]
    if nodes:
        L += ["### Gathering", "", "Nodes placed by `Trigger.cdb` give: " + ", ".join(ctx.link("items", n) for n in nodes) +
              ". Positions on the " + ctx.link("fields", fid, "field page") + ".", ""]

    slots = [s for s in fm.get("dungeon_slots") or [] if isinstance(s, dict)]
    if slots:
        L += ["### Dungeon groups", "",
              "`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its "
              "distance to the nation's nearest fort (*guess*, from "
              "[[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).", "",
              "Here: " + ", ".join("group %s slot %s" % (s.get("group"), s.get("slot")) for s in slots), ""]
    sch = [s for s in fm.get("schedule") or [] if isinstance(s, dict)]
    if sch:
        L += ["### Event schedule", "",
              "`Event_Dungeon` rows. The `hour` value is the number the world map's event list shows "
              "([[gameplay/video-dungeon-run#6. Event dungeon list (world map, Dungeon tab)|Nas Village run §6]]); "
              "what it means is not known.", "",
              table_md(["hour?", "open (min)", "row field", "c2", "c3", "c4"],
                       [(s.get("hour"), s.get("minutes"), s.get("from_field"), s.get("c2"), s.get("c3"), s.get("c4")) for s in sch])]

    L += ["### Rules from the guides", "",
          "Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in "
          "[[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. "
          "Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].", ""]
    refs = maps.doc_refs(ctx).get(("fields", fid), [])
    if refs:
        L += ["### Mentioned in", ""] + maps.ref_lines(refs) + [""]
    return "\n".join(L)
