---
title: "Skeleton King's Magic Dagger"
type: "item"
id: 35009
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 35009"]
name_key: "ItemName_35009"
kind: 31
kind_name: "Weapon"
classes: ["Punisher"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 2
weapon_base: 31
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 31}
skills: [5139, 5140, 5141, 5142]
reinforce: 33
icon: {"file": "Weapon_PCM_01.dds", "index": 20}
obtained_from:
  - {"how": "craft", "recipe": 927}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=492b52 type=d36ca9 id=7c22fa sources=8b01e5 name_key=e3db5e kind=632667 kind_name=631b4f classes=51f98f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=da4b92 weapon_base=632667 stats=db11c4 options=2e0fea skills=872ca5 reinforce=b6692e icon=c82c6b obtained_from=d098f6 -->
|  |  |
|---|---|
|  | ![Skeleton King's Magic Dagger](../assets/items/35009.png) |
| **Item id** | `35009` |
| **Kind** | Weapon (31) |
| **Classes** | Punisher |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 2 |
| **Icon** | `ui/icons/Weapon_PCM_01.dds` cell 20 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 31 | WeaponBase row |

### Weapon base

WeaponBase row 31. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 140, `c3` = 60, `c4` = 200, `c5` = 380.

### Weapon skills

Weapon base 31. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5139-poisonous-blade|Poisonous Blade]]
2. [[wiki/skills/5140-assassination|Assassination]]
3. [[wiki/skills/5141-fang-of-knives|Fang of Knives]]
4. [[wiki/skills/5142-final-strike|Final Strike]]

### Reinforcement

ItemSancMet row 33 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 30 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 32 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 32 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 927 | [[wiki/items/2751-the-death-head-s-sealed-weapon\|The Death Head's Sealed Weapon]] × 1, [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 2 | 0 | 40 |

### Where to get it

- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
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
