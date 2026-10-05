---
title: "Magical Blade Shield : Flame"
type: "item"
id: 10005
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10005"]
name_key: "ItemName_10005"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 6
stats:
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 2, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 6}
skills: [5266, 5271, 5268, 5269]
reinforce: 32
icon: {"file": "Weapon_PCE_01.dds", "index": 40}
obtained_from:
  - {"how": "craft", "recipe": 930}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=9e4245 type=d36ca9 id=8b954a sources=4529be name_key=7a2d63 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=c1dfd9 stats=03d72e options=b588e6 skills=b0a8d9 reinforce=cb4e52 icon=8ff19d obtained_from=1f6035 -->
|  |  |
|---|---|
|  | ![Magical Blade Shield : Flame](wiki/assets/items/10005.png) |
| **Item id** | `10005` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-saint\|Saint weapons]] |
| **Classes** | [[wiki/classes/1-saint\|Saint]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 40 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +8 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +2 | × (tier × 15 + reinforce level) | 2 |
| Ability Power | +10 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 6 | WeaponBase row |

### Weapon base

WeaponBase row 6. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 140, `c3` = 60, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 6. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5266-fiery-anger|Fiery Anger]]
2. [[wiki/skills/5271-flame-armor|Flame armor]]
3. [[wiki/skills/5268-fiery-fury|Fiery Fury]]
4. [[wiki/skills/5269-flame-area|Flame area]]

### Reinforcement

ItemSancMet row 32 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 8 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 16 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 16 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 930 | [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon\|The Arch devil Akasha's Sealed Weapon]] × 1, [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] × 1, [[wiki/items/1932-essence-of-fire\|Essence of Fire]] × 2 | 0 | 40 |

### Where to get it

- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 2 (Gacha_05.cdb; odds are server side)
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
