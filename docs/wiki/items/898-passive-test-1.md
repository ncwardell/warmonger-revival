---
title: "Passive Test 1"
type: "item"
id: 898
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 898"]
name_key: "ItemName_66"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 300}
cost_pair:
  - {"currency": 2, "amount": 300}
stats:
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 100, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
options:
  - {"code": 303, "value": 2012}
icon: {"file": "Artifacts_01.png", "index": 22}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=69cc4d type=d36ca9 id=6b2e24 sources=92fe96 name_key=49756c kind=e1822d kind_name=c90f98 classes=92d079 bind=2be88c price=8a0da0 cost_pair=0babca stats=e8bebe options=4aac6f icon=d17477 obtained_from=97d170 -->
|  |  |
|---|---|
| **Item id** | `898` |
| **Kind** | Helmet (50) |
| **Category** | [[wiki/items/armor-helmet\|Helmets]] |
| **Classes** | all |
| **Buy price** | 300 Gold |
| **Icon** | `ui/icons/Artifacts_01.png` cell 22 |

### Tooltip

> Final upgrade effects : Attack +30, Attack Speed +16

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +8 | × (tier × 15 + reinforce level) | 1 |
| Health | +100 | × (tier × 15 + reinforce level) | 31 |
| Health | +200 | × (tier × 15 + reinforce level) | 31 |
| Attack | +6 | × tier | 1 |
| Attack | +6 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 303 | 2012 | unknown |

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
