---
title: "Armor Penetration Rune"
type: "item"
id: 7083
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7083", "client (server-only table): Item_Jewel.cdb id 83"]
name_key: "ItemName_7083"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 13, "stat": "Armor Penetration", "value": 2, "scale": "flat"}
  - {"code": 13, "stat": "Armor Penetration", "value": 12, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 9}
icon: {"file": "Items_29.png", "index": 33}
obtained_from:
  - {"how": "jewel_craft", "recipe": 81}
---
<!-- generated:start -->
<!-- generated-keys: title=49e5d7 type=d36ca9 id=4dea86 sources=a840c6 name_key=7fc7c0 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=5e0d58 options=9b3b47 icon=f80c65 obtained_from=1f794c -->
|  |  |
|---|---|
|  | ![Armor Penetration Rune](../assets/items/7083.png) |
| **Item id** | `7083` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_29.png` cell 33 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration | +2 | flat | 13 |
| Armor Penetration | +12 | flat (from Item_Jewel) | 13 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 9 | rune grade? |

Jewel upgrade (JewelSocketMake 81): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7082-armor-penetration-rune|Armor Penetration Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/video-rune-upgrades|Video notes: rune upgrade attempts (ZonderCoRe)]]
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
