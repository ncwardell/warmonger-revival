---
title: "Potion of Health [Quest] recipe"
type: "recipe"
id: 749
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 749", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "client: [[gameplay/consumables]] §4 (fortress Owen, unit 214, has the full Item_Make category 1 list)"]
result: {"item": 2598, "count": 100}
materials:
  - {"item": 2593, "count": 100}
  - {"item": 2594, "count": 2}
gold: 3000
success_rate: 100
category: 1
filter_mask: 4194305
level: 1
raw: {"c27": 47}
npc: [214]
---
<!-- generated:start -->
<!-- generated-keys: title=e1dbf9 type=61613a id=01055f sources=d21e98 result=89c301 materials=314ae1 gold=7507d4 success_rate=310b86 category=356a19 filter_mask=6eb8df level=356a19 raw=bd5938 -->
|  |  |
|---|---|
|  | ![](../assets/items/2598.png) |
| **Recipe id** | `749` (`Item_Make`) |
| **Makes** | [[wiki/items/2598-potion-of-health-quest\|Potion of Health (Quest)]] × 100 |
| **Gold** | 3,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Level (c24, *guess*)** | 1 |
| **Category / filter** | 1 / `0x400001` |
| **Crafted at** | unknown (not in the client; add `npc:`) |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](../assets/items/2593.png) | [[wiki/items/2593-empty-flask-a\|Empty Flask (A)]] | 100 |  |
| ![](../assets/items/2594.png) | [[wiki/items/2594-crystal-red\|Crystal : Red]] | 2 |  |

Unknown columns: `c27` = 47 (`c28` is the decoder's `gold@28`, which is not the gold cost).

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/consumables|Consumables and clickables]]
- [[gameplay/potion-regen|Potion regeneration ticks]]
<!-- generated:end -->

## Notes

Crafted at **Owen** (Red Union, unit 214) in the fortress, which has the full alchemy list ([[gameplay/consumables|Consumables]] §4, *client*). Alchemy recipes always succeed (100 %) ([[gameplay/consumables|Consumables]] §1, *client*).

Quest-only recipe for the alchemy tutorial: it uses the bind-on-pickup quest copies of the inputs and names quest 47 in its last column ([[gameplay/consumables|Consumables]] §6, *client*).

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
