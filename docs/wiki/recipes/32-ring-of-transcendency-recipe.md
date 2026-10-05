---
title: "Ring of Transcendency recipe"
type: "recipe"
id: 32
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 32", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Odin crafts gear; Courage/Rise are craft-only at Odin) + client via [[gameplay/consumables]] §4 (Training Camp Odin's craft list 6 is a copy of Item_Make category 0); category 0 → fortress Odin 213 is inferred"]
result: {"item": 428, "count": 1}
materials:
  - {"item": 700, "count": 11}
gold: 10000
success_rate: 100
category: 0
filter_mask: 16777344
superior: {"chance": 5, "item": 460}
level: 1
raw: {"c28": 165}
npc: [213]
---
<!-- generated:start -->
<!-- generated-keys: title=0496ea type=61613a id=cb4e52 sources=54e695 result=d530f2 materials=1925b2 gold=8a12a3 success_rate=310b86 category=b6589f filter_mask=16666f superior=5b3487 level=356a19 raw=2b2a6b -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/428.png) |
| **Recipe id** | `32` (`Item_Make`) |
| **Makes** | [[wiki/items/428-ring-of-transcendency\|Ring of Transcendency]] × 1 |
| **Gold** | 10,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Superior result** | 5 % → [[wiki/items/460-ring-of-transcendency\|Ring of Transcendency]] (*guess*: c19@40 / @44) |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 0 / `0x1000080` |
| **Crafted at** | [[wiki/npcs/213-odin\|Odin]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 11 |  |

Unknown columns: `c28` = 165 (`c28` is the decoder's `gold@28`, which is not the gold cost).

Other recipes for the same item: [[wiki/recipes/2032-ring-of-transcendency-recipe|recipe 2032]]

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.
<!-- generated:end -->

## Notes

Crafted at **Odin** (Blue Union, unit 213) in the fortress: the guides name Odin as the gear crafter ([[gameplay/items-and-crafting|Items and crafting]] §3). Normal gear costs 10–30 Blue Crystals per piece (*guide*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

Sockets (1–3) are rolled when the item is created and never added later ([[gameplay/items-and-crafting|Items and crafting]] §2, *guide*). From WM 0726 crafted gear has a small chance to come out **superior**; from WM 0824 yellow jewels can stand in for missing materials on normal gear ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

## Sources

- guide: [[gameplay/items-and-crafting]] §3 (Odin crafts gear; Courage/Rise are craft-only at Odin) + client via [[gameplay/consumables]] §4 (Training Camp Odin's craft list 6 is a copy of Item_Make category 0); category 0 → fortress Odin 213 is inferred

## Open questions

Category 0 → Odin is inferred from the Training Camp copy (list 6) and the guides; the client does not link a craft list to the fortress Odin directly. WM 0824 also lets gear be crafted at the nation castle; which castle NPC offers it is not recorded ([[gameplay/events-and-schedules|Events and schedules]] §5).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
