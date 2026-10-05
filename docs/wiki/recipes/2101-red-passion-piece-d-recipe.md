---
title: "Red Passion Piece [D] recipe"
type: "recipe"
id: 2101
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 2101", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "client: [[gameplay/consumables]] §4 (category 7 = the Training Camp passion converter, 220 instead of 200 fragments); unit 336 is the Training Camp unit whose UnitDB list is 7 ([[wiki/npcs/336-paraman|unit 336]])"]
result: {"item": 612, "count": 100}
materials:
  - {"item": 611, "count": 220}
gold: 2500
success_rate: 100
category: 7
filter_mask: 2
level: 10
npc: [336]
---
<!-- generated:start -->
<!-- generated-keys: title=f3bf4f type=61613a id=86e1d3 sources=937760 result=5fe2fd materials=abd7b1 gold=a6a084 success_rate=310b86 category=902ba3 filter_mask=da4b92 level=b1d578 -->
|  |  |
|---|---|
|  | ![](../assets/items/612.png) |
| **Recipe id** | `2101` (`Item_Make`) |
| **Makes** | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 100 |
| **Gold** | 2,500 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Level (c24, *guess*)** | 10 |
| **Category / filter** | 7 / `0x2` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 220 |  |

Other recipes for the same item: [[wiki/recipes/801-red-passion-piece-d-recipe|recipe 801]], [[wiki/recipes/817-red-passion-piece-d-recipe|recipe 817]], [[wiki/recipes/2108-red-passion-piece-d-recipe|recipe 2108]]

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/video-rune-upgrades|Video notes: rune upgrade attempts (ZonderCoRe)]]
<!-- generated:end -->

## Notes

Training Camp list (UnitDB list 7): passion conversion at a worse rate than the fortress (220 instead of 200 fragments) plus a few weapons ([[gameplay/consumables|Consumables]] §4, *client*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- client: [[gameplay/consumables]] §4 (category 7 = the Training Camp passion converter, 220 instead of 200 fragments); unit 336 is the Training Camp unit whose UnitDB list is 7 ([[wiki/npcs/336-paraman|unit 336]])

## Open questions

Unit 336 is named Paraman (Legendary Blacksmith) in the client but carries list 7; no video shows who offered this list in the camp.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
