---
title: "PvP Armor Rune"
type: "item"
id: 7153
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7153", "client (server-only table): Item_Jewel.cdb id 153"]
name_key: "ItemName_7153"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 142, "stat": "PvP Armor", "value": 2, "scale": "flat"}
  - {"code": 137, "stat": "option 137", "value": 2, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 16}
icon: {"file": "Items_25.png", "index": 19}
obtained_from:
  - {"how": "jewel_craft", "recipe": 151}
---
<!-- generated:start -->
<!-- generated-keys: title=1f4563 type=d36ca9 id=454be5 sources=cbc315 name_key=396fbb kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=076c78 options=3a5286 icon=fd54cf obtained_from=b8fd20 -->
|  |  |
|---|---|
|  | ![PvP Armor Rune](../assets/items/7153.png) |
| **Item id** | `7153` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_25.png` cell 19 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Armor | +2 | flat | 142 |
| option 137 | +2 | flat (from Item_Jewel) | 137 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 16 | rune grade? |

Jewel upgrade (JewelSocketMake 151): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7152-pvp-armor-rune|PvP Armor Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/sources|Sources and gaps]]
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
