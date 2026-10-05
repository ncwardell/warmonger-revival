---
title: "Blue Passion Fragments [C] recipe"
type: "recipe"
id: 2104
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 2104", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "client: [[gameplay/consumables]] §4 (category 7 = the Training Camp passion converter, 220 instead of 200 fragments); unit 336 is the Training Camp unit whose UnitDB list is 7 ([[wiki/npcs/336-paraman|unit 336]])"]
result: {"item": 603, "count": 65}
materials:
  - {"item": 602, "count": 220}
gold: 5000
success_rate: 100
category: 7
filter_mask: 2
level: 10
npc: [336]
---
<!-- generated:start -->
<!-- generated-keys: title=8b69ee type=61613a id=a8c97e sources=76364a result=814a1a materials=fdc1d8 gold=f8237d success_rate=310b86 category=902ba3 filter_mask=da4b92 level=b1d578 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/603.png) |
| **Recipe id** | `2104` (`Item_Make`) |
| **Makes** | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 65 |
| **Gold** | 5,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Level (c24, *guess*)** | 10 |
| **Category / filter** | 7 / `0x2` |
| **Crafted at** | [[wiki/npcs/336-paraman\|Paraman]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 220 |  |

Other recipes for the same item: [[wiki/recipes/807-blue-passion-fragments-c-recipe|recipe 807]], [[wiki/recipes/823-blue-passion-fragments-c-recipe|recipe 823]]

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.
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
