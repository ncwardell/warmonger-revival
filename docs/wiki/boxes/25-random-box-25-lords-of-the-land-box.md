---
title: "Random box 25 (Lords of the Land Box?)"
type: "box"
id: 25
status: "stub"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 25", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)"]
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

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
