---
title: "Komodo's Ring recipe"
type: "recipe"
id: 332
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 332", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Odin crafts gear; Courage/Rise are craft-only at Odin) + client via [[gameplay/consumables]] §4 (Training Camp Odin's craft list 6 is a copy of Item_Make category 0); category 0 → fortress Odin 213 is inferred"]
result: {"item": 3038, "count": 1}
materials:
  - {"item": 2704, "count": 1}
  - {"item": 1932, "count": 1}
gold: 100000
success_rate: 60
category: 0
filter_mask: 33554560
level: 10
npc: [213]
---
<!-- generated:start -->
<!-- generated-keys: title=658851 type=61613a id=ef2afd sources=9a7b97 result=75e730 materials=54fac4 gold=409e95 success_rate=e6c3dd category=b6589f filter_mask=e42ab3 level=b1d578 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/3038.png) |
| **Recipe id** | `332` (`Item_Make`) |
| **Makes** | [[wiki/items/3038-komodo-s-ring\|Komodo's Ring]] × 1 |
| **Gold** | 100,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 60 % |
| **Level (c24, *guess*)** | 10 |
| **Category / filter** | 0 / `0x2000080` |
| **Crafted at** | [[wiki/npcs/213-odin\|Odin]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/2704.png) | [[wiki/items/2704-horn-of-komodo\|Horn of Komodo]] | 1 |  |
| ![](wiki/assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 1 |  |

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.
<!-- generated:end -->

## Notes

Crafted at **Odin** (Blue Union, unit 213) in the fortress: the guides name Odin as the gear crafter ([[gameplay/items-and-crafting|Items and crafting]] §3). Normal gear costs 10–30 Blue Crystals per piece (*guide*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

Sockets (1–3) are rolled when the item is created and never added later ([[gameplay/items-and-crafting|Items and crafting]] §2, *guide*). From WM 0726 crafted gear has a small chance to come out **superior**; from WM 0824 yellow jewels can stand in for missing materials on normal gear ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

Success 60 % in the client. The craft window warns "There is a chance to fail in creating this item" for superior items ([[gameplay/items-and-crafting|Items and crafting]] §3, *image*).

## Sources

- guide: [[gameplay/items-and-crafting]] §3 (Odin crafts gear; Courage/Rise are craft-only at Odin) + client via [[gameplay/consumables]] §4 (Training Camp Odin's craft list 6 is a copy of Item_Make category 0); category 0 → fortress Odin 213 is inferred

## Open questions

Category 0 → Odin is inferred from the Training Camp copy (list 6) and the guides; the client does not link a craft list to the fortress Odin directly. WM 0824 also lets gear be crafted at the nation castle; which castle NPC offers it is not recorded ([[gameplay/events-and-schedules|Events and schedules]] §5).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
