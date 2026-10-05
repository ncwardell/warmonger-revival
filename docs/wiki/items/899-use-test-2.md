---
title: "Use Test 2"
type: "item"
id: 899
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 899"]
name_key: "ItemName_67"
kind: 51
kind_name: "Armor"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 300}
cost_pair:
  - {"currency": 2, "amount": 300}
use_skill: 800
cooldown_s: 60
cooldown_group: 3
stats:
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 100, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
options:
  - {"code": 210, "value": 800}
  - {"code": 261, "value": 60}
  - {"code": 262, "value": 3}
icon: {"file": "Artifacts_01.png", "index": 22}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=5080c0 type=d36ca9 id=49ca49 sources=c2dbbc name_key=740e3b kind=b7eb6c kind_name=e687cb classes=92d079 bind=2be88c price=8a0da0 cost_pair=0babca use_skill=290a52 cooldown_s=e6c3dd cooldown_group=77de68 stats=e8bebe options=272068 icon=d17477 obtained_from=97d170 -->
|  |  |
|---|---|
| **Item id** | `899` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Buy price** | 300 Gold |
| **Cooldown** | 60 s (group 3) |
| **On use: skill** | [[wiki/skills/800-rune-of-teleportation\|Rune of Teleportation]] |
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
| 210 | 800 | skill cast on use |
| 261 | 60 | cooldown (s) |
| 262 | 3 | cooldown group |

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
