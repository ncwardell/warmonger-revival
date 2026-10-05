---
title: "Magical Frost Bow"
type: "item"
id: 15004
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 15004"]
name_key: "ItemName_15004"
kind: 31
kind_name: "Weapon"
classes: ["Punisher"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 26
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 26}
skills: [5112, 5113, 5114, 5115]
reinforce: 11
icon: {"file": "Weapon_PCM_01.dds", "index": 3}
obtained_from:
  - {"how": "craft", "recipe": 907}
  - {"how": "craft", "recipe": 2202}
  - {"how": "quest_reward", "quest": 81, "count": 1}
  - {"how": "quest_reward", "quest": 772, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=7cce5f type=d36ca9 id=da002e sources=73735e name_key=027e09 kind=632667 kind_name=631b4f classes=51f98f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=887309 stats=db11c4 options=07adf5 skills=db1a22 reinforce=17ba07 icon=c02ec8 obtained_from=afefea -->
|  |  |
|---|---|
|  | ![Magical Frost Bow](wiki/assets/items/15004.png) |
| **Item id** | `15004` |
| **Kind** | Weapon (31) |
| **Classes** | Punisher |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCM_01.dds` cell 3 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 26 | WeaponBase row |

### Weapon base

WeaponBase row 26. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 140, `c3` = 10, `c4` = 750, `c5` = 340.

### Weapon skills

Weapon base 26. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5112-sharp-edges|Sharp Edges]]
2. [[wiki/skills/5113-potential-power|Potential Power]]
3. [[wiki/skills/5114-hail-of-arrows|Hail of Arrows]]
4. [[wiki/skills/5115-spinning-whirlwind|Spinning Whirlwind]]

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
| 907 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |
| 2202 | [[wiki/items/854-shining-passion\|Shining Passion]] × 3, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 50 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]] × 1
- Reward of quest [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 02, grade 3 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
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
