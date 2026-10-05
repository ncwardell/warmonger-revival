---
title: "D-MaceShd-04"
type: "item"
id: 20018
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 20018"]
name_key: "ItemName_20018"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 60
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 60}
skills: []
reinforce: 11
icon: {"file": "Weapon_01.png", "index": 32}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=62bafe type=d36ca9 id=d29cdc sources=91cb03 name_key=31554f kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=e6c3dd stats=c45f77 options=fcb05a skills=97d170 reinforce=17ba07 icon=dc7c9a obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![D-MaceShd-04](wiki/assets/items/20018.png) |
| **Item id** | `20018` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_01.png` cell 32 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +10 | × (tier × 15 + reinforce level) | 2 |
| Attack | +10 | × tier | 1 |
| Ability Power | +10 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 60 | WeaponBase row |

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
