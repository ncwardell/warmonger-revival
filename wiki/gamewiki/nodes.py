"""Nodes: one page per Trigger.cdb row -- the field objects the client places
itself (docs/gameplay/npc-locations.md section 7).

  Trigger   id@00, field@04, type@08 = gadget number (0 for gathering nodes),
            shape@0c (5 gathering, 4 talkable), x@10 / z@14, item_or_quest@28
            (gathering: the material item), model@30.., scale@18, name_key@48
            (UnitName_<n>; not a UnitDB row: UnitName_238 here is "Scout",
            while UnitDB 238 is Wren)

Kinds:
  gather     104 herb / ore nodes in dungeons 121-129 and 142 (type 0, shape 5)
  quest_npc  19 talkable quest gadgets (Scout, Scout Leader, Ghost soldier ...).
             The gadget number links them to Quest: objective type 5 'a',
             giver c12@1c, receiver c19@30 (contract/quests.yaml). The nation
             copies of one gadget share its number (1 = rows 9901/10001/10101).
"""
import re

from . import common
from .common import Page, table_md

TYPE = "nodes"
KIND = "node"
LABEL = "Node"
PLURAL = "Nodes"
DESCRIPTION = ("Field objects the client places itself (`Trigger.cdb`): herb and ore gathering "
               "nodes in the dungeons, and the talkable quest gadgets (Scout, Scout Leader, "
               "Ghost soldier ...). Town NPCs are under [[wiki/npcs/index|NPCs]].")
REQUIRED = ["field", "x", "z"]
REQUIRED_GATHER = ["item", "respawn_s"]       # respawn and yield are server data
REQUIRED_QUEST = ["quests"]


def name(ctx, id_):
    r = ctx.table("Trigger").get(id_)
    if r is None:
        return None
    return ctx.s(r.get("name_key")) or (r.get("name") or "").strip() or None


class Index:
    def __init__(self, ctx):
        self.obj, self.giver, self.receiver = {}, {}, {}
        for q in ctx.table("Quest"):
            qid = q.int("id")
            for n in range(1, 6):
                if q.int("obj%d_type" % n) == 5 and q.int("obj%d_a" % n):
                    self.obj.setdefault(q.int("obj%d_a" % n), []).append(
                        (qid, n, [q.int("obj%d_map%d" % (n, k)) for k in (1, 2, 3)], q.int("obj%d_c" % n)))
            if q.int("c12@1c"):
                self.giver.setdefault(q.int("c12@1c"), []).append(qid)
            if q.int("c19@30"):
                self.receiver.setdefault(q.int("c19@30"), []).append(qid)
        self.talks = {}
        for r in ctx.table("QuestTalk"):
            self.talks.setdefault(r.get("speaker_unit_key"), []).append(r)
        self.docs = None


def build(ctx):
    ix = Index(ctx)
    ctx.nodes_index = ix
    for r in ctx.table("Trigger"):
        id_ = r.int("id")
        gadget = r.int("type")
        kind = "gather" if gadget == 0 and r.int("shape") == 5 else "quest_npc" if r.int("shape") == 4 else "other"
        f = {"kind": kind, "field": r.int("field"), "x": r.float("x"), "z": r.float("z")}
        if gadget:
            f["gadget"] = gadget
        f["shape"] = r.int("shape")
        f["name_key"] = r.str("name_key")
        f["model"] = r.int("model")
        f["scale"] = r.float("scale")
        sources = ["client: Trigger.cdb id %d" % id_]
        req = list(REQUIRED)
        if kind == "gather":
            f["item"] = r.int("item_or_quest") or None
            f.setdefault("respawn_s", None)
            req += REQUIRED_GATHER
        elif r.int("item_or_quest"):
            f["item_or_quest"] = r.int("item_or_quest")
        if gadget:
            q = {}
            obj = [qid for qid, _n, _m, _c in ix.obj.get(gadget, [])]
            if obj:
                q["objective"] = sorted(set(obj))
            if ix.giver.get(gadget):
                q["gives"] = ix.giver[gadget]
            if ix.receiver.get(gadget):
                q["receives"] = ix.receiver[gadget]
            if q:
                f["quests"] = q
                sources.append("client: Quest.cdb objective type 5 / c12@1c / c19@30 (gadget %d)" % gadget)
            gives_item = sorted({c for _q, _n, _m, c in ix.obj.get(gadget, []) if c})
            if gives_item:
                f["quest_items"] = gives_item
            req += REQUIRED_QUEST
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body, required=req)


def body(ctx, page):
    ix = ctx.nodes_index
    fm, id_ = page.fm, page.id
    L = []
    info = []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Trigger id", "`%d`" % id_))
    info.append(("Kind", {"gather": "gathering node", "quest_npc": "talkable quest gadget"}.get(fm.get("kind"), fm.get("kind"))))
    info.append(("Field", "%s at (%s, %s)" % (ctx.link("fields", fm["field"]), fm.get("x"), fm.get("z"))))
    if fm.get("gadget"):
        info.append(("Gadget number", "`%d` (what quests refer to)" % fm["gadget"]))
    if fm.get("item"):
        info.append(("Gives", ctx.link("items", fm["item"])))
    if fm.get("respawn_s") is not None:
        info.append(("Respawn", "%s s" % fm["respawn_s"]))
    info.append(("Model", "ObjectList `%s`, scale %s" % (fm.get("model"), fm.get("scale"))))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    if fm.get("kind") == "gather":
        L += ["Gathering nodes are client data only for their place and material. How long a node "
              "takes to come back (`respawn_s`), how many items it gives and how long gathering "
              "takes were server rules; add them with a source when known.", ""]

    q = fm.get("quests") if isinstance(fm.get("quests"), dict) else {}
    if q:
        L += ["### Quests", ""]
        for key, text in (("objective", "Must be reached or talked to in"), ("gives", "Gives"),
                          ("receives", "Takes the turn-in of")):
            if q.get(key):
                L.append("- **%s:** %s" % (text, ", ".join(ctx.link("quests", x) for x in q[key])))
        if fm.get("quest_items"):
            L.append("- **Quest item handed out:** %s" % ", ".join(ctx.link("items", i) for i in fm["quest_items"]))
        L.append("")
        talks = ix.talks.get(fm.get("name_key"), [])
        if talks:
            L += ["Speaks in `QuestTalk` rows %s (the dialogue is on the quest pages)." % ", ".join(
                sorted({t.get("quest_id") for t in talks}, key=int)), ""]
        copies = [i for i, p in ctx.pages(TYPE).items() if p.get("gadget") == fm.get("gadget") and i != id_]
        if copies:
            L += ["Same gadget in the other nations' copies: %s." % ", ".join(
                ctx.link(TYPE, i, "%s (%d)" % (ctx.title(TYPE, i), i)) for i in sorted(copies)), ""]

    # mentions in the hand-written pages
    from .npcs import gameplay_docs, near_times, TS_RE
    if ix.docs is None:
        ix.docs = gameplay_docs()
    id_re = re.compile(r"(?<![\w=.:/#-])%d(?![\w.:%%])" % id_)
    hits = []
    for stem, title, text in ix.docs:
        ts = []
        found = False
        for line in text.split("\n"):
            if id_re.search(TS_RE.sub("", line)) and ("Trigger" in line or "trigger" in line or (page.title or "") in line):
                found = True
                ts += [t for t in near_times(line, id_re) if t not in ts]
        if found:
            hits.append("- [[gameplay/%s|%s]]%s" % (stem, common.link_text(title), " at " + ", ".join(ts[:6]) if ts else ""))
    if hits:
        L += ["### Seen in", ""] + hits + [""]
    return "\n".join(L)
