---
title: "Random box 24 (Phase of Gaia Box?)"
type: "box"
id: 24
status: "stub"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 24", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)"]
contents:
  - {"slot": 0, "item": 602, "count": 50, "p": 0}
  - {"slot": 1, "item": 612, "count": 50, "p": 0}
  - {"slot": 2, "item": 701, "count": 20, "p": 0}
  - {"slot": 3, "item": 701, "count": 30, "p": 0}
  - {"slot": 4, "item": 701, "count": 30, "p": 0}
  - {"slot": 5, "item": 701, "count": 40, "p": 0}
  - {"slot": 6, "item": 602, "count": 100, "p": 0}
  - {"slot": 7, "item": 612, "count": 100, "p": 0}
  - {"slot": 8, "item": 602, "count": 100, "p": 0}
  - {"slot": 9, "item": 612, "count": 100, "p": 0}
value_4c: 100000
opened_by_guess: 1027
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=74cd4f type=24f03d id=4d134b sources=da9e8e contents=985ef0 value_4c=409e95 opened_by_guess=e194ee kind=364c90 -->
|  |  |
|---|---|
|  | ![](../assets/items/1027.png) |
| **RandomBox id** | `24` |
| **Opened by** | [[wiki/items/1027-phase-of-gaia-box\|Phase of Gaia Box]] (*guess*, not confirmed) |
| **Value @4c** | 100,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 50 |  |
| 1 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 50 |  |
| 2 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 20 |  |
| 3 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 30 |  |
| 4 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 30 |  |
| 5 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 40 |  |
| 6 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 100 |  |
| 7 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 100 |  |
| 8 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 100 |  |
| 9 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 100 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/lords-of-the-land|Lords of the Land buff and quest]], section *3. Stack level → buff → box (`WinAffect`)*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Added from the source hunt (see ((gameplay/sources/Sources and gaps)))*
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
