---
title: "Bracelet of Rise"
type: "item"
id: 443
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 443"]
name_key: "ItemName_443"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 5, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 50, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 45, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 140, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_06.png", "index": 33}
obtained_from:
  - {"how": "craft", "recipe": 47}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=b0ad12 type=d36ca9 id=ac3e7b sources=e90d38 name_key=fe3c2d kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=29acd3 reinforce=356a19 icon=993a60 obtained_from=e85ec2 -->
|  |  |
|---|---|
|  | ![Bracelet of Rise](wiki/assets/items/443.png) |
| **Item id** | `443` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_06.png` cell 33 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Armor | +5 | × (tier × 15 + reinforce level) | 6 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Magic Resist | +10 | × tier | 7 |
| Armor | +10 | × tier | 6 |
| Mana | +10 | × tier | 33 |
| Magic Resist | +50 | flat | 7 |
| Armor | +45 | flat | 6 |
| Mana | +140 | flat | 33 |

### Reinforcement

ItemSancMet row 1 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 47 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 23 | 345 | 100 |

### Where to get it

- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

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
