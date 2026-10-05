"""Buffs: one page per Skill_Buff row (buffs, debuffs, statuses, transforms).

Client sources (data/tables/*.tsv, see docs/spec/data-tables.md and
docs/spec/combat.md section 2.6):
  Skill_Buff   name key (the name is often a whole sentence), is_buff?,
               stack_type?, group? (+0x44 category), duration (the column is
               named duration_ms but counts 200 ms ticks: 1500 = the tooltips'
               "5 minutes", docs/gameplay/consumables.md; 2100000000 =
               permanent), 3 effects {code, value}, icon
  Skill_Base   effect slots of the types in skills.BUFF_TYPES apply a buff;
               requirement type 1 needs one
  Item_Base    option 301 = buff applied when the item is used
  WinAffect    war-winner reward buff
  Policy       buff_or_skill (nation policies; server-only table)

Effect codes are the ItemOption stat codes (1 Attack, 101 Attack %, ...) plus
special codes the client handles itself (combat.md 2.6: 0x1b8 mana shield,
0x167 transform, 0xe7/0xe8 levels, 0x192-0x194/0x19b basic-attack override,
0x3e9). Most codes from 200 up are not decoded.
"""
from . import common, skills
from .common import Page, fmt_num, table_md

TYPE = "buffs"
KIND = "buff"
LABEL = "Buff"
DESCRIPTION = ("Every buff and debuff in the client's `Skill_Buff` table: what skills, items, "
               "war rewards and policies apply, with duration and stat effects. Many names are "
               "the in-game buff tooltip.")
REQUIRED = ["duration", "effects"]
UNION_KEYS = ["applied_by"]
PERMANENT = 2100000000
TICK = 0.2          # seconds per Skill_Buff duration unit (docs/gameplay/consumables.md)
DURATION_SOURCE = "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"
SPECIAL = {440: "mana shield (damage hits MP first)", 359: "transform", 231: "level? (char+0x657)",
           232: "level? (char+0x658)", 402: "basic attack override", 403: "basic attack override",
           404: "basic attack override", 411: "basic attack override", 1001: "special 0x3e9"}


def code_text(ix, code):
    if code in SPECIAL:
        return SPECIAL[code]
    opt = ix.options.get(code)
    return (opt.get("name") or "").strip() if opt is not None else "code %d (unknown)" % code


class Index:
    def __init__(self, ctx):
        t = ctx.table
        self.options = {r.int("code"): r for r in t("ItemOption")}
        self.skill_ids = t("Skill_Base").by()
        self.by_skill, self.req_skill = {}, {}
        for r in t("Skill_Base"):
            for n in range(1, 5):
                ty, v = r.int("eff%d_type" % n), r.int("eff%d_value" % n)
                if ty in skills.BUFF_TYPES:
                    self.by_skill.setdefault(v, []).append((r.int("id"), n, ty, r.int("eff%d_rate" % n)))
            for n in (1, 2):
                if r.int("req%d_type" % n) == 1:
                    self.req_skill.setdefault(r.int("req%d_a" % n), []).append(r.int("id"))
        self.items = {}
        for r in t("Item_Base"):
            for slot in range(1, 11):
                if r.int("opt%d_type" % slot) == 301:
                    self.items.setdefault(r.int("opt%d_value" % slot), []).append(r.int("id"))
        self.war = {}
        for r in t("WinAffect"):
            if r.int("buff"):
                self.war.setdefault(r.int("buff"), []).append(r)
        self.policy = {}
        try:
            for r in t("Policy"):
                self.policy.setdefault(r.int("buff_or_skill"), []).append(r)
        except OSError:
            pass


def index(ctx):
    if getattr(ctx, "buffs_index", None) is None:
        ctx.buffs_index = Index(ctx)
    return ctx.buffs_index


def mentions(ctx):
    if getattr(ctx, "_buff_mentions", None) is None:
        ctx._buff_mentions = skills.find_mentions(ctx, TYPE, "Skill_Buff", id_column="buff")
    return ctx._buff_mentions


def build(ctx):
    ix = index(ctx)
    rows = {}
    for r in ctx.table("Skill_Buff"):
        rows.setdefault(r.int("id"), []).append(r)
    for id_, same in rows.items():
        r = same[0]          # first row wins, as in Table.by(); later ones are listed
        f = {}
        f["name_key"] = r.str("name_key")
        dur = r.int("duration_ms")
        if dur == PERMANENT:
            f["duration"] = {"ticks": dur, "permanent": True}
        elif dur:
            f["duration"] = {"ticks": dur, "seconds": round(dur * TICK, 3), "permanent": False}
        else:
            f["duration"] = None
        f["is_buff"] = r.int("is_buff")
        f["stack_type"] = r.int("stack_type")
        f["group"] = r.int("group")
        effects = []
        for n in range(1, 4):
            code = r.int("eff%d_type" % n)
            if code:
                effects.append({"code": code, "stat": code_text(ix, code), "value": r.int("eff%d_value" % n)})
        f["effects"] = effects
        f["icon"] = {"file": r.str("icon_file"), "index": r.int("icon_idx")} if r.str("icon_file") else None
        applied = []
        for sid, slot, ty, rate in ix.by_skill.get(id_, []):
            applied.append({"skill": sid, "slot": slot, "type": ty, "rate": rate})
        for item in ix.items.get(id_, []):
            applied.append({"item": item})
        for w in ix.war.get(id_, []):
            applied.append({"war_reward": w.int("id")})
        f["applied_by"] = applied
        if ix.req_skill.get(id_):
            f["required_by"] = ix.req_skill[id_]
        if len(same) > 1:
            f["duplicate_rows"] = [{"duration_ticks": o.int("duration_ms"), "group": o.int("group"),
                                    "effects": [[o.int("eff%d_type" % n), o.int("eff%d_value" % n)]
                                                for n in range(1, 4) if o.int("eff%d_type" % n)],
                                    "icon": [o.get("icon_file") or "", o.int("icon_idx")]} for o in same[1:]]
        sources = ["client: Skill_Buff.cdb id %d" % id_]
        if dur and dur != PERMANENT:
            sources.append(DURATION_SOURCE)
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body)


def body(ctx, page):
    ix = index(ctx)
    fm, id_ = page.fm, page.id
    L, info = [], []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Buff id", "`%d`" % id_))
    d = fm.get("duration")
    if isinstance(d, dict):
        if d.get("permanent"):
            info.append(("Duration", "permanent"))
        else:
            secs = d.get("seconds", (d.get("ticks") or 0) * TICK)
            m, sec = divmod(secs, 60)
            shown = ("%d min %s s" % (m, fmt_num(round(sec, 1))) if sec else "%d min" % m) if m else "%s s" % fmt_num(round(secs, 1))
            info.append(("Duration", "%s (%s ticks of 200 ms; unit from [[gameplay/consumables]])" % (shown, fmt_num(d.get("ticks", 0)))))
    info.append(("Buff / debuff", "flag %s (is_buff?, guessed column)" % fm.get("is_buff")))
    info.append(("Stack type", "%s (guessed column)" % fm.get("stack_type")))
    if fm.get("group"):
        info.append(("Group", "%s (+0x44 category; buffs of one group replace each other?)" % fm["group"]))
    if isinstance(fm.get("icon"), dict):
        ic = fm["icon"]
        info.append(("Icon", "`ui/icons/%s` cell %s" % (ic.get("file"), ic.get("index"))))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    name = ctx.s("SkillBuff_%d" % id_) or ctx.s(fm.get("name_key"))
    if name:
        L += ["### Tooltip", "", common.quote(name)]

    eff = [e for e in (fm.get("effects") or []) if isinstance(e, dict)]
    if eff:
        rows = []
        for e in eff:
            v = e.get("value")
            shown = fmt_num(v) if isinstance(v, (int, float)) else str(v)
            if e.get("code") in (402, 403, 404, 411) and v in ix.skill_ids:
                shown += " (%s)" % ctx.link("skills", v)
            rows.append((e.get("code"), e.get("stat") or code_text(ix, e.get("code", 0)), shown))
        L += ["### Effects", "", "Effect codes read as `ItemOption` stat codes (*assumed*: a few rows "
              "disagree with their own tooltip, e.g. buff 1 \"EXP +15%\" uses code 41).", "",
              table_md(["code", "effect", "value"], rows)]
    else:
        L += ["### Effects", "", "No effect codes in the client: what this buff does (a stun, a "
              "mark, a status) is server-side. Add `effects:` by hand when known.", ""]

    dup = fm.get("duplicate_rows")
    if isinstance(dup, list) and dup:
        L += ["> [!warning] `Skill_Buff` has %d more row(s) with this id (shown in `duplicate_rows`). "
              "This page uses the first; which one the game used is unknown." % len(dup), ""]
    by = []
    for a in fm.get("applied_by") or []:
        if not isinstance(a, dict):
            continue
        if "skill" in a:
            by.append("Skill %s, effect slot %s (type %s, rate %s%%)" % (
                ctx.link("skills", a["skill"]), a.get("slot"), a.get("type"), a.get("rate")))
        elif "item" in a:
            by.append("Using %s (Item_Base option 301)" % ctx.link("items", a["item"]))
        elif "war_reward" in a:
            w = ctx.table("WinAffect").get(a["war_reward"])
            by.append("War-winner reward, WinAffect row %s%s" % (
                a["war_reward"], " (%s minutes?)" % w.get("minutes") if w is not None and w.int("minutes") else ""))
        else:
            by.append("%s (hand-entered)" % ", ".join("%s %s" % kv for kv in a.items()))
    for p in ix.policy.get(id_, []):
        by.append("Nation policy %s `%s` (Policy.cdb, server-only; buff_or_skill)" % (
            p.int("id"), ctx.s(p.get("name_key")) or p.get("name_key")))
    if by:
        L += ["### Applied by", ""] + ["- " + b for b in by] + [""]
    req = fm.get("required_by")
    if isinstance(req, list) and req:
        L += ["### Needed by", "", "Skills whose requirement slot (type 1) names this buff: " +
              ", ".join(ctx.link("skills", s) for s in req if isinstance(s, int)), ""]

    code = skills.code_mentions(ctx, id_, "buff")
    if code:
        L += ["### Current server", ""] + ["- `%s` line %d: `%s`" % (f, n, l[:140].replace("`", "'"))
                                            for f, n, l in code] + [""]
    ment = mentions(ctx).get(id_, [])
    if ment:
        L += ["### Mentioned in", ""] + skills.mention_lines(ment) + [""]
    return "\n".join(L)
