---
title: "Magic resist Penetration Rune"
type: "item"
id: 7093
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7093", "client (server-only table): Item_Jewel.cdb id 93"]
name_key: "ItemName_7093"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 2, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 12, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 3}
obtained_from:
  - {"how": "jewel_craft", "recipe": 91}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=f82984 sources=de4261 name_key=df27d9 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=f44b17 options=054ccf icon=45027c obtained_from=b6f759 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](../assets/items/7093.png) |
| **Item id** | `7093` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_29.png` cell 3 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +2 | flat | 14 |
| Magic resist Penetration | +12 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

Jewel upgrade (JewelSocketMake 91): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7092-magic-resist-penetration-rune|Magic resist Penetration Rune]].

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
