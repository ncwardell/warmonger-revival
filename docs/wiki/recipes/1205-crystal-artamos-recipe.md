---
title: "Crystal : Artamos recipe"
type: "recipe"
id: 1205
status: "partial"
missing: ["npc"]
sources: ["client: Item_Make.cdb id 1205", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "notes: [[gameplay/events-and-schedules]] §9 (WM 1107: Innocence Crystal = 5 Innocence Pieces + Red fragments; durability 1,500, −5/s)"]
result: {"item": 8504, "count": 1}
materials:
  - {"item": 9004, "count": 5}
  - {"item": 613, "count": 50}
gold: 50000
success_rate: 100
category: 3
filter_mask: 1
---
<!-- generated:start -->
<!-- generated-keys: title=914053 type=61613a id=b74e9c sources=18904a result=820869 materials=361ea6 gold=c2d4c5 success_rate=310b86 category=77de68 filter_mask=356a19 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/8504.png) |
| **Recipe id** | `1205` (`Item_Make`) |
| **Makes** | [[wiki/items/8504-crystal-artamos\|Crystal : Artamos]] × 1 |
| **Gold** | 50,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Category / filter** | 3 / `0x1` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/9004.png) | [[wiki/items/9004-piece-artamos\|Piece : Artamos]] | 5 |  |
| ![](wiki/assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 50 |  |

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.
<!-- generated:end -->

## Notes

The WM 1107 patch notes describe the Innocence Crystal recipe as **5 Innocence Pieces + Red fragments**, which matches this row (5 × Piece + 50 Red Passion Fragments [D]) ([[gameplay/events-and-schedules|Events and schedules]] §9, *notes + client*). The crystal has no level limit and 1,500 durability, losing 5 per second while transformed (same source).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- notes: [[gameplay/events-and-schedules]] §9 (WM 1107: Innocence Crystal = 5 Innocence Pieces + Red fragments; durability 1,500, −5/s)

## Open questions

Which NPC offers Item_Make category 3 (Innocence crystals and heroes) is not in any source; the guides name only Farrell, Odin, Alan, Owen and Paraman ([[gameplay/items-and-crafting|Items and crafting]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
