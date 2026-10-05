---
title: "Magical Thunder Wand"
type: "item"
id: 11001
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 11001"]
name_key: "ItemName_10001"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 102
stats:
  - {"code": 1, "stat": "Attack", "value": 4, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 14, "scale": "tier"}
options:
  - {"code": 200, "value": 102}
skills: [10004, 10005, 10006, 10007]
reinforce: 12
icon: {"file": "Weapon_PCE_01.dds", "index": 33}
obtained_from:
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=3f4fa2 type=d36ca9 id=9de8ff sources=11fa71 name_key=67c239 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=c8306a stats=1fb006 options=583f7b skills=eb6ef9 reinforce=7b5200 icon=df9804 obtained_from=501dc8 -->
|  |  |
|---|---|
|  | ![Magical Thunder Wand](../assets/items/11001.png) |
| **Item id** | `11001` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 33 |

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
| 200 | 102 | WeaponBase row |

### Weapon base

WeaponBase row 102. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 100, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 102. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/10004-thunderbolt|Thunderbolt]]
2. [[wiki/skills/10005-lightning-strike|Lightning Strike]]
3. [[wiki/skills/10006-ball-of-lighting|Ball of Lighting]]
4. [[wiki/skills/10007-might-of-thunder-god|Might of Thunder God]]

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
