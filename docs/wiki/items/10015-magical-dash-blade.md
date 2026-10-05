---
title: "Magical Dash Blade"
type: "item"
id: 10015
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10015"]
name_key: "ItemName_10015"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 16
stats:
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "tier"}
options:
  - {"code": 200, "value": 16}
skills: [5048, 5050, 5052, 5054]
reinforce: 11
icon: {"file": "Weapon_PCE_01.dds", "index": 16}
obtained_from:
  - {"how": "craft", "recipe": 901}
  - {"how": "random_box", "box": 2}
  - {"how": "random_box", "box": 4}
  - {"how": "random_box", "box": 5}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=8f814a type=d36ca9 id=848f94 sources=8fba17 name_key=0f9cf4 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=1574bd stats=0447a2 options=270e23 skills=e0b65e reinforce=17ba07 icon=3eda32 obtained_from=b411e3 -->
|  |  |
|---|---|
|  | ![Magical Dash Blade](wiki/assets/items/10015.png) |
| **Item id** | `10015` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-saint\|Saint weapons]] |
| **Classes** | [[wiki/classes/1-saint\|Saint]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 16 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +2 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Attack | +2 | × tier | 1 |
| Ability Power | +8 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 16 | WeaponBase row |

### Weapon base

WeaponBase row 16. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 100, `c3` = 90, `c4` = 250, `c5` = 380.

### Weapon skills

Weapon base 16. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5048-restriction|Restriction]]
2. [[wiki/skills/5050-punishing-charge|Punishing Charge]]
3. [[wiki/skills/5052-blessing-of-order|Blessing of Order]]
4. [[wiki/skills/5054-light-of-judgement|Light of Judgement]]

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
| 901 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 2 (RandomBox.cdb; odds are server side)
- In random box table row 4 (RandomBox.cdb; odds are server side)
- In random box table row 5 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 2 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
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
