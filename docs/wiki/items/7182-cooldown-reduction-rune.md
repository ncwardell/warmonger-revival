---
title: "Cooldown Reduction Rune"
type: "item"
id: 7182
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7182", "client (server-only table): Item_Jewel.cdb id 182"]
name_key: "ItemName_7182"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 1, "scale": "flat"}
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 2, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 19}
icon: {"file": "Items_27.png", "index": 50}
obtained_from:
  - {"how": "craft", "recipe": 1819}
  - {"how": "random_box", "box": 49}
---
<!-- generated:start -->
<!-- generated-keys: title=a62c86 type=d36ca9 id=b7c1d0 sources=e95fc5 name_key=9633e6 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=efcfa1 options=c1a4c7 icon=396f31 obtained_from=a57131 -->
|  |  |
|---|---|
|  | ![Cooldown Reduction Rune](wiki/assets/items/7182.png) |
| **Item id** | `7182` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 50 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Cooldown Reduction(%) | Cooldown Reduction +1% | flat | 212 |
| Cooldown Reduction(%) | Cooldown Reduction +2% | flat (from Item_Jewel) | 212 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 19 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1819 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/816-onyx\|Onyx]] × 5 | 0 | 100 |

### Where to get it

- In random box table row 49 (RandomBox.cdb; odds are server side)
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
