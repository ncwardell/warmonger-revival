---
title: "Belt of Transcendency"
type: "item"
id: 458
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 458"]
name_key: "ItemName_426"
kind: 55
kind_name: "Belt"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 2000}
cost_pair:
  - {"currency": 2, "amount": 2000}
rarity: 1
stats:
  - {"code": 2, "stat": "Ability Power", "value": 3, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 11, "scale": "tier"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 15, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 16, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 200, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_08.png", "index": 61}
obtained_from:
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=a50bd0 type=d36ca9 id=06be19 sources=0ddbbb name_key=cd99bc kind=8effee kind_name=ddf027 classes=92d079 bind=883bf8 price=05563f cost_pair=ce9832 rarity=356a19 stats=32701a reinforce=da4b92 icon=3849bb obtained_from=7a497e -->
|  |  |
|---|---|
|  | ![Belt of Transcendency](wiki/assets/items/458.png) |
| **Item id** | `458` |
| **Kind** | Belt (55) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 2,000 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_08.png` cell 61 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +3 | × (tier × 15 + reinforce level) | 2 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Mana Regeneration | +1 | × (tier × 15 + reinforce level) | 34 |
| Ability Power | +11 | × tier | 2 |
| Mana Regeneration | +1 | × tier | 34 |
| Mana | +15 | × tier | 33 |
| Ability Power | +16 | flat | 2 |
| Mana | +200 | flat | 33 |
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
