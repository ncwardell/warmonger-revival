---
title: "Tome of Cooldown [Quest] recipe"
type: "recipe"
id: 599
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 599", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "client: [[gameplay/consumables]] §4 (fortress Owen, unit 214, has the full Item_Make category 1 list)"]
result: {"item": 2599, "count": 10}
materials:
  - {"item": 2595, "count": 30}
  - {"item": 2596, "count": 1}
  - {"item": 2597, "count": 2}
gold: 900
success_rate: 100
category: 1
filter_mask: 4194308
level: 1
raw: {"c27": 48}
npc: [214]
---
<!-- generated:start -->
<!-- generated-keys: title=ef7b0f type=61613a id=13b724 sources=d5b745 result=87636a materials=66d95c gold=28cc22 success_rate=310b86 category=356a19 filter_mask=e91fa6 level=356a19 raw=513f82 -->
|  |  |
|---|---|
|  | ![](../assets/items/2599.png) |
| **Recipe id** | `599` (`Item_Make`) |
| **Makes** | [[wiki/items/2599-tome-of-cooldown-quest\|Tome of Cooldown (Quest)]] × 10 |
| **Gold** | 900 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 1 / `0x400004` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/2595.png) | [[wiki/items/2595-peppermint-powder\|Peppermint powder]] | 30 |  |
| ![](../assets/items/2596.png) | [[wiki/items/2596-empty-scroll-a\|Empty Scroll (A)]] | 1 |  |
| ![](../assets/items/2597.png) | [[wiki/items/2597-burning-water\|Burning water]] | 2 |  |

Unknown columns: `c27` = 48 (`c28` is the decoder's `gold@28`, which is not the gold cost).

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/consumables|Consumables and clickables]]
<!-- generated:end -->

## Notes

Crafted at **Owen** (Red Union, unit 214) in the fortress, which has the full alchemy list ([[gameplay/consumables|Consumables]] §4, *client*). Alchemy recipes always succeed (100 %) ([[gameplay/consumables|Consumables]] §1, *client*).

Quest-only recipe for the alchemy tutorial: it uses the bind-on-pickup quest copies of the inputs and names quest 48 in its last column ([[gameplay/consumables|Consumables]] §6, *client*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- client: [[gameplay/consumables]] §4 (fortress Owen, unit 214, has the full Item_Make category 1 list)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
