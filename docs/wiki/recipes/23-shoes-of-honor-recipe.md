---
title: "Shoes of Honor recipe"
type: "recipe"
id: 23
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 23", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Odin crafts gear; Courage/Rise are craft-only at Odin) + client via [[gameplay/consumables]] §4 (Training Camp Odin's craft list 6 is a copy of Item_Make category 0); category 0 → fortress Odin 213 is inferred"]
result: {"item": 419, "count": 1}
materials:
  - {"item": 700, "count": 13}
gold: 10000
success_rate: 100
category: 0
filter_mask: 16777224
superior: {"chance": 5, "item": 491}
level: 1
raw: {"c28": 195}
npc: [213]
---
<!-- generated:start -->
<!-- generated-keys: title=4a4f2a type=61613a id=d435a6 sources=004afc result=e1a100 materials=abbb5c gold=8a12a3 success_rate=310b86 category=b6589f filter_mask=96c62c superior=e42cf1 level=356a19 raw=0d675d -->
|  |  |
|---|---|
|  | ![](../assets/items/419.png) |
| **Recipe id** | `23` (`Item_Make`) |
| **Makes** | [[wiki/items/419-shoes-of-honor\|Shoes of Honor]] × 1 |
| **Gold** | 10,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Superior result** | 5 % → [[wiki/items/491-shoes-of-honor\|Shoes of Honor]] (*guess*: c19@40 / @44) |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 0 / `0x1000008` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 13 |  |

Unknown columns: `c28` = 195 (`c28` is the decoder's `gold@28`, which is not the gold cost).

Other recipes for the same item: [[wiki/recipes/2023-shoes-of-honor-recipe|recipe 2023]]

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
