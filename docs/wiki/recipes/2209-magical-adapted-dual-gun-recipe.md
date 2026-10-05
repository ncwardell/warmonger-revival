---
title: "Magical adapted Dual Gun recipe"
type: "recipe"
id: 2209
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 2209", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "client: [[gameplay/consumables]] §4 (category 7 = the Training Camp passion converter, 220 instead of 200 fragments); unit 336 is the Training Camp unit whose UnitDB list is 7 ([[wiki/npcs/336-paraman|unit 336]])"]
result: {"item": 10011, "count": 1}
materials:
  - {"item": 854, "count": 3}
  - {"item": 700, "count": 50}
gold: 10000
success_rate: 100
category: 7
filter_mask: 16777233
superior: {"chance": 5, "item": 11011}
level: 1
npc: [336]
---
<!-- generated:start -->
<!-- generated-keys: title=f838f9 type=61613a id=6f5067 sources=e125d9 result=d51ce8 materials=c06eb2 gold=8a12a3 success_rate=310b86 category=902ba3 filter_mask=b0800a superior=c0cd76 level=356a19 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/10011.png) |
| **Recipe id** | `2209` (`Item_Make`) |
| **Makes** | [[wiki/items/10011-magical-adapted-dual-gun\|Magical adapted Dual Gun]] × 1 |
| **Gold** | 10,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Superior result** | 5 % → [[wiki/items/11011-magical-adapted-dual-gun\|Magical adapted Dual Gun]] (*guess*: c19@40 / @44) |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 7 / `0x1000011` |
| **Crafted at** | [[wiki/npcs/336-paraman\|Paraman]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 3 |  |
| ![](wiki/assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 50 |  |

Other recipes for the same item: [[wiki/recipes/922-magical-adapted-dual-gun-recipe|recipe 922]]

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
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
