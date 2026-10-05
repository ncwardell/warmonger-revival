---
title: "Random box 44 (Box of the Participant II?)"
type: "box"
id: 44
status: "stub"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 44", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)"]
contents:
  - {"slot": 0, "item": 951, "count": 1, "p": 1}
  - {"slot": 1, "item": 881, "count": 2, "p": 0}
  - {"slot": 2, "item": 1010, "count": 1, "p": 1}
  - {"slot": 3, "item": 881, "count": 2, "p": 0}
  - {"slot": 4, "item": 881, "count": 2, "p": 0}
  - {"slot": 5, "item": 1043, "count": 1, "p": 0}
  - {"slot": 6, "item": 1043, "count": 1, "p": 0}
  - {"slot": 7, "item": 1043, "count": 1, "p": 0}
  - {"slot": 8, "item": 1043, "count": 1, "p": 0}
  - {"slot": 9, "item": 1043, "count": 1, "p": 0}
value_4c: 10000
opened_by_guess: 1044
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=418e57 type=24f03d id=98fbc4 sources=f053a3 contents=32953a value_4c=8a12a3 opened_by_guess=f67392 kind=364c90 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/1044.png) |
| **RandomBox id** | `44` |
| **Opened by** | [[wiki/items/1044-box-of-the-participant-ii\|Box of the Participant II]] (*guess*, not confirmed) |
| **Value @4c** | 10,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 |  | item 951 (not in `Item_Base`) | 1 | 1 |
| 1 | ![](wiki/assets/items/881.png) | [[wiki/items/881-potion-of-brisk-b\|Potion of Brisk (B)]] | 2 |  |
| 2 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 | 1 |
| 3 | ![](wiki/assets/items/881.png) | [[wiki/items/881-potion-of-brisk-b\|Potion of Brisk (B)]] | 2 |  |
| 4 | ![](wiki/assets/items/881.png) | [[wiki/items/881-potion-of-brisk-b\|Potion of Brisk (B)]] | 2 |  |
| 5 | ![](wiki/assets/items/1043.png) | [[wiki/items/1043-box-of-the-participant-iii\|Box of the Participant III]] | 1 |  |
| 6 | ![](wiki/assets/items/1043.png) | [[wiki/items/1043-box-of-the-participant-iii\|Box of the Participant III]] | 1 |  |
| 7 | ![](wiki/assets/items/1043.png) | [[wiki/items/1043-box-of-the-participant-iii\|Box of the Participant III]] | 1 |  |
| 8 | ![](wiki/assets/items/1043.png) | [[wiki/items/1043-box-of-the-participant-iii\|Box of the Participant III]] | 1 |  |
| 9 | ![](wiki/assets/items/1043.png) | [[wiki/items/1043-box-of-the-participant-iii\|Box of the Participant III]] | 1 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/potion-regen|Potion regeneration ticks]], section *What the live server paid (S grade)*
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
