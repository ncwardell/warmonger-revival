---
title: "Bracelet of Courage"
type: "item"
id: 471
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 471"]
name_key: "ItemName_439"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1300}
cost_pair:
  - {"currency": 2, "amount": 1300}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 3, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 4, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 60, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 40, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 140, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_06.png", "index": 32}
obtained_from:
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=259d86 type=d36ca9 id=5e5ad0 sources=10b330 name_key=a2a240 kind=54ceb9 kind_name=c2576a classes=92d079 bind=883bf8 price=78953d cost_pair=4dda47 rarity=356a19 stats=ab108e reinforce=da4b92 icon=9dfbbc obtained_from=7a497e -->
|  |  |
|---|---|
|  | ![Bracelet of Courage](wiki/assets/items/471.png) |
| **Item id** | `471` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,300 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_06.png` cell 32 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +3 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +4 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +11 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Mana | +10 | × tier | 33 |
| Armor | +60 | flat | 6 |
| Magic Resist | +40 | flat | 7 |
| Mana | +140 | flat | 33 |
| Mana Regeneration | +2 | flat | 34 |

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

- Hero gacha pool 01, grade 2 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
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
