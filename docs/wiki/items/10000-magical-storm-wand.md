---
title: "Magical Storm Wand"
type: "item"
id: 10000
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10000"]
name_key: "ItemName_10000"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 1}
skills: [5008, 5009, 5010, 5011]
reinforce: 11
icon: {"file": "Weapon_PCE_01.dds", "index": 32}
obtained_from:
  - {"how": "craft", "recipe": 918}
  - {"how": "random_box", "box": 1}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=108ba1 type=d36ca9 id=8a12a3 sources=781891 name_key=def08e kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=356a19 stats=977f84 options=8f14f7 skills=931601 reinforce=17ba07 icon=51cb55 obtained_from=2580dc -->
|  |  |
|---|---|
|  | ![Magical Storm Wand](wiki/assets/items/10000.png) |
| **Item id** | `10000` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 32 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +2 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Ability Power | +10 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 1 | WeaponBase row |

### Weapon base

WeaponBase row 1. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 100, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 1. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5008-squall|Squall]]
2. [[wiki/skills/5009-breeze|Breeze]]
3. [[wiki/skills/5010-blessed-wind|Blessed Wind]]
4. [[wiki/skills/5011-eye-of-the-storm|Eye of the Storm]]

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
| 918 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 1 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 3 (Gacha_02.cdb; odds are server side)
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
