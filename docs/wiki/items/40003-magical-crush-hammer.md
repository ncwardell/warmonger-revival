---
title: "Magical Crush Hammer"
type: "item"
id: 40003
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 40003"]
name_key: "ItemName_40003"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 67
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 67}
skills: [5294, 5295, 5296, 5297]
reinforce: 11
icon: {"file": "Weapon_PCD_01.dds", "index": 19}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=7fd242 type=d36ca9 id=417968 sources=141df0 name_key=3355c6 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=4d89d2 stats=db11c4 options=b4e925 skills=eb5c34 reinforce=17ba07 icon=e32f4e obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Magical Crush Hammer](wiki/assets/items/40003.png) |
| **Item id** | `40003` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 19 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 67 | WeaponBase row |

### Weapon base

WeaponBase row 67. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 80, `c3` = 70, `c4` = 200, `c5` = 340.

### Weapon skills

Weapon base 67. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5294-crushing-blow|Crushing Blow]]
2. [[wiki/skills/5295-head-butt|Head Butt]]
3. [[wiki/skills/5296-howl-of-victory|Howl of Victory]]
4. [[wiki/skills/5297-unyielding-will|Unyielding Will]]

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

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
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
