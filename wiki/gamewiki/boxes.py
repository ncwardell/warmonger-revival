"""Random boxes: one page per RandomBox row (page id = RandomBox id).

Client source: RandomBox.cdb, 10 x {item, count, p} + one value @4c the
decoder calls gold? (0 .. 500,000). There is no odds column and no column in
Item_Base that points a box item (kind 43) at a RandomBox row, so which item
opens which row is a *guess* from names and contents (GUESS below), kept out
of the required ``opened_by`` field until someone confirms it.

Front matter:
  contents        [{slot, item, count, p}] in table order          (required)
  odds            per-slot odds -- not in the client                (required)
  opened_by       Item_Base id of the box item that opens this row  (required)
  opened_by_guess the guessed box item (see GUESS)
  value_4c        the unknown @4c value (gold? grows with box tier)
"""
import json

from . import _econ
from .common import Page, fmt_num, table_md

TYPE = "boxes"
KIND = "random_box"
LABEL = "Random box"
PLURAL = "Random boxes"
DESCRIPTION = ("Every row of the client's `RandomBox` table: the ten possible results of a box item. "
               "Odds are not in the client, and which box item opens which row is not either "
               "(the pages give a guess).")
REQUIRED = ["contents", "odds", "opened_by"]

# RandomBox row -> box item, *guess*:
#   20-25 Gaia / Lords of the Land boxes 1023-1028 (crystals; events-and-schedules,
#         WM 0426: the Lords of the Land reward became blue/yellow crystals by buff level)
#   30-35 Box of the Victorious VI..I 1030-1035, 40-45 Box of the Participant VI..I
#   46-50 [Bronze]..[Diamond] Medal Reward Box 1051-1055 (each holds the next medal)
#   51    Halloween reward box 1056 (holds the Jack transform scroll 763)
#   81-83 Random box of dye 1057-1059
GUESS = {}
GUESS.update({20 + i: 1023 + i for i in range(6)})
GUESS.update({30 + i: 1030 + i for i in range(6)})
GUESS.update({40 + i: 1040 + i for i in range(6)})
GUESS.update({46 + i: 1051 + i for i in range(5)})
GUESS.update({51: 1056, 81: 1057, 82: 1058, 83: 1059})


def name(ctx, id_):
    g = GUESS.get(id_)
    n = ctx.name("items", g) if g else None
    return "Random box %d (%s?)" % (id_, n) if n else "Random box %d" % id_


def build(ctx):
    for r in ctx.table("RandomBox"):
        bid = r.int("id")
        contents = []
        for slot in range(1, 11):
            code = r.int("item%d_code" % slot)
            if code:
                contents.append({"slot": slot - 1, "item": code, "count": r.int("item%d_count" % slot),
                                 "p": r.int("item%d_p" % slot)})
        f = {"contents": contents, "value_4c": r.int("gold")}
        if bid in GUESS:
            f["opened_by_guess"] = GUESS[bid]
        sources = ["client: RandomBox.cdb id %d" % bid,
                   "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)"]
        yield Page(TYPE, bid, ctx.title(TYPE, bid), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, bid = page.fm, page.id
    guess = fm.get("opened_by_guess")
    opened = fm.get("opened_by")
    info = []
    shown = opened or guess
    if isinstance(shown, int) and ctx.image("items", shown):
        info.append(("", "![](%s)" % ctx.image("items", shown)))
    info.append(("RandomBox id", "`%d`" % bid))
    if opened:
        info.append(("Opened by", _econ.item_link(ctx, opened)))
    elif guess:
        info.append(("Opened by", "%s (*guess*, not confirmed)" % _econ.item_link(ctx, guess)))
    else:
        info.append(("Opened by", "unknown"))
    info.append(("Value @4c", "%s (unknown; decoder guesses gold. The Lord of the Land reward box "
                              "cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules|server "
                              "rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*)"
                 % fmt_num(fm.get("value_4c") or 0)))
    odds = fm.get("odds")
    info.append(("Odds", (odds if isinstance(odds, str) else json.dumps(odds, ensure_ascii=False))
                 if odds else "unknown (server side)"))
    L = [table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info])]
    rows = []
    for c in fm.get("contents") or []:
        if isinstance(c, dict):
            it = c.get("item", 0)
            rows.append((c.get("slot"), _econ.item_icon(ctx, it), _econ.item_link(ctx, it),
                         fmt_num(c.get("count") or 0), c.get("p") or ""))
    L += ["### Contents", "",
          "One of these is given when the box is used (contract `use_item`; *guess*: one roll per "
          "use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).", "",
          table_md(["slot", "", "item", "count", "p"], rows)]
    if guess:
        L += ["### Why this box item", "",
              "No client column links a box item to a RandomBox row. The guess pairs rows and box items "
              "by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the "
              "Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the "
              "Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set "
              "`opened_by:` once a source confirms it.", ""]
        nm = ctx.name("items", guess)
        refs = _econ.gameplay_refs(r"\b%d\b|%s" % (guess, _re_name(nm))) if nm else []
        if refs:
            L += ["### Seen in", ""] + _econ.refs_md(refs) + [""]
    return "\n".join(L)


def _re_name(n):
    import re
    words = re.findall(r"\w+", n or "")
    return r"\W+".join(re.escape(w) for w in words) if len(words) >= 2 else r"(?!x)x"
