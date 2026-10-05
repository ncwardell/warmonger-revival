"""Fame ranks: one page per FameRank row (page id = rank 0..19).

Client sources:
  FameRank     rank, name key (FameRank_N), UI element key
  Level_Table  fame_threshold@0c of rows 0..9: FUN_005cde32(fame) counts the
               rows whose threshold <= fame, so rank r (1..10) starts at row
               r-1's threshold (600, 1,860 ... 15,863,773; x3.1 per step). Rows
               10+ hold 0: ranks 11-19 are not reached by fame alone.
Evidence: docs/gameplay/crush-patch-notes (CO staff rank structure: Soldier
600 - 55,410 fame, Veteran 55,411 - 5,117,346, then Officer by individual
ranking 25-73, General 4-25, Imperator 1-3, Marshal fort owners / 20, King one
per nation; WM thresholds are exactly the CO numbers), progression-and-economy
§1 (character sheet shows Rank "Officer [5]"). Contract social.yaml: chat
command channel needs fame rank >= 15 (rec+0x656; >= 200 = GM).

Front matter:
  requirement  {"min_fame": n} or {"ranking": "..."}           (required)
  name_key, min_fame, next_min_fame
"""
from .common import Page, fmt_num, table_md

TYPE = "fame-ranks"
KIND = "fame-rank"
LABEL = "Fame rank"
PLURAL = "Fame ranks"
DESCRIPTION = ("The 20 fame ranks of the client's `FameRank` table, from Novice to King. Ranks 1–10 "
               "start at a personal fame threshold from `Level_Table`; the higher ranks were given by "
               "ranking (Crush Online staff), not by fame alone.")
REQUIRED = ["requirement"]
SRC_CO = ("docs: [[gameplay/crush-patch-notes]] (CO rank structure: Soldier 600–55,410, Veteran "
          "55,411–5,117,346 fame; Officer, General, Imperator, Marshal, King by ranking; WM thresholds "
          "equal the CO numbers)")
# CO staff rank structure (crush-patch-notes): who holds the ranking ranks.
RANKING = {
    "Officer": "individual ranking 25–73 (Crush Online staff)",
    "General": "individual ranking 4–25 (Crush Online staff)",
    "Imperator": "individual ranking 1–3 (Crush Online staff)",
    "Marshal": "20 per nation (8 after a later council); from 15 Dec 2016 every fort owner (Crush Online staff)",
    "King": "one per nation (Crush Online staff)",
}


def name(ctx, id_):
    return ctx.s("FameRank_%d" % id_)


def thresholds(ctx):
    """[min fame of rank 1, rank 2, ...] from Level_Table rows 0.. (non-zero)."""
    out = []
    for r in ctx.table("Level_Table"):
        v = r.float("fame_threshold")
        if not v:
            break
        out.append(int(round(v)))
    return out


def build(ctx):
    th = thresholds(ctx)
    for r in ctx.table("FameRank"):
        rank = r.int("rank")
        nm = ctx.s(r.get("name_key")) or ""
        base = nm.split(" [")[0]
        f = {"name_key": r.str("name_key"), "ui_key": r.str("ui_key")}
        sources = ["client: FameRank.cdb rank %d" % rank]
        if rank == 0:
            f["min_fame"] = 0
        elif rank <= len(th):
            f["min_fame"] = th[rank - 1]
            sources.append("client: Level_Table.cdb row %d fame_threshold@0c (FUN_005cde32)" % (rank - 1))
        if rank < len(th):
            f["next_min_fame"] = th[rank]
        if "min_fame" in f:
            f["requirement"] = {"min_fame": f["min_fame"]}
        if base in RANKING:
            f["ranking"] = RANKING[base]
            sources.append(SRC_CO)
            if "min_fame" not in f:
                f["requirement"] = {"ranking": RANKING[base]}
        elif base in ("Soldier", "Veteran"):
            sources.append(SRC_CO)
        yield Page(TYPE, rank, ctx.title(TYPE, rank), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, rank = page.fm, page.id
    info = [("Rank", "`%d` (rec+0x656)" % rank)]
    if fm.get("min_fame") is not None:
        info.append(("Fame from", fmt_num(fm["min_fame"])))
    if fm.get("next_min_fame"):
        info.append(("Next rank at", fmt_num(fm["next_min_fame"])))
    if fm.get("ranking"):
        info.append(("Held by", fm["ranking"]))
    if rank >= 15:
        info.append(("Chat", "may use the command channel (`#`, fame rank ≥ 15; contract social.yaml)"))
    L = [table_md(["", ""], [("**%s**" % k, v) for k, v in info])]
    L += ["### How ranks work", "",
          "The client counts the `Level_Table` rows whose `fame_threshold` is at most the character's "
          "fame (`FUN_005cde32`). Ten rows have a threshold (600 up to 15,863,773, ×3.1 per step), so "
          "fame alone reaches rank 10 at most. In Crush Online the top ranks (Officer to King) went by "
          "ranking and land; the thresholds are exactly the Crush numbers "
          "([[gameplay/crush-patch-notes|Crush patch notes]]). Rank 10 *Officer [1]* has both a client "
          "threshold and the Crush ranking rule. A 2018 Warmonger character sheet shows *Officer [5]* "
          "at 81,500 fame ([[gameplay/progression-and-economy|Progression]] §1), far below that "
          "threshold, so Warmonger also gave the Officer ranks by ranking (*inferred*).", ""]
    rows = []
    for p, f in sorted(ctx.pages(TYPE).items()):
        cur = "**%s**" % f.get("title") if p == rank else ctx.link(TYPE, p)
        rows.append((p, cur, fmt_num(f["min_fame"]) if isinstance(f.get("min_fame"), int) else "–",
                     f.get("ranking") or ""))
    L += ["### All ranks", "", table_md(["rank", "name", "fame from", "held by"], rows)]
    L += ["Achievements that count fame: %s, %s." % (ctx.link("achievements", 22), ctx.link("achievements", 23)), ""]
    return "\n".join(L)
