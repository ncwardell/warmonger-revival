---
title: "Magical Devil Wand"
type: "item"
id: 11020
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 11020"]
name_key: "ItemName_10020"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 121
stats:
  - {"code": 1, "stat": "Attack", "value": 4, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 14, "scale": "tier"}
options:
  - {"code": 200, "value": 121}
skills: [10177, 10180, 10178, 10179]
reinforce: 12
icon: {"file": "Weapon_PCE_01.dds", "index": 39}
obtained_from:
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=3ab850 type=d36ca9 id=c47a5f sources=1d1bbd name_key=d98e14 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=8bd795 stats=1fb006 options=394ade skills=d388c6 reinforce=7b5200 icon=c2c93b obtained_from=501dc8 -->
|  |  |
|---|---|
|  | ![Magical Devil Wand](wiki/assets/items/11020.png) |
| **Item id** | `11020` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 39 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +4 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +10 | × (tier × 15 + reinforce level) | 2 |
| Ability Power | +14 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 121 | WeaponBase row |

### Weapon base

WeaponBase row 121. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 100, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 121. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/10177-hand-of-curse|Hand of Curse]]
2. [[wiki/skills/10180-petrification|Petrification]]
3. [[wiki/skills/10178-hush|Hush]]
4. [[wiki/skills/10179-dark-matter|Dark Matter]]

### Reinforcement

ItemSancMet row 12 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 6 |
| 2 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 6 |
| 3 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 8 |
| 4 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15 |
| 5 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15 |
| 6 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 16 |

### Where to get it

- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
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
