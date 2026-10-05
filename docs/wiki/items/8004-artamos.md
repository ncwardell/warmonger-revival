---
title: "Artamos"
type: "item"
id: 8004
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8004"]
name_key: "ItemName_8004"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 2
weapon_base: 73
stats: []
options:
  - {"code": 200, "value": 73}
  - {"code": 201, "value": 5}
skills: [20202, 20204, 20215, 20207, 20208, 20209, 20211, 20213]
reinforce: 23
icon: {"file": "Items_20.png", "index": 31}
obtained_from:
  - {"how": "craft", "recipe": 1505}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=d105b8 type=d36ca9 id=f34304 sources=7387e6 name_key=5c6f79 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=da4b92 weapon_base=35e995 stats=97d170 options=82ceb5 skills=927a9a reinforce=d435a6 icon=e5f8ba obtained_from=06c299 -->
|  |  |
|---|---|
|  | ![Artamos](wiki/assets/items/8004.png) |
| **Item id** | `8004` |
| **Kind** | Innocence (18) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 2 |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 73 | WeaponBase row |
| 201 | 5 | Innocence value? |

### Weapon base

WeaponBase row 73. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 2954, `c3` = 115, `c4` = 750, `c5` = 380.

### Weapon skills

Weapon base 73. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20202-covert-step|Covert Step]]
2. [[wiki/skills/20204-hungry-arrows|Hungry arrows]]
3. [[wiki/skills/20215-hunting-eye|Hunting Eye]]
4. [[wiki/skills/20207-hunter-s-rage|Hunter's Rage]]
5. [[wiki/skills/20208-capture-weakness|Capture Weakness]]
6. [[wiki/skills/20209-invisible-prison|Invisible prison]]
7. [[wiki/skills/20211-improved-hand|Improved Hand]]
8. [[wiki/skills/20213-prudent-blow|Prudent blow]]

### Reinforcement

ItemSancMet row 23 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20, [[wiki/items/621-orange-passion-fragments-d\|Orange Passion Fragments (D)]] × 8 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 8 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 25, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 25, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 10 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 32, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 32, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 32, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 32, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 15 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 32, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 32, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 15 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1505 | [[wiki/items/9004-piece-artamos\|Piece : Artamos]] × 100, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 200 | 0 | 100 |

### Where to get it

- Hero gacha pool 03, grade 1 (Gacha_03.cdb; odds are server side)
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
