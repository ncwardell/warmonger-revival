---
title: "Magical Dash Hammer"
type: "item"
id: 20002
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 20002"]
name_key: "ItemName_20002"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 44
stats:
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
options:
  - {"code": 200, "value": 44}
skills: [5059, 5060, 5061, 5062]
reinforce: 11
icon: {"file": "Weapon_PCD_01.dds", "index": 18}
obtained_from:
  - {"how": "craft", "recipe": 913}
  - {"how": "random_box", "box": 2}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=8b97dd type=d36ca9 id=a95eed sources=564bfc name_key=83e743 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=98fbc4 stats=76534b options=9f617c skills=81f6ae reinforce=17ba07 icon=48567c obtained_from=119090 -->
|  |  |
|---|---|
|  | ![Magical Dash Hammer](wiki/assets/items/20002.png) |
| **Item id** | `20002` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 18 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +4 | × (tier × 15 + reinforce level) | 2 |
| Attack | +6 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +4 | × tier | 2 |
| Attack | +6 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 44 | WeaponBase row |

### Weapon base

WeaponBase row 44. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 70, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 44. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5059-crippling-blow|Crippling Blow]]
2. [[wiki/skills/5060-charging-chariot|Charging Chariot]]
3. [[wiki/skills/5061-fury|Fury]]
4. [[wiki/skills/5062-meteor|Meteor]]

### Reinforcement

ItemSancMet row 11 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 2 |
| 4 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 3 |
| 5 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 7 |
| 6 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 8 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 913 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 2 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 2 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)
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
