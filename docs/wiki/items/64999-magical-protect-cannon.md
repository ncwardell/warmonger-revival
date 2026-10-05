---
title: "Magical Protect Cannon"
type: "item"
id: 64999
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 64999"]
name_key: "ItemName_20021"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 90000}
cost_pair:
  - {"currency": 2, "amount": 90000}
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
  - {"code": 3, "stat": "Attack Speed", "value": 999999999, "scale": "flat"}
reinforce: 2
icon: {"file": "Weapon_PCD_01.dds", "index": 0}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=36f709 type=d36ca9 id=ddafcb sources=b07a24 name_key=147816 kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=316dcd cost_pair=d47b8d stats=d5f901 reinforce=da4b92 icon=8539c7 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Magical Protect Cannon](wiki/assets/items/64999.png) |
| **Item id** | `64999` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 90,000 Gold |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 0 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +10 | × (tier × 15 + reinforce level) | 2 |
| Attack | +10 | × tier | 1 |
| Ability Power | +10 | × tier | 2 |
| Attack Speed | +999999999 | flat | 3 |

### Reinforcement

ItemSancMet row 2 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 4 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 4 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 6 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 10 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 15 |

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
