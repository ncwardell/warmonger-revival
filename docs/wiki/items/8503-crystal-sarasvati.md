---
title: "Crystal : Sarasvati"
type: "item"
id: 8503
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8503"]
name_key: "ItemName_8503"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 2
period: 1500
weapon_base: 72
stats: []
options:
  - {"code": 200, "value": 72}
  - {"code": 201, "value": 54}
skills: [20152, 20153, 20154, 20156, 20157, 20158, 20160, 20161]
reinforce: 23
icon: {"file": "Items_20.png", "index": 43}
obtained_from:
  - {"how": "craft", "recipe": 1204}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=9b5ace type=d36ca9 id=8308fe sources=a1004a name_key=695684 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=da4b92 period=7841fb weapon_base=c09763 stats=97d170 options=e78fe2 skills=f08e58 reinforce=d435a6 icon=0a3e2d obtained_from=8ff878 -->
|  |  |
|---|---|
|  | ![Crystal : Sarasvati](../assets/items/8503.png) |
| **Item id** | `8503` |
| **Kind** | Innocence (18) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 2 |
| **Period** | 1500 (unit unknown; costume duration) |
| **Icon** | `ui/icons/Items_20.png` cell 43 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 72 | WeaponBase row |
| 201 | 54 | Innocence value? |

### Weapon base

WeaponBase row 72. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 2047, `c3` = 755, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 72. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20152-aim-of-water|Aim of water]]
2. [[wiki/skills/20153-water-shield|Water shield]]
3. [[wiki/skills/20154-puddle|Puddle]]
4. [[wiki/skills/20156-blessing-of-water|Blessing of water]]
5. [[wiki/skills/20157-water-strike|Water strike]]
6. [[wiki/skills/20158-blow-of-water|Blow of water]]
7. [[wiki/skills/20160-goddess|Goddess]]
8. [[wiki/skills/20161-wave-of-water|Wave of water]]

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
| 1204 | [[wiki/items/9003-piece-sarasvati\|Piece : Sarasvati]] × 5, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 50 | 0 | 100 |

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
