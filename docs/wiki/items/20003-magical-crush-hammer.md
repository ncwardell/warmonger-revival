---
title: "Magical Crush Hammer"
type: "item"
id: 20003
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 20003"]
name_key: "ItemName_20003"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 45
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 45}
skills: [5067, 5068, 5069, 5070]
reinforce: 11
icon: {"file": "Weapon_PCD_01.dds", "index": 19}
obtained_from:
  - {"how": "craft", "recipe": 914}
  - {"how": "craft", "recipe": 2205}
  - {"how": "quest_reward", "quest": 82, "count": 1}
  - {"how": "quest_reward", "quest": 773, "count": 1}
  - {"how": "random_box", "box": 3}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=7fd242 type=d36ca9 id=918e02 sources=0689d5 name_key=9e1221 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=fb6443 stats=db11c4 options=96ad32 skills=a0d417 reinforce=17ba07 icon=e32f4e obtained_from=947977 -->
|  |  |
|---|---|
|  | ![Magical Crush Hammer](wiki/assets/items/20003.png) |
| **Item id** | `20003` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-guardian\|Guardian weapons]] |
| **Classes** | [[wiki/classes/5-guardian\|Guardian]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 19 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 45 | WeaponBase row |

### Weapon base

WeaponBase row 45. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 70, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 45. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5067-crushing-blow|Crushing Blow]]
2. [[wiki/skills/5068-head-butt|Head Butt]]
3. [[wiki/skills/5069-howl-of-victory|Howl of Victory]]
4. [[wiki/skills/5070-unyielding-will|Unyielding Will]]

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
| 914 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |
| 2205 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]] × 1
- Reward of quest [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]] × 1
- In random box table row 3 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 2 (Gacha_02.cdb; odds are server side)
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
