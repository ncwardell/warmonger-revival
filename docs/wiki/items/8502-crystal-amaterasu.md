---
title: "Crystal : Amaterasu"
type: "item"
id: 8502
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8502"]
name_key: "ItemName_8502"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 2
period: 1500
weapon_base: 71
stats: []
options:
  - {"code": 200, "value": 71}
  - {"code": 201, "value": 53}
skills: [20102, 20103, 20104, 20105, 20106, 20107, 20108, 20109]
reinforce: 23
icon: {"file": "Items_20.png", "index": 42}
obtained_from:
  - {"how": "craft", "recipe": 1203}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=2280ab type=d36ca9 id=b8b946 sources=b50265 name_key=a03000 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=da4b92 period=7841fb weapon_base=d02560 stats=97d170 options=f4649e skills=7f6b3b reinforce=d435a6 icon=1059c1 obtained_from=f822f6 -->
|  |  |
|---|---|
|  | ![Crystal : Amaterasu](wiki/assets/items/8502.png) |
| **Item id** | `8502` |
| **Kind** | Innocence (18) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 2 |
| **Period** | 1500 (unit unknown; costume duration) |
| **Icon** | `ui/icons/Items_20.png` cell 42 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 71 | WeaponBase row |
| 201 | 53 | Innocence value? |

### Weapon base

WeaponBase row 71. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 396, `c3` = 2122, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 71. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20102-explosion|Explosion]]
2. [[wiki/skills/20103-snow-of-the-sun|Snow of the Sun]]
3. [[wiki/skills/20104-two-suns-kra-tura|Two suns (Kra, Tura)]]
4. [[wiki/skills/20105-a-warm-flame|A warm flame]]
5. [[wiki/skills/20106-flame-pillar|Flame pillar]]
6. [[wiki/skills/20107-the-source-of-the-sun|The source of the sun]]
7. [[wiki/skills/20108-shield-of-the-sun|Shield of the Sun]]
8. [[wiki/skills/20109-the-flame-of-the-sun|The Flame of the Sun]]

### Reinforcement

ItemSancMet row 23 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20, [[wiki/items/621-orange-passion-fragments-d\|Orange Passion Fragments (D)]] × 8 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 8 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 25, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 25, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 10 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 32, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 32, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 32, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 32, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 15 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 32, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 32, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 15 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1203 | [[wiki/items/9002-piece-amaterasu\|Piece : Amaterasu]] × 5, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 50 | 0 | 100 |

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
