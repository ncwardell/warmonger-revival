---
title: "Skeleton King's Magic Cannon"
type: "item"
id: 20014
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 20014"]
name_key: "ItemName_20014"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 68
stats:
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 2, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 2, "scale": "tier"}
options:
  - {"code": 200, "value": 68}
skills: [5298, 5299, 5301, 5302]
reinforce: 32
icon: {"file": "Weapon_PCD_01.dds", "index": 4}
obtained_from:
  - {"how": "craft", "recipe": 926}
  - {"how": "random_box", "box": 5}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=b216d1 type=d36ca9 id=15f935 sources=5d5725 name_key=d97363 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=b4c96d stats=c5b730 options=3d887f skills=59eadd reinforce=cb4e52 icon=a19198 obtained_from=56a13c -->
|  |  |
|---|---|
|  | ![Skeleton King's Magic Cannon](wiki/assets/items/20014.png) |
| **Item id** | `20014` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-guardian\|Guardian weapons]] |
| **Classes** | [[wiki/classes/5-guardian\|Guardian]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 4 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +8 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +2 | × (tier × 15 + reinforce level) | 2 |
| Attack | +8 | × tier | 1 |
| Ability Power | +2 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 68 | WeaponBase row |

### Weapon base

WeaponBase row 68. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 160, `c3` = 40, `c4` = 700, `c5` = 380.

### Weapon skills

Weapon base 68. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5298-rocket-shot|Rocket Shot]]
2. [[wiki/skills/5299-smoke-screen|Smoke Screen]]
3. [[wiki/skills/5301-step-back|Step Back]]
4. [[wiki/skills/5302-careful-attack|Careful Attack]]

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
| 926 | [[wiki/items/2751-the-death-head-s-sealed-weapon\|The Death Head's Sealed Weapon]] × 1, [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 2 | 0 | 40 |

### Where to get it

- In random box table row 5 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 2 (Gacha_05.cdb; odds are server side)

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
