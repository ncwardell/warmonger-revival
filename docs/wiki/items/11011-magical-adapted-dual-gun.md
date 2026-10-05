---
title: "Magical adapted Dual Gun"
type: "item"
id: 11011
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 11011"]
name_key: "ItemName_10011"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 112
stats:
  - {"code": 1, "stat": "Attack", "value": 14, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 14, "scale": "tier"}
options:
  - {"code": 200, "value": 112}
skills: [10102, 10103, 10104, 10105]
reinforce: 12
icon: {"file": "Weapon_PCE_01.dds", "index": 0}
obtained_from:
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=e0c382 type=d36ca9 id=fcae78 sources=2c7a05 name_key=b6fbe8 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=601ca9 stats=c43914 options=2c8fef skills=5566dd reinforce=7b5200 icon=5868a7 obtained_from=501dc8 -->
|  |  |
|---|---|
|  | ![Magical adapted Dual Gun](../assets/items/11011.png) |
| **Item id** | `11011` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 0 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +14 | × (tier × 15 + reinforce level) | 1 |
| Attack | +14 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 112 | WeaponBase row |

### Weapon base

WeaponBase row 112. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 120, `c3` = 30, `c4` = 750, `c5` = 380.

### Weapon skills

Weapon base 112. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/10102-ankle-aim|Ankle Aim]]
2. [[wiki/skills/10103-rapid-reload|Rapid Reload]]
3. [[wiki/skills/10104-entangling-bullet|Entangling Bullet]]
4. [[wiki/skills/10105-suppressing-fire|Suppressing Fire]]

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

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
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
