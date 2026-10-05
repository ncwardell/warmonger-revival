---
title: "Attack Speed(%) Rune"
type: "item"
id: 7174
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7174", "client (server-only table): Item_Jewel.cdb id 174"]
name_key: "ItemName_7174"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 3, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 8, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 32}
obtained_from:
  - {"how": "jewel_craft", "recipe": 172}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=5fc772 sources=ceac2a name_key=6c5f88 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=23b9d6 options=109d7f icon=5ea85c obtained_from=dbc4af -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](wiki/assets/items/7174.png) |
| **Item id** | `7174` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_27.png` cell 32 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +3% | flat | 103 |
| Attack Speed(%) | Attack Speed +8% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

Jewel upgrade (JewelSocketMake 172): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15 from [[wiki/items/7173-attack-speed-rune|Attack Speed(%) Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.
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
