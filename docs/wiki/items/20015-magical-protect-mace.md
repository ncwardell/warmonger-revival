---
title: "Magical Protect Mace"
type: "item"
id: 20015
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 20015"]
name_key: "ItemName_20015"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 57
stats:
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "tier"}
options:
  - {"code": 200, "value": 57}
skills: [5351, 5352, 5353, 5354]
reinforce: 11
icon: {"file": "Weapon_PCD_01.dds", "index": 32}
obtained_from:
  - {"how": "craft", "recipe": 915}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=b43622 type=d36ca9 id=05fcaa sources=5b84c1 name_key=9113e0 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=9109c8 stats=b4cf00 options=7c8452 skills=0755e7 reinforce=17ba07 icon=0819a6 obtained_from=e0e36c -->
|  |  |
|---|---|
|  | ![Magical Protect Mace](wiki/assets/items/20015.png) |
| **Item id** | `20015` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-guardian\|Guardian weapons]] |
| **Classes** | [[wiki/classes/5-guardian\|Guardian]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 32 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +6 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +4 | × (tier × 15 + reinforce level) | 2 |
| Attack | +6 | × tier | 1 |
| Ability Power | +4 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 57 | WeaponBase row |

### Weapon base

WeaponBase row 57. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 160, `c3` = 40, `c4` = 200, `c5` = 380.

### Weapon skills

Weapon base 57. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5351-divine-recovery|Divine Recovery]]
2. [[wiki/skills/5352-protection-of-justice|Protection of Justice]]
3. [[wiki/skills/5353-destruction-of-light|Destruction of light]]
4. [[wiki/skills/5354-holy-shield|Holy Shield]]

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
| 915 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- Hero gacha pool 02, grade 2 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
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
