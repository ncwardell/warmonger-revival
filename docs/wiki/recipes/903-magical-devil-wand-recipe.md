---
title: "Magical Devil Wand recipe"
type: "recipe"
id: 903
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 903", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Farrell makes normal weapons and does passion conversion, Item_Make rows 801–827); unit 237 per [[gameplay/npc-locations]] §3 (Farrell 237/317)"]
result: {"item": 10020, "count": 1}
materials:
  - {"item": 854, "count": 5}
  - {"item": 700, "count": 100}
gold: 50000
success_rate: 100
category: 2
filter_mask: 16777233
superior: {"chance": 5, "item": 11020}
level: 2
npc: [237]
---
<!-- generated:start -->
<!-- generated-keys: title=0c8712 type=61613a id=437aa7 sources=b36e08 result=53ac49 materials=e059b5 gold=c2d4c5 success_rate=310b86 category=da4b92 filter_mask=b0800a superior=fc0af0 level=da4b92 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/10020.png) |
| **Recipe id** | `903` (`Item_Make`) |
| **Makes** | [[wiki/items/10020-magical-devil-wand\|Magical Devil Wand]] × 1 |
| **Gold** | 50,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Superior result** | 5 % → [[wiki/items/11020-magical-devil-wand\|Magical Devil Wand]] (*guess*: c19@40 / @44) |
| **Level (c24, *guess*)** | 2 |
| **Category / filter** | 2 / `0x1000011` |
| **Crafted at** | [[wiki/npcs/237-farrell\|Farrell]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 5 |  |
| ![](wiki/assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 100 |  |

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
<!-- generated:end -->

## Notes

Normal weapons are crafted at **Farrell** from 3 or 5 of a medal-bought material (2 bronze medals each at Athan) plus 50 / 70 / 100 crystals ([[gameplay/items-and-crafting|Items and crafting]] §3, *guide*). From WM 0920 crafted weapons have a small chance to come out **superior** ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- guide: [[gameplay/items-and-crafting]] §3 (Farrell makes normal weapons and does passion conversion, Item_Make rows 801–827); unit 237 per [[gameplay/npc-locations]] §3 (Farrell 237/317)

## Open questions

Farrell's unit id: the fortress Farrell is 237; a second Farrell (317) has no recorded position ([[gameplay/npc-locations]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
