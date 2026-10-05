---
title: "Tempest Fisher"
type: "item"
id: 8007
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 8007"]
name_key: "ItemName_8007"
kind: 18
kind_name: "Innocence"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
weapon_base: 76
stats: []
options:
  - {"code": 200, "value": 76}
  - {"code": 201, "value": 8}
skills: [20302, 20303, 20305, 20306, 20307, 20308, 20309, 20310]
reinforce: 21
icon: {"file": "Items_20.png", "index": 20}
obtained_from:
  - {"how": "craft", "recipe": 1508}
  - {"how": "gacha", "pool": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=c1779d type=d36ca9 id=e60228 sources=357d0e name_key=3c63b4 kind=9e6a55 kind_name=83b4bf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a weapon_base=d54ad0 stats=97d170 options=5d7a1d skills=56f33f reinforce=472b07 icon=ebd420 obtained_from=36c228 -->
|  |  |
|---|---|
|  | ![Tempest Fisher](wiki/assets/items/8007.png) |
| **Item id** | `8007` |
| **Kind** | Innocence (18) |
| **Category** | [[wiki/items/hero-items\|Innocence (hero) items]] |
| **Classes** | all |
| **Hero form** | [[wiki/heroes/8-tempest-fisher\|Tempest Fisher]] |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_20.png` cell 20 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 76 | WeaponBase row |
| 201 | 8 | Innocence value? |

### Weapon base

WeaponBase row 76. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 340, `c3` = 1920, `c4` = 750, `c5` = 300.

### Weapon skills

Weapon base 76. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/20302-water-of-deceleration|Water of deceleration]]
2. [[wiki/skills/20303-water-column|Water column]]
3. [[wiki/skills/20305-fin-of-fisher|Fin of Fisher]]
4. [[wiki/skills/20306-tsunami|Tsunami]]
5. [[wiki/skills/20307-fisher-s-protection|Fisher's Protection]]
6. [[wiki/skills/20308-earthquake|Earthquake]]
7. [[wiki/skills/20309-divine|Divine]]
8. [[wiki/skills/20310-fisher-s-cries|Fisher's cries]]

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
| 1508 | [[wiki/items/9007-piece-tempest-fisher\|Piece : Tempest Fisher]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 200 | 0 | 100 |

### Where to get it

- Hero gacha pool 03, grade 1 (Gacha_03.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/sources|Sources and gaps]]
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
