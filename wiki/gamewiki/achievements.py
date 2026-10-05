"""Achievements: one page per Achievement_Base row (page id = achievement id 0..39).

Client sources:
  Achievement_Base  name/explain keys, category@01 (GUI_CharAchieve_Category_N:
                    Normal, War, Battle, Repute, Creation, Explore), goal1..10 (the
                    counter value for each of the 10 grades), reward1..10, c25@64
                    (order inside the category)
  StringAll         AchievementName_N, AchievementExplainText_N ('%s' = the goal)
Contract (contract/quests.yaml 0x485-0x489): the server keeps 40 entries
{PreStep, RewardStep, Value, Time}; when a counter crosses goal[PreStep] the
grade is reached (0x489 toast "Achievements.%02d"); claiming (0x487) adds
reward[RewardStep] Yellow Jewels. What each counter counts is server logic.

Titles: the client has no player titles to link to. Its TitleName_N strings
are NPC names (UnitDB name_key: TitleName_1 = Freya ...), and the u16 "title"
in the match-result packet is the Lords-of-the-Land level (char+0x297,
WinAffect). Achievements pay Yellow Jewels only.

Evidence: docs/gameplay/progression-and-economy §7 (categories and point
totals, jewels per achievement), lords-of-the-land (row 36).

Front matter:
  goals     [10 counter thresholds]                       (required, client)
  rewards   [10 Yellow Jewel amounts]                     (required, client)
  tracks    what the counter counts (server event)        (required)
  category, category_name, order, explain
"""
import re

from .common import Page, clean_name, fmt_num, table_md

TYPE = "achievements"
KIND = "achievement"
LABEL = "Achievement"
DESCRIPTION = ("Every achievement in the client's `Achievement_Base` table: ten grades per "
               "achievement, each with a goal and a Yellow Jewel reward. What each counter counts is "
               "server logic (`tracks`). The client has no player titles: achievements pay jewels only.")
REQUIRED = ["goals", "rewards", "tracks"]
SRC_CONTRACT = "contract: quests.yaml 0x485–0x489 (achievement table, claim adds reward[step] Yellow Jewels)"
SRC_DOCS = "docs: [[gameplay/progression-and-economy]] §7 (categories, point totals, jewel rewards)"
# Counters with an obvious server event, from the explain text (*inferred*).
FAME_RANKS = {22, 23}


def build(ctx):
    for r in ctx.table("Achievement_Base"):
        id_ = r.int("id")
        cat = r.int("category")
        explain = clean_name(ctx.s(r.get("explain_key")) or "")
        f = {"name_key": r.str("name_key"), "category": cat,
             "category_name": ctx.s("GUI_CharAchieve_Category_%d" % cat),
             "order": r.int("c25"), "explain": explain,
             "goals": [r.int("goal%d" % n) for n in range(1, 11)],
             "rewards": [r.int("reward%d" % n) for n in range(1, 11)],
             "reward_currency": "Yellow Jewel"}
        sources = ["client: Achievement_Base.cdb id %d" % id_, SRC_CONTRACT, SRC_DOCS]
        f = {k: v for k, v in f.items() if v is not None}
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, id_ = page.fm, page.id
    goals = fm.get("goals") or []
    rewards = fm.get("rewards") or []
    info = [("Achievement id", "`%d` (index in the 40-entry table)" % id_),
            ("Category", "%s (%s)" % (fm.get("category_name") or "?", fm.get("category"))),
            ("Order in category", fm.get("order")),
            ("Total reward", "%s Yellow Jewels over 10 grades" % fmt_num(sum(x for x in rewards if isinstance(x, int))))]
    if fm.get("tracks"):
        info.append(("Tracks", fm["tracks"]))
    L = [table_md(["", ""], [("**%s**" % k, v) for k, v in info])]
    ex = fm.get("explain") or ""
    rows = []
    for n in range(max(len(goals), len(rewards))):
        g = goals[n] if n < len(goals) else None
        text = re.sub(r"%s", fmt_num(g), ex) if isinstance(g, int) and "%s" in ex else ex
        rows.append((n + 1, fmt_num(g) if isinstance(g, int) else "", rewards[n] if n < len(rewards) else "", text))
    L += ["### Grades", "",
          "Reaching a goal unlocks the grade; claiming it pays the reward in Yellow Jewels "
          "(`contract/quests.yaml` 0x487).", "",
          table_md(["grade", "goal", "reward", "text"], rows)]
    L += ["### Server", "",
          "What raises this counter is not in the client (`tracks`, required). The explain text above "
          "is the best hint.", ""]
    rel = []
    if id_ in FAME_RANKS:
        rel.append("Fame thresholds of the ranks: [[wiki/fame-ranks/index|Fame ranks]].")
    if id_ == 36:
        rel.append("[[gameplay/lords-of-the-land|Lords of the Land]] (this row's thresholds are quoted there).")
    if fm.get("category_name"):
        same = sorted(p for p, f in ctx.pages(TYPE).items() if f.get("category") == fm.get("category") and p != id_)
        if same:
            rel.append("Same category: %s." % ", ".join(ctx.link(TYPE, p) for p in same))
    if rel:
        L += ["### Related", ""] + ["- " + x for x in rel] + [""]
    return "\n".join(L)
