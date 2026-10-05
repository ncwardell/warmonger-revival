---
title: "Critical Strike (%) Rune"
type: "item"
id: 7202
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7202", "client (server-only table): Item_Jewel.cdb id 202"]
name_key: "ItemName_7202"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 1, "scale": "flat"}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 5, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 21}
icon: {"file": "Items_27.png", "index": 10}
obtained_from:
  - {"how": "craft", "recipe": 1821}
  - {"how": "random_box", "box": 49}
---
<!-- generated:start -->
<!-- generated-keys: title=93afc2 type=d36ca9 id=ecb216 sources=c938f7 name_key=794b13 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=3cb647 options=0ca6e9 icon=af6cb7 obtained_from=686d3b -->
|  |  |
|---|---|
|  | ![Critical Strike (%) Rune](wiki/assets/items/7202.png) |
| **Item id** | `7202` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 10 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike +(%) | Critical Strike +1% | flat | 109 |
| Critical Strike Deal(%) | Critical Strike Deal +5% | flat (from Item_Jewel) | 110 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 21 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1821 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/814-topaz\|Topaz]] × 5 | 0 | 100 |

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
