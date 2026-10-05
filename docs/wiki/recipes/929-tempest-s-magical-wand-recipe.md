---
title: "Tempest's magical wand recipe"
type: "recipe"
id: 929
status: "complete"
missing: []
sources: ["client: Item_Make.cdb id 929", "docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = output count, c23 = gold cost)", "guide: [[gameplay/items-and-crafting]] §3 (Farrell makes normal weapons and does passion conversion, Item_Make rows 801–827); unit 237 per [[gameplay/npc-locations]] §3 (Farrell 237/317)"]
result: {"item": 10004, "count": 1}
materials:
  - {"item": 2753, "count": 1}
  - {"item": 2703, "count": 1}
  - {"item": 1933, "count": 2}
gold: 100000
success_rate: 40
category: 2
filter_mask: 33554449
level: 3
raw: {"c2": 1}
npc: [237]
---
<!-- generated:start -->
<!-- generated-keys: title=88da81 type=61613a id=e29f7b sources=ff5f98 result=6c1f51 materials=e6d869 gold=409e95 success_rate=af3e13 category=da4b92 filter_mask=5c54ba level=77de68 raw=e722a2 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/10004.png) |
| **Recipe id** | `929` (`Item_Make`) |
| **Makes** | [[wiki/items/10004-tempest-s-magical-wand\|Tempest's magical wand]] × 1 |
| **Gold** | 100,000 (before the fort's price rate; one screenshot shows × 1.5) |
| **Success** | 40 % |
| **Level (c24, *guess*)** | 3 |
| **Category / filter** | 2 / `0x2000011` |
| **Crafted at** | [[wiki/npcs/237-farrell\|Farrell]] |

### Materials

|  | item | count | x |
|---|---|---|---|
| ![](wiki/assets/items/2753.png) | [[wiki/items/2753-the-tempest-fisher-s-sealed-weapon\|The Tempest Fisher's Sealed Weapon]] | 1 |  |
| ![](wiki/assets/items/2703.png) | [[wiki/items/2703-fin-of-fisher\|Fin of Fisher]] | 1 |  |
| ![](wiki/assets/items/1933.png) | [[wiki/items/1933-essence-of-water\|Essence of Water]] | 2 |  |

Unknown columns: `c2` = 1 (`c28` is the decoder's `gold@28`, which is not the gold cost).

NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), Alan (runes), Owen (alchemy), Paraman (superior weapons) — [[gameplay/items-and-crafting|Items and crafting]] §3.
<!-- generated:end -->

## Notes

Normal weapons are crafted at **Farrell** from 3 or 5 of a medal-bought material (2 bronze medals each at Athan) plus 50 / 70 / 100 crystals ([[gameplay/items-and-crafting|Items and crafting]] §3, *guide*). From WM 0920 crafted weapons have a small chance to come out **superior** ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

Gold here is the client's base cost. In-game screenshots show the fort's price rate on top, ×1.5 in the fort that was photographed ([[gameplay/items-and-crafting|Items and crafting]] §3, [[gameplay/consumables|Consumables]] §1, *image*).

## Behaviour

Success 40 % in the client. The craft window warns "There is a chance to fail in creating this item" for superior items ([[gameplay/items-and-crafting|Items and crafting]] §3, *image*).

## Sources

- guide: [[gameplay/items-and-crafting]] §3 (Farrell makes normal weapons and does passion conversion, Item_Make rows 801–827); unit 237 per [[gameplay/npc-locations]] §3 (Farrell 237/317)

## Open questions

Farrell's unit id: the fortress Farrell is 237; a second Farrell (317) has no recorded position ([[gameplay/npc-locations]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
