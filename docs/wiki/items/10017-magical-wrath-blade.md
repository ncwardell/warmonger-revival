---
title: "Magical Wrath Blade"
type: "item"
id: 10017
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10017"]
name_key: "ItemName_10017"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 18
stats:
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "tier"}
options:
  - {"code": 200, "value": 18}
skills: [5022, 5023, 5024, 5025]
reinforce: 11
icon: {"file": "Weapon_PCE_01.dds", "index": 17}
obtained_from:
  - {"how": "craft", "recipe": 902}
  - {"how": "craft", "recipe": 2201}
  - {"how": "quest_reward", "quest": 80, "count": 1}
  - {"how": "quest_reward", "quest": 769, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=1e1465 type=d36ca9 id=4cc58c sources=26ad24 name_key=0c78b6 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=9e6a55 stats=0447a2 options=e6c27e skills=a006a6 reinforce=17ba07 icon=ac8162 obtained_from=da692c -->
|  |  |
|---|---|
|  | ![Magical Wrath Blade](wiki/assets/items/10017.png) |
| **Item id** | `10017` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-saint\|Saint weapons]] |
| **Classes** | [[wiki/classes/1-saint\|Saint]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 17 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +2 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Attack | +2 | × tier | 1 |
| Ability Power | +8 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 18 | WeaponBase row |

### Weapon base

WeaponBase row 18. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 100, `c3` = 90, `c4` = 250, `c5` = 380.

### Weapon skills

Weapon base 18. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5022-blade-storm|Blade storm]]
2. [[wiki/skills/5023-wings-of-fair-wind|Wings of fair wind]]
3. [[wiki/skills/5024-blink-like-wind|Blink like wind]]
4. [[wiki/skills/5025-wrath-of-the-west|Wrath of the West]]

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
| 902 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |
| 2201 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]] × 1
- Reward of quest [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 02, grade 3 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
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
