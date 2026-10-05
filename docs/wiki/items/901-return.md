---
title: "Return"
type: "item"
id: 901
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 901"]
name_key: "ItemName_901"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 0}
cost_pair:
  - {"currency": 2, "amount": 0}
stats:
  - {"code": 13, "stat": "Armor Penetration", "value": 100, "scale": "level"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 100, "scale": "level"}
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 50, "scale": "tier"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 50, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 10000, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 10000, "scale": "flat"}
icon: {"file": "Artifacts_02.png", "index": 10}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=f9617f type=d36ca9 id=a071f3 sources=10e5e9 name_key=2b3a25 kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=32a324 cost_pair=395e20 stats=679657 icon=70d819 obtained_from=97d170 -->
|  |  |
|---|---|
| **Item id** | `901` |
| **Kind** | Bracelet (56) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Buy price** | 0 Gold |
| **Icon** | `ui/icons/Artifacts_02.png` cell 10 |

### Tooltip

> Return test

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration | +100 | × (tier × 15 + reinforce level) | 13 |
| Magic resist Penetration | +100 | × (tier × 15 + reinforce level) | 14 |
| Armor Penetration(%) | Armor Penetration +50% | × tier | 113 |
| Magic resist Penetration(%) | Magic resist Penetration +50% | × tier | 114 |
| Attack | +10000 | flat | 1 |
| Ability Power | +10000 | flat | 2 |

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
