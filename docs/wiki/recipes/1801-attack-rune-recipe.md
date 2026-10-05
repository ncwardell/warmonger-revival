---
title: "Attack Rune recipe"
type: "recipe"
id: 1801
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 1801", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §2 (runes are crafted at Alan, Rune Maker, unit 323 per [[gameplay/npc-locations]] §3)"]
result: {"item": 7002, "count": 1}
materials:
  - {"item": 700, "count": 10}
  - {"item": 812, "count": 2}
gold: 5000
success_rate: 100
category: 4
filter_mask: 1
raw: {"c28": 200}
npc: [323]
---
<!-- generated:start -->
<!-- generated-keys: title=6ba2c6 type=61613a id=775ea0 sources=4cf738 result=b915aa materials=332c7e gold=f8237d success_rate=310b86 category=1b6453 filter_mask=356a19 raw=fc6d8f -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7002.png) |
| **Recipe id** | `1801` (`Item_Make`) |
| **Makes** | [[wiki/items/7002-attack-rune\|Attack Rune]] × 1 |
| **Gold** | 5,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 100 % |
| **Category / filter** | 4 / `0x1` |
| **Crafted at** | [[wiki/npcs/323-alan\|Alan]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 10 |  |
| ![](wiki/assets/items/812.png) | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 2 |  |

Unknown columns: `c28` = 200 (`c28` is the decoder's `gold@28`, which is not the gold cost).

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.

### Result mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/video-rune-upgrades|Video notes: rune upgrade attempts (ZonderCoRe)]]
<!-- generated:end -->

## Notes

Runes are crafted at **Alan** (Rune Maker, unit 323) in the fortress; T2/T3 runes need the fort's Rune mastery ([[gameplay/items-and-crafting|Items and crafting]] §2, *guide*). From WM 0824 yellow jewels can stand in for missing materials on T1 runes ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

A guide screenshot shows the T1 Attack rune at 10 Blue Crystals + 1 red gem material + **7,500 gold** → Attack +5 ([[gameplay/items-and-crafting|Items and crafting]] §2, *image*); 7,500 = the client's 5,000 × 1.5 fort rate.

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- guide: [[gameplay/items-and-crafting]] §2 (runes are crafted at Alan, Rune Maker, unit 323 per [[gameplay/npc-locations]] §3)

## Open questions

The screenshot shows 1 red gem material; the client asks for 2 Red bloodstone (812).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
