---
title: "Necklace of Rise"
type: "item"
id: 441
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 441"]
name_key: "ItemName_441"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 5, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 50, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 45, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_06.png", "index": 34}
obtained_from:
  - {"how": "craft", "recipe": 45}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=92d1fe type=d36ca9 id=5dd8b5 sources=e990ca name_key=a25427 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=250840 reinforce=356a19 icon=4b7b43 obtained_from=03a12d -->
|  |  |
|---|---|
|  | ![Necklace of Rise](wiki/assets/items/441.png) |
| **Item id** | `441` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_06.png` cell 34 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +5 | × (tier × 15 + reinforce level) | 7 |
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Health | +15 | × (tier × 15 + reinforce level) | 31 |
| Magic Resist | +10 | × tier | 7 |
| Armor | +10 | × tier | 6 |
| Health | +10 | × tier | 31 |
| Magic Resist | +50 | flat | 7 |
| Armor | +45 | flat | 6 |
| Health | +250 | flat | 31 |

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
| 45 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 25 | 375 | 100 |

### Where to get it

- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
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
