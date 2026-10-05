---
title: "Crystal : Morion"
type: "item"
id: 8505
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8505"]
name_key: "ItemName_8505"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
period: 1500
weapon_base: 74
stats: []
options:
  - {"code": 200, "value": 74}
  - {"code": 201, "value": 56}
skills: [19951, 19956, 19953, 19954, 19958, 19959, 19960, 19961]
reinforce: 22
icon: {"file": "Items_20.png", "index": 45}
obtained_from:
  - {"how": "craft", "recipe": 1206}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=7fa250 type=d36ca9 id=3578d2 sources=83d47d name_key=690599 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 period=7841fb weapon_base=1f1362 stats=97d170 options=3ade5a skills=b09239 reinforce=12c6fc icon=208e98 obtained_from=90ce3f -->
|  |  |
|---|---|
|  | ![Crystal : Morion](wiki/assets/items/8505.png) |
| **Item id** | `8505` |
| **Kind** | Innocence (18) |
| **Category** | [[wiki/items/hero-items\|Innocence (hero) items]] |
| **Classes** | all |
| **Hero form** | [[wiki/heroes/56-morion-crystal\|Morion (Crystal)]] |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Period** | 1,500 = the crystal's durability (−5 per second transformed, WM 1107) |
| **Icon** | `ui/icons/Items_20.png` cell 45 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 74 | WeaponBase row |
| 201 | 56 | Innocence value? |

### Weapon base

WeaponBase row 74. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 2465, `c3` = 378, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 74. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/19951-fiery-anger|Fiery Anger]]
2. [[wiki/skills/19956-flame-armor|Flame armor]]
3. [[wiki/skills/19953-fury-of-fire|Fury of fire]]
4. [[wiki/skills/19954-flame-area|Flame area]]
5. [[wiki/skills/19958-push|Push]]
6. [[wiki/skills/19959-flame-wave|Flame wave]]
7. [[wiki/skills/19960-two-flames|Two Flames]]
8. [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]]

### Reinforcement

ItemSancMet row 22 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10, [[wiki/items/621-orange-passion-fragments-d\|Orange Passion Fragments (D)]] × 4 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 4 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 12, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 12, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 6 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 16, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 16, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 6 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 16, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 16, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 8 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 16, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 16, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 8 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1206 | [[wiki/items/9005-piece-morion\|Piece : Morion]] × 5, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 50 | 0 | 100 |

### Where to get it

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
