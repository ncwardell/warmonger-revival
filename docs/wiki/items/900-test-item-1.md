---
title: "Test Item 1"
type: "item"
id: 900
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 900"]
name_key: "ItemName_900"
kind: 57
kind_name: "Ring"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
stats:
  - {"code": 6, "stat": "Armor", "value": 100, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 100, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 100, "scale": "level"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 200, "scale": "tier"}
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 90, "scale": "flat"}
  - {"code": 5, "stat": "Movement", "value": 900, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 90000, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 30000, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_02.png", "index": 2}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=36bcc7 type=d36ca9 id=28cc22 sources=256efe name_key=c86bf2 kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=2be88c price=8c6ae2 cost_pair=982f5a stats=5e245c reinforce=da4b92 icon=c01c43 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Test Item 1](wiki/assets/items/900.png) |
| **Item id** | `900` |
| **Kind** | Ring (57) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_02.png` cell 2 |

### Tooltip

> Makes you almost as powerful as Raifs.

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +100 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +100 | × (tier × 15 + reinforce level) | 7 |
| Mana | +100 | × (tier × 15 + reinforce level) | 33 |
| Mana Regeneration | +200 | × tier | 34 |
| Cooldown Reduction(%) | Cooldown Reduction +90% | flat | 212 |
| Movement | +900 | flat | 5 |
| Health | +90000 | flat | 31 |
| Health Regeneration | +30000 | flat | 32 |

### Reinforcement

ItemSancMet row 2 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 4 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 4 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 6 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 10 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 15 |

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
