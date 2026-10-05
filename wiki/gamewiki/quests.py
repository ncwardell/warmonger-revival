"""Quests: one page per Quest.cdb row.

Client sources (data/tables/*.tsv; contract/quests.yaml has the evidence):
  Quest        291 rows. The TSV header names are partly older guesses; what
               each column is (contract/quests.yaml header + server_rules,
               docs/gameplay/video-character-creation-and-tutorial.md §3):
                 kind@02        quest group (loader FUN_0043e5a5 maps it to a
                                display group whose name is QuestType_*; the
                                Client.exe string table order Main, Sub,
                                Repeat, Guide, Daily, Guild, NDaily, NWeek,
                                NMonth, Help gives groups 1..10)
                 c4@08          prerequisite completion bit (0 = none)
                 c5@0c          exclusion bit (0 = none)
                 c6@04          this quest's completion bit (0 = none: no
                                bit is set, the quest can be taken again)
                 c7@10          contract: fort index the player's nation must
                                own; the values are 121-129 (dungeon fields)
                 map1..3@12     offer map per nation (Arslan, Erion, Armia)
                 start_npc?@18  giver NPC (UnitDB template)
                 c12@1c         giver gadget (Trigger type@08 number)
                 prev_quest?@20 OFFER dialogue (QuestTalk id)
                 c14@11         'automatic' flag (contract: auto-complete
                                when there is no receiver)
                 map4..6@24     turn-in map per nation
                 c18@2c         turn-in NPC
                 c19@30         turn-in gadget
                 next_quest?@34 COMPLETION dialogue (QuestTalk id)
                 pre1..5        prerequisites {type, a..e}
                 flag1..5@f0    objective stages (cumulative end index)
                 obj1..5        {type, a..e, map1..3, u16, quick-text key}
                 rew1..5        {type, a..e}
                 help_image / help_text_key   tip window
  QuestTalk    dialogue rows (speaker, portrait, 10 lines {side 0 NPC /
               1 player, type 1 line / 5-6 end, text key})
  NoticeQuest  quest-board rows (c2@04 = board tab 0 Free / 1 War / 2 Daily,
               matching GUI_QuestBoard_SubTitle_0..2; *inferred*)
  UnitDB       kill groups: objective unit ids >= 9999 are matched against
               UnitDB i32@80 (docs/gameplay/precept-shop.md)
  Trigger      quest gadgets (nodes): gadget number = Trigger type@08

Chain: quest B follows quest A when B's prerequisite bit (c4) is A's
completion bit (c6). ``next`` lists them. Some follow-ups are not chained by
bits (quest 6 has no giver and no prerequisite; the server starts it at the
quest 5 turn-in, per the videos): VIDEO_NEXT adds those, with the source. An
empty ``next`` counts as missing only for main (kind 0) quests, where the
story is expected to continue; elsewhere a chain end is normal.

Objective and reward types whose parameters are not understood yet are not
written to ``objectives`` / ``rewards`` (so those stay *missing*); the raw rows
go to ``objectives_client`` / ``rewards_client`` instead. Once a person (or a
better decoder here) fills ``objectives``, the hand value is kept.

Hand-written knowledge (docs/gameplay/*.md) is linked per quest with the
video timestamp of each mention ("Seen in"). Displayed exp (``shown``) uses the
rule the videos observed (video-early-quests.md §4: kind 0 shows table / 1.1,
kind 1 table / 1.2, kind 3 the table value; kind 2 lessons show the table value,
video-tutorial-walkthrough.md step 3-5).
"""
import re

from . import common
from .common import Page, clean_text, fmt_num, quote, repeat, table_md

TYPE = "quests"
KIND = "quest"
LABEL = "Quest"
PLURAL = "Quests"
DESCRIPTION = ("Every quest in the client's `Quest.cdb`: the story chain, side quests, lessons "
               "(tutorial tips), repeatable, war, daily/weekly/monthly board quests and advice "
               "quests, with givers, objectives, rewards, chain and dialogue. The tutorial chain "
               "as played is described in [[gameplay/video-tutorial-walkthrough|Video notes: tutorial "
               "walkthrough]] and [[gameplay/video-character-creation-and-tutorial|Video notes: "
               "character creation and tutorial]].")
REQUIRED = ["giver", "turn_in", "objectives", "rewards", "next"]

NATIONS = ["Arslan", "Erion", "Armia"]
# kind@02 -> display group (loader switch) -> QuestType_* string key
KIND_GROUP = {0: 1, 1: 2, 2: 4, 3: 3, 7: 5, 8: 5, 9: 7, 10: 8, 11: 9, 12: 10}
GROUP_KEY = {1: "QuestType_Main", 2: "QuestType_Sub", 3: "QuestType_Repeat", 4: "QuestType_Guide",
             5: "QuestType_Daily", 6: "QuestType_Guild", 7: "QuestType_NDaily", 8: "QuestType_NWeek",
             9: "QuestType_NMonth", 10: "QuestType_Help"}
# exp shown in the reward panel = table / factor (video observation, see docstring)
EXP_SHOWN = {0: 1.1, 1: 1.2, 2: 1.0, 3: 1.0}
EXP_SOURCE = {
    0: "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)",
    1: "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)",
    2: "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)",
    3: "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)",
}
AUTO_GIVER_KINDS = {0, 1, 2, 12}
# Follow-ups the client data does not chain (no bit links them) but the videos
# show: {quest: ([next quest ids], source)}. Main-story chain ends with no
# entry here stay *missing* 'next' until someone checks them.
VIDEO_NEXT = {
    5: ([6, 28], "video: [[gameplay/video-character-creation-and-tutorial]] step 11 and "
                 "[[gameplay/video-tutorial-walkthrough]] steps 10 and 16 (quests 6 and 28 start "
                 "at the quest 5 turn-in)"),
}
AUTO_GIVER_SOURCE = ("video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain "
                     "quests start on their own)")
CLASS_IDS = {1: "Saint", 4: "Punisher", 5: "Guardian", 7: "Valkyrie"}     # Create_Char class@00
CLASS_MASK = [(1, "Saint"), (2, "Punisher"), (16, "Guardian"), (4, "Valkyrie")]
BOARD_TABS = {0: "Free", 1: "War", 2: "Daily"}
# Daily / weekly / monthly quests: c6@04 is a bit of the periodic done mask
# (byte kind-9 of G+0x2e6c), not of the 320-bit completion flags (contract).
PERIODIC = {9: "daily", 10: "weekly", 11: "monthly"}
# Objective type 1 targets that are not units (UnitDB 1 is a player class):
# read from the tracker texts ("Every monster will be counted", "Killed
# Middle boss", "Killed boss", "Boss Hunting"); *inferred*.
SPECIAL_TARGETS = {1: "any_monster", 2: "any_middle_boss", 3: "any_boss"}
TARGET_TEXT = {"any_monster": "any monster", "any_middle_boss": "any middle boss", "any_boss": "any boss"}

# Objective types: (label, {front-matter key: column}) -- None = parameters
# not understood yet (row goes to objectives_client).
OBJ = {
    0: ("report", {}),                                   # tracker line only (e.g. "Bring them to Floyd")
    1: ("kill", None),                                   # handled specially
    3: ("acquire_item", {"item": "a", "count": "b"}),
    4: ("talk", {"npc": "a", "talk": "e"}),
    5: ("gadget", {"gadget": "a", "talk": "e"}),
    7: ("reach_level", {"level": "a"}),
    8: ("gather", {"item": "a", "count": "b"}),
    9: ("sell_item", {"item": "a", "count": "b"}),
    10: ("buy_item", {"item": "a", "count": "b"}),
    11: ("craft_item", {"item": "a", "count": "b"}),
    12: ("reach_map", {"map": "b"}),
    13: ("use_item", {"item": "a", "count": "b"}),
    # client-detected events (C->S 0x492), contract/quests.yaml
    10001: ("client_attack", {"param": "a"}),
    10003: ("client_equip", {"slot": "a"}),
    10004: ("client_open_panel", {"panel": "a"}),
    10005: ("client_item_update", {"param": "a"}),
    10007: ("client_legion_core", {"item": "a"}),
    10008: ("client_swap_weapon", {}),
    10009: ("client_value", {"param": "a"}),
    10010: ("client_decompose", {"item": "a"}),
    10012: ("client_equip_rune", {}),
}
OBJ_TEXT = {
    0: "report (tracker line, done at the turn-in)", 1: "kill / collect", 2: "kill enemy players?",
    3: "acquire item", 4: "talk to NPC", 5: "talk to quest gadget", 6: "reinforce?", 7: "reach level",
    8: "gather", 9: "sell item", 10: "buy item", 11: "craft item", 12: "reach map", 13: "use item",
    14: "move to battlefield / monster area?", 15: "monster-area war / occupation?", 17: "expand inventory?",
    21: "join or create a legion?", 22: "invite legion members?", 23: "legion battle?", 24: "sell ether?",
    25: "buy ether?", 26: "craft gear (category a)?", 28: "rune reinforcement?", 29: "attack tower?",
    30: "build nexus?", 31: "imprint?", 32: "set TP skill?", 33: "nexus add-on?", 34: "dimension gate?",
    10001: "client event: attack / skill used", 10003: "client event: equip (a = slot kind)",
    10004: "client event: panel opened (a: 1 world map, 2 reinforce, 3 TP panel, 4 quest board)",
    10005: "client event: item update", 10007: "client event: legion core / item use",
    10008: "client event: weapon swap", 10009: "client event: value reached", 10010: "client event: decomposition",
    10012: "client event: rune equipped", 10013: "client event: transform? (no client sender found)",
}
# Reward types understood well enough for a server (contract + videos).
REW_TEXT = {1: "item", 2: "exp", 4: "gold", 5: "fame?", 6: "negative value (cost?)", 7: "unknown 7",
            8: "item", 9: "unknown 9", 10: "unknown 10"}


def name(ctx, id_):
    row = ctx.table("Quest").get(id_)
    if row is None:
        return None
    return ctx.s(row.get("title_key")) or (row.get("name(Eng)") or "").strip() or None


# ---------------------------------------------------------------------- index

class Index:
    def __init__(self, ctx):
        t = ctx.table
        self.quests = list(t("Quest"))
        self.by_bit = {}
        self.by_req = {}
        for q in self.quests:
            if q.int("c6") and q.int("kind") not in PERIODIC:
                self.by_bit.setdefault(q.int("c6"), []).append(q.int("id"))
            if q.int("c4"):
                self.by_req.setdefault(q.int("c4"), []).append(q.int("id"))
        self.talk = t("QuestTalk").by()
        self.board = {}
        for r in t("NoticeQuest"):
            if r.int("quest_id"):
                self.board.setdefault(r.int("quest_id"), []).append(r)
        self.groups = {}
        for u in t("UnitDB"):
            g = u.int("i32@80")
            if g:
                self.groups.setdefault(g, []).append(u.int("id"))
        self.units = t("UnitDB").by()
        self.gadgets = {}
        try:
            for r in t("Trigger"):
                if r.int("shape") == 4 and r.int("type"):
                    self.gadgets.setdefault(r.int("type"), []).append(r.int("id"))
        except OSError:
            pass
        self.dungeon_fields = {r.int("field") for r in t("DungeonAdmission")}
        self.server = server_quests()
        self.seen = seen_in(ctx, self)


def server_quests():
    """Quest ids server/quests.py currently enables (its allowlist)."""
    try:
        text = (common.REPO / "server" / "quests.py").read_text(encoding="utf-8")
    except OSError:
        return set()
    m = re.search(r"qid not in \(([\d,\s]+)\)", text)
    return {int(x) for x in re.findall(r"\d+", m.group(1))} if m else set()


# ---------------------------------------------------- hand-written knowledge

TS = re.compile(r"\[(\d+(?::\d\d){1,2})\]\((https?://[^)\s]+)\)")
REF = re.compile(r"\b(?:[Qq]uests?|[Ll]essons?)\s+((?:[`*]*\d+[`*]*(?:\s*(?:/|,|→|–|and|or)\s*(?=[`*]*\d))?)+)")
QSHORT = re.compile(r"\bQ(\d{1,4})\b")
BOLD = re.compile(r"(\*{1,2})([^*\n]+?)\1\s*\(([^)\n]*)")
STEP = re.compile(r"^\s*(\d+)\.\s")


def _norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def seen_in(ctx, ix):
    """{quest id: {doc: (title, [(step, ts text, url)])}} from docs/gameplay."""
    titles = {q.int("id"): _norm(ctx.name(TYPE, q.int("id"))) for q in ix.quests}
    by_title = {}
    for qid, t in titles.items():
        by_title.setdefault(t, set()).add(qid)
    out = {}
    for f in sorted((common.DOCS / "gameplay").glob("*.md")):
        fm, body = common.parse_front_matter(f.read_text(encoding="utf-8"))
        doc = "gameplay/" + f.stem
        dtitle = fm.get("title") or f.stem
        for line in body.split("\n"):
            hits = {}
            for m in REF.finditer(line):
                grp = m.group(1)
                if re.match(r"\s+(?:bosses|monsters|kills|times|points|exp|gold|days)\b", line[m.end():]):
                    continue                                 # "Boss Hunt quest 50 bosses"
                for a, b in re.findall(r"(\d+)\s*–\s*(\d+)", grp):
                    if 0 < int(b) - int(a) <= 30:
                        for n in range(int(a), int(b) + 1):
                            hits.setdefault(n, m.start())
                for n in re.findall(r"\d+", grp):
                    if m.group(0)[0] in "Qq" or int(n) >= 100:      # "Lesson 1" is not quest 1
                        hits[int(n)] = min(hits.get(int(n), m.start()), m.start())
            for m in QSHORT.finditer(line):
                hits[int(m.group(1))] = min(hits.get(int(m.group(1)), m.start()), m.start())
            for m in BOLD.finditer(line):
                want = _norm(re.sub(r'^.*?"(.*)"$', r"\1", m.group(2)))
                cand = by_title.get(want, set())
                for n in re.findall(r"`(\d+)`", m.group(3)):
                    if int(n) in cand:
                        hits[int(n)] = min(hits.get(int(n), m.start()), m.start())
            if not hits:
                continue
            stamps = [(m.start(), m.group(1), m.group(2)) for m in TS.finditer(line)]
            sm = STEP.match(line)
            step = int(sm.group(1)) if sm else None
            for qid, pos in hits.items():
                if qid not in titles:
                    continue
                ts = min(stamps, key=lambda s: abs(s[0] - pos)) if stamps else None
                entry = (step, ts[1] if ts else None, ts[2] if ts else None)
                lst = out.setdefault(qid, {}).setdefault(doc, (dtitle, []))[1]
                if entry not in lst:
                    lst.append(entry)
    return out


# ---------------------------------------------------------------------- build

def _vals(row, prefix, n):
    return {x: row.int("%s%d_%s" % (prefix, n, x)) for x in "abcde"}


def objectives_of(ctx, ix, q):
    """-> (decoded list, all understood?)"""
    out, ok = [], True
    for n in range(1, 6):
        t = q.int("obj%d_type" % n)
        v = _vals(q, "obj", n)
        key = q.str("obj%d_text_key" % n)
        if not t and not ctx.s(key):
            continue
        maps = [q.int("obj%d_map%d" % (n, k)) for k in (1, 2, 3)]
        o = {"n": n, "type": t}
        if t == 1:
            target = v["a"]
            if target in SPECIAL_TARGETS:
                o.update(what="collect" if v["d"] else "kill", target=SPECIAL_TARGETS[target])
            elif target in ix.units:
                o.update(what="collect" if v["d"] else "kill", unit=target)
            elif target in ix.groups:
                o.update(what="collect" if v["d"] else "kill", unit_group=target, units=ix.groups[target])
            else:
                o.update(what="collect" if v["d"] else "kill", target=target)
                ok = False          # 2 / 3 / 9999: boss classes? not a unit or group
            o["count"] = v["b"]
            if v["d"]:
                o.update(item=v["d"], rate=v["c"])
        elif t in OBJ and OBJ[t][1] is not None:
            o["what"] = OBJ[t][0]
            for k, col in OBJ[t][1].items():
                if v[col]:
                    o[k] = v[col]
            rest = {c: v[c] for c in "abcde" if v[c] and c not in OBJ[t][1].values()}
            if rest:
                o["extra"] = rest
        else:
            o["what"] = None
            o.update({c: v[c] for c in "abcde" if v[c]})
            ok = False
        if any(maps):
            o["maps"] = maps
        if key:
            o["text_key"] = key
        out.append(o)
    return out, ok


def rewards_of(ctx, q):
    out, ok = [], True
    kind = q.int("kind")
    for n in range(1, 6):
        t = q.int("rew%d_type" % n)
        if not t:
            continue
        v = _vals(q, "rew", n)
        r = {"type": t}
        if t == 2:
            r.update(what="exp", amount=v["a"])
            if kind in EXP_SHOWN:
                r["shown"] = int(round(v["a"] / EXP_SHOWN[kind]))
        elif t == 4:
            r.update(what="gold", amount=v["a"])
        elif t == 1:
            r.update(what="item", item=v["b"], count=v["c"] or 1)
            a = v["a"]
            if a == 0:
                r["pick"] = "fixed"
            elif a == 11:
                r["pick"] = "choose"
            elif a in CLASS_IDS:
                r.update(pick="class", **{"class": CLASS_IDS[a]})
            else:
                r.update(pick=None, a=a)
                ok = False
            if v["e"]:
                r["e"] = v["e"]
            if v["d"]:
                r["d"] = v["d"]
        elif t == 8:
            r.update(what="item", item=v["a"], count=v["b"] or 1, pick="fixed")
        else:
            r["what"] = None
            r.update({c: v[c] for c in "abcde" if v[c]})
            ok = False
        out.append(r)
    return out, ok


def prerequisites_of(q):
    out = []
    for n in range(1, 6):
        t = q.int("pre%d_type" % n)
        if not t:
            continue
        v = _vals(q, "pre", n)
        p = {"type": t}
        if t == 1:
            p.update(what="class", classes=[c for b, c in CLASS_MASK if v["a"] & b], mask=v["a"])
        elif t == 4:
            p.update(what="level")
            if v["a"]:
                p["a"] = v["a"]
            if v["b"]:
                p["min"] = v["b"]
            if v["c"]:
                p["max"] = v["c"]
        elif t == 6:
            p.update(what="item", item=v["a"], count=v["b"] or 1)
        elif t == 7:
            p.update(what="legion?", **{c: v[c] for c in "abcde" if v[c]})
        else:
            p.update(what=None, **{c: v[c] for c in "abcde" if v[c]})
        out.append(p)
    return out


def build(ctx):
    ix = Index(ctx)
    ctx.quests_index = ix
    for q in ix.quests:
        id_ = q.int("id")
        kind = q.int("kind")
        f = {}
        sources = ["client: Quest.cdb id %d" % id_]
        if not q.str("title_key") and not any(q.int("%s%d_type" % (p, n)) for p in ("obj", "rew") for n in range(1, 6)) \
                and not q.int("start_npc") and not q.int("c12"):
            # 13 placeholder rows (825-837): no title, objectives, rewards or giver.
            yield Page(TYPE, id_, ctx.title(TYPE, id_), fields={"kind": kind, "unused": True},
                       sources=sources, body=body, required=[])
            continue
        f["name_key"] = q.str("title_key")
        f["kind"] = kind
        grp = KIND_GROUP.get(kind, 6)
        f["kind_name"] = ctx.s(GROUP_KEY[grp])
        pre = prerequisites_of(q)
        lv = next((p for p in pre if p.get("what") == "level"), None)
        if lv and (lv.get("min") or lv.get("max")):
            f["level"] = {k: lv[k] for k in ("min", "max") if k in lv}
        cls = next((p for p in pre if p.get("what") == "class"), None)
        if cls:
            f["classes"] = cls["classes"]

        # giver / turn-in
        board = ix.board.get(id_, [])
        if q.int("start_npc"):
            f["giver"] = {"npc": q.int("start_npc")}
        elif q.int("c12"):
            f["giver"] = {"gadget": q.int("c12")}
        elif board:
            f["giver"] = {"board": board[0].int("id")}
            sources.append("client: NoticeQuest.cdb id %s" % ", ".join(str(r.int("id")) for r in board))
        elif kind in AUTO_GIVER_KINDS:
            f["giver"] = {"auto": True}
            sources.append(AUTO_GIVER_SOURCE)
        else:
            f["giver"] = None
        if q.int("c18"):
            f["turn_in"] = {"npc": q.int("c18")}
        elif q.int("c19"):
            f["turn_in"] = {"gadget": q.int("c19")}
        elif q.int("c14"):
            f["turn_in"] = {"auto": True}
        else:
            f["turn_in"] = None
        offer = [q.int("map%d" % k) for k in (1, 2, 3)]
        back = [q.int("map%d" % k) for k in (4, 5, 6)]
        if any(offer):
            f["offer_maps"] = offer
        if any(back):
            f["turn_in_maps"] = back
        periodic = kind in PERIODIC
        if periodic:
            f["periodic"] = {"reset": PERIODIC[kind], "mask_bit": q.int("c6")}
        else:
            f["bit"] = q.int("c6")
        if q.int("c4"):
            f["requires_bit"] = q.int("c4")
        if q.int("c5"):
            f["excludes_bit"] = q.int("c5")
        if q.int("c7"):
            f["owned_field"] = q.int("c7")
        if q.int("c14"):
            f["automatic"] = True
        f["prev"] = sorted(x for x in ix.by_bit.get(q.int("c4"), []) if x != id_) if q.int("c4") else []
        f["next"] = sorted(x for x in ix.by_req.get(q.int("c6"), []) if x != id_) if q.int("c6") and not periodic else []
        if id_ in VIDEO_NEXT:
            f["next"] = sorted(set(f["next"]) | set(VIDEO_NEXT[id_][0]))
            sources.append(VIDEO_NEXT[id_][1])
        f["prev"] = sorted(set(f["prev"]) | {k for k, (v, _s) in VIDEO_NEXT.items() if id_ in v})
        if pre:
            f["prerequisites"] = pre
        f["stages"] = [q.int("flag%d" % k) for k in range(1, 6)]
        objs, obj_ok = objectives_of(ctx, ix, q)
        rews, rew_ok = rewards_of(ctx, q)
        f["objectives"] = objs if obj_ok else None
        if not obj_ok:
            f["objectives_client"] = objs
        f["rewards"] = rews if rew_ok else None
        if not rew_ok:
            f["rewards_client"] = rews
        if any(r.get("shown") for r in rews):
            sources.append(EXP_SOURCE[kind])
        talks = {}
        if q.int("prev_quest"):
            talks["offer"] = q.int("prev_quest")
        if q.int("next_quest"):
            talks["complete"] = q.int("next_quest")
        f.update({"offer_talk": talks.get("offer"), "complete_talk": talks.get("complete")})
        for o in objs:
            if o.get("talk"):
                talks.setdefault("objective %d" % o["n"], o["talk"])
        for tid in sorted(set(talks.values())):
            if tid in ix.talk:
                sources.append("client: QuestTalk.cdb id %d" % tid)
        if q.str("help_image") or q.str("help_text_key"):
            f["help"] = {k: v for k, v in (("image", q.str("help_image")), ("text_key", q.str("help_text_key"))) if v}
        if board:
            f["board"] = [{"row": r.int("id"), "tab": r.int("c2")} for r in board]
        # Which REQUIRED fields the client data itself settles as "none":
        # a chain end (no quest requires this bit) and a quest with no rewards.
        req = list(REQUIRED)
        if not f["next"] and kind != 0:
            req.remove("next")       # side / repeat / help quests: a chain end is normal
        if rew_ok and not rews:
            req.remove("rewards")
        if obj_ok and not objs and f["turn_in"]:
            req.remove("objectives")
        f = {k: v for k, v in f.items() if v is not None or k in REQUIRED}
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body, required=req)


# ------------------------------------------------------------------ rendering

def field_link(ctx, ix, fid):
    if not fid:
        return "—"
    return ctx.link("dungeons" if fid in ix.dungeon_fields else "fields", fid) + " (%d)" % fid


def maps_text(ctx, ix, maps):
    if not maps or not any(maps):
        return None
    if len(set(maps)) == 1:
        return field_link(ctx, ix, maps[0])
    return " · ".join("%s: %s" % (n, field_link(ctx, ix, m)) for n, m in zip(NATIONS, maps))


def gadget_link(ctx, ix, g):
    rows = ix.gadgets.get(g, [])
    if not rows:
        return "gadget %d (no Trigger row)" % g
    return "%s (gadget %d)" % (" / ".join(ctx.link("nodes", r) for r in rows[:3]), g)


def who(ctx, ix, ref):
    if not isinstance(ref, dict):
        return None
    if ref.get("npc"):
        return ctx.unit_link(ref["npc"])
    if ref.get("gadget"):
        return gadget_link(ctx, ix, ref["gadget"])
    if ref.get("board"):
        return "quest board (NoticeQuest row %s)" % ref["board"]
    if ref.get("auto"):
        return "automatic"
    return ", ".join("%s %s" % kv for kv in ref.items())


def item_n(ctx, item, count):
    return "%s × %s" % (ctx.link("items", item), fmt_num(count)) if count and count != 1 else ctx.link("items", item)


def objective_line(ctx, ix, o, need_text):
    t, w = o.get("type"), o.get("what")
    txt = None
    if t == 1:
        if o.get("unit"):
            tgt = ctx.unit_link(o["unit"])
        elif o.get("unit_group"):
            us = o.get("units") or []
            tgt = "any unit of kill group %d (%s)" % (o["unit_group"], ", ".join(ctx.unit_link(u) for u in us[:6]))
        elif o.get("target") in TARGET_TEXT:
            tgt = TARGET_TEXT[o["target"]] + " (target code %s)" % {v: k for k, v in SPECIAL_TARGETS.items()}[o["target"]]
        else:
            tgt = "target `%s` (not a unit or kill group)" % o.get("target")
        if o.get("item"):
            txt = "Collect %s from %s (drop %s%%)" % (item_n(ctx, o["item"], o.get("count")), tgt, o.get("rate"))
        else:
            txt = "Kill %s × %s" % (tgt, o.get("count"))
    elif w == "talk":
        txt = "Talk to %s" % ctx.unit_link(o["npc"]) + (" (dialogue %d)" % o["talk"] if o.get("talk") else "")
    elif w == "gadget":
        txt = "Talk to %s" % gadget_link(ctx, ix, o["gadget"]) + (" (dialogue %d)" % o["talk"] if o.get("talk") else "")
    elif w == "reach_level":
        txt = "Reach level %s" % o.get("level")
    elif w == "reach_map":
        txt = "Go to %s" % field_link(ctx, ix, o.get("map"))
    elif w in ("acquire_item", "gather", "sell_item", "buy_item", "craft_item", "use_item"):
        verb = {"acquire_item": "Acquire", "gather": "Gather", "sell_item": "Sell", "buy_item": "Buy",
                "craft_item": "Craft", "use_item": "Use"}[w]
        txt = "%s %s" % (verb, item_n(ctx, o.get("item"), o.get("count")) if o.get("item") else "an item")
    elif w == "report":
        txt = "Report (tracker line; done by turning the quest in)"
    elif w and w.startswith("client_"):
        txt = OBJ_TEXT.get(t, w)
        if o.get("item"):
            txt += ": " + ctx.link("items", o["item"])
        elif any(k in o for k in ("param", "slot", "panel")):
            txt += " (a = %s)" % (o.get("param") or o.get("slot") or o.get("panel"))
    else:
        txt = "Type %s — %s; values %s" % (t, OBJ_TEXT.get(t, "unknown"), ", ".join(
            "%s=%s" % (c, o[c]) for c in "abcde" if c in o) or "none")
    if o.get("extra"):
        txt += " (also %s)" % ", ".join("%s=%s" % kv for kv in o["extra"].items())
    shown = ctx.s(o.get("text_key")) if need_text else None
    if shown:
        shown = clean_text(shown).replace("%s", "(0/%s)" % o.get("count") if o.get("count") else "").replace("\n", " ").strip()
        txt += " — tracker: “%s”" % shown
    return txt


def reward_line(ctx, r):
    w = r.get("what")
    if w == "exp":
        s = "%s exp" % fmt_num(r.get("amount", 0))
        if r.get("shown") is not None and r.get("shown") != r.get("amount"):
            s += " (shown in game as %s)" % fmt_num(r["shown"])
        return s
    if w == "gold":
        return "%s gold" % fmt_num(r.get("amount", 0))
    if w == "item":
        return item_n(ctx, r.get("item"), r.get("count")) + (" (e = %s)" % r["e"] if r.get("e") else "")
    return "Type %s — %s; values %s" % (r.get("type"), REW_TEXT.get(r.get("type"), "unknown"), ", ".join(
        "%s=%s" % (c, r[c]) for c in "abcde" if c in r) or "none")


def dialogue(ctx, ix, tid, expect=None, gadget=None, player="You"):
    """QuestTalk row as a quote. The speaker is linked to ``expect`` (the
    quest's giver / turn-in / objective NPC) when the names agree, else to the
    row's speaker_unit_key unit when that name agrees; speaker_unit_key alone
    is not reliable (QuestTalk 641 'Scout' names UnitName_238 = Wren)."""
    r = ix.talk.get(tid)
    if r is None:
        return ["*QuestTalk %d is not in the client.*" % tid, ""]
    speaker = ctx.s(r.get("speaker_key")) or "NPC"
    short = speaker.split(":")[0].strip()
    m = re.match(r"UnitName_(\d+)$", r.get("speaker_unit_key") or "")
    L = []
    cands = [u for u in (expect, int(m.group(1)) if m else None) if u and u in ix.units]
    unit = next((u for u in cands if _norm(ctx.name(ctx.unit_type(u), u)) == _norm(short)), None)
    gad = gadget if gadget else None
    if unit:
        L += ["Speaker: %s" % ctx.unit_link(unit), ""]
    elif gad and gad in ix.gadgets:
        L += ["Speaker: %s" % gadget_link(ctx, ix, gad), ""]
    elif short:
        L += ["Speaker: %s" % short, ""]
    lines = []
    for side, typ, key, _p in repeat(r, "line%d_side", "line%d_type", "line%d_text_key", "line%d_param",
                                     skip_zero=False):
        text = ctx.s(key) if isinstance(key, str) else None
        if typ in (5, 6) and not text:
            lines.append("*(%s)*" % ("accept / continue" if typ == 5 else "end"))
            continue
        if not text:
            continue
        who_ = player if side == 1 else short
        body = clean_text(text).strip().replace("\n", "<br>")
        lines.append("**%s:** %s" % (who_, body))
    L += ["\n".join("> " + l + "  " if i < len(lines) - 1 else "> " + l for i, l in enumerate(lines)), ""]
    return L


def body(ctx, page):
    ix = ctx.quests_index
    fm, id_ = page.fm, page.id
    q = ctx.table("Quest").get(id_)
    L = []
    if fm.get("unused"):
        return ("Empty row in the client's `Quest.cdb` (row %d, kind %s): no title, giver, objectives or "
                "rewards. Probably a placeholder; the server can skip it (`unused: true`)." % (id_, fm.get("kind")))
    img = ctx.image(TYPE, id_)
    giver = fm.get("giver") if isinstance(fm.get("giver"), dict) else {}
    if not img and giver.get("npc"):
        img = ctx.image(ctx.unit_type(giver["npc"]), giver["npc"])
    info = []
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Quest id", "`%d`" % id_))
    info.append(("Kind", "%s (kind %s)" % (fm.get("kind_name") or "?", fm.get("kind"))))
    if isinstance(fm.get("level"), dict):
        lv = fm["level"]
        info.append(("Level", "%s–%s" % (lv.get("min", "?"), lv.get("max", "")) if lv.get("max") else "%s+" % lv.get("min")))
    if fm.get("classes"):
        info.append(("Classes", ", ".join(fm["classes"])))
    info.append(("Giver", who(ctx, ix, fm.get("giver")) or "**unknown**"))
    info.append(("Turn in", who(ctx, ix, fm.get("turn_in")) or "**unknown**"))
    if maps_text(ctx, ix, fm.get("offer_maps")):
        info.append(("Offered on", maps_text(ctx, ix, fm.get("offer_maps"))))
    if maps_text(ctx, ix, fm.get("turn_in_maps")) and fm.get("turn_in_maps") != fm.get("offer_maps"):
        info.append(("Turned in on", maps_text(ctx, ix, fm.get("turn_in_maps"))))
    per = fm.get("periodic") if isinstance(fm.get("periodic"), dict) else None
    if per:
        info.append(("Repeats", "%s (periodic done-mask bit %s; contract: resets daily 00:00 UTC+1 / Monday / the 1st)" % (
            per.get("reset"), per.get("mask_bit"))))
    else:
        info.append(("Completion bit", fm.get("bit") or "none (no bit is set: can be taken again)"))
    if fm.get("requires_bit"):
        info.append(("Requires bit", fm["requires_bit"]))
    if fm.get("excludes_bit"):
        info.append(("Not after bit", fm["excludes_bit"]))
    if fm.get("owned_field"):
        info.append(("Field c7@10", "%s (contract: fort the nation must own)" % field_link(ctx, ix, fm["owned_field"])))
    if fm.get("automatic"):
        info.append(("Automatic flag", "set (c14@11)"))
    if fm.get("board"):
        info.append(("Quest board", ", ".join("row %s, %s tab" % (b.get("row"), BOARD_TABS.get(b.get("tab"), b.get("tab")))
                                              for b in fm["board"] if isinstance(b, dict))))
    if id_ in ix.server:
        info.append(("Current server", "enabled in `server/quests.py`"))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    # chain
    L += ["### Chain", ""]
    prev, nxt = fm.get("prev") or [], fm.get("next") or []
    same = [x for x in ix.by_bit.get(fm.get("bit") or -1, []) if x != id_]
    L.append("- **After:** %s" % (", ".join(ctx.link(TYPE, x) for x in prev) if prev else
                                  ("bit %s (no quest sets it)" % fm["requires_bit"] if fm.get("requires_bit") else "nothing (no prerequisite bit)")))
    L.append("- **Next:** %s" % (", ".join(ctx.link(TYPE, x) for x in nxt) if nxt else "nothing: no quest requires this quest's bit (chain end)"))
    if same:
        L.append("- **Shares completion bit %s with:** %s (completing one closes the others)" % (
            fm.get("bit"), ", ".join(ctx.link(TYPE, x) for x in same)))
    if fm.get("excludes_bit"):
        ex = ix.by_bit.get(fm["excludes_bit"], [])
        L.append("- **Not offered after:** %s" % (", ".join(ctx.link(TYPE, x) for x in ex) or "bit %s" % fm["excludes_bit"]))
    L.append("")

    pre = [p for p in (fm.get("prerequisites") or []) if isinstance(p, dict)]
    if pre:
        rows = []
        for p in pre:
            w = p.get("what")
            if w == "class":
                d = ", ".join(p.get("classes") or []) + " (mask %s)" % p.get("mask")
            elif w == "level":
                d = "level %s%s" % (p.get("min", "?"), "–%s" % p["max"] if p.get("max") else "+") + (
                    " (a = %s, meaning unknown)" % p["a"] if p.get("a") else "")
            elif w == "item":
                d = "carries %s" % item_n(ctx, p.get("item"), p.get("count"))
            else:
                d = ", ".join("%s=%s" % (k, v) for k, v in p.items() if k not in ("type", "what")) or "no values"
            rows.append((p.get("type"), w or "unknown", d))
        L += ["### Requirements", "", table_md(["type", "meaning", "value"], rows)]

    # objectives
    objs = fm.get("objectives")
    shown_objs = objs if isinstance(objs, list) else fm.get("objectives_client")
    L += ["### Objectives", ""]
    if not isinstance(objs, list) and isinstance(shown_objs, list):
        L += ["> [!warning] Not all objective types are decoded",
              "> The rows below are the client's (`objectives_client`). Write the server-ready list "
              "into `objectives:` once the unclear ones are understood.", ""]
    if isinstance(shown_objs, list) and shown_objs:
        for i, o in enumerate(x for x in shown_objs if isinstance(x, dict)):
            line = objective_line(ctx, ix, o, True)
            m = o.get("maps")
            if m and any(m) and m != fm.get("offer_maps"):
                line += " — on " + maps_text(ctx, ix, m)
            L.append("%d. %s" % (o.get("n", i + 1), line))
        st = fm.get("stages")
        if isinstance(st, list) and any(st) and st not in ([5] * 5,):
            L += ["", "Stages (`flag1..5` = %s): objectives unlock in steps; with the first unfinished "
                  "objective *i*, objectives 1..flag*i* are active (contract/quests.yaml)." % st]
        elif isinstance(st, list) and not any(st):
            L += ["", "Stages are all 0: the client never reports progress for this quest (contract/quests.yaml)."]
    else:
        L.append("None in the client: the quest is done by talking to the turn-in NPC." if fm.get("turn_in")
                 else "None in the client.")
    L.append("")

    # rewards
    rews = fm.get("rewards")
    shown_rews = rews if isinstance(rews, list) else fm.get("rewards_client")
    L += ["### Rewards", ""]
    if not isinstance(rews, list) and isinstance(shown_rews, list):
        L += ["> [!warning] Not all reward types are decoded",
              "> The rows below are the client's (`rewards_client`). Write the server-ready list into "
              "`rewards:` once the unclear ones are understood.", ""]
    rl = [r for r in (shown_rews or []) if isinstance(r, dict)]
    if rl:
        basic = [r for r in rl if r.get("what") in ("exp", "gold") or r.get("pick") == "fixed"]
        choose = [r for r in rl if r.get("pick") == "choose"]
        by_class = [r for r in rl if r.get("pick") == "class"]
        other = [r for r in rl if r not in basic and r not in choose and r not in by_class]
        if basic:
            L.append("- **Basic reward:** " + "; ".join(reward_line(ctx, r) for r in basic))
        if choose:
            L.append("- **Choose one:** " + " *or* ".join(reward_line(ctx, r) for r in choose))
        if by_class:
            L.append("- **By class:** " + "; ".join("%s: %s" % (r.get("class"), reward_line(ctx, r)) for r in by_class))
        for r in other:
            L.append("- " + reward_line(ctx, r))
        if any(r.get("shown") not in (None, r.get("amount")) for r in rl):
            L += ["", "The reward panel shows quest exp lower than the table: kind 0 quests show the table "
                  "value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of "
                  "the two the original server granted is not known."]
    else:
        L.append("None in the client.")
    L.append("")

    # dialogue
    talks = []
    tin = fm.get("turn_in") if isinstance(fm.get("turn_in"), dict) else {}
    if fm.get("offer_talk"):
        talks.append(("Offer", fm["offer_talk"], giver.get("npc"), giver.get("gadget")))
    for o in (shown_objs or []):
        if isinstance(o, dict) and o.get("talk"):
            talks.append(("Objective %s" % o.get("n"), o["talk"], o.get("npc"), o.get("gadget")))
    if fm.get("complete_talk"):
        talks.append(("Completion", fm["complete_talk"], tin.get("npc"), tin.get("gadget")))
    if talks:
        L += ["### Dialogue", ""]
        done = set()
        for label, tid, unit, gad in talks:
            if tid in done:
                continue
            done.add(tid)
            L += ["#### %s (QuestTalk %d)" % (label, tid), ""]
            L += dialogue(ctx, ix, tid, unit, gad)
    help_ = fm.get("help") if isinstance(fm.get("help"), dict) else {}
    ht = ctx.s(help_.get("text_key")) if help_ else None
    if ht or help_.get("image"):
        L += ["### Tip window", ""]
        if ht:
            L.append(quote(ht))
        if help_.get("image"):
            L += ["Image `%s`." % help_["image"], ""]

    # hand-written knowledge
    seen = ix.seen.get(id_, {})
    if seen:
        L += ["### Seen in", ""]
        for doc, (title, entries) in sorted(seen.items()):
            parts = []
            for step, ts, url in entries[:6]:
                s = ("step %d" % step) if step else ""
                if ts:
                    s += (" at " if s else "at ") + "[%s](%s)" % (ts, url)
                if s:
                    parts.append(s)
            L.append("- [[%s|%s]]%s" % (doc, common.link_text(str(title)), ": " + "; ".join(parts) if parts else ""))
        L.append("")
    ment = [m for m in ctx.mentions(page.title if fm.get("name_key") else None) if m[0] not in seen]
    if ment:
        L += ["### Mentioned in", ""] + ["- [[%s|%s]]" % (p, common.link_text(str(t))) for p, t in ment] + [""]
    return "\n".join(L)
