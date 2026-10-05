---
title: "Crystal : Guardian"
type: "item"
id: 8501
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8501"]
name_key: "ItemName_8501"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
period: 1500
weapon_base: 70
stats: []
options:
  - {"code": 200, "value": 70}
  - {"code": 201, "value": 52}
skills: [20063, 20062, 20060, 20055, 20056, 20054, 20059, 20058]
reinforce: 21
icon: {"file": "Items_20.png", "index": 41}
obtained_from:
  - {"how": "craft", "recipe": 1202}
  - {"how": "quest_reward", "quest": 44, "count": 1}
  - {"how": "quest_reward", "quest": 45, "count": 1}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=d7887d type=d36ca9 id=2c804a sources=10daac name_key=09e858 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a period=7841fb weapon_base=b7103c stats=97d170 options=47f832 skills=8f4f64 reinforce=472b07 icon=af683f obtained_from=579a97 -->
|  |  |
|---|---|
|  | ![Crystal : Guardian](wiki/assets/items/8501.png) |
| **Item id** | `8501` |
| **Kind** | Innocence (18) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Period** | 1500 (unit unknown; costume duration) |
| **Icon** | `ui/icons/Items_20.png` cell 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 70 | WeaponBase row |
| 201 | 52 | Innocence value? |

### Weapon base

WeaponBase row 70. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 2659, `c3` = 368, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 70. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20063-advent|Advent]]
2. [[wiki/skills/20062-maximized-efficiency|Maximized Efficiency]]
3. [[wiki/skills/20060-a-warrior-s-body|A Warrior's Body]]
4. [[wiki/skills/20055-critical-strike|Critical Strike]]
5. [[wiki/skills/20056-magical-zone|Magical Zone]]
6. [[wiki/skills/20054-magical-protection|Magical Protection]]
7. [[wiki/skills/20059-absorbing-magic|Absorbing Magic]]
8. [[wiki/skills/20058-overload|Overload]]

### Reinforcement

ItemSancMet row 21 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 5, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 5, [[wiki/items/621-orange-passion-fragments-d\|Orange Passion Fragments (D)]] × 2 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 5, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 5, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 2 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 6, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 6, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 3 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 8, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 8, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 3 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 8, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 8, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 4 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 8, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 8, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 4 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1202 | [[wiki/items/9001-piece-guardian\|Piece : Guardian]] × 5, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/44-innocence-report|Innocence report]] × 1
- Reward of quest [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]] × 1
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
