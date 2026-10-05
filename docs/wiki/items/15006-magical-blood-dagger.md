---
title: "Magical Blood Dagger"
type: "item"
id: 15006
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 15006"]
name_key: "ItemName_15006"
kind: 31
kind_name: "Weapon"
classes: ["Punisher"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 28
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 28}
skills: [5055, 5056, 5057, 5058]
reinforce: 11
icon: {"file": "Weapon_PCM_01.dds", "index": 17}
obtained_from:
  - {"how": "craft", "recipe": 909}
  - {"how": "random_box", "box": 5}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=6bf6b5 type=d36ca9 id=d2e6b6 sources=3b0139 name_key=018d34 kind=632667 kind_name=631b4f classes=51f98f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=0a57cb stats=db11c4 options=384aa5 skills=2e2ec0 reinforce=17ba07 icon=65a2ea obtained_from=69594f -->
|  |  |
|---|---|
|  | ![Magical Blood Dagger](wiki/assets/items/15006.png) |
| **Item id** | `15006` |
| **Kind** | Weapon (31) |
| **Category** | [[wiki/items/weapons-punisher\|Punisher weapons]] |
| **Classes** | [[wiki/classes/4-punisher\|Punisher]] |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCM_01.dds` cell 17 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 28 | WeaponBase row |

### Weapon base

WeaponBase row 28. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 120, `c3` = 30, `c4` = 200, `c5` = 380.

### Weapon skills

Weapon base 28. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5055-bloody-revenge|Bloody Revenge]]
2. [[wiki/skills/5056-wild-threat|Wild Threat]]
3. [[wiki/skills/5057-running-wild|Running Wild]]
4. [[wiki/skills/5058-feast-of-blood|Feast of Blood]]

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
| 909 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 5 (RandomBox.cdb; odds are server side)
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
