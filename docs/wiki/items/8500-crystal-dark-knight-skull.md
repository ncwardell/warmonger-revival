---
title: "Crystal : Dark knight Skull"
type: "item"
id: 8500
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8500"]
name_key: "ItemName_8500"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
period: 1500
weapon_base: 69
stats: []
options:
  - {"code": 200, "value": 69}
  - {"code": 201, "value": 51}
skills: [20004, 20005, 20000, 20006, 20007, 20008, 20012, 20009]
reinforce: 21
icon: {"file": "Items_20.png", "index": 40}
obtained_from:
  - {"how": "craft", "recipe": 1201}
  - {"how": "quest_reward", "quest": 44, "count": 1}
  - {"how": "quest_reward", "quest": 761, "count": 1}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=b00ded type=d36ca9 id=4b6e9e sources=f75ad8 name_key=283131 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a period=7841fb weapon_base=a72b20 stats=97d170 options=51d0ec skills=f2ce3f reinforce=472b07 icon=6f1b64 obtained_from=a41e2e -->
|  |  |
|---|---|
|  | ![Crystal : Dark knight Skull](wiki/assets/items/8500.png) |
| **Item id** | `8500` |
| **Kind** | Innocence (18) |
| **Category** | [[wiki/items/hero-items\|Innocence (hero) items]] |
| **Classes** | all |
| **Hero form** | [[wiki/heroes/51-dark-knight-skull-crystal\|Dark Knight Skull (Crystal)]] |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Period** | 1,500 = the crystal's durability (−5 per second transformed, WM 1107) |
| **Icon** | `ui/icons/Items_20.png` cell 40 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 69 | WeaponBase row |
| 201 | 51 | Innocence value? |

### Weapon base

WeaponBase row 69. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 2378, `c3` = 404, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 69. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20004-overcharge|Overcharge]]
2. [[wiki/skills/20005-cut|Cut]]
3. [[wiki/skills/20000-dark-knight-skull-passive|Dark Knight Skull Passive]]
4. [[wiki/skills/20006-heaven-and-earth|Heaven and Earth]]
5. [[wiki/skills/20007-sweep|Sweep]]
6. [[wiki/skills/20008-scream-of-the-dead|Scream of the Dead]]
7. [[wiki/skills/20012-aura-of-death|Aura of Death]]
8. [[wiki/skills/20009-tomb-of-the-dead|Tomb of the Dead]]

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
| 1201 | [[wiki/items/9000-piece-dark-knight-skull\|Piece : Dark knight Skull]] × 5, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/44-innocence-report|Innocence report]] × 1
- Reward of quest [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]] × 1
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
