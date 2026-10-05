---
title: "Shoes of Honor"
type: "item"
id: 491
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 491"]
name_key: "ItemName_419"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1300}
cost_pair:
  - {"currency": 2, "amount": 1300}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 11, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 43, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 23, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 300, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 26, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_07.png", "index": 53}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=48182a type=d36ca9 id=014a1a sources=f7dc94 name_key=9da94e kind=c5b76d kind_name=a64daf classes=92d079 bind=883bf8 price=78953d cost_pair=4dda47 rarity=356a19 stats=b88a7b reinforce=da4b92 icon=dbd5a1 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Shoes of Honor](../assets/items/491.png) |
| **Item id** | `491` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,300 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_07.png` cell 53 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Armor | +11 | × tier | 6 |
| Magic Resist | +11 | × tier | 7 |
| Armor | +43 | flat | 6 |
| Magic Resist | +23 | flat | 7 |
| Health | +300 | flat | 31 |
| Movement(%) | Movement +26% | flat | 105 |

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
