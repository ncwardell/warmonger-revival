---
title: "Magical Devil Wand"
type: "item"
id: 30020
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 30020"]
name_key: "ItemName_30020"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 85
stats:
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 85}
skills: [5471, 5474, 5472, 5473]
reinforce: 12
icon: {"file": "Weapon_PCE_01.dds", "index": 39}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=3ab850 type=d36ca9 id=a0d7b7 sources=2d75dc name_key=f7f198 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=135224 stats=9064e3 options=f958c4 skills=25c250 reinforce=7b5200 icon=c2c93b obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Magical Devil Wand](wiki/assets/items/30020.png) |
| **Item id** | `30020` |
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
| Ability Power | +10 | × (tier × 15 + reinforce level) | 2 |
| Ability Power | +10 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 85 | WeaponBase row |

### Weapon base

WeaponBase row 85. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 50, `c3` = 100, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 85. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5471-cursed-hand|Cursed Hand]]
2. [[wiki/skills/5474-petrification|Petrification]]
3. [[wiki/skills/5472-hush|Hush]]
4. [[wiki/skills/5473-dark-matter|Dark Matter]]

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

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

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
