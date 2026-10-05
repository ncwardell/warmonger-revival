---
title: "Skeleton king's Magic Gun"
type: "item"
id: 10014
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10014"]
name_key: "ItemName_10014"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 15
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 15}
skills: [5145, 5147, 5148, 5150]
reinforce: 32
icon: {"file": "Weapon_PCE_01.dds", "index": 4}
obtained_from:
  - {"how": "craft", "recipe": 923}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=83c353 type=d36ca9 id=ef75f7 sources=0a9087 name_key=eb6cfb kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=f1abd6 stats=db11c4 options=1f25ab skills=5d98bb reinforce=cb4e52 icon=f4596f obtained_from=123ada -->
|  |  |
|---|---|
|  | ![Skeleton king's Magic Gun](wiki/assets/items/10014.png) |
| **Item id** | `10014` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 4 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 15 | WeaponBase row |

### Weapon base

WeaponBase row 15. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 140, `c3` = 30, `c4` = 750, `c5` = 380.

### Weapon skills

Weapon base 15. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5145-energetic-bullet|Energetic Bullet]]
2. [[wiki/skills/5147-flash-bang|Flash Bang]]
3. [[wiki/skills/5148-rapid-dash|Rapid Dash]]
4. [[wiki/skills/5150-skull-king-s-claw|Skull king's Claw]]

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
| 923 | [[wiki/items/2751-the-death-head-s-sealed-weapon\|The Death Head's Sealed Weapon]] × 1, [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 2 | 0 | 40 |

### Where to get it

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
