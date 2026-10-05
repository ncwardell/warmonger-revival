---
title: "Magical Blast Cannon"
type: "item"
id: 20011
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 20011"]
name_key: "ItemName_20011"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 53
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 53}
skills: [5116, 5117, 5118, 5119]
reinforce: 11
icon: {"file": "Weapon_PCD_01.dds", "index": 1}
obtained_from:
  - {"how": "craft", "recipe": 917}
  - {"how": "random_box", "box": 4}
  - {"how": "random_box", "box": 5}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=633e77 type=d36ca9 id=95e708 sources=b31669 name_key=342d4f kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=c5b76d stats=db11c4 options=b2a212 skills=0c05f7 reinforce=17ba07 icon=127859 obtained_from=035b83 -->
|  |  |
|---|---|
|  | ![Magical Blast Cannon](wiki/assets/items/20011.png) |
| **Item id** | `20011` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 1 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 53 | WeaponBase row |

### Weapon base

WeaponBase row 53. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 130, `c3` = 20, `c4` = 700, `c5` = 380.

### Weapon skills

Weapon base 53. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5116-quick-shot|Quick Shot]]
2. [[wiki/skills/5117-empowered-shot|Empowered Shot]]
3. [[wiki/skills/5118-heat-stomp|Heat Stomp]]
4. [[wiki/skills/5119-man-in-the-war|Man in the war]]

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
| 917 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 4 (RandomBox.cdb; odds are server side)
- In random box table row 5 (RandomBox.cdb; odds are server side)
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 02, grade 3 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)
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
