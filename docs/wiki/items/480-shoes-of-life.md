---
title: "Shoes of Life"
type: "item"
id: 480
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 480"]
name_key: "ItemName_404"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1100}
cost_pair:
  - {"currency": 2, "amount": 1100}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 1, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 40, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 20, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 12, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 6, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 80, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 10, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_10.png", "index": 15}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=5aa355 type=d36ca9 id=6153f0 sources=1b3363 name_key=c6bbef kind=c5b76d kind_name=a64daf classes=92d079 bind=883bf8 price=ec494a cost_pair=bf2342 rarity=356a19 stats=3b0362 reinforce=da4b92 icon=112072 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Shoes of Life](../assets/items/480.png) |
| **Item id** | `480` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,100 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_10.png` cell 15 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +1 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Health | +40 | × tier | 31 |
| Mana | +20 | × tier | 33 |
| Armor | +12 | flat | 6 |
| Magic Resist | +6 | flat | 7 |
| Mana | +80 | flat | 33 |
| Movement(%) | Movement +10% | flat | 105 |

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

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
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
