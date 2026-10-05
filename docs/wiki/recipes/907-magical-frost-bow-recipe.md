---
title: "Magical Frost Bow recipe"
type: "recipe"
id: 907
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 907", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Farrell makes normal weapons and does passion conversion, Item_Make rows 801–827); unit 237 per [[gameplay/npc-locations]] §3 (Farrell 237/317)"]
result: {"item": 15004, "count": 1}
materials:
  - {"item": 854, "count": 3}
  - {"item": 700, "count": 50}
gold: 10000
success_rate: 100
category: 2
filter_mask: 16777249
superior: {"chance": 5, "item": 16004}
level: 1
npc: [237]
---
<!-- generated:start -->
<!-- generated-keys: title=7ff24e type=61613a id=bd7c80 sources=34e76e result=f3d887 materials=c06eb2 gold=8a12a3 success_rate=310b86 category=da4b92 filter_mask=619013 superior=f69b74 level=356a19 -->
|  |  |
|---|---|
|  | ![](../assets/items/15004.png) |
| **Recipe id** | `907` (`Item_Make`) |
| **Makes** | [[wiki/items/15004-magical-frost-bow\|Magical Frost Bow]] × 1 |
| **Gold** | 10,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Superior result** | 5 % → [[wiki/items/16004-magical-frost-bow\|Magical Frost Bow]] (*guess*: c19@40 / @44) |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 2 / `0x1000021` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 3 |  |
| ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 50 |  |

Other recipes for the same item: [[wiki/recipes/2202-magical-frost-bow-recipe|recipe 2202]]

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
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
