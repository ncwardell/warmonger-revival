---
title: "Necklace of Mediation"
type: "item"
id: 453
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 453"]
name_key: "ItemName_421"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1500}
cost_pair:
  - {"currency": 2, "amount": 1500}
rarity: 1
stats:
  - {"code": 2, "stat": "Ability Power", "value": 5, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 7, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 7, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 16, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 77, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 135, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 125, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_08.png", "index": 56}
obtained_from:
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=623426 type=d36ca9 id=4ac2bb sources=751631 name_key=63e5f0 kind=80e28a kind_name=7b4b74 classes=92d079 bind=883bf8 price=e0f635 cost_pair=9ce603 rarity=356a19 stats=4f4432 reinforce=da4b92 icon=46fa1a obtained_from=7a497e -->
|  |  |
|---|---|
|  | ![Necklace of Mediation](wiki/assets/items/453.png) |
| **Item id** | `453` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_08.png` cell 56 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +5 | × (tier × 15 + reinforce level) | 2 |
| Mana | +7 | × (tier × 15 + reinforce level) | 33 |
| Health | +7 | × (tier × 15 + reinforce level) | 31 |
| Ability Power | +16 | × tier | 2 |
| Mana | +10 | × tier | 33 |
| Ability Power | +77 | flat | 2 |
| Mana | +135 | flat | 33 |
| Health | +125 | flat | 31 |
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
