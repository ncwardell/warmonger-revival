---
title: "Magic resist Penetration Rune"
type: "item"
id: 7097
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7097", "client (server-only table): Item_Jewel.cdb id 97"]
name_key: "ItemName_7097"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 8, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 42, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 7}
obtained_from:
  - {"how": "jewel_craft", "recipe": 95}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=346fa8 sources=763ff7 name_key=2fc93a kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=309b5c options=054ccf icon=f144cc obtained_from=bef014 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](../assets/items/7097.png) |
| **Item id** | `7097` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_29.png` cell 7 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +8 | flat | 14 |
| Magic resist Penetration | +42 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

Jewel upgrade (JewelSocketMake 95): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7096-magic-resist-penetration-rune|Magic resist Penetration Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
