---
title: "Spirit Robe"
type: "item"
id: 486
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 486"]
name_key: "ItemName_414"
kind: 51
kind_name: "Armor"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 2000}
cost_pair:
  - {"currency": 2, "amount": 2000}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 5, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 12, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 12, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 44, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 25, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 380, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 11, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_02.png", "index": 53}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=caa06d type=d36ca9 id=6cc71d sources=10b7f9 name_key=211dc5 kind=b7eb6c kind_name=e687cb classes=92d079 bind=883bf8 price=05563f cost_pair=ce9832 rarity=356a19 stats=d7a711 reinforce=da4b92 icon=5f078d obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Spirit Robe](../assets/items/486.png) |
| **Item id** | `486` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 2,000 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_02.png` cell 53 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +5 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +11 | × tier | 6 |
| Magic Resist | +12 | × tier | 7 |
| Mana | +12 | × tier | 33 |
| Armor | +44 | flat | 6 |
| Magic Resist | +25 | flat | 7 |
| Health | +380 | flat | 31 |
| Movement(%) | Movement +11% | flat | 105 |

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

- [[gameplay/gear-stats|Gear stats (Crush Online artifacts)]]
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
