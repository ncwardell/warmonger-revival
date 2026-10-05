---
title: "Random box 25 (Lords of the Land Box?)"
type: "box"
id: 25
status: "partial"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 25", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)", "guide + client: [[gameplay/lords-of-the-land]] §3 (stack level 1–6 → box items 1023–1028; contents not known) + notes: [[gameplay/events-and-schedules]] §2 (WM 0426 reward became Blue/Yellow crystals by buff level; opening cost 300,000 → 200,000 gold in WM 0920)"]
contents:
  - {"slot": 0, "item": 602, "count": 100, "p": 0}
  - {"slot": 1, "item": 612, "count": 100, "p": 0}
  - {"slot": 2, "item": 701, "count": 30, "p": 0}
  - {"slot": 3, "item": 701, "count": 40, "p": 0}
  - {"slot": 4, "item": 701, "count": 40, "p": 0}
  - {"slot": 5, "item": 701, "count": 60, "p": 0}
  - {"slot": 6, "item": 602, "count": 150, "p": 0}
  - {"slot": 7, "item": 612, "count": 150, "p": 0}
  - {"slot": 8, "item": 602, "count": 150, "p": 0}
  - {"slot": 9, "item": 612, "count": 150, "p": 0}
value_4c: 150000
opened_by_guess: 1028
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=4ef1ff type=24f03d id=f6e112 sources=00053e contents=c8e29c value_4c=22ee31 opened_by_guess=d9935e kind=364c90 -->
|  |  |
|---|---|
|  | ![](../assets/items/1028.png) |
| **RandomBox id** | `25` |
| **Opened by** | [[wiki/items/1028-lords-of-the-land-box\|Lords of the Land Box]] (*guess*, not confirmed) |
| **Value @4c** | 150,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 100 |  |
| 1 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 100 |  |
| 2 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 30 |  |
| 3 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 40 |  |
| 4 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 40 |  |
| 5 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 60 |  |
| 6 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 150 |  |
| 7 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 150 |  |
| 8 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 150 |  |
| 9 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 150 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/lords-of-the-land|Lords of the Land buff and quest]], section *3. Stack level → buff → box (`WinAffect`)*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Added from the Crush Online forum (see ((gameplay/crush-mechanics)), ((gameplay/crush-patch-notes)))*
- Seen in [[gameplay/sources|Sources and gaps]], section *9. What is still missing*
<!-- generated:end -->

## Notes

The Lords of the Land war buff pays one box per stack level: level 6 → box item 1028 ([[gameplay/lords-of-the-land|Lords of the Land]] §3, *client* `WinAffect`). Kelsey's quests 117/763/764/765 also reward boxes 1024–1027 ([[gameplay/lords-of-the-land|Lords of the Land]] §4). From WM 0426 the box reward became Blue or Yellow crystals depending on the buff level, which fits this row's passion and crystal contents; from WM 0920 opening the box costs **200,000 gold** (was 300,000) ([[gameplay/events-and-schedules|Events and schedules]] §2, *notes*).

## Behaviour

Claiming a box resets the buff and the compensation row to zero ([[gameplay/lords-of-the-land|Lords of the Land]] §1, *image*). Only the winning team got the buff and the box in Crush Online (Nov 2016), and the box contents were changed on 22 Dec 2016 (image lost) ([[gameplay/crush-patch-notes|Crush patch notes]], *staff*).

## Sources

- guide + client: [[gameplay/lords-of-the-land]] §3 (stack level 1–6 → box items 1023–1028; contents not known) + notes: [[gameplay/events-and-schedules]] §2 (WM 0426 reward became Blue/Yellow crystals by buff level; opening cost 300,000 → 200,000 gold in WM 0920)

## Open questions

[[gameplay/lords-of-the-land|Lords of the Land]] §3 says no `RandomBox` row lists the box items 1023–1028, so their contents are unknown; this row matching box 1028 stays a guess. The opening cost (200,000 / 300,000 gold) does not match this row's `value_4c` (150,000).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
