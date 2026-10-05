---
title: "Helmet of Honor"
type: "item"
id: 489
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 489"]
name_key: "ItemName_417"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1500}
cost_pair:
  - {"currency": 2, "amount": 1500}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 4, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 11, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 43, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 23, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 105, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_08.png", "index": 39}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=eff2d4 type=d36ca9 id=343ae8 sources=189502 name_key=e966a6 kind=e1822d kind_name=c90f98 classes=92d079 bind=883bf8 price=e0f635 cost_pair=9ce603 rarity=356a19 stats=a0beb3 reinforce=da4b92 icon=a06501 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Helmet of Honor](wiki/assets/items/489.png) |
| **Item id** | `489` |
| **Kind** | Helmet (50) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_08.png` cell 39 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +4 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Armor | +11 | × tier | 6 |
| Magic Resist | +11 | × tier | 7 |
| Health | +15 | × tier | 31 |
| Armor | +43 | flat | 6 |
| Magic Resist | +23 | flat | 7 |
| Mana | +105 | flat | 33 |
| Movement(%) | Movement +13% | flat | 105 |

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

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
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
