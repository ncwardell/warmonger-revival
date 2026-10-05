---
title: "Skeleton King's Magic Cannon recipe"
type: "recipe"
id: 928
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 928", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide + image: [[gameplay/items-and-crafting]] §3 (Paraman makes the superior Skeleton King's weapons; 150,000 gold + 3 materials, can fail, fort Weapon mastery 3); unit 322 per [[gameplay/npc-locations]] §3"]
result: {"item": 40014, "count": 1}
materials:
  - {"item": 2751, "count": 1}
  - {"item": 2701, "count": 1}
  - {"item": 1930, "count": 2}
gold: 100000
success_rate: 40
category: 2
filter_mask: 33554497
level: 4
raw: {"c2": 2}
npc: [322]
---
<!-- generated:start -->
<!-- generated-keys: title=f62758 type=61613a id=3eac69 sources=41c569 result=8d4efa materials=b112e4 gold=409e95 success_rate=af3e13 category=da4b92 filter_mask=bdac30 level=1b6453 raw=32370f -->
|  |  |
|---|---|
|  | ![](../assets/items/40014.png) |
| **Recipe id** | `928` (`Item_Make`) |
| **Makes** | [[wiki/items/40014-skeleton-king-s-magic-cannon\|Skeleton King's Magic Cannon]] × 1 |
| **Gold** | 100,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 40 % |
| **Level (c24, *guess*)** | 4 |
| **Category / filter** | 2 / `0x2000041` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/2751.png) | [[wiki/items/2751-the-death-head-s-sealed-weapon\|The Death Head's Sealed Weapon]] | 1 |  |
| ![](../assets/items/2701.png) | [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] | 1 |  |
| ![](../assets/items/1930.png) | [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] | 2 |  |

Unknown columns: `c2` = 2 (`c28` is the decoder's `gold@28`, which is not the gold cost).

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
<!-- generated:end -->

## Notes

Superior Skeleton King's weapons come from **Paraman** (Legendary Blacksmith, unit 322): a guide screenshot shows **150,000 gold + 3 materials**, a fail warning and fort Weapon mastery 3; stats Attack +140, AP +60, range +200 ([[gameplay/items-and-crafting|Items and crafting]] §3, *image*). The client's 100,000 gold × 1.5 fort rate gives the 150,000 shown.

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

Success 40 % in the client. The craft window warns "There is a chance to fail in creating this item" for superior items ([[gameplay/items-and-crafting|Items and crafting]] §3, *image*).

## Sources

- guide + image: [[gameplay/items-and-crafting]] §3 (Paraman makes the superior Skeleton King's weapons; 150,000 gold + 3 materials, can fail, fort Weapon mastery 3); unit 322 per [[gameplay/npc-locations]] §3

## Open questions

The client files these rows in the same Item_Make category (2) as Farrell's weapons and passion conversion; the guide puts them at Paraman. Paraman 322's UnitDB function is "Weapon Alchemy" rather than "Create" ([[wiki/npcs/322-paraman|Paraman]]).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
